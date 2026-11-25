#!/usr/bin/env python3
"""链接可用性检查：读取 Markdown 中的链接，批量验证状态并缓存结果。

判定规则：

- 2xx 与 3xx 视为有效；
- 404、410、DNS 失败与超时视为失败；
- 403 与 429 视为反爬阻断，单独报告但不判失败；
- 命中缓存且未过期的结果不再重复请求。

用法：

    python3 check_links.py --file generated/ai-trends/2026-11-24.md \
        --cache generated/ai-trends/.cache --out link-check.json
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import re
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
LINK_PATTERN = re.compile(r"\]\((https?://[^)\s]+)(?:\s+\"[^\"]*\")?\)")


def fetch_status(url: str, timeout: int) -> tuple[int, str]:
    """优先使用 curl：部分站点会拒绝 Python 的 TLS 指纹，导致误判为不可达。"""
    command = [
        "curl",
        "-sS",
        "-L",
        "-o",
        os.devnull,
        "--max-time",
        str(timeout),
        "-A",
        USER_AGENT,
        "-w",
        "%{http_code}",
        url,
    ]
    try:
        completed = subprocess.run(
            command, capture_output=True, text=True, timeout=timeout + 5, check=False
        )
        if completed.returncode == 0:
            status = completed.stdout.strip()
            if status.isdigit():
                return int(status), ""
    except FileNotFoundError:
        pass
    except subprocess.TimeoutExpired:
        pass
    except Exception as error:  # noqa: BLE001
        pass

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/json,*/*",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            response.read(2048)
            return response.status, ""
    except urllib.error.HTTPError as error:
        return error.code, ""
    except Exception as error:  # noqa: BLE001
        return 0, f"{type(error).__name__}: {error}"


def load_cache(path: str) -> dict:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    return {}


def main() -> int:
    parser = argparse.ArgumentParser(description="检查 Markdown 链接可用性")
    parser.add_argument("--file", required=True)
    parser.add_argument("--cache", default="generated/ai-trends/.cache")
    parser.add_argument("--out", default="")
    parser.add_argument("--timeout", type=int, default=15)
    parser.add_argument("--jobs", type=int, default=8)
    parser.add_argument("--ttl-hours", type=int, default=24)
    args = parser.parse_args()

    with open(args.file, "r", encoding="utf-8") as handle:
        content = handle.read()

    urls = sorted({urllib.parse.unquote(match.group(1)) for match in LINK_PATTERN.finditer(content)})
    os.makedirs(args.cache, exist_ok=True)
    cache_path = os.path.join(args.cache, "link-status.json")
    cache = load_cache(cache_path)
    ttl_seconds = args.ttl_hours * 3600

    results = {}
    to_check = []
    now = time.time()
    for url in urls:
        entry = cache.get(url)
        if entry and (now - entry.get("checked_at", 0)) < ttl_seconds:
            results[url] = entry
        else:
            to_check.append(url)

    if to_check:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
            futures = {pool.submit(fetch_status, url, args.timeout): url for url in to_check}
            for future in concurrent.futures.as_completed(futures):
                url = futures[future]
                status, error = future.result()
                entry = {
                    "status": status,
                    "error": error,
                    "checked_at": now,
                }
                results[url] = entry
                if status > 0:
                    cache[url] = entry

        # 瞬时失败（状态 0）多为并发下的连接问题，串行重试一次再判定
        for _ in range(2):
            pending = [url for url, entry in results.items() if entry.get("status", 0) == 0]
            if not pending:
                break
            for url in pending:
                time.sleep(0.5)
                status, error = fetch_status(url, args.timeout)
                entry = {"status": status, "error": error, "checked_at": time.time()}
                results[url] = entry
                if status > 0:
                    cache[url] = entry

    with open(cache_path, "w", encoding="utf-8") as handle:
        json.dump(cache, handle, ensure_ascii=False, indent=2)

    failed = []
    blocked = []
    for url, entry in results.items():
        status = entry.get("status", 0)
        if status == 0 or status in {404, 410}:
            failed.append({"url": url, **entry})
        elif status in {403, 429}:
            blocked.append({"url": url, **entry})
        elif status >= 400:
            failed.append({"url": url, **entry})

    report = {
        "file": args.file,
        "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "total_urls": len(urls),
        "valid": len(urls) - len(failed) - len(blocked),
        "failed": failed,
        "blocked": blocked,
    }
    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as handle:
            json.dump(report, handle, ensure_ascii=False, indent=2)
    print(json.dumps({key: value for key, value in report.items() if key not in {"failed", "blocked"}}, ensure_ascii=False))
    for item in failed:
        print(f"FAIL {item.get('status')} {item['url']}")
    for item in blocked:
        print(f"BLOCKED {item.get('status')} {item['url']}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
