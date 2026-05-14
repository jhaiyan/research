# Authoritative Data Sources Configuration

This file defines the **seed data sources** and **runtime crawl strategy** for the `llm-coding-agents-comparison` skill.

Seed sources are handpicked for authority, reliability, influence, and popularity.
Additional sources are discovered dynamically at runtime via multi-layer crawling.

---

## Tier 1 Seed Sources (Always Fetch on Every Run)

### LLM General Benchmarks

| Source | URL | Purpose |
| :----- | :-- | :------ |
| LMSYS Chatbot Arena | https://lmarena.ai | Widest human-preference LLM ranking leaderboard |
| Artificial Analysis | https://artificialanalysis.ai/models | Speed, quality, and price comparison across all major models |
| HuggingFace Open LLM Leaderboard | https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard | Authoritative open-model evaluation |

### Coding-Specific Benchmarks

| Source | URL | Purpose |
| :----- | :-- | :------ |
| SWE-bench | https://www.swebench.com | Most authoritative coding agent benchmark (software engineering tasks) |
| Aider Leaderboard | https://aider.chat/docs/leaderboards/ | Coding-specific LLM ranking with detailed benchmark scores |
| Papers With Code — HumanEval | https://paperswithcode.com/sota/code-generation-on-humaneval | SOTA tracking for code generation |

### Discovery and News

| Source | URL | Purpose |
| :----- | :-- | :------ |
| Hacker News | https://news.ycombinator.com | Developer community; fastest signal for new tools and model discussions |
| Artificial Analysis Blog | https://artificialanalysis.ai/blog | In-depth model analysis articles |

---

## Runtime Source Discovery Strategy (Crawl)

After fetching seed sources, use the following strategy to dynamically discover additional authoritative sources.

### Crawl Parameters

| Parameter | Value | Description |
| :-------- | :---- | :---------- |
| Max depth | 9 hops | From any seed source, follow links up to 9 levels deep |
| Time filter | Last 3 years | Only include pages published or last updated within 3 years |
| Breadth limit | 3 links/page | Follow at most the 3 highest-scoring outbound links per page |
| Total page cap | 30 pages | Stop crawling after visiting 30 pages total across all layers |

### Link Relevance Scoring (Determines Which Links to Follow)

Score each candidate link and skip those with score < 2:

| Condition | Score |
| :-------- | ----: |
| Domain is a known authoritative site (arxiv.org, github.com, huggingface.co, paperswithcode.com, etc.) | +1 |
| URL contains keywords: llm, model, benchmark, coding, agent, comparison, leaderboard, eval | +1 |
| Page title mentions specific model names or benchmark names | +1 |
| Published or last updated within the last 6 months | +2 |
| Domain is .edu or a research institution | +1 |

### Crawl Termination Conditions

Stop crawling when ANY of the following is met:

- Max depth reached (9 hops)
- Total pages visited exceeds 30
- No unvisited links with score ≥ 2 remain in the current layer

### Discovery Search Queries (Run in Parallel with Crawl)

Run these searches simultaneously while crawling. Fetch the top 2 most relevant result pages per query.

```text
new LLM benchmark leaderboard {YYYY}
AI coding agent comparison review {YYYY}
best programming LLM {YYYY} evaluation
SWE-bench new agent results {YYYY}
LLM evaluation site:arxiv.org {YYYY}
AI coding tool ranked {YYYY-MM}
大模型 编程能力 排行 {YYYY}
coding assistant benchmark {YYYY-MM}
```
