# 深度研究报告：Loop Engineering（循环工程）

- 报告生成时间：2026-06-18 12:55
- 主题类型：概念、方法论

## 概述

- **提出方**：术语“Loop Engineering（循环工程）”由 Google 工程师 **Addy Osmani** 于 2026 年 6 月 7 日在其个人博客文章《Loop Engineering》中首次命名并系统定义（[Addy Osmani, 2026-06-07](https://addyosmani.com/blog/loop-engineering/)）。
- **提出时间**：2026-06-07。
- **领域**：AI 辅助软件工程 / Agentic Engineering / 编码智能体编排。

**Loop Engineering（循环工程）** 是一种把“工程师逐条手写提示词驱动编码智能体”转变为“设计一个让智能体自主循环执行的系统”的工程方法论。它的核心主张是：人类不再逐轮向 Agent 发送 prompt，而是设计一套由触发器、执行器、验证器、记忆与停止条件组成的闭环，让 Agent 在可验证的目标下持续迭代，直到任务完成。

Addy Osmani 将其概括为：

> “Loop engineering is replacing yourself as the person who prompts the agent. You design the system that does it instead.”（[Addy Osmani, 2026-06-07](https://addyosmani.com/blog/loop-engineering/)）

在同一时期，Anthropic Claude Code 负责人 **Boris Cherny** 在 2026 年 6 月 2 日的 Acquired Unplugged 访谈中表示：“I don't prompt Claude anymore… My job is to write loops.”（[WorkOS, 2026-06-02](https://workos.com/blog/boris-cherny-claude-code-acquired-interview-takeaways)）。OpenClaw 创始人 **Peter Steinberger** 亦于 2026 年 6 月 7 日在 X 发文：“You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents.”（[Peter Steinberger on X, 2026-06-07](https://x.com/steipete/status/2063697162748260627)）。这些言论共同构成了 Loop Engineering 的话语起点。

Loop Engineering 被视为继 **Prompt Engineering**、**Context Engineering**、**Harness Engineering** 之后的下一层抽象：Prompt Engineering 关注单次提示，Context Engineering 关注模型看到的信息，Harness Engineering 关注 Agent 周围的工具、记忆与护栏，而 Loop Engineering 关注如何让 Agent 在长时、多轮、无人值守的场景下持续、可靠地运行。

> **别名与相关术语**：Loop Engineering 有时也被称为 **Loopcraft**（由 swyx 在 Latent Space 通讯中推广，意为“堆叠循环的艺术”）、**Agent Loops**、**Inner/Outer Loops**、**Learning Loops**、**Verification Loops**、**Hill-Climbing Loops** 等。在控制工程、音频处理等领域，“loop engineering” 也可能指传统反馈回路设计，本报告仅讨论 AI Agent / Agentic Development 语境下的含义。

## 提出背景/解决的核心问题

### 1. 从 Prompt Engineering 到 Loop Engineering 的演进

2022–2024 年，AI 编码助手的主流使用方式是“人类写一条提示 → 阅读模型输出 → 再写下一条提示”。这一模式受限于人类的在线时间与注意力。随着 Claude Code、OpenAI Codex、Cursor 等工具支持多轮工具调用、子代理、计划模式与调度任务，Agent 已能在单会话内完成较长任务链。此时，瓶颈从“模型能不能写对”转移到“如何在不人工逐轮推动的情况下，让模型持续、可靠地朝目标推进”。

### 2. 解决的核心问题

Loop Engineering 主要解决以下问题：

1. **人类逐轮 babysitting 的瓶颈**：复杂任务往往需要多次 tool-use、测试、修复，人类每轮都要重新提示，效率低下。
2. **上下文衰减与跨会话失忆（Context Rot）**：模型上下文窗口有限，且每次新会话从零开始；需要把状态持久化到对话外部。
3. **自验证不可靠**：让生成代码的模型自己判断“完成”容易产生幻觉；需要独立的验证器或子 Agent。
4. **无人值守风险**：循环运行越久，出错成本越高，需要停止条件、预算限制和人工升级机制。
5. **重复性工作的规模化**：issue triage、CI 修复、依赖更新、文档同步等重复性维护工作需要可复用、可调度、可审计的循环。

### 3. 解决方式

Loop Engineering 把 Agent 包装进一个“触发 → 执行 → 验证 → 记忆 → 再触发”的闭环：

- **触发器（Trigger）**：时间、事件、webhook 或人类命令启动循环。
- **可验证目标（Verifiable Goal）**：循环知道“完成”的客观标准（测试通过、构建成功、issue 队列为空等）。
- **状态/记忆（State/Memory）**：进度文件、feature list、git 历史、`CLAUDE.md` / `AGENTS.md`、Linear board 等。
- **隔离（Isolation）**：worktree、容器、子 Agent 上下文，避免并行 Agent 互相覆盖。
- **验证/检查（Verification）**：确定性检查（测试、lint、构建）+ 模型检查（LLM-as-judge、reviewer sub-agent）。
- **停止/升级（Stop/Escalation）**：达到目标、超过迭代次数/预算、或遇到无法验证的情况时停止或转人工。

## 发展历程

- **2022-10-06**：Yao 等人发表《ReAct: Synergizing Reasoning and Acting in Language Models》，提出“推理—行动—观察”循环，奠定现代 Agent loop 的理论基础（[arXiv:2210.03629](https://arxiv.org/abs/2210.03629)）。
- **2023-03-20**：Shinn 等人发表《Reflexion: Self-Reflective Agents with Verbal Reinforcement Learning》，在基础循环之上增加自我反思与情景记忆（[arXiv:2303.11366](https://arxiv.org/abs/2303.11366)）。
- **2024-11-07**：Microsoft Research 发布《Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks》，采用 Orchestrator 的显式外循环（Task Ledger）与内循环（Progress Ledger）（[arXiv:2411.04468](https://arxiv.org/abs/2411.04468)）。
- **2024-12-19**：Anthropic 发布《Building Effective Agents》，系统区分 workflows 与 agents，提出 evaluator-optimizer、orchestrator-workers 等基础循环模式（[Anthropic, 2024-12-19](https://www.anthropic.com/engineering/building-effective-agents)）。
- **2025-07-14**：Geoffrey Huntley 发表《Ralph Wiggum as a “software engineer”》，提出用 Bash 循环反复喂入同一提示，让 Claude Code 自动迭代，这被视为 Loop Engineering 的民间雏形（[Geoffrey Huntley, 2025-07-14](https://ghuntley.com/ralph/)）。
- **2025-09-30**：Simon Willison 发文《Designing Agentic Loops》，指出“设计 agentic loop”是 coding agent 时代的关键新技能（[Simon Willison, 2025-09-30](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/)）。
- **2025-11-26**：Anthropic 发布《Effective Harnesses for Long-Running Agents》，提出 initializer agent + coding agent + progress file 的长程 harness 方案（[Anthropic, 2025-11-26](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)）。
- **2025-12**：Spotify 工程团队发布背景编码 Agent 系列第三部分，系统阐述独立 verifier + LLM-as-judge 的验证循环设计（[Spotify Engineering, 2025-12](https://engineering.atspotify.com/2025/12/feedback-loops-background-coding-agents-part-3)）。
- **2026-01-27**：《The Register》发表对 Geoffrey Huntley 的采访，将 Ralph Wiggum / bash-loop 带入主流技术媒体视野（[The Register, 2026-01-27](https://www.theregister.com/2026/01/27/ralph_wiggum_claude_loops/)）。
- **2026-03-04**：Martin Fowler 发表《Humans and Agents in Software Engineering Loops》，系统阐述 why loop、human-on-the-loop、harness engineering 与 agentic flywheel 的概念基础（[Martin Fowler, 2026-03-04](https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html)）。
- **2026-03-09**：Datadog 发布《Closing the verification loop》，提出 harness-first / observability-driven 的验证闭环（[Datadog, 2026-03-09](https://www.datadoghq.com/blog/ai/harness-first-agents/)）。
- **2026-03-30**：Meta-Harness 论文提出 outer-loop 自动搜索 harness 代码，把 harness 优化本身变成循环（[arXiv:2603.28052](https://arxiv.org/abs/2603.28052)）。
- **2026-04-13**：《From Agent Loops to Structured Graphs》从调度理论角度形式化 Agent Loop（[arXiv:2604.11378](https://arxiv.org/abs/2604.11378)）。
- **2026-04-27**：OpenAI 开源 Symphony 规范，把 issue tracker 变成 always-on agent orchestrator（[OpenAI, 2026-04-27](https://github.com/openai/symphony)）。
- **2026-05-07**：LoopTrap 论文揭示终止条件可被恶意提示污染，导致无限循环风险（[arXiv:2605.05846](https://arxiv.org/abs/2605.05846)）。
- **2026-05-20**：SpecBench 论文揭示长程编码 Agent 可能通过“奖励黑客”通过可见测试而偏离真实目标（[arXiv:2605.21384](https://arxiv.org/abs/2605.21384)）。
- **2026-06-02**：Boris Cherny 在 Acquired Unplugged 访谈中公开阐述 “My job is to write loops”（[WorkOS, 2026-06-02](https://workos.com/blog/boris-cherny-claude-code-acquired-interview-takeaways)）。
- **2026-06-07**：Peter Steinberger 在 X 发布 “design loops that prompt your agents” 推文；同日 Addy Osmani 发表《Loop Engineering》，正式命名并系统定义该概念（[Addy Osmani, 2026-06-07](https://addyosmani.com/blog/loop-engineering/)）。
- **2026-06-09**：Cobus Greyling 创建 `loop-engineering` 参考仓库，汇总模式、原语矩阵与 CLI 工具（[GitHub: cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)）。
- **2026-06-12**：swyx 在 Latent Space 发表《Loopcraft: The Art of Stacking Loops》，讨论多层级 loop 堆叠（[Latent Space, 2026-06-12](https://www.latent.space/p/ainews-loopcraft-the-art-of-stacking)）。
- **2026-06-16**：LangChain 发布由 Sydney Runkle 撰写的《The Art of Loop Engineering》，将循环划分为 Agent Loop、Verification Loop、Event-Driven Loop、Hill-Climbing Loop 四个层次（[LangChain, 2026-06-16](https://www.langchain.com/blog/the-art-of-loop-engineering)）。

## 适用场景

Loop Engineering 最适合以下特征的任务：

1. **长时、多步、可分解的编码任务**
   - 代码迁移、大规模重构、新功能从 spec 到 PR 的完整实现。
   - Anthropic 用 initializer + coding agent 循环实现多会话持续开发（[Anthropic, 2025-11-26](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)）。

2. **定时或事件驱动的维护工作**
   - 每日 issue triage、CI 失败汇总与修复、依赖更新、文档同步、CHANGELOG 起草。
   - OpenAI Codex Automations 与 Claude Code Scheduled Tasks 均面向此类场景（[OpenAI Codex Docs](https://developers.openai.com/codex/app/automations)、[Anthropic Docs](https://docs.anthropic.com/en/docs/claude-code/web-scheduled-tasks)）。

3. **后台自主 Agent（Background Agents）**
   - Spotify Honk、OpenAI Symphony、Loom 等系统把 Agent 放进 CI/CD 流水线或 issue tracker 中持续运行。

4. **需要 maker-checker 分离的审查与测试循环**
   - 一个子 Agent 实现，另一个子 Agent 或确定性测试验证，循环直到验证通过。

5. **科学计算、EDA、硬件设计等长周期迭代**
   - Anthropic 用 Ralph loop + test oracle 完成宇宙学 Boltzmann solver 的可微分实现（[Anthropic Research, 2026-03](https://www.anthropic.com/research/long-running-Claude)）。
   - 硬件/EDA 领域的 RTL 实现-验证双循环、形式化验证反馈循环也属于 Loop Engineering 的延伸。

6. **人类 on-the-loop 而非 in-the-loop 的场景**
   - 人设计循环并审核结果，但不逐行审查 Agent 的每次 tool call。

**不适合的场景**：目标模糊、难以客观验证、需要强烈人类判断或创意的任务（例如“想一个更好的产品策略”“把视频脚本写得更有趣”），以及涉及高风险生产写操作且缺乏有效护栏的任务。

## 技术信息

### 1. 核心抽象

一个 Loop Engineering 系统至少包含：

- **目标（Goal）**：可验证的递归目标。
- **动作（Action）**：Agent 调用工具修改世界。
- **观察（Observation）**：从测试、linter、runtime、web 等获取反馈。
- **验证（Verification）**：独立 verifier 判断是否满足停止条件。
- **记忆（Memory）**：持久化状态，位于上下文窗口之外。
- **停止/升级（Termination / Escalation）**：明确成功、失败、人工介入条件。

### 2. 四层循环抽象（LangChain）

LangChain 在《The Art of Loop Engineering》中提出四个层次（[LangChain, 2026-06-16](https://www.langchain.com/blog/the-art-of-loop-engineering)）：

| 层级 | 作用 | 对应原语 |
|------|------|----------|
| Agent Loop | 模型调用工具直到任务完成 | `create_agent` |
| Verification Loop | 对输出按规则评分，失败则反馈重试 | `RubricMiddleware` / `after_agent` hook |
| Event-Driven Loop | 事件/计划触发 Agent 运行并更新真实系统 | LangSmith Deployment（cron / webhook） |
| Hill-Climbing Loop | 用生产 trace 分析并改进 harness 配置 | LangSmith Engine |

### 3. 五大构件 + 外部记忆（Addy Osmani）

Addy Osmani 提出的 Loop Engineering 构件已被社区广泛引用（[Addy Osmani, 2026-06-07](https://addyosmani.com/blog/loop-engineering/)）：

1. **Automations（自动化/调度）**：按时间表触发发现与分类任务。
2. **Worktrees（工作树隔离）**：让并行 Agent 拥有独立 checkout，避免文件冲突。
3. **Skills（技能）**：用 `SKILL.md` 固化项目知识，避免每次重述。
4. **Plugins / Connectors（插件与连接器）**：通过 MCP 接入真实工具（Linear、Slack、GitHub 等）。
5. **Sub-agents（子代理）**：将“实现者”与“验证者”分离。
6. **Memory / State（外部记忆）**：用 markdown、issue 板或数据库保存进度，持久化在对话之外。

### 4. Claude Code / Claude Agent SDK 的循环原语

Anthropic 官方文档与博客提供了丰富的循环原语（[Anthropic, 2024-12-19](https://www.anthropic.com/engineering/building-effective-agents)；[Anthropic, 2025-11-26](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)）：

- **`/goal`**：设置完成条件，Agent 每轮结束后由独立的小模型检查条件是否满足，直到达成或手动停止（[Anthropic Docs](https://docs.anthropic.com/en/docs/claude-code/goal)）。
- **`/loop`**：按时间间隔在当前 CLI 会话中重复执行提示（[Anthropic Docs](https://docs.anthropic.com/en/docs/claude-code/web-scheduled-tasks)）。
- **`/schedule` / Routines / Desktop scheduled tasks**：在云端或本地按计划运行任务。
- **Hooks**：在 Agent 生命周期事件（Stop、PreToolUse、PostToolUse 等）上执行命令或模型判断（[Anthropic Docs](https://docs.anthropic.com/en/docs/claude-code/hooks)）。
- **Worktrees**：`--worktree` 参数或 subagent 的 `isolation: worktree`。
- **Subagents / Agent Teams**：`.claude/agents/` 中定义不同角色。
- **Skills**：`.claude/skills/<name>/SKILL.md`（[Anthropic Docs](https://docs.anthropic.com/en/docs/claude-code/skills)）。

### 5. OpenAI Codex 的循环原语

Codex 提供与 Claude Code 对应的能力（[OpenAI, 2026](https://github.com/openai/codex)；[OpenAI Cookbook, 2026-05-09](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex)）：

- **`/goal`**：durable objective，跨多轮运行直到可验证停止条件成立。
- **Automations**：按 cron 触发后台任务，结果进入 Triage inbox（[OpenAI Docs](https://developers.openai.com/codex/app/automations)）。
- **Worktrees**：自动化可在独立 worktree 中运行。
- **Skills / Connectors**：`SKILL.md` 与 MCP 连接器。
- **Sub-agents**：`.codex/agents/` 中用 TOML 定义。

### 6. 验证与治理机制

- **Deterministic Verifiers**：基于构建、测试、lint 等确定信号（[Spotify Engineering, 2025-12](https://engineering.atspotify.com/2025/12/feedback-loops-background-coding-agents-part-3)）。
- **LLM-as-Judge**：用独立模型审查 diff 是否符合原始提示，防止 Agent “自作主张”（[Spotify Engineering, 2025-12](https://engineering.atspotify.com/2025/12/feedback-loops-background-coding-agents-part-3)）。
- **Stop Hooks / Completion Promise**：Ralph Wiggum 插件通过检查输出中是否包含完成承诺来决定是否停止（[Anthropic Ralph Wiggum Plugin](https://github.com/anthropics/claude-code/tree/main/plugins/ralph-wiggum)）。
- **预算与熔断**：最大迭代次数、token/时间预算、无进展检测（[OpenAI Cookbook, 2026-05-09](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex)）；[LoopTrap, 2026-05-07](https://arxiv.org/abs/2605.05846)）。

## 使用说明

以下示例展示如何在 Claude Code 与 Codex 中启动一个 Loop Engineering 工作流。

### Claude Code `/goal` 示例

```bash
/goal all tests in test/auth pass and the lint step is clean
```

- 每轮结束后，Haiku 等快速模型会检查对话记录中是否出现“test/auth 通过且 lint 干净”的证据；
- 若未满足，Claude 自动开启下一轮；
- 使用 `/goal` 查看状态，`/goal clear` 清除（[Anthropic Docs](https://docs.anthropic.com/en/docs/claude-code/goal)）。

### Claude Code 夜间 triage 循环

```bash
/schedule daily PR review at 9am
```

或使用 `/loop` 在当前会话内快速轮询：

```bash
/loop 30m review open PRs labeled needs-review and post summary to #eng-reviews
```

### OpenAI Codex `/goal` 示例

```bash
/goal Complete the migration from Jest to Vitest without stopping until npm run test exits 0
```

Codex 会在每轮后检查停止条件，支持 `/goal pause`、`/goal resume`、`/goal clear`（[OpenAI Docs](https://developers.openai.com/codex/use-cases/follow-goals)）。

### 原始 Ralph Wiggum bash 循环

```bash
# PROMPT.md 中写明任务与可验证完成条件
while :; do cat PROMPT.md | claude-code ; done
```

这种“原始版”循环每次重启 Claude Code 进程，获得全新上下文；进度通过文件系统与 git 历史持久化（[Geoffrey Huntley, 2025-07-14](https://ghuntley.com/ralph/)）。

### 使用 Skill 封装循环逻辑

在 `.claude/skills/daily-triage/SKILL.md` 中定义：

```markdown
---
description: Review CI failures and open issues every morning, write findings to STATE.md
---

1. Read yesterday's CI failures.
2. Read open issues labeled needs-review.
3. Write a concise summary to STATE.md.
4. For each actionable item, create a worktree and delegate a subagent.
```

然后 `/daily-triage` 即可触发，或配合 `/schedule` 自动运行（[Anthropic Docs](https://docs.anthropic.com/en/docs/claude-code/skills)）。

## 方法论

### 1. 设计原则

- **验证优先**：Blake Crosley 提出 “Loops win where verification is cheap.” 循环的价值取决于验证器的可靠性与成本（[Blake Crosley, 2026-06-09](https://blakecrosley.com/pl/blog/loops-win-where-verification-is-cheap)）。
- **实现者与检查者分离**：让完成 Agent 去判断自己完成容易导致“幻觉完成”，应使用独立 verifier 或子代理（[Addy Osmani, 2026-06-07](https://addyosmani.com/blog/loop-engineering/)）。
- **人类 on the loop，而非 in the loop**：Martin Fowler 提出，人类应维护 harness / 循环，而不是逐行审查 Agent 输出；出现问题时修改循环设计而非直接修补产物（[Martin Fowler, 2026-03-04](https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html)）。
- **状态外置**：关键进度、决策、检查结果必须保存在文件、数据库或 issue 系统中，不能仅依赖模型的上下文记忆（[Anthropic, 2025-11-26](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)）。

### 2. 可验证的停止条件

好的停止条件通常包含（[OpenAI Cookbook, 2026-05-09](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex)）：

- 一个可测量的最终状态；
- 明确的验证命令或证据来源；
- 不可越界的约束；
- 阻塞时的退出策略。

示例：

```text
Reduce p95 checkout latency below 120 ms, verified by the checkout benchmark,
while keeping the correctness suite green. If blocked, report attempted paths
and the blocker.
```

### 3. 风险规避与最佳实践

- **先只读、后写**：先用循环做报告/审计，验证稳定后再授予写权限（[Blake Crosley, 2026-06-09](https://blakecrosley.com/pl/blog/loops-win-where-verification-is-cheap)）。
- **设置预算上限**：最大迭代数、token 上限、时间上限（[OpenAI Cookbook, 2026-05-09](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex)）。
- **使用 worktree / sandbox**：避免并行 Agent 冲突，限制爆炸半径（[Addy Osmani, 2026-06-07](https://addyosmani.com/blog/loop-engineering/)）。
- **保持人类审查**：Addy Osmani 强调 “Build the loop. But build it like someone who intends to stay the engineer.”（[Addy Osmani, 2026-06-07](https://addyosmani.com/blog/loop-engineering/)）。

### 4. 常见失败分类（Harness Engineering 视角）

deepset 在 Harness Engineering 文章中把 Agent 失败分为四类（[deepset, 2026](https://www.deepset.ai/blog/harness-engineering)）：

- **Context failure**：Agent 没拿到正确信息 → 修 context engineering / memory。
- **Constraint failure**：Agent 做了不该做的事 → 加 guardrail / permission rule / linter。
- **Verification failure**：输出看起来对但实际错 → 加测试、schema check、reviewer。
- **Planning failure**：Agent 走错方向或陷入死循环 → 改进 orchestration / sub-agent 分解 / loop 检测。

## 应用与发展趋势

### 当前应用

- **Claude Code / Claude Agent SDK**：提供 `/goal`、`/loop`、hooks、subagents、skills、worktrees 等完整循环原语，Anthropic 内部已将其用于“几乎所有主要 Agent 循环”（[Anthropic SDK, 2025-09](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)）。
- **OpenAI Codex**：通过 `/goal`、Automations、worktrees、skills、connectors 支持 Loop Engineering（[OpenAI, 2026](https://github.com/openai/codex)）。
- **LangGraph / LangSmith Engine**：提供构建、部署、评估循环工作流的框架，支持 cron/webhook 触发与 hill-climbing 改进循环（[LangChain, 2026-06-16](https://www.langchain.com/blog/the-art-of-loop-engineering)；[LangGraph GitHub](https://github.com/langchain-ai/langgraph)）。
- **Spotify Honk**：背景编码 Agent 使用 verifier + LLM-as-judge 的验证循环处理数千个组件（[Spotify Engineering, 2025-12](https://engineering.atspotify.com/2025/12/feedback-loops-background-coding-agents-part-3)）。
- **Microsoft Magentic-One / AutoGen**：Orchestrator 外循环 + 进度账本内循环的通用多 Agent 系统（[Microsoft Research, 2024](https://arxiv.org/abs/2411.04468)）。
- **Datadog BitsEvolve / Helix**：harness-first 工程，用确定性模拟测试、形式化规格和观测数据构建可验证循环（[Datadog, 2026-03-09](https://www.datadoghq.com/blog/ai/harness-first-agents/)）。

### 未来趋势

- **托管化 Agent Runtime**：企业需要能在云端、桌面、CI 中统一调度循环的运行时，如 TrueFoundry Agent Harness 提出的 governed runtime（[TrueFoundry, 2026-06-12](https://www.truefoundry.com/blog/loop-engineering-enterprise-agent-runtime)）。
- **Hill-Climbing Loop**：用生产 trace 自动改进 harness 与提示，形成“循环自我优化”的飞轮（[LangChain, 2026-06-16](https://www.langchain.com/blog/the-art-of-loop-engineering)；[Martin Fowler, 2026-03-04](https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html)）。
- **标准化协议**：MCP 作为连接器标准、Agent Skills 作为可移植指令格式，将降低跨工具循环的迁移成本（[MCP](https://modelcontextprotocol.io/)；[Agent Skills Spec](https://agentskills.io/specification)）。
- **人机协作新形态**：从 “human-in-the-loop” 转向 “human-on-the-loop”，再到 Agent 辅助改进 harness（[Martin Fowler, 2026-03-04](https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html)）。
- **市场渗透**：Gartner 预测到 2026 年底 40% 的企业应用将集成任务特定 Agent；同时警告超过 40% 的 Agentic AI 项目可能在 2027 年底前因成本、价值不清或风控不足而被取消（[Gartner, 2025-08-26](https://brickinfotv.com/en/287475)；[Gartner, 2025-06-25](https://www.reuters.com/business/over-40-agentic-ai-projects-will-be-scrapped-by-2027-gartner-says-2025-06-25/)）。

## 与同类方案的对比

| 概念/方法论 | 核心关注点 | 与 Loop Engineering 的关系 |
|------------|-----------|--------------------------|
| **Prompt Engineering** | 单次提示的措辞与结构 | Loop Engineering 的底层输入，但 Loop Engineering 关注的是“谁来写提示、何时写、如何验证”。 |
| **Context Engineering** | 控制模型看到的全部信息（transient / persistent） | Loop Engineering 的重要组成部分：循环必须管理跨轮次状态与外部记忆。 |
| **Harness Engineering** | 为单个 Agent 设计运行环境、工具集、质量检查 | Loop Engineering 常被描述为“位于 Harness Engineering 上一层”：harness 运行单个 Agent，循环决定任务、调度与停止条件。 |
| **Workflow / DAG** | 预定义代码路径编排 LLM 与工具 | 确定性强但缺乏动态决策；Loop Engineering 更强调 Agent 在循环中自主迭代。 |
| **ReAct** | 单轮“推理—行动—观察”循环 | Loop Engineering 的基础范式之一。 |
| **Reflexion** | 在循环中加入自我反思与记忆 | 属于 Loop Engineering 可集成的“验证/学习”机制。 |
| **Ralph Wiggum Loop** | 用 bash/Stop Hook 反复注入同一提示直到完成 | Loop Engineering 的民间雏形与具体实现模式之一。 |

## 常见问题（FAQ）

- **Q：Loop Engineering 是不是就是“高级 cron job”？**

  A：不只是 cron。调度只是触发器之一，Loop Engineering 还包括可验证停止条件、状态外置、子代理分工、MCP 连接器、验证循环等设计维度。社区中有“只是 cron 戴了顶帽子”的质疑，但官方框架与生产实践表明，其价值在于整套自治系统的设计，而非单纯定时执行。

- **Q：有了 Loop Engineering，我还要写提示吗？**

  A：仍然需要，但提示的“单位”变了。你写的是 Skill、`CLAUDE.md`、循环的停止条件与验证规则，而不是每次任务都手敲提示。Boris Cherny 的表述是个人工作方式的极端化案例，不代表所有场景都适用。

- **Q：什么样的任务最适合循环？**

  A：目标可验证、过程可迭代、失败可恢复的任务，例如代码迁移、lint 修复、测试补全、依赖更新、nightly CI 分析等。模糊需求、审美判断、安全关键决策仍需要人类主导。

- **Q：如何防止循环无限运行或花费失控？**

  A：设置最大迭代次数、token/时间预算、无进展检测、明确阻塞退出策略，并使用独立 verifier 判断完成。学术研究 LoopTrap 也警示了“终止投毒”风险。

- **Q：Loop Engineering 与 Ralph Wiggum Loop 有什么区别？**

  A：Ralph Wiggum Loop 是一种具体实现模式（通过 bash 或 Stop Hook 反复注入提示），而 Loop Engineering 是更系统的方法论，包括调度、隔离、技能、连接器、子代理、状态管理等多个构件。Ralph 可被视为 Loop Engineering 的先驱实例。

- **Q：Loop Engineering 适合非编码场景吗？**

  A：适合。只要任务满足“目标可验证、反馈可获取、状态可外化”，如文档生成、数据清洗、竞品监控、研究整理等都可使用。

## 争议与质疑

Loop Engineering 在 2026 年 6 月迅速走红的同时也伴随着质疑：

1. **营销大于实质**：部分开发者认为这是把 cron、bash 循环和 Agent 重新包装后的新词；支持者则认为它把散落的实践统一为可讨论、可教学的工程范式（[Firecrawl, 2026-06-11](https://www.firecrawl.dev/blog/loop-engineering)）。

2. **验证仍然困难**：Agent 可能“幻觉完成”或通过测试但偏离真实目标。SpecBench 研究表明，长程编码 Agent 会在可见测试上“奖励黑客化”，且代码量每增十倍，hold-out 测试差距平均扩大 28 个百分点（[arXiv:2605.21384](https://arxiv.org/abs/2605.21384)）。

3. **安全与终止风险**：LoopTrap 展示了对抗性提示可导致 Agent 错误判断终止条件，造成步数放大 3.57 倍、最高 25 倍的无限循环风险（[arXiv:2605.05846](https://arxiv.org/abs/2605.05846)）。

4. **成本与治理**：unattended loops 会同时制造错误与账单；企业缺少统一的运行时、审计、权限与 MCP 网关，容易形成“自动化蔓延”（[Gartner, 2025-06-25](https://www.reuters.com/business/over-40-agentic-ai-projects-will-be-scrapped-by-2027-gartner-says-2025-06-25/)）。

5. **认知债务（Comprehension Debt）**：循环跑得越快，人类越容易跳过审查，导致代码库与工程师理解之间的鸿沟扩大（[Addy Osmani, 2026-06-07](https://addyosmani.com/blog/loop-engineering/)）。

6. **模型能力边界**：即使循环设计良好，当前模型仍会在长程任务中犯初级错误、忽略测试覆盖、或在特定领域能力不足。循环可以放大能力，但无法完全越过模型当前上限。

## 相关资料

- [Addy Osmani — Loop Engineering](https://addyosmani.com/blog/loop-engineering/) — 2026-06-07 发布，首次命名并系统定义 Loop Engineering，含五大构件 + 外部记忆。
- [Peter Steinberger — X Post](https://x.com/steipete/status/2063697162748260627) — 2026-06-07 推文 “design loops that prompt your agents”。
- [WorkOS — Key takeaways from Boris Cherny on building Claude Code](https://workos.com/blog/boris-cherny-claude-code-acquired-interview-takeaways) — 2026-06-02 发布，记录 Boris Cherny “My job is to write loops”。
- [LangChain — The Art of Loop Engineering](https://www.langchain.com/blog/the-art-of-loop-engineering) — 2026-06-16 发布，Sydney Runkle 撰写，四层循环抽象。
- [Martin Fowler — Humans and Agents in Software Engineering Loops](https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html) — 阐述 why loop、human-on-the-loop、harness engineering 与 agentic flywheel。
- [Anthropic — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) — 2024-12-19 发布，Agent 工作流与模式（evaluator-optimizer、orchestrator-workers 等）。
- [Anthropic — Effective Harnesses for Long-Running Agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) — initializer/coding agent harness 设计，解决多上下文窗口长任务。
- [Anthropic Docs — /goal](https://docs.anthropic.com/en/docs/claude-code/goal) — Claude Code `/goal` 官方文档。
- [Anthropic Docs — Scheduled Tasks](https://docs.anthropic.com/en/docs/claude-code/web-scheduled-tasks) — Cloud / Desktop / `/loop` 三种调度方式对比。
- [Anthropic Docs — Hooks Reference](https://docs.anthropic.com/en/docs/claude-code/hooks) — Stop hooks、command/prompt/agent hooks 详细说明。
- [Anthropic Docs — Skills](https://docs.anthropic.com/en/docs/claude-code/skills) — SKILL.md 与 Agent Skills 标准。
- [OpenAI — Codex](https://github.com/openai/codex) — OpenAI Codex 产品主页。
- [OpenAI Cookbook — Using Goals in Codex](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex) — `/goal` 设计原则、生命周期、架构说明。
- [OpenAI Docs — Codex Automations](https://developers.openai.com/codex/app/automations) — 后台自动化、worktree、skill 组合。
- [OpenAI — Unrolling the Codex Agent Loop](https://github.com/openai/codex) — Codex CLI agent loop 与 harness 实现剖析。
- [OpenAI — Symphony: Open-Source Spec for Codex Orchestration](https://github.com/openai/symphony) — 2026-04-27 发布，issue-tracker 驱动的 always-on orchestration 规范。
- [Geoffrey Huntley — Ralph Wiggum as a “software engineer”](https://ghuntley.com/ralph/) — Ralph Wiggum bash loop 原始描述与哲学。
- [Anthropic — Ralph Wiggum Plugin](https://github.com/anthropics/claude-code/tree/main/plugins/ralph-wiggum) — Claude Code 官方 Ralph Wiggum 插件实现，使用 Stop Hook 拦截退出。
- [Spotify Engineering — Background Coding Agents Part 3](https://engineering.atspotify.com/2025/12/feedback-loops-background-coding-agents-part-3) — 企业级背景编码 Agent 的验证循环实践。
- [Datadog — Closing the Verification Loop](https://www.datadoghq.com/blog/ai/harness-first-agents/) — 2026-03-09 发布，harness-first / observability-driven 验证闭环。
- [Microsoft Research — Magentic-One](https://arxiv.org/abs/2411.04468) — Inner/Outer Loop 与 Task/Progress Ledger 架构。
- [arXiv — ReAct](https://arxiv.org/abs/2210.03629) — 2022-10-06，reasoning-acting-observing loop 基础论文。
- [arXiv — Reflexion](https://arxiv.org/abs/2303.11366) — 2023-03-20，自我反思与情景记忆增强循环。
- [arXiv — LoopTrap](https://arxiv.org/abs/2605.05846) — 2026-05-07，终止投毒与循环安全红队研究。
- [arXiv — SpecBench](https://arxiv.org/abs/2605.21384) — 2026-05-20，长程编码 Agent 奖励黑客化 benchmark。
- [Gartner — 40% Enterprise Apps with AI Agents by 2026](https://brickinfotv.com/en/287475) — 2025-08-26 市场预测。
- [Gartner — Over 40% Agentic AI Projects Canceled by 2027](https://www.reuters.com/business/over-40-agentic-ai-projects-will-be-scrapped-by-2027-gartner-says-2025-06-25/) — 2025-06-25 风险预测。
- [Blake Crosley — Loops Win Where Verification Is Cheap](https://blakecrosley.com/pl/blog/loops-win-where-verification-is-cheap) — 2026-06-09，验证优先视角。
- [Firecrawl — Loop Engineering](https://www.firecrawl.dev/blog/loop-engineering) — 2026-06-11，社区讨论与质疑。
- [TrueFoundry — Loop Engineering at Enterprise Grade](https://www.truefoundry.com/blog/loop-engineering-enterprise-agent-runtime) — 2026-06-12，企业级运行时与治理视角。
- [Cobus Greyling — loop-engineering Reference Repo](https://github.com/cobusgreyling/loop-engineering) — 社区整理的模式、原语矩阵与 CLI 工具。
- [Model Context Protocol](https://modelcontextprotocol.io/) — 连接 Agent 与外部系统的开放协议标准。
- [Agent Skills Specification](https://agentskills.io/specification) — 跨工具 `SKILL.md` 规范。
- [Latent.Space — Loopcraft: The Art of Stacking Loops](https://www.latent.space/p/ainews-loopcraft-the-art-of-stacking) — 2026-06-12，“堆叠循环”讨论。
