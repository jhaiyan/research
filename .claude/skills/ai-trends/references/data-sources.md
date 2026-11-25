# 数据源分层与轮换规则

本文件用于**人工维护**来源清单。常规运行不执行来源清理，采集清单以 `.claude/skills/ai-trends/sources.json` 为准，本文件解释分层理由、覆盖范围与已知失效来源。

## 分层定义

| 层级 | 定义 | 运行策略 |
| ---- | ---- | -------- |
| A | 官方实验室公告、原始论文与预印本、监管与政府文件、代码仓库、权威榜单 API | 每次运行都采集 |
| B | 权威科技媒体、重要社区、知名中文媒体 | 每次运行选取预算内的一组，逐周轮换 |
| C | 个人博客、聚合站、二手解读、垂直小站 | 仅在出现明确缺口时手工抓取，或只作线索 |

## 运行策略

1. `scripts/collect.py` 默认启用 A 层；B 层按 `sources.json` 中 `tier` 字段与轮换表选择；C 层不进入自动采集。
2. B 层每周轮换，规则见下方轮换表；同一事件若已在 A 层出现，不再从 B 层重复验证。
3. C 层来源只能作为线索，不得作为唯一来源；报告中引用前必须回溯到 A 层或独立可靠来源。
4. 单一域名连续失败达到 `failure_circuit_breaker` 次后跳过，避免无效重试。
5. 新的权威来源先记入报告的「新发现的数据源」一节，人工复核后再并入 `sources.json`。

---

## A 层：官方与原始来源

### 实验室与产品公告

| 来源 | 地址 | 覆盖内容 |
| ---- | ---- | ---- |
| Anthropic News | <https://www.anthropic.com/news> | Claude 发布、安全研究、企业合作 |
| OpenAI News | <https://openai.com/news/> | GPT 发布、公司公告 |
| OpenAI 失准事故索引 | <https://openai.com/safety-alignment/misalignment-reports/> | Agent 对齐事故公开记录 |
| Google DeepMind Blog | <https://deepmind.google/blog/> | Gemini、世界模型、Alpha 系列研究 |
| Google Blog AI | <https://blog.google/technology/ai/> | 产品公告与模型发布 |
| Hugging Face Blog | <https://huggingface.co/blog> | 开放模型与工程实践 |
| NVIDIA Newsroom | <https://nvidianews.nvidia.com/news> | 公司公告与治理事件 |
| NVIDIA Developer Blog | <https://blogs.nvidia.com/blog/category/deep-learning/> | 硬件与推理优化 |
| Thinking Machines Lab | <https://thinkingmachines.ai/> | 模型架构与训练方法一手说明 |
| Z.ai Blog | <https://z.ai/blog/glm-5.4> | GLM 系列模型发布 |
| Mistral AI News | <https://mistral.ai/news/> | 模型与商业合作 |
| Meta 工程博客 | <https://engineering.fb.com/> | 开源研究与系统实践；`ai.meta.com/blog` 拒绝自动化访问，需手工抓取 |

### 论文与榜单

| 来源 | 地址 | 说明 |
| ---- | ---- | ---- |
| arXiv API | <https://export.arxiv.org/api/query> | 按分类与提交时间检索 cs.AI、cs.LG、cs.CL |
| Hugging Face Papers | <https://huggingface.co/papers> | 社区精选论文 |
| LMSYS Chatbot Arena | <https://lmarena.ai> | 人类偏好榜单 |
| OpenCompass | <https://opencompass.org.cn> | 中文模型评测 |
| Papers With Code | <https://paperswithcode.com/latest> | 论文与实现 |

### 社区与代码

| 来源 | 地址 | 说明 |
| ---- | ---- | ---- |
| Hacker News（Algolia API） | <https://hn.algolia.com/api/v1/search> | 按时间与分数检索讨论，含标题、分数、评论数与讨论 ID |
| GitHub Trending | <https://github.com/trending?since=weekly> | 周榜与月榜，配套仓库 API 核实 Stars |
| GitHub REST API | <https://api.github.com/repos/{owner}/{repo}> | 仓库元数据与最近提交 |

