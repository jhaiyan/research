# 深度研究报告：Harness Engineering（驾驭工程）

- 报告生成时间：2026-05-15 17:00
- 主题类型：概念、方法论

## 概述

- 提出方：Mitchell Hashimoto（2026 年 2 月 5 日首次提出），OpenAI（2026 年 2 月 17 日正式命名），Anthropic（2025 年 11 月实质相同的实践方法论）
- 提出时间：2026 年 2 月 5 日（Mitchell Hashimoto 首次提出「harness engineering」概念），2026 年 2 月 17 日（OpenAI 正式命名），2025 年 11 月 26 日（Anthropic 实质相同的实践方法论更早出现）
- 领域：AI Agent 工程化、LLM 应用架构、软件开发方法论

Harness Engineering（驾驭工程）是一种将 AI Agent 系统工程化的方法论，核心理念是 **「Agent = Model + Harness」**——AI Agent 的成功不仅取决于底层模型能力，更取决于围绕模型构建的「驾驭系统」（harness）的设计质量。该概念由 **Mitchell Hashimoto 于 2026 年 2 月 5 日首次提出**（比 OpenAI 早 12 天），定义为「任何时候发现 agent 犯错，都花时间设计解决方案防止 agent 再犯同样的错误」。随后 OpenAI 于 2026 年 2 月 17 日正式命名并广泛传播，Anthropic 的实践方法论（2025 年 11 月）实质相同但未用此名称。该方法论涵盖上下文管理、工具接口设计、验证循环、记忆系统、权限体系等核心组件，强调通过系统化的工程实践提升 AI Agent 的可靠性、可控性和可维护性。其核心转变在于：传统工程是人类写代码交由机器执行，而 Harness Engineering 是人类设计约束系统（AGENTS.md、架构规则、自定义 linter、反馈回路），由智能体在约束内自主编写代码，机器执行验证。

## 提出背景/解决的核心问题

### 背景

随着 GPT-4、Claude Opus 4、GPT-5 等强大语言模型的诞生，AI 编码能力取得显著进步。然而在实际项目中，模型本身的能力并不能直接转化为可靠的代码产出。研究发现，即使是最先进的模型，在没有适当工程化支持下，仍然会在复杂项目中失败。

这一现象的根源在于：AI 智能体需要一个完整的「操作系统」来有效地执行任务，而这个「操作系统」就是 Harness。正如物理计算机需要操作系统来管理硬件资源一样，AI 智能体需要一个 Harness 来管理上下文、工具、验证和状态。

### 要解决的核心问题

1. **上下文窗口限制与 context rot**：长时运行代理需要在多个上下文窗口间工作，新会话开始时无记忆；随着上下文窗口填充，模型性能会下降
2. **自我评估偏差**：代理倾向于「自信地赞扬自己的工作」，即使质量平庸
3. **上下文焦虑**：模型在接近感知上下文限制时可能过早结束
4. **失败模式复杂**：非确定性系统的新失败模式随模型改进而不断涌现
5. **验证循环缺失**：缺乏有效的反馈机制来确认智能体输出是否正确
6. **状态持久化不足**：长时间运行任务中断后无法从断点恢复
7. **框架 vs Harness 的混淆**：很多团队试图用「框架」解决问题，但框架自己构建重试逻辑、状态持久化、任务队列等，导致重复工作

### 核心解决思路

Harness Engineering 提出将 AI Agent 的智能（模型）与使其智能可操作的系统（harness）分离。根据 LangChain 的定义：**Agent = Model + Harness**，即代理由模型提供智能，由 harness 使其智能可操作。

关键原则：
- 代理输出不佳几乎总是 harness 问题，而非模型问题
- 好的 harness 不应消除人类输入，而应引导人类输入到最重要的地方
- 迭代改进：将观察到的失败模式反馈到 harness 优化中

## 发展历程

