# SDD 项目一览表

| 项目 | 项目托管平台 | 作者 | 创建时间 | 主要开发<br>语言及框架 | Spec-Driven<br>Development | Coding<br>Agent | 项目说明 |
| :--- | :----------- | :--- | :------: | :--------------------: | :------------------------: | :-------------: | :------- |
| [Nexus Engine](https://github.com/developerz-ai/nexus-engine) | GitHub (0 Stars) | developerz-ai | 2026-05-17 | TypeScript<br>Rust, WGPU, Vercel AI SDK, MCP | 自研SDD ("No code is written until its spec exists"，规格树存储在 docs/) | nexus-coder, nexus-mcp-server | AI-first 跨平台游戏引擎，完全由 AI 构建和维护，支持 ECS 架构、headless operation、确定性回放 |
| [Skaro](https://github.com/skarodev/skaro) | GitHub (81 Stars) | skarodev | 2026-02-24 | Python<br>Svelte, JavaScript, FastAPI, Node.js | 自研SDD (.skaro/ 目录管理 artifacts，clarify→plan→implement→tests 工作流) | AI 协调层 | 开源 spec-driven 软件开发工作空间，开发者保持架构师角色，AI 作为执行者 |
| [Praxis OS](https://github.com/edward-hhai/praxis-os) | GitHub (7 Stars) | edward-hhai | 2025-10-27 | Python<br>MCP Server, LanceDB | 自研SDD (spec_creation_v1, spec_execution_v1 工作流，RAG 驱动语义搜索) | Cursor, Claude Code, Cline, GitHub Copilot | 开源 spec-driven 开发操作系统，结合 Universal CS Fundamentals、语言特定生成 |
| [BBShop](https://github.com/zig8953/BBShop) | GitHub (0 Stars) | zig8953 | 2026-05-30 | C#<br>ASP.NET Core 9, EF Core | 自研SDD (三阶段 SDLC 工作流程，YAML 状态机，SPEC.MD 为唯一真值来源) | Claude Code | 电子商务后端系统，实现产品目录、购物车、订单和库存管理 |
| [Open Mercato](https://github.com/open-mercato/open-mercato) | GitHub (1373 Stars) | open-mercato | 2025-09-10 | TypeScript<br>Next.js App Router, MikroORM | 自研SDD (.ai/specs/ 目录管理规格，AGENTS.md 定义 AI 代理规则) | Cursor, Claude Code, Codex | AI 工程基础框架，内置 CRM/ERP 模块，预置架构决策使 AI Agent 可基于既定规范构建应用 |

---

## Nexus Engine

- Repo URL：[Nexus Engine](https://github.com/developerz-ai/nexus-engine)
- 项目托管平台：GitHub
- 作者：developerz-ai
- 创建时间：2026-05-17
- 项目说明：AI-first 跨平台游戏引擎，"The Linux of game engines"。完全由 AI 构建和维护，支持 ECS 架构、headless operation、确定性回放。MIT 永久开源协议，无闭源变体，无版税，无单一人类维护者作为故障点。
- 主要开发语言：TypeScript (80.1%)、Rust (18.3%)、Shell (1.6%)
- 主要开发框架：WGPU (WebGPU)、Vercel AI SDK + OpenRouter、Model Context Protocol (MCP)
- Spec-Driven Development：核心原则："No code is written until its spec exists"。完整规格树存储在 `docs/` 目录，涵盖架构、合约、子系统、AI 智能体协议。所有代码行都根据规格进行评判。贡献工作流程：1. 阅读 constitution (vision.md) 2. 阅读 binding laws (principles.md) 3. 找到或编写变更规格 4. 先写测试 5. 实现 6. 提交 PR
- Coding Agent：项目内置 nexus-coder（内置 AI 编程智能体，使用 Vercel AI SDK + OpenRouter，支持大规模并行执行，模型可热插拔）、nexus-mcp-server（MCP 服务器，支持 Claude Desktop、Claude Code、Cursor、Zed、ChatGPT Desktop、browser 等多种 AI 主机）、项目提供 118 个专业 AI subagents

---

## Skaro

- Repo URL：[Skaro](https://github.com/skarodev/skaro)
- 项目托管平台：GitHub
- 作者：skarodev
- 创建时间：2026-02-24
- 项目说明：开源 spec-driven 软件开发工作空间。开发者保持架构师角色，AI 作为执行者。支持架构审查、ADR、DevPlans、逐步任务执行、Git 集成、模型使用分析和特定技术栈指令集。
- 主要开发语言：Python (52.8%)、Svelte (35.4%)、JavaScript (10.1%)
- 主要开发框架：FastAPI (后端)、Svelte (前端)、Node.js 18+ (dashboard)
- Spec-Driven Development：项目 artifacts 存储在 `.skaro/` 目录，与代码版本控制共存；包含 constitution、architecture、ADR 等规范文档；任务遵循固定工作流：clarify → plan → implement → tests；完成度经验证而非假定的；AI 在定义的边界内工作，而非依赖临时 prompting
- Coding Agent：项目作为 AI 协调层，支持可配置的 LLM 提供商、模型、skills 和技术栈特定指令集。提供"repository-aware context"机制，让 AI 获得与当前步骤相关的聚焦上下文，而非全量代码库。AI 行为可配置，支持不同模型、提供商和技能。

---

## Praxis OS

- Repo URL：[Praxis OS](https://github.com/edward-hhai/praxis-os)
- 项目托管平台：GitHub
- 作者：edward-hhai
- 创建时间：2025-10-27
- 项目说明：开源 spec-driven 开发操作系统，结合 Universal CS Fundamentals（适用于任何语言的通用模式）、语言特定生成（LLM 为每个项目生成定制化指导）、MCP RAG Server（语义搜索标准，上下文减少 90%）、专业 Sub-Agents（设计验证、并发分析、测试生成）。支持对话式安装，AI Agent 自动完成安装和配置。
- 主要开发语言：Python (98.2%)、Shell (1.8%)
- 主要开发框架：MCP (Model Context Protocol) Server、LanceDB 向量数据库、Phase-gated workflows
- Spec-Driven Development：项目包含完整的 SDD 工作流定义：`spec_creation_v1` 工作流（规范创建阶段）、`spec_execution_v1` 工作流（规范执行阶段）；标准通过 `.praxis-os/` 目录分发到项目，RAG 驱动的语义搜索提供检索；阶段门控工作流确保规范执行的可控性
- Coding Agent：明确支持多种 AI Coding Agent：Cursor（通过 `.cursorrules` 触发行为）、Claude Code（通过 `.claude/CLAUDE.md` 配置）、Cline（通过 `.clinerules` 触发行为）、GitHub Copilot（通过 `.github/copilot-instructions.md` 配置）；安装方式：用户只需对 AI Agent 说 "Install prAxIs OS from github.com/honeyhiveai/praxis-os for [Agent]" 即可自动完成安装

---

## BBShop

- Repo URL：[BBShop](https://github.com/zig8953/BBShop)
- 项目托管平台：GitHub
- 作者：zig8953（个人）
- 创建时间：2026-05-30
- 项目说明：BBShop 是一个电子商务后端系统，实现核心在线商店场景，包括产品目录、购物车、订单和库存管理。该项目采用 Spec-Driven Development (SDD) 方法论，通过结构化的三阶段 SDLC 流程（分析→设计→实现）开发，每个阶段有明确的工件和审批门槛。
- 主要开发语言：C#
- 主要开发框架：ASP.NET Core 9, Entity Framework Core, FluentValidation, Serilog, OpenTelemetry, Docker, Docker Compose
- Spec-Driven Development：项目采用完整的三阶段 SDLC 工作流程：1) 分析阶段 (`.spec/01-analysis.md`) - 定义问题陈述和范围；2) 设计阶段 (`.spec/02-design.md`) - 创建技术规格；3) 实现阶段 (`.spec/implementation/`) - AI 根据已批准的规格生成代码。所有工件使用 YAML 前置元数据定义状态 (DRAFT → READY_FOR_REVIEW → APPROVED)，并通过状态机确保下游阶段只能消费已 APPROVED 的上游工件。规格文档 (SPEC.MD) 作为唯一真值来源，所有实现必须严格遵循规格。
- Coding Agent：项目使用 Claude Code 作为主要 AI 编码助手。CLAUDE.md 文件定义了 AI 助手的工作规则，要求在实现任何功能前先阅读 SPEC.MD，并遵循 WORKFLOW.MD 定义的 SDLC 流程。WORKFLOW.MD 详细描述了状态转换规则、失效级联机制和审计日志，确保 AI 的行为被严格限定在定义的规格内。

---

## Open Mercato

- Repo URL：[Open Mercato](https://github.com/open-mercato/open-mercato)
- 项目托管平台：GitHub
- 作者：open-mercato
- 创建时间：2025-09-10
- 项目说明：Open Mercato 是一个 AI 工程基础框架（AI-Engineering Foundation Framework），内置 CRM/ERP 模块（多租户、RBAC、事件流、定价、销售流程等），旨在让 AI 编码代理（Cursor、Claude Code、Codex）能够基于预定义的架构决策和规范进行开发，而非重复造轮子。项目采用 spec-first 开发方式，所有规格文档存储在 `.ai/specs/` 目录，AI 输出具有可重现性。
- 主要开发语言：TypeScript (92.7%)
- 主要开发框架：Next.js App Router, MikroORM, PostgreSQL, Redis, Awilix DI
- Spec-Driven Development：采用 spec-first 开发方法，新功能或重大变更前需在 `.ai/specs/` 文件夹中编写设计规范；规范文档使用 `{YYYY-MM-DD}-{title}.md` 命名格式；规范文档包含：TLDR、概述、问题陈述、解决方案、架构、数据模型、API 契约、风险与影响评估、合规报告、变更日志；`.ai/specs/AGENTS.md` 定义了 AI 代理规则：实施前检查 OSS 和企业版规范目录、创建新规范时需更新规范、保持规范与代码同步；规范分离：`.ai/specs/` 包含开源版规范，`.ai/specs/enterprise/` 包含企业版规范
- Coding Agent：支持多种 AI 编码代理：Cursor、Claude Code、Codex；项目提供 Claude Code 沙盒实例，可在 30 秒内启动包含 Claude Code、Codex、VS Code 和 Open Mercato 的开发环境；`.ai/skills/` 目录包含多种技能配置，支持 AI 代理的自主工作流程；AI 助手内置于管理页面，代理按模块、权限和工具允许列表进行作用域控制