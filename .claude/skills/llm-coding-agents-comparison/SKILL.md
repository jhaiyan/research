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

- **Data sources**: Hardcoded Tier-1 seeds in `references/data-sources.md`; Source Discovery Subagent performs quick verification + a few targeted WebSearches (no deep multi-layer crawl). Each data source only contributes its **Top 20** entries.
- **Manufacturers**: Base list in `references/manufacturers.md` + runtime discovery; the file is updated in-place when new manufacturers are found
- **LLM names**: Never hardcoded — discovered at runtime by the Target Discovery Subagent (cap: top 20)
- **Coding Agents**: Never hardcoded — discovered at runtime by the Target Discovery Subagent (cap: top 20)
- **Research subagent count**: 2 per group (LLM, Agent) instead of 5 — the marginal value of subagents 3–5 was low because they read the same sources and ran the same queries; the value of subagent 1→2 (basic cross-check) is the only one worth paying for
- **Subagent work split**: Each research subagent in a group owns a disjoint half of the target list (no overlap). This replaces the original "5 subagents each research the whole list" pattern.

## Parameters

- `output_path`: Optional. Absolute path for output file. Defaults to `./comparison/coding-agents/coding-agents-{YYYYMMDD}.md` where `{YYYYMMDD}` is obtained from the shell.
- `target_count_cap`: Optional. Maximum number of LLMs and Agents to include in the final report. Default: 20 (each).

## Execution Flow Overview

