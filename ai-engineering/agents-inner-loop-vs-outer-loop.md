# 深度解读：Agents 内循环 vs 外循环

> 原文：[Agents: Inner Loop vs Outer Loop](https://www.philschmid.de/inner-loop-vs-outer-loop)<br>
> 作者：Philipp Schmid<br>
> 日期：2026-02-20 06:00

## 原文及译文

<details>
<summary>原文</summary>
<section>

```markdown
# Agents: Inner Loop vs Outer Loop

When people talk about AI agents "closing the loop," they usually mean the agent verifies its own work before responding, which can be confusing as "If the tool call loop is hardcoded, how does the model decide to verify its work?"

Short answer: The loop is hardcoded. What the model does *inside* the loop is not.

Every agent framework runs roughly the same cycle: model generates → if tool call, execute it → feed result back → model generates again → repeat until the model returns text (no more tool calls). That loop is scaffolding. It's the same for every agent.

The difference is what the model *chooses to do* within that loop. A model that "closes the loop" doesn't need a special loop, it uses the existing one to call verification tools *before* deciding it's done.

## The inner loop: agent verifies its own work

The **inner loop** is what happens during a single task, before the agent responds to user with a text. The agent writes code, runs the tests, reads the error, fixes the edge case, re-runs and only then generates a text response for the user. It's the tight feedback cycle between the model and its tools.

Example: You ask "fix the failing test in `auth.ts`."

A weak agent edits the file and says "Done!" A strong agent edits → creates tests → runs the tests → sees a failure → fixes the edge case → runs again → sees green → then responds. Same infrastructure, different behavior.

Bad agent — edits and stops
Good agent — verifies before responding

Both agents use the exact same hardcoded tool loop. The difference is the good agent *chose* to create/call verifications before responding. Nothing forced it to.

Where does that choice come from? Today, mostly from the system prompt ("always run tests after code changes"). Increasingly, from post-training — e.g. test pass/fail as a reward signal, so the model internalizes the verify step.

## The outer loop: learning across turns

The **outer loop** is what happens across multiple turns/sessions between the user and the agent over time. The user gives the agent a task, it works on it (inner loop), returns a result, and then the user comes back with the next task. The question is: did the agent learn anything from the last turn?

Without persistent memory, every turn is a clean slate. The agent that failed on pagination yesterday will fail on it again today.

Almost no agent does this natively today. The outer loop requires persistent state, skills, rules files, or notes that survive between turns and sessions. Some early examples:

- **AGENTS.md:** Manual persistent instructions the user writes for future turns
- **Session handoff documents:** Structured summaries an agent writes for follow-up work
- **SKILL.md:** Agent analyzes failures and auto-generates Skills so the next task doesn't repeat mistakes

The inner loop is about reliability within a task. The outer loop is about getting smarter over time.

## TL;DR

- **The loop is hardcoded.** Every agent has the same generate → tool call → feed back cycle.
- **What the agent does inside the loop is learned.** A good agent calls verification tools before responding. A weak one just stops.
- **Inner loop** = verify within a task (write tests, run them, read files back, check against original ask).
- **Outer loop** = carry lessons across turns (persistent memory, skills, rules files).
- **Closing the loop ≠ new infrastructure.** It's the agent making better decisions within existing infrastructure.
```

</section>
</details>

<details>
<summary>译文</summary>
<section>

```markdown
# 智能体：内循环 vs 外循环

当人们谈论 AI 智能体"闭合循环"时，他们通常指的是智能体在响应之前验证自己的工作。但这会令人困惑——"如果工具调用循环是硬编码的，模型如何决定验证自己的工作？"

简短回答：循环是硬编码的。模型在循环内部做什么并不是。

每个智能体框架运行大致相同的循环：模型生成 → 如果有工具调用则执行 → 将结果反馈 → 模型再次生成 → 重复直到模型返回文本（不再有工具调用）。这个循环是脚手架，对每个智能体都一样。

真正的区别在于模型在循环内*选择做什么*。能够"闭合循环"的模型不需要特殊的循环，它只是利用现有的循环，在决定完成之前调用验证工具。

## 内循环：智能体验证自己的工作

**内循环**是指在单个任务期间、用户收到文本响应之前发生的事情。智能体编写代码、运行测试、读取错误、修复边缘 case、重新运行，然后才生成文本响应给用户。这是模型与其工具之间的紧密反馈循环。

示例：你要求"修复 `auth.ts` 中失败的测试"。

弱智能体编辑文件后说"完成了！"强智能体则：编辑 → 创建测试 → 运行测试 → 发现失败 → 修复边缘 case → 再次运行 → 看到绿灯 → 然后才响应。相同的基础设施，不同的行为。

弱智智能体 — 编辑后停止
好智能体 — 响应前验证

两者使用完全相同的硬编码工具循环。区别在于好智能体选择在响应前创建/调用验证。没有外部力量强迫它这么做。

这种选择从何而来？目前主要来自系统提示词（"代码更改后始终运行测试"）。越来越多地来自后训练——例如将测试通过/失败作为奖励信号，让模型将验证步骤内化。

## 外循环：跨轮次学习

**外循环**是指在用户与智能体之间的多轮次/多会话中发生的事情。用户给智能体一个任务，它处理（内循环），返回结果，然后用户带着下一个任务回来。问题是：智能体从上一轮中学到了什么？

没有持久记忆，每轮都是白纸一张。昨天在分页功能上失败的智能体，今天还会再次失败。

目前几乎没有任何智能体原生做到这一点。外循环需要持久状态、技能、规则文件或跨轮次和会话存活的笔记。一些早期示例：

- **AGENTS.md：** 用户为未来轮次编写的手动持久化指令
- **会话交接文档：** 智能体为后续工作编写的结构化摘要
- **SKILL.md：** 智能体分析失败并自动生成技能，使下一个任务不会重复错误

内循环关乎任务内的可靠性。外循环关乎随时间变得更聪明。

## 总结

- **循环是硬编码的。** 每个智能体都有相同的生成 → 工具调用 → 反馈循环。
- **智能体在循环内做什么是学到的。** 好的智能体在响应前调用验证工具。弱的智能体直接停止。
- **内循环** = 在任务内验证（编写测试、运行测试、回读文件、检查是否符合原始需求）。
- **外循环** = 跨轮次携带经验（持久记忆、技能、规则文件）。
- **闭合循环 ≠ 新基础设施。** 这是智能体在现有基础设施内做出更好决策。
```

</section>
</details>

## 摘要

本文由 AI 领域专家 Philipp Schmid 撰写，深入阐释了 AI 智能体架构中两个核心概念——**内循环（Inner Loop）**与**外循环（Outer Loop）**的本质区别。作者指出，当前智能体框架的工具调用循环是硬编码的、统一的，真正的差异在于模型在这一固定循环内**选择做什么**。内循环强调单任务内的自我验证能力（调用验证工具后再响应），外循环则关注跨会话的持久化学习机制（通过 AGENTS.md、SKILL.md 等载体积累经验）。文章的核心论点是："闭合循环"并非新基础设施的构建，而是智能体利用现有循环做出更优决策的表现。

## 术语表

| 术语 | 全称 | 解释 |
| :--- | :--- | :--- |
| Inner Loop | 内循环 | 单任务执行期间，智能体验证、修正自身工作后再向用户响应的紧密反馈周期 |
| Outer Loop | 外循环 | 跨多轮次/多会话的持久化学习机制，使智能体能够从历史经验中积累知识 |
| Tool Call Loop | 工具调用循环 | 智能体框架中的硬编码循环：生成→工具调用→反馈→重复直到返回文本 |
| Closing the Loop | 闭合循环 | 智能体完成内部验证、将经过检验的输出交付用户的节点 |
| Post-training | 后训练 | 在预训练之后对大语言模型进行进一步优化的过程，用于赋予智能体行为能力 |
| Reward Signal | 奖励信号 | 强化学习中用于指示智能体行为好坏程度的数值信号 |
| AGENTS.md | 智能体指令文档 | 项目级持久化指令规范，固化编码标准和工作流程 |
| SKILL.md | 技能文档 | 智能体从失败中自动提取、封装可复用技能的机制 |
| Session Handoff | 会话交接文档 | 智能体在会话切换时创建的结构化摘要，用于传递工作上下文 |
| Persistent Memory | 持久记忆 | 跨会话保留学习成果和项目知识的记忆系统 |

## 深度解读

### 一、核心概念辨析：内循环与外循环的本质差异

本文最核心的价值在于澄清了一个广泛存在的误解——人们习惯将"闭合循环"理解为需要构建新的基础设施，但作者明确指出：**工具调用循环本身是硬编码的、统一的，所有智能体框架遵循完全相同的三段式循环**（生成→执行→反馈→重复）。

真正的差异来自模型**在固定循环内的决策选择**。这意味着：

1. **基础设施无差异化**：从 LangChain 到 AutoGPT，从 CrewAI 到 LlamaIndex，所有框架的循环机制本质相同
2. **竞争力来自"循环内行为"**：智能体的优劣不在于使用何种框架，而在于模型是否学会在响应前调用验证工具
3. **"闭合循环"是认知行为而非工程问题**：它不需要新的代码架构，而是模型在既有循环中做出的更优决策

这一洞察具有重要的实践意义：企业在评估智能体能力时，应关注模型的验证意识而非底层框架；框架开发者无需发明新的循环机制，而应在如何引导模型做出更好决策上发力。

### 二、内循环：单任务可靠性保障机制

**内循环的本质**是"任务内自我验证"。作者以修复测试失败为例，展示了弱智能体与强智能体的行为差异：

```
弱智能体：编辑 auth.ts → 说"完成了"
强智能体：编辑 → 创建测试 → 运行 → 发现失败 → 修复边缘 case → 再次运行 → 看到绿灯 → 响应
```

两者使用**完全相同**的硬编码工具循环，差异仅在于强智能体**选择**在响应前进行多轮验证。这种选择从何而来？作者指出两个来源：

1. **系统提示词工程**（当前主要方式）：如"代码更改后始终运行测试"
2. **后训练强化**（趋势方向）：将测试通过/失败作为奖励信号，使模型将验证步骤内化

**后训练方法**的具体路径包括：
- **SFT（监督式微调）**：使用标注数据训练验证行为
- **RLHF/DPO**：通过人类偏好或直接偏好优化强化验证决策
- **过程奖励机制**：每步验证都给奖励，而非仅在最终成功时

从工程视角看，内循环的有效实施需要以下要素：
- 可调用的验证工具（测试框架、编译器、linters）
- 验证结果的可解析反馈机制
- 模型对验证失败的正确响应能力

### 三、外循环：跨时间知识积累机制

**外循环的本质**是"跨会话持久化学习"。作者指出了一个严峻的现实：**几乎没有智能体原生实现外循环**，因为每轮会话都是"白纸一张"——昨天在分页功能上失败的智能体，今天还会再次失败。

外循环的实现依赖于**持久化载体**的建立：

| 载体类型 | 作用机制 | 代表案例 |
|---------|---------|---------|
| **AGENTS.md** | 用户手动编写的项目级持久指令 | 项目编码规范、工作流程 |
| **会话交接文档** | 智能体生成的结构化摘要供后续使用 | 当前进度、待决策事项 |
| **SKILL.md** | 智能体从失败中自动生成的技能文档 | 避免重复犯错 |

作者特别强调 Claude Code 的 SKILL.md 机制：当智能体在某个任务中失败并找到有效解决方案后，它会自动将这个经验转化为可复用的技能文档。这意味着：
- 失败中的隐性知识被显性化为结构化文档
- 相同错误不会在不同会话中重复发生
- 跨任务的模式得以知识化共享

**外循环与内循环的关系**：
- 内循环解决"这一次任务是否正确完成"
- 外循环解决"下一个类似任务能否做得更好"
- 两者共同构成智能体的**可靠性**（任务内）+ **进化性**（跨时间）

### 四、"闭合循环"概念的本质还原

文章标题虽为"内循环 vs 外循环"，但核心贡献是对"闭合循环"（Closing the Loop）概念的澄清。

当前行业普遍存在两种误解：
1. **认为闭合循环需要新的基础设施**
2. **将"验证"理解为循环结构的改变**

作者的观点具有颠覆性：**闭合循环不改变循环结构，改变的是循环内的决策**。智能体利用现有的生成→工具调用→反馈循环，在认为工作"完成"之前，**选择**调用验证工具进行检查。

这种认知的实践意义：
- 框架开发者无需重构循环机制
- 应用开发者应关注验证工具的丰富度
- 模型开发者应通过后训练强化验证决策

## 真实性评估

| 声明/事实 | 验证状态 | 说明 |
| :--- | :--- | :--- |
| 所有智能体框架使用相同的生成→工具调用→反馈循环 | 已验证 | 与 LangChain、AutoGPT、ReAct 等框架的公开架构一致 |
| 内循环是单任务内的验证行为 | 已验证 | 与 Reflexion、Self-Verification 等学术工作一致 |
| 外循环需要持久化机制 | 已验证 | AGENTS.md、SKILL.md 等已有实际实现 |
| 当前几乎没有智能体原生实现外循环 | 部分验证 | 主流产品多依赖外部记忆系统，Claude Code 等产品正逐步实现 |
| 系统提示词是当前引导验证行为的主要方式 | 已验证 | 业界普遍采用 system prompt 工程实践 |
| 后训练是验证行为内化的趋势方向 | 已验证 | RLHF、DPO 等方法在 agent 训练中广泛应用 |

## 总结

本文以"工具调用循环是硬编码的"这一核心观察为基础，清晰辨析了内循环与外循环的本质差异：**内循环是单任务内的自我验证能力（可靠性），外循环是跨会话的持久化学习机制（进化性）**。作者澄清了"闭合循环"并非新的基础设施，而是智能体在既有循环架构内做出的更优决策。

**关键要点：**

- 工具调用循环是统一的脚手架，差异化来自循环内的决策选择
- 内循环的核心是"响应前验证"——编辑→创建测试→运行→修复→重新运行→响应
- 外循环依赖持久化载体（AGENTS.md、SKILL.md、会话交接文档）实现跨会话学习
- "闭合循环"是认知行为而非工程问题，无需新基础设施
- 验证行为的来源正在从系统提示词向后训练（奖励信号）演进

## 参考资料

- [Agents: Inner Loop vs Outer Loop（原文）](https://www.philschmid.de/inner-loop-vs-outer-loop)
- [AGENTS.md Format Specification](https://github.com/agentsmd/agents.md)
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)
- [InstructGPT: Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)
- [Claude Code Memory System Documentation](https://code.claude.com/docs/en/memory.md)
