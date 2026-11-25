#!/usr/bin/env python3
"""确定性采集：按 sources.json 抓取候选条目，输出 candidates.jsonl。

设计约束：

- 仅使用 Python 标准库，无需安装依赖；
- 已知来源直接抓取，不通过搜索引擎发现；
- 原始响应落盘缓存，重复执行优先命中缓存；
- 单请求超时、重试上限与同域熔断，避免无限等待；
- 采集结果只做“标题＋链接＋日期”的粗筛，重要性判断交给筛选代理。

用法：

    python3 collect.py --sources sources.json --since 2026-11-09 --until 2026-11-24 \
        --out generated/ai-trends/.work/2026-11-24/candidates.jsonl
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timezone

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

MONTHS = {
    name.lower(): index
    for index, name in enumerate(
        [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ],
        start=1,
    )
}

DATE_PATTERNS = (
    (re.compile(r"(\d{4})-(\d{1,2})-(\d{1,2})"), "ymd"),
    (re.compile(r"(\d{4})/(\d{1,2})/(\d{1,2})"), "ymd"),
    (re.compile(r"(\d{4})年(\d{1,2})月(\d{1,2})日"), "ymd"),
    (re.compile(r"([A-Z][a-z]{2,8})\.?\s+(\d{1,2}),?\s+(\d{4})"), "mdy"),
)

ANCHOR_PATTERN = re.compile(
    r"<a\b[^>]*href=[\"']([^\"'#][^\"']*)[\"'][^>]*>(.*?)</a>", re.S | re.I
)
TAG_PATTERN = re.compile(r"<[^>]+>")
SPACE_PATTERN = re.compile(r"\s+")


def strip_tags(fragment: str) -> str:
    return SPACE_PATTERN.sub(" ", TAG_PATTERN.sub(" ", fragment)).strip()


def canonical_url(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    host = parsed.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    query_pairs = [
        (key, value)
        for key, value in urllib.parse.parse_qsl(parsed.query)
        if not key.lower().startswith("utm_")
        and key.lower() not in {"ref", "source", "fbclid", "gclid", "s", "spm"}
    ]
    path = parsed.path.rstrip("/") or "/"
    return urllib.parse.urlunsplit(("https", host, path, urllib.parse.urlencode(query_pairs), ""))


def content_id(url: str) -> str:
    return hashlib.sha1(canonical_url(url).encode("utf-8")).hexdigest()[:16]


def find_date(text: str) -> str | None:
    for pattern, kind in DATE_PATTERNS:
        match = pattern.search(text)
        if not match:
            continue
        try:
            if kind == "ymd":
                year, month, day = (int(part) for part in match.groups())
            else:
                month = MONTHS.get(match.group(1).lower())
                if not month:
                    continue
                day, year = int(match.group(2)), int(match.group(3))
            return date(year, month, day).isoformat()
        except ValueError:
            continue
    return None


def curl_fetch(url: str, timeout: int):
    """用 curl 抓取。部分站点会拒绝 Python 的 TLS 指纹，curl 更接近真实浏览器。"""
    command = [
        "curl",
        "-sS",
        "-L",
        "--max-time",
        str(timeout),
        "-A",
        USER_AGENT,
        "-H",
        "Accept: text/html,application/xhtml+xml,application/json,application/atom+xml,*/*",
        "-w",
        "\n%{http_code}",
        url,
    ]
    try:
        completed = subprocess.run(
            command, capture_output=True, text=True, timeout=timeout + 5, check=False
        )
    except FileNotFoundError:
        return None, 0, "curl 不可用"
    except subprocess.TimeoutExpired:
        return None, 0, "curl 超时"
    if completed.returncode != 0:
        return None, 0, completed.stderr.strip()[:120] or f"curl 退出码 {completed.returncode}"
    body, _, status = completed.stdout.rpartition("\n")
    try:
        status_code = int(status.strip())
    except ValueError:
        status_code = 0
    if status_code >= 400:
        return None, status_code, f"HTTP {status_code}"
    return body, status_code, ""


def fetch(url: str, cache_dir: str, ttl_seconds: float, timeout: int, retries: int):
    """返回 (文本, 是否命中缓存, 错误信息)。"""
    cache_file = os.path.join(cache_dir, f"raw-{hashlib.sha1(url.encode()).hexdigest()}.cache")
    if os.path.exists(cache_file) and (time.time() - os.path.getmtime(cache_file)) < ttl_seconds:
        with open(cache_file, "r", encoding="utf-8") as handle:
            return handle.read(), True, ""

    last_error = ""
    for attempt in range(retries + 1):
        text, status, error = curl_fetch(url, timeout)
        if text is not None:
            os.makedirs(cache_dir, exist_ok=True)
            with open(cache_file, "w", encoding="utf-8") as handle:
                handle.write(text)
            return text, False, ""
        last_error = error
        if status in {400, 401, 403, 404, 410}:
            break
        try:
            request = urllib.request.Request(
                url,
                headers={
                    "User-Agent": USER_AGENT,
                    "Accept": "text/html,application/xhtml+xml,application/json,application/atom+xml,*/*",
                },
            )
            with urllib.request.urlopen(request, timeout=timeout) as response:
                text = response.read().decode("utf-8", "replace")
            os.makedirs(cache_dir, exist_ok=True)
            with open(cache_file, "w", encoding="utf-8") as handle:
                handle.write(text)
            return text, False, ""
        except urllib.error.HTTPError as error:
            last_error = f"HTTP {error.code}"
            if error.code in {400, 401, 403, 404, 410}:
                break
        except Exception as error:  # noqa: BLE001 - 采集阶段需要吞掉所有网络异常
            last_error = f"{type(error).__name__}: {error}"
        if attempt < retries:
            time.sleep(0.5)
    return None, False, last_error


def extract_index_items(html: str, base_url: str, max_items: int):
    items = []
    for match in ANCHOR_PATTERN.finditer(html):
        url = urllib.parse.urljoin(base_url, match.group(1))
        title = strip_tags(match.group(2))
        if len(title) < 8:
            continue
        window = strip_tags(html[match.end() : match.end() + 500])
        published = find_date(f"{title} {window}")
        items.append({"title": title, "url": url, "published_at": published})
        if len(items) >= max_items:
            break
    return items


def extract_hn_items(payload: str, max_items: int):
    hits = json.loads(payload).get("hits", [])
    items = []
    for hit in hits:
        title = hit.get("title") or hit.get("story_title")
        if not title:
            continue
        published = None
        created_at = hit.get("created_at")
        if created_at:
            published = datetime.fromisoformat(created_at.replace("Z", "+00:00")).date().isoformat()
        items.append(
            {
                "title": title,
                "url": hit.get("url") or f"https://news.ycombinator.com/item?id={hit.get('objectID')}",
                "published_at": published,
                "discussion_url": f"https://news.ycombinator.com/item?id={hit.get('objectID')}",
                "points": hit.get("points"),
                "comments": hit.get("num_comments"),
            }
        )
        if len(items) >= max_items:
            break
    return items


def extract_arxiv_items(payload: str, max_items: int):
    items = []
    entries = re.findall(r"<entry>(.*?)</entry>", payload, re.S)
    for entry in entries:
        title_match = re.search(r"<title>(.*?)</title>", entry, re.S)
        id_match = re.search(r"<id>(.*?)</id>", entry, re.S)
        published_match = re.search(r"<published>(.*?)</published>", entry, re.S)
        summary_match = re.search(r"<summary>(.*?)</summary>", entry, re.S)
        if not title_match or not id_match:
            continue
        published = None
        if published_match:
            published = datetime.fromisoformat(
                published_match.group(1).replace("Z", "+00:00")
            ).date().isoformat()
        items.append(
            {
                "title": SPACE_PATTERN.sub(" ", title_match.group(1)).strip(),
                "url": id_match.group(1).strip(),
                "published_at": published,
                "summary": SPACE_PATTERN.sub(" ", summary_match.group(1)).strip()[:600]
                if summary_match
                else "",
            }
        )
        if len(items) >= max_items:
            break
    return items


TRENDING_RESERVED_OWNERS = {
    "sponsors",
    "topics",
    "orgs",
    "collections",
    "users",
    "login",
    "signup",
    "features",
    "about",
    "pricing",
    "notifications",
    "market",
    "readme",
    "apps",
}


def extract_trending_items(html: str, base_url: str, max_items: int):
    items = []
    for block in re.split(r"<article", html)[1:]:
        repo = None
        heading_match = re.search(r'<h2[^>]*>\s*<a[^>]*href="/([^"]+)"', block, re.S)
        if heading_match:
            repo = heading_match.group(1).strip()
        else:
            for candidate in re.findall(r'href="/([\w.\-]+/[\w.\-]+)"', block):
                owner = candidate.split("/")[0]
                if owner.lower() in TRENDING_RESERVED_OWNERS:
                    continue
                repo = candidate
                break
        if not repo or repo.count("/") != 1:
            continue
        if repo.split("/")[0].lower() in TRENDING_RESERVED_OWNERS:
            continue
        plain = strip_tags(block)
        period_match = re.search(r"([\d,]+)\s+stars\s+(this week|this month)", plain)
        added = None
        period = None
        if period_match:
            added = int(period_match.group(1).replace(",", ""))
            period = period_match.group(2)
        totals_match = re.search(r"([\d,]+)\s+([\d,]+)\s+Built by", plain)
        stars_total = None
        forks = None
        if totals_match:
            stars_total = int(totals_match.group(1).replace(",", ""))
            forks = int(totals_match.group(2).replace(",", ""))
        items.append(
            {
                "title": repo,
                "url": urllib.parse.urljoin(base_url, f"/{repo}"),
                "published_at": None,
                "repo": repo,
                "stars_total": stars_total,
                "forks": forks,
                "period_stars": added,
                "period": period,
            }
        )
        if len(items) >= max_items:
            break
    return items


def build_request_url(source: dict, config: dict, since: date, until: date) -> str:
    kind = source["kind"]
    url = source["url"]
    if kind == "hn":
        start = int(datetime.combine(since, datetime.min.time(), tzinfo=timezone.utc).timestamp())
        end = int(datetime.combine(until, datetime.min.time(), tzinfo=timezone.utc).timestamp())
        filters = f"created_at_i>{start},created_at_i<{end},points>100"
        return f"{url}?tags=story&numericFilters={urllib.parse.quote(filters)}&hitsPerPage=100"
    if kind == "arxiv":
        category = config.get("arxiv_categories", {}).get(source["id"], "cat:cs.AI")
        query = f"({category}) AND submittedDate:[{since.strftime('%Y%m%d')}0000 TO {until.strftime('%Y%m%d')}2359]"
        return (
            f"{url}?search_query={urllib.parse.quote(query)}"
            f"&sortBy=submittedDate&sortOrder=descending&max_results={source.get('max_items', 30)}"
        )
    return url


def collect_source(source: dict, config: dict, args) -> dict:
    since = date.fromisoformat(args.since)
    until = date.fromisoformat(args.until)
    url = build_request_url(source, config, since, until)
    ttl_hours = config.get("cache_ttl_hours", {}).get("index", 12)
    ttl_seconds = ttl_hours * 3600 if source["kind"] == "index" else 3600
    timeout = args.timeout * 3 if source["kind"] == "arxiv" else args.timeout
    payload, cached, error = fetch(url, args.cache, ttl_seconds, timeout, args.retries)
    result = {
        "source_id": source["id"],
        "tier": source["tier"],
        "kind": source["kind"],
        "fetch_url": url,
        "from_cache": cached,
        "error": error,
        "items": [],
    }
    if payload is None:
        return result
    if source["kind"] == "index":
        result["items"] = extract_index_items(payload, url, source.get("max_items", 30))
    elif source["kind"] == "hn":
        result["items"] = extract_hn_items(payload, source.get("max_items", 60))
    elif source["kind"] == "arxiv":
        result["items"] = extract_arxiv_items(payload, source.get("max_items", 30))
    elif source["kind"] == "github-trending":
        result["items"] = extract_trending_items(payload, url, source.get("max_items", 30))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="采集 ai-trends 候选条目")
    parser.add_argument("--sources", default="sources.json")
    parser.add_argument("--since", required=True)
    parser.add_argument("--until", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--stats-out", default="")
    parser.add_argument("--cache", default="generated/ai-trends/.cache")
    parser.add_argument("--timeout", type=int, default=15)
    parser.add_argument("--retries", type=int, default=1)
    parser.add_argument("--jobs", type=int, default=6)
    parser.add_argument("--include-undated", action="store_true")
    parser.add_argument("--tiers", default="A,B", help="本次启用的来源层级")
    args = parser.parse_args()

    with open(args.sources, "r", encoding="utf-8") as handle:
        config = json.load(handle)

    enabled_tiers = {tier.strip() for tier in args.tiers.split(",") if tier.strip()}
    sources = [source for source in config["sources"] if source["tier"] in enabled_tiers]

    since = date.fromisoformat(args.since)
    until = date.fromisoformat(args.until)

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
        futures = {
            pool.submit(collect_source, source, config, args): source for source in sources
        }
        for future in concurrent.futures.as_completed(futures):
            try:
                results.append(future.result())
            except Exception as error:  # noqa: BLE001
                source = futures[future]
                results.append(
                    {
                        "source_id": source["id"],
                        "tier": source["tier"],
                        "kind": source["kind"],
                        "fetch_url": source["url"],
                        "from_cache": False,
                        "error": f"{type(error).__name__}: {error}",
                        "items": [],
                    }
                )

    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    written = 0
    in_window = 0
    undated = 0
    with open(args.out, "w", encoding="utf-8") as handle:
        for result in sorted(results, key=lambda item: item["source_id"]):
            for item in result["items"]:
                record = {
                    "id": content_id(item["url"]),
                    "title": item["title"],
                    "url": item["url"],
                    "canonical_url": canonical_url(item["url"]),
                    "published_at": item.get("published_at"),
                    "source_id": result["source_id"],
                    "source_tier": result["tier"],
                    "kind": result["kind"],
                    "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                    "from_cache": result["from_cache"],
                }
                for extra in (
                    "discussion_url",
                    "points",
                    "comments",
                    "summary",
                    "repo",
                    "stars_total",
                    "forks",
                    "period_stars",
                    "period",
                ):
                    if extra in item:
                        record[extra] = item[extra]
                written += 1
                if record["published_at"] is None and result["kind"] == "github-trending":
                    record["published_at"] = until.isoformat()
                    record["date_semantics"] = "snapshot"
                if record["published_at"] is None:
                    undated += 1
                    # A 级来源的索引页常不暴露日期，保留条目交给筛选代理判断，避免漏掉重大公告
                    if not args.include_undated and result["tier"] != "A":
                        continue
                    record["date_confidence"] = "unknown"
                else:
                    published = date.fromisoformat(record["published_at"])
                    if published < since or published > until:
                        continue
                in_window += 1
                handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    stats = {
        "sources_attempted": len(sources),
        "sources_failed": sum(1 for result in results if result["error"]),
        "sources": [
            {
                "source_id": result["source_id"],
                "tier": result["tier"],
                "items": len(result["items"]),
                "from_cache": result["from_cache"],
                "error": result["error"],
            }
            for result in sorted(results, key=lambda item: item["source_id"])
        ],
        "records_written": written,
        "records_in_window": in_window,
        "records_without_date": undated,
    }
    if args.stats_out:
        os.makedirs(os.path.dirname(os.path.abspath(args.stats_out)), exist_ok=True)
        with open(args.stats_out, "w", encoding="utf-8") as handle:
            json.dump(stats, handle, ensure_ascii=False, indent=2)
    print(json.dumps({key: value for key, value in stats.items() if key != "sources"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
