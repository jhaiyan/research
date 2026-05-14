# LLM 和 Coding Agents 比较

> **报告生成日期**：2026年05月19日<br>
> **检索数据源**：共分析 14 个网站和文章，涵盖官方文档、基准测试平台、技术媒体、开发者社区及学术来源；数据源通过最多 3 层爬取动态发现
>
> 2026 年编程 LLM 市场竞争激烈，GPT-5.5 系列以 Intelligence Index 60 分领先全场，Claude Opus 4.7 以 57 分紧随其后。Gemini 3.1 Pro、DeepSeek R1、Kimi K2.6 等模型在编码基准测试中表现优异。开源模型如 Llama 4 Scout（10M 上下文）、GLM-5（代码生成 SOTA）持续缩小与闭源模型的差距。
>
> 主流模型普遍具备 1M token 上下文窗口，多模态能力成为标配。o1/o3/o4 等推理模型在数学和代码任务上表现突出。
>
> AI 编码 Agent 领域呈现 "Claude Code + Cursor" 双雄争霸格局。Claude Code 以 4.7 分领先全场，在 Repo 理解、长周期任务、并行子代理等方面优势明显。Cursor v3.4/Composer 2.5 以 4.5-4.6 分排名第二，支持多模型和云端 Agent。开源工具 Aider（3.6-4.2）在代码生成基准测试中表现优异，支持 200+ 模型。

## LLM 比较

