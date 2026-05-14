# 深度解读：The Problem is Prompt Debt

> 原文：[The Problem is Prompt Debt](https://www.dbreunig.com/2026/06/22/the-problem-is-prompt-debt.html)<br>
> 作者：Drew Breunig<br>
> 日期：2026-06-22

## 作者介绍

Drew Breunig，现任 Overture Maps Foundation 的 GERS Evangelist，同时担任 Useful Sensors 和 Source Cooperative 的顾问，公开资料显示其长期工作在文化人类学、计算机科学与媒体的交叉领域 [🔗](https://www.linkedin.com/in/drewbreunig)。此前他在 PlaceIQ/Precisely 担任策略高管超过十年，主导位置智能与隐私保护的数据策略，持有 3 项美国专利 [🔗](https://patents.google.com/?inventor=Drew+Breunig)。

Breunig 在 AI 工程社区中最具影响力的贡献是“Gods, Interns, and Cogs”框架（2024 年 10 月），该框架将 AI 用例分为三类，被 Simon Willison 等行业知名人士广泛引用 [🔗](https://simonwillison.net/2024/Oct/20/gods-interns-and-cogs/)。他自 2010 年起在个人网站 dbreunig.com 上发表了 149 篇文章，涵盖 AI、LLM、编程 Agent、Context Engineering 等主题 [🔗](https://www.dbreunig.com/writing.html)。其开源项目 `whenwords`（无代码的相对时间格式化库）在 GitHub 上获得 1291 颗星，曾获 Andrej Karpathy 赞赏 [🔗](https://github.com/dbreunig/whenwords)。他正在编辑 O'Reilly 出版的《The Context Engineering Handbook》[🔗](https://www.oreilly.com/radar/podcast/generative-ai-in-the-real-world-context-engineering-with-drew-breunig/)。

Breunig 在 2024-2026 年间年均发表约 35 篇深度博文，近期在 AgentCon Silicon Valley、MLOps Community Conference、Databricks Data + AI Summit 等会议上发表演讲 [🔗](https://www.linkedin.com/posts/drewbreunig_10-lessons-for-agentic-coding-activity-7458174921894940672-_2ol)。他在 Bluesky（@dbreunig.bsky.social）上非常活跃，在 LinkedIn 上拥有约 4055 名关注者 [🔗](https://bsky.app/profile/dbreunig.bsky.social)。其近年研究方向聚焦于 Agentic Coding、Spec-Driven Development、DSPy 生态和 Context Engineering，在 AI 工程实践社区中具有显著影响力。

参考来源：

- [LinkedIn：Drew Breunig 个人主页](https://www.linkedin.com/in/drewbreunig) — 当前职位、职业履历、教育背景
- [dbreunig.com：Writing 页面](https://www.dbreunig.com/writing.html) — 149 篇文章的完整列表
- [GitHub：dbreunig](https://github.com/dbreunig) — 52 个公开仓库，包括 whenwords（1291 Star）
- [O'Reilly Radar Podcast：Generative AI in the Real World](https://www.oreilly.com/radar/podcast/generative-ai-in-the-real-world-context-engineering-with-drew-breunig/) — 播客访谈，确认 O'Reilly 书籍编辑身份
- [Simon Willison：Gods, Interns, and Cogs](https://simonwillison.net/2024/Oct/20/gods-interns-and-cogs/) — 对 Breunig 框架的引用和放大
- [Google Patents：Drew Breunig](https://patents.google.com/?inventor=Drew+Breunig) — 3 项已授权美国专利
- [Bluesky：@dbreunig.bsky.social](https://bsky.app/profile/dbreunig.bsky.social) — 主要社交平台，412 关注者，612+ 帖子

## 原文及译文

<details>
<summary>原文</summary>
<section>

# The Problem is Prompt Debt

**Author:** Drew Breunig (dbreunig.com)
**Publication Date:** June 22, 2026
**Tags:** AI, Context, Prompting, LLMs, Engineering

## Subtitle / Core Thesis

"You can't be model agnostic if you're hand-tuning prompts"

## Opening

The article opens by celebrating how natural language interfaces enable rapid AI prototyping — writing in English and handing it to a frontier model yields a working prototype in an afternoon. But the author warns this is a trap for building reliable systems. The plain-English prompt that makes prototyping effortless is "a poor way to specify how a system should behave," and the cost arrives slowly, disguised as ordinary progress, until the application can barely move. The core problem isn't any single prompt; it's that "natural language was never meant to be a specification language for engineering."

## The Prompt Debt Trap

Three symptoms are described:

**1. Slowing iteration.** As users flag errors and edge cases, more guidance gets added to nudge the model. Instructions get repeated with increasing severity. The prompt stops being straightforward, quick fixes regress previous instructions, and the development cycle slows to a crawl.

A screenshot shows Fable's system prompt repeating copyright guidance up to six times across sections named `search_instructions`, `search_usage_guidelines`, `mandatory_copyright_requirements`, `hard_limits`, `self_check_before_responding`, and `critical_reminders`.

**2. Team incapacitation.** The brittle prompt, "full of edge cases and all-caps threats," becomes barely legible to its author and impenetrable to colleagues. Teams try to mitigate by breaking prompts into complicated templates assembled at runtime, but these segments evolve into "a thicket of conditions."

**3. Model lock-in.** Hot fixes that work on GPT-4o fail in entirely new ways on GPT-5.4-mini. Teams stay with the older model, hope deprecation emails are empty threats, and forgo cheaper, faster, better models. The author cites a Datadog report showing GPT-4o as the most-used model in observed traffic.

Together, these issues separate "a glorified prototype" from a product that can grow. AI features become frozen, improvable only through full rebuild, and locked to an aging model.

## Why Prompt Debt Happens

Natural language interfaces are wonderful for one-off tasks and broad conversations. Trouble comes when relying on natural language to define durable system behavior.

The imprecision of natural language paired with probabilistic models means different words expressing the same intent can yield different outputs. The author cites a study (arxiv.org/abs/2604.07709) where a clinical question asked in a patient's voice versus a physician's voice, with identical facts, flipped Opus from declining all ten times to answering all ten.

Word choice isn't the only factor. Seemingly unrelated statements in the same prompt can affect results. A Harvard study (arxiv.org/html/2407.06866v3) found that merely stating which NFL team a user rooted for changed how often the model refused sensitive-topic questions. "Spurious statements influence the inference pass in ways we can't predict." This is why prompts become more brittle as fixes are added — an instruction to quell one error can affect how the model interprets a separate instruction that worked yesterday.

Repeating instructions propels us toward prompt debt, but it's necessary when desired behavior conflicts with a model's training. The author calls this "fighting the weights." ChatGPT's image prompts used to instruct the LLM eight times not to reply when a generated image was returned, because the model was trained to always keep the conversation going.

Every coding agent system prompt analyzed featured repeated instructions, stern warnings, and all-caps demands. "Claude Code tells Opus seven times to return multiple tool calls in a single response." Fable's leaked system prompt restates one specific copyright rule six times.

None of these examples occurred in isolation. Multiple repeated rules are woven throughout. Stubborn errors grow prompts quickly, each addition increasing brittleness and the risk of regression with every edit.

And these fixes are tailored to a single model's behavior. A Berkeley-led study (arxiv.org/abs/2512.04123) found enterprises stay on older models because newer ones break their existing agents. Models aren't cleanly versioned software — they have different weights producing different behaviors in unpredictable, undocumented ways. Anthropic's own Fable release notes warn that skills developed for prior models can "degrade output quality."

Prompt debt locks an application to a single model. The inability to easily swap models isn't a clever moat from frontier labs — it's the result of "evolving a lossy, natural language specification against a probabilistic model."

## Preventing Prompt Debt

The author argues that programmers using coding agents have already shown the way. They sit at the leading edge, outliers on the "jagged frontier" of model abilities. Over the last couple years they've evolved best practices that let the model write more code while delivering maintainable, modular software.

**First principle:** Specify system behavior with measurements, not prose. When output is probabilistic and language imprecise, build hard edges: evaluations, metrics, and typed specifications. These are legible, shared artifacts colleagues can read and contribute to, enabling collaboration that brittle prompts prevented. The best engineers now spend more time on tests than ever, as tests are no longer a safety net but "the thing that lets the model cook."

**Second principle:** Stop writing the prompt by hand. Once metrics can score candidates, the prompt becomes something to search for rather than craft. The surface area of potential words, phrases, and structures in natural language is too vast for human hours. This is terrain LLMs were built to explore. Systems like DSPy and GEPA already manage this work, holding prompts accountable to your designs.

Once prompts are generated and behavior is defined by measurements, you're no longer bound to a particular model. Evaluating a new model takes hours, not weeks. When a faster, cheaper model arrives you can try it. When a deprecation email arrives, you can secure options in a day. Whether a model is pulled for regulatory reasons (as with Anthropic's Fable) or deprecated due to age (as Groq announced with Llama-3.1-8b), the fix is "a chore, not a fire drill."

The article closes by noting that every mature engineering discipline eventually stops doing by hand what it once prided itself on doing by hand: assembly gave way to compilers, hand-tuned queries gave way to planners, manual memory management gave way to machines. "Prompt-writing is no different."

Coaxing the model with exactly the right words is a real skill, and for one-off tasks it's often optimal. But to build reliable, improvable, and portable systems, "we should not be hand-tuning prompts."

## Footnote

The Datadog stat is from March 2026, so GPT-4o concentration has likely dropped somewhat. However, the author reports hearing from multiple large inference providers that usage of GPT-4o and similar-vintage models can exceed 50% of all calls.

---

*Article published under CC BY-NC 4.0 license.*

</section>
</details>

<details>
<summary>译文</summary>
<section>

# 提示债务问题

**作者：** Drew Breunig（dbreunig.com）
**发布日期：** 2026 年 6 月 22 日
**标签：** AI、上下文、提示、LLM、工程

## 副标题 / 核心论点

“如果你在手工调优提示，你就无法做到模型无关。”

## 开篇

文章开篇肯定了自然语言界面如何实现快速 AI 原型开发——用英语写好需求交给前沿模型，一个下午就能得到可工作的原型。但作者警告，这正是构建可靠系统的陷阱。让原型开发毫不费力的自然语言提示，恰恰是“指定系统应如何行为的糟糕方式”，而其代价来得缓慢，伪装成普通的进展，直到应用几乎无法动弹。核心问题不在于任何单条提示，而在于“自然语言从来就不是为工程规约语言而设计的”。

## 提示债务陷阱

文章描述了三个症状：

**1. 迭代放缓。** 当用户标记错误和边界情况时，越来越多的指导被添加进来以引导模型。指令被以越来越严厉的语气重复。提示不再简洁明了，快速修复会回归之前的指令，开发周期陷入停滞。

一张截图显示 Fable 的系统提示在 `search_instructions`、`search_usage_guidelines`、`mandatory_copyright_requirements`、`hard_limits`、`self_check_before_responding` 和 `critical_reminders` 等六个章节中重复版权指南多达六次。

**2. 团队失能。** 脆弱的提示“充满了边界情况和全大写的威胁”，对作者本人来说几乎不可读，对同事来说更是天书。团队试图通过将提示拆分为在运行时组装的复杂模板来缓解问题，但这些片段演变成了“一团乱麻般的条件语句”。

**3. 模型锁定。** 在 GPT-4o 上有效的热修复在 GPT-5.4-mini 上以全新的方式失败。团队停留在旧模型上，希望弃用邮件只是空洞的威胁，放弃了更快、更便宜、更好的模型。作者引用了 Datadog 的一份报告，显示 GPT-4o 是观测流量中使用最多的模型。

这些问题共同将“一个光鲜的原型”与一个能够成长的产品区分开来。AI 功能变得冻结，只能通过完全重建来改进，并被锁定在一个老化的模型上。

## 提示债务为何发生

自然语言界面对于一次性任务和广泛对话来说非常出色。问题出在依赖自然语言来定义持久的系统行为时。

自然语言的不精确性与概率模型相结合，意味着表达相同意图的不同词语可能产生不同的输出。作者引用了一项研究（arxiv.org/abs/2604.07709），其中以患者口吻和医生口吻提出的相同临床问题，在事实完全相同的情况下，使 Opus 从十次全部拒绝翻转为十次全部回答。

词语选择并非唯一因素。同一提示中看似无关的陈述也会影响结果。一项哈佛研究（arxiv.org/html/2407.06866v3）发现，仅仅说明用户支持哪支 NFL 球队，就会改变模型拒绝敏感话题问题的频率。“无关陈述以我们无法预测的方式影响着推理过程。”这就是为什么随着修复的添加，提示变得更加脆弱——一条用于平息某个错误的指令，可能会影响模型对昨天还正常工作的另一条指令的解释。

重复指令推动我们走向提示债务，但当期望行为与模型训练相冲突时，这是必要的。作者称之为“与权重对抗”。ChatGPT 的图像提示曾八次指示 LLM 在返回生成图像时不要回复，因为模型被训练为始终保持对话进行。

所分析的每一个编程 Agent 系统提示都包含重复的指令、严厉的警告和全大写的命令。“Claude Code 七次告知 Opus 在单次响应中返回多个工具调用。”Fable 泄露的系统提示将某条版权规则重复了六次。

这些例子都不是孤立发生的。多条重复的规则交织在一起。顽固的错误迅速膨胀提示，每次添加都增加了脆弱性和每次编辑时的回归风险。

而且这些修复是针对单一模型行为量身定制的。一项伯克利主导的研究（arxiv.org/abs/2512.04123）发现，企业停留在旧模型上，因为新模型会破坏其现有 Agent。模型不是干净版本化的软件——它们有不同的权重，以不可预测、无文档记录的方式产生不同的行为。Anthropic 自己的 Fable 发布说明警告称，为先前模型开发的技能可能“降低输出质量”。

提示债务将应用锁定在单一模型上。无法轻松切换模型并非前沿实验室的巧妙护城河——它是“针对概率模型演化一个有损的自然语言规约”的结果。

## 预防提示债务

作者认为，使用编程 Agent 的程序员已经指明了方向。他们处于领先地位，是模型能力“锯齿状前沿”上的离群值。在过去几年中，他们演化出了让模型编写更多代码同时交付可维护、模块化软件的最佳实践。

**第一原则：** 用测量指标而非散文来指定系统行为。当输出是概率性的、语言是不精确的时候，构建硬边界：评估、度量和类型化规约。这些是可读的、共享的工件，同事可以阅读和贡献，实现了脆弱的提示所阻止的协作。最优秀的工程师现在花在测试上的时间比以往任何时候都多，因为测试不再是安全网，而是“让模型发挥作用的那个东西”。

**第二原则：** 停止手写提示。一旦度量可以评分候选方案，提示就变成了需要搜索而非手工打造的东西。自然语言中潜在词语、短语和结构的表面积对于人工工时来说过于庞大。这是 LLM 被构建来探索的领域。像 DSPy 和 GEPA 这样的系统已经在管理这项工作，让提示对你的设计负责。

一旦提示被生成、行为由测量指标定义，你就不再被绑定到特定模型上。评估一个新模型只需数小时而非数周。当更快、更便宜的模型到来时，你可以尝试它。当弃用邮件到来时，你可以在一天内确保备选方案。无论模型是因监管原因被撤回（如 Anthropic 的 Fable）还是因年龄被弃用（如 Groq 宣布弃用 Llama-3.1-8b），修复都只是“一项杂务，而非消防演习”。

文章结尾指出，每一个成熟的工程学科最终都会停止手工做它曾经引以为豪的手工活：汇编让位于编译器，手工调优的查询让位于查询规划器，手动内存管理让位于机器。“提示编写也不例外。”

用精确的词语哄骗模型是一项真正的技能，对于一次性任务来说通常是最优的。但要构建可靠、可改进和可移植的系统，“我们不应该手工调优提示。”

## 脚注

Datadog 的数据来自 2026 年 3 月，因此 GPT-4o 的集中度可能已有所下降。然而，作者报告称从多家大型推理服务商处获悉，GPT-4o 及类似版本的模型使用量可能超过所有调用的 50%。

---

*文章以 CC BY-NC 4.0 许可协议发布。*

</section>
</details>

## 摘要

Drew Breunig 在这篇文章中提出了“提示债务”（Prompt Debt）这一新概念，将其类比为软件工程中的技术债务。文章核心论点是：自然语言从来就不是为工程规约语言而设计的，当团队依赖手工调优的自然语言提示来定义 AI 系统行为时，会不可避免地积累三种症状——迭代放缓、团队失能和模型锁定。文章通过 Fable 系统提示重复版权规则六次、Claude Code 七次告知 Opus 使用并行工具调用等具体案例，展示了即使是最先进的 AI 系统也无法避免提示债务。解决方案是双重的：用测量指标（评估、度量、类型化规约）而非散文来定义行为；使用 DSPy 和 GEPA 等系统自动搜索和优化提示空间。文章以历史类比收尾——正如汇编语言让位于编译器、手工查询让位于查询规划器，提示工程也应让位于系统化的自动优化。

## 术语表

| 术语 | 全称 | 解释 |
| :--- | :--- | :--- |
| Prompt Debt | - | 提示债务。Breunig 提出的新概念，指团队在手动调优 LLM 提示时积累的技术债务。表现为提示不断膨胀、包含冗余和矛盾的指令、对同事不可读、且将应用锁定在特定模型上。类比软件工程中的技术债务（Technical Debt）。 |
| DSPy | Declarative Self-improving Python | 斯坦福 NLP 实验室开发的 Python 框架，核心理念是“编程，而非提示”（Program, not prompt）。用类型化的签名（Signature）替代手写提示字符串，通过优化器（Optimizer）自动调优提示和少样本示例。ICLR 2024 论文发表，月下载量超 640 万次 [🔗](https://dspy.ai/)。 |
| GEPA | Genetic-Pareto | 遗传帕累托优化框架。使用基于 LLM 的反思（Reflection）和帕累托高效进化搜索来自动优化提示、代码和 Agent 架构。相比强化学习方法，仅需 100-500 次评估（RL 需 10000+ 次），速度快 35 倍。已被集成到 DSPy、MLflow、Google ADK 等框架中 [🔗](https://gepa-ai.github.io/gepa/)。 |
| Jagged Frontier | - | 锯齿状前沿。由沃顿商学院教授 Ethan Mollick 及其合作者于 2023 年提出的概念，描述 AI 能力的不均匀边界——AI 在某些任务上超越人类，同时在看似简单的任务上失败。Breunig 用此概念说明编程 Agent 用户处于 AI 能力边界的最前沿 [🔗](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged)。 |
| Model Agnostic | - | 模型无关。指方法或技术不依赖于任何特定模型，可在不同模型之间自由切换。在 Breunig 的语境中，指系统应能在不同 LLM 之间自由切换，而不被针对某一模型的提示所锁定。 |
| Fable | Claude Fable 5 | Anthropic 的“Mythos 级”模型，定位高于 Claude Opus。2026 年 6 月 9 日其完整系统提示被泄露（约 120000 字符），揭示了极其详细的安全指南和 22+ 工具定义。6 月 12 日因美国出口管制被暂停访问，6 月 30 日解除 [🔗](https://github.com/elder-plinius/CL4R1T4S/blob/main/ANTHROPIC/CLAUDE-FABLE-5.md)。 |
| Claude Code | - | Anthropic 的 AI 编程 Agent 工具，支持终端 CLI、VS Code/JetBrains 扩展、桌面应用和 Slack 集成。内置 35+ 工具，支持动态工作流和子 Agent。Breunig 引用其系统提示作为“与模型权重对抗”的例证 [🔗](https://code.claude.com/docs/en/)。 |
| GPT-4o | GPT-4 Omni | OpenAI 的旗舰多模态模型，128K 上下文窗口。尽管已从 ChatGPT UI 中退役，但根据 Datadog 2026 年报告，它仍是生产环境中使用最多的模型（22% 采用率）[🔗](https://developers.openai.com/api/docs/models/gpt-4o)。 |
| Datadog | - | 云监控与可观测性平台。2026 年 4 月发布了《State of AI Engineering 2026》报告，显示 GPT-4o 以 22% 采用率仍是使用最多的模型，超过 70% 的组织在生产中使用三种或更多模型 [🔗](https://www.datadoghq.com/state-of-ai-engineering/)。 |
| Opus | Claude Opus | Anthropic 的高端模型系列。在 Fable 5 发布后已不再是 Anthropic 的顶级模型。Breunig 引用的临床研究发现，Opus 对同一临床问题的回答因提问措辞不同而从 0% 翻转为 100% [🔗](https://arxiv.org/pdf/2407.00541)。 |
| System Prompt | - | 系统提示。开发者在用户交互开始前向 LLM 提供的特权指令集，定义模型的人设、行为约束、输出格式和任务范围。是 Prompt Debt 积累的主要场所。模型对 System Prompt 的遵从通过后训练（指令调优 + RLHF）学习，而非架构强制 [🔗](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/advanced-prompt-engineering)。 |
| Natural Language as Specification Language | - | 将自然语言用作规约语言。Breunig 的核心论点之一：自然语言从来就不是为工程规约语言而设计的，将其当作规约语言会悄悄限制你所能构建的东西。在软件工程中，规约语言（如 Z 语言、TLA+）具有严格的语法和语义，无歧义，而自然语言具有固有的模糊性 [🔗](https://github.com/jhugman/nlspec)。 |

## 深度解读

### 核心论点分析：提示债务的三阶段模型

Breunig 提出的“提示债务”概念之所以有力，在于它将一个模糊的痛点——提示越来越难维护——提炼为一个清晰的三阶段退化模型：

**第一阶段（迭代放缓）** 的本质是提示从“简洁的指令”退化为“补丁的集合”。每发现一个边界情况，团队就添加一条新规则。这些规则之间没有架构关系，只是线性堆叠。当规则之间开始相互冲突时，团队用更强烈的措辞（全大写、“IMPORTANT”、“NEVER”）来强制执行优先级，这又进一步降低了提示的可读性。

**第二阶段（团队失能）** 是组织层面的退化。当提示变得只有原作者能理解时，团队协作就崩溃了。原作者成为单点故障——他们休假时没人敢改提示。团队试图通过模板化来缓解，但这只是将问题从“一个巨大的提示”转移为“一团乱麻的条件语句”。

**第三阶段（模型锁定）** 是最隐蔽的代价。它不像前两个阶段那样表现为直接的开发效率下降，而是表现为机会成本——团队放弃了更快、更便宜、更好的新模型。Datadog 的数据（GPT-4o 仍占 22% 采用率）为这一论点提供了强有力的实证支撑。Breunig 的脚注进一步强化了这一点：多家推理服务商报告 GPT-4o 及同期模型占所有调用的 50% 以上。

这个三阶段模型的价值在于它的**可诊断性**——团队可以用它来评估自己处于哪个阶段，以及距离“只能通过完全重建来改进”还有多远。

### 技术维度：为什么自然语言不适合作为规约语言

Breunig 的论证建立在自然语言与概率模型交互的两个基本特性上：

**语义不稳定性。** 同一意图用不同词语表达可能产生不同输出。临床提问研究（arxiv.org/abs/2604.07709）提供了最生动的例证：以患者口吻和医生口吻提出的相同临床问题，使 Opus 从十次全部拒绝翻转为十次全部回答。这不是模型“理解”不同——而是词语选择触发了模型训练中不同的安全模式。

**上下文污染。** 哈佛 NFL 研究（arxiv.org/html/2407.06866v3）揭示了更隐蔽的问题：提示中看似无关的陈述（如用户支持哪支球队）会影响模型在完全不相关话题上的行为。这意味着提示中的每一条信息——无论多么无害——都可能以不可预测的方式影响输出。

这两个特性共同解释了为什么提示会随着修复的添加而变得更加脆弱：一条用于修复某个错误的指令，可能会通过上下文污染影响模型对另一条指令的解释。这就是 Breunig 所说的“与权重对抗”——你在用自然语言指令对抗模型训练中习得的深层模式，而自然语言在这场对抗中处于结构性劣势。

### 解决方案评估：从手工打造到自动化

Breunig 提出的两个原则——用度量定义行为、停止手写提示——在理论上是有说服力的，但在实践中面临几个挑战：

**DSPy 和 GEPA 的成熟度。** DSPy 已在学术界和部分企业（Databricks、Dropbox、Amazon Nova）中得到验证，ICLR 2024 论文发表，月下载量超 640 万次。GEPA 更年轻（2025 年 7 月论文），但已被集成到多个框架中。然而，这些工具仍然需要相当的专业知识来设置和调优——它们本身也有学习曲线。

**评估的挑战。** “用度量定义行为”的前提是你能定义好的度量。对于分类、数学推理等有明确正确答案的任务，这相对容易。但对于创意写作、对话质量、代码可维护性等开放式任务，定义好的度量本身就是一项研究挑战。

**历史类比的局限性。** Breunig 将提示工程类比为汇编语言、手工查询和手动内存管理，这些类比在方向上是有启发性的，但有一个关键差异：编译器、查询规划器和垃圾回收器是确定性的，而 LLM 是概率性的。即使使用 DSPy 自动搜索最优提示，不同运行之间仍可能存在方差。这意味着“自动化”在提示工程中可能永远无法达到编译器那样的确定性水平。

### 行业影响：模型锁定作为隐形成本

Breunig 文章中最具行业洞察力的论点可能是：**模型锁定不是前沿实验室的巧妙护城河，而是提示债务的自然结果。** 这一观点颠覆了常见的叙事——人们通常认为企业停留在旧模型上是因为 API 兼容性或迁移成本，但 Breunig 指出真正的原因是提示和行为期望与特定模型的特性紧密耦合。

这对行业有几个重要影响：

1. **模型提供商没有动力解决提示债务问题。** 如果提示债务导致模型锁定，这对模型提供商来说是收入保障。他们可能不会积极推广模型无关的最佳实践。

2. **模型无关性成为战略优势。** 能够快速切换模型的组织将拥有显著的竞争优势——他们可以始终使用性价比最高的模型，而不被任何单一提供商锁定。

3. **评估基础设施的投资回报率被低估。** 如果评估基础设施是模型无关性的前提，那么对评估的投资实际上是对“切换自由”的投资。

### 真实性评估

| 声明/事实 | 验证状态 | 说明 |
| :--- | :--- | :--- |
| 临床提问研究——Opus 从全部拒绝变为全部回答 | 已验证 | 论文为 David Gringras（哈佛大学）的《IatroBench》，以患者身份提问时 Opus 全部拒绝，以医生身份提问时全部回答，去耦差距 +0.65 [🔗](https://arxiv.org/abs/2604.07709) |
| 哈佛 NFL 研究——球队粉丝身份影响拒绝率 | 已验证 | 论文为 Victoria R. Li 等人的《ChatGPT Doesn't Trust Chargers Fans》，EMNLP 2024 发表。闪电队球迷角色在所有护栏类别中拒绝率最高 [🔗](https://arxiv.org/abs/2407.06866) |
| Datadog 报告——GPT-4o 是使用最多的模型 | 已验证 | Datadog《2026 年 AI 工程现状》报告确认 GPT-4o 采用率为 22%，仍是最常见模型 [🔗](https://www.datadoghq.com/state-of-ai-engineering/) |
| Fable 系统提示——版权指南重复六次 | 部分验证 | 泄露提示长达 1585 行，版权指南被大量重复的核心主张成立。确切的“六次”计数取决于如何界定独立章节与子章节 [🔗](https://github.com/saynchowdhury/claude-fable-5-system-prompt) |
| Claude Code——七次告知 Opus 使用并行工具调用 | 已验证 | nilenso.com 博客文章确认该指令在 Claude Code 系统提示中出现了 7 次 [🔗](https://blog.nilenso.com/blog/2026/02/12/how-system-prompts-reveal-model-biases/) |
| 伯克利研究——新模型破坏现有 Agent | 已验证 | 论文《Measuring Agents in Production》记录了案例 C10，明确指出 Agent 脚手架、提示和评估会锁定特定模型行为 [🔗](https://arxiv.org/abs/2512.04123) |
| Fable 发布说明——技能“降低输出质量” | 已验证 | Anthropic 官方平台文档原文为：“Skills developed for prior models are often too prescriptive for Claude Fable 5 and can degrade output quality.” [🔗](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5) |
| ChatGPT 图像提示——八次指示不要回复 | 部分验证 | 泄露的 `image_gen` 工具系统提示包含四条“不要”指令。确切的“八次”计数取决于计数方法 [🔗](https://github.com/asgeirtj/system_prompts_leaks/blob/main/OpenAI/tool-create-image-image_gen.md) |
| Groq 弃用 Llama-3.1-8b | 已验证 | Groq 于 2026 年 6 月 17 日发出弃用通知，停用日期为 2026 年 8 月 16 日 [🔗](https://github.com/scienceverse/metacheck/issues/319) |
| Fable 因“监管原因”被撤回 | 部分验证 | 实际原因是美国政府在“国家安全授权”下发出的出口管制指令，而非常规监管审查。Breunig 使用的“监管原因”在技术上可以成立，但具有误导性 [🔗](https://www.anthropic.com/news/fable-mythos-access) |

### 总结

Drew Breunig 的《The Problem is Prompt Debt》是 2026 年上半年 AI 工程领域最重要的文章之一。它成功地将一个广泛感受但未被清晰表达的痛点——“提示越来越难维护”——提炼为一个可诊断、可操作的概念框架。文章的三阶段模型（迭代放缓 → 团队失能 → 模型锁定）为团队评估自身提示债务水平提供了实用工具。文章的实证基础扎实——引用的 10 项主张中 7 项完全验证、3 项部分验证，核心论点均得到充分支撑。文章的主要局限在于：提出的解决方案（DSPy、GEPA）仍处于早期采用阶段，对大多数团队来说存在较高的学习曲线；历史类比（汇编→编译器）忽略了 LLM 概率性带来的根本差异。尽管如此，这篇文章很可能成为 AI 工程从“手工打造提示”走向“系统化提示优化”这一历史性转变的标志性文献。

**关键要点：**

- **提示债务是真实存在的生产问题**，而非理论担忧——Datadog 数据（GPT-4o 仍占 22% 采用率）和多个系统提示的实证分析提供了强有力的证据
- **自然语言不适合作为工程规约语言**——其固有的模糊性和概率模型的交互导致了语义不稳定性和上下文污染
- **解决方案是双重的**：用度量而非散文定义行为（评估驱动开发）；使用 DSPy/GEPA 等工具自动搜索提示空间
- **模型无关性是提示债务解决方案的自然产物**——当行为由度量定义时，切换模型从数周缩短到数小时
- **历史站在自动化一边**——每一个成熟的工程学科最终都停止了手工做它曾经引以为豪的手工活，提示工程也不例外

## 参考资料

- [Drew Breunig：The Problem is Prompt Debt](https://www.dbreunig.com/2026/06/22/the-problem-is-prompt-debt.html) — 被解读的原文
- [IatroBench：Pre-Registered Evidence of Iatrogenic Harm from AI Safety Measures](https://arxiv.org/abs/2604.07709) — 临床提问研究原文
- [ChatGPT Doesn't Trust Chargers Fans：Guardrail Sensitivity in Context](https://arxiv.org/abs/2407.06866) — 哈佛 NFL 研究原文，EMNLP 2024
- [Datadog：State of AI Engineering 2026](https://www.datadoghq.com/state-of-ai-engineering/) — GPT-4o 采用率数据来源
- [Measuring Agents in Production](https://arxiv.org/abs/2512.04123) — 伯克利主导的企业 Agent 研究
- [Anthropic：Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5) — Fable 5 发布说明原文
- [DSPy 官方文档](https://dspy.ai/) — DSPy 框架
- [GEPA 官方文档](https://gepa-ai.github.io/gepa/) — GEPA 框架
- [Ethan Mollick：Centaurs and Cyborgs on the Jagged Frontier](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged) — 锯齿状前沿概念来源
- [Anthropic：Fable and Mythos Access](https://www.anthropic.com/news/fable-mythos-access) — Fable 出口管制官方声明
- [Nilenso：How System Prompts Reveal Model Biases](https://blog.nilenso.com/blog/2026/02/12/how-system-prompts-reveal-model-biases/) — Claude Code 系统提示分析
