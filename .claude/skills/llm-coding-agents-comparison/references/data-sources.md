# Authoritative Data Sources Configuration

This file defines the **seed data sources** and **authority ratings** for the `llm-coding-agents-comparison` skill.

Seed sources are handpicked for authority, reliability, influence, and popularity. Each source is tagged with an **authority tier (T1–T4)** used by the synthesis layer to weight conflicting evidence.

> **Top-20 rule**: Every leaderboard, benchmark, and aggregator in this list contributes only its **Top 20** entries to the report. When querying any of these sources, take the top 20 — do not paginate or scroll further. The deep multi-layer crawl that earlier versions of this skill performed (9 hops, 30 pages) has been removed; the diminishing returns did not justify the cost.

---

## Authority Tier System

Each data source is assigned an authority tier based on five dimensions:

1. **机构背景** — official / academic / independent third-party / commercial aggregator
2. **方法论透明度** — evaluation methodology publicly documented and reproducible
3. **数据覆盖面** — coverage breadth (how many models) and freshness (update cadence)
4. **独立验证能力** — whether raw data / scripts are available for independent verification
5. **社区认可度** — how widely cited by model vendors, technical media, and researchers

| Tier | 权威度 | Typical Profile | Weight (合成阶段) |
| :--: | :----- | :-------------- | ----------------: |
| **T1** | 极高 | 方法论透明、官方或学术背景、被业内广泛引用、可独立验证 | 3.0× |
| **T2** | 高 | 方法论透明、社区认可度高、独立第三方 | 2.0× |
| **T3** | 中 | 有方法论但覆盖面有限或更新频率低，或以聚合他人数据为主 | 1.0× |
| **T4** | 低 | 方法论不透明、商业聚合为主、数据时效不明 | 0.5× |

> Phase 3.3 的差异解决规则使用此表：同等时效下，Tier 越高的源数据权重越大。具体见 `SKILL.md` Step 3.3。

---

## Tier 1 Seed Sources (Always Fetch on Every Run)

### LLM General Benchmarks

| Source | URL | Authority | Purpose |
| :----- | :-- | :-------: | :------ |
| Artificial Analysis — Models | https://artificialanalysis.ai/models | **T1** | 独立 AI 研究机构，速度/质量/价格对比，方法论公开 |
| Artificial Analysis — Coding Agents | https://artificialanalysis.ai/agents/coding-agents | **T1** | AA 的子页面，专门评估 coding agents |
| HuggingFace Open LLM Leaderboard | https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard | **T1** | 业内领先的开源 AI 平台，聚合多项公开基准 |
| LMSYS Arena 镜像 — HuggingFace Space | https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard | **T1** | LMSYS Arena 的 HF 镜像，lmarena.ai 不可达时的替代 |
| Vellum LLM Leaderboard | https://www.vellum.ai/llm-leaderboard | **T1** | 跨模型综合排行，独立维护 |
| LMSYS Arena 镜像 — Presenc AI | https://presenc.ai/research/chatbot-arena-elo-leaderboard-june-2026 | **T2** | Arena Elo 月度快照，lmarena.ai 不可达时的替代 |

### Coding-Specific Benchmarks

| Source | URL | Authority | Purpose |
| :----- | :-- | :-------: | :------ |
| SWE-bench | https://www.swebench.com/index.html | **T1** | 软件工程任务的学术金标准 |
| Aider Leaderboard | https://aider.chat/docs/leaderboards/ | **T1** | 开源项目官方，多语言代码基准 |
| Terminal Bench | https://www.tbench.ai/ | **T1** | Stanford + Harbor + Laude Institute 联合发布的终端任务基准 |
| Program Bench | https://programbench.com/ | **T1** | Meta Superintelligence Labs + Stanford + Harvard 联合发布 |
| Steel.dev SWE-bench Verified | https://leaderboard.steel.dev/leaderboards/swe-bench-verified | **T1** | SWE-bench Verified 的 Vals.ai 验证实现 |

### Discovery and News

| Source | URL | Authority | Purpose |
| :----- | :-- | :-------: | :------ |
| Hacker News | https://news.ycombinator.com | **T1** | Y Combinator 知名技术社区，新工具和新模型讨论的最快信号源 |
| Artificial Analysis Blog | https://artificialanalysis.ai/blog | **T1** | 独立 AI 研究机构的深度模型分析文章 |

### Supplementary Aggregators (T2/T3 — use with care)

| Source | URL | Authority | Purpose |
| :----- | :-- | :-------: | :------ |
| BenchLM — Coding | https://benchlm.ai/coding | **T2** | 独立基准聚合平台，权重方法学公开 |
| LLM Stats — Best AI for Web Development | https://llm-stats.com/best-ai-for-web-development | **T2** | 独立 LLM 基准平台，方法论公开且支持复现 |
| ModelGrep Leaderboard | https://modelgrep.com/leaderboard | **T2** | 独立排名平台，依赖 Artificial Analysis Intelligence Index 等外部源 |
| LLM Podium Leaderboard | https://llmpodium.com/leaderboard | **T3** | 多源聚合平台；Podium Score 含方法学说明但本身是二次聚合 |

> **注意**：T2/T3 源主要用于发现新模型、补充覆盖和交叉验证。任何关键评分主张（如「某模型 SWE-bench 第一」）必须由至少一个 T1 源交叉确认，否则在报告中标记 `[待验证]`。

---

## Runtime Source Discovery Strategy

The original multi-layer crawl (9 hops, 30 pages, 3-year filter) has been **removed**. Runtime discovery is now a two-step process:

### Step 1: Tier-1 Verification

The Discovery Subagent performs **one** WebFetch per Tier-1 seed URL listed above to confirm it is accessible and record what data it contains. No follow-up crawling, no breadth-first expansion.

### Step 2: Targeted Discovery Searches

The Discovery Subagent runs a small number of WebSearches to surface new manufacturers and products:

```text
new LLM benchmark leaderboard {YYYY}
AI coding agent comparison review {YYYY}
best programming LLM {YYYY} evaluation
大模型 编程能力 排行 {YYYY}
coding assistant benchmark {YYYY-MM}
```

For each search, take the **Top 5 result pages** — never paginate further.

### Top-20 Cap on Every Source

When a Tier-1 source (leaderboard, benchmark, news feed) provides a ranked list, the Discovery Subagent takes the **Top 20** entries from that source. The same cap applies to research subagents when they read leaderboards: take the top 20, do not scroll.

### Runtime-Discovered Sources

Any source discovered at runtime via WebSearch MUST be assigned an authority tier before being added to `sources.md`. If a discovered source cannot be reliably tier-rated, default to T3 and note the reason in `sources.md`.
