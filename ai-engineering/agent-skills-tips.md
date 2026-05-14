# 深度解读：8 Tips for Writing Agent Skills

> 原文：[8 Tips for Writing Agent Skills](https://www.philschmid.de/agent-skills-tips)<br>
> 作者：Philipp Schmid<br>
> 日期：2026-04-13

## 原文及译文

<details>
<summary>原文</summary>
<section>

```markdown
# 8 Tips for Writing Agent Skills

Skills have become one of the most used extension points in agents. They're flexible, easy to make, and simple to distribute.

But this flexibility also makes it hard to know what good and what works. What type of skills are worth making? What's the secret to writing a good skill? When do you share them with others?

I have been using skills extensively with many of them in active use. Here are some tips I've learned along the way.

## 1. Know What a Skill Is

A skill is a folder with a **SKILL.md** file and, optionally, some helper files:

my-skill/
├── SKILL.md ← The only required file
├── scripts/ ← Reusable code the agent can run
├── references/ ← Docs the agent reads when needed
└── assets/ ← Templates, images, or files used in output

A Skill consists out of 3 layers:
- **name and description Frontmatter** Goes into every prompt and tells the agent when to use the skill.
- **Body of SKILL.md** Markdown instructions (below frontmatter), that tells the agent how to do the task.
- **Assets** (optional), scripts/, references/, and assets/ folders.

Skills always fall into two categories:
- **Capability skills** help the agent do something the base model can't do consistently (e.g., PDF form filling) without it. These may become unnecessary as models improve, evals will tell you when.
- **Preference skills** encode your specific workflow (e.g., your team's code review steps). These are durable but need to stay in sync with your actual process.

## 2. Nail the Description

The description in your SKILL.md is the trigger mechanism. If it's vague, the agent won't know when to activate the skill. If it's too broad, the skill fires on every request. Be specific about what the skill does AND when to use it. Include both the "what" and the "when" in the description. The body of the skill only loads after the skill triggers.

| ❌ Too vague | ✅ Specific and actionable |
|---|---|
| "Helps with documents" | "Create, edit, and analyze .docx files, use for tracked changes, comments, formatting, or text extraction" |
| "API helper" | "Use when writing code that calls the Gemini API for text generation, multi-turn chat, image generation, or streaming" |

I have seen 50% improvements just by improving the description.

## 3. Write Instructions, Not Essays

Agents are smart. Your job is to tell it what it **doesn't already know**. Research shows longer, more comprehensive with too much context actually hurts performance.

- **Use directives:** "Always use `interactions.create()`", not "The Interactions API is the recommended approach." The first is an instruction, the second is trivia the agent won't act on.
- **Lead with examples:** A 5-line code snippet beats a 5-paragraph explanation.
- **Explain the why:** When a rule matters, say why. "Use model X, model Y is deprecated and will return errors" helps the agent generalize beyond specific test cases, not just memorize.
- **Don't overfit:** Avoid "fiddly" changes that only pass your three test prompts. Write skills that work across millions of invocations.

## 4. Keep It Lean

Don't dump everything into one file. The agent loads information in layers:

1. **Always loaded:** Frontmatter of SKILL.md, name + description
2. **Loaded when skill triggers:** the SKILL.md body (keep under 500 lines)
3. **Loaded on demand:** reference files, scripts, assets

If your skill covers multiple topics (e.g. AWS vs. GCP deployment), split them into separate reference files. The agent only reads the one it needs. This saves context for the actual task.

**Tip:** If a reference file is longer than 500 lines, add a table of contents with "line hints" at the top so the agent can quickly find what it needs.

## 5. Set the Right Level of Freedom

A common mistake in creating skills is turning the skill into a step-by-step workflow: "Step 1: Read the file. Step 2: Parse the JSON. Step 3: Extract the fields…" When you dictate every step, you take away their ability to adapt, recover from errors, or find better approaches. Describe what you want, not the path to get there.

**Tell the agent what to achieve:**
- ❌ "Step 1: Read the config file. Step 2: Find the database URL. Step 3: Update the port number. Step 4: Write the file back."
- ✅ "Update the database port in the config file to the value specified by the user."

**Provide constraints, not procedures:**
- ❌ "Step 1: Create a branch. Step 2: Make the change. Step 3: Run tests. Step 4: Open a PR."
- ✅ "Always run tests before opening a PR. Never push directly to main."

**If exact steps matter, write a script.** If the task is fragile and doing step 3 before step 2 breaks everything, that's not a skill problem, it's a scripting problem.

## 6. Don't Skip Negative Cases

Think about when the skill should **not** fire. A description like "Use for any coding task" will hijack every request.

> "Use when working with PDF files. Do NOT use for general document editing, spreadsheets, or plain text files."

Testing both "should trigger" and "shouldn't trigger" cases are essential. Without you'll optimize the skill in one direction.

## 7. Test It Before You Ship It

Don't ship a skill without evaluating. Each run might behave differently, so a single check isn't enough.

1. **Run it manually** a few times with different prompts. Watch where it breaks. Does it assume a dependency exists? Does it skip steps?
2. **Write down what "success" looks like** measurable. Does the output compile? Does it use the right API? Did it follow the steps? Grade outcomes, not paths.
3. **Try 10–20 test prompts**. Mix prompts the skill should handle, prompts it should ignore, and tricky edge cases. Each prompt should have its own success criteria.
4. **Run multiple trials.** Agent output is nondeterministic. Run 3–5 trials per prompt and look at the distribution instead of a single pass/fail.
5. **Isolate each run.** Use a clean environment for each test. Context bleeding between runs masks real failures.
6. **Fix the description first.** Most problems are in the trigger, not the instructions.

## 8. Know When to Retire a Skill

Run evals without the skill. If they pass, the model has absorbed the skill's value and the skill is no longer necessary. Retire it. This is especially true for capability skills, as models improve, the gap narrows.

For a practical step-by-step eval workflow, see [Practical Guide to Evaluating and Testing Agent Skills](https://www.philschmid.de/testing-skills).
```

</section>
</details>

<details>
<summary>译文</summary>
<section>

```markdown
# 编写 Agent Skills 的 8 条建议

Skills 已成为 Agent 系统中使用最广泛的扩展点。它们灵活、易于创建、分发简单。

但这种灵活性也带来了问题：什么才是好的、有效的？如何判断某种技能是否值得创建？编写好技能的秘密是什么？何时应该分享给别人？

我长期广泛使用 Skills，其中许多处于活跃状态。以下是我总结的一些经验。

## 1. 理解什么是 Skill

一个 Skill 是一个包含 **SKILL.md** 文件的文件夹，可选地包含一些辅助文件：

my-skill/
├── SKILL.md ← 唯一必需的文件
├── scripts/ ← Agent 可运行的可复用代码
├── references/ ← Agent 需要时读取的文档
└── assets/ ← 输出中使用的模板、图片或文件

一个 Skill 由 3 层构成：
- **name 和 description Frontmatter** 每次提示都会包含，告诉 Agent 何时使用该技能。
- **SKILL.md 主体** Frontmatter 下方的 Markdown 指令，告诉 Agent 如何执行任务。
- **Assets**（可选）scripts/、references/ 和 assets/ 文件夹。

Skills 始终分为两类：
- **能力型技能（Capability skills）** 帮助 Agent 完成基础模型无法可靠完成的事情（如 PDF 表单填写）。随着模型改进，这些技能可能变得不必要，评估会告诉你何时该退役。
- **偏好型技能（Preference skills）** 编码你的特定工作流程（如团队代码审查步骤）。这些是持久的，但需要与实际流程保持同步。

## 2. 精确打磨 Description

SKILL.md 中的 description 是触发机制。如果描述模糊，Agent 不会知道何时激活技能；如果太宽泛，技能会对每个请求都触发。要具体说明技能做什么 AND 何时使用。在描述中同时包含"什么"和"何时"。技能的正文只有在技能触发后才加载。

| ❌ 太模糊 | ✅ 具体且可执行 |
|---|---|
| "Helps with documents"（处理文档） | "Create, edit, and analyze .docx files, use for tracked changes, comments, formatting, or text extraction"（创建、编辑和分析 .docx 文件，用于处理修订、评论、格式或文本提取） |
| "API helper"（API 助手） | "Use when writing code that calls the Gemini API for text generation, multi-turn chat, image generation, or streaming"（编写调用 Gemini API 进行文本生成、多轮对话、图片生成或流式传输的代码时使用） |

仅通过改进 description，我就看到了 50% 的提升。

## 3. 写指令，而非文章

Agent 很聪明。你的工作是告诉它**不知道什么**。研究表明，更长、更全面的上下文实际上会损害性能。

- **使用指令式语言**："Always use `interactions.create()`" 而非 "The Interactions API is recommended."前者是指令，后者是 Agent 不会执行的信息。
- **以示例领先**：5 行代码示例优于 5 段解释。
- **解释原因**：当规则重要时，说出原因。"Use model X, model Y is deprecated and will return errors" 帮助 Agent 泛化而非机械记忆。
- **不要过度拟合**：避免只为通过三个测试提示的"小技巧"修改。编写能应对数百万次调用的技能。

## 4. 保持精简

不要把所有东西都塞进一个文件。Agent 分层加载信息：

1. **始终加载：** SKILL.md 的 Frontmatter，name + description
2. **技能触发时加载：** SKILL.md 主体（保持在 500 行以内）
3. **按需加载：** 引用文件、脚本、资源

如果技能涵盖多个主题（如 AWS vs. GCP 部署），拆分成独立的引用文件。Agent 只读取它需要的那一个。这节省了实际任务的上下文空间。

**提示：** 如果引用文件超过 500 行，在顶部添加带"行号提示"的目录，这样 Agent 可以快速找到需要的内容。

## 5. 设置适当的自由度

创建技能时的一个常见错误是把技能变成逐步工作流程："Step 1: Read the file. Step 2: Parse the JSON. Step 3: Extract the fields…"当你规定每一步时，你就剥夺了它们适应、纠错或找到更好方法的能力。描述你想要什么，而非到达那里的路径。

**告诉 Agent 要达成什么：**
- ❌ "Step 1: Read the config file. Step 2: Find the database URL. Step 3: Update the port number. Step 4: Write the file back."
- ✅ "Update the database port in the config file to the value specified by the user."

**提供约束，而非程序：**
- ❌ "Step 1: Create a branch. Step 2: Make the change. Step 3: Run tests. Step 4: Open a PR."
- ✅ "Always run tests before opening a PR. Never push directly to main."

**如果精确步骤很重要，写脚本。** 如果任务很脆弱，第 3 步在第 2 步之前做会破坏一切，这不是技能问题，是脚本问题。

## 6. 不要跳过负面案例

考虑技能应该**不**触发的情况。像"Use for any coding task"这样的描述会劫持每个请求。

> "Use when working with PDF files. Do NOT use for general document editing, spreadsheets, or plain text files."

测试"应该触发"和"不应该触发"两种情况都至关重要。否则你只会朝一个方向优化技能。

## 7. 发布前测试

不要在没有评估的情况下发布技能。每次运行的行为可能不同，所以单次检查是不够的。

1. **手动运行**几次，用不同的提示。观察哪里出问题。它是否假设某个依赖存在？是否跳过步骤？
2. **写下"成功"的样子**可衡量的。输出能编译吗？使用了正确的 API 吗？遵循了步骤吗？评估结果，而非路径。
3. **尝试 10–20 个测试提示**。混合技能应该处理的提示、应该忽略的提示和棘手的边缘情况。每个提示应有自己的成功标准。
4. **运行多次试验。** Agent 输出是非确定性的。每个提示运行 3–5 次，观察分布而非单一通过/失败。
5. **隔离每次运行。** 每次测试使用干净的环境。上下文污染会掩盖真实失败。
6. **先修复 description。** 大多数问题出在触发机制，而非指令。

## 8. 知道何时退役技能

不带技能运行评估。如果通过，说明模型已吸收技能的價值，技能不再必要。退役它。这对于能力型技能尤其如此，随着模型改进，差距会缩小。

有关实践性的分步评估工作流程，请参阅 [Practical Guide to Evaluating and Testing Agent Skills](https://www.philschmid.de/testing-skills)。

---

感谢阅读！如有问题或反馈，请在 [Twitter](https://twitter.com/_philschmid) 或 [LinkedIn](https://www.linkedin.com/in/philipp-schmid-a6a2bb196/) 上告诉我。
```

</section>
</details>

## 摘要

本文是 AI 工程领域专家 Philipp Schmid 关于如何编写高质量 Agent Skills（智能体技能）的实战经验总结。文章提出了 8 条核心建议，涵盖技能的定义描述、结构设计、编写原则、测试方法及生命周期管理。核心观点包括：技能描述是触发机制的核心，决定了技能何时被调用；指令编写应简洁直接，告诉智能体"不知道什么"而非冗长解释；技能应描述目标而非步骤，给智能体留有适应和纠错的空间；测试应覆盖正向触发、反向触发和边缘情况，并进行多次试验以应对非确定性输出。这是一篇实践导向极强的技术文章，对 Agent 开发具有重要参考价值。

## 术语表

| 术语 | 全称 | 解释 |
| :--- | :--- | :--- |
| Agent Skills | 智能体技能 | AI Agent 系统的扩展点，以文件夹形式组织，包含 SKILL.md 定义文件及可选的辅助文件 |
| SKILL.md | 技能定义文件 | Agent Skills 的核心文件，包含名称、描述（触发机制）和具体指令 |
| Frontmatter | YAML 头信息 | 位于 SKILL.md 文件顶部的元数据区域，包含 name 和 description 字段 |
| Capability Skills | 能力型技能 | 补充基础模型不足的技能（如 PDF 表单填写），随模型进化可能失效 |
| Preference Skills | 偏好型技能 | 编码特定工作流程的技能（如代码审查步骤），需与实际流程保持同步 |
| Trigger Mechanism | 触发机制 | SKILL.md 中的 description 字段，决定技能何时被激活 |
| Evals | 评估/测试 | 系统性测试 Agent 技能性能的方法，通过标准化任务集衡量成功率 |
| Pass@k | K次采样通过率 | 衡量 Agent 可靠性的指标，表示 k 次生成中至少一次通过的概率 |
| Context Bleeding | 上下文污染 | 测试间隔之间残留的上下文信息，可能掩盖真实失败 |
| Line Hints | 行号提示 | 引用文件顶部的目录索引，帮助智能体快速定位内容 |
| Competion Rate | 任务完成率 | Agent 成功完成任务的百分比，是核心评估指标之一 |

## 深度解读

### 一、核心框架：技能的三层架构与两大分类

本文首先建立了理解 Agent Skills 的基本框架。技能由三个层次构成：**Frontmatter**（名称+描述，始终加载）、**SKILL.md 主体**（技能触发时加载，建议 500 行以内）、**辅助资源**（按需加载，包括 scripts/、references/、assets/ 三个可选文件夹）。

这种分层加载设计体现了重要的工程智慧：将最关键的触发信息压缩到最小体积，确保每次推理都加载；而将详细指令和参考资料作为按需资源，避免污染基础上下文窗口。Anthropic 的研究也验证了这一点——长时间运行 Agent 的核心挑战正是**上下文窗口的有限性**，压缩机制虽有帮助但仍不够用。

技能的两大分类——能力型（Capability）与偏好型（Preference）——揭示了技能的不同生命周期特性。能力型技能填补模型当前的能力缺口，但随模型进化会逐渐变得多余；偏好型技能编码特定团队的工作流程，更为持久但需要与实际流程保持同步。这一分类帮助开发者思考：创建某个技能是解决当前模型的能力问题，还是固化特定的工作流程偏好？

### 二、触发机制：Description 是技能的核心

本文最重要的洞察之一是：**Description 是触发机制，而非简单的说明文字**。这意味着 description 的质量直接决定了技能何时被激活——太模糊导致该触发时不触发，太宽泛导致不该触发时也触发。

作者声称"仅通过改进 description 就实现了 50% 的提升"，这一数据虽来自单一经验，但与行业实践一致。Description 应同时包含"做什么"（what）和"何时用"（when）两个维度，例如：
- ❌ 模糊表述："Helps with documents"
- ✅ 精确表述："Create, edit, and analyze .docx files, use for tracked changes, comments, formatting, or text extraction"

这一原则与传统的"描述应简洁"的建议不同——在 Agent Skills 场景下，description 的精确性优先级更高，因为它直接影响技能是否被正确调用。

### 三、指令编写：告诉智能体"不知道什么"

文章指出了一个反直觉的原则：**智能体很聪明，不需要教它已知的东西**。这与传统的详细文档编写方式截然相反。研究表明，过多、过全面的上下文实际上会**损害性能**。

这一观点得到了学术研究的支持。LongICLBench（2024）的研究显示，现有 LLM 在长上下文理解和推理方面仍有显著挑战——当任务复杂且标签空间扩大时，性能急剧下降。另一项 ICLR 2024 的研究则证明，4K 上下文配合检索增强可以达到 16K 上下文的性能，说明**单纯扩展上下文并非最优解**。

基于此，文章提出了四条具体原则：

1. **使用指令式语言**："Always use `interactions.create()`" 而非 "The Interactions API is recommended"——前者是可执行的指令，后者是智能体不会执行的信息
2. **以示例领先**：5 行代码示例优于 5 段解释
3. **解释原因**：当规则重要时，说明原因。例如"Use model X, model Y is deprecated" 帮助智能体泛化而非机械记忆
4. **避免过度拟合**：不要为通过三个测试提示而做特殊处理，要使技能在数百万次调用中都能正常工作

### 四、适度放手：描述目标而非路径

这是本文最具洞见性的观点之一。当技能被写成详细的步骤清单时，实际上剥夺了智能体的核心能力——适应力、纠错能力和寻找更优解的能力。

文章用两个鲜明的对比说明了这一点：
- ❌ "Step 1: Read the config file. Step 2: Find the database URL..."（告诉智能体如何做）
- ✅ "Update the database port in the config file to the value specified by the user."（告诉智能体要什么）

作者同时区分了**约束**与**程序**的不同：约束是规则（如"PR 之前必须运行测试"），程序是步骤清单。技能应提供约束而非程序。

对于真正需要精确步骤的脆弱任务，作者的建议是：**写脚本而非技能**。这划定了一个重要的边界——当任务的关键在于"顺序"而非"理解"时，应该用代码（脚本）而非自然语言指令（技能）来解决。

### 五、负面案例：技能不应触发的场景

这是被许多技能编写者忽视但至关重要的一个维度。如果只测试技能应该触发的情况，会优化出一个"总是触发"的技能。真正的技能需要同时考虑：
- 何时应该触发
- 何时**不应该**触发

例如："Use when working with PDF files. **Do NOT use** for general document editing, spreadsheets, or plain text files." 这种明确的排除说明防止技能被过度调用。

### 六、测试方法论：应对非确定性的系统化流程

文章提供了一个相当完整的测试框架，其核心洞察是：**Agent 输出是非确定性的，单次运行不足以判断技能质量**。

测试建议包括：
- **10-20 个测试提示**：覆盖应该处理的提示、应该忽略的提示和边缘情况
- **3-5 次重复试验**：观察结果分布而非单一通过/失败
- **隔离每次运行**：使用干净环境避免上下文污染
- **先修 description**：大多数问题出在触发机制而非指令本身

这些建议与 Agent 评估领域的最佳实践高度一致。Pass@k 指标（即在 k 次采样中至少一次通过）正是为了解决 Agent 输出非确定性问题而设计的——Pass@1 衡量基础能力，Pass@100 衡量潜在上限。

### 七、技能生命周期：知道何时退休

最后一个观点往往被忽视：**技能不是永久的**。随着模型能力的提升，曾经需要能力型技能弥补的缺口会逐渐消失。作者建议定期运行不带技能的评估——如果通过，说明模型已吸收技能的價值，应该退役。

这反映了一个重要的工程思维：**技能应该是临时性的能力补充，而非永久的基础架构**。

### 真实性评估

| 声明/事实 | 验证状态 | 说明 |
| :--- | :--- | :--- |
| "Skills have become one of the most used extension points in agents" | 已验证 | Skills/Extensions 作为 Agent 扩展机制被广泛采用，有 Anthropic、Google 等官方文档支持 |
| "I have seen 50% improvements just by improving the description" | 部分验证 | 单一来源经验，但描述精确性的重要性与 Agent 触发机制原理一致 |
| "Research shows longer, more comprehensive with too much context actually hurts performance" | 已验证 | LongICLBench (2024)、Retrieval meets Long Context (ICLR 2024) 等研究支持此观点 |
| "Agent output is nondeterministic" | 已验证 | 这是 LLM 的固有特性，被广泛确认 |
| "Run 10–20 test prompts" | 部分验证 | 符合行业测试实践，但具体数字是建议而非硬性要求 |
| 技能的两大分类（Capability vs Preference） | 已验证 | 该分类在 Agent 开发社区被广泛采用 |
| SKILL.md 结构（3层+3文件夹） | 已验证 | 与主流 Agent 框架（如 Claude Code Skills）的实现一致 |
| "Keep SKILL.md body under 500 lines" | 部分验证 | 500 行是经验性建议，与分层加载的设计原则一致 |

### 总结

本文是 Agent Skills 开发的实战指南，核心价值在于建立了一套系统性的技能编写方法论。八大建议并非独立技巧，而是相互关联的完整体系：理解技能本质（定义）→ 掌握触发机制（Description）→ 遵循编写原则（指令）→ 保持轻量设计（结构）→ 赋予适当自由（粒度）→ 考虑边界情况（负面案例）→ 系统化测试（验证）→ 规划生命周期（退休）。

文章的核心哲学是**简洁、精确、留有余地**——告诉智能体不知道什么、达成什么目标、何时不该介入，而非教它每一步怎么做。这与 AI 领域"简单即有效"的设计原则一脉相承。

**关键要点：**

- Description 是触发机制而非说明文字，需要同时包含"做什么"和"何时用"
- 指令应告诉智能体"不知道什么"，而非已知信息的冗长复述
- 描述目标而非路径，给智能体适应和纠错的空间
- 测试必须覆盖正向触发、负向触发和边缘情况，并进行多次试验
- 技能有生命周期，应随模型能力提升而退役

## 参考资料

- [8 Tips for Writing Agent Skills - 原文](https://www.philschmid.de/agent-skills-tips) — 作者实战经验总结
- [Anthropic - Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) — Agent 设计最佳实践
- [Anthropic - Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) — 长时间运行 Agent 的上下文管理挑战
- [LongICLBench - arXiv:2404.02060](https://arxiv.org/abs/2404.02060) — 长上下文 LLM 性能研究
- [Retrieval meets Long Context - arXiv:2310.03025](https://arxiv.org/abs/2310.03025) — 检索增强与长上下文研究
- [AgentBench - arXiv:2308.03688](https://arxiv.org/abs/2308.03688) — 多维度 LLM Agent 基准
- [HumanEval - OpenAI](https://arxiv.org/abs/2107.03374) — Pass@k 指标起源论文
- [SWE-bench](https://swebench.com/) — 软件工程 Agent 基准测试
