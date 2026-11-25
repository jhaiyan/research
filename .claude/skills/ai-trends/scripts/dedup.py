#!/usr/bin/env python3
"""去重与合并：把 candidates.jsonl 合并为统一候选池 deduped.jsonl。

合并规则：

1. 规范化 URL 完全一致的条目合并为一条，保留全部来源；
2. 标题归一化后与日期一致的条目合并为一条；
3. 来源层级取最优（A 优于 B 优于 C），并记录全部来源链接。

用法：

    python3 dedup.py --in candidates.jsonl --out deduped.jsonl --stats-out dedup-stats.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import unicodedata

PUNCTUATION = re.compile(r"[^\w一-鿿]+")
TIER_ORDER = {"A": 0, "B": 1, "C": 2}


def normalize_title(title: str) -> str:
    folded = unicodedata.normalize("NFKC", title or "").lower()
    return PUNCTUATION.sub("", folded)


def record_key(record: dict) -> str:
    canonical = record.get("canonical_url") or record.get("url") or ""
    if canonical:
        return "url:" + canonical
    return "title:" + normalize_title(record.get("title", "")) + "|" + str(record.get("published_at"))


def title_key(record: dict) -> str:
    if not record.get("published_at"):
        return ""
    return normalize_title(record.get("title", "")) + "|" + record["published_at"]


def merge(target: dict, incoming: dict) -> None:
    target["published_at"] = target.get("published_at") or incoming.get("published_at")
    if TIER_ORDER.get(incoming.get("source_tier", "C"), 2) < TIER_ORDER.get(target.get("source_tier", "C"), 2):
        target["source_tier"] = incoming.get("source_tier")
    sources = target.setdefault("sources", [])
    for source in incoming.get("sources", []):
        if source not in sources:
            sources.append(source)
    for key in ("discussion_url", "points", "comments", "summary", "repo", "period_stars", "period"):
        if key not in target and key in incoming:
            target[key] = incoming[key]


def main() -> int:
    parser = argparse.ArgumentParser(description="合并 ai-trends 候选条目")
    parser.add_argument("--in", dest="input", required=True)
    parser.add_argument("--out", dest="output", required=True)
    parser.add_argument("--stats-out", default="")
    args = parser.parse_args()

    records = []
    with open(args.input, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                records.append(json.loads(line))

    merged: dict[str, dict] = {}
    by_title: dict[str, str] = {}
    for record in records:
        enriched = dict(record)
        enriched.setdefault(
            "sources",
            [
                {
                    "url": record.get("url"),
                    "tier": record.get("source_tier"),
                    "source_id": record.get("source_id"),
                }
            ],
        )
        key = record_key(enriched)
        if key in merged:
            merge(merged[key], enriched)
            continue
        title_key_value = title_key(enriched)
        if title_key_value and title_key_value in by_title:
            existing = merged[by_title[title_key_value]]
            merge(existing, enriched)
            for source in enriched["sources"]:
                if source not in existing["sources"]:
                    existing["sources"].append(source)
            continue
        merged[key] = enriched
        if title_key_value:
            by_title[title_key_value] = key

    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as handle:
        for record in merged.values():
            record["id"] = hashlib.sha1(
                (record.get("canonical_url") or record.get("url") or record["title"]).encode("utf-8")
            ).hexdigest()[:16]
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    tier_counts: dict[str, int] = {}
    dated = 0
    for record in merged.values():
        tier_counts[record.get("source_tier", "C")] = tier_counts.get(record.get("source_tier", "C"), 0) + 1
        if record.get("published_at"):
            dated += 1

    stats = {
        "input_records": len(records),
        "merged_records": len(merged),
        "removed_duplicates": len(records) - len(merged),
        "with_date": dated,
        "without_date": len(merged) - dated,
        "tier_counts": tier_counts,
    }
    if args.stats_out:
        os.makedirs(os.path.dirname(os.path.abspath(args.stats_out)), exist_ok=True)
        with open(args.stats_out, "w", encoding="utf-8") as handle:
            json.dump(stats, handle, ensure_ascii=False, indent=2)
    print(json.dumps(stats, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
