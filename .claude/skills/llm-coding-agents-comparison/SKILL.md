---
name: llm-coding-agents-comparison
description: |
  Explore and compare the latest programming LLMs and AI coding agents, generating comprehensive comparison reports with cross-verified data from multiple authoritative sources. Trigger this skill when the user asks for "LLM comparison", "coding agent comparison", "AI coding tools comparison", "programming LLM benchmark", "Claude vs GPT vs Gemini comparison", "best AI coding assistant", or wants a comprehensive survey of current LLM and coding agent landscape.
disable-model-invocation: true
allowed-tools: Agent, WebSearch, WebFetch, Bash, Write, Read, Edit
---

# LLM and Coding Agents Comparison

Produce a comprehensive, cross-verified comparison report of current programming-capable LLMs and AI coding agents. Data is gathered through parallel subagent research and synthesized with rigorous cross-validation.

## Architecture Principles

- **Data sources**: Hardcoded Tier-1 seeds in `references/data-sources.md` + runtime multi-layer crawl discovery (up to 9 layers, 3-year filter, max 30 pages)
- **Manufacturers**: Base list in `references/manufacturers.md` + runtime discovery; the file is updated in-place when new manufacturers are found
- **LLM names**: Never hardcoded — discovered at runtime by the Target Discovery Subagent
- **Coding Agents**: Never hardcoded — discovered at runtime by the Target Discovery Subagent

## Parameters

- `output_path`: Optional. Absolute path for output file. Defaults to `./comparison/coding-agents/coding-agents-{YYYYMMDD}.md` where `{YYYYMMDD}` is obtained from the shell.

## Execution Flow Overview

```
Phase 0: Preparation (parallel reads)
  ├── Get exact date from shell
  ├── Read references/data-sources.md
  ├── Read references/manufacturers.md
  └── Read references/llm-prompt.md and references/agent-prompt.md

Phase 0.5: Discovery (2 parallel specialized subagents)
  ├── Source Discovery Subagent
  │   ├── Fetch all Tier 1 seeds from data-sources.md
  │   ├── Crawl outward: up to 9 layers, 3-year filter, top-3 links/page, max 30 pages
  │   ├── Run parallel discovery searches
  │   └── Output → .temp/llm-agent-comparison/sources.md
  └── Target Discovery Subagent
      ├── Read manufacturers.md (base list)
      ├── For each manufacturer, search for their latest LLMs and coding agents
      ├── Run broad discovery searches to find new manufacturers and products
      ├── Update references/manufacturers.md if new manufacturers found
      ├── Output → .temp/llm-agent-comparison/llm-targets.md
      └── Output → .temp/llm-agent-comparison/agent-targets.md

Phase 1 + Phase 2 (PARALLEL): Research (10 subagents)
  ├── Phase 1: 5 LLM subagents — research every entry in llm-targets.md
  └── Phase 2: 5 Agent subagents — research every entry in agent-targets.md
  (All 10 subagents also read sources.md for enriched source access)

Phase 3: Cross-Validation and Synthesis

Phase 4: Final Report Generation
```

---

## Phase 0: Preparation

### Step 0.1: Get Exact Date from Shell

Run the following commands. **Never guess or infer the date — always use the shell output.**

```bash
date +"%Y%m%d"          # → {YYYYMMDD}  e.g. 20260519
date +"%Y%m%d%H%M%S"    # → {YYYYMMDDHHmmss}  e.g. 20260519143022
date +"%Y年%m月%d日"    # → {YYYY年MM月DD日}  e.g. 2026年05月19日
date +"%Y"              # → {YYYY}  e.g. 2026
date +"%Y-%m"           # → {YYYY-MM}  e.g. 2026-05
```

Store all five values. Inject them verbatim into every subagent prompt.

### Step 0.2: Read Reference Files and Create Temp Directory

Read all four reference files in parallel:
- `.claude/skills/llm-coding-agents-comparison/references/data-sources.md`
- `.claude/skills/llm-coding-agents-comparison/references/manufacturers.md`
- `.claude/skills/llm-coding-agents-comparison/references/llm-prompt.md`
- `.claude/skills/llm-coding-agents-comparison/references/agent-prompt.md`

