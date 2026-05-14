---
name: deep-read
description: |
  Deep-read and analyze web articles. Trigger this skill when the user asks to
  "deep-read" (深度解读) a URL, deeply analyze an article, thoroughly interpret web content,
  research terms and concepts in an article, verify article authenticity, or
  comprehensively evaluate an article. Also applies when a user sends a URL and
  asks to analyze, interpret, translate, summarize, or verify its contents.
  Phrases like "research this article" (研究这篇文章), "analyze this link" (分析这个链接), or "interpret this
  report" (解读这份报告) should also trigger this skill. This skill performs in-depth research,
  term extraction, fact-checking, and multi-dimensional analysis on a single
  article/webpage, producing a structured Chinese-language report.
disable-model-invocation: true
---

# Deep Read

Perform an in-depth analysis of a given URL and generate a structured analytical report.

## When to Use

Activate this skill when the user asks for deep reading, analysis, or research of an article or URL. Typical trigger phrases include:
- "deep-read this link"
- "analyze this article"
- "research this URL"
- "deeply interpret this report"
- "verify the content of this article"
- user directly sends a URL and asks for analysis

## Workflow

### Step 1: Fetch Page Content

Use the `WebFetch` tool to retrieve the main body of the page. Extract:
- Title
- Author / Organization
- Publication date
- Body content (Markdown format)

If `WebFetch` cannot retrieve the full content, try using `Bash` with `curl` or `wget` to fetch the HTML, then extract the body.

### Step 2: Language Detection and Translation

Detect the source language:
- If the body is primarily **Chinese**, skip translation.
- If the body is **another language**, translate it into **fluent, accurate Chinese**.

Translation requirements:
- Preserve the original tone and style.
- Keep professional terms in English with Chinese annotations.
- Ensure numbers, data, and quotes remain accurate.

### Step 3: Author Background Research

The 【作者介绍】 section is short by design — typically **3 short paragraphs** in plain prose (no subsections). Its sole purpose is to help readers quickly judge the article's credibility, so the research effort is concentrated on what establishes the author's authority on the topic, not on exhaustive biography.

