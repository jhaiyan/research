---
name: recommendation
description: High-quality recommendation engine for researching and ranking items. Use this whenever the user asks for "the best", "最好", "top recommendations", "推荐", or a list of high-quality tools, services, or resources. It employs 5 independent subagents to research, cross-verify findings across at least 5 sources per item, and synthesize a final authoritative ranked list.
disable-model-invocation: true
---

# Recommendation Research Workflow

This skill implements a rigorous, multi-agent research and synthesis process to provide authoritative recommendations.

## Phase 0: Topic Analysis & Dimension Definition

Before launching subagents, the main agent must determine the most appropriate evaluation criteria for the specific topic.

1. **Dimensional Research**: Perform a quick targeted research to identify how experts evaluate the requested items (e.g., for "Code Review Agents", dimensions might be "Autonomous Capability", "Verification Mechanism", "Integration Ease", and "Community Trust").
2. **Define Evaluation Matrix**: Select 3-5 key dimensions that will serve as the column headers for all subagent reports and the final synthesis table.
3. **Standardize Metrics**: Define what constitutes a "high" vs "low" score for each dimension to ensure consistency across subagents.

## Phase 1: Parallel Independent Research

Launch 5 independent `general-purpose` agents to research the topic. **CRITICAL: Each subagent MUST be given the EXACT SAME task prompt — same objectives, same evaluation dimensions, same instructions. DO NOT assign different focus areas, domains, angles, or specialized roles to different subagents.** Their independence must come from independent execution of the **identical** task. This is essential for meaningful cross-verification.

The main agent MUST pass the specific evaluation dimensions defined in Phase 0 to each subagent.

**Instructions for each Subagent:**

1. **Authoritative Source Discovery**: Before searching for candidates, identify a diverse list of high-signal sources relevant to the topic. This must include:
   - Global authoritative websites, specialized forums (e.g., Hacker News, Reddit, StackOverflow), and industry-standard lists.
   - Sources in multiple languages (e.g., English, Chinese, Japanese) to avoid linguistic bias.
   - Niche engineering blogs, academic repositories, or official documentation hubs.
2. **Multi-Source Research & Candidate Expansion**: Using the discovered sources, identify and extract a minimum of 3 times (3x) the number of items requested by the user (e.g., if the user asks for Top 5, you MUST find at least 15 candidates). This is a HARD REQUIREMENT to ensure a diverse and high-quality pool for synthesis.
   > **Fallback**: If after thorough research fewer candidates are found, report ALL candidates discovered, even if less than 3x. Do not fabricate or pad entries. Include a note in Chinese explaining the limitation (e.g., "经多轮检索共发现 X 条，符合验证标准的共 Y 条").
3. **Strict URL & Fact Verification**: For every candidate:
   - **Liveness Check**: You MUST use `WebFetch` to verify the official URL. If the page returns a 404 or is unreachable, the candidate MUST be discarded.
   - **Cross-Verification**: Verify the item's reputation, quality, and claims across **at least 5 different credible, independent sources**.
4. **Comprehensive Reporting**: Return your findings to the main agent via your result message. **Your ENTIRE output must be a single markdown table. NO other text, NO headers, NO explanations, NO summaries, NO separate sections, NO lists outside the table. Just the table.**
   ```markdown
   | 状态 | {推荐条目类型} | {Dimension 1} | {Dimension 2} | ... | {Dimension N} | 推荐理由 | 验证状态 |
   | ---: | :--- | :--- | :--- | ... | :--- | :--- | :--- |
   | {排名/候选} | [{条目名称}]({条目官方URL}) | {评价} | {评价} | ... | {评价} | {推荐理由} | {e.g. URL 200 OK, 5+ sources verified} |
   ```
   > **推荐理由 must describe the item's own merits** — its features, quality, reputation, adoption, and unique strengths. Do NOT use "most agents mentioned it" or consensus counts as the reason.
   >
   > **DO NOT save any files to disk. DO NOT create intermediate reports.**
   >
   > You MUST report the ENTIRE pool of identified candidates (all 15+ if 5 were requested, not just your top picks). Use the following table format. The number of dimension columns must match the dimensions provided by the main agent in Phase 0:

## Phase 2: Synthesis and Validation

Once all 5 subagents have returned their reports, the main agent must perform the following:

1. **Comparative Analysis**: Compare the 5 reports. Identify commonalities, outliers, and contradictions.
2. **Conflict Resolution**: If reports contradict each other (e.g., different rankings for the same item), perform a targeted search using authoritative/primary sources to resolve the conflict.
3. **Deduplication**: Merge all candidate lists and remove duplicate entries.
4. **Final Selection**: From the deduplicated pool of cross-verified candidates, select the top $N$ items (where $N$ is the user's requested count) based on the strongest evidence and the defined dimensions.
   > **CRITICAL: 推荐理由 must describe the item's own merits — its features, quality, reputation, adoption, and unique strengths. Do NOT use "X/Y subagents recommended it" or "most subagents mentioned it" as the primary justification. Subagent consensus is a necessary filtering condition, not a sufficient recommendation reason. Cross-verification counts belong only in the `最终评估说明` column.**

## Phase 3: Final Output Generation

**CRITICAL: Save the final report to `{project-root}/generated/{topic}-recommendation-report-{YYYYMMDDHHmmss}.md`**

- The output path MUST be `{project-root}/generated/` — the `generated/` directory at the **PROJECT ROOT**, NOT inside the skill directory (e.g., NOT `.claude/skills/recommendation/generated/`)
- Use `date +"%Y%m%d%H%M%S"` to generate the timestamp
- Before writing, ensure the `generated/` directory exists at project root (create it with `mkdir -p` if needed)

**Instructions for the main agent:**

- The report MUST contain exactly two sections: `## 推荐列表` and `## 各子代理的研究报告`. Do NOT add extra sections.
- In the `## 各子代理的研究报告` section, each subagent's table MUST include the **FULL candidate pool** that the subagent identified (at least 3x the number of items requested by the user). Do NOT truncate, summarize, or only list top picks. Every candidate row the subagent reported must appear in the final report so that the cross-verification is fully transparent.
- The number of dimension columns in both tables must match the dimensions defined in Phase 0.

**The report MUST follow this exact Markdown format. Do NOT add any text outside the specified structure:**

```markdown
# {Title of the Recommendation}

报告生成时间：{YYYY-MM-DD HH:mm}

## 推荐列表

| 排名 | {推荐条目类型} | {Dimension 1} | {Dimension 2} | ... | {Dimension N} | 推荐理由 |
| ---: | :--- | :--- | :--- | ... | :--- | :--- |
| {排名} | [{条目名称}]({条目官方URL}) | {评价} | {评价} | ... | {评价} | {推荐理由} |

## 各子代理的研究报告

<details>
<summary>子代理 {子代理编号}</summary>
<section>

| 状态 | {推荐条目类型} | {Dimension 1} | {Dimension 2} | ... | {Dimension N} | 推荐理由 | 最终评估说明 |
| ---: | :--- | :--- | :--- | ... | :--- | :--- | :--- |
| {排名/候选} | [{条目名称}]({条目官方URL}) | {评价} | {评价} | ... | {评价} | {推荐理由} | {主代理最终评估说明} |

</section>
</details>
```
