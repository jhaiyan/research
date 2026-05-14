# Deep Research Report Template

## Report Template

``````markdown
# 深度研究报告：{概念或术语名或技术或产品名}

- 报告生成时间：{YYYY-MM-DD HH:mm，通过 date 命令生成}
- 主题类型：{概念/术语/技术/产品/工具/框架等，可同时标注多个类型，如"概念、技术"}

## 概述

- [提出方|出品方]：{概念或术语的提出方|技术或产品的出品方，严格求证原始出处}
- [提出时间|出品时间]：{概念或术语的提出时间|技术或产品的出品时间，严格求证最早时间}
- 领域：{概念术语或技术产品的所在领域}

{简短的核心概述，突出重点、价值、提出背景及解决的问题}

## 提出背景/解决的核心问题

{详细阐述提出背景、起源时间、事件脉络、要解决的问题及解决方式}

## 发展历程

<!-- 以时间线形式描述技术的完整发展历程，包括但不限于：提出、引发关注、发展、热议/讨论争议、稳定或淘汰、应用实践、波折、现状、前景等阶段 -->

- {YYYY年M月D日} {简述，简述内容应标明出处，如"Someone 在 [Article Title](https://example.com/articles/1) 发表文章引发热议"，务必确保链接有效、可达}

## 适用场景

{适用场景}

## 技术信息

{详细的技术信息}

## 安装说明

{技术产品的安装说明，跨平台产品要分平台说明}

## 使用说明

{技术产品的使用说明，包含典型场景的应用示例}

## 方法论

{设计哲学、方法论、最佳实践、避坑指南、常见错误排查指南}

## 应用与发展趋势

{应用现状与未来发展趋势}

## 与同类方案的对比

<!-- 如果 Topic 是"概念/方法论"类型，本 section 应该对比：
- 该概念的不同理论定义/流派（不同学者对同一概念的不同诠释）
- 该方法论的替代/竞争方法论
- 不要把"实现该概念的产品/框架"放在这里比较——产品/框架应放在"适用场景"或"应用与发展趋势"中作为实践案例 -->

<!-- 如果 Topic 是"产品/工具"类型，本 section 用来对比同类竞品：
- 功能对比
- 性能对比
- 生态对比 -->

<!-- 如果 Topic 是"技术/框架"类型，本 section 用来对比同类技术方案：
- 架构对比
- API 设计对比
- 适用场景对比 -->

{以表格形式说明与同类方案的全方位对比}

## 常见问题（FAQ）

- **Q：{问题1}**

  A：{回答1}

- **Q：{问题2}**

  A：{回答2}

## 争议与质疑

{争议与质疑}

## 相关资料

- [{网站名} - {文章标题}]({URL，必须能够正常访问}) - {简要描述}

``````

**If a section is not applicable to the specific topic, omit that entire section.** Do not add any sections beyond those listed in the template.

## Report Content Requirements

1. **Accuracy**: Every factual claim must be traceable to a verified source. Do not invent dates, version numbers, or statistics.
2. **Source Quality**: References must be to live, accessible URLs. Do not include 404 links. Prefer official documentation and reputable publications.
3. **Balance**: Present controversies and criticisms fairly. Do not advocate for or against the topic — let the evidence speak.
4. **Depth**: Go beyond surface-level descriptions. Explain *how* and *why*, not just *what*.
5. **Practicality**: Where applicable (tools, frameworks), include concrete installation steps, code examples, and real-world usage patterns.
6. **Currency**: For fast-evolving topics, prioritize recent information but acknowledge historical context.
7. **Language**: The report body must be in Chinese. Code examples, tool names, and proper nouns may remain in English.
8. **Formatting**: Mixed Chinese-English content must follow these rules:
    - Add spaces between Chinese characters and English words: `AI 模型` not `AI模型`
    - Use full-width punctuation in Chinese context: `“REST”是“Representational State Transfer”的缩写` not `"REST" 是 "Representational State Transfer" 的缩写`
    - Use `'`, `"`, `()` and so on in code examples or English text
    - Use `‘’`, `“”`, `（）` and so on in Chinese text for quotations
9. **Completeness**: Ensure all applicable sections from the template are populated. If information for a section is genuinely unavailable after exhaustive search, state so explicitly rather than omitting the section silently.
10. **Topic Type Distinction**: For ambiguous topics that could be both concept and product, or concept and technology:
    - At the start of the report, explicitly state the topic type classification
    - Label each section or subsection with `[概念]` or `[产品]` or `[技术]` when content mixes types
    - Never conflate different types under the same header
    - If a concept name overlaps with a product name (e.g., "Foo" could be a concept AND a product), keep them strictly separate — do not mix content from different types
    - If both exist and the user's intent is unclear, prioritize the more likely interpretation and note the ambiguity
11. **Origin Accuracy (CONCEPT TOPICS ONLY)**: When the topic is a concept:
    - The origin MUST be verified by checking the ACTUAL SEMANTIC CONTENT of the claimed origin source
    - **Temporal Priority Rule (CRITICAL)**: If Source A defines the concept earlier than Source B, then Source A is the confirmed origin — NOT Source B — even if Source B has 100x more citations or backlinks
    - **Reject citation count as origin evidence**: citations measure influence and propagation speed, NOT origin
    - **Semantic Confirmation (CRITICAL)**: The confirmed origin must discuss the **same domain/topic** as the research topic — not a homonym with the same name but different meaning
    - The origin is the FIRST publication that DEFINED or COINED the concept, not the first product that implemented it
    - If the origin is a personal blog post, academic paper, or conference talk — cite it as the origin even if no products use that exact name
    - If multiple sources claim to be the origin, trace the semantic lineage: which came first, what did subsequent sources cite/build upon
    - Explicitly label which source is the "confirmed origin (YYYY-MM-DD)" and which are "named/popularized by" later sources

## Quality Checklist

Before finalizing any report (subagent report or final report), verify:

- [ ] All URLs in references are valid and accessible (not 404 or broken)
- [ ] The report follows the exact template format
- [ ] No section contains fabricated or unverified claims
- [ ] Controversial points present multiple sides fairly
- [ ] All facts are cross-verified through multiple authoritative sources
- [ ] Dates are verified by checking the actual page, not assumed from citations
- [ ] All external sources mentioned are formatted as valid hyperlinks