- **2024 年 12 月 19 日** Anthropic 发表 [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)，提出工作流与代理的架构区分、五种工作流模式
- **2025 年 11 月 26 日** Anthropic 发表 [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)，首次系统阐述长时间运行 Agent 的 harness 设计方法论（双 Agent 架构：Initializer Agent + Coding Agent）
- **2026 年 2 月 5 日** Mitchell Hashimoto（Terraform、Vagrant 作者）发表 [My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey)，**首次提出「Harness Engineering」概念**，定义为「任何时候发现 agent 犯错，都花时间设计解决方案防止 agent 再犯同样的错误」，比 OpenAI 早 12 天
- **2026 年 2 月 17 日** OpenAI 发表 [Harness Engineering: Harnessing Codex in an Agent-First World](https://openai.com/index/harness-engineering/)，**正式命名「Harness Engineering」术语**（在 Mitchell Hashimoto 之后）
- **2026 年 2 月 17 日** Martin Fowler 发表早期备忘录，首次阐述「Agent = Model + Harness」概念
- **2026 年 2 月 17 日** LangChain 发表 [Improving Deep Agents with harness engineering](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering)，展示通过 harness 优化将 Terminal Bench 2.0 分数从 52.8 提升至 66.5（+13.7 分）
- **2026 年 3 月 3 日** Inngest 发表 [Your Agent Needs a Harness, Not a Framework](https://www.inngest.com/blog/your-agent-needs-a-harness-not-a-framework)，强调状态管理、重试、追踪作为一等基础设施
- **2026 年 3 月 10 日** LangChain 发表 [The Anatomy of an Agent Harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness)，系统解构 Agent Harness 的核心组件
- **2026 年 3 月 12 日** HumanLayer 发表 [Skill Issue: Harness Engineering for Coding Agents](https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents)，论证弱结果通常是 Harness 问题而非模型问题
- **2026 年 3 月 24 日** Anthropic 发表 [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)，提出 Generator-evaluator 架构、Sprint Contract 等设计模式
- **2026 年 4 月 2 日** Thoughtworks 的 Birgitta Böckeler 发表 [Harness Engineering Framework](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html)，建立系统性双控制系统理论框架
- **2026 年 3 月** 学术论文《Harness Engineering for Language Agents (CAR decomposition)》发布在预印本平台，提出控制-代理-运行时（CAR）分解框架

## 适用场景

### 场景 1：长时间运行的编码任务

Harness Engineering 最典型的应用场景是复杂代码项目的持续开发。通过双 Agent 架构、feature list 追踪、init.sh 脚本初始化，Agent 可以在多个会话中持续推进工作而不丢失上下文。

**代表案例**：Anthropic 展示的 full-stack web app 克隆项目，跨越多个上下文窗口完成复杂功能。

### 场景 2：需要严格验证的生产环境开发

在需要保证代码质量和正确性的场景中，Harness 的验证循环确保每个功能都经过测试验证。生成器-评估器模式特别适合主观质量评估（如 UI 设计），因为没有二进制的正确性标准。

**代表案例**：Digital Audio Workstation (DAW) 项目，三次构建-QA 循环后产出可用的浏览器音乐制作程序。

### 场景 3：多 Agent 协作系统

当多个 Agent 需要协同工作时（如规划 Agent、执行 Agent、评估 Agent），Harness 提供了 Agent 间通信、状态共享和职责分离的框架。

**代表案例**：三 Agent 架构（Planner-Generator-Evaluator）的 Retro Game Maker 应用，16 个功能跨 10 个 sprints 完成。

### 场景 4：需要 Human-in-the-Loop 的复杂决策

在关键决策点需要人类审核的场景中，Harness 可以设计战略性 checkpoint，让人类在关键时刻介入而非全程监控。

### 场景 5：前端设计与创意迭代

GAN 风格的设计-评估循环非常适合 UI/UX 设计，评估 Agent 使用 Playwright MCP 与实际页面交互，通过截图和详细评估驱动美学演进。

**代表案例**：迭代 10 轮后的博物馆级空间 3D CSS 设计，展示了远超初始方案的创意产出。

## 技术信息

### 核心公式：Agent = Model + Harness

Harness 涵盖了除 AI 模型本身之外的一切：

- **系统提示词**（System Prompts）：引导 Agent 行为
- **工具/MCPs**（Tools/Skills/MCPs）：Agent 与外部世界交互的接口
- **基础设施**（Bundled Infrastructure）：文件系统、沙箱、浏览器环境
- **编排逻辑**（Orchestration Logic）：子 Agent 生成、模型路由
- **Hooks/Middleware**：压缩、继续执行等确定性逻辑

### 控制机制：Guides（前馈）与 Sensors（反馈）

**Guides（前馈控制）**：
- 在 Agent 行动前 anticipatory 影响行为
- 目的是提高首次尝试成功的概率
- 示例：系统提示词、工具描述、规格说明、AGENTS.md

**Sensors（反馈控制）**：
- 在 Agent 行动后观察结果
- 启用自我纠正循环
- 示例：测试、linter、类型检查、AI 代码审查

### 执行类型

| 类型 | 特征 | 示例 | 延迟 |
|------|------|------|------|
| Computational | 确定性、CPU 密集、快速 | 测试、linter、类型检查、结构分析 | 毫秒到秒级 |
| Inferential | 语义分析、GPU/NPU 密集、概率性 | AI 代码审查、突变测试 | 秒到分钟级 |

### 三种调节类别（Martin Fowler 框架）

| 类别 | 目标 | 实现方式 |
|------|------|----------|
| **Maintainability Harness** | 结构质量 | 重复检测、复杂度检查、风格强制 |
| **Architecture Fitness Harness** | 架构特性 | 架构特征定义与检查（Fitness Functions） |
| **Behaviour Harness** | 功能行为 | 引导/感知功能行为（当前最薄弱环节） |

### 五 Harness 子系统模型

根据 Learn Harness Engineering 课程，Harness 包含五个核心子系统：

1. **Instructions（指令）**：渐进式引导 Agent 行为（非巨型文件）
2. **State Management（状态管理）**：跨会话追踪进度
3. **Verification（验证）**：测试通过作为完成证据
4. **Scope Control（范围控制）**：限制 Agent 单一功能工作
5. **Session Lifecycle（会话生命周期）**：从初始化到干净交接的程序

### 关键设计模式

**1. 双 Agent 架构（Two-Agent Architecture）**
- **Initializer Agent**：首次会话建立环境，创建 init.sh、feature_list.json、claude-progress.txt 等制品
- **Coding Agent**：后续会话基于既有上下文继续工作，读取进度文件和功能列表选择最高优先级任务

**2. 生成器-评估器循环（Generator-Evaluator Loop）**
受 GAN 启发的架构，生成器产生输出，独立的评估器提供结构化反馈，驱动迭代改进。特别适合主观质量评估。

**3. Sprint Contract（冲刺契约）**
在每个工作块之前，生成器和评估器协商「完成」的定义，确保代码编写前对齐。

**4. 三 Agent 协作（Planner-Generator-Evaluator）**
- **Planner Agent**：将 1-4 句提示扩展为完整产品规格说明
- **Generator Agent**：使用 React、Vite、FastAPI、SQLite/PostgreSQL 技术栈逐 sprint 实现特性
- **Evaluator Agent**：通过 Playwright MCP 进行测试，根据标准评分

**5. 上下文管理策略**
- **Compaction（压缩）**：在原位置汇总对话历史
- **Reset（重置）**：清除窗口，通过结构化制品交接
- **Sub-agent 模式**：子 Agent 作为「上下文防火墙」，阻止中间噪声累积到父线程

### CAR 分解框架（学术定义）

根据预印本论文《Harness Engineering for Language Agents》：

- **Control（控制）**：定义任务规格、约束和验证条件
- **Agent（代理）**：负责推理、规划和执行
- **Runtime（运行时）**：提供执行环境、状态管理和资源调度

## 方法论

### 核心设计哲学

1. **从 Desired Behavior 反向工作**：从期望的 Agent 行为出发，识别必要的 Harness 特性
2. **最小化复杂度**：找到最简单的解决方案，只有在需要时才增加复杂度
3. **模型能力匹配**：Harness 复杂度应与模型能力匹配，随模型进化逐步简化非必要组件
4. **分离判断与执行**：怀疑的 Evaluator 胜过自我批评的 Generator
5. **透明性**：确保代理决策过程可追踪、可理解

### 最佳实践

1. **渐进式披露（Progressive Disclosure）**
   - 不要一次性灌输所有信息
   - 提供入口点（AGENTS.md），让 Agent 按需导航
   - Skills 实现按需加载而非启动时全部注入

2. **质量左移（Keep Quality Left）**
   - 按成本和关键性分配检查
   - 快速、廉价的控制（lint、类型检查）放在提交前
   - 昂贵的传感器（突变测试、AI 审查）放在集成后

3. **持久化所有内容到磁盘**
   - Repository 是唯一真实来源
   - Agent 无法使用看不见的信息
   - 所有决策和计划使用版本控制的制品

4. **验证优于胜利（Verification before Victory）**
   - 要求测试、lint、类型检查通过后才算完成
   - 端到端验证确保功能真正工作

5. **构建-验证循环**
   - 计划→发现→构建→验证→修复的循环
   - 鼓励 Agent 运行测试并与规格对照，而非与自己的代码对照

6. **成功沉默（Success is Silent）**
   - 构建/测试输出只显示错误
   - 成功时静默退出

### 避坑指南

1. **避免「dumb zone」问题**：不要在提示中塞入过多指令，这会导致智能体进入「愚蠢区域」，应该使用结构化 Harness 而非超长提示

2. **不要假设模型能处理所有边界情况**：每个失败模式都需要明确的处理策略

3. **不要让 Harness 过度耦合特定模型**：便于未来更换模型

4. **不要过度工程化 Harness**：警惕「在狗的内侧套 harness」的反模式

5. **新模型发布时重新审视 harness**：移除不再承载的组件，添加新能力

### 常见错误排查

| 问题 | 可能原因 | 解决方案 |
|------|----------|----------|
| Context Rot（模型性能随上下文长度下降） | 上下文窗口填充过多 | 使用子 Agent 架构、实施上下文压缩、限制上下文长度 |
| Doom Loop（重复编辑同一文件） | 缺乏跳出机制 | LoopDetectionMiddleware 追踪每文件编辑次数，多次后插入提示 |
| Premature Completion Claims（过早声称完成） | 缺乏验证机制 | feature list 机制，要求端到端验证通过才标记完成 |
| 上下文焦虑（接近限制时提前结束） | 模型感知限制 | 使用上下文重置或升级到更新的模型（如 Opus 4.6） |

## 应用与发展趋势

### 当前状态

Harness Engineering 已从概念发展为完整的工程实践体系：

- **社区资源丰富**：awesome-harness-engineering (922 stars)、learn-harness-engineering (4,281 stars)、walkinglabs/awesome-harness-engineering (2,449 stars) 等
- **工具链成熟**：LangChain (136,763 stars)、LangGraph、Claude Agent SDK、Model Context Protocol (MCP) 等基础设施完善
- **Benchmark 验证**：Terminal Bench 2.0 显示 Harness 优化可带来 13.7 点的性能提升（52.8→66.5）
- **企业采用**：Stripe 使用「minions」架构，包含基于启发式的 pre-push hooks；多个企业级框架如 KWeaver Core、syrin-python 等出现

### 性能影响案例

根据 LangChain 的实验：

| 指标 | 数值 |
|------|------|
| Terminal Bench 2.0 提升 | 52.8 → 66.5 (+13.7) |
| 模型 | gpt-5.2-codex（固定） |
| 优化手段 | 仅 Harness 调整（System Prompt、Tools、Middleware） |

### 生态工具矩阵

| 类别 | 工具 |
|------|------|
| Agent 框架与编排 | LangGraph (graph-based state machines)、LiteLLM (100+ LLM provider routing)、Google ADK、Microsoft TaskWeaver、Claude Agent SDK |
| 记忆与状态 | Letta (MemGPT)、mem0、Zep、Stash |
| 工具集成 | Model Context Protocol (MCP) servers、Composio (250+ SaaS API wrappers)、Microsoft Skills Framework |
| 评估与验证 | SkillTester benchmark、AutoHarness (constraint synthesis)、AgentDoG (diagnostic guardrails) |
| 学习资源 | awesome-harness-engineering、learn-harness-engineering、harness-engineering-playbook |

### 关键趋势

1. **Harness 作为一等工程对象**：团队开始将 Harness 设计视为与代码同等重要的工程实践

2. **自适应 Harness**：根据模型能力动态调整 Harness 复杂度

3. **多 Agent 系统的 Typed Schema**：Agent 间通信需要明确的类型化接口

4. **评估驱动开发**：类似代码覆盖率的 Harness 覆盖率指标出现

5. **协议标准化**：MCP（Model Context Protocol）、A2A（Agent-to-Agent）、AG-UI 等协议推动生态整合

6. **Harness 与模型训练耦合**：Claude Code 和 Codex 等产品在后训练中加入了 harness 循环，发现有用的原语被添加到 harness，再用于下一代模型训练

## 与同类方案的对比

### 概念定义的不同流派

| 来源 | 定义侧重点 |
|------|-----------|
| Mitchell Hashimoto | Harness Engineering 是防止 agent 重复犯错的设计实践，强调错误驱动的迭代改进 |
| OpenAI | Harness Engineering 是使用 Codex 构建可靠 Agent 的系统方法 |
| Anthropic | Harness 是连接离散会话、实现长时间运行的桥梁系统，强调双 Agent 架构和 Generator-Evaluator |
| Martin Fowler | Harness 是结合前馈（Guides）和反馈（Sensors）的控制系统，实现代码库自趋近目标状态 |
| LangChain | Harness 是除模型本身外的所有代码、配置和执行逻辑 |
| 学术论文 | Control-Agent-Runtime 分解框架 |

### Harness vs Framework

| 维度 | Harness | Framework |
|------|---------|-----------|
| 核心理念 | 连接、保护、编排组件，不自己做工作 | 构建自己的重试逻辑、状态持久化、任务队列 |
| 状态管理 | Steps 作为独立可重试单元，通过持久化实现跨会话 | 通常内置状态管理，可能与具体实现耦合 |
| 重试机制 | 利用现有的 durable event-driven 基础设施 | 自建重试逻辑 |
| 关注点 | 基础设施而非 AI 问题 | 应用逻辑 |
| 复杂度 | 最小化复杂度，按需增加 | 通常提供完整解决方案 |

**关键洞察**：框架试图做所有事情，而 Harness 复用了现有基础设施，让 Agent 专注于决策。

### 不同 Harness 设计模式的对比

| 模式 | 适用场景 | 优势 | 局限 |
|------|---------|------|------|
| 双 Agent 架构 | 长时间跨会话任务 | 会话间连续性好，初始化清晰 | 需要精心设计的交接制品 |
| 生成器-评估器 | 主观质量评估（设计、创意） | 独立评估更可靠 | 增加延迟，需要额外计算资源 |
| 多 Agent 协作 | 复杂系统需要专业分工 | 可扩展性好，角色清晰 | 通信开销大，协调复杂 |
| Sprint Contract | 需要明确「完成」定义的任务 | 减少歧义，提高效率 | 协商过程本身有开销 |

### 方法论演进对比

| 方法 | 核心理念 | 适用场景 | 局限性 |
|------|----------|----------|--------|
| 传统编程 | 人类编写代码 → 机器执行 | 确定性任务 | 无法处理非确定性 AI 任务 |
| Prompt Engineering | 优化提示词 | 单次交互优化 | 缺乏系统性工程支撑 |
| Harness Engineering | 人类设计约束 → 代理编写代码 → 机器执行 | 非确定性、复杂任务 | 相对较新，生态还在成熟 |
| Agent Framework | 提供完整开发框架 | 快速构建 Agent | 可能过度抽象，定制受限 |

### 重要澄清

注意：**Claude Code** 是一款实现 Harness Engineering 思想的具体产品（Anthropic 的 AI 编码工具），而非 Harness Engineering 本身。Harness Engineering 是关于如何设计「驾驭系统」的方法论，Claude Code 是践行该方法论的典型案例。同样，LangChain、AutoGPT 等是实现 Agent 相关模式的框架，而非 Harness Engineering 概念的定义者。

## 常见问题（FAQ）

- **Q：Harness Engineering 和 Agent Framework 有什么区别？**

  A：Framework 构建自己的基础设施（重试、状态、队列），而 Harness 复用现有 durable 基础设施。Framework 做工作，Harness 连接和编排。Framework 提供了 Harness 的骨架，但每个团队仍需根据自身需求定制化配置。

- **Q：为什么弱结果通常是 Harness 问题而非模型问题？**

  A：研究表明，同一模型在不同 Harness 下表现差异巨大。Opus 4.6 在 Claude Code harness 中排名第 33 位，在另一 harness 中排名第 5 位。模型性能本身可能没有问题，而是 Harness 配置不当导致模型无法发挥全部潜力。

- **Q：如何判断一个 harness 是否有效？**

  A：关键指标包括：首次尝试成功率、迭代周期数、人工介入频率、长时间运行的上下文保持能力。建议使用 Terminal Bench、SWE-bench 等标准化基准进行评估。

- **Q：我需要为每个 Agent 项目重新设计 Harness 吗？**

  A：不。可以从模板开始，根据任务复杂度调整。Harness 应该是渐进的——从简单开始，只有在遇到问题时才增加复杂度。工具如 AGENTS.md、feature_list.json、init.sh 都有现成的模板可用。

- **Q：什么情况下应该移除 Harness 组件？**

  A：当模型能力提升使得某些组件变为非必要负载（non-load-bearing）时，应移除。设计原则是「find the simplest solution possible, and only increase complexity when needed」。

- **Q：子 Agent 如何帮助处理上下文限制？**

  A：子 Agent 作为「上下文防火墙」，阻止中间噪声累积到父线程。它们返回的是精简的答案和来源引用，而非完整的推理过程，从而保持父上下文清洁。

- **Q：Harness Engineering 适用于所有类型的 AI 代理吗？**

  A：主要适用于需要复杂推理、长时运行、多步骤执行的 AI 编码代理。对于简单的一次性任务，复杂的 harness 可能过度。

- **Q：如何开始应用 Harness Engineering？**

  A：可以从创建 AGENTS.md 文件开始，定义项目的架构规范和约束规则。然后逐步引入 lint 配置、测试套件和状态管理机制。参考 Awesome 列表获取资源。

## 争议与质疑

### 争议 1：「所有问题都是配置问题」的二元论

HumanLayer 提出「It's not a model problem, it's a configuration problem」，将所有 Agent 失败归因于 Harness 配置。但这可能过于简化——某些任务确实超出当前模型能力，单纯优化 Harness 无法解决。

**评估**：可信度 Medium。虽然 Harness 优化通常能带来显著提升，但「所有问题都是配置问题」的说法可能忽略了模型固有局限。LangChain 的实验（13.7 点提升）支持 Harness 重要性，但也承认存在模型能力边界。

### 争议 2：ETH Zurich 研究的矛盾发现

ETH Zurich 2026 年研究测试了 138 个 agentfiles：
- LLM 生成的 agentfiles 实际上降低了性能
- 人类编写的 agentfiles 仅帮助约 4%
- Agent 使用更多推理 token（14-22%）但没有提升解决率

这与 Harness Engineering 的核心理念（精心设计的 Harness 能显著提升 Agent 性能）存在张力。

**评估**：可信度 Medium-High。学术研究提供了对照实验证据，但研究对象是「agentfiles」（系统提示）而非完整的 Harness 系统（包含工具、中间件、验证循环），测量粒度存在差异。

### 争议 3：概念原创性争议

有多个来源声称是 Harness Engineering 的起源：
- **Mitchell Hashimoto**（Terraform、Vagrant 作者）在 2026 年 2 月 5 日首次提出并定义概念
- **OpenAI** 在 2026 年 2 月 17 日正式命名（晚 12 天）
- **Anthropic** 的实践方法论（2025 年 11 月 26 日）实质相同但未用此名称
- **Thoughtworks** 的 Martin Fowler 框架在 2026 年 4 月发布

**评估**：经用户指正，**真正的概念起源是 Mitchell Hashimoto**，发表于 2026 年 2 月 5 日，比 OpenAI 早 12 天。Mitchell 的定义是：「anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that mistake again.」OpenAI 是命名者但非原创者。Anthropic 的实践（双 Agent 架构、Generator-Evaluator 等）实质相同但命名不同。

### 争议 4：上下文压缩的信息丢失风险

压缩和重置都涉及上下文信息的丢弃。虽然保留了「最重要」的内容，但不可避免会丢失某些潜在有用的信息。对于需要长期记忆的项目，这可能导致重复错误或丢失重要上下文。

**评估**：可信度 High。这是结构化取舍的已知局限。解决方案是设计高质量的交接制品，但这增加了工程负担。

### 争议 5：标准化的缺失

目前 Harness Engineering 缺乏统一的标准或规范。不同实现（Claude Code 的实践、LangChain 的模式、OpenAI 的规范）之间存在差异，使得最佳实践的传播和采纳存在障碍。

**评估**：可信度 High。这是一个新兴领域，标准化需要时间。AGENTS.md 格式的努力是一个积极信号，但距离真正的行业标准还有距离。

### 争议 6：框架复杂性的质疑

批评者认为过度复杂的 harness 系统反而降低了 AI 代理的灵活性，增加了维护成本。Martin Fowler 也提到：「有人指出，在 harness 外面再套 harness 是没有意义的。」

**评估**：可信度 Medium。社区工具正在解决这一问题（如自动同步、配置验证），但对于小团队确实存在额外负担。关键在于保持 Harness 简单，只有在真正需要时才增加复杂度。

## 相关资料

- [Mitchell Hashimoto - My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey) - **真正的概念起源**，2026 年 2 月 5 日首次提出「Harness Engineering」定义
- [OpenAI - Harness Engineering: Harnessing Codex in an Agent-First World](https://openai.com/index/harness-engineering/) - OpenAI 官方 Harness Engineering 概念首发（2026 年 2 月 17 日，正式命名）
- [OpenAI 中文版 - Harness Engineering](https://openai.com/zh-Hans-CN/index/harness-engineering/) - OpenAI 官方中文翻译版本
- [Anthropic - Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) - 双 Agent 架构与会话管理核心文章
- [Anthropic - Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps) - Generator-evaluator 循环与三 Agent 架构
- [Anthropic - Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) - Anthropic Agent 工作流指南
- [Martin Fowler - Harness Engineering Framework](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html) - Thoughtworks 系统性框架分析
- [LangChain - The Anatomy of an Agent Harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness) - Agent Harness 五核心组件解构
- [LangChain - Improving Deep Agents with harness engineering](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering) - 实验证明 Harness 改进效果（Terminal Bench 2.0: 52.8→66.5）
- [HumanLayer - Skill Issue: Harness Engineering for Coding Agents](https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents) - 论证弱结果通常是 Harness 问题而非模型问题
- [Inngest - Your Agent Needs a Harness, Not a Framework](https://www.inngest.com/blog/your-agent-needs-a-harness-not-a-framework) - 状态、重试、追踪作为一等基础设施
- [预印本 - Harness Engineering for Language Agents (CAR decomposition)](https://www.preprints.org/manuscript/202603.1756) - 学术论文，提出控制-代理-运行时（CAR）分解
- [驾驭工程：从 Claude Code 源码到 AI 编码最佳实践](https://zhanghandong.github.io/harness-engineering-from-cc-to-ai-coding/) - 基于 Claude Code 源码的中文技术书籍
- [GitHub - learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) - 4,281 stars，12 讲座+6 项目的官方风格教程课程
- [GitHub - awesome-harness-engineering (walkinglabs)](https://github.com/walkinglabs/awesome-harness-engineering) - 2,449 stars，工具和指南汇总
- [GitHub - ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) - 922 stars，AI Agent Harness 工具和模式汇总
- [GitHub - deusyu/harness-engineering](https://github.com/deusyu/harness-engineering) - 2,719 stars，中文深度学习档案
- [GitHub - Agent Governance](https://github.com/bounce12340/agent-governance) - 以三权分立与 Harness Engineering 为核心的 AI Agent 治理框架
- [GitHub - AGENTS.md format specification](https://github.com/agentsmd/agents.md) - Agent 指令格式规范