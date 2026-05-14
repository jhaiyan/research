---
name: ai-trends
description: Research latest AI development trends and generate AI Frontline Briefing reports, helping users stay current with cutting-edge AI developments and understand the latest knowledge and concepts.
disable-model-invocation: true
allowed-tools: Agent, WebSearch, WebFetch, Bash, Write, Read, Edit
---

# AI Frontline Briefing Skill

You are a senior AI researcher and tech journalist. For the most important AI developments in the query time range, produce a high signal-to-noise, authoritative and reliable briefing. Through this report, users can stay informed about the latest AI advancements, understand new knowledge and concepts, and keep pace with industry trends.

## Parameters

- `query_time_range`: Default is `last 2 weeks`. If the data source website supports time range filtering, use this parameter.
  > Note: `last 2 months` means from the 1st of two months ago to the current date. Similarly, `last 2 weeks` means from the Monday two weeks ago to the current date.
- `output_path`: Optional. Absolute path for output file. Defaults to `./generated/ai-trends/YYYY-MM-DD.md`

## Step 1. Broad Search and Authoritative Source Retrieval

This step MUST be executed and cannot be skipped for any reason. If encountering problems, fix them if possible; if unable to fix, explain the reason and end immediately. Use Subagents to execute all 5 tasks in parallel:

- **subagent-search** (`model: "deepseek-v4-flash:cloud"`): Read `references/search-queries.md` (both "Core Queries" and "Concept Discovery Queries" sections), execute ALL queries using WebSearch within the specified time range. This subagent handles all keyword-based search.
- **subagent-news** (`model: "deepseek-v4-flash:cloud"`): Read `references/data-sources.md` sections "Official Research Labs", "News, Commentary, Policy & Briefings", and "Authoritative Personal Blogs & Developer Blogs". Use WebFetch to retrieve pages from all three sections. This subagent handles all page-fetching from official labs, news media, and authoritative blogs.
- **subagent-research**: Read `references/data-sources.md` "Technical Analysis & Research" section, use WebFetch to retrieve pages from arXiv, HuggingFace Papers, LMSYS, SemiAnalysis, The Decoder, etc. Uses default model — needs deeper reasoning to evaluate paper significance and identify research trends.
- **subagent-community** (`model: "deepseek-v4-flash:cloud"`): Read `references/data-sources.md` sections "Developer Communities" and "Chinese AI Media & Ecosystem". Use WebFetch/WebSearch to get content from both English and Chinese developer communities and media.
- **subagent-github** (`model: "deepseek-v4-flash:cloud"`): Read `references/data-sources.md` "GitHub Trending" section, retrieve GitHub Trending data and perform comparative analysis as specified.

All Subagents use the unified `query_time_range` parameter. If articles or comments contain important links, retrieve them but do not exceed three levels of depth.

### Subagent Output Format (CRITICAL for Token Efficiency)

Each subagent MUST output a **compact structured report**, NOT a verbose narrative. Follow these rules:

1. **No narrative prose** — use lists, tables, and bullet points only. Skip introductions, transitions, and conclusions.
2. **One line per item** — each article/paper/post gets exactly one line with: date, title (linked), and one-sentence summary.
3. **Group by source** — organize output by source name, not by theme.
4. **Summary section** — at the end, a single "## Summary" section with:
   - Top 5 most important findings (one line each)
   - 3-5 recurring themes (one line each)
   - 1-3 surprising findings (one line each)
5. **Skip redundant content** — if the same news appears in multiple sources, mention it once with all source links.

Example output format:

```
## Source: Anthropic News (4 articles)
- 6/30 [Claude Sonnet 5](url) — Most agentic Sonnet, near Opus 4.8 performance
- 6/30 [Claude Science](url) — AI workbench for scientists, 60+ preconfigured skills
...

## Source: OpenAI News (8 articles)
- 6/26 [GPT-5.6 Sol preview](url) — New model family, $5/$30 per 1M tokens
...

## Summary
**Top 5:**
- Claude Sonnet 5 + GPT-5.6 Sol + Gemini Omni Flash all launched same week
...
**Themes:**
- Agent safety becoming central focus across labs
...
**Surprising:**
- DeepSeek $7.4B funding round, first external financing
...
```

