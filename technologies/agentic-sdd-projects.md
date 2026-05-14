# SDD + AI Coding 优秀开源项目参考

报告生成时间：2026-06-05

## 评估方法

本报告通过 5 个独立研究代理（general-purpose agents）从 GitHub、GitLab、Bitbucket、知名技术博客（Hacker News、Reddit r/ClaudeAI）、Awesome 列表、GitHub Trending、Anthropic / OpenAI / Cursor / Aider 官方博客、知名开发者博客（Simon Willison、Addy Osmani 等）多源搜索，共发现 250+ 候选项目（已 WebFetch 验证 URL 200 OK，5+ 源交叉验证）。经去重、交叉验证、冲突解决后，筛选出**同时高度实践 SDD 与 AI Coding**、**完整且开源**、**文档充分**的代表性项目。

## 评估维度

1. **AI Coding 实践度** — 项目的开发是否使用 AI 工具（如 CLAUDE.md、AGENTS.md、AI 协作开发流程、AI 代理编排）
2. **SDD 实践度** — 项目是否真正使用 Spec-Driven Development 方法（specs/ 目录、规范模板、spec-first 工作流、spec → implementation 流程）
3. **文档完善度** — 关于 AI Coding 和 SDD 最佳实践的说明文档质量
4. **社区活跃度** — GitHub stars、贡献者数量、最近活动、采用率
5. **项目完整度** — 项目是否完整、生产可用、架构合理

## 推荐列表