Also run: `mkdir -p .temp/llm-agent-comparison/`

---

## Phase 0.5: Discovery (2 Parallel Specialized Subagents)

**CRITICAL**: Launch BOTH subagents simultaneously in a single message. Do not wait for one before starting the other.

### Source Discovery Subagent

This subagent builds an enriched, verified source list by crawling outward from authoritative seed sources.

**Subagent Prompt:**

``````markdown
You are the Source Discovery Subagent for a LLM/Coding Agent comparison report.

**Today's date: {YYYY年MM月DD日}**
**Current year-month: {YYYY-MM}**

## Your Mission

Compile an enriched, verified list of authoritative data sources about LLMs and AI coding agents.
Start from seed sources and crawl outward layer by layer.

## Step 1: Read the Crawl Configuration

Read `.claude/skills/llm-coding-agents-comparison/references/data-sources.md`.
This file contains all Tier 1 seed URLs, crawl parameters, link relevance scoring rules, and discovery search queries.

## Step 2: Fetch All Tier 1 Seeds

Fetch every Tier 1 seed URL via WebFetch. Record what useful data (model rankings, benchmark scores, recent articles) you found on each page.

## Step 3: Multi-Layer Source Crawl

Use the parameters from `data-sources.md`:

- **Max depth**: 9 hops from any seed
- **Time filter**: Only pages published or last updated within the last 3 years
- **Breadth limit**: At each page, follow at most 3 highest-scoring outbound links
- **Total page cap**: Stop after 30 pages fetched across all layers

For each fetched page:

1. Extract outbound links
2. Score each link using the relevance scoring rules in `data-sources.md`
3. Skip links with score < 2
4. Follow the top-3 highest-scoring, unvisited links
5. Repeat until max depth or page cap reached

## Step 4: Run Parallel Discovery Searches

Run all discovery search queries listed in `data-sources.md` (substitute `{YYYY}` and `{YYYY-MM}` with the actual values).
For each search, WebFetch the top 2 most relevant result pages.

## Step 5: Write Output

Save to `.temp/llm-agent-comparison/sources.md`:

```markdown
# Discovered Sources

Generated: {YYYY年MM月DD日}
Total pages fetched: {N}
Total unique sources: {N}

## Tier 1 Seeds (All Fetched)

| Source | URL | Key Data Found |
| :----- | :-- | :------------- |
| {name} | {url} | {e.g. "Top 20 models by Elo score as of {date}"} |

## Crawl-Discovered Sources (Layers 1–9)

| Source | URL | Layer | Key Data Found |
| :----- | :-- | :---: | :------------- |
| {name} | {url} | {N} | {what data it contains} |

## Search-Discovered Sources

| Source | URL | Key Data Found |
| :----- | :-- | :------------- |
| {name} | {url} | {what data it contains} |
```

Only include sources you actually fetched and confirmed accessible. Flag potentially outdated pages with `[可能过时]`.
``````

---

### Target Discovery Subagent

This subagent discovers which LLMs and Coding Agents exist RIGHT NOW by searching the web — no hardcoded names anywhere.

**Subagent Prompt:**

``````markdown
You are the Target Discovery Subagent for a LLM/Coding Agent comparison report.

**Today's date: {YYYY年MM月DD日}**
**Current year-month: {YYYY-MM}**

## Your Mission

Discover what LLMs and AI coding agents exist today by searching the web dynamically. Produce:
1. An updated `manufacturers.md` (if new manufacturers are found)
2. `llm-targets.md` — the definitive research target list for Phase 1
3. `agent-targets.md` — the definitive research target list for Phase 2

## Step 1: Read the Base Manufacturer List

Read `.claude/skills/llm-coding-agents-comparison/references/manufacturers.md`.
Treat it as a starting point, not a complete or current list.

## Step 2: Discover New Manufacturers

Run these searches to find manufacturers that may have emerged since the file was last updated:

