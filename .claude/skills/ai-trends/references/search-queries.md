# Search Query Keywords

This file defines the search keyword templates used in the broad search phase. Subagents replace `[MON YEAR]` with actual month and year (e.g., `May 2026`) and limit time range to the specified query time range.

For date-based filtering, use format: `after:YYYY-MM-DD before:YYYY-MM-DD`

## Core Queries

```text
AI model release [MON YEAR]
LLM open source release [MON YEAR]
AI agent framework SDK [MON YEAR]
AI hardware chip announcement [MON YEAR]
embodied AI robotics humanoid [MON YEAR]
AI safety alignment [MON YEAR]
AI regulation policy [MON YEAR]
anthropic openai google deepmind mistral meta AI news [MON YEAR]
AI funding acquisition [MON YEAR]
site:news.ycombinator.com AI [MON YEAR]
LLM engineering methodology best practices [MON YEAR]
AI paradigm shift [MON YEAR]
"beyond" OR "replacing" OR "is the new" engineering AI [MON YEAR]
AI terminology "what is" OR "introducing" [MON YEAR]
AI research paper arxiv [MON YEAR]
AI production reliability observability [MON YEAR]
LLM application architecture patterns [MON YEAR]
AI agent infrastructure orchestration [MON YEAR]
LLM production system design [MON YEAR]
AI developer workflow paradigm [MON YEAR]
LLM context engineering [MON YEAR]
LLM application architecture [MON YEAR]
site:news.ycombinator.com "engineering" "LLM" OR "AI agent" [MON YEAR]
site:zhihu.com "AI" OR "LLM" OR "Agent" [MON YEAR]
site:news.qq.com "AI" OR "LLM" OR "Agent" [MON YEAR]
"new paradigm" AI LLM [MON YEAR]
具身智能 机器人 最新 [MON YEAR]
国产 AI 芯片 发布 [MON YEAR]
中国 AI 政策 监管 [MON YEAR]
中国 AI 创业公司 融资 [MON YEAR]
大模型 价格 调整 [MON YEAR]
AI 行业 应用 落地 [MON YEAR]
中国 AI 开源模型 DeepSeek Qwen 千问 MiniMax GLM 智谱 最新进展 [MON YEAR]
```

## Concept Discovery Queries

Aimed at capturing emerging terms and paradigm shifts - concepts being named for the first time, not already established terms:

```text
"introducing" "new approach" AI LLM -"product launch" -"funding" [MON YEAR]
"what we call" AI engineering [MON YEAR]
"emerging pattern" AI agent [MON YEAR]
"a new paradigm" AI [MON YEAR]
"why we need" AI methodology [MON YEAR]
"is the new" engineering AI OR LLM [MON YEAR]
"beyond prompt engineering" [MON YEAR]
"prompt engineering" ("context engineering" OR "next" OR "beyond" OR "replacing" OR "evolved into") AI OR LLM [MON YEAR]
"Agent = Model +" OR "model + " (scaffold OR layer OR system OR infrastructure) [MON YEAR]
"the missing layer" OR "new layer" OR "new discipline" OR "new engineering" (AI OR LLM) [MON YEAR]
"rise of" OR "era of" OR "year of" engineering (AI OR LLM) [MON YEAR]
site:latent.space [MON YEAR]
site:martinfowler.com AI [MON YEAR]
site:philschmid.de "new" [MON YEAR]
site:blog.langchain.com [MON YEAR]
site:news.ycombinator.com "what is" AI [MON YEAR]
site:reddit.com/r/LocalLLaMA "has anyone tried" [MON YEAR]
site:reddit.com/r/MachineLearning "new technique" [MON YEAR]
site:reddit.com/r/MachineLearning "what do you call" [MON YEAR]
"what is" ("engineering" OR "paradigm") (AI agent OR LLM) [MON YEAR]
```