| Project | Platform | Stars | Author | Created At | Main Language | Main Framework | Description |
| :------ | :------- | :---- | :----- | :--------: | :------------ | :------------- | :---------- |
| [github/spec-kit](https://github.com/github/spec-kit) | GitHub | 109k | GitHub | 2025-07 | Python | Specify CLI | GitHub 官方出品的 SDD 工具包，constitution→specify→clarify→plan→tasks→implement 完整六阶段流程；支持 30+ AI 编码代理（Claude Code、Codex、Cursor、Copilot、Gemini CLI），模板化 CLAUDE-template.md 与 AGENTS.md 注入，事实标准制定者 |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | GitHub | 53k | Fission AI | 2025-08 | TypeScript | Node.js CLI | "SDD for AI coding assistants" 旗手，proposal/specs/design/tasks 四件套；支持 25+ AI 工具，原生 AGENTS.md，Propose→Apply→Archive 三步走，brownfield（存量项目）友好 |
| [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | GitHub | 48.6k | BMad Code LLC | 2024 | JavaScript | npx CLI + Web Bundles | AI 敏捷开发方法论，12+ 专业代理角色（PM/架构师/开发/UX/QA）协作，Party Mode 多代理会议，PRD→Stories→Dev→QA gate 完整流程，跨平台分发（Gemini/ChatGPT 适配） |
| [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | GitHub | 63.9k | TÂCHES (gsd-build) | 2024 | JavaScript | Claude Code Plugin | 极简 meta-prompting + 上下文工程 + SDD 三位一体，专为 Claude Code 设计；spec→plan→execute 循环，PRD/路线图/阶段产物 78 个 release，meta-prompting 范式标杆 |
| [kirodotdev/Kiro](https://github.com/kirodotdev/Kiro) | GitHub | 3.8k | Amazon | 2025-07 | TypeScript | Kiro IDE/CLI | AWS 出品 agentic IDE，原生 `.kiro/specs/` 结构化规范，Requirements→Design→Tasks→Implementation 完整 4 阶段，Hooks/Steering/MCP 全栈集成 |
| [awslabs/aidlc-workflows](https://github.com/awslabs/aidlc-workflows) | GitHub | 2.7k | AWS Labs | 2025 | Python | AI-DLC 规则驱动 | AWS 官方 AI-DLC（AI-Driven Development Lifecycle），三阶段自适应工作流 Inception→Construction→Operations，方法论先行、agent 无关，企业级 |
| [gotalab/cc-sdd](https://github.com/gotalab/cc-sdd) | GitHub | 3.4k | Gota Lab | 2025 | TypeScript | Agent Skills 17 套 | 极简可适配 SDD harness，spec 即合约，TDD RED→GREEN，单一 Skill 一次注入 8 个 AI agent（Claude/Codex/Cursor/Copilot/Windsurf/OpenCode/Gemini/Antigravity），跨代理覆盖最广 |
| [Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp) | GitHub | 4.2k | Pimzino | 2025 | TypeScript | MCP Server | MCP 标准化 SDD 工具，结构化 Requirements→Design→Tasks 工作流，VSCode 扩展 + Web 实时仪表盘 + 审批流，支持 Claude/Cursor/Windsurf/Cline/Continue/Codex |
| [Pimzino/claude-code-spec-workflow](https://github.com/Pimzino/claude-code-spec-workflow) | GitHub | 3.8k | Pimzino | 2024 | TypeScript | Claude Code | 专为 Claude Code 设计的 4 阶段 SDD 工作流（需求/设计/任务/实现），Report→Analyze→Fix→Verify 修复流，steering 文档机制，60-80% token 节省 |
| [Priivacy-ai/spec-kitty](https://github.com/Priivacy-ai/spec-kitty) | GitHub | 1.3k | Priivacy AI | 2025 | Python | spec-kitty CLI + Kanban | 严肃软件工程师的 SDD 框架，spec→plan→tasks→next→review→accept→merge 完整链，支持多 AI 工具，git worktrees 隔离并行 + 自动合并，本地 Kanban 仪表盘 |
| [potpie-ai/potpie](https://github.com/potpie-ai/potpie) | GitHub | 5.4k | Potpie AI | 2024 | Python | FastAPI + Neo4j | "Spec-driven development for large codebases"，基于代码库知识图谱 + Spec Agent 自动生成 PRD，面向大型代码库的 SDD 实践代表 |
| [modu-ai/moai-adk](https://github.com/modu-ai/moai-adk) | GitHub | 1.1k | Modu AI | 2024 | Go | MoAI ADK | SPEC-First Agentic Development Kit，EARS 格式 SPEC，24 AI agent + 52 skill，Plan→Run→Sync 流水线，TRUST 5 质量门禁，4 语言文档，单二进制零依赖 |
| [MrLesk/Backlog.md](https://github.com/MrLesk/Backlog.md) | GitHub | 5.7k | MrLesk | 2024 | TypeScript | Bun + MCP | "Built for spec-driven AI development"，Markdown-native 任务管理 + Kanban + Web 浏览器，CLI + MCP 的 spec-driven AI 开发循环，186 个 release 持续演进 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | GitHub | 48.4k | Addy Osmani | 2025 | Shell+JS | 多 AI Agent 技能包 | Google Chrome 团队工程总监出品，23 个 SKILL.md 生产级技能（含 spec-driven-development），跨多 AI agent（Claude/Cursor/Codex）即装即用 |
| [garrytan/gstack](https://github.com/garrytan/gstack) | GitHub | 107k | Garry Tan (Y Combinator CEO) | 2025 | TypeScript | Bun + Markdown | 23 个角色化工具（CEO/设计师/工程经理/发布经理/QA），/spec 五阶段精确 spec 化，Codex 质量门禁，完整 review 链路 |
| [buildermethods/agent-os](https://github.com/buildermethods/agent-os) | GitHub | 4.8k | Brian Casel | 2025 | Shell | 工具无关 | "Agents that build the way you would"，自动发现/部署/塑造 codebase 标准并撰写更好 spec，注入式系统兼容 Claude/Cursor/Antigravity |
| [maxritter/pilot-shell](https://github.com/maxritter/pilot-shell) | GitHub | 1.7k | Max Ritter | 2025 | TypeScript + Python | Claude Code + Codex | 真实工程师的 Claude Code/Codex 实践集，spec-driven 规划 + 强制 TDD + 持久化记忆 + 质量门禁，跨工具桥接的 shell 包装 |
| [phodal/routa](https://github.com/phodal/routa) | GitHub | 1.6k | Phodal | 2025 | TypeScript + Rust | Next.js + Tauri | Board-as-spec 看板即规范，ROUTA/CRAFTER/GATE 严格证据链，YAML 外化角色定义，INVEST 检查的 YAML 契约，工作区优先多代理协调 |
| [Gentleman-Programming/agent-teams-lite](https://github.com/Gentleman-Programming/agent-teams-lite) | GitHub | 1.2k | Gentleman Programming | 2024 | Shell | Markdown 编排 | 编排器 + 9 个专业子智能体（spec→orchestrator→sub-agents→verification），纯 Markdown 零依赖即开即用，跨 Claude Code/OpenCode/Cursor |
| [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | GitHub | 208k | affaan-m | 2025 | 多语言 | 跨 harness | 251 skill + 63 sub-agent + TDD 闭环 + AgentShield 安全审计，跨 8+ AI 平台（Claude/Codex/Cursor/Gemini），研究优先范式 |
| [wasp-lang/open-saas](https://github.com/wasp-lang/open-saas) | GitHub | 14.6k | Wasp | 2025 | TypeScript | Wasp 全栈 | AI-Ready 全栈 SaaS 启动器，内置 AGENTS.md + skills + Claude Code plugin，认证/支付/邮件/分析全栈模板，把 AI Coding 落地到生产的产品级案例 |
| [agentsmd/agents.md](https://github.com/agentsmd/agents.md) | GitHub | 22k | agents.md | 2024 | TypeScript | Next.js | AGENTS.md 开放标准本身，README 即规约，被 Claude Code、Cursor、Codex 等共同采纳为 AI 代理指导文件规范的事实标准 |
| [microsoft/skills](https://github.com/microsoft/skills) | GitHub | 2.5k | Microsoft | 2025 | TypeScript | Astro Docs | 微软官方 Context-Driven Development，174 技能 + AGENTS.md 模板，Ralf Loop 验证，配套 Skill Explorer 站点，覆盖 Python/.NET/TS/Java/Rust 等 SDK |
| [Engineering4AI/awesome-spec-driven-development](https://github.com/Engineering4AI/awesome-spec-driven-development) | GitHub | 176 | Engineering4AI | 2025-11 | Markdown | Awesome List | 唯一专门 curate SDD 工具链的 awesome list，按工具/标准/工作流/MCP 分类，是研究 SDD 生态的最佳入口 |
| [gsd-build/gsd-2](https://github.com/gsd-build/gsd-2) | GitHub | 7.7k | gsd-build | 2025 | TypeScript | GSD 2.0 | GSD 升级版，强调长周期自治代理与智能压缩，VSCode 扩展 + Studio + Web + Docker 多端，自研 orchestrator |

## 重点关注项目（用于启动 AI Native SDD 新项目参考）

如果只能参考**少数几个项目**来启动新的 AI Native + SDD 项目，建议按以下优先级深入研究：

### 第一梯队（SDD 标杆 + 主流 AI 编码代理兼容）

1. **[github/spec-kit](https://github.com/github/spec-kit)** — GitHub 官方标准，六阶段流程完整
2. **[Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)** — 25+ AI 工具兼容，brownfield 友好
3. **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** — MCP 标准化，跨工具通用

### 第二梯队（多代理协作 + 工业级质量）

4. **[bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)** — 多代理角色协作
5. **[modu-ai/moai-adk](https://github.com/modu-ai/moai-adk)** — SPEC-First + TRUST 5 质量门禁
6. **[Priivacy-ai/spec-kitty](https://github.com/Priivacy-ai/spec-kitty)** — 团队级工程化（Kanban + worktree）

### 第三梯队（特定场景最佳实践）

7. **[kirodotdev/Kiro](https://github.com/kirodotdev/Kiro)** — AWS agentic IDE 体验参考
8. **[potpie-ai/potpie](https://github.com/potpie-ai/potpie)** — 大型代码库 SDD 参考
9. **[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)** — Google Chrome 团队生产级技能库

## 候选池（其他值得关注的项目）

| Project | Platform | Stars | Author | Created At | Main Language | Main Framework | Description |
| :------ | :------- | :---- | :----- | :--------: | :------------ | :------------- | :---------- |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | GitHub | 35.8k | Yeachan Heo | 2025 | TypeScript | Claude Code + tmux | 19 个多 agent 编排，team/autopilot/ralph/ultrawork 多模式，自动 skill 提取 |
| [coleam00/Archon](https://github.com/coleam00/Archon) | GitHub | 22.2k | Cole Medin | 2025 | TypeScript | Bun | 首个开源 AI coding harness 构建器，YAML 工作流引擎，fire-and-forget 模式 |
| [Davila7/claude-code-templates](https://github.com/Davila7/claude-code-templates) | GitHub | 27.8k | Davila7 | 2025 | Python | npx CLI | Claude Code 配置模板聚合仓库（agents/commands/MCPs/hooks/skills），生态分发枢纽 |
| [ariel-frischer/autospec](https://github.com/ariel-frischer/autospec) | GitHub | 134 | ariel-frischer | 2025 | Go | 单二进制 CLI | YAML 优先 spec→plan→tasks→implement，程序化校验，bounded session 节省 80% 成本 |
| [open-mercato/open-mercato](https://github.com/open-mercato/open-mercato) | GitHub | 1.4k | open-mercato | 2024 | TypeScript | Next.js + MikroORM | 真实生产项目，独立"Spec Driven Development"章节与 `.ai/specs/` 目录，架构感知 AI 工具链 |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | GitHub | 960 | Lokesh | 2025 | Python + TS | Multi-CLI | 41 agent 类型 + 8 swarm，RARV-C 闭环，11 个质量门禁 + 反谄媚检查 |
| [catlog22/Claude-Code-Workflow](https://github.com/catlog22/Claude-Code-Workflow) | GitHub | 2.1k | catlog22 | 2025 | TypeScript | JSON-driven | Team Architecture v2 事件驱动 beat 模型，多 CLI 编排（Gemini/Codex/Qwen） |
| [liatrio-labs/spec-driven-workflow](https://github.com/liatrio-labs/spec-driven-workflow) | GitHub | 85 | Liatrio | 2025 | Python | Skill | 技能优先的 SDD 4 步工作流，跨 Claude/Cursor/Windsurf/Codex 工具 |
| [formulahendry/mcp-server-spec-driven-development](https://github.com/formulahendry/mcp-server-spec-driven-development) | GitHub | 430 | formulahendry | 2025 | TypeScript | MCP Server | EARS 需求格式 + 3 个 MCP prompt（需求/设计/代码），小巧即用 |
| [calderbuild/VibeDoc](https://github.com/calderbuild/VibeDoc) | GitHub | 375 | calderbuild | 2025 | Python | Gradio | AI 产品经理 + 架构师，自动生成结构化开发计划 + 模块级 prompt 模板 |
| [madebyaris/spec-kit-command-cursor](https://github.com/madebyaris/spec-kit-command-cursor) | GitHub | 183 | madebyaris | 2025 | Shell + Python | Cursor Plugin | 显式声明 "Spec-Driven Development for Cursor IDE"，6 子智能体 + 5 技能 |
| [centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup) | GitHub | 2.4k | centminmod | 2025 | Python | Memory Bank | 双内存 CLAUDE.md 模板 + memory bank，3 套渐进式披露模板，Anthropic 最佳实践 |
| [OneRedOak/claude-code-workflows](https://github.com/OneRedOak/claude-code-workflows) | GitHub | 3.8k | OneRedOak | 2025 | Markdown | Claude Code + GH Actions | 三大评审 workflow（code/design/security）+ Playwright MCP 自动化 |
| [shot-gun-sh/shotgun](https://github.com/shot-gun-sh/shotgun) | GitHub | 677 | shotgun-sh | 2025 | Python | CLI | 代码库感知 spec 撰写，研究优先 + codebase-aware SDD 工作流 |
| [tzachbon/smart-ralph](https://github.com/tzachbon/smart-ralph) | GitHub | 339 | tzachbon | 2026-01 | Shell | Claude Code Plugin | Ralph Wiggum 循环 + Claude Code，spec-driven research→requirements→design→tasks→execution |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | GitHub | 130k | Anthropic | 2024 | Python + Node | Agentic CLI | Claude Code 官方仓库，130k Stars，agentic 编码工具事实标准 |
| [Aider-AI/aider](https://github.com/Aider-AI/aider) | GitHub | 45.8k | Aider-AI | 2023 | Python | Terminal AI Pair | 终端 AI 结对编程工具，仓库地图 + git 集成，事实标准 |
| [continuedev/continue](https://github.com/continuedev/continue) | GitHub | 33.5k | Continue | 2023 | TypeScript | VSCode/JetBrains | 开源 AI 编码助手，源受控 AI 检查 + CI 强制执行 |
| [TabbyML/tabby](https://github.com/TabbyML/tabby) | GitHub | 33.6k | TabbyML | 2023 | Rust | 自托管 AI | 自托管 on-prem AI 编码助手，MODEL_SPEC.md 规范 |
| [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) | GitHub | 24.9k | Alibaba | 2025 | TypeScript | esbuild | 通义千问官方终端 agent，Skills + SubAgents，Terminal-Bench 37.5% |
| [Plandex-AI/plandex](https://github.com/Plandex-AI/plandex) | GitHub | 15.4k | Plandex | 2024 | Go | CLI | 规划先行 AI agent，2M token 上下文，tree-sitter 项目映射，plan 版本控制 |
| [sst/opencode](https://github.com/sst/opencode) | GitHub | 170k | SST | 2024 | TypeScript | Bun + SST | "The open source AI coding agent"，build/plan 双模式，含 specs/ 与 AGENTS.md |
| [opencode-ai/opencode](https://github.com/opencode-ai/opencode) | GitHub | 12.8k | opencode-ai | 2024 | Go | Bubble Tea + Cobra | 终端 AI 编码工具，Go 编写，多 LLM provider |
| [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | GitHub | 5k | Microsoft | 2025 | Python | Gradio | 文本空间 skill 优化器，自动迭代 prompt 训练，300-2000 token 紧凑产物 |
| [getcursor/cursor](https://github.com/getcursor/cursor) | GitHub | 32.9k | Cursor | 2022 | N/A | Stub Repo | Cursor 商业 IDE 仓库（实际产品闭源），影响力大但开源贡献低 |

## 调研方法论说明

- **数据源**: GitHub、GitLab、知名技术博客（Hacker News、Reddit r/ClaudeAI、r/LocalLLaMA）、Awesome 列表、GitHub Trending、AI 公司官方博客（Anthropic、OpenAI、Cursor、Aider）、知名开发者博客（Simon Willison、Addy Osmani）
- **搜索关键词（中英双语）**: "Spec-Driven Development"、"spec driven"、"AI Coding"、"Claude Code"、"specification first"、"AI native development"、"规范驱动开发"、"AI 编程"、AGENTS.md、CLAUDE.md、specs/、spec-kit
- **URL 验证**: 所有项目均经 WebFetch 验证 200 OK 可访问
- **交叉验证**: 每个项目至少在 5 个独立可信来源中被提及或验证
- **冲突解决**: 对不同代理报告中的 star 数、创建时间等元数据冲突，按 GitHub 当前数据为准
- **去重**: 5 个代理共发现 250+ 候选，去重后保留 ~50 个代表性项目

## 给新项目的启示

启动 AI Native + SDD 新项目时，建议：

1. **选定 SDD 工具链**: 从 spec-kit（标准）或 OpenSpec（灵活）二选一作为基础
2. **选择 AI 编码代理**: Claude Code 生态最丰富（spec-kit、OpenSpec、gsd、Pimzino 系列、cc-sdd 等均原生支持）；Codex 适合追求快速简洁
3. **建立 SDD 流程**: Constitution → Spec → Plan → Tasks → Implement 五阶段
4. **集成多代理**: 参考 BMAD-METHOD、modu-ai/moai-adk 的角色化代理设计
5. **质量门禁**: 借鉴 TRUST 5（modu-ai）、RARV-C（loki-mode）等质量框架
6. **文档化最佳实践**: 在项目中维护 `CLAUDE.md` / `AGENTS.md` / `specs/` 三个核心目录