1. `new AI company LLM model released {YYYY}`
2. `new AI startup model {YYYY} funding announcement`
3. `AI 大模型 新公司 新模型 {YYYY}`
4. `emerging LLM provider {YYYY} benchmark`
5. `new AI coding assistant company {YYYY}`
6. `AI model company Series A B funding {YYYY}`

For each new manufacturer found: verify they have an actual released, publicly accessible model (not just a press release or funding announcement). Do NOT add companies with no live model.

## Step 3: Discover Current LLMs

For **each manufacturer** in the list (base + newly discovered), search for their latest models:

```text
[manufacturer name] latest model release {YYYY}
[manufacturer name] [model family] newest version {YYYY}
[manufacturer name] LLM API available {YYYY-MM}
```

For each manufacturer: find the specific model name(s) and version(s) currently available; confirm the model is actively maintained (not deprecated or replaced); include only the latest 1–2 generations.

Also run broad discovery searches to catch any models or manufacturers you might have missed:

```text
top LLM benchmark leaderboard {YYYY-MM}
LMSYS Arena new models {YYYY}
best coding LLM {YYYY} comparison
new LLM release {YYYY} programming
HuggingFace leaderboard top models {YYYY}
大模型 最新 排行 {YYYY}
```

Compile a deduplicated list of all currently active LLMs found. For each, record: manufacturer, model name and version, approximate release date, and official page URL (if found; verify it's model-specific via WebFetch before including).

## Step 4: Discover Current Coding Agents

Run these discovery searches:

```text
best AI coding agent {YYYY} review
AI coding assistant comparison {YYYY}
SWE-bench agent leaderboard {YYYY}
new AI coding tool released {YYYY}
AI IDE extension coding assistant {YYYY}
AI 编程助手 最新 对比 {YYYY}
coding agent review developer {YYYY-MM}
VS Code AI extension popular {YYYY}
```

For each coding agent found: verify it is actively maintained (last update within 12 months — check GitHub release dates or official blog). Exclude discontinued, rebranded-beyond-recognition, or vaporware tools.

Compile a deduplicated list of all currently active coding agents.

## Step 5: Write Output Files

### File 1: Update manufacturers.md (only if new manufacturers found)

If you discovered manufacturers not in `.claude/skills/llm-coding-agents-comparison/references/manufacturers.md`, append new rows to the appropriate tables. Keep all existing content intact. Update the "Last Updated" line at the top.

### File 2: LLM Target List

Write `.temp/llm-agent-comparison/llm-targets.md`:

```markdown
# LLM Research Targets

Generated: {YYYY年MM月DD日}
Source: Target Discovery Subagent

This list was compiled dynamically from current web sources — NOT from hardcoded training data.
Phase 1 research subagents MUST research EVERY model listed here.

## Target LLMs

| # | Manufacturer | Model Name | Version / Release Date | Official Page | Notes |
| - | :----------- | :--------- | :--------------------- | :------------ | :---- |
| 1 | ... | ... | ... | ... | ... |

## Discovery Summary

- Manufacturers searched: {N}
- New manufacturers found (not in base list): {list or "none"}
- Total LLM entries: {N}
- Models excluded and why: {list or "none"}
- Searches run: {N} queries, {N} pages fetched
```

### File 3: Coding Agent Target List

Write `.temp/llm-agent-comparison/agent-targets.md`:

```markdown
# Coding Agent Research Targets

Generated: {YYYY年MM月DD日}
Source: Target Discovery Subagent

This list was compiled dynamically from current web sources — NOT from hardcoded training data.
Phase 2 research subagents MUST research EVERY agent listed here.

## Target Agents

| # | Manufacturer | Agent Name | Primary Models (initial) | Official Page | Notes |
| - | :----------- | :--------- | :----------------------- | :------------ | :---- |
| 1 | ... | ... | ... | ... | ... |

## Discovery Summary

- New agents found not previously known: {list or "none"}
- Total agent entries: {N}
- Agents excluded and why: {list or "none"}
- Searches run: {N} queries, {N} pages fetched
```

## Self-Assessment Before Saving

- [ ] Did I search every manufacturer in the base list?
- [ ] Did I run enough broad searches to surface new manufacturers?
- [ ] Is every LLM entry a currently active model (not deprecated or superseded)?
- [ ] Does the agent list include all actively maintained tools, including less-popular open-source ones?
- [ ] Run one final broad search to confirm nothing significant was missed.
``````

---

### Wait for Both Phase 0.5 Subagents

Wait for both subagents to complete. Verify these files exist:

- `.temp/llm-agent-comparison/sources.md`
- `.temp/llm-agent-comparison/llm-targets.md`
- `.temp/llm-agent-comparison/agent-targets.md`

If any file is missing, retry the failed subagent once. If it fails again, proceed with available data and note the gap in the final report.

---

## Phase 1 & Phase 2: Parallel Research (10 Subagents)

**CRITICAL**: Launch all 10 subagents as **background agents** simultaneously in a single message. Record each task ID returned from the Agent tool call — you will need these IDs for the timeout/retry mechanism below.

Record the group start time immediately after launch:

```bash
date +%s    # → {group_start_unix}  (Unix timestamp, for elapsed-time math)
```

### Phase 1: LLM Research (5 Subagents)

Launch 5 independent `general-purpose` subagents with **IDENTICAL** prompts (substitute `{SubagentNumber}`):

``````markdown
You are LLM Research Subagent #{SubagentNumber} of 5.

- **Today's date: {YYYY年MM月DD日}**
- **Current year-month: {YYYY-MM}**

Read the full research guide from `.claude/skills/llm-coding-agents-comparison/references/llm-prompt.md` and follow its instructions exactly.

Your target list is in `.temp/llm-agent-comparison/llm-targets.md` — compiled dynamically from current web sources.
Your enriched source list is in `.temp/llm-agent-comparison/sources.md` — use these as primary research starting points.

Research EVERY model in the target list. Use `{YYYY}` and `{YYYY-MM}` in all search queries — never infer the date.

Save your complete findings to `.temp/llm-agent-comparison/llm-research-{YYYYMMDDHHmmss}-{SubagentNumber}.md`.

CRITICAL RULES:
- Do NOT use Baidu or low-credibility sources
- Verify every hyperlink via WebFetch — model-specific pages only, not manufacturer homepages; omit any link that redirects to a homepage or fails
- Insert a space between Chinese characters and adjacent English letters/numbers in ALL output
- Every score must be backed by specific evidence from at least 3 sources
- Complete the MANDATORY SELF-ASSESSMENT in the research guide before saving
- **EXACT VERSION NUMBERS**: Always use the specific, full version string (e.g., `GPT-4.5`, `Claude Sonnet 4.6`, `Gemini 2.5 Pro`). NEVER use a vague family name like `GPT-5` when a specific point-release exists. If you cannot confirm the exact version, search harder before falling back.
- **NO LAZY N/A**: Never mark a field as N/A (or `-`) without first exhausting every search angle — official docs, API pages, arXiv papers, benchmark sites, press releases, GitHub repos, community discussions. Mark as `-` ONLY if the data is genuinely absent after diligent multi-source searching. Dig hard. No excuses.
- **EXCLUDE UNRELEASED / KEY-DATA-MISSING MODELS**: Skip any model that (a) has not been publicly released or is not accessible via API/public access, OR (b) lacks publicly verifiable data for at least 3 of these key fields: context size, a coding benchmark score, and cost. Document every excluded model with a reason in the Raw Data section.
``````

### Phase 2: Coding Agent Research (5 Subagents)

Launch 5 independent `general-purpose` subagents with **IDENTICAL** prompts (substitute `{SubagentNumber}`):

``````markdown
You are Coding Agent Research Subagent #{SubagentNumber} of 5.

- **Today's date: {YYYY年MM月DD日}**
- **Current year-month: {YYYY-MM}**

Read the full research guide from `.claude/skills/llm-coding-agents-comparison/references/agent-prompt.md` and follow its instructions exactly.

Your target list is in `.temp/llm-agent-comparison/agent-targets.md` — compiled dynamically from current web sources.
Your enriched source list is in `.temp/llm-agent-comparison/sources.md` — use these as primary research starting points.

Research EVERY agent in the target list. Use `{YYYY}` and `{YYYY-MM}` in all search queries — never infer the date.

Save your complete findings to `.temp/llm-agent-comparison/agent-research-{YYYYMMDDHHmmss}-{SubagentNumber}.md`.

CRITICAL RULES:

- Do NOT use Baidu or low-credibility sources
- Verify every hyperlink via WebFetch — agent-specific pages only, not manufacturer homepages; omit any link that redirects to a homepage or fails
- Insert a space between Chinese characters and adjacent English letters/numbers in ALL output
- Scores must be fair for ALL agents including less-popular ones (Aider, Continue.dev, Codex CLI, Cody, etc.)
- Every score must be backed by specific evidence from at least 3 sources
- Complete the MANDATORY SELF-ASSESSMENT in the research guide before saving
- **EXACT VERSION NUMBERS**: Use the precise, full product name and version where known (e.g., `Claude Code 1.x`, `Cursor 0.45`). NEVER use vague identifiers when a specific version is publicly documented.
- **NO LAZY N/A**: Never mark a field as N/A (or `-`) without first exhausting every search angle — official docs, GitHub repos, SWE-bench results, pricing pages, changelog, community discussions. Mark as `-` ONLY if the data is genuinely absent after diligent multi-source searching. Dig hard. No excuses.
- **EXCLUDE UNRELEASED / KEY-DATA-MISSING AGENTS**: Skip any agent that (a) has not been publicly released or is not accessible, OR (b) lacks publicly verifiable data for at least 3 key capability dimensions after exhaustive searching. Document every excluded agent with a reason in the Raw Data section.
``````

### Monitoring and Timeout/Retry Mechanism

Apply the following logic **independently** to each group (LLM group = subagents 1–5; Agent group = subagents 1–5). Both groups run concurrently.

#### Monitoring Loop

Every 5 minutes after launch, run these checks in parallel:

```bash
date +%s                                   # current Unix timestamp
ls .temp/llm-agent-comparison/             # which output files exist
```

Use `TaskList` to confirm which background tasks are still running vs. completed.

#### Phase A — Waiting for 3 completions

A subagent is **complete** when its output file exists in `.temp/llm-agent-comparison/`:
- LLM subagents: `llm-research-*-{N}.md`
- Agent subagents: `agent-research-*-{N}.md`

Once **3 subagents in a group** have completed, record:
- `t3 = current Unix timestamp`
- `t_elapsed = t3 - group_start_unix`  (seconds it took to get 3 completions)

#### Phase B — 10-minute countdown per remaining subagent

For each remaining (still-running) subagent in the group, start a personal 10-minute countdown from `t3`.

Check every 5 minutes. If a subagent has **not** completed within 10 minutes of `t3`:

1. Find its task ID (recorded at launch, or via `TaskList`)
2. Call `TaskStop(task_id)` to terminate it
3. Launch one **replacement subagent** (same prompt, same `{SubagentNumber}`) as a background agent, with this **urgent time-limit notice prepended to the prompt**:

   > **URGENT TIME LIMIT**: You are a replacement for a subagent that timed out. You MUST write your output file within **{t_elapsed} seconds** from now — this is a hard deadline. Prioritize breadth: cover every target with sufficient evidence, but do not over-invest in any single item. Failing to write the output file is not acceptable.

4. Record: `replacement_task_id` and `replacement_start = current Unix timestamp`

#### Phase C — Replacement timeout

Check each replacement subagent every 5 minutes. If `current_time - replacement_start > t_elapsed` and it has **not** completed:

1. Call `TaskStop(replacement_task_id)` to terminate it
2. Mark this slot as **failed** — do NOT retry again
3. Note the gap in the final report and proceed with available data

#### Hard Stop

Once all slots in a group have either (a) completed, (b) been replaced and completed, or (c) been stopped after replacement failure, the group is **done**. Proceed to Phase 3 once both groups are done.

---

## Phase 3: Cross-Validation and Synthesis

### Step 3.1: Read All Subagent Reports

Read all generated files from `.temp/llm-agent-comparison/`:

- `llm-research-{timestamp}-1.md`, `-2.md`, `-3.md`
- `agent-research-{timestamp}-1.md`, `-2.md`, `-3.md`

### Step 3.2: Comparative Analysis

For each model/agent, compare the 5 subagent reports side-by-side:

1. **Consensus**: All or majority agree → high confidence
2. **Partial Consensus**: 3 of 5 agree → medium confidence, verify
3. **Discrepancy**: Conflicting data → must resolve
4. **Gap**: Information in some reports but not others → investigate

### Step 3.3: Discrepancy Resolution

For every discrepancy:

1. Perform targeted WebSearch and WebFetch to find additional sources
2. Apply the three-tier priority order **in sequence**:
   - **① Timeliness**: A source from the last 3 months takes precedence regardless of tier. Data older than 6 months → flag `[可能过时]`.
   - **② Authority**: Among equally recent sources, apply credibility weights: Tier 1 = 3×, Tier 2 = 2×, Tier 3 = 1×, Tier 4 = 0.5×.
   - **③ Credibility**: Among equally recent and tiered sources, prefer specific numbers, reproducible methodology, and named authors.
3. All resolutions must be backed by at least 3 independent sources
4. Record each resolution with supporting evidence

### Step 3.4: Final Score Determination

For each scored dimension:
- All subagents agree → use consensus score
- Majority agree → use majority, verify with independent search
- All differ → perform additional research, use most credible source

**综合评价 precision rule**: Compute 综合评价 as a **decimal score (0.0–5.0) rounded to one decimal place** (e.g., `4.3`, `3.8`) that reflects nuanced differences between items. **Display the one-decimal value directly in the report** — do NOT convert to a bar symbol. This value is used for both sorting and display. Record it in the Raw Data section as well.

### Step 3.5: Source Deduplication

Collect all `### 主要参考数据来源` entries from all available research reports plus `sources.md`. Deduplicate by URL. Record total unique source count across all subagents. Use the deduplicated list in the final report appendix.

---

## Phase 4: Final Report Generation

### Step 4.1: Prepare Output Directory

```bash
mkdir -p comparison/coding-agents/
```

### Step 4.2: Generate Report Content

Write the final report in **Chinese** to the output file.

**Report Template:**

```markdown
# LLM 和 Coding Agents 比较

> **报告生成日期**：{YYYY年MM月DD日}<br>
> **检索数据源**：共分析 {N} 个网站和文章，涵盖官方文档、基准测试平台、技术媒体、开发者社区及学术来源；数据源通过最多 {N} 层爬取动态发现
>
> {LLM overview paragraph 1: current programming LLM landscape and major trends}
>
> {LLM overview paragraph 2 (optional): notable new models and significant changes}
>
> {Coding Agents overview paragraph 1: current AI coding agent landscape and major trends}
>
> {Coding Agents overview paragraph 2 (optional): notable new tools and significant changes}

## LLM 比较

| 制造商 | 模型 | 场景 | 上下文大小 | 最大输入 | 最大输出 | 推理能力 | 数学能力 | 编程能力 | 视觉能力 | 指令遵循 | 幻觉控制 | 多语言 | 长上下文<br>有效性 | JSON/<br>Tool Call | 开源 | 成本 | 综合评价 | 适用场景 |
| :----- | :--- | :--- | ---------: | -------: | -------: | :------: | :------: | :------: | :------: | :------: | :------: | :----: | :----------------: | :----------------: | :--: | :--: | ------: | :----- |
{table rows sorted by 综合评价 descending}

## Coding Agents 比较

| 制造商 | Agent | 第三方<br>模型 | Repo 理解 | 批量重构 | 自我纠错 | 长周期任务 | 工程能力 | Git 工作流 | 上下文压缩 | 记忆管理 | 并行子代理 | 工具调用 | 安全性 | 灵活性 | 成本控制 | 综合评价 | 强项 | 弱项 |
| :----- | :---- | :------------: | :-------: | :------: | :------: | :--------: | :------: | :--------: | :--------: | :------: | :--------: | :------: | :----: | :----: | :------: | ------: | :--- | :--- |
{table rows sorted by 综合评价 descending}

## 附录：数据来源

{deduplicated list of key sources from all subagents, sorted by tier}

- [{Site Name} - {Page Title}]({URL}) - {description of what data this source provided}
```

### Step 4.3: Strict Format Compliance

**MUST follow these rules EXACTLY:**

1. **No extra sections**: Only LLM table, Agents table, and appendix — nothing else.
2. **Bar notation**: Scored capability columns use ONLY: `-` (0), `⚪️` (1), `🟡` (2), `🟠` (3), `🔴` (4), `⚫️` (5). **Exception: the 综合评价 column displays the one-decimal value directly** (e.g., `4.3`, `3.8`) — do NOT use a bar symbol there.
3. **Pre-write sort check** ⚠️: Before calling Write, enumerate all rows by 综合评价 **decimal score** (from Step 3.4). Confirm non-increasing order. Fix any violation before writing.
4. **Sorting**: Both tables sorted by 综合评价 descending (highest first), NO out-of-order rows.
5. **Open Source**: Exactly `✅` or `❌`.
6. **Third-Party Model Support** (Agents table, 第三方模型 column): Exactly `✅` (supports third-party models), `❌` (does not support), or `❓` (unclear or unverified after research).
7. **Cost**: Exactly `⚫️`, `🔴`, `🟠`, `🟡`, `⚪️`.
8. **Header format** ⚠️: The ENTIRE header block — date line, source count line, AND all overview paragraphs — MUST be inside a Markdown blockquote (every line prefixed with `> `). Empty `>` lines between paragraphs. The `<br>` after the date line is MANDATORY.
9. **Alignment**: Follow `:---` / `---:` / `:--:` markers exactly.
10. **Manufacturer names**: Chinese companies use Chinese names (`智谱`, `月之暗面`, `深度求索`, `阿里云`); Western companies use official English names.
11. **Hyperlinks**: 制造商 and 模型/Agent columns must include verified markdown hyperlinks. For each URL: WebFetch it and confirm (a) HTTP 200 and (b) the page is model/agent-specific — not a manufacturer homepage. If it redirects to a homepage or fails, omit the link. A missing link is always better than a wrong link.
12. **Token counts**: Use `128K`, `1M`, `64K` — never raw numbers like `128000`.
13. **Recency**: Only the latest 1–2 generations per manufacturer. Remove deprecated or superseded models.
14. **Chinese-English spacing** ⚠️: Insert a space between Chinese characters and adjacent English letters, numbers, or symbols throughout ALL report output. Examples: `SWE-bench 得分` not `SWE-bench得分`; `Git 工作流` not `Git工作流`; `128K 上下文` not `128K上下文`.
15. **场景 column (LLM table)** ⚠️: For each model, identify ALL distinct deployment modes or access contexts that carry different technical specifications. Each scenario gets its own row; the 模型 cell repeats the model name. Research every possible scenario — API, web interfaces, thinking/reasoning variants, CLI tools, third-party cloud deployments — before concluding a model has only one scenario.
16. **适用场景 (LLM table)**: Short comma-separated Chinese labels.
17. **强项 / 弱项 (Agents table)**: Short comma-separated Chinese labels.
18. **Appendix**: Include `## 附录：数据来源` with deduplicated, verified source links.

### Step 4.4: Write Output File

Write the complete report to:
- Default: `comparison/coding-agents/coding-agents-{YYYYMMDD}.md`
- If `output_path` parameter was provided, use that instead.

After writing, inform the user of the file path.

---

## Quality Checklist

### Phase 0 — Preparation

- [ ] Exact date obtained from `date` command (not guessed); all 5 date values stored
- [ ] All 4 reference files read
- [ ] `.temp/llm-agent-comparison/` directory created

### Phase 0.5 — Discovery

- [ ] Source Discovery Subagent and Target Discovery Subagent launched simultaneously
- [ ] `sources.md` exists — contains Tier 1 seeds plus crawl- and search-discovered sources
- [ ] `llm-targets.md` exists — compiled from runtime web searches, not hardcoded names
- [ ] `agent-targets.md` exists — compiled from runtime web searches, not hardcoded names
- [ ] `references/manufacturers.md` updated if new manufacturers were discovered

### Phase 1 & 2 — Research

- [ ] All 10 research subagents launched simultaneously as **background agents**; task IDs recorded
- [ ] `group_start_unix` recorded immediately after launch via `date +%s`
- [ ] Each LLM subagent read `llm-targets.md` and researched every entry
- [ ] Each Agent subagent read `agent-targets.md` and researched every entry
- [ ] All 10 subagents read `sources.md` as primary source starting points
- [ ] All 10 subagents completed the MANDATORY SELF-ASSESSMENT before saving
- [ ] Monitoring loop ran every 5 min; `t3` and `t_elapsed` recorded once 3 in each group completed
- [ ] Stuck subagents (no output after 10 min post-`t3`) stopped via `TaskStop` and replaced
- [ ] Replacements given `t_elapsed` seconds; stopped via `TaskStop` if they also timed out
- [ ] All gaps (stopped/failed subagents) noted in the final report

### Phase 3 — Cross-Validation

- [ ] All available research reports read and compared side-by-side
- [ ] Discrepancies resolved with independent verification and documented
- [ ] Final 综合评价 computed as decimal for precise sorting; bar symbol used in report only
- [ ] Final scores determined through consensus or authoritative sources
- [ ] Sources deduplicated across all subagents; total unique count recorded

### Phase 4 — Report

- [ ] Output directory created
- [ ] Report written in Chinese with EXACT template format
- [ ] Header blockquote contains ALL lines including overview paragraphs (every line starts with `> `)
- [ ] `<br>` tag present after the date line; empty `>` lines between blockquote paragraphs
- [ ] Pre-write sort check performed — both tables confirmed non-increasing by 综合评价
- [ ] Both tables sorted by 综合评价 descending with NO out-of-order rows
- [ ] 综合评价 column shows one-decimal values (e.g., `4.3`, `3.8`), NOT bar symbols
- [ ] Bar notation used for scored capability columns; open source and cost markers correct
- [ ] 第三方模型 column (Agents table) uses `✅`/`❌`/`❓` only
- [ ] LLM table has 场景 column; each distinct deployment scenario has its own row
- [ ] No extra sections or content beyond the template
- [ ] Source count and max crawl depth reported in the header
- [ ] Manufacturer names use native language (Chinese companies in Chinese)
- [ ] Every hyperlink WebFetch-verified as model/agent-specific (not homepage redirects)
- [ ] Token counts use human-readable format (128K, 1M, not raw numbers)
- [ ] Only latest 1–2 model generations; deprecated models excluded
- [ ] Chinese-English spacing applied throughout (spaces between Chinese and English/numbers)
- [ ] `## 附录：数据来源` section included with deduplicated, verified source links

---

## Design Rationale

1. **Discovery-First Architecture**: LLM names and Coding Agent names are never hardcoded anywhere in this skill. Phase 0.5 compiles research targets dynamically from current web sources, ensuring the report always reflects the actual landscape at runtime — not the state of training data.
2. **Manufacturer List as a Living Document**: `references/manufacturers.md` is a starting-point base list. The Target Discovery Subagent searches for new manufacturers on each run and appends them in-place, so the file grows more accurate over time.
3. **Multi-Layer Source Crawl**: The Source Discovery Subagent follows citation and link trails up to 9 layers deep (capped at 30 pages with a 3-year time filter). This surfaces sources that are not directly indexed but are referenced by authoritative pages — simulating how an expert researcher follows leads.
4. **Parallel Discovery**: Source discovery and target discovery run simultaneously in Phase 0.5, minimizing total wall-clock time while maximizing input richness for Phase 1 & 2.
5. **Research Subagents as Focused Evaluators**: Phase 1 & 2 subagents receive explicit target lists and source lists rather than discovering their own targets. This separation of concerns eliminates anchoring bias and ensures every discovered target receives equal research attention.
