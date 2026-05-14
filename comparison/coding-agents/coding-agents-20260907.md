# LLM 和 Coding Agents 比较

> **报告生成日期**：2026年09月07日<br>
> **检索数据源**：共分析 88 个独立网站和文章，涵盖 Tier-1 基准平台（Artificial Analysis、Vellum、SWE-bench、Aider、ProgramBench、Steel.dev、Terminal Bench）、官方厂商文档（Anthropic、OpenAI、Google DeepMind、xAI、Meta、Mistral、Cohere、Amazon、NVIDIA、智谱、月之暗面、阿里云、深度求索、字节跳动、JetBrains、Sourcegraph、StackBlitz、Warp、SST、Kilo 等）、Tier-2 聚合平台（BenchLM、LLM Stats、ModelGrep、LLM Podium、DataLearner）以及 T3/T4 技术媒体与开发者社区；数据源以 Tier-1 种子源为主，按需补充动态检索结果；最大爬取深度 1（不进行多层级扩散），每源最多取 Top 20。
>
> 2026 年 9 月编程大模型格局呈现"前沿领先 + 开源崛起"双轨态势：Anthropic Claude Opus 5 在 SWE-bench Verified（Vals.ai 独立测量 97.00% [🔗](https://leaderboard.steel.dev/leaderboards/swe-bench-verified "Steel.dev SWE-bench Verified")）与 ProgramBench（4.5% Resolved，#1 [🔗](https://programbench.com/ "ProgramBench")）继续保持榜首，Claude Fable 5.1 与 Claude Mythos 5.1 在 Artificial Analysis Intelligence Index 包揽前三 [🔗](https://artificialanalysis.ai/models "Artificial Analysis Models")；OpenAI 以 GPT-6 Astra（AA #3）、GPT-5.6 Sol（Vellum Agentic Coding #1 96.2% [🔗](https://www.vellum.ai/llm-leaderboard "Vellum LLM Leaderboard")）与 GPT-5.6 Pro（LMArena 6 月快照 #1 ~1465 Elo [🔗](https://presenc.ai/research/chatbot-arena-elo-leaderboard-june-2026 "Presenc AI LMSYS Arena 月度快照")）形成高、中、低三档全覆盖；中国阵营 Kimi K3 拿下开放权重综合榜首（AA Intelligence Index 50），Qwen3.8-Max（2.4T 总参数 / 95B 激活 MoE）与 DeepSeek V4 Pro 0813（Steel.dev 独立 SWE-bench Verified 96.4%，开源权重最高）紧贴前沿 [🔗](https://www.tryfriday.ai/blog/kimi-k3-benchmarks-pricing-context-window "Friday AI Kimi K3 Benchmarks") [🔗](https://www.alibabagroup.com/document-2021044032125272064 "Alibaba Group Qwen3.8-Max") [🔗](https://labindex.ai/outputs/deepseek/deepseek-v4-pro "LabIndex DeepSeek-V4-Pro-0813")。
>
> 视觉、长上下文、工具调用能力继续成为分水岭：Gemini 3.2 Pro 在视觉维度取得行业领先分数，Anthropic 与 OpenAI 全系列已原生支持 1M 级上下文；定价方面，GPT-5、Llama 4 Scout（自部署）与 Nemotron 系列凭借开源或低价占据"成本优势"端，o3-pro 仍为单 token 价格最高档。Claude Mythos 5/5.1 通过 Anthropic Glasswing 计划向受邀机构开放，定位网络安全、生命科学等双用敏感任务。
>
> 2026 年 9 月 AI 编程 Agent 格局经历重大重组：SpaceX 于 2026-08-14/15 完成对 Anysphere（Cursor）的 $60B 收购，Cursor 成为 SpaceXAI 全资子公司 [🔗](https://cursor.com/changelog "Cursor 官方 changelog")；Cognition 于 2026-06-02 将 Windsurf 正式更名为 Devin Desktop，并以 Claude Opus 5 为默认后端在 SWE-bench Verified 持续领跑 [🔗](https://cognition.com/blog/devin-2 "Devin 2 官方博客")；Anthropic 以 Claude Code 2.x 独立抗衡，凭借 Sub-agents 并行编排与 MCP 工具生态占据终端 Agent 领先位置 [🔗](https://code.claude.com/docs/en/overview "Claude Code 官方文档")。
>
> 同时国产与开源力量加速追赶：阿里云 Qoder CN（原通义灵码 2026 重塑版）以 Quest 自主任务委托与 Repo Wiki 进入综合前五 [🔗](https://qoder.com "Qoder 国际版")；opencode（Anomalyco fork，175K+ stars）以 75+ 模型提供商中立性与 Plan/Build 双模式安全机制成为开源代表 [🔗](https://opencode.ai "opencode.ai 官方")；Cline CLI 2.0 通过 Memory Bank、Agent Teams 与 Durable Session 在企业场景崭露头角 [🔗](https://cline.bot "Cline 官网")。补全、交互式 Agent、云端 Agent 三类形态的边界进一步模糊。

## LLM 比较

| 制造商 | 模型 | 场景 | 上下文<br>大小 | 最大<br>输入 | 最大<br>输出 | 推理<br>能力 | 数学<br>能力 | 编程<br>能力 | 视觉<br>能力 | 指令<br>遵循 | 幻觉<br>控制 | 多语言 | 长上下文<br>有效性 | JSON/<br>Tool Call | 开源 | 成本 | 综合<br>评价 | 适用场景 |
| :----- | :--- | :--- | -------------: | -----------: | -----------: | :----------: | :----------: | :----------: | :----------: | :----------: | :----------: | :----: | :----------------: | :----------------: | :--: | :--: | ----------: | :------- |
| [Anthropic](https://www.anthropic.com "Anthropic 官方网站") | [Claude Opus 5](https://www.anthropic.com/claude/opus "Claude Opus 5 模型页") | API | 1M | 1M | 128K | 10 | 10 | 10 | 9 | 10 | 10 | 8 | 10 | 10 | ❌ | 7 | 10 | 复杂编程、深度代理、代码审查、企业级智能体 |
| [Anthropic](https://www.anthropic.com "Anthropic 官方网站") | [Claude Fable 5.1](https://www.anthropic.com/claude/fable "Claude Fable 5.1 模型页") | API（Max Effort，1M 上下文） | 1M | 1M | 128K | 10 | 10 | 8 | 9 | 10 | 10 | 10 | 10 | 10 | ❌ | 3 | 10 | 深度知识工作、长时程代理、复杂多阶段任务、科研计算 |
| [Anthropic](https://www.anthropic.com "Anthropic 官方网站") | [Claude Mythos 5.1](https://www.anthropic.com/claude/mythos "Claude Mythos 5.1 模型页") | API（Glasswing 限定访问） | 1M | 1M | 128K | 10 | 10 | 8 | 9 | 10 | 10 | 8 | 10 | 10 | ❌ | 3 | 10 | 网络安全、生命科学等双用敏感任务（仅受邀机构） |
| [Anthropic](https://www.anthropic.com "Anthropic 官方网站") | [Claude Mythos 5](https://www.anthropic.com/claude/mythos "Claude Mythos 5 模型页") | API（Glasswing 限定访问） | 200K | 200K | 32K | 8 | 10 | 8 | 9 | 7 | 10 | 8 | 8 | 10 | ❌ | 3 | 8 | 安全/生命科学研究、长上下文代理、多步骤推理 |
| [OpenAI](https://openai.com "OpenAI 官方网站") | [GPT-6 Astra](https://developers.openai.com/api/docs/models "OpenAI API Models") | API（max effort，1.05M 上下文） | 1.05M | 1.05M | 128K | 10 | 10 | 8 | 9 | 10 | 10 | 10 | 10 | 10 | ❌ | 3 | 8 | 端到端最难任务、代理、Web 开发、深度研究 |
| [OpenAI](https://openai.com "OpenAI 官方网站") | [GPT-5.6 Sol](https://developers.openai.com/api/docs/models "OpenAI API Models") | API | 1.05M | 1.05M | 128K | 8 | 10 | 8 | 9 | 10 | 10 | 10 | 10 | 10 | ❌ | 8 | 8 | 软件工程代理、代码生成、终端操作、网页浏览 |
| [月之暗面](https://www.moonshot.cn "月之暗面 Kimi") | [Kimi K3](https://www.kimi.com "Kimi K3 官网") | API（max 思考） | 1M | 1M | 32K | 8 | 10 | 8 | 9 | 7 | 7 | 8 | 8 | 10 | ✅ | 8 | 8 | 长上下文编程、智能体任务、知识工作 |
| [OpenAI](https://openai.com "OpenAI 官方网站") | [GPT-5.6 Pro](https://openai.com "OpenAI 官方网站") | API | 1.05M | 1.05M | 128K | 8 | 10 | 7 | 9 | 10 | 10 | 10 | 10 | 10 | ❌ | 6 | 6 | 通用对话、高质量输出、长上下文推理 |
| [OpenAI](https://openai.com "OpenAI 官方网站") | [GPT-5](https://openai.com/gpt-5 "OpenAI GPT-5 介绍页") | API | 400K | 400K | 128K | 6 | 8 | 8 | 9 | 7 | 10 | 8 | 5 | 10 | ❌ | 10 | 6 | 高质量代码、推理、视觉，结构化输出，性价比高 |
| [OpenAI](https://openai.com "OpenAI 官方网站") | [o3-pro](https://openrouter.ai/openai/o3-pro "OpenRouter o3-pro") | API（强化学习推理） | 200K | 200K | 100K | 8 | 10 | 8 | 9 | 7 | 7 | 8 | 3 | 7 | ❌ | 1 | 6 | 深度推理、复杂多步规划、工具使用、PDF/图像 |
| [Google DeepMind](https://deepmind.google "Google DeepMind 官方网站") | [Gemini 3.2 Pro](https://deepmind.google "Google DeepMind Gemini") | API | 1M | 1M | 64K | 6 | 8 | 7 | 10 | 7 | 10 | 10 | 10 | 10 | ❌ | 8 | 6 | 多模态推理、长上下文、视频理解、代理 |
| [Google DeepMind](https://deepmind.google "Google DeepMind 官方网站") | [Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/pricing "Google AI Gemini Pricing") | API（Preview） | 1M | 1M | 64K | 6 | 8 | 7 | 10 | 7 | 10 | 10 | 10 | 10 | ❌ | 8 | 6 | 高级智能、代理、Vibe Coding、多模态 |
| [Anthropic](https://www.anthropic.com "Anthropic 官方网站") | [Claude Sonnet 4.6](https://www.anthropic.com/claude/sonnet "Claude Sonnet 4.6 模型页") | API（1M 上下文） | 1M | 1M | 64K | 4 | 5 | 5 | 9 | 7 | 10 | 8 | 10 | 7 | ❌ | 7 | 6 | 编码、代理、计算机使用、生产级高吞吐 |
| [深度求索](https://www.deepseek.com "深度求索 DeepSeek") | [DeepSeek V4 Pro 0813](https://www.deepseek.com "DeepSeek 官网") | API（Responses / Codex） | 1M | 1M | 384K | 6 | 8 | 7 | 8 | 7 | 7 | 8 | 8 | 10 | ✅ | 3 | 6 | 智能体编程、工具调用、长输出 |
| [阿里云](https://qwenlm.github.io "通义千问 Qwen") | [Qwen3.7-Max](https://www.alibabacloud.com "Qwen3.7-Max 阿里云") | API | 1M | 1M | 33K | 6 | 10 | 7 | 8 | 7 | 7 | 8 | 5 | 7 | ❌ | 4 | 6 | 智能体编程、长时 CUDA 优化 |
| [阿里云](https://qwenlm.github.io "通义千问 Qwen") | [Qwen3.8-Max](https://www.alibabagroup.com "Qwen3.8-Max 阿里集团") | API / 开源权重 | 1M | 1M | 66K | 6 | 10 | 7 | 9 | 7 | 7 | 10 | 8 | 7 | ✅ | 3 | 6 | 多模态、智能体协作、自主编码 |
| [Amazon](https://aws.amazon.com "Amazon Web Services") | [Nova Premier 1.0](https://aws.amazon.com/ai/generative-ai/nova/ "Amazon Nova 模型页") | Amazon Bedrock API | 1M | 1M | 32K | 6 | 8 | 5 | 9 | 7 | 3 | 5 | 8 | 7 | ❌ | 6 | 6 | 蒸馏教学、长文档智能体 |
| [xAI](https://x.ai "xAI 官方网站") | [Grok 4.6](https://docs.x.ai/docs/models "xAI Grok 模型列表") | API | 500K | 500K | 32K | 4 | 5 | 5 | 8 | 3 | 7 | 5 | 8 | 7 | ❌ | 8 | 4 | 代码、聊天、实时搜索、视觉理解 |
| [xAI](https://x.ai "xAI 官方网站") | [Grok 4](https://x.ai/news/grok-4 "xAI Grok 4 发布页") | API | 256K | 256K | 32K | 4 | 5 | 5 | 8 | 3 | 7 | 5 | 3 | 7 | ❌ | 8 | 4 | 实时搜索、聊天、工具使用 |
| [Meta AI](https://ai.meta.com "Meta AI 官方网站") | [Llama 4 Maverick](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct "Llama 4 Maverick 模型卡") | API / 开源权重 | 1M | 1M | 8K | 4 | 5 | 5 | 8 | 3 | 3 | 8 | 5 | 3 | ✅ | 1 | 4 | 多模态、多语言、代码生成 |
| [智谱](https://zhipuai.cn "智谱 Zhipu AI") | [GLM-5.3](https://z.ai "GLM-5.3 Z.ai") | API / 开源权重 | 1M | 1M | 128K | 4 | 5 | 5 | 8 | 3 | 3 | 8 | 5 | 7 | ✅ | 3 | 4 | 长代码生成、网络安全、智能体 |
| [Mistral AI](https://mistral.ai "Mistral AI 官方网站") | [Mistral Large 3 675B Instruct](https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512 "Mistral Large 3 模型卡") | API / 开源权重 | 256K | 256K | 8K | 4 | 5 | 5 | 8 | 3 | 3 | 8 | 5 | 7 | ✅ | 1 | 4 | 通用智能体、多语言、工具调用 |
| [NVIDIA](https://www.nvidia.com "NVIDIA 官方网站") | [Nemotron 3 Ultra 550B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-Base-BF16 "Nemotron 3 Ultra 模型卡") | 开源权重 / NVIDIA NIM | 1M | 1M | 8K | 4 | 5 | 3 | 7 | 3 | 3 | 5 | 10 | 3 | ✅ | 0 | 4 | 长上下文智能体、企业部署 |
| [Amazon](https://aws.amazon.com "Amazon Web Services") | [Nova Pro 1.0](https://aws.amazon.com/ai/generative-ai/nova/ "Amazon Nova 模型页") | Amazon Bedrock API | 300K | 300K | 5K | 4 | 5 | 3 | 9 | 3 | 3 | 5 | 5 | 7 | ❌ | 2 | 4 | 多模态、智能体工具调用 |
| [Meta AI](https://ai.meta.com "Meta AI 官方网站") | [Muse Spark 1.3](https://ai.meta.com "Meta AI Muse Spark") | API | 1M | 1M | 8K | 4 | 5 | 5 | 7 | 3 | 3 | 5 | 5 | 3 | ❌ | 4 | 4 | 通用生成、推理、工具调用 |
| [Meta AI](https://ai.meta.com "Meta AI 官方网站") | [Llama 4 Scout](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct "Llama 4 Scout 模型卡") | API / 开源权重 | 10M | 10M | 8K | 2 | 3 | 3 | 8 | 0 | 0 | 5 | 5 | 0 | ✅ | 0 | 2 | 超长上下文检索、本地部署 |
| [NVIDIA](https://www.nvidia.com "NVIDIA 官方网站") | [Nemotron 3 Super 120B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 "Nemotron 3 Super 模型卡") | 开源权重 / NVIDIA NIM | 1M | 1M | 8K | 4 | 3 | 3 | 7 | 3 | 3 | 5 | 10 | 3 | ✅ | 0 | 2 | 高吞吐智能体、低延迟 |
| [Amazon](https://aws.amazon.com "Amazon Web Services") | [Nova Lite 1.0](https://aws.amazon.com/ai/generative-ai/nova/ "Amazon Nova 模型页") | Amazon Bedrock API | 300K | 300K | 5K | 2 | 3 | 2 | 8 | 0 | 0 | 3 | 3 | 3 | ❌ | 1 | 2 | 多模态 RAG、低成本 |
| [Amazon](https://aws.amazon.com "Amazon Web Services") | [Nova Micro 1.0](https://aws.amazon.com/ai/generative-ai/nova/ "Amazon Nova 模型页") | Amazon Bedrock API | 128K | 128K | 5K | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | ❌ | 0 | 0 | 高吞吐分类、提取、低延迟 |
| [Cohere](https://cohere.com "Cohere 官方网站") | [Command A+](https://cohere.com/blog/command-a-plus "Command A+ 博客") | Cohere API | 128K | 128K | 64K | 0 | 0 | 2 | 8 | 0 | 0 | 10 | 3 | 3 | ✅ | 6 | 0 | 主权 AI、企业 RAG、多语言 |

## Coding Agents 比较

| 制造商 | Agent | 第三方<br>模型 | Repo<br>理解 | 批量<br>重构 | 自我<br>纠错 | 长周期<br>任务 | 工程<br>能力 | Git<br>工作流 | 上下文<br>压缩 | 记忆<br>管理 | 并行<br>子代理 | 工具<br>调用 | 安全性 | 灵活性 | 成本<br>控制 | 综合<br>评价 | 强项 | 弱项 |
| :----- | :---- | :------------: | :----------: | :----------: | :----------: | :------------: | :----------: | :-----------: | :------------: | :----------: | :------------: | :----------: | :----: | :----: | :----------: | ----------: | :--- | :--- |
| [Anthropic](https://www.anthropic.com "Anthropic 官方网站") | [Claude Code 2.x](https://code.claude.com/docs/en/overview "Claude Code 官方文档") | ✅ | 8 | 10 | 7 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 8 | 8 | 2 | 10 | 仓库理解与多文件编辑、Sub-agents 并行编排、MCP 工具生态成熟 | 默认仅 Anthropic 模型（第三方需 BYOK），订阅价位偏高 |
| [SpaceXAI（Anysphere）](https://cursor.com "Cursor 官网") | [Cursor（Composer 2.5 / Grok 4.6）](https://cursor.com/changelog "Cursor 更新日志") | ✅ | 8 | 8 | 7 | 10 | 10 | 8 | 8 | 6 | 10 | 7 | 6 | 8 | 2 | 10 | 多模型路由 Cursor Router、自托管 Machine 隔离执行、Composer 2.5 内核编辑能力强 | 后台 Agents 仍依赖云端任务调度，本地体验偶发掉线 |
| [Cognition AI](https://www.cognition-labs.com "Cognition AI 官网") | [Devin 2.2 / Devin Desktop](https://cognition.com/blog/devin-2 "Devin 2 官方博客") | ❓ | 8 | 8 | 3 | 10 | 10 | 8 | 6 | 6 | 10 | 10 | 6 | 3 | 0 | 10 | 端到端 Issue → PR、自带云端 IDE 与浏览器操作、多 Devin 并行 | 平台绑定较重，单价偏高，长任务偶发幻觉 |
| [Google DeepMind](https://deepmind.google "Google DeepMind 官方网站") | [Gemini CLI v0.60.0-nightly](https://github.com/google-gemini/gemini-cli "Gemini CLI GitHub") | ❓ | 5 | 5 | 7 | 5 | 5 | 8 | 6 | 2 | 5 | 10 | 10 | 5 | 8 | 10 | 1M 上下文窗口、Google Search 原生集成、GitHub Actions 集成 | 默认绑定 Gemini 模型，多模态仍以文本为主 |
| [阿里云](https://www.aliyun.com "阿里云官网") | [Qoder CN](https://qoder.com "Qoder 国际版") | ✅ | 5 | 8 | 3 | 10 | 5 | 5 | 8 | 8 | 8 | 7 | 6 | 5 | 6 | 10 | Quest 自主任务委托、Repo Wiki 自动文档、MCP + NES 多行编辑 | 国内版响应国际版反馈滞后，模型路由仍在演进 |
| [OpenAI](https://openai.com "OpenAI 官方网站") | [Codex CLI 0.153.4](https://github.com/openai/codex "Codex CLI GitHub") | ❓ | 3 | 8 | 7 | 8 | 10 | 5 | 8 | 4 | 7 | 10 | 6 | 3 | 4 | 7 | 沙箱安全执行、Plugin CLI、Guardian review 与 compact 机制 | 第三方模型接入范围有限，云端 Codex 与 CLI 模型能力不对称 |
| [GitHub（Microsoft）](https://github.com "GitHub 官网") | [GitHub Copilot + Copilot Coding Agent](https://github.com/features/copilot "GitHub Copilot 官网") | ✅ | 8 | 8 | 3 | 8 | 5 | 10 | 6 | 6 | 8 | 7 | 8 | 5 | 4 | 7 | GitHub Issue / PR 原生集成、Agents Tab 与组织级管控、免费档可用 | 长链路决策依赖云端轮询，单步推理深度不及 Cursor / Claude Code |
| [Anysphere / SpaceXAI](https://cursor.com "Cursor 官网") | [Cursor Harness（Cloud Agents）](https://cursor.com/blog/cloud-agents "Cursor Cloud Agents 博客") | ✅ | 5 | 8 | 3 | 10 | 10 | 8 | 6 | 4 | 10 | 7 | 8 | 3 | 2 | 7 | 3 倍加速预构建环境、动态 Machine 池、自托管隔离 | 主要为 Cursor 订阅增量能力，单独订阅粒度有限 |
| [JetBrains](https://www.jetbrains.com "JetBrains 官网") | [JetBrains AI Assistant + Junie](https://www.jetbrains.com/junie "Junie 官网") | ✅ | 8 | 10 | 7 | 5 | 5 | 8 | 6 | 6 | 7 | 7 | 8 | 3 | 4 | 7 | IDE 静态分析与 LLM 深度融合、Junie Local 本地推理、Junie CLI + MCP | 强绑定 JetBrains IDE，Community 版受限，BYOK 需额度 |
| [Sourcegraph](https://sourcegraph.com "Sourcegraph 官网") | [Sourcegraph Cody Enterprise + Amp](https://sourcegraph.com/amp "Sourcegraph Amp") | ✅ | 10 | 8 | 3 | 8 | 5 | 5 | 8 | 8 | 10 | 7 | 6 | 5 | 2 | 7 | 跨仓库代码图谱、1M+ token 上下文、Orbs 远端执行 | Cody 已仅企业版、Amp 桌面调度体验仍在演进 |
| [Cline](https://cline.bot "Cline 官网") | [Cline CLI 2.0 / Cline Teams](https://github.com/cline/cline "Cline GitHub") | ✅ | 8 | 10 | 10 | 8 | 5 | 8 | 8 | 8 | 10 | 10 | 8 | 8 | 8 | 7 | Apache 2.0 开源、多 Agent Teams、Memory Bank + Durable Session、任意 OpenAI 兼容端点 | 团队版 UI（Kanban）尚新，企业级审计与 SSO 起步较晚 |
| [Google](https://jules.google "Google Jules") | [Jules / Antigravity](https://jules.google "Jules 主页") | ❌ | 5 | 5 | 7 | 10 | 10 | 8 | 6 | 8 | 10 | 10 | 10 | 0 | 0 | 7 | 异步 GitHub PR 全流程、Antigravity Agent Manager 多智能体编排 | 仅个人 Gmail 账号，无法 Workspace/企业；Jules V2（Jitro）开发中 |
| [SST](https://sst.dev "SST 官网") | [opencode（Anomalyco fork）](https://opencode.ai "opencode 官网") | ✅ | 3 | 5 | 3 | 5 | 5 | 8 | 6 | 4 | 8 | 10 | 6 | 10 | 8 | 7 | 75+ 模型提供商完全中立、Plan/Build 双模式安全、MIT 100% 开源 | 终端用户友好度低于 Claude Code，更新节奏激进偶发 bug |
| [Aider](https://aider.chat "Aider 官网") | [Aider v0.86.1](https://aider.chat/HISTORY.html "Aider 版本历史") | ✅ | 8 | 5 | 7 | 3 | 0 | 10 | 6 | 4 | 2 | 3 | 6 | 8 | 6 | 3 | 100+ 语言、Repo Map 自动摘要、原生 Git 自动提交、纯 BYOK 零抽成 | 终端交互为主，缺少并行子代理与长周期调度，云能力薄弱 |
| [StackBlitz](https://stackblitz.com "StackBlitz 官网") | [Bolt.new](https://bolt.new "Bolt.new 官网") | ✅ | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 4 | 3 | 0 | 3 | 浏览器内 WebContainers 零配置、AI 全栈生成、部署集成完整 | Token 消耗快、浏览器内存限制 2–3 GB、Python 支持弱 |
| [Warp](https://www.warp.dev "Warp 官网") | [Warp（Agent Mode 3.0）](https://www.warp.dev/agent-mode "Warp Agent Mode") | ✅ | 3 | 3 | 3 | 3 | 5 | 5 | 4 | 2 | 5 | 7 | 6 | 3 | 4 | 3 | 终端原生 GPU 加速、模型选择覆盖 Fable/Opus/GPT/Gemini/GLM/Kimi、SWE-bench Verified 75.8% | 高级功能锁在 $20–$200/月付费层、CLI 模式较新 |
| [Cognition](https://www.cognition-labs.com "Cognition AI 官网") | [mini-SWE-agent](https://github.com/SWE-agent/mini-swe-agent "mini-SWE-agent GitHub") | ✅ | 3 | 3 | 3 | 3 | 0 | 5 | 2 | 0 | 3 | 0 | 2 | 8 | 10 | 3 | 仅 100 行 Python 模型无关、Bash-only 透明执行、74% SWE-bench Verified | 无 IDE 集成、无丰富 UI，仅适合命令行研究/基准 |
| [Kilo Code](https://kilo.ai "Kilo Code 官网") | [Kilo Code](https://kilo.ai "Kilo Code 官网") | ✅ | 3 | 5 | 0 | 3 | 0 | 5 | 4 | 4 | 7 | 3 | 4 | 8 | 10 | 3 | Roo/Cline 之上的超集、500+ 模型零加价、多平台（VS Code/JetBrains/CLI/Cloud/Slack） | 模型生态仍以 Claude/GPT 为主、记忆与并行子代理未深度优化 |
| [Replit](https://replit.com "Replit 官网") | [Replit Agent 4](https://replit.com "Replit Agent 4") | ✅ | 0 | 0 | 3 | 3 | 0 | 0 | 2 | 2 | 5 | 3 | 2 | 3 | 2 | 0 | 浏览器内自然语言→部署一体化、Plan mode 三种模式按预算分级 | 复杂大型工程易卡顿、Credit 消耗难精确预测 |
| [字节跳动](https://www.bytedance.com "字节跳动官网") | [Trae IDE](https://www.trae.ai "Trae IDE 官网") | ✅ | 3 | 3 | 0 | 5 | 0 | 3 | 4 | 2 | 3 | 3 | 0 | 3 | 8 | 0 | Claude 4.5 Sonnet 默认、多模型 BYOK 支持、免费策略激进 | 数据出境合规顾虑、无 Windows 完整版长期打磨、模型切换不够平滑 |

## 附录：数据来源

### Tier 1（极高权威）

- [Artificial Analysis — Models](https://artificialanalysis.ai/models "Artificial Analysis Models") — Claude Fable 5.1 / Opus 5 / GPT-6 Astra / Kimi K3 / GLM-5.3 / Qwen3.8 等多榜综合与 Intelligence Index
- [Artificial Analysis — Coding Agents](https://artificialanalysis.ai/agents/coding-agents "AA Coding Agents") — Coding Agent Index 综合 DeepSWE、Terminal-Bench v2.1、SWE-Atlas-QnA 三项基准
- [Vellum LLM Leaderboard](https://www.vellum.ai/llm-leaderboard "Vellum LLM Leaderboard") — Claude Fable 5.1 / Mythos 5.1 / Opus 5 综合排名，GPT-5.6 Sol Agentic Coding 96.2%
- [Steel.dev SWE-bench Verified](https://leaderboard.steel.dev/leaderboards/swe-bench-verified "Steel.dev SWE-bench Verified") — Claude Opus 5 97.00%（Vals.ai）、DeepSeek V4 Pro 0813 96.4% 等独立 SWE-bench 测量
- [Aider Polyglot Leaderboard](https://aider.chat/docs/leaderboards/ "Aider Leaderboard") — GPT-5 high 88.0%（#1）、o3-pro high 84.9%（#3）、grok-4 high 79.6%（#7）
- [Program Bench](https://programbench.com/ "Program Bench") — Claude Opus 5 (xhigh) 4.5% Resolved（#1）、GPT-5.6 Sol (xhigh) 1.0% / 15.5% Almost
- [Presenc AI — LMSYS Arena 6 月快照](https://presenc.ai/research/chatbot-arena-elo-leaderboard-june-2026 "Presenc AI LMSYS Arena 月度快照") — GPT-5.6 Pro ~1465 Elo（#1）、Claude Mythos 5 ~1458、Gemini 3.2 Pro ~1448、DeepSeek V4.1 Pro ~1410、Llama 4.5 Maverick ~1370、GLM-6 ~1360、Mistral Large 3 ~1352
- [HuggingFace Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard "HuggingFace Open LLM Leaderboard") — 业内领先的开源 AI 平台聚合多项公开基准
- [LMSYS Arena — HuggingFace Space 镜像](https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard "LMSYS Arena HF 镜像") — LMSYS Arena 镜像，lmarena.ai 不可达时的替代
- [SWE-bench](https://www.swebench.com/index.html "SWE-bench") — 软件工程任务的学术金标准
- [Terminal Bench](https://www.tbench.ai/ "Terminal Bench") — Stanford + Harbor + Laude Institute 联合发布的终端任务基准
- [Hacker News](https://news.ycombinator.com "Hacker News") — 新工具与新模型讨论的最快信号源
- [Artificial Analysis Blog](https://artificialanalysis.ai/blog "Artificial Analysis Blog") — 独立 AI 研究机构深度模型分析文章

### Tier 1 — 厂商官方文档

- [Anthropic Claude Pricing](https://platform.claude.com/docs/en/about-claude/pricing "Anthropic Claude Pricing") — 各 Claude 模型输入/输出/缓存定价与上下文窗口
- [Anthropic Claude Opus](https://www.anthropic.com/claude/opus "Claude Opus") — Claude Opus 5 模型介绍与定价
- [Anthropic Claude Fable](https://www.anthropic.com/claude/fable "Claude Fable") — Claude Fable 5.1 模型介绍
- [Anthropic Claude Mythos](https://www.anthropic.com/claude/mythos "Claude Mythos") — Claude Mythos 5 / 5.1 与 Glasswing 限定访问说明
- [Anthropic Claude Sonnet](https://www.anthropic.com/claude/sonnet "Claude Sonnet") — Claude Sonnet 4.6 模型介绍
- [OpenAI API Models](https://developers.openai.com/api/docs/models "OpenAI API Models") — GPT-6 Astra、GPT-5.6 Sol / Terra / Luna 模型 ID 与上下文
- [OpenAI API Pricing](https://developers.openai.com/api/docs/pricing "OpenAI API Pricing") — 各 OpenAI 模型分档定价
- [OpenRouter GPT-5](https://openrouter.ai/openai/gpt-5 "OpenRouter GPT-5") — GPT-5 上下文窗口、最大输出、价格
- [OpenRouter o3-pro](https://openrouter.ai/openai/o3-pro "OpenRouter o3-pro") — o3-pro 上下文 200K、最大输出 100K、价格
- [xAI Grok Pricing](https://docs.x.ai/docs/pricing "xAI Grok Pricing") — Grok 4.6 / 4.5 / 4.3 / 4.20 输入/输出/缓存定价与上下文
- [xAI Grok Models](https://docs.x.ai/docs/models "xAI Grok Models") — Grok 4.6 上下文 500K、知识截止 2026-02-01
- [xAI Grok 4 News](https://x.ai/news/grok-4 "xAI Grok 4") — Grok 4 256K 上下文、SuperGrok / Premium+ / API 渠道
- [Google AI Gemini Pricing](https://ai.google.dev/gemini-api/docs/pricing "Google AI Gemini Pricing") — Gemini 3.1 Pro $2/$12（≤200K）、$4/$18（>200K）与缓存、Batch / Flex / Priority
- [Google AI Gemini Models](https://ai.google.dev/gemini-api/docs/models "Google AI Gemini Models") — Gemini 3.1 Pro Preview 模型端点说明
- [HuggingFace — Llama-4-Maverick-17B-128E-Instruct](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct "Llama 4 Maverick") — MMLU-Pro 80.5、GPQA Diamond 69.8、LiveCodeBench 43.4
- [HuggingFace — Llama-4-Scout-17B-16E-Instruct](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct "Llama 4 Scout") — MMLU-Pro 74.3、GPQA Diamond 57.2、LiveCodeBench 32.8、10M 上下文
- [HuggingFace — Mistral-Large-3-675B-Instruct-2512](https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512 "Mistral Large 3") — Apache 2.0、256K 上下文、Granular MoE 架构
- [Mistral AI — Mistral 3 News](https://mistral.ai/news/mistral-3 "Mistral 3 release") — Mistral Large 3 发布公告
- [AWS — Amazon Nova](https://aws.amazon.com/ai/generative-ai/nova/ "Amazon Nova") — Nova 系列总览（Micro 128K、Lite 300K、Pro 300K、Premier 1M）
- [AWS Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "AWS Bedrock Pricing") — Nova 系列价格层级
- [Cohere — Command A+](https://cohere.com/blog/command-a-plus "Command A+") — 218B MoE、128K 上下文、Apache 2.0、τ²-Bench 85%、Terminal-Bench Hard 25%
- [NVIDIA — Nemotron 3 Ultra](https://research.nvidia.com/labs/nemotron/Nemotron-3-Ultra/ "Nemotron 3 Ultra") — 550B/55B、1M 上下文、OpenMDW-1.1、PinchBench 91%
- [Friday AI — Kimi K3 Benchmarks](https://www.tryfriday.ai/blog/kimi-k3-benchmarks-pricing-context-window "Kimi K3") — 2.8T 总参数、MoE 16/896、Terminal-Bench 2.1 88.3、SWE-bench 76.8%、$3/$15 价格
- [LabIndex — DeepSeek-V4-Pro-0813](https://labindex.ai/outputs/deepseek/deepseek-v4-pro "DeepSeek V4 Pro 0813 GA") — 1.6T MoE、1M 上下文、384K 输出、MIT 开源
- [Dataconomy — GLM-5.3](https://dataconomy.com/ai-models/glm-5-3 "GLM-5.3") — 744B/40B MoE、1M 上下文、128K 输出、2026-08-14 发布、SWE-bench 57.8%、CyberGym 84.5%
- [Alibaba Cloud — Qwen3.7 Agent Frontier](https://www.alibabacloud.com/blog/qwen3-7-the-agent-frontier_603154 "Qwen3.7 Agent Frontier") — 1M 上下文、AA Intelligence 56.6、Terminal-Bench 2.0 69.7、HMMT 97.1
- [Alibaba Group — Qwen3.8-Max](https://www.alibabagroup.com/document-2021044032125272064 "Qwen3.8-Max") — 2.4T/95B MoE、2026-08-03 杭州云栖发布、多模态、9 芯片适配
- [Vals AI — Qwen3.7 Max](https://vals.ai/models/alibaba_qwen3.7-max "Vals AI Qwen3.7 Max") — 独立 Intelligence Index 56.6 验证
- [Claude Code 官方文档](https://code.claude.com/docs/en/overview "Claude Code 官方文档") — Claude Code 2.x 功能、Sub-agents、MCP、第三方 provider
- [Claude Code 产品页](https://claude.com/product/claude-code "Claude Code 产品页") — Claude Code 定价、模型支持、能力清单
- [Cursor 官方 changelog](https://cursor.com/changelog "Cursor changelog") — Self-hosted Machines（2026-09-02）、Cloud Agents 改进、Composer 2.5、Grok 4.6 等事件
- [Cursor Cloud Agents 博客](https://cursor.com/blog/cloud-agents "Cursor Cloud Agents") — Cursor Harness 多模型并行、长周期执行
- [Cursor Router 博客](https://cursor.com/blog "Cursor Blog") — 多模型调度与 Cursor Router
- [Devin 2 官方博客](https://cognition.com/blog/devin-2 "Devin 2 官方博客") — Devin 2.2 多 Devin 并行、Devin Wiki、Interactive Planning
- [Devin 官网](https://devin.ai/ "Devin 官网") — Devin Desktop 产品形态
- [Codex CLI GitHub 主页](https://github.com/openai/codex "Codex CLI GitHub") — Codex CLI 0.153.x 最新版本、122k stars
- [Codex CLI Releases](https://github.com/openai/codex/releases "Codex CLI Releases") — 0.153.4 修复与 0.153.0 Plugin CLI、Guardian review
- [OpenAI Codex CLI 介绍](https://openai.com/index/introducing-codex-cli/ "OpenAI Codex CLI 介绍") — Codex CLI 定位与用法
- [GitHub Copilot 产品页](https://github.com/features/copilot "GitHub Copilot 官网") — 多档定价、Claude / Codex agents、模型策略
- [GitHub Copilot Docs](https://docs.github.com/en/copilot "GitHub Copilot Docs") — BYOK、LTS、FedRAMP 合规模型
- [GitHub Changelog Agents Tab](https://github.blog/changelog/2026-01-26-introducing-the-agents-tab-in-your-repository/ "Agents Tab") — 仓库级 Agents Tab 引入
- [JetBrains Junie 官网](https://www.jetbrains.com/junie "Junie 官网") — Junie 2026-06 离开 Beta、价格、模型
- [Junie 帮助文档](https://www.jetbrains.com/help/ai-assistant/junie-agent.html "Junie 帮助文档") — Junie CLI、Custom Subagents、MCP
- [Junie 博客](https://blog.jetbrains.com/junie/ "Junie 博客") — Junie Local、SWE-Rebench
- [Sourcegraph Amp 官网](https://sourcegraph.com/amp "Sourcegraph Amp") — Amp 多模型路由、Orbs、Puck
- [Sourcegraph 主页](https://sourcegraph.com "Sourcegraph 主页") — Cody 企业版定位、SCIP、Batch Changes
- [Aider 官网](https://aider.chat "Aider 官网") — Repo Map、Git 自动 commit、100+ 语言、Voice-to-code
- [Aider GitHub](https://github.com/Aider-AI/aider "Aider GitHub") — 48.8k stars、13k commits
- [Aider 版本历史](https://aider.chat/HISTORY.html "Aider 版本历史") — v0.86.1 最新 release、GPT-5 reasoning_effort
- [Cline 官网](https://cline.bot "Cline 官网") — 多模型、Agent Teams、Memory Bank、250+ 贡献者
- [Cline GitHub](https://github.com/cline/cline "Cline GitHub") — 67.6k stars、Apache 2.0
- [opencode.ai 官方](https://opencode.ai "opencode.ai 官方") — SST opencode 核心功能与定价数据
- [Gemini CLI GitHub](https://github.com/google-gemini/gemini-cli "Gemini CLI GitHub") — Gemini CLI 最新版本与特性
- [Gemini CLI release notes](https://geminicli.com/docs/changelogs "Gemini CLI release notes") — Gemini CLI 版本历史
- [jules.google](https://jules.google "Google Jules") — 异步编码 Agent 主页
- [deepmind.google/technologies/antigravity](https://deepmind.google/technologies/antigravity/ "Google Antigravity") — Google Antigravity 官方技术页
- [replit.com](https://replit.com "Replit Agent 4") — Replit Agent 4 官方
- [bolt.new](https://bolt.new "Bolt.new 官方") — StackBlitz Bolt.new 官方
- [warp.dev/agent-mode](https://www.warp.dev/agent-mode "Warp Agent Mode") — Warp Agent Mode 主页
- [warp.dev/pricing](https://www.warp.dev/pricing "Warp Pricing") — Warp 定价与模型支持
- [mini-SWE-agent GitHub](https://github.com/SWE-agent/mini-swe-agent "mini-SWE-agent") — mini-SWE-agent 仓库
- [trae.ai](https://www.trae.ai "Trae IDE 官方") — 字节跳动 Trae 官方
- [aliyun.com — 通义灵码 / Qoder CN](https://www.aliyun.com/product/yunxiao/lingma "Qoder CN 主页") — 阿里云 Qoder CN 主页
- [help.aliyun.com — Qoder CN 更新日志](https://help.aliyun.com/zh/lingma/product-overview/dynamics-and-announcements/ "Qoder CN 更新日志") — Qoder CN 版本演进
- [kilo.ai](https://kilo.ai "Kilo Code 官网") — Kilo Code 主页

### Tier 2（高权威）

- [BenchLM — Coding](https://benchlm.ai/coding "BenchLM Coding") — Claude Fable 5.1 84.2（#1）、Opus 5 75.6、GPT-6 Astra 75.3、Grok 4.6 66.8
- [BenchLM — Best Proprietary](https://benchlm.ai/best/proprietary "BenchLM Best Proprietary") — 同 BenchLM 主体，方法论公开
- [LLM Stats — Best AI for Web Development](https://llm-stats.com/best-ai-for-web-development "LLM Stats Web Dev") — GPT-6 Astra 49.0（#1）、GPT-5.6 Sol 46.0（#2）、Claude Fable 5 45.9
- [LLM Stats Benchmarks](https://llm-stats.com/benchmarks "LLM-Stats Benchmarks") — GPT-6 Astra 60.7（#1）、Claude Fable 5.1 56.8（#2）、Opus 5 55.4（#3）
- [ModelGrep Leaderboard](https://modelgrep.com/leaderboard "ModelGrep 排行榜") — Claude Fable 5.1 Intelligence 56.8（#1）、GPT-6 Astra 54.7、Opus 5 54.1、Grok 4.6 50.6
- [LLM Podium Leaderboard](https://llmpodium.com/leaderboard "LLM Podium") — Mythos Preview Podium 97.4（#1）、Fable 5.1 88.4、GPT-6 Astra 86.2、Opus 5 81.4、Sol 80.8
- [ModelGrep — Muse Spark 1.3](https://modelgrep.com/models/meta/muse-spark-1-3 "Muse Spark 1.3 on ModelGrep") — Muse Spark 1.3 价格、上下文、Intelligence 53.0
- [Presenc AI — Llama 4.5 Release Brief](https://presenc.ai/research/llama-4-5-release-brief "Llama 4.5 release brief") — Llama 4.5 Maverick 中期刷新说明
- [DataLearner AI Leaderboards](https://www.datalearner.com/en/leaderboards "DataLearner AI Leaderboards") — Claude Fable 5.1 65（#1）、Claude Opus 5 64.7、o3-pro Agent 84.9
- [iCreat AI — DeepSeek V4 Pro 0813 Pricing](https://icreat.ai/blogs/deepseek-v4-pro-0813-benchmarks-api-pricing "DeepSeek V4 Pro 0813 pricing") — 8-16 峰谷定价机制
- [TechCrunch — Amazon Nova Premier](https://techcrunch.com/?p=3001640 "Amazon Nova Premier launch") — Nova Premier 1M 上下文、$2.50/$12.50 价格
- [CloudPrice — Mistral Large 3](https://cloudprice.net/models/mistral-large-3 "Mistral Large 3 pricing") — $0.50/$1.50 per 1M tokens、多云定价对比
- [AwesomeAgents — Nemotron 3 Super](https://awesomeagents.ai/news/nvidia-nemotron-3-super-120b-agentic-ai "Nemotron 3 Super 120B") — 120B/12B、2026-03-11 发布、RULER@1M 91.75%
- [InfoQ — OpenCode](https://www.infoq.com/news/2025/07/opencode-open-source-claude-code-alternative/ "InfoQ OpenCode") — opencode 行业对比
- [MarkTechPost — Claude Code vs OpenCode](https://www.marktechpost.com/2025/09/03/comparison-claude-code-vs-opencode-cross-platform-terminal-ai-coding/ "MarkTechPost Claude Code vs OpenCode") — opencode 与 Claude Code 对比
- [AIToolSkit — Gemini CLI 0.37.1](https://www.aitoolskit.io/learn/gemini-cli-0-37-1-google-terminal-agent-2026 "AIToolSkit Gemini CLI") — Gemini CLI 新特性
- [AlternativeTo — Warp 2.0](https://alternativeto.net/news/2025/6/warp-2-0-introduce-a-unified-agentic-development-environment-running-within-the-terminal "AlternativeTo Warp 2.0") — Warp 2.0 评测
- [TheAIAgentIndex — Jules Review 2026](https://theaiagentindex.com/agents/jules "TheAIAgentIndex Jules Review") — Jules 第三方评测
- [Respan.ai — Google Antigravity vs Google Jules](https://www.respan.ai/market-map/compare/google-antigravity-vs-google-jules "Respan.ai Antigravity vs Jules") — Antigravity vs Jules 对比
- [AIToolCrunch — Jules Review 2026](https://www.aitoolcrunch.com/tools/jules "AIToolCrunch Jules Review") — Jules 第三方评测
- [TheAgentTimes — Cline CLI 2.0](https://theagenttimes.com/articles/cline-cli-20-the-coding-agent-that-left-the-ide-and-learned-to-run-headless "TheAgentTimes Cline CLI 2.0") — Cline CLI 2.0 评测
- [AiCentralResources — Amp](https://www.aicentralresources.com/tool/amp "AiCentralResources Amp") — Amp 评测
- [Knowara — Cody by Sourcegraph Review](https://knowara.com/ai-tools/coding/cody-by-sourcegraph-review/ "Knowara Cody Review") — Cody 评测
- [AiStackNav — Cline Review 2026](https://en.aistacknav.com/cline-review-2026 "AiStackNav Cline Review") — Cline 2026 综合评测

### Tier 3 / 4（中 / 低权威 — 用于补充覆盖）

- [DigitalJournal — Alibaba Launches Qoder](https://www.digitaljournal.com/pr/news/accesswire/alibaba-launches-qoder-agentic-coding-1226555787.html "DigitalJournal Qoder") — Qoder 国际版发布
- [Stdaily — 阿里发布新一代 AI 编程平台 Qoder](https://www.stdaily.com/web/gdxw/2025-08/22/content_388981.html "Stdaily Qoder 发布") — Qoder 中文报道
- [Sohu — 阿里发布全新 Qoder](https://m.sohu.com/a/1068371209_120988576 "Sohu Qoder") — Qoder 中文报道
- [Dev.to — Qoder AI Code Editor Review](https://dev.to/czmilo/complete-guide-2025-qoder-ai-code-editor-in-depth-review-and-user-guide-1d6o "Dev.to Qoder Review") — Qoder 完整评测
- [Builder.io — Trae vs Cursor](https://www.builder.io/blog/trae-vs-cursor "Builder.io Trae vs Cursor") — Trae 第三方对比
- [Fast.io — Trae AI Coding Tools](https://fast.io/blog/trae-ai-coding-tools "Fast.io Trae") — Trae 概览
- [Codura — Trae](https://www.codura.com/trae "Codura Trae") — Trae 工具卡片
- [AIToolRadar — Bolt.new Review 2026](https://www.aitoolradar.net/ai-tools/bolt-new "AIToolRadar Bolt.new") — Bolt.new 评测
- [DevStarsJ — Bolt.new Guide 2026](https://devstarsj.github.io/ai-tools/2026-04-02-Bolt-New-AI-Full-Stack-Web-App-Builder-Complete-Guide "DevStarsJ Bolt.new Guide") — Bolt.new 完整指南
- [BuildFastWithAI — Bolt.new Review 2026](https://www.buildfastwithai.com/ai-tools/bolt-new "BuildFastWithAI Bolt.new") — Bolt.new 评测
- [DevToolScout — Bolt.new Review 2026](https://www.devtoolscout.com/reviews/bolt-new-review-2026-build-full-stack-apps-from-scratch-with-ai "DevToolScout Bolt.new") — Bolt.new 评测
- [GitHubHelp — Kilo Code](https://githubhelp.com/yzhou277am/kilocode "GitHubHelp Kilo Code") — Kilo Code 说明
