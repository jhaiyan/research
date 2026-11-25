#!/usr/bin/env python3
"""证据库管理：校验、追加与统计 evidence.jsonl。

证据对象是简报的唯一事实来源：报告中每条数据都必须能对应一条证据记录，
每条证据记录都必须带来源链接与核验状态。

子命令：

    python3 evidence.py add --file evidence.jsonl --data entry.json
    python3 evidence.py validate --file evidence.jsonl
    python3 evidence.py summary --file evidence.jsonl

校验规则与 schemas/evidence.schema.json 保持一致：必填字段、枚举取值与
最小来源数量；未通过校验的记录不会被写入。
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from urllib.parse import urlsplit

REQUIRED_FIELDS = (
    "id",
    "title",
    "url",
    "published_at",
    "source_tier",
    "verification_status",
    "claims",
    "sources",
)

TIERS = {"A", "B", "C"}
STATUSES = {
    "primary_verified",
    "corroborated",
    "unverified",
    "disputed",
    "refuted",
}


def validate(entry: dict) -> list[str]:
    problems = []
    for field in REQUIRED_FIELDS:
        if field not in entry:
            problems.append(f"缺少字段：{field}")
    if not isinstance(entry.get("claims"), list) or not entry.get("claims"):
        problems.append("claims 必须是非空数组")
    if not isinstance(entry.get("sources"), list) or not entry.get("sources"):
        problems.append("sources 必须是非空数组")
    if entry.get("source_tier") not in TIERS:
        problems.append("source_tier 必须是 A、B 或 C")
    if entry.get("verification_status") not in STATUSES:
        problems.append(f"verification_status 必须是 {sorted(STATUSES)} 之一")
    for claim in entry.get("claims", []) or []:
        if not isinstance(claim, dict) or not claim.get("text") or not claim.get("source_url"):
            problems.append("claims 中每项都需要 text 与 source_url")
        else:
            parsed = urlsplit(claim["source_url"])
            if parsed.scheme not in {"http", "https"}:
                problems.append(f"claim 来源链接无效：{claim['source_url']}")
    for source in entry.get("sources", []) or []:
        if not isinstance(source, dict) or not source.get("url") or source.get("tier") not in TIERS:
            problems.append("sources 中每项都需要 url 与合法 tier")
    status = entry.get("verification_status")
    independent = [
        source
        for source in (entry.get("sources") or [])
        if source.get("role") == "independent"
    ]
    if status == "corroborated" and not independent:
        problems.append("corroborated 至少需要一个 role 为 independent 的来源")
    if status == "primary_verified" and not any(
        source.get("role") == "primary" for source in (entry.get("sources") or [])
    ):
        problems.append("primary_verified 至少需要一个 role 为 primary 的来源")
    return problems


def read_entries(path: str) -> list[dict]:
    entries = []
    if not os.path.exists(path):
        return entries
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                entries.append(json.loads(line))
    return entries


def main() -> int:
    parser = argparse.ArgumentParser(description="管理 ai-trends 证据库")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="追加一条证据")
    add_parser.add_argument("--file", required=True)
    add_parser.add_argument("--data", default="", help="单条 JSON 文件；缺省时从标准输入读取")

    validate_parser = subparsers.add_parser("validate", help="校验证据文件")
    validate_parser.add_argument("--file", required=True)

    summary_parser = subparsers.add_parser("summary", help="输出证据库统计")
    summary_parser.add_argument("--file", required=True)

    args = parser.parse_args()

    if args.command == "add":
        raw = (
            open(args.data, "r", encoding="utf-8").read()
            if args.data
            else sys.stdin.read()
        )
        entry = json.loads(raw)
        problems = validate(entry)
        if problems:
            for problem in problems:
                print(f"INVALID {problem}")
            return 1
        entry.setdefault(
            "recorded_at", datetime.now(timezone.utc).isoformat(timespec="seconds")
        )
        os.makedirs(os.path.dirname(os.path.abspath(args.file)), exist_ok=True)
        with open(args.file, "a", encoding="utf-8") as handle:
            handle.write(json.dumps(entry, ensure_ascii=False) + "\n")
        print(f"OK {entry['id']}")
        return 0

    entries = read_entries(args.file)
    if args.command == "validate":
        invalid = 0
        for entry in entries:
            problems = validate(entry)
            if problems:
                invalid += 1
                print(f"INVALID {entry.get('id', 'unknown')}：{'; '.join(problems)}")
        print(json.dumps({"total": len(entries), "invalid": invalid}, ensure_ascii=False))
        return 1 if invalid else 0

    status_counts: dict[str, int] = {}
    tier_counts: dict[str, int] = {}
    domains = set()
    for entry in entries:
        status = entry.get("verification_status", "unknown")
        status_counts[status] = status_counts.get(status, 0) + 1
        tier = entry.get("source_tier", "unknown")
        tier_counts[tier] = tier_counts.get(tier, 0) + 1
        for source in entry.get("sources", []) or []:
            host = urlsplit(source.get("url", "")).netloc
            if host:
                domains.add(host)
    print(
        json.dumps(
            {
                "total": len(entries),
                "by_status": status_counts,
                "by_tier": tier_counts,
                "unique_domains": len(domains),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
