# 如何写好 AGENTS.md

> 原文：[Writing a Good AGENTS.md](https://www.philschmid.de/writing-good-agents)<br>
> 作者：Philipp Schmid<br>
> 日期：2026-02-24

## 原文及译文

<details>
<summary>原文</summary>
<section>

### Writing a Good AGENTS.md

AGENTS.md is injected into every coding agent conversation. It's infrastructure. And like all infrastructure, writing it well is harder than it looks.

Here's what the data and practitioners tell us about what actually works.

---

#### The Data Says: Less Is More

Research from ETH Zurich (2025) and HumanLayer's practical experience reveal a counterintuitive finding: more content in AGENTS.md often makes things worse.

**Key findings:**

- Auto-generated AGENTS.md files reduce task success rates by ~3% on average while increasing inference costs by over 20%.
- Human-written versions offer only marginal ~4% improvements while still raising costs by up to 19%.
- Stronger models (e.g., GPT-5.2) showed inconsistent results: 2% improvement on one benchmark, 3% degradation on another.
- Codebase overviews don't accelerate agent file discovery—agents require roughly equal steps with or without them.
- LLM-generated files improved performance by 2.7% only when all other documentation was removed, suggesting they harm performance specifically when duplicating existing resources.
- Agents respect AGENTS.md instructions faithfully, but unnecessary requirements increase reasoning tokens by 14–22%.

The takeaway: every line you add to AGENTS.md has a cost. Make sure it earns its place.

---

#### What to Include

**The WHAT — technology stack and structure**

Include your technology stack, project structure, and what each major component does. This is especially critical for monorepos: define which directories are apps, shared packages, and services.

**The WHY — project purpose**

Explain the project's purpose and the intent behind key components. This helps agents understand the underlying goal, not just the structure.

**The HOW — build, test, and verify**

Include the commands and procedures to build, test, and verify the project. Be explicit about non-obvious tooling choices.

> Example: specify `uv` instead of `pip`, or `bun` instead of `npm`. When agents see a tool mentioned in AGENTS.md, they use it **160 times more often** than unmentioned alternatives.

---

#### What NOT to Include

**Detailed codebase overviews or directory listings**

Research shows these don't accelerate agent file discovery. Agents navigate code effectively without them.

**Code style guidelines**

Use linters and formatters instead. They're faster, cheaper, and deterministic. LLMs naturally adopt existing code patterns—explicit style instructions are redundant and costly.

**Task-specific instructions that apply conditionally**

Since AGENTS.md appears in every session, instructions that only apply sometimes dilute agent focus. Frontier models reliably handle 150–200 instructions, but the agent harness already consumes roughly 50 of those slots. Every non-universal instruction competes for that budget.

**Auto-generated content**

Neither `/init` commands nor agent-self-generated AGENTS.md files improve outcomes. Write it yourself.

---

#### How to Structure It

**Keep it short**

The emerging consensus: under 300 lines. HumanLayer maintains theirs under 60 lines. Every line enters every session—quality matters far more than coverage.

**Use progressive disclosure**

Don't consolidate everything into AGENTS.md. Maintain task-specific documentation in separate files and reference them:

```
# Testing
See agent_docs/running_tests.md for test setup and commands.

# Database
Schema and migration guide: agent_docs/database_schema.md
```

The agent reads those files only when the task requires it.

**Reference, don't embed**

Point to file locations (using `file:line` format) rather than embedding code snippets that become outdated. AGENTS.md should be stable; implementation details belong in the source.

**Treat it as infrastructure**

Deliberate authorship only. Don't use AGENTS.md as a scratchpad or working document. It's injected everywhere—every careless line carries a cost.

</section>
</details>
<details>
<summary>译文</summary>
<section>

### 如何写好 AGENTS.md

AGENTS.md 会被注入每一次编程 Agent 对话。它是基础设施。和所有基础设施一样，写好它比看起来要难。

以下是数据和实践者告诉我们的真正有效的方法。

---

#### 数据说：少即是多

ETH Zurich（2025）的研究和 HumanLayer 的实践经验揭示了一个反直觉的发现：AGENTS.md 中的内容越多，往往越差。

**关键发现：**

- 自动生成的 AGENTS.md 平均使任务成功率降低约 3%，同时将推理成本提高超过 20%。
- 人工编写的版本仅提供约 4% 的边际改善，但仍将成本提高多达 19%。
- 更强的模型（如 GPT-5.2）表现出不一致的结果：在一个基准测试上提升 2%，在另一个上下降 3%。
- 代码库概述并不能加速 Agent 的文件发现——有没有它们，Agent 所需的步骤数大致相同。
- 仅当移除所有其他文档时，LLM 生成的文件才能提升 2.7% 的性能，这表明它们只有在不重复现有资源时才不会造成损害。
- Agent 会忠实遵守 AGENTS.md 中的指令，但不必要的要求会使推理 Token 增加 14–22%。

结论：你在 AGENTS.md 中添加的每一行都有成本。确保它值得被放在那里。

---

#### 应包含什么

**WHAT — 技术栈与结构**

包含你的技术栈、项目结构以及每个主要组件的作用。对于 Monorepo 来说尤为关键：明确哪些目录是应用、共享包和服务。

**WHY — 项目目的**

解释项目的目的以及关键组件背后的意图。这帮助 Agent 理解底层目标，而不仅仅是结构。

**HOW — 构建、测试与验证**

包含构建、测试和验证项目的命令与流程。明确说明非显而易见的工具选择。

示例：指定使用 `uv` 而非 `pip`，或使用 `bun` 而非 `npm`。当 Agent 在 AGENTS.md 中看到某个工具被提及时，它使用该工具的频率比未提及的替代工具高 **160 倍**。

---

#### 不应包含什么

**详细的代码库概述或目录列表**

研究表明这些内容并不能加速 Agent 的文件发现。Agent 即使没有它们也能有效地导航代码。

**代码风格指南**

改用 Linter 和 Formatter。它们更快、更便宜、且确定性强。LLM 会自然地采用现有的代码模式——明确的风格指令是多余的，且代价不菲。

**仅在特定条件下适用的任务专用指令**

由于 AGENTS.md 出现在每个会话中，仅有时适用的指令会分散 Agent 的注意力。前沿模型能可靠处理 150-200 条指令，但 Agent Harness 本身已占用约 50 个槽位。每一条非通用指令都在争夺这个有限的预算。

**自动生成的内容**

无论是 `/init` 命令还是 Agent 自生成的 AGENTS.md 文件，都不能改善结果。请自己手写。

---

#### 如何组织结构

**保持简短**

业界共识是：不超过 300 行。HumanLayer 将他们的 AGENTS.md 保持在 60 行以内。每一行都会进入每次会话——质量远比覆盖范围重要。

**使用渐进式披露**

不要把所有内容都集中在 AGENTS.md 中。在独立文件中维护特定任务的文档，并在 AGENTS.md 中引用它们：

```
# 测试
参见 agent_docs/running_tests.md 中的测试配置和命令。

# 数据库
Schema 和迁移指南：agent_docs/database_schema.md
```

Agent 只在任务需要时才读取这些文件。

**引用，不要嵌入**

使用文件位置引用（`file:line` 格式），而不是嵌入容易过时的代码片段。AGENTS.md 应该保持稳定；实现细节属于源代码。

**将其视为基础设施**

只能经过深思熟虑后才能写入。不要将 AGENTS.md 用作草稿本或工作文档。它会被注入每个地方——每一行草率的内容都有代价。

</section>
</details>

## 深度解读

这篇文章表面上是在讲"怎么写 AGENTS.md"，但它真正的价值在于：**用数据打破了关于 AI Agent 配置文件的几乎所有直觉。**

文章不是经验分享，而是实验结论——而那些结论大多是反直觉的。

---

### 一、最重要的数据：AGENTS.md 很可能正在拖累你的 Agent

文章引用的 ETH Zurich 2025 研究和 HumanLayer 实践数据，得出了一个让人不安的结论：

> **自动生成的 AGENTS.md 平均使任务成功率下降 3%，同时将推理成本提高超过 20%。**

即使是精心手写的版本，也只带来约 4% 的改善，代价是高达 19% 的成本增加。

这意味着：**大多数团队维护的 AGENTS.md，可能是净负收益的。**

为什么会这样？文章给出了两个核心机制：

**机制一：重复文档的代价**

LLM 生成的配置文件只有在移除所有其他文档时才能带来正收益（+2.7%）。一旦代码库里已经有 README、代码注释、文档文件，AGENTS.md 里的重复信息不会强化指令，反而会引入噪声——Agent 需要花额外 Token 来协调两个来源之间的细微差异。

**机制二：不必要指令的推理成本**

"Agents respect AGENTS.md instructions faithfully, but unnecessary requirements increase reasoning tokens by 14–22%."

Agent 不会忽略 AGENTS.md 里的内容，它会认真处理每一行。多余的指令不是被跳过，而是被消化——消化需要 Token，Token 就是钱，也是上下文空间。

这两个机制共同说明：**AGENTS.md 是一个高度受"内容质量"影响的系统，而不是"内容越多越好"的系统。**

---

### 二、160 倍效应：AGENTS.md 是工具偏置注入器

文章中最惊人的数据点：

> **当 Agent 在 AGENTS.md 中看到某个工具被提及时，它使用该工具的频率比未提及工具高 160 倍。**

这个数字意味着 AGENTS.md 对 Agent 的工具选择行为有决定性影响，远超任何单次对话中的指令。

这揭示了一个重要的系统属性：**AGENTS.md 不只是配置文件，它是工具路由的偏置层。**

实际影响：
- 如果你希望团队统一使用 `uv` 而不是 `pip`，在 AGENTS.md 中写一行比在代码评审中反复提醒有效得多
- 如果 AGENTS.md 中错误地提到了某个已弃用的工具，Agent 会以 160 倍的频率选择它
- 如果某个内部工具没有在 AGENTS.md 中出现，Agent 几乎不会主动使用它

这让 AGENTS.md 的工具提及成为一个需要谨慎管理的"高杠杆变量"——小小的遗漏或错误，会在每次 Agent 任务中被放大。

---

### 三、指令预算：一个被忽视的架构约束

文章提到了一个重要的系统限制：

> **前沿模型能可靠处理 150-200 条指令，但 Agent Harness 本身已占用约 50 个槽位。**

这意味着留给 AGENTS.md 的实际"指令预算"是 100-150 条。而且这个预算是被所有内容共享的：

```
指令总预算（150-200 条）
  ├── Agent Harness 消耗（~50 条）
  ├── AGENTS.md 通用指令
  ├── 每次会话的任务指令
  └── 工具说明、系统 Prompt 等
```

这引出了 AGENTS.md 设计的核心原则：**只放真正通用的、高价值的指令。**

任何只在特定任务类型中才有意义的指令，都不应该出现在 AGENTS.md 里——它会在无关任务中消耗宝贵的指令预算，同时带来不必要的推理负担（14-22% 的 Token 增加）。

这也是"渐进式披露"架构的根本理由：将任务专用文档放在独立文件里，Agent 只在需要时读取，从而将上下文的使用与任务的实际需求对齐。

---

### 四、Linter > 样式指南：确定性工具优于概率性指令

文章建议不在 AGENTS.md 中放代码风格指南，改用 Linter 和 Formatter，理由是"更快、更便宜、且确定性强"。

这个建议背后有更深的工程原理：

**概率性执行 vs. 确定性执行**

```
代码风格指南（写在 AGENTS.md）→ LLM 理解并尽力遵守 → 偶尔偏差
Linter / Formatter               → 机械执行              → 零偏差
```

LLM 对自然语言指令的遵守是概率性的，即使是非常清晰的指令也有小概率被忽视或误解。而 Linter 的执行是确定性的，不受上下文影响，不消耗 Token，也不占用指令预算。

这是一个更普遍的工程原则的具体应用：**凡是能用代码/工具强制执行的约束，就不要用自然语言来描述。** 把自然语言指令预算留给真正只能用自然语言表达的判断性约束。

---

### 五、Progressive Disclosure：一种 Context Engineering 架构模式

文章提出的"渐进式披露"结构，本质上是把 Context Engineering 的最佳实践引入了 AGENTS.md 设计：

```
AGENTS.md（始终加载）
  ↓ 引用
agent_docs/running_tests.md（任务需要时加载）
agent_docs/database_schema.md（任务需要时加载）
agent_docs/deployment_guide.md（任务需要时加载）
```

这与 Skill 的分层加载机制如出一辙：将"始终需要"的内容与"按需需要"的内容分离，让每次 Agent 会话的实际 Context 与任务需求精确匹配。

**文件引用 vs. 内容嵌入**

文章建议使用 `file:line` 格式引用而不是嵌入代码片段，理由是"代码片段容易过时"。这里有一个更深的考量：

- **嵌入代码片段**：AGENTS.md 成为第二个"真相来源"，需要与实际代码保持同步，维护成本高，且容易产生信息漂移
- **引用文件位置**：AGENTS.md 只是指针，真相仍在源代码中，Agent 读到的永远是最新内容

这让 AGENTS.md 更像一张"地图"，而不是一份"手册"——地图告诉你去哪里找信息，但不复制信息本身。

---

### 六、文章最重要的元观点：AGENTS.md 是基础设施

文章最后的建议是"Treat it as infrastructure"，这不只是一条实践建议，而是一个认知框架的转变。

**把 AGENTS.md 当成文档** → 越详细越好，不断追加 → 成本上升，效果下降

**把 AGENTS.md 当成基础设施** → 每一行都需要理由，变更需要谨慎，需要定期评估有效性 → 精简、稳定、高价值

这和 Skill 的"退休"建议有相同的底层逻辑：**AI Agent 系统的配置文件需要主动管理，而不是被动积累。** 随着模型能力提升、工具链变化、项目演进，AGENTS.md 中的某些内容会失去价值，甚至变成负担。定期审视和精简，和定期添加一样重要。

---

### 七、文章没有明说但值得关注的问题

**1. 团队共识问题**

如果 AGENTS.md 是团队共享的基础设施，谁有权修改它？缺乏治理的 AGENTS.md 很容易退化成"什么都往里塞"的垃圾桶，正是那种使成本上升、效果下降的反模式。

**2. 不同 Agent 系统的兼容性**

AGENTS.md 是 OpenAI Codex 等系统的约定，但不同 Agent 框架（Claude Code 的 CLAUDE.md、Cursor 的 `.cursorrules`）有各自的格式和加载规则。文章的建议是针对 AGENTS.md 的，但其核心原则——保持简短、用渐进式披露、不重复现有文档——对所有这类配置文件都适用。

**3. 基准测试的局限性**

ETH Zurich 的研究数据基于特定的编码任务基准，实际项目的任务分布可能不同。"代码库概述不加速文件发现"这个结论，在一个有复杂 Monorepo 结构的大型项目中是否同样成立，值得怀疑。数据驱动的建议需要在具体场景中验证。

---

### 核心结论

如果把这篇文章的洞察浓缩为一个框架：

**AGENTS.md = 通用偏置层，而非知识库**

它的核心职责是：
1. **工具路由**：明确指定非显而易见的工具选择（160 倍效应）
2. **结构定向**：帮助 Agent 快速理解项目的 WHAT、WHY、HOW
3. **上下文指针**：引用任务专用文档，而非复制内容

它不应该是：
- 代码库的百科全书
- 风格偏好的说明书
- 自动生成填充的内容
- 随时间不断膨胀的文档

以及一条与直觉相悖但有数据支撑的核心原则：

> **AGENTS.md 的价值不来自内容的丰富度，而来自内容的精准度。每一行都有代价，只有真正通用且无法从其他地方获取的信息，才值得占用这个空间。**

这是"Less is More"在 Agent 配置工程中最具体的体现。