### 政策与治理

| 来源 | 地址 | 说明 |
| ---- | ---- | ---- |
| California Government Operations Agency | <https://www.govops.ca.gov/> | 加州 AI 治理报告原文 |
| 北京市政府门户 | <https://english.beijing.gov.cn/> | 产业行动计划原文 |
| 工信部政策文件 | <https://www.miit.gov.cn/> | 产业与网络接入规范 |
| 美国 SEC EDGAR | <https://www.sec.gov/cgi-bin/browse-edgar> | 上市与并购原始文件 |
| IETF Datatracker | <https://datatracker.ietf.org/> | 协议与标准草案 |

---

## B 层：媒体、社区与中文生态

每次运行按预算选取，轮换表如下：

| 轮换周 | 英文媒体与研究 | 中文媒体 | 社区 |
| -------- | -------------- | -------- | ---- |
| 第 1 周 | TechCrunch AI、VentureBeat AI | 量子位、钛媒体 | Hacker News、V2EX |
| 第 2 周 | The Decoder、The New Stack | 机器之心、36氪 | Hacker News、OSChina |
| 第 3 周 | The Register、MIT Technology Review | 财新、证券时报 | Hacker News、V2EX |
| 第 4 周 | The Batch、Import AI | 智东西、xix.ai | Hacker News、OSChina |

固定补充源：[Berkeley News](https://news.berkeley.edu/)、[IEEE Spectrum](https://spectrum.ieee.org/)、[VentureBeat AI](https://venturebeat.com/ai/) 与 [TechCrunch AI](https://techcrunch.com/category/artificial-intelligence/) 始终保留在 B 层候选中。

---

## C 层：按需来源

以下来源仅在明确缺口时手工抓取，不得作为唯一来源：

- 个人博客：[Simon Willison](https://simonwillison.net)、[Martin Fowler](https://martinfowler.com)、[Chip Huyen](https://huyenchip.com)、[Philipp Schmid](https://www.philschmid.de)、[Mitchell Hashimoto](https://mitchellh.com/writing)、[Addy Osmani](https://addyosmani.com/)
- 聚合与解读：i-Scoop、The Deep Feed、AI Papers Academy、ApplyData、ExplainX、Loop Engineering、Skillenai、BestHub、Agno、PromptFluent
- 投资与市场：Tracxn、Black Matter VC、Predictive Ventures、Not Boring
- 中文：VibeVibe、AgentScout、KeyLinking、GitCode

---

## 已知失效或降级来源

| 来源 | 状态 | 处理 |
| ---- | ---- | ---- |
| Qwen LM Blog | 长期停更 | 改用 Qwen 官方文档与模型卡 |
| 同步科技 SyncedReview | 2025 年 8 月后停更 | 移除 |
| CSDN AI 频道 | 无有效内容 | 移除 |
| AgentScout | 内容停留在 2026 年 7 月 | 降级至 C 层 |
| karpathy.ai | 站点为空 | 移除 |
| lilianweng.github.io | 2025 年 5 月后停更 | 移除 |
| blog.keras.io | 2018 年后停更 | 移除 |
| ai.meta.com/blog | 拒绝自动化访问，返回 400 | 改用 Meta 工程博客，必要时手工抓取 |
| arXiv 列表与 API | 常见超时，需更长的请求超时 | 采集脚本对 arXiv 使用三倍超时；仍失败时用 WebFetch 抓取摘要页 |
| Berkeley News、The New Stack | 对脚本返回 403 | 保留在清单内，由 WebFetch 补抓；失败则记入覆盖缺口 |

---

## 维护规则

1. 每季度复核一次 A 层与 B 层来源的可达性与更新频率，维护动作不在常规简报运行内。
2. 新来源并入前必须满足：可访问、当年有更新、主题相关、信噪比可接受。
3. 同一机构的多个栏目合并为一条，避免重复采集。
4. 出现某域名在引用链中重复出现 3 次以上时，先记入报告的「新发现的数据源」，人工确认后再并入。
