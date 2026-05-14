# 深度解读：Beyond vibe coding: The five building blocks of AI-native engineering

> 原文：[Beyond vibe coding: The five building blocks of AI-native engineering](https://www.thoughtworks.com/insights/blog/generative-ai/beyond-vibe-coding-the-five-building-blocks-of-aI-native-engineering)<br>
> 作者：Sunit Parekh（Thoughtworks）<br>
> 日期：2026-03-18

## 原文及译文

<details>
<summary>原文（English）</summary>
<section>

> "In 2026, the software engineering landscape has moved beyond 'vibe coding'."

The article opens by noting that throwing raw prompts at a chat interface no longer works in enterprise software development. To build production-grade software, developers must treat AI as a sophisticated engineering stack through **orchestrating** five core building blocks: an **agent**, a **model**, a **methodology** like BMAD™, a **spec**, and **context**.

### Choose your agent

The agent is described as the "autonomous execution layer" and "an active participant in the development workflow, significantly surpassing basic reactive assistants." Core competencies include:

- Navigating and analyzing the file system. The agent "interrogates the project's directory, analyzes architecture and understands component interdependencies."
- Executing terminal commands. It runs dependency installs, build scripts, git operations, and diagnostics, "directly controlling the environment."
- Automated testing and verification. It "initiates test suites (such as unit and integration) to validate code changes."
- Autonomous multi-file editing and refactoring. It "implements complex changes across multiple files cohesively."
- Supervised autonomy. Operations are "under human supervision."

Popular agents listed: Claude Code (Anthropic), OpenCode (open-source, terminal-native), Cline (VS Code, open-source), Antigravity / Cursor / Windsurf (agent-first IDEs).

### Choosing the model

The article frames a "critical division of labor: the agent manages the execution of tasks and actions, while the model serves as the repository and processor of knowledge." By 2026, the market has "moved away from a 'one-size-fits-all' large general-purpose model" toward specialization.

Specialized model categories: code generation, architectural reasoning ("digital architect"), test and QA, documentation/knowledge synthesis, security/vulnerability analysis.

| Model | Strength | Best use case |
|---|---|---|
| Claude 4.6 Sonnet | Adaptive thinking | Complex agentic planning and large-scale code migration |
| Gemini 3.1 Pro | Context window and code reasoning | Large-scale codebase analysis, architectural thinking (2M+ tokens) |
| GPT 5.3 Codex | Raw reasoning and multi-modal understanding | Hard algorithmic problems, one-shot bug fixes, UI/UX mockups |
| GLM 5 | Cost-efficiency | Open-source high-volume boilerplate generation and unit testing |

### Choosing a methodology

The article identifies "agent thrashing" — where AI loops endlessly in self-correction — as a key risk. The solution is to "shift the paradigm from informal, open-ended generative interactions."

Methodology components: structured prompts (AI as the engineer), CI/CD integration (AI as the committer), test-driven AI / TDA (AI as quality assurance), version control and audit trails (AI as the documentarian), human oversight and vetting (human as the architect/reviewer).

Highlighted methodologies:
- **BMAD Method** — "a methodology for Agile AI-driven development that simulates a multi-role software team through role-based agent orchestration," using "a specialized loop of 'plan-analysis-design-architect-dev-test' personas" to reduce "hallucination drift" by requiring cross-agent consensus.
- **Thoughtworks AI/works™** — supports legacy modernization with a "3-3-3 delivery model — a concept in three days, functional prototype in three weeks and production-ready MVP in three months."

### Prompt using specs

The article states: "the bottleneck of development has shifted from raw coding to the precise articulation of requirements" and "the effectiveness of an autonomous coding agent is directly proportional to the quality of its input specification."

Toolkits mentioned:
- **SpecKit** (GitHub) — "five-step pipeline: constitution, specify, plan, tasks and implement."
- **OpenSpec** (Fission-AI) — "a fast three-step workflow: proposal, apply and archive." Suited for "brownfield" projects.
- **BMAD Quick Flow** — "transitions from raw requirements to a technical specification (quick-spec), immediate coding (quick-dev), and optional validation (code-review)."

### Providing context

The final layer is "context engineering," defined as "the strategic curation of institutional knowledge and design principles provided to AI assistants to enforce enterprise standards."

Context components: context engineering and Agent Skills, rules and instructions (e.g., `AGENTS.md`, `.cursorrules`), security guardrails ("never-allow" rules), design systems and architecture, Thoughtworks AI/works™ Context Integration (automated context harvesting from enterprise codebases).

### The new engineering stack

Closing summary: "software development with AI shifts from vibe coding to thoughtful orchestration. Success lies in the deliberate combination of the right agent, the most suitable model, a proven methodology like BMAD™, a precise spec, and well-defined context."

</section>
</details>

<details>
<summary>译文（中文）</summary>
<section>

> "2026 年，软件工程领域已经走出了 vibe coding 阶段。"

文章开篇即指出：在企业级软件开发中，仅向聊天界面丢入原始提示词（prompt）的做法已经不再奏效。要构建生产级软件，开发者必须将 AI 视为一套精密的工程栈，并通过**编排（orchestrating）**五个核心构件来实现：**智能体（agent）**、**模型（model）**、**方法论（methodology）**（如 BMAD™）、**规约（spec）** 与 **上下文（context）**。

### 一、选择智能体

文中将智能体定义为"自主执行层"（autonomous execution layer）——"开发工作流中的主动参与者，远远超越了基础的反应式助手"。其核心能力包括：

- **浏览与分析文件系统**：智能体"审问（interrogate）项目目录，分析架构并理解组件间的相互依赖"。
- **执行终端命令**：运行依赖安装、构建脚本、Git 操作与诊断，"直接控制环境"。
- **自动化测试与验证**：发起单元测试、集成测试等测试套件，"验证代码变更"。
- **自主多文件编辑与重构**：跨多个文件"内聚地实现复杂变更"。
- **受监督的自主性**：所有操作"处于人工监督之下"。

文中列举的主流智能体：Claude Code（Anthropic）、OpenCode（开源、终端原生）、Cline（VS Code、开源），以及 Antigravity / Cursor / Windsurf（agent-first IDE）。

### 二、选择模型

文章提出了一个关键的分工原则："智能体负责执行任务与动作，模型则是知识的载体与处理者。"到 2026 年，市场已经"摆脱了'一刀切'的通用大模型"，走向专业化分工。

专业化的模型类别：代码生成、架构推理（"数字架构师"）、测试与质量保障、文档与知识合成、安全与漏洞分析。

| 模型 | 强项 | 最佳使用场景 |
|---|---|---|
| Claude 4.6 Sonnet | 自适应思考（Adaptive thinking） | 复杂的智能体规划与大规模代码迁移 |
| Gemini 3.1 Pro | 上下文窗口与代码推理 | 大规模代码库分析、架构思考（2M+ tokens） |
| GPT 5.3 Codex | 原始推理与多模态理解 | 高难度算法题、单次性 bug 修复、UI/UX 草图 |
| GLM 5 | 成本效率 | 开源场景下大批量样板代码与单元测试生成 |

### 三、选择方法论

文章把"智能体抖动（agent thrashing）"——即 AI 在自我纠错中无限循环——视为关键风险，主张"将范式从非正式的、开放式的生成式交互，转变为结构化方法论"。

方法论构成：结构化提示词（AI 作为工程师）、CI/CD 集成（AI 作为提交者）、测试驱动 AI / TDA（AI 作为质量保障者）、版本控制与审计追踪（AI 作为文档员）、人工监督与把关（人作为架构师/评审者）。

重点方法论：
- **BMAD Method**："面向敏捷 AI 驱动开发的方法论，通过角色化智能体编排模拟多角色软件团队"，使用"plan-analysis-design-architect-dev-test（规划-分析-设计-架构-开发-测试）的专门循环"，并通过"跨智能体共识"来降低"幻觉漂移（hallucination drift）"。
- **Thoughtworks AI/works™**：以"3-3-3 交付模型"支持遗留系统现代化——"3 天形成概念、3 周做出功能原型、3 个月交付生产级 MVP"。

### 四、用规约进行提示

文章断言："开发的瓶颈已从原始编码转向需求的精准表达"，"自主编码智能体的效能与其输入规约的质量成正比"。

文中提及的规约工具箱：
- **SpecKit**（GitHub）："五步流水线——constitution（宪法）、specify（规约）、plan（计划）、tasks（任务）、implement（实现）"。
- **OpenSpec**（Fission-AI）："快速三步工作流——proposal（提案）、apply（应用）、archive（归档）"，特别适合"棕地（brownfield）"项目。
- **BMAD Quick Flow**："从原始需求到技术规约（quick-spec），再到立即编码（quick-dev），以及可选的验证（code-review）"。

### 五、提供上下文

最后一层是"上下文工程（context engineering）"——"为 AI 助手精心组织企业机构知识与设计原则，以强制企业标准落地"。

上下文构成：上下文工程与 Agent 技能、规则与指令（如 `AGENTS.md`、`.cursorrules`）、安全护栏（"never-allow"规则）、设计系统与架构、Thoughtworks AI/works™ 上下文集成（从企业代码库自动采集上下文）。

### 结语：新的工程栈

总结陈词："AI 时代的软件开发正在从 vibe coding 走向深思熟虑的编排（thoughtful orchestration）。成功的关键在于：有意识地把正确的智能体、最合适的模型、经过验证的方法论（如 BMAD™）、精准的规约以及定义良好的上下文，组合在一起。"

</section>
</details>

## 摘要

Thoughtworks 技术专家 Sunit Parekh 在 2026 年 3 月撰文提出：vibe coding 时代已经结束，企业级 AI 编程必须从"丢提示词给聊天界面"转向"精心编排五大构件"——智能体（agent）、模型（model）、方法论（methodology，如 BMAD）、规约（spec）和上下文（context）。文章以五大构件为骨架，系统梳理了 2026 年 AI 原生工程栈的格局：agent-first IDE 与终端原生 agent 并起、模型按任务领域专业化、BMAD 强调多角色 agent 共识、SpecKit/OpenSpec 等规约工具箱崛起、`AGENTS.md`/`.cursorrules` 与"never-allow"安全护栏构成上下文层。文章既是 Thoughtworks 自家 AI/works™ 平台的导引，也是行业对"vibe coding 已死、AI-native engineering 当立"这一判断的代表性论述。

## 术语表

| 术语 | 全称 / 缩写 | 解释 |
| :--- | :--- | :--- |
| Vibe coding | "凭感觉编码" | 由前 OpenAI/Tesla AI 负责人 Andrej Karpathy 于 2025 年 2 月创造的术语，指开发者只通过自然语言描述意图、让 LLM 生成全部代码、而不必理解代码本身的编程方式。Merriam-Webster 已收录，Collins 评为 2025 年度词汇。 |
| AI-native engineering | AI 原生工程 | 把 AI 智能体视为软件交付链一等公民、围绕 agent 重构 SDLC 的工程范式，与 cloud-native 类比。对应"AI-assisted"（AI 作为外挂辅助）。Thoughtworks AI/works™、Microsoft、a16z 等机构于 2025–2026 年同步推广。 |
| Agent thrashing | 智能体抖动 | 智能体在自我纠错中无限循环、反复尝试几乎相同的修复、在两个错误方案之间震荡或陷入无收敛的工具调用循环。虽未进入官方标准术语，但 Thoughtworks Tech Radar Vol. 34 用 "context rot"、"instruction bloat" 等相邻概念描述同类失效模式。 |
| Hallucination drift | 幻觉漂移 | 多轮/多智能体协作中，初始幻觉未被纠正而被后续轮次当作事实引用、沿工作流逐层放大的现象。BMAD 通过"双阶段工作流 + 多角色共识 + agent-as-code"试图缓解。 |
| BMAD Method | Breakthrough Method for Agile AI-Driven Development | BMad Code, LLC 维护的开源敏捷 AI 开发框架（GitHub 48.5k stars, MIT 协议），含 12+ 角色化 agent（PM/Architect/Developer/UX/QA 等）和 34+ 工作流。 |
| BMAD Quick Flow | — | BMAD 内置的轻量化并行轨道，跳过完整 PRD/架构阶段，以 `bmad-quick-dev` 直接产出 `spec-*.md` + 代码，适合 bug 修复、小特性。 |
| Agent Skills | — | Anthropic 于 2025 年正式发布的"智能体技能包"——以 `SKILL.md`（含 YAML frontmatter）+ 脚本/资源/模板组成的目录，遵循"渐进式披露"原则，与 MCP 互补。 |
| Context engineering | 上下文工程 | 2025 年中由 Shopify CEO Tobi Lütke 公开提出、Karpathy 转推强化的概念，Thoughtworks Tech Radar Vol. 34 列为 Adopt 级。指为 LLM 任务动态拼装 system prompt、对话历史、长期记忆、RAG 检索、工具等上下文，是超越单条 prompt 工程的系统化实践。 |
| TDA (Test-driven AI) | 测试驱动 AI | 把 TDD 的红绿循环映射到 LLM/agent 的方法论：先写可执行行为评估（assertion / LLM-as-judge / 工具调用断言），让 AI 最小改动使其通过，重构后再纳入 CI。2026 年仍处于社区/厂商并列状态，无统一标准。 |
| TDA 在原文中体现为 | "Test-driven AI / TDA" | 文章将其作为方法论五大组成之一，对应"AI as quality assurance"角色，要求 agent 在写代码同时或基于测试进行开发。 |
| `AGENTS.md` | — | 由 OpenAI Codex、Amp、Google Jules、Cursor、Factory 等发起的开放 Markdown 约定，2025–2026 年移交给 Linux Foundation 旗下 Agentic AI Foundation (AAIF) 托管，是面向 AI 编码 agent 的"README"。 |
| `.cursorrules` | — | Cursor IDE 早期（2025 年前）的项目规则约定，已被新版 `.cursor/rules/*.mdc` 取代，但本文作为时间快照仍予以引用。 |
| SpecKit | GitHub Spec Kit | GitHub 官方推出的规约驱动开发（SDD）工具集，108k stars，五步流水线：constitution / specify / plan / tasks / implement。 |
| OpenSpec | — | Fission-AI 维护的开源 SDD 框架（52.3k stars），以"proposal / apply / archive"三步工作流著称，特别适合棕地项目。 |
| AI/works™ | — | Thoughtworks 于 2025–2026 年推出的"Agentic Development Platform"，定位为 AI 时代的 SDLC，包含 6 大能力（反向工程、动态规约、规约到代码、开发者体验、控制平面、运行时运维）。 |
| 3-3-3 delivery model | 3 天 / 3 周 / 3 个月交付模型 | Thoughtworks 配合 AI/works™ 提出的交付节奏：3 天对齐概念 → 3 周做出原型 → 3 个月交付生产 MVP。 |
| "never-allow" 规则 | — | AI Agent 工具调用层的一类硬约束安全策略（deny-by-default），例如禁止删除生产数据库、禁止 force-push 主分支、禁止写入硬编码密钥。 |
| Hexagonal Architecture | 六边形架构 / 端口与适配器 | 由 Alistair Cockburn 于 2005 年命名的架构模式，核心是把应用核心与外部 I/O 通过端口（Ports）和适配器（Adapters）解耦。在 AI 工程中常作为"安全策略集中点"和"AI 适配层隔离"的参考架构。 |
| Brownfield / Greenfield | 棕地 / 绿地项目 | Brownfield 指在遗留系统上做改造，Greenfield 指从零开始的新项目。AI agent 在 Greenfield 上更易发挥，Brownfield 必须配合上下文工程与长时记忆。 |
| Claude Code | — | Anthropic 推出的终端 / IDE / Web / Slack 全平台 AI 编程 agent，专有软件。 |
| OpenCode | — | anomalyco 维护的开源（MIT）AI 编程 agent，169k stars，v1.15.13，原生终端。 |
| Cline | — | Cline Bot Inc. 维护的开源（Apache 2.0）agent，VS Code/JetBrains/CLI/SDK 全形态，v3.86.2。 |
| Cursor | — | Anysphere, Inc. 开发的 agent-first IDE，专有软件，v3.6（2026-05）。 |
| Windsurf | — | Cognition AI 旗下的 agentic IDE（Codeium 已被 Cognition 收购）。 |
| Antigravity | — | Google 旗下 agent-first IDE（域名有效），本文成文时公开信息有限，可视为"Google 对标 Cursor/Windsurf"的产品信号。 |

## 深度解读

### 一、核心论点：从 vibe coding 到 "thoughtful orchestration"

文章的核心命题是一个范式判断：**vibe coding 已经被企业级 AI 工程抛弃**。作者并非否定 LLM 编程的价值，而是主张"丢提示词"这种交互方式无法支撑生产系统，必须升级为对五大构件的有意识编排。这是一个**工具使用成熟度曲线**的判断：开发者从 Copilot 阶段（行内补全）→ Chat 阶段（聊天式生成）→ Vibe coding 阶段（凭感觉接受）→ AI-native engineering 阶段（把 AI 视为工程栈并主动治理）。

论据层面，作者在文中并未给出"vibe coding 失败"的量化统计，而是通过五大构件的罗列——agent、model、methodology、spec、context——把"AI 编程"这个庞大议题拆解为可治理、可评估的子系统。这与 Martin Fowler 在 *Exploring Gen AI*、Thoughtworks Tech Radar Vol. 34（2026.04 主题 "agentic world"）的整体方向一致：**AI 编程不是"模型之争"，而是"工程栈之争"**。

值得注意的是，**文章在论据上偏向"Thoughtworks 自家方案"**：BMAD 与 AI/works™ 都被作为标杆方法论/平台，而其他代表性方法论（如 OpenAI 的 eval-driven development、Hamel Husain 的 Braintrust eval、Microsoft 的 SDD 实践、Anthropic 的 Building Effective Agents）并未被对比讨论。这是 Thoughtworks 内容营销与最佳实践分享的典型组合——读者在接收洞见的同时，也在接受一个供应商视角的方案推荐。

### 二、五大构件的层次结构：一个"软件工程栈"的隐喻

把五大构件**并列**陈列是文章最具教学价值的设计。它把无形的"AI 编程"概念**映射**为开发者熟悉的"软件工程栈"心智模型：

| 构件 | 隐喻的角色 | 关键能力 |
|---|---|---|
| **Agent** | "自主执行层" | 文件系统、终端、测试、多文件编辑 |
| **Model** | "知识载体" | 推理、规划、生成 |
| **Methodology** | "开发流程" | 角色分工、CI/CD 集成、审计 |
| **Spec** | "规约" | 需求表达、任务分解、验收标准 |
| **Context** | "上下文" | 规则、技能、安全护栏、设计系统 |

这个结构暗示了一个**重要的工程观点**：AI 编程的有效性 ≠ "选用最强大的模型"。即便使用 Claude 4.6 Sonnet 或 GPT-5.3 Codex，如果缺乏结构化方法论、清晰规约和工程级上下文，agent 仍会陷入 thrashing、hallucination drift 等失效模式。这与 Thoughtworks Tech Radar Vol. 34 把"context rot"、"agent instruction bloat"列为 Caution 级的判断相互印证。

**值得商榷的"agent vs model 严格分工"论断**：文章把"agent 负责执行、model 负责知识"做了相对清晰的二分。但在 2026 年的实际工程中，越来越多 agent 框架（如 Claude Code 的 Routines、Cursor 的 Composer 2.5）让 agent 本身具有长时记忆和策略推理能力，model 也会参与决策。两者界限正在融合。文章的"分工"框架对教学有益，但不应被视为严格的工程事实。

### 三、方法论之争：BMAD 与 SDD 工具箱的崛起

文章把 BMAD Method 作为方法论标杆，提及"plan-analysis-design-architect-dev-test 的专门循环"和"跨 agent 共识"。根据交叉验证：

- **真实存在**：BMAD-METHOD 仓库（48.5k stars, MIT）确认存在，由 BMad Code, LLC 维护；
- **官方术语略有出入**：文章中"plan-analysis-design-architect-dev-test"是对 BMAD 实际阶段（analysis, planning, architecture/solutioning, implementation）的**重新表述**，官方文档更常用"BMM 四阶段 + 12+ 角色 agent"。文章版本更易读但**不严格对应官方术语**，建议读者查 BMAD 官方文档核对。
- **设计哲学**：BMAD 强调"agent-as-code"——把 agent 和 prompt 作为可版本化资产——与"上下文工程"和"spec-driven development"形成方法论三角。

文章同时点名了 **SpecKit**（GitHub 官方 SDD 工具集，108k stars）和 **OpenSpec**（Fission-AI，52.3k stars），构成 2026 年"spec-driven development"三大开源工具的代表性图景：

| 工具 | 主导方 | 核心工作流 | 强项 |
|---|---|---|---|
| **BMAD** | BMad Code, LLC | 4 阶段 + 12+ 角色 agent | 多角色协作、全生命周期 |
| **SpecKit** | GitHub 官方 | constitution→specify→plan→tasks→implement | 流水线化、官方背书 |
| **OpenSpec** | Fission-AI | proposal→apply→archive | 轻量、棕地友好 |

三者并非互斥——BMAD 可与 SpecKit 流程互相替代或叠加。它们的共同点是把"代码"从一等公民降级为"规约的派生品"——这一思想可以追溯到 1980 年代的"程序 = 规约的精化"研究，但在 LLM 时代获得了新的实践意义。

### 四、模型选择：从"一个模型"到"任务专属模型"

文中给出的模型选择表是文章具体性最强的部分：

- **Claude 4.6 Sonnet**：2026 年 2 月发布的 Sonnet 最新版，1M token 上下文、$3/$15 per M tokens，自适应思考能力突出。文中推荐用于"复杂智能体规划 + 大规模代码迁移"，与 Sonnet 4.6 的官方定位一致。
- **Gemini 3.1 Pro**：仍可使用，但 2026 年 6 月时已被 Gemini 3.5 系列（含 3.5 Flash/Pro）部分取代。文章成文时（2026 年 3 月）尚属最新，读者参考时需注意时间窗口。
- **GPT 5.3 Codex**：真实存在，但 OpenAI 已在 2026 年 3 月 5 日发布 **GPT-5.4 for Codex** 取代之。文中"GPT 5.3"是发布时的合理选择，但已不是当前最前沿。
- **GLM 5**：智谱 AI 的 754B MoE 模型，2025 年 4 月发布。文章中的"GLM 5"是发布时版本，**2026 年 2 月已有 GLM-5.1**（SWE-Bench Pro 58.4 领先 GPT-5.4 的 57.7）发布。读者参考时同样要注意时间差。

**重要的工程观点**：文章反复强调"specialization"——按任务类型（代码生成、架构推理、测试、文档、安全）选模型。这与 2025–2026 年"小而专的 SLM（small language model）+ 大通用模型"的混合架构趋势一致，**不是选"最强模型"，而是选"最合适的模型"**。

### 五、上文工程：AGENTS.md、Agent Skills 与"never-allow" 护栏

文章最后将"上下文"作为整合层。三个观察值得关注：

1. **`AGENTS.md` 已成为事实标准**：2025 年发起、2026 年由 Linux Foundation 旗下 Agentic AI Foundation 托管，已被 60,000+ 开源项目采用。文中把它与 `.cursorrules` 并列，但 `.cursorrules` 已被 Cursor 官方 `.cursor/rules/*.mdc` 取代——这是文章时间快照的一个小局限。
2. **Agent Skills ≠ MCP**：文章提及 Agent Skills 但未深入辨析。实际上，**Skills（教 agent 如何使用工具）** 与 **MCP（提供工具调用的标准化通道）** 是互补关系，Anthropic 官方也明确两者是 complementary。在企业落地时，Skills 往往借助 MCP 暴露的工具。
3. **"never-allow" 规则对接 OWASP LLM Top 10**：这是文章中较工程化的提法，对应 deny-by-default 的安全策略——例如禁止 AI 删除生产数据库、禁止 force-push 主分支、禁止写硬编码密钥。在 OWASP LLM01（Prompt Injection）/ LLM02（Insecure Output Handling）等标准下，这类规则已经逐渐从"可选"变为"必选"。

### 六、争议与不同观点

文章作为"vibe coding 已死"判断的代表性论述，存在几处值得讨论的立场：

- **"vibe coding 已死"过于绝对**。Vibe coding 在原型探索、一次性脚本、创意编程、教学场景仍有价值。Simon Willison 本人也强调"生产代码 ≠ 一次性代码"。把 vibe coding 视为"完全不可取"会低估其在低风险场景的效率。
- **"agent vs model 分工"过于刚性**。如前所述，2026 年的 agent 与 model 能力正在融合，框架化 agent（CrewAI、LangGraph、Anthropic SDK）的"agent"本身已包含规划/反思等高阶推理。
- **过度推崇 BMAD**。文章把 BMAD 作为唯一标杆方法论，但同样有 Braintrust 的 eval-driven、Anthropic 的 eval-driven、Hamel Husain 的"evals as the new PRD"等并行路径。多方法论并存才是 2026 年现实。
- **未充分量化成本**。"3-3-3 model"听起来吸引人，但未给出 3 天 / 3 周 / 3 个月的资源投入估计（团队规模、token 成本、人月工时）。Thoughtworks 作为商业咨询方有理由保留此信息，但对读者而言降低了可执行性。

### 七、真实性评估

| 声明 / 事实 | 验证状态 | 说明 |
| :--- | :--- | :--- |
| 2026 年 vibe coding 已不足 | **部分验证** | vibe coding 风险有 Veracode、CodeRabbit、GitClear、METR 等多项研究支持，但"完全过时"为作者立场判断 |
| BMAD Method 真实存在 | **已验证** | 官方仓库 `bmad-code-org/BMAD-METHOD`（48.5k stars, MIT）确认 |
| BMAD 工作流为 "plan-analysis-design-architect-dev-test" | **部分验证** | 该表述是对官方"analysis/planning/architecture/implementation"四阶段的**重新概括**，不是官方原始术语 |
| 3-3-3 交付模型 | **已验证** | Thoughtworks 官方页面确认为 AI/works™ 配套方法：3 天概念、3 周原型、3 个月 MVP |
| SpecKit 五步流水线 | **已验证** | 官方仓库 `github/spec-kit`（108k stars）确认为 constitution / specify / plan / tasks / implement |
| OpenSpec 三步工作流 | **已验证** | Fission-AI 仓库（52.3k stars）确认为 proposal / apply / archive |
| Claude 4.6 Sonnet | **已验证** | 2026 年 2 月 17 日发布，1M token 上下文、自适应思考能力 |
| Gemini 3.1 Pro | **已验证（但已非最新）** | 真实存在；2026 年 6 月时已被 3.5 系列部分取代 |
| GPT 5.3 Codex | **已验证（但已非最新）** | 2026 年 2 月 5 日发布；2026 年 3 月 5 日已被 GPT-5.4 取代 |
| GLM 5 | **已验证（但已非最新）** | 真实存在；2026 年 2 月已有 GLM-5.1 取代 |
| Antigravity 是 Google agent-first IDE | **部分验证** | 域名有效、属 Google 资产，但公开详情有限，定位与 Cursor/Windsurf 类似的判断为合理推测 |
| Claude Code / OpenCode / Cline / Cursor / Windsurf 列表 | **已验证** | 五者均确认存在；OpenCode 169k stars、Cline 62.6k stars、Cursor v3.6、Windsurf 已归 Cognition AI |
| `AGENTS.md` 由 Linux Foundation 托管 | **已验证** | 由 OpenAI/Amp/Google/Cursor/Factory 发起，2025–2026 移交 Linux Foundation 旗下 AAIF |
| 作者 Sunit Parekh 为 Thoughtworks 成员 | **已验证** | 文章页脚 /profiles/s/sunit-parekh 链接确认 |
| 发布日期 2026-03-18 | **已验证** | 文章 header 明确标注 |

### 八、总结

本文是 2026 年 AI-native engineering 议题的代表性行业论述。它把"AI 编程"从一个混沌议题**结构化为五大构件**——agent、model、methodology、spec、context——并以 Thoughtworks 自身方法论（BMAD、AI/works™、3-3-3 交付模型）为标杆，给出了"vibe coding 已死、thoughtful orchestration 当立"的核心判断。**真正的价值**在于提供了可治理、可评估、可投资的工程心智模型；**真正的局限**在于供应商视角与时间快照——文中引用的部分模型版本（GPT 5.3、GLM 5、Gemini 3.1 Pro）已在 3 个月内被新一代取代，部分方法论（BMAD 工作流表述、`.cursorrules`）也已不是当前主流。**读者应将其视为"范式框架"而非"工具清单"**——五大构件的层次结构比具体产品/版本号更值得长期记忆。

**关键要点：**

- **范式判断**：vibe coding 已被企业级 AI 工程抛弃，"编排"取代"提示"成为新的核心能力。
- **五大构件**：agent、model、methodology、spec、context——把 AI 编程拆解为可治理的工程栈。
- **模型专业化**：任务专属模型（代码、架构、测试、文档、安全）取代"一个模型打天下"。
- **方法论三角**：BMAD（多角色 agent）+ SpecKit（流水线规约）+ OpenSpec（轻量棕地）构成 2026 年 SDD 三大开源支柱。
- **上下文工程**：从 `AGENTS.md`、Agent Skills 到 "never-allow" 安全护栏，context 已成为 AI 编程的差异化要素。
- **时间快照局限**：模型版本号更新极快（GPT-5.3 → GPT-5.4 仅 1 个月），读者参考时需注意发布时点。

## 参考资料

- [Wikipedia: Vibe coding](https://en.wikipedia.org/wiki/Vibe_coding) — 核实 vibe coding 起源、定义与行业批评的研究证据
- [Thoughtworks Technology Radar Vol. 34](https://www.thoughtworks.com/en-us/radar) — 核实 context engineering 为 Adopt 级、context rot/instruction bloat 为 Caution 级的官方立场
- [Thoughtworks AI/works™](https://www.thoughtworks.com/en-us/ai/works) — 核实 3-3-3 交付模型与 AI/works 6 大能力的官方定义
- [Anthropic — Building effective agents](https://www.anthropic.com/research/building-effective-agents) — 核实 Orchestrator-Workers 模式与 agent 失效模式
- [Anthropic — Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) — 核实 Agent Skills 的渐进式披露机制
- [BMAD-METHOD on GitHub](https://github.com/bmad-code-org/BMAD-METHOD) — 核实 BMAD 框架、四阶段工作流、12+ 角色 agent 的官方说明
- [BMAD Method Documentation](https://docs.bmad-method.org/reference/workflow-map/) — 核实 BMAD Quick Flow 与 workflow map
- [GitHub Spec Kit](https://github.com/github/spec-kit) — 核实 SpecKit 五步流水线与官方 README
- [Fission-AI / OpenSpec](https://github.com/Fission-AI/OpenSpec) — 核实 OpenSpec 三步工作流（proposal / apply / archive）
- [agents.md](https://agents.md/) — 核实 AGENTS.md 规范与 Linux Foundation 托管信息
- [Cursor 官方 Context Rules 文档](https://cursor.com/docs/context/rules) — 核实 `.cursorrules` 已被 `.cursor/rules/*.mdc` 取代
- [philschmid — Context Engineering](https://www.philschmid.de/context-engineering) — 核实 context engineering 由 Tobi Lütke 起源、Karpathy 转推的传播链
- [Anthropic — Claude Sonnet 4.6 发布说明](https://www.anthropic.com/news/claude-sonnet-4-6) — 核实 Claude 4.6 Sonnet 于 2026-02-17 发布与规格
- [Hugging Face — zai-org/GLM-5.1](https://huggingface.co/zai-org/GLM-5.1) — 核实 GLM-5.1 在 2026 年 2 月发布、SWE-Bench Pro 58.4 等指标
- [Wikipedia — OpenAI Codex (AI agent)](https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)) — 核实 Codex CLI 与 GPT-5.3 / GPT-5.4 的发布时序
- [Google DeepMind — Gemini 模型页](https://deepmind.google/models/gemini/) — 核实 Gemini 3.1 / 3.5 系列发布状态
- [Alistair Cockburn — Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/) — 核实六边形架构的原始定义
- [OWASP — Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — 核实 LLM01/LLM02 等安全标准
- [Martin Fowler — Exploring Gen AI](https://martinfowler.com/articles/exploring-gen-ai.html) — 参考其对 Gen AI 工程的整体论述
