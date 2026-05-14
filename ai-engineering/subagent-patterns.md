# Agent 如何管理其他 Agent：2026 年的四种 Subagent 模式

> 原文：[How Agents Manage Other Agents: Four Subagents Patterns in 2026](https://www.philschmid.de/subagent-patterns-2026)<br>
> 作者：Philipp Schmid<br>
> 日期：2026-05-05

## 原文及译文

<details>
<summary>原文</summary>
<section>

### How Agents Manage Other Agents: Four Subagents Patterns in 2026

I previously wrote about subagents and their benefits for reliability through task isolation. Since then, model capabilities around planning and tool use have improved enough to make patterns previously considered too fragile now viable in production—including persistent worker pools and direct agent-to-agent messaging.

In this post, I'll walk through four patterns for orchestrating subagents, starting from the simplest function-call style and progressing to full agent teams. Each pattern builds on the previous and adds new orchestration capabilities.

#### Pattern 1: Inline Tool — Subagent as a Function Call

The simplest pattern treats subagent calls identically to any other tool call. The main agent invokes a `call_agent` tool, passes a task description, and receives results as a tool response. The subagent runs independently with its own context, tools, and system instructions.

From the main agent's perspective, calling a subagent is identical to calling `read_file` or `run_command`. This offers two variations:

**Synchronous:** The tool blocks until the subagent completes, and results arrive as a normal tool response.

**Asynchronous:** The tool returns immediately with an agent ID. The subagent's result is injected into the conversation as a notification message when it finishes, allowing the main agent to execute other tool calls concurrently.

**Appropriate use cases:** Self-contained tasks that don't require follow-up—research lookups, code reviews, file analysis, test generation.

**Limitations:** Works with any model that supports tool use, but offers no ability to send follow-up instructions, monitor progress mid-task, or cancel early. Misunderstandings only surface when results return.

Most subagent use cases start and stay here. It's the right choice until you have a concrete reason to add complexity.

#### Pattern 2: Fan-Out — Spawn Agents and Wait for Results

This pattern separates spawning from result collection into distinct steps. `spawn_agent` returns immediately with an agent ID; `wait_agent` blocks until that agent completes. The key difference from Pattern 1: the model controls the sequencing.

The model can spawn multiple agents, do its own work, then collect results whenever it's ready. As I described: "The model spawned two agents and read a file in the same turn, then decided to wait."

**Appropriate use cases:** Multiple independent parallel tasks where results don't depend on each other, and the main agent doesn't need intermediate results to start new work.

**Limitations:** Model quality directly affects the benefit. A model that always calls `wait_agent` immediately after spawning gets no parallelism advantage over Pattern 1. Still fire-and-forget—no mid-task course correction.

#### Pattern 3: Agent Pool — Persistent Agents with Messaging

Agents become stateful and interactive. They persist across multiple turns rather than terminating after a single task. The main agent uses a richer tool set: `spawn_agent`, `send_message`, `wait_agent`, `list_agents`, `kill_agent`. Each agent retains its full conversation history, enabling multi-step coordinated workflows.

Results arrive per-message via `wait_agent`. Each call returns the next agent response, so the main agent processes results incrementally. This lets the main agent route information between specialists—sending research results to a writer, sending a draft to a reviewer—without restarting agents from scratch.

**Appropriate use cases:** Multi-step collaborations where agents need to work together over several turns, with the main agent coordinating information flow between specialists.

**Limitations:** The main agent must track multiple agent states simultaneously and route information correctly. Smaller models frequently lose context or forget lifecycle management. Typically manageable for frontier models with 2–4 agents.

#### Pattern 4: Teams — Agents Talk to Each Other

Agents communicate directly without routing through the main agent. The main agent establishes the team structure—spawning specialists and defining roles—then steps back. Agents coordinate independently through direct messaging.

The planner messaging the implementer, the implementer sending code to the reviewer, the reviewer sending feedback back to the implementer—all of that happens inside the agents' own conversations. The main agent only receives the final result.

**Appropriate use cases:** Large-scale tasks where coordination complexity exceeds what a single orchestrating agent can manage sequentially.

**Limitations:** Every team member requires frontier-class capabilities—not just the main agent. Agents must independently decide who to message and when to report completion. Infrastructure challenges include cycle detection, conflict resolution for concurrent edits, and shutdown coordination. Debugging is significantly harder because inter-agent message chains are invisible to the main context.

#### How to Choose

| Pattern | Core Tools | Main Agent Role | Agent Lifetime |
| :------ | :--------- | :-------------- | :------------- |
| Inline Tool | `call_agent` | Caller | Single task |
| Fan-Out | `spawn_agent`, `wait_agent` | Dispatcher | Single task |
| Agent Pool | Full toolkit | Coordinator | Multi-turn |
| Teams | All tools + cross-agent messaging | Supervisor | Persistent |

Start with Pattern 1 for most tasks. Most tasks that feel like they need a multi-agent system work fine with a well-prompted inline tool call. Progress to Pattern 2 for genuinely independent parallel work, Pattern 3 for collaborative multi-step workflows requiring specialists, and Pattern 4 only when coordination complexity exceeds what a single orchestrating agent can manage.

Model capability requirements escalate with each pattern. Patterns 1 and 2 work with any tool-capable model. Patterns 3 and 4 require frontier-class models. For smaller or less capable models, stay with Patterns 1 and 2.

A task that takes 4 coordinated agents today may be solvable by a single agent with a better model tomorrow. The framework provides the tools; the model decides the orchestration strategy.

</section>
</details>
<details>
<summary>译文</summary>
<section>

### Agent 如何管理其他 Agent：2026 年的四种 Subagent 模式

此前我写过关于 Subagent 及其通过任务隔离提升可靠性的文章。此后，模型在规划和工具使用方面的能力已经有了足够大的提升，使得过去被认为过于脆弱的模式——包括持久化 Worker Pool 和 Agent 间直接通信——如今在生产环境中切实可行。

在本文中，我将逐一介绍编排 Subagent 的四种模式，从最简单的函数调用风格出发，逐步演进到完整的 Agent Team。每种模式都在前一种的基础上构建，并引入新的编排能力。

#### Pattern 1：Inline Tool — Subagent 即函数调用

最简单的模式：将调用 Subagent 与调用任何其他工具完全等同对待。主 Agent 调用 `call_agent` 工具，传入任务描述，以工具返回值的形式接收结果。Subagent 在独立上下文、工具集和系统指令下运行。

从主 Agent 的视角来看，调用 Subagent 与调用 `read_file` 或 `run_command` 没有任何区别。该模式有两种变体：

**同步模式：** 工具调用会阻塞，直到 Subagent 完成，结果以普通 Tool Response 的形式返回。

**异步模式：** 工具立即返回一个 Agent ID。Subagent 完成后，其结果以通知消息的形式注入主对话，使主 Agent 可以在等待期间并发执行其他工具调用。

**适用场景：** 无需后续追问的独立任务——信息检索、代码审查、文件分析、测试生成。

**局限性：** 适用于任何支持 Tool Use 的模型，但无法发送后续指令、在任务中途监控进度或提前取消。误解只有在结果返回时才会暴露。

绝大多数 Subagent 使用场景都从这里出发，并止步于此。在没有具体理由增加复杂性之前，这是正确的选择。

#### Pattern 2：Fan-Out — 派生 Agent 并等待结果

该模式将"派生"与"收集结果"分离为独立步骤。`spawn_agent` 立即返回一个 Agent ID；`wait_agent` 则阻塞等待该 Agent 完成。与 Pattern 1 的关键区别在于：**模型控制时序**。

模型可以派生多个 Agent，执行自己的工作，然后在准备好时再收集结果。就像我所描述的："模型在同一轮中派生了两个 Agent 并读取了一个文件，然后决定等待。"

**适用场景：** 多个独立的并行任务，结果之间互不依赖，且主 Agent 不需要中间结果即可启动新工作。

**局限性：** 模型质量直接影响收益。如果模型总是在派生后立即调用 `wait_agent`，则相比 Pattern 1 毫无并行优势。仍然是"即发即忘"——无法在任务中途进行纠正。

#### Pattern 3：Agent Pool — 带消息传递的持久化 Agent

Agent 变得有状态且可交互。它们不再在单次任务后终止，而是跨多轮持久存在。主 Agent 使用更丰富的工具集：`spawn_agent`、`send_message`、`wait_agent`、`list_agents`、`kill_agent`。每个 Agent 保留完整的对话历史，从而实现多步骤协调工作流。

结果通过 `wait_agent` 逐条消息返回。每次调用返回下一条 Agent 响应，主 Agent 因此可以增量处理结果。这使主 Agent 能够在各专业 Agent 之间路由信息——将研究结果发送给写作 Agent，将草稿发送给审核 Agent——而无需重新启动 Agent。

**适用场景：** 需要多轮协作的场景，Agent 之间需要相互配合，主 Agent 负责协调各专业 Agent 之间的信息流转。

**局限性：** 主 Agent 必须同时追踪多个 Agent 的状态并正确路由信息。较小的模型经常丢失上下文或忘记生命周期管理。对于前沿模型而言，管理 2-4 个 Agent 通常是可行的。

#### Pattern 4：Teams — Agent 之间直接通信

Agent 之间直接通信，无需通过主 Agent 路由。主 Agent 建立 Team 结构——派生各专业 Agent 并定义角色——然后退居幕后。Agent 之间通过直接消息传递独立协调。

Planner 向 Implementer 发送消息，Implementer 将代码发送给 Reviewer，Reviewer 将反馈发回给 Implementer——所有这些都在 Agent 自己的对话中发生。主 Agent 只接收最终结果。

**适用场景：** 大规模任务，其中协调复杂度超出单个编排 Agent 串行处理的能力上限。

**局限性：** 每个 Team 成员都需要前沿级别的能力——不仅仅是主 Agent。Agent 必须自主决定向谁发送消息以及何时报告完成。基础设施挑战包括：循环检测、并发编辑的冲突解决、以及关闭协调。调试难度显著增加，因为 Agent 间的消息链对主上下文是不可见的。

#### 如何选择

| Pattern | 核心工具 | 主 Agent 角色 | Agent 生命周期 |
| :------ | :------- | :------------ | :------------- |
| Inline Tool | `call_agent` | 调用者 | 单次任务 |
| Fan-Out | `spawn_agent`, `wait_agent` | 调度者 | 单次任务 |
| Agent Pool | 完整工具集 | 协调者 | 多轮 |
| Teams | 全部工具 + 跨 Agent 消息 | 监督者 | 持久 |

对大多数任务从 Pattern 1 开始。大多数感觉需要多 Agent 系统的任务，用一个精心提示的内联工具调用就能完美解决。在确实有独立并行工作时推进到 Pattern 2，在需要专业 Agent 协作的多步骤工作流时使用 Pattern 3，只有在协调复杂度超出单个编排 Agent 能力时才使用 Pattern 4。

每种模式对模型能力的要求逐级提升。Pattern 1 和 2 适用于任何支持 Tool Use 的模型；Pattern 3 和 4 则需要前沿级别的模型。对于较小或能力较弱的模型，应保持在 Pattern 1 和 2 范围内。

今天需要 4 个协调 Agent 才能完成的任务，明天可能只需要一个更强的模型就能单独解决。框架提供工具；模型决定编排策略。

</section>
</details>

## 深度解读

这篇文章的核心，不是在讲"多 Agent"本身，而是在尝试给 **Subagent 系统建立一套分层架构学（Architecture Taxonomy）**。

作者 Philipp Schmid 把 2026 年 AI Coding / Agent Systems 里越来越常见的"Agent 管理 Agent"现象，拆成了四种递进式模式。文章本质上是在回答三个问题：

> 什么时候只需要调用一个 Subagent？什么时候需要长期存活的 Agent Pool？什么时候会演化成真正的 Agent Team？

---

### 一、文章最核心的观察：Agent 正在从 Tool 演化为 Runtime

作者认为，随着模型的 Planning、Tool Use、Long Horizon Execution 能力提升，Agent 架构正在从"单 Agent + Tool Calling"逐渐演进为"Agent Orchestration（智能体编排）"。

这意味着：

- Agent 不再只是"调用工具"，而是开始"管理其他 Agent"
- Subagent 不再只是函数调用，它们开始具有生命周期（Lifecycle）、状态（State）、消息机制（Messaging）、协作关系（Coordination）和自主性（Autonomy）

四种模式对应的本质抽象：

| Pattern | 本质 | 类比 | 特征 |
| :------ | :--- | :--- | :--- |
| Pattern 1：Inline Tool | Subagent = Function | RPC / Tool Call | 上下文隔离 |
| Pattern 2：Fan-Out | Subagent = Future / Task | async task / Promise | 并行执行 |
| Pattern 3：Agent Pool | Subagent = Actor | Actor Model | 长期存活 |
| Pattern 4：Teams | Subagent = Autonomous Organization | Multi-Agent Society | 自主协作 |

这比文章原文更抽象，但更接近本质。

---

### 二、Pattern 1：上下文隔离才是真正的价值

这是目前绝大多数 AI Coding 产品实际在用的模式，本质是：把一个 specialized prompt 封装成 tool。

```text
Main Agent
  ↓
call subagent (security-reviewer / test-generator / docs-writer)
  ↓
wait result
```

它真正解决的问题不是"并行"，而是 **Context Isolation（上下文隔离）**。

如果安全审查、测试生成、文档总结全部塞进主上下文，会污染主 Agent 的 Reasoning Trajectory。将它们封装为独立 Subagent，主 Agent 的上下文保持干净，Subagent 在自己的独立上下文中专注执行。

这是文章没有明说，但其实最关键的点：

> LLM 最大的问题之一就是 Context Entanglement（上下文纠缠）。Subagent 的本质价值是上下文隔离，而不是并行。

这一层非常像 Unix Process、Microservice、RPC、Lambda Function。作者说"绝大多数系统停留在这里就够了"，是非常务实的工程建议。

---

### 三、Pattern 2：Agent 开始具备 Runtime 行为

Fan-Out 模式的核心变化是：`spawn` 和 `collect` 分离了。

```text
spawn_agent()   ← 立即返回
spawn_agent()   ← 立即返回
do my own work
wait_agent()    ← 在需要时再等待
```

这其实就是 Future / Promise 模型，极其类似 `Promise.all`、goroutine、asyncio、Ray、Celery。

**为什么这是重要跃迁？**

主 Agent 开始拥有 **调度权（Scheduling Power）**，不再是简单的 `call → wait`，而是可以 `spawn → do work → wait later`。这意味着 Agent 开始具备 Runtime 行为。

**现实中的问题：**

作者提到"模型必须知道什么时候 wait"，这是非常真实的困难。很多模型会在 `spawn` 之后立即 `wait`，等于没有并行。

更深层的问题是：**模型并不擅长 Scheduling**。它们擅长 Reasoning 和 Generation，但不擅长 Runtime Orchestration、Dependency Management、Concurrency Optimization。所以很多多 Agent 系统实际上比单 Agent 更慢、更贵、更脆弱。

---

### 四、Pattern 3：最关键的一层——Persistent Agent 出现了

这是整篇文章最重要的一层。这里出现了 **Persistent Agent（持久化 Agent）**。

Agent 不再是 `spawn → finish → destroy`，而是：

```text
spawn once
keep alive
message repeatedly (send research → receive result → send refinement...)
```

**本质上，这已经进入 Actor Model 了。**

极其像 Erlang Actor、Akka、Orleans——每个 Agent 有自己的 State，有 Mailbox，可以 Message Passing，长期存在。

**为什么这很重要？**

因为 **State Persistence（状态持续化）** 出现了。举例：Research Agent 在第一次任务后，不需要重新学习上下文，因为它保留了对话历史。主 Agent 可以说"用你之前找到的资料写一个大纲"——Subagent 知道"之前找到的资料"是什么。

这是当前 AI Agent 系统最大的演化方向——Claude Code Agent Teams、OpenAI Codex Cloud Workers、Cursor Background Agents、Devin-like systems 都在往这里走，因为单轮 Stateless Agent 已经开始触顶。

**但问题也巨大：**

主 Agent 必须同时追踪多个 Agent 的状态，记住哪个 Agent 持有什么上下文：

```text
agent-researcher 知道 benchmark 数据
agent-writer     知道 outline 结构
agent-reviewer   知道 draft v2 的修改意见
```

这已经接近 **Operating System Scheduler + IPC** 的复杂度了。**Agent Memory Routing 本身是一个困难问题**，作者的提示——"对于前沿模型管理 2-4 个 Agent 通常可行"——其实是一个很保守的工程边界。

---

### 五、Pattern 4：真正的分布式自治系统

Pattern 4 不再是"Tool System"，而是 **Distributed Autonomous System**。

```text
Main Agent（建立结构，然后退出）
  ├── Agent A (Planner)
  │     ↕ 直接消息
  ├── Agent B (Implementer)
  │     ↕ 直接消息
  └── Agent C (Reviewer)
```

Agent 之间直接通信，主 Agent 不再是所有信息的中转站。这非常像 Distributed Systems、Swarm Intelligence、Blackboard Systems。

**为什么作者说"只有前沿模型能做到这一点"？**

因为每个 Agent 都必须自主规划、自主协作、自主决定消息目标、自主判断何时完成。这对模型能力要求极高——不仅仅是主 Agent，**每一个 Team 成员**都需要这种能力。

**文章没有深入但真正困难的工程问题：**

1. **Cycle Detection**：Agent A 等 Agent B，Agent B 等 Agent A——死锁如何检测和打破？
2. **Conflict Resolution**：两个 Agent 同时修改同一文件，这已经是 Distributed Transaction 问题
3. **Observability**：Agent 间通信隐藏在各自的上下文中，Debug 极其困难，和 Distributed Tracing、Microservice Observability 是同一个问题
4. **Cost Explosion**：Token × Agent Count 可能造成指数级开销

---

### 六、文章最重要但最容易被忽视的一句话

> "A task that takes 4 coordinated agents today may be solvable by a single agent with a better model tomorrow."

这是整个 Agent 行业最容易被忽视的问题。

**"多 Agent"很多时候只是模型能力不足的补丁。**

2024 年需要 `planner + coder + reviewer` 三个 Agent 协作的任务，2026 年的 frontier model 可能一个就能完成。这意味着 Agent 系统架构有一个隐性的"技术债"风险——你为模型局限性设计的复杂编排，可能随着模型进步而变成过度工程。

真正稳定的不是"Agent 数量"，而是：

- **Context Engineering**（上下文工程）
- **Task Decomposition**（任务分解）

这两个能力无论模型如何进步，都是有价值的。

---

### 七、文章遗漏的关键维度

文章框架很清晰，但在以下几个真正困难的问题上涉及过浅：

**1. Shared Memory Problem**

多个 Agent 如何共享"世界模型"？Agent A 修改了代码，Agent B 不知道——Memory Divergence 是 Pattern 3/4 最大的隐患之一。

**2. Token Economics**

多 Agent 系统的成本分析几乎缺失。Pattern 3 和 4 在前沿模型上运行，每个 Agent 有独立的 Context Window，总 Token 消耗可能比单 Agent 高出数倍甚至数十倍。很多看起来"聪明"的多 Agent 系统，实际上更慢、更贵、更不稳定。

**3. Observability Gap**

Pattern 4 最大的工程挑战是不可观测性（Unobservable）。Agent 间通信隐藏在各自上下文中，没有统一的 Trace，调试和监控极其困难。这和 Kubernetes、Terraform、企业低代码平台曾经面临的问题完全一致——**自动化系统过度叠加后，没有人真正理解整体**。

**4. 过度乐观的模型假设**

文章认为"前沿模型"能解决 Pattern 3/4 的协调问题，但现实中即使是 Claude Opus 或 GPT-4o，在复杂多轮多 Agent 协调场景中仍然频繁出现状态丢失、角色混淆、生命周期管理失败等问题。

---

### 八、对工程实践的真正启发

如果你正在构建 AI Coding、Agent Runtime、Workflow Engine 或 Multi-Agent Orchestration 系统，这篇文章最值得吸收的不是"四种模式的分类"，而是：

**Agent 是一种 Runtime Architecture，不是 Prompt Engineering。**

四种模式实际上在重新发明：

| Agent 概念 | 对应的系统工程概念 |
| :--------- | :----------------- |
| Inline Tool | OS System Call / RPC |
| Fan-Out | Future / Promise / Coroutine |
| Agent Pool | Actor System / Thread Pool |
| Teams | Distributed Process / Microservice Mesh |

底层执行单元从 `CPU process` 变成了 `LLM cognition`，但系统设计的核心问题——状态管理、消息传递、调度、并发控制、可观测性——一个都没有减少。

**工程实践的三条原则：**

1. **从 Pattern 1 开始，有明确理由再升级**：大多数"感觉需要多 Agent"的任务，一个精心设计的 Inline Tool Call 就够了。复杂性的代价是真实的
2. **可观测性先于架构**：在上 Pattern 3/4 之前，先建立 Agent 生命周期追踪、消息流日志、状态快照机制
3. **Context Engineering > Agent Count**：更清晰的任务分解、更好的上下文隔离、更精确的 Prompt，往往比增加一个 Agent 更有效

---

### 核心结论

这篇文章真正讲的是：

> **AI Agent Systems 正在从 Tool Calling 演化为 Distributed Cognitive Runtime。**

四种 Pattern 对应的演化路径：

```text
Function（函数）
  → Async Task（异步任务）
    → Actor（持久化行为体）
      → Autonomous Organization（自治组织）
```

这是 2026 年 AI 工程领域最值得关注的架构演化方向。而工程师在这条路上最重要的能力，不是"会用多 Agent 框架"，而是**知道什么时候不需要用**——以及在必须用的时候，如何控制复杂性、保持可观测性、避免"多 Agent"变成"多问题"。
