# 检索查询集合

本文件是**按需调用**的查询库，不是每次执行都要跑完的清单。

执行规则见 `SKILL.md` 第 2 节：已知来源优先用 `scripts/collect.py` 直接抓取；只有出现明确缺口时，才从下面按需取用。标准模式下缺口查询不超过 `budgets.json` 中的 `max_discovery_queries`（标准档为 12），概念发现查询不超过 6 条。

时间过滤统一使用 `after:YYYY-MM-DD before:YYYY-MM-DD`，其中 `before` 取结束日期的下一天，避免漏掉当日内容。

---

## 一、缺口查询集（标准模式最多 12 条）

只有在脚本采集后确认存在缺口时才使用，每条查询必须写明要填补的缺口。

| 编号 | 查询模板 | 适用缺口 |
| ---- | -------- | -------- |
| G1 | `AI model release {MON YEAR}` | 官方索引未覆盖的模型发布 |
| G2 | `LLM open weights release {MON YEAR}` | 开放权重模型遗漏 |
| G3 | `AI agent framework SDK release {MON YEAR}` | Agent 框架与 SDK 变更 |
| G4 | `AI chip GPU datacenter announcement {MON YEAR}` | 算力与芯片发布 |
| G5 | `embodied AI robot humanoid deployment {MON YEAR}` | 具身智能落地事件 |
| G6 | `AI safety incident report {MON YEAR}` | 安全事故与评测披露 |
| G7 | `AI regulation policy law {MON YEAR}` | 监管与立法进展 |
| G8 | `AI funding acquisition IPO {MON YEAR}` | 融资、并购与上市 |
| G9 | `大模型 发布 开源 {MON YEAR}` | 中文模型发布 |
| G10 | `具身智能 机器人 政策 落地 {MON YEAR}` | 中文机器人产业与政策 |
| G11 | `中国 AI 芯片 算力 训练 {MON YEAR}` | 国产算力与训练进展 |
| G12 | `AI terminology "introducing" OR "what is" {MON YEAR}` | 新概念线索 |

定向补充（只针对已知域名，不再做泛搜索）：

```text
site:news.ycombinator.com "engineering" LLM
site:github.com "agent" "skills" release
site:arxiv.org "agent" "harness"
```

---

## 二、概念发现查询（最多 6 条，仅在筛选代理认为必要时使用）

概念发现的目标是找到“被命名的方法”，不是找所有新词。优先用少量宽查询，再由筛选代理判断。

```text
"introducing" "new approach" AI LLM -"product launch" -"funding"
"beyond prompt engineering" OR "context engineering" AI
"what we call" AI engineering
"a new paradigm" AI agent
"is the new" engineering AI OR LLM
"the missing layer" OR "new discipline" (AI OR LLM)
```

概念候选进入验证阶段后，才按 `references/term-detection.md` 的反向搜索规则做定向核查。

---

## 三、扩展查询库（仅 `deep` 模式或逐周轮换使用）

标准模式下不要执行本节。`deep` 模式下按轮换分组选取，总量仍受 `max_discovery_queries` 约束。

### 模型与算力

```text
AI hardware chip announcement {MON YEAR}
LLM inference price change {MON YEAR}
AI model benchmark leaderboard {MON YEAR}
```

### 生态与工程

```text
LLM engineering methodology best practices {MON YEAR}
LLM context engineering {MON YEAR}
LLM application architecture {MON YEAR}
AI agent infrastructure orchestration {MON YEAR}
LLM production system design {MON YEAR}
AI production reliability observability {MON YEAR}
AI developer workflow paradigm {MON YEAR}
```

### 社区与社区讨论

```text
site:news.ycombinator.com "what is" AI
site:reddit.com/r/LocalLLaMA "has anyone tried"
site:reddit.com/r/MachineLearning "new technique"
site:reddit.com/r/vibecoding
site:zhihu.com AI Agent 工程
site:v2ex.com AI 模型
```

### 专题博客轮换

```text
site:latent.space
site:martinfowler.com AI
site:philschmid.de
site:blog.langchain.com
site:simonwillison.net
site:newsletter.pragmaticengineer.com
```

### 中文生态

```text
中国 AI 创业公司 融资 {MON YEAR}
大模型 价格 调整 {MON YEAR}
AI 行业 应用 落地 {MON YEAR}
中国 AI 开源模型 DeepSeek Qwen 千问 MiniMax GLM 智谱 最新进展 {MON YEAR}
中国 AI 政策 监管 {MON YEAR}
```