```text
Phase 0: Preparation (parallel reads)
  ├── Get exact date from shell
  ├── Read references/data-sources.md
  ├── Read references/manufacturers.md
  └── Read references/llm-prompt.md and references/agent-prompt.md

Phase 0.5: Discovery (1 specialized subagent)
  └── Target + Source Discovery Subagent
      ├── Verify Tier 1 sources from data-sources.md are accessible (1 WebFetch per source)
      ├── Read manufacturers.md (base list)
      ├── For each manufacturer, search for their latest LLMs and coding agents (Top 20 each)
      ├── Run broad discovery searches to find new manufacturers and products (Top 20 per search)
      ├── Update references/manufacturers.md if new manufacturers found
      └── Output → .temp/llm-agent-comparison/sources.md
                  .temp/llm-agent-comparison/llm-targets.md
                  .temp/llm-agent-comparison/agent-targets.md

Phase 1 + Phase 2 (PARALLEL): Research (4 subagents)
  ├── Phase 1: 2 LLM subagents — split llm-targets.md into halves; each owns one half
  └── Phase 2: 2 Agent subagents — split agent-targets.md into halves; each owns one half
  (All 4 subagents also read sources.md for source access)

Phase 3: Cross-Validation and Synthesis (orchestrator-only, no subagents)

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

> **Subagent prompt files are read by the Phase 1 & 2 subagents themselves, not by the orchestrator.** The orchestrator only needs to know they exist and where they are so it can pass the paths in the subagent prompts.

---

## Phase 0.5: Discovery (1 Subagent)

**NOTE**: The original design launched 2 separate subagents (Source Discovery + Target Discovery). They have been merged into a single subagent because both work from the same manufacturer list and the same Tier-1 sources. The deep multi-layer crawl (9 hops, 30 pages) has been removed — discovery now only does quick verification of Tier-1 sources and a small number of targeted WebSearches.

### Combined Discovery Subagent

This subagent verifies Tier-1 sources are still accessible, discovers new manufacturers / LLMs / agents, and produces the target lists for Phase 1 & 2.

**Subagent Prompt:**

``````markdown
You are the Discovery Subagent for a LLM/Coding Agent comparison report.

**Today's date: {YYYY年MM月DD日}**
**Current year-month: {YYYY-MM}**
**Top-N cap**: {N} (default 20) — never exceed this for any list.

## Your Mission

Three things:
1. Verify Tier-1 sources from `data-sources.md` are accessible (one quick WebFetch per source).
2. Discover which LLMs and AI coding agents exist RIGHT NOW — no hardcoded names anywhere.
3. Produce three output files: `sources.md`, `llm-targets.md`, `agent-targets.md`.

## Step 1: Verify Tier-1 Sources

Read `.claude/skills/llm-coding-agents-comparison/references/data-sources.md`.
For each Tier-1 seed URL listed there, perform **one** WebFetch and record whether it is accessible and what data it contains. Stop after the verification pass — **no multi-layer crawling, no link following, no breadth-first expansion**.

## Step 2: Read the Base Manufacturer List

Read `.claude/skills/llm-coding-agents-comparison/references/manufacturers.md`.
Treat it as a starting point, not a complete or current list.

## Step 3: Discover New Manufacturers (Top 20)

Run a small set of broad discovery searches to find manufacturers that may have emerged since the file was last updated:

```text
new AI company LLM model released {YYYY}
AI 大模型 新公司 新模型 {YYYY}
new AI coding assistant company {YYYY}
```

For each candidate manufacturer found, **WebFetch the top result page** to verify they have an actual released, publicly accessible model (not just a press release or funding announcement). Do NOT add companies with no live model.

Cap new-manufacturer additions at **Top 20** — if you find more, keep only the 20 most significant (by model availability, funding, or community recognition).

## Step 4: Discover Current LLMs (Top 20)

For **each manufacturer** in the list (base + newly discovered), run one search:

```text
[manufacturer name] latest model release {YYYY-MM}
```

Pick at most the **Top 20 currently active LLMs** across all manufacturers, deduplicated. Selection priority:
1. Coding-specialized or coding-strong models
2. Models released or significantly updated within the last 6 months
3. Models on T1 leaderboards (LMSYS, Artificial Analysis, SWE-bench)
4. Models with verifiable public API or open weights

For each LLM: record manufacturer, exact model name + version, approximate release date, official page URL. WebFetch the official page to confirm it is model-specific (not a manufacturer homepage) before including the link.

Also run a few broad sweeps, but **each search consumes only the Top 5 result pages**:

```text
top LLM benchmark leaderboard {YYYY-MM}
best coding LLM {YYYY} comparison
大模型 最新 排行 {YYYY}
```

## Step 5: Discover Current Coding Agents (Top 20)

Run a small set of discovery searches, **Top 5 result pages per query**:

```text
best AI coding agent {YYYY} review
SWE-bench agent leaderboard {YYYY-MM}
AI coding assistant comparison {YYYY}
AI 编程助手 最新 对比 {YYYY}
```

For each agent: verify it is actively maintained (last update within 12 months — check GitHub release dates or official blog). Pick at most the **Top 20 currently active agents**. Exclude discontinued, rebranded-beyond-recognition, or vaporware tools.

## Step 6: Write Output Files

### File 1: Update manufacturers.md (only if new manufacturers found)

If you discovered manufacturers not in `.claude/skills/llm-coding-agents-comparison/references/manufacturers.md`, append new rows to the appropriate tables. Keep all existing content intact. Update the "Last Updated" line at the top.

### File 2: sources.md

Save to `.temp/llm-agent-comparison/sources.md`:

```markdown
# Discovered Sources

Generated: {YYYY年MM月DD日}

## Tier 1 Seeds (Verified Accessible)

| Source | URL | Accessible | Key Data Found |
| :----- | :-- | :--------: | :------------- |
| {name} | {url} | ✅/❌ | {e.g. "Top 20 models by Elo"} |

## Discovery Searches (Top 5 pages per query)

| Query | Pages Fetched | New Sources Found |
| :---- | ------------: | :---------------- |
| {query} | {N} | {list or "none"} |
```

### File 3: llm-targets.md

Write `.temp/llm-agent-comparison/llm-targets.md`:

```markdown
# LLM Research Targets

Generated: {YYYY年MM月DD日}
Source: Discovery Subagent

This list was compiled dynamically from current web sources — NOT from hardcoded training data.
Phase 1 subagents MUST research EVERY model listed here.

## Target LLMs (Top {N})