Investigate the author through **authoritative, reliable, and trustworthy sources** (e.g., LinkedIn 个人主页、GitHub/GitLab 个人主页、所在公司或机构官方页面、个人官方博客或官网、维基百科、学术论文数据库、知名媒体报道、行业大会演讲资料、出版方作者介绍页等）。**严禁使用来源不明、内容农场或低权威度站点作为依据**。

What the three paragraphs should cover (kept tight; if a piece of information is not public, write "未公开" / "暂无可靠信息" rather than guess):

1. **第一段（身份定位）**：当前职位、所在组织、所属团队；一句话点明其与文章主题的关系。
2. **第二段（履历与代表作）**：与本文主题相关的关键履历、参与过的有公开记录的重大项目、发表的高影响力论文 / 书籍 / 文章 / 开源项目。
3. **第三段（活跃度与研究方向）**：近期发文频率、最近一次公开活动、近年的研究方向与技术栈，帮助读者判断作者在该话题上是否持续深耕。

Execution requirements:

1. Use **at least 3 independent Agents** to run parallel searches across different source types (e.g., one Agent 负责个人主页与公司页面，一个 Agent 负责学术/出版记录，一个 Agent 负责社交平台与媒体报道）。
2. Cross-verify key facts (current employer, key projects, notable works) against at least **3 distinct authoritative sources**.
3. For information that cannot be verified, clearly label it as "暂无可靠来源" — do not fabricate or speculate.
4. If the author **cannot be identified** (e.g., anonymous post, organization-authored article, byline missing), explicitly state so and **omit** the 【作者介绍】 section entirely.
5. All references used in the author introduction must be listed in the section's own 参考来源 list, with URLs that return HTTP status < 400 and meaningful content.

### Step 4: Extract Terms and Concepts

Read the full text carefully and extract all items that need explanation:
- **Professional terms** (technical vocabulary, industry jargon)
- **Abbreviations / acronyms** (e.g., AI, GDP, API)
- **Organizations / institutions** (e.g., NSA, WHO)
- **Personal names** (important figures need identity and background)
- **Laws, regulations, standards**
- **Products / technologies**
- **Historical events / allusions**
- **Other concepts that may hinder understanding**

For each extracted term, use multiple independent Agents to research in parallel:
- Full name (if an abbreviation)
- Accurate Chinese translation / explanation
- Specific meaning in the article's context
- Related background knowledge

Use at least **3 independent Agents** to research these terms in parallel, then merge results, deduplicate, and ensure accuracy and completeness.

### Step 5: Content Authenticity Verification

Verify key facts, data, and claims in the article:

1. Identify all **verifiable factual claims**, including:
   - Statistics
   - Historical event descriptions
   - Attributed statements / opinions
   - Technical parameters / performance metrics
   - Specifics like time, place, quantity

2. Use multiple Agents to search authoritative sources for **cross-verification** in parallel:
   - Use `WebSearch` to find multiple sources.
   - Prioritize authoritative sources (official institutions, academic journals, mainstream media, government sites).
   - Verify key claims against at least **3 distinct sources**.

3. Label verification results:
   - **Verified**: supported by multiple authoritative sources
   - **Partially verified**: only one source or of moderate credibility
   - **Questionable**: no reliable source found, or contradicts other sources
   - **Incorrect**: clearly refuted by reliable sources

### Step 6: In-Depth Interpretation

Based on the article content and verification results, perform a multi-dimensional analysis:

**Analysis dimensions (flexibly choose at least 2-3 based on article type):**

- **Core argument analysis**: main viewpoints, argument logic, strength of evidence
- **Background and context**: era background, industry environment, related history
- **Technical / professional dimension**: involved technical principles, professional methods, implementation details
- **Impact and significance**: scope of influence, long-term significance, potential consequences
- **Stakeholders**: individuals, organizations, groups involved and their positions and interests
- **Controversies and differing views**: different voices, opposing opinions, academic disputes
- **Trend judgment**: whether trends reflected in the article hold, future direction
- **Practical guidance value**: practical significance for readers / practitioners

**Interpretation requirements:**
- **Sufficient and necessary**: do not omit important content, nor pile up irrelevant information
- **Highlight key points**: focus on the most valuable parts of the article
- **Illustrate with examples**: use vivid, reasonable, and appropriate examples to aid understanding
- **Label controversies**: clearly mark controversial content and explain the points of contention
- **Value judgment**: point out the true value of the article

### Step 7: Generate Report

Consolidate all the above into a structured report and save it to a file.

**Output path:**

```text
generated/{kebab-case-topic}-deep-read-{YYYYMMDDHHmmss}.md
```

Where `{kebab-case-topic}` is generated from the article title (take the first 3-5 keywords, hyphenated, lowercase).

**Report format template (MUST be output in Chinese):**

``````markdown
# 深度解读：{文章标题}

> 原文：[{文章标题}]({文章URL})<br>
> 作者：{作者姓名/组织}<br>
> 日期：{YYYY-MM-DD HH:mm}

## 作者介绍

<!-- 仅在作者可识别时输出本节。目的是用几段话帮助读者快速判断文章的可信度：
     谁在写、目前在做什么、有哪些可核实的履历与代表作、在该话题上是否持续活跃。
     所有非平凡陈述都必须来自权威、可信、可靠的渠道（LinkedIn 个人主页、所在公司
     或机构官方页面、个人官方博客或官网、GitHub/GitLab 个人主页、维基百科、学术论文
     数据库、知名媒体报道、行业大会演讲资料、出版方作者介绍页等）。若某项信息
     查不到可靠来源，写 "未公开" 或 "暂无可靠信息"，不要凭空补全。若作者完全无法
     识别（如匿名稿、机构署名、署名缺失），则整节省略。 -->

{作者姓名}，{一句话身份定位，例如：现任 XX 公司 XX 团队 XX 职位，公开资料显示其长期关注 XX 方向}。{可选的权威代表作或任职背景的简短引述，例如：曾就职于 XX / 主导过 XX 项目 / 代表作包括 XX}

{第二段：履历亮点与代表作。重点是与本文主题直接相关的经历、参与的代表性项目、发表的高影响力论文或开源项目，让读者了解作者在该话题上的"发言资格"。信息不足时诚实写 "暂无公开资料"，不要编造。}

{第三段：近期活跃度与研究方向。简要说明作者最近的发文频率、所在社区或平台上的动态、长期关注的研究方向，帮助读者判断其结论是否建立在持续深耕之上。}

参考来源：

- [{来源}：{标题}]({URL}) — {简要说明引用此资料的原因}
- ...

## 原文及译文

<!-- Include this section ONLY if the original is NOT Chinese -->

<details>
<summary>原文</summary>
<section>

{原文 Markdown 格式}

</section>
</details>

<details>
<summary>译文</summary>
<section>

{译文 Markdown 格式}

</section>
</details>

## 摘要

{一段话总结文章的核心重点，100-300字}

## 术语表

<!-- Omit this section if no terms need explanation -->

| 术语 | 全称 | 解释 |
| :--- | :--- | :--- |
| {术语/缩写} | {全称，非缩写则留"-"} | {详细解释说明，2-4句话} |
| ... | ... | ... |

## 深度解读

### {主题/视角/维度1}

{深度展开分析，包含：核心观点、论据评估、相关背景}

### {主题/视角/维度2}

{深度展开分析}

<!-- Add more dimensions as needed -->

### 真实性评估

{对文章中关键事实的验证结果汇总}

| 声明/事实 | 验证状态 | 说明 |
| :--- | :--- | :--- |
| {具体声明} | 已验证/部分验证/存疑/有误 | {验证详情} |
| ... | ... | ... |

### 总结

{用一段精炼的话总结全文分析结论}

**关键要点：**

- {要点1}
- {要点2}
- {要点3}

## 参考资料

<!-- Omit this section if there are no external references -->

- [{参考资料标题}]({URL}) — {简要说明引用此资料的原因}
- ...
``````

## Quality Requirements

1. **Translation quality**: if translation is needed, it should be fluent and natural, accurately conveying the original meaning.
2. **Term accuracy**: term explanations should be authoritative and accurate, from reliable sources.
3. **Strict verification**: key facts must be cross-verified; do not blindly trust a single source.
4. **In-depth analysis**: go beyond summarizing content; analyze underlying logic, impact, and significance.
5. **Objectivity and fairness**: remain neutral on controversial content; present multiple perspectives.
6. **Format compliance**: strictly follow the report template above; ensure consistent output format.
7. **Author introduction quality**: the 【作者介绍】 section is short prose (no subsections), aimed at letting readers judge credibility; every non-trivial claim must be backed by an authoritative source listed in the section's 参考来源 list; if a piece of information cannot be sourced, either omit the sentence or mark it as "未公开" / "暂无可靠信息"; never fabricate biographical details.

## Notes

- If the article URL is inaccessible or content retrieval fails, inform the user and ask them to confirm the URL.
- If the article is very short (less than 500 words), ask the user to confirm whether they still want a deep read.
- Term research should focus on the meaning actually used in the article, not general definitions.
- When verifying, prioritize authoritative sources such as official, academic, and mainstream media.
- For content that cannot be verified, clearly label it "Unable to verify" — do not guess.
- References and citations in the report must have URLs that are accessible and do not return 404 or other errors.
- For the 【作者介绍】 section: only include it when the author is identifiable. If the byline is missing, generic (e.g., "编辑部"), or the author uses an opaque pseudonym with no verifiable public footprint, omit the section entirely rather than guessing.
- If multiple authors share the byline, cover each one with the same level of rigor; if a contributor has no public footprint, list them with "暂无可靠信息" rather than skipping silently.
- The 【作者介绍】 section's own 参考来源 list is independent of the main report's 参考资料 list at the bottom; do not mix them.
- 【作者介绍】 is intentionally brief (about 3 short paragraphs in plain prose, no subsections); resist the urge to expand it into a full biography.