| 制造商 | 模型 | 场景 | 上下文大小 | 最大输入 | 最大输出 | 推理能力 | 数学能力 | 编程能力 | 视觉能力 | 指令遵循 | 幻觉控制 | 多语言 | 长上下文有效性 | JSON/Tool Call | 开源 | 成本 | 综合评价 | 适用场景 |
| :----- | :--- | :--- | ---------: | -------: | -------: | :------: | :------: | :------: | :------: | :------: | :------: | :----: | :-------------: | :-------------: | :--: | :--: | ------: | :----- |
| [OpenAI](https://openai.com) | [GPT-5.5 (xhigh)](https://platform.openai.com/docs/models) | API | 922K | - | - | ⚫️ | ⚫️ | ⚫️ | 🟠 | ⚫️ | ⚫️ | ⚫️ | ⚫️ | ⚫️ | ❌ | 🔴 | 5.0 | 代码生成、复杂推理、前沿智能 |
| [Anthropic](https://www.anthropic.com) | [Claude Opus 4.7](https://docs.anthropic.com/en/docs/about-claude/models) | API | 1M | 1M | 128K | ⚫️ | ⚫️ | ⚫️ | ⚫️ | ⚫️ | ⚫️ | ⚫️ | ⚫️ | ⚫️ | ❌ | 🟠 | 4.9 | 复杂推理、代码生成、长任务 Agent |
| [Google DeepMind](https://deepmind.google) | [Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models) | API | 1M | - | - | ⚫️ | ⚫️ | ⚫️ | ⚫️ | ⚫️ | 🟠 | ⚫️ | ⚫️ | 🔴 | ❌ | 🟠 | 4.8 | 多模态理解、长上下文推理 |
| [OpenAI](https://openai.com) | [o3](https://platform.openai.com/docs/models) | Thinking (API) | 128K | 128K | 32K | ⚫️ | ⚫️ | ⚫️ | - | 🟠 | 🟠 | 🟡 | ⚫️ | 🟠 | ❌ | 🔴 | 4.6 | 复杂推理、数学问题解决 |
| [Anthropic](https://www.anthropic.com) | [Claude Sonnet 4.6](https://docs.anthropic.com/en/docs/about-claude/models) | API | 1M | 1M | 64K | ⚫️ | 🔴 | ⚫️ | 🟠 | ⚫️ | ⚫️ | ⚫️ | ⚫️ | ⚫️ | ❌ | 🟡 | 4.6 | 平衡智能与速度、代码开发 |
| [深度求索](https://www.deepseek.com) | [DeepSeek R1](https://www.deepseek.com) | API | 128K | 128K | 32K | ⚫️ | ⚫️ | 🔴 | - | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | ❌ | ⚪️ | 4.5 | 数学推理、代码生成、复杂推理 |
| [xAI](https://x.ai) | [Grok 4.3](https://x.ai/api) | API | 2M | - | - | 🔴 | 🔴 | 🔴 | 🟠 | 🟠 | 🟠 | 🟡 | 🔴 | 🟠 | ❌ | 🟡 | 4.6 | 超长上下文、实时推理 |
| [Moonshot AI](https://www.moonshot.cn) | [Kimi K2.6](https://www.moonshot.cn) | API | 256K | 256K | 32K | 🔴 | 🔴 | 🔴 | ⚫️ | 🟠 | 🟠 | 🔴 | 🔴 | 🟠 | ❌ | 🟡 | 4.5 | 代码生成、多模态 Agent、长程任务 |
| [Meta AI](https://www.llama.com) | [Llama 4 Scout](https://www.llama.com) | 开源权重 | 10M | 10M | 32K | 🟠 | 🟡 | 🟡 | 🟠 | 🟠 | 🟠 | ⚫️ | ⚫️ | 🟠 | ✅ | 🟡 | 4.5 | 超长上下文、开源部署 |
| [Google DeepMind](https://deepmind.google) | [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models) | API | 1M | - | - | 🔴 | 🔴 | 🔴 | ⚫️ | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | ❌ | 🟡 | 4.4 | 多模态推理、复杂编码 |
| [深度求索](https://www.deepseek.com) | [DeepSeek V4](https://api-docs.deepseek.com) | API | 1M | 1M | 384K | 🔴 | 🔴 | 🔴 | 🟡 | 🟠 | 🟠 | 🟠 | ⚫️ | 🟠 | ❌ | 🟡 | 4.4 | 超长上下文、复杂推理 |
| [智谱](https://www.zhipuai.cn) | [GLM-5](https://www.zhipuai.cn) | API | 200K | 200K | 32K | 🔴 | 🔴 | 🔴 | 🟠 | ⚫️ | 🟠 | 🟠 | 🟠 | 🟠 | ✅ | 🟡 | 4.4 | 代码生成、开源 SOTA、Agent 编程 |
| [Anthropic](https://www.anthropic.com) | [Claude Opus 4.7](https://www.anthropic.com/claude/opus) | Thinking | 1M | 1M | 200K | ⚫️ | ⚫️ | ⚫️ | 🟠 | ⚫️ | ⚫️ | ⚫️ | ⚫️ | ⚫️ | ❌ | 🔴 | 4.8 | 复杂推理、代码生成、智能体 |
| [Mistral AI](https://mistral.ai) | [Mistral Large 3](https://docs.mistral.ai/getting-started/models/) | API | 128K | 128K | 32K | 🔴 | 🟠 | 🔴 | ⚫️ | 🔴 | 🟠 | 🟠 | 🟠 | 🔴 | ✅ | 🟠 | 4.2 | 开源多模态、代码生成 |
| [Mistral AI](https://mistral.ai) | [Devstral 2](https://mistral.ai/news/devstral) | API | 128K | 128K | 32K | 🟡 | 🟡 | ⚫️ | - | 🟠 | 🟠 | 🟠 | 🟠 | 🟡 | ✅ | ⚪️ | 4.2 | 代码 Agent、SWE-bench、软件工程 |
| [Anthropic](https://www.anthropic.com) | [Claude Haiku 4.5](https://www.anthropic.com/claude/haiku) | API | 128K | 128K | 32K | 🟠 | 🟠 | 🟠 | 🟡 | 🟠 | 🟠 | 🟠 | 🟡 | 🟠 | ❌ | 🟡 | 3.8 | 快速推理、轻量级任务 |
| [Mistral AI](https://mistral.ai) | [Mistral Small 4](https://mistral.ai/news/mistral-small-4) | API | 256K | 256K | 32K | 🟠 | 🟠 | 🟠 | - | 🟠 | 🟠 | 🟠 | 🟠 | 🟡 | ✅ | 🟡 | 4.0 | 代码生成、推理任务 |
| [阿里云](https://qwenLM.github.io) | [Qwen3](https://qwenLM.github.io) | 开源权重 | 131K | 131K | 32K | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | ⚫️ | 🟠 | 🟠 | ✅ | ⚪️ | 4.1 | 多语言、代码生成、指令遵循 |
| [Cerebras](https://www.cerebras.ai) | [Codex-Spark](https://www.cerebras.ai) | API | 128K | 128K | 32K | 🟠 | 🟡 | 🔴 | - | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | ❌ | ⚪️ | 3.5 | 极速代码生成 |

## Coding Agents 比较

| 制造商 | Agent | 第三方模型 | Repo 理解 | 批量重构 | 自我纠错 | 长周期任务 | 工程能力 | Git 工作流 | 上下文压缩 | 记忆管理 | 并行子代理 | 工具调用 | 安全性 | 灵活性 | 成本控制 | 综合评价 | 强项 | 弱项 |
| :----- | :---- | :--------: | :-------: | :------: | :------: | :--------: | :------: | :--------: | :--------: | :------: | :--------: | :------: | :----: | :----: | :------: | ------: | :--- | :--- |
| [Anthropic](https://www.anthropic.com) | [Claude Code](https://code.claude.com) | ✅ | 🔴 | 🔴 | 🟠 | ⚫️ | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🟠 | 4.7 | 大型 Repo 分析、多文件重构、MCP 集成 | CLI 界面、学习曲线 |
| [Anysphere](https://www.cursor.com) | [Cursor 3.4](https://www.cursor.com) | ✅ | 🔴 | 🔴 | 🟠 | 🔴 | 🔴 | 🟠 | 🔴 | 🟠 | 🟠 | 🔴 | 🟠 | 🔴 | 🟠 | 4.6 | Composer 2.5 云端代理、实时协作 | 定价偏高、封闭生态 |
| [Replit](https://replit.com) | [Replit Agent 4](https://replit.com) | ✅ | 🟠 | 🔴 | 🟠 | 🔴 | 🟠 | 🟠 | 🟡 | 🟡 | 🔴 | 🟠 | 🟡 | 🟠 | 🟠 | 4.0 | 并行代理、内置基建、100+ 集成 | 平台锁定、成本较高 |
| [Aider](https://aider.chat) | [Aider 0.86.0](https://aider.chat) | ✅ | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🔴 | 🟠 | 🟡 | ❌ | 🟠 | 🔴 | 🔴 | ⚫️ | 4.2 | 终端编程、100+ 语言支持、Git 集成 | 非图形界面 |
| [GitHub](https://github.com) | [GitHub Copilot](https://github.com/features/copilot) | ✅ | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🔴 | 🟠 | 🟠 | ❌ | 🟠 | 🟠 | 🟠 | 🟠 | 4.0 | IDE 深度集成、Git 工作流强大 | Agent 能力有限、成本控制难 |
| [OpenAI](https://openai.com) | [Codex CLI](https://github.com/openai/codex) | ✅ | 🟠 | 🟡 | 🟡 | 🟡 | 🟡 | 🟠 | 🟡 | 🟡 | ❌ | 🟠 | 🟠 | 🟡 | 🟡 | 3.4 | 轻量 CLI、ChatGPT 集成 | 功能单一、非桌面端专用 |
| [Sourcegraph](https://sourcegraph.com) | [Cody](https://sourcegraph.com/cody) | ✅ | 🔴 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🔴 | 🟡 | ❌ | 🟡 | 🟠 | 🟠 | 🟡 | 3.3 | 全代码库上下文、Search API 集成 | Enterprise 依赖、功能分散 |
| [Tabnine](https://www.tabnine.com) | [Tabnine Enterprise](https://www.tabnine.com) | ✅ | 🟠 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟠 | 🟡 | ❌ | 🟡 | 🔴 | 🟠 | 🟠 | 3.3 | 隐私优先、零数据保留、air-gapped | 定价高、Agent 能力有限 |
| [Continue](https://continue.dev) | [Continue 1.2.22](https://continue.dev) | ✅ | 🟠 | 🟡 | 🟡 | 🟡 | 🟡 | 🔴 | 🟡 | 🟡 | ❌ | 🟡 | 🔴 | 🟠 | 🟠 | 3.2 | 开源可扩展、PR 检查集成 | 功能较单一、缺少 Agent 能力 |
| [Windsurf](https://windsurf.com) | [Windsurf 2.0](https://windsurf.com) | ✅ | 🟠 | 🟡 | 🟡 | 🟠 | 🟡 | 🟡 | 🟡 | 🟡 | ❌ | 🟡 | 🟡 | 🟡 | 🟡 | 3.1 | 本地+云端混合代理 | 文档有限、知名度低 |
| [JetBrains](https://www.jetbrains.com) | [Junie](https://blog.jetbrains.com/junie/) | ✅ | 🟠 | 🟡 | 🟡 | 🟠 | 🟡 | 🟡 | 🟡 | 🟡 | ❌ | 🟡 | 🟠 | 🟡 | 🟡 | 3.0 | LLM-agnostic、IDE 深度集成 | Beta 阶段、功能待完善 |
| [Lovable](https://lovable.dev) | [Lovable](https://lovable.dev) | ❓ | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | ❌ | 🟡 | 🟡 | 🟠 | 🟡 | 2.8 | 快速原型、无代码构建 | 非开发者工具、深度弱 |
| [Vercel](https://vercel.com) | [v0](https://v0.app) | ❓ | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | ❌ | 🟡 | 🟡 | 🟠 | 🟡 | 2.7 | 快速部署、前端专精 | 前端局限、非通用工具 |
| [JetBrains](https://www.jetbrains.com) | [AI Assistant](https://www.jetbrains.com/ai) | ❌ | 🟠 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | ❌ | 🟡 | 🟠 | 🟡 | 🟡 | 2.6 | JetBrains 生态集成 | 功能基础、非独立产品 |
| [字节跳动](https://www.bytedance.com) | [Trae](https://trae.ai) | ❌ | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | ❌ | 🟡 | 🟡 | 🟡 | 🟡 | 2.3 | 中文界面、ByteDance 生态 | 资料稀缺、国际认可度低 |
| [百度](https://www.baidu.com) | [Comate](https://comate.baidu.com) | ❌ | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | ❌ | 🟡 | 🟡 | 🟡 | 🟡 | 2.2 | 中文生态、ERNIE 集成 | 资料稀缺、国际化弱 |
| [OpenAI](https://openai.com) | [ChatGPT (coding mode)](https://chatgpt.com) | ❌ | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | ❌ | 🟡 | 🟡 | 🟡 | 🟠 | 2.5 | 通用对话、多模态 | 非专业 IDE、上下文有限 |

## 附录：数据来源

- [Artificial Analysis Models](https://artificialanalysis.ai/models) - Intelligence Index 评分、模型排名、360+ 模型评估
- [Artificial Analysis Leaderboards](https://artificialanalysis.ai/leaderboards/models) - Intelligence Index Elo 评分系统
- [Aider Leaderboard](https://aider.chat/docs/leaderboards/) - 编程基准测试、GPT-5 88.0% 准确率
- [Claude Code 文档](https://code.claude.com/docs) - 完整功能列表、MCP、sub-agents、git 集成
- [Cursor 官网](https://www.cursor.com) - Composer 2.5 (May 18, 2026)、v3.4 (May 13, 2026)
- [Cursor Changelog](https://www.cursor.com/changelog) - 版本历史、并行执行
- [Anthropic Claude Models](https://docs.anthropic.com/en/docs/about-claude/models) - Claude 全系列定价、上下文、API ID
- [Google Gemini API Docs](https://ai.google.dev/gemini-api/docs/models) - Gemini 3/2.5 系列模型列表
- [DeepSeek API Docs](https://api-docs.deepseek.com) - DeepSeek V4/V3/R1 定价
- [Mistral AI Models](https://docs.mistral.ai/getting-started/models/) - Mistral 全系列模型概述
- [xAI API](https://x.ai/api) - Grok 模型 API 信息
- [Moonshot AI](https://www.moonshot.cn) - Kimi K2.6 规格
- [Llama Website](https://www.llama.com) - Llama 4 Scout/Maverick 上下文、定价
- [Zhipu AI](https://www.zhipuai.cn) - GLM-5 规格、开源 SOTA 声明
- [Replit Agent](https://replit.com/agent) - Agent 4 功能详情
- [Aider GitHub](https://github.com/Aider-AI/aider) - 44k stars、版本 0.86.0
- [Continue GitHub](https://github.com/continuedev/continue) - 33.3k stars、版本 1.2.22
- [Tabnine Enterprise](https://www.tabnine.com/enterprise) - 企业隐私功能
- [GitHub Copilot](https://github.com/features/copilot) - 功能列表、定价
- [OpenAI Codex CLI](https://github.com/openai/codex) - 83.8k stars、版本 0.131.0