| # | Manufacturer | Model Name | Version / Release Date | Official Page | Notes |
| - | :----------- | :--------- | :--------------------- | :------------ | :---- |
| 1 | ... | ... | ... | ... | ... |

## Discovery Summary

- Manufacturers searched: {N}
- New manufacturers found: {list or "none"}
- Total LLM entries: {N} (capped at {N})
- Models excluded and why: {list or "none"}
```

### File 4: agent-targets.md

Write `.temp/llm-agent-comparison/agent-targets.md`:

```markdown
# Coding Agent Research Targets

Generated: {YYYY年MM月DD日}
Source: Discovery Subagent

This list was compiled dynamically from current web sources — NOT from hardcoded training data.
Phase 2 subagents MUST research EVERY agent listed here.

## Target Agents (Top {N})

| # | Manufacturer | Agent Name | Primary Models (initial) | Official Page | Notes |
| - | :----------- | :--------- | :----------------------- | :------------ | :---- |
| 1 | ... | ... | ... | ... | ... |

## Discovery Summary

- Total agent entries: {N} (capped at {N})
- Agents excluded and why: {list or "none"}
```

## Self-Assessment Before Saving

- [ ] Did I cap the LLM list at Top 20 (or specified N)? Did I cap agents at Top 20?
- [ ] Did I avoid multi-layer crawling and stop at Tier-1 verification?
- [ ] Is every entry a currently active model/agent?
``````

---

### Wait for Phase 0.5 Subagent

Wait for the subagent to complete. Verify these files exist:

- `.temp/llm-agent-comparison/sources.md`
- `.temp/llm-agent-comparison/llm-targets.md`
- `.temp/llm-agent-comparison/agent-targets.md`

If any file is missing, retry once. If it fails again, proceed with available data and note the gap in the final report.

---

## Phase 1 & Phase 2: Parallel Research (4 Subagents)

**CRITICAL**: Launch all 4 subagents as **background agents** simultaneously in a single message. Record each task ID returned from the Agent tool call — you will need these IDs for the timeout/retry mechanism below.

Record the group start time immediately after launch:

```bash
date +%s    # → {group_start_unix}  (Unix timestamp, for elapsed-time math)
```

### Split the Target List

After Phase 0.5 completes, read `llm-targets.md` and `agent-targets.md`. For each, split the entries into two **disjoint halves**:

- LLM Subagent #1: rows 1 to ceil(N/2)
- LLM Subagent #2: rows ceil(N/2)+1 to N
- Agent Subagent #1: rows 1 to ceil(N/2)
- Agent Subagent #2: rows ceil(N/2)+1 to N

Each subagent owns its half and must NOT research entries owned by its partner. This replaces the original "5 subagents each research the whole list" pattern, which produced 5× overlapping reports.

### Phase 1: LLM Research (2 Subagents)

Launch 2 independent `general-purpose` subagents with **different** prompts (different `{SubagentNumber}` AND different `{TargetRange}`):

``````markdown
You are LLM Research Subagent #{SubagentNumber} of 2.

- **Today's date: {YYYY年MM月DD日}**
- **Current year-month: {YYYY-MM}**
- **Your target range**: rows {TargetRange} of `.temp/llm-agent-comparison/llm-targets.md` (e.g., rows 1–10). Research ONLY this range. Do NOT research entries outside this range — Subagent #{OtherNumber} owns those.

Read the full research guide from `.claude/skills/llm-coding-agents-comparison/references/llm-prompt.md` and follow its instructions exactly.

Your target list is in `.temp/llm-agent-comparison/llm-targets.md` — research only the rows in your range.
Your source list is in `.temp/llm-agent-comparison/sources.md` — use these as primary research starting points.

Save your complete findings to `.temp/llm-agent-comparison/llm-research-{YYYYMMDDHHmmss}-{SubagentNumber}.md`.

CRITICAL RULES:
- Do NOT use Baidu or low-credibility sources
- Verify every hyperlink via WebFetch — model-specific pages only, not manufacturer homepages; omit any link that redirects to a homepage or fails
- Insert a space between Chinese characters and adjacent English letters/numbers in ALL output
- **3-source rule applies only to SCORED fields (capability dimensions, overall)**. Categorical fields (manufacturer name, open source ✅/❌, token counts, version strings) require 1 authoritative source only.
- Each model: run 2–3 focused queries (not 5+). Stop when you have the 3-source consensus for a score.
- **EXACT VERSION NUMBERS**: Always use the specific, full version string (e.g., `GPT-4.5`, `Claude Sonnet 4.6`, `Gemini 2.5 Pro`). NEVER use a vague family name like `GPT-5` when a specific point-release exists. If you cannot confirm the exact version, search harder before falling back.
- **NO LAZY N/A**: Never mark a field as N/A (or `-`) without first checking the official API docs, model card, and one leaderboard. Mark as `-` ONLY if the data is genuinely absent. Do not over-search categorical fields.
- **EXCLUDE UNRELEASED / KEY-DATA-MISSING MODELS**: Skip any model that (a) has not been publicly released or is not accessible via API/public access, OR (b) lacks publicly verifiable data for at least 3 of these key fields: context size, a coding benchmark score, and cost. Document every excluded model with a reason in the Raw Data section.
- **STAY IN YOUR RANGE**: Do NOT research entries outside {TargetRange} — Subagent #{OtherNumber} is responsible for those.
``````

### Phase 2: Coding Agent Research (2 Subagents)

Launch 2 independent `general-purpose` subagents with **different** prompts:

``````markdown
You are Coding Agent Research Subagent #{SubagentNumber} of 2.

- **Today's date: {YYYY年MM月DD日}**
- **Current year-month: {YYYY-MM}**
- **Your target range**: rows {TargetRange} of `.temp/llm-agent-comparison/agent-targets.md`. Research ONLY this range. Do NOT research entries outside this range — Subagent #{OtherNumber} owns those.

Read the full research guide from `.claude/skills/llm-coding-agents-comparison/references/agent-prompt.md` and follow its instructions exactly.

Your target list is in `.temp/llm-agent-comparison/agent-targets.md` — research only the rows in your range.
Your source list is in `.temp/llm-agent-comparison/sources.md` — use these as primary research starting points.

Save your complete findings to `.temp/llm-agent-comparison/agent-research-{YYYYMMDDHHmmss}-{SubagentNumber}.md`.

CRITICAL RULES:

- Do NOT use Baidu or low-credibility sources
- Verify every hyperlink via WebFetch — agent-specific pages only, not manufacturer homepages; omit any link that redirects to a homepage or fails
- Insert a space between Chinese characters and adjacent English letters/numbers in ALL output
- Scores must be fair for ALL agents including less-popular ones (Aider, Continue.dev, Codex CLI, Cody, etc.)
- **3-source rule applies only to SCORED fields (capability dimensions, overall)**. Categorical fields (manufacturer name, third-party model support, version strings) require 1 authoritative source only.
- Each agent: run 2–3 focused queries (not 5+). Stop when you have the 3-source consensus for a score.
- **EXACT VERSION NUMBERS**: Use the precise, full product name and version where known (e.g., `Claude Code 1.x`, `Cursor 0.45`). NEVER use vague identifiers when a specific version is publicly documented.
- **NO LAZY N/A**: Never mark a field as N/A (or `-`) without first checking the official docs and one leaderboard/review site. Do not over-search categorical fields.
- **EXCLUDE UNRELEASED / KEY-DATA-MISSING AGENTS**: Skip any agent that (a) has not been publicly released or is not accessible, OR (b) lacks publicly verifiable data for at least 3 key capability dimensions. Document every excluded agent with a reason in the Raw Data section.
- **STAY IN YOUR RANGE**: Do NOT research entries outside {TargetRange} — Subagent #{OtherNumber} is responsible for those.
``````

### Monitoring and Timeout/Retry Mechanism

Apply the following logic **independently** to each group (LLM group = subagents 1–2; Agent group = subagents 1–2). Both groups run concurrently.

#### Monitoring Loop

Every 5 minutes after launch, run these checks in parallel:

```bash
date +%s                                   # current Unix timestamp
ls .temp/llm-agent-comparison/             # which output files exist
```

Use `TaskList` to confirm which background tasks are still running vs. completed.

#### Phase A — Waiting for 1 completion

A subagent is **complete** when its output file exists in `.temp/llm-agent-comparison/`:

- LLM subagents: `llm-research-*-{N}.md`
- Agent subagents: `agent-research-*-{N}.md`

Once **1 subagent in a group** has completed, record:

- `t1 = current Unix timestamp`
- `t_elapsed = t1 - group_start_unix`  (seconds it took to get 1 completion)

#### Phase B — 10-minute countdown per remaining subagent

For each remaining (still-running) subagent in the group, start a personal 10-minute countdown from `t1`.

Check every 5 minutes. If a subagent has **not** completed within 10 minutes of `t1`:

1. Find its task ID (recorded at launch, or via `TaskList`)
2. Call `TaskStop(task_id)` to terminate it
3. Launch one **replacement subagent** (same prompt, same `{SubagentNumber}`) as a background agent, with this **urgent time-limit notice prepended to the prompt**:

   > **URGENT TIME LIMIT**: You are a replacement for a subagent that timed out. You MUST write your output file within **{t_elapsed} seconds** from now — this is a hard deadline. Prioritize breadth: cover every target in your range with sufficient evidence, but do not over-invest in any single item. Failing to write the output file is not acceptable.

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

- `llm-research-{timestamp}-1.md`, `-2.md`
- `agent-research-{timestamp}-1.md`, `-2.md`

### Step 3.2: Comparative Analysis

For each model/agent, compare the 2 subagent reports side-by-side:

1. **Consensus**: Both subagents agree → high confidence
2. **Discrepancy**: Conflicting data → must resolve
3. **Gap**: Information in one report but not the other → investigate

> **Note on coverage**: Because the 2 subagents in each group own **disjoint halves** of the target list, no model/agent appears in both reports. Cross-validation between the two subagents is therefore impossible at the model level. Validation at the **source level** is still possible (e.g., if a coding score for `Claude Sonnet 4.6` from Subagent #1 disagrees with a T1 leaderboard read by Subagent #2 for a different model, the disagreement flags a data quality issue). Apply this comparison only to overlapping data points (e.g., sources, methodology, scoring patterns).

### Step 3.3: Discrepancy Resolution

For every discrepancy:

1. Perform at most 1–2 targeted WebSearch / WebFetch to find a tiebreaker source (do not over-invest)
2. Apply the three-tier priority order **in sequence**:
   - **① Timeliness**: A source from the last 3 months takes precedence regardless of tier. Data older than 6 months → flag `[可能过时]`.
   - **② Authority**: Among equally recent sources, apply credibility weights: **T1 = 3×, T2 = 2×, T3 = 1×, T4 = 0.5×** (defined in `references/data-sources.md`).
   - **③ Credibility**: Among equally recent and tiered sources, prefer specific numbers, reproducible methodology, and named authors.
3. A single T1 source is sufficient to resolve a discrepancy; no 3-source consensus is required at the discrepancy stage
4. Record each resolution with supporting evidence

### Step 3.4: Final Score Determination (10-Point Relative Normalization)

For each scored dimension:

- The single subagent's score is used as-is (no second subagent reports the same model because of the disjoint split)
- Flag the model as `[单源]` if the score came from only one subagent
- The synthesis layer may perform a single targeted verification WebSearch/WebFetch if a score looks anomalous; otherwise use the subagent's raw score

**All scored columns use a 0–10 integer scale with relative normalization.** Subagents collect raw integer scores (0–10) per dimension. After consolidating all subagent reports, apply this normalization to **every scored column**:

1. Compute the column-wide `min` and `max` across all models/agents.
2. For each value `v`: `final = round(((v - min) / (max - min)) × 10)`, clamped to `[0, 10]`.
3. **The lowest-scoring item → `0`; the highest → `10`; everything else linearly interpolated.**
4. If `min == max` (all items equal), assign every item `5` (mid).
5. **Display rule**: The final report shows the normalized integer 0–10 directly (e.g., `9`, `7`, `0`). **No bar symbols, no decimals.** Record both raw and normalized values in the Raw Data section.

**Cost column special case (LLM table)**: Cost is inverse-scored — higher cost = lower score. Subagents record the relative API cost tier as a raw integer 0–10 where `0 = cheapest` and `10 = most expensive`. After the standard normalization above, **flip** each value via `10 - final` so the cheapest item ends up at 10 and the most expensive at 0.

**Why relative**: A 0–10 absolute scale requires every subagent to share a common yardstick, which is impractical across heterogeneous benchmarks. Relative normalization guarantees the displayed extremes actually appear in the report (at least one `0` and one `10` per column), preserves the rank order produced by the evidence, and makes per-column comparison meaningful within each run.

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
> **检索数据源**：共分析 {N} 个网站和文章，涵盖官方文档、基准测试平台、技术媒体、开发者社区及学术来源；数据源以 Tier-1 种子源为主，按需补充动态检索结果
>
> {LLM overview paragraph 1: current programming LLM landscape and major trends}
>
> {LLM overview paragraph 2 (optional): notable new models and significant changes}
>
> {Coding Agents overview paragraph 1: current AI coding agent landscape and major trends}
>
> {Coding Agents overview paragraph 2 (optional): notable new tools and significant changes}

## LLM 比较

| 制造商 | 模型 | 场景 | 上下文<br>大小 | 最大输入 | 最大输出 | 推理能力 | 数学能力 | 编程能力 | 视觉能力 | 指令遵循 | 幻觉控制 | 多语言 | 长上下文<br>有效性 | JSON/<br>Tool Call | 开源 | 成本 | 综合评价 | 适用场景 |
| :----- | :--- | :--- | -------------: | -------: | -------: | :------: | :------: | :------: | :------: | :------: | :------: | :----: | :----------------: | :----------------: | :--: | :--: | ------: | :----- |
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
2. **Score display (10-point integers)**: All scored columns — capability dimensions AND 综合评价 — display the **normalized integer 0–10 directly** in the final report (e.g., `9`, `7`, `0`). **No bar symbols, no decimals.** Display `0` (not `-`) for the lowest item per column after normalization; do not use `-` as a marker in scored columns.
3. **Pre-write sort check** ⚠️: Before calling Write, enumerate all rows by 综合评价 **normalized integer** (from Step 3.4). Confirm non-increasing order. Fix any violation before writing.
4. **Sorting**: Both tables sorted by 综合评价 descending (highest first), NO out-of-order rows.
5. **Open Source**: Exactly `✅` or `❌`. Categorical, not scored.
6. **Third-Party Model Support** (Agents table, 第三方模型 column): Exactly `✅` (supports third-party models), `❌` (does not support), or `❓` (unclear or unverified after research). Categorical, not scored.
7. **Cost (LLM table)**: Display the **normalized integer 0–10 directly** (e.g., `8`, `3`, `0`). Higher score = lower cost (better value). Inverse scoring applied in Phase 3.4.
8. **Header format** ⚠️: The ENTIRE header block — date line, source count line, AND all overview paragraphs — MUST be inside a Markdown blockquote (every line prefixed with `>` followed by a space). Empty `>` lines between paragraphs. The `<br>` after the date line is MANDATORY.
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

- [ ] Discovery Subagent launched (single subagent, no multi-layer crawl)
- [ ] `sources.md` exists — Tier-1 seeds verified accessible plus a small number of discovery searches (Top 5 pages per query)
- [ ] `llm-targets.md` exists — Top 20 currently active LLMs, compiled from runtime web searches
- [ ] `agent-targets.md` exists — Top 20 currently active agents, compiled from runtime web searches
- [ ] `references/manufacturers.md` updated if new manufacturers were discovered

### Phase 1 & 2 — Research

- [ ] All 4 research subagents (2 LLM + 2 Agent) launched simultaneously as **background agents**; task IDs recorded
- [ ] `group_start_unix` recorded immediately after launch via `date +%s`
- [ ] Target list split into disjoint halves; each subagent owns one half (LLM #1 = first half, LLM #2 = second half, same for Agent)
- [ ] Each subagent read `sources.md` as primary source starting points
- [ ] Each subagent completed the (now shorter) SELF-ASSESSMENT before saving
- [ ] Monitoring loop ran every 5 min; `t1` and `t_elapsed` recorded once 1 in each group completed
- [ ] Stuck subagents (no output after 10 min post-`t1`) stopped via `TaskStop` and replaced
- [ ] Replacements given `t_elapsed` seconds; stopped via `TaskStop` if they also timed out
- [ ] All gaps (stopped/failed subagents) noted in the final report

### Phase 3 — Cross-Validation

- [ ] All available research reports read and compared side-by-side
- [ ] Discrepancies resolved with independent verification and documented
- [ ] Final scores normalized to **relative 0–10 integers** (lowest = 0, highest = 10) per column; raw and normalized values recorded
- [ ] Cost column inverse-scored (higher cost = lower score); flip applied so cheapest = 10, most expensive = 0
- [ ] Final scores determined through consensus or authoritative sources
- [ ] Authority tier weights applied per Step 3.3 (T1 = 3×, T2 = 2×, T3 = 1×, T4 = 0.5×)
- [ ] Sources deduplicated across all subagents; total unique count recorded

### Phase 4 — Report

- [ ] Output directory created
- [ ] Report written in Chinese with EXACT template format
- [ ] Header blockquote contains ALL lines including overview paragraphs (every line starts with `>` followed by a space)
- [ ] `<br>` tag present after the date line; empty `>` lines between blockquote paragraphs
- [ ] Pre-write sort check performed — both tables confirmed non-increasing by 综合评价
- [ ] Both tables sorted by 综合评价 descending with NO out-of-order rows
- [ ] All scored columns (capability dimensions + 综合评价) display **normalized integers 0–10** (no bar symbols, no decimals)
- [ ] At least one `0` and one `10` appear per scored column after normalization
- [ ] Cost column displays inverse-scored 0–10 integers (higher score = lower cost)
- [ ] Open Source column uses `✅`/`❌` only; Third-Party Model Support uses `✅`/`❌`/`❓` only
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
2. **Manufacturer List as a Living Document**: `references/manufacturers.md` is a starting-point base list. The Discovery Subagent searches for new manufacturers on each run and appends them in-place, so the file grows more accurate over time.
3. **Top-20 Source Cap**: Every data source (leaderboard, benchmark, news feed) contributes only its Top 20 entries. This caps total research work to a known bound, prevents the report from being dominated by long-tail minor models/agents, and keeps each subagent's research load bounded.
4. **No Multi-Layer Crawl**: The original 9-hop / 30-page multi-layer crawl was removed. The Discovery Subagent now does (a) one WebFetch per Tier-1 seed for accessibility verification, and (b) a small number of targeted WebSearches (Top 5 pages per query). The diminishing returns of deep crawling did not justify the cost.
5. **Single Discovery Subagent**: Source verification and target discovery are merged into one subagent. They share the same manufacturer list and the same sources — separating them doubled orchestration overhead without adding coverage.
6. **2 Subagents per Group, Disjoint Halves**: Phase 1 has 2 LLM subagents and Phase 2 has 2 Agent subagents, each owning one half of the target list. The original 5-subagent design produced 5× overlapping reports with marginal additional coverage; 2 subagents with disjoint ownership guarantees the entire list is covered exactly once and the second subagent serves as a partial cross-check on scoring patterns (not on individual models).
7. **Research Subagents as Focused Evaluators**: Phase 1 & 2 subagents receive explicit target ranges and source lists rather than discovering their own targets. This separation of concerns eliminates anchoring bias and ensures every discovered target receives equal research attention.