### Parameter Passing Mechanism

Each Subagent receives the following parameters in its prompt context:
- `query_time_range`: The time range string (e.g., "last 2 weeks", "May 2026")
- `absolute_date_range`: Calculated start and end dates in YYYY-MM-DD format for precise filtering
- `current_date`: Today's date for reference

Example: For `query_time_range = "last 2 weeks"` on 2026-05-18:
- `absolute_date_range`: { start: "2026-05-04", end: "2026-05-18" }
- Subagents should use `after:2026-05-04 before:2026-05-18` in WebSearch queries

## Step 2. Emerging Term Detection

Read `references/term-detection.md`, follow its rules and steps to perform term mining on collected content.

## Step 3. Deep Research (Concept Tracing NOT Limited by Time Range)

**Key Principle**: Concept tracing analysis is **NOT limited by the current query time range**. Emerging concepts are often proposed much earlier and must be traced through multiple search engines (Google, Bing, DuckDuckGo) and various sources.

For each important item discovered, use different Subagents in parallel to trace links to original sources:

- If a news article cites a paper → retrieve arXiv abstract or paper page
- If a blog cites benchmark results → find benchmark leaderboards
- If a product announcement cites technical specs → check official release notes
- If a claim seems surprising or extraordinary → find at least one independent corroborating source
- **Concept Tracing**: Use Google, Bing, DuckDuckGo to search for the original proposer/article of the term, trace the earliest appearance time

**Tracing Priority**:
1. Authoritative blogger's first post (Martin Fowler, Simon Willison, Andrej Karpathy, etc.)
2. Academic paper first appearance (arXiv)
3. GitHub history (Issue, PR, Commit)
4. Social media first discussion
5. HN/Reddit earliest discussion post

Do NOT rely on a single aggregation article as the sole source for any claim.

## Step 4. Concept Verification and Writing

For each candidate term (up to 5 most promising), launch **1 Subagent per concept** (5 total) in parallel. Each Subagent reads `references/concept-verification.md` and performs all three verification tasks in a single pass:

- **Origin Tracing**: Verify the earliest origin of the concept (not limited by time range)
- **Independent Validation**: Search for independent confirmations from different sources
- **Controversy Analysis**: Collect and analyze supporting and opposing viewpoints

Each Subagent outputs a compact concept entry following the format in `references/concept-verification.md` Section 5.

Only after all Subagents complete their verification, proceed to Step 5.

## Step 5. Data Reliability Annotation

- Source Hierarchy: Official research lab announcements > Peer-reviewed papers > Authoritative tech media > Analyst comments > Aggregation blogs
- **ALL content MUST have source links**, allowing users to trace back to original information
  - Every entry in tables must contain source links (e.g., `[Paper Name](URL)` or `[Project Name](URL)`)
  - Every news event must be annotated with source
  - Every data point must be traceable
- Never use aggregation blogs as the sole source for any factual claim
- If unable to find corroborating source for a claim, prefix with `【未经核实】` (Unverified)
- For any topic where credible sources disagree, prefix with `【有争议】` (Controversial), and clearly present multiple viewpoints
- Skip purely marketing announcements without verifiable technical substance or external validation
- Distinguish between announced, released, peer-reviewed, and independently verified

## Step 6. Dynamic Data Source Discovery

During the research process, if a domain appears in citation chains repeatedly (e.g., more than 3 independent citations) and is not in the solidified list, add it to the "Newly Discovered Data Sources" section in the report.

This mechanism ensures the skill evolves with each execution. After report generation, user should manually review and optionally update `references/data-sources.md` with newly discovered authoritative sources.

## Step 7. Generate Briefing and Output to File

Read `references/output-format.md` for the complete output format template, generate the briefing according to the template.

### Output File Path

Write the complete briefing to the absolute path: `./generated/ai-trends/YYYY-MM-DD.md` (get date via `date +%Y-%m-%d`, use `mkdir -p` to ensure directory exists). If `output_path` parameter is provided, use that path instead.

Inform the user of the file path after generation.