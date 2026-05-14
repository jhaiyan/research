# 深度解读：What Is Code?

> 原文：[What Is Code?](https://martinfowler.com/articles/what-is-code.html)<br>
> 作者：Unmesh Joshi（Thoughtworks 杰出工程师，著有 *Patterns of Distributed Systems*）<br>
> 日期：2026-05-12

## 原文及译文

<details>
<summary>原文</summary>
<section>

# What Is Code?

*By Unmesh Joshi — 12 May 2026 — Tag: generative AI*

## Introduction

What is code? At a high level, the answer seems obvious. Code is what developers write to instruct a machine. But with modern LLMs, we no longer need to type every word to produce code. So a deeper question emerges: if producing code becomes cheaper, what remains valuable about code?

## Two Aspects of Code

Code has always served two distinct but intertwined purposes. First, it is a set of instructions to a machine. Second, it is a conceptual model of the problem domain. In the era of LLMs, this is the part being commoditized. The activity of coding is where these two aspects meet, as developers shape concepts, names, boundaries, and relationships.

## Conceptual Models and Vocabulary

Making the conceptual model explicit is the deeper aspect of coding, driven by the domain and use cases. Vocabulary is the set of words used in a particular language or subject. Knowing English is not enough to understand a software development article; software development is a broad, mature field with its own technical vocabulary. Communication depends on shared vocabulary. Whether we are communicating with a person, a framework, or an LLM, the words we use must map to concepts that the receiver can understand and act upon.

## Vocabulary in Code

A well-designed codebase is a representation of a certain vocabulary. Software development sits on the intersection of various domains — banking, finance, retail, inventory, healthcare, insurance on one end, and web, infrastructure, AI, data engineering on the other. Vocabulary is more than labels: it carries meaning, constraints, and design consequences.

Coding for a domain is fundamentally an act of translation. The developer maps the domain vocabulary onto the vocabulary of technical domains. Concepts become types, relationships become interfaces, rules become invariants, and workflows become compositions. The right abstraction often is not obvious upfront; it reveals itself only as you continually mold and refactor the code against real-world constraints.

Frameworks and libraries are codified vocabularies that capture common patterns, with the Spring Framework cited as an example.

## Bounded Contexts and Local Vocabularies

Frameworks work well for stable, recurring structures, but domains like online retail or stock exchange differ. The main reason there is no universal high-level framework is that the vocabulary is not stable enough across all instances of the domain. This leads to the idea of a bounded context, which marks the boundary within which a particular vocabulary and model are valid.

Techniques like TDD are praised for helping discover the right names, the right abstractions, and the right boundaries. The article connects this to agile values and to the ubiquitous language of Domain-Driven Design — a shared language developed by developers and domain experts and tested continuously against working software.

## Programming Languages As Thinking Tools

Building vocabulary through code requires active engagement in writing and reshaping code; not just passive review of generated code. Programming languages serve as thinking tools — Go's channels, Java's object-oriented model, and Rust's ownership model all shape how problems are approached.

**Code example — Future API composition in Java:**

```java
var future1 = action1();
future1.thenCompose(val1 -> action2(val1))
       .thenCompose(val2 -> action3(val2))
```

The author comments that knowing the concepts and vocabulary of functional programming is crucial to be able to implement this API well. Not knowing those concepts results in awkward implementation and usage.

**Code example — pseudo-formal spec for snapshot isolation:**

```
Begin(T, coord):
  R(T) := HLC(coord).now()
  writeSet(T) := {}


Read(T, N, key):
    N.HLC.tick(R(T)) //HLC advanced. So any write or commit after this is guaranteed to be at a higher ts
    return latest committed version of key with ts <= R(T)


Write(T, N, key, value):
    N.HLC.tick(R(T))
    if LatestCommittedVersion(key).ts > R(T):
        abort T
    place provisional intent for (key, value)
    writeSet(T) := writeSet(T) union {key}
```

The author notes that this pseudo-formal spec helped clarify my thinking and served as a good basis for further discussions, implementation and validations through tests.

## Working with LLMs

LLMs are trained on vocabulary from text and code and learn recurring relationships between names, APIs, libraries, frameworks, idioms, design patterns, and implementation structures. If our prompts use vague or inconsistent language, the model has to guess the design we intend. Precise, consistent vocabulary embodied in the code allows the LLM to map intent more reliably.

## Cognitive Debt

The article introduces cognitive debt, which accumulates when words, abstractions, and structures are used without their meaning being well understood by the people working with them. LLMs amplify this risk by generating plausible code quickly. The problem is not that the LLM generated code. The problem is that the code introduced vocabulary faster than the developers built understanding.

## Code as a Shared Conceptual Model

Referring to a prior article on *Designing Abstractions with LLMs*, the author states: writing code has two deeply interwoven activities: discovering and applying abstractions. Strong abstractions, executable behavior, tests, types, and invariants all help constrain the model and make its output more useful. The author reports success using LLMs with tools like PlantUML, since LLMs by design work best to map vocabularies.

## Code Itself as Harness and Context

The author argues that a lot of discussion on context engineering and harness engineering treats code as blackbox. Instead, a well structured code with abstractions forming a well defined vocabulary itself acts as the most important part of the harness and context. Good design frees teams to choose different LLM models without worry about prompt accuracy.

## Conclusion

As LLMs make code generation cheaper, the mechanical act of writing instructions becomes less central. What becomes more important is making the conceptual model explicit, discovering the right vocabulary, and refining that vocabulary through iteration, domain expertise, and feedback. Code is still instructions for a machine. But it is also a model of understanding. In the LLM era, that second role becomes even more important.

## Acknowledgments

The author thanks Rebecca Parsons and Martin Fowler for feedback on early drafts. Additional reviewers included Margaret Story, Max Kanat-Alexander, Premanand Chandrasekaran, Nate Schutta, Kavi Sekhon, Misma Silfver, Ricardo Piccoli, and Vinod Kumaar R. Gemini and ChatGPT were used to help refine language and assist with copy-editing.

Significant Revisions: 12 May 2026: published.

</section>
</details>

<details>
<summary>译文</summary>
<section>

# 什么是代码？

*作者：Unmesh Joshi — 2026 年 5 月 12 日 — 标签：generative AI*

## 引言

什么是代码？从宏观上看，答案似乎显而易见——代码是开发者写给机器执行的一组指令。但随着现代 LLM 的出现，我们已不必逐字敲下每一行代码来产出代码了。于是，一个更深刻的问题浮现出来：**如果"生产代码"变得廉价，代码中真正有价值的部分还剩下什么？**

## 代码的两重属性

代码一直承担着两种不同却相互交织的职能。第一，它是给机器执行的一组指令。第二，它是问题域的**概念模型**（conceptual model）。在 LLM 时代，被商品化的恰恰是前者。编码这项活动，正是这两种职能交汇的地方——开发者在此塑造概念、命名、边界与关系。

## 概念模型与词汇

让概念模型变得显式，是编码工作中更深层的一面，它由领域（domain）和用例所驱动。**词汇**（vocabulary）是指某一特定语言或学科中使用的词语集合。懂英语并不足以理解一篇软件开发文章，因为软件开发是一个宽广、成熟的领域，有自身的技术词汇。**沟通依赖于共享词汇**——无论我们是在与人、与框架，还是与 LLM 沟通，所用之词必须能映射到接收方能理解并据此行动的概念之上。

## 代码中的词汇

一个精心设计的代码库，是某种**词汇的具象表达**。软件开发横跨多个领域——一端是银行、金融、零售、库存、医疗、保险，另一端是 Web、基础设施、AI、数据工程。词汇不仅仅是标签：**它承载意义、约束与设计后果**。

针对某一领域编码，本质上是一种**翻译行为**——开发者将领域词汇映射到技术词汇之上。概念变成类型，关系变成接口，规则变成不变量（invariant），工作流变成组合（composition）。正确的抽象往往不会在一开始就显现；它只有在不断以真实世界的约束来打磨和重构代码时才浮现出来。

框架与库则是**被编码化的词汇表**（codified vocabularies）——它们捕获了常见模式，文中以 Spring Framework 为例。

## 限界上下文与本地词汇

框架在稳定、重复的结构上表现良好，但像在线零售或股票交易所这样的领域则不同。**不存在通用的高层框架**，根本原因在于：相关词汇在领域的所有实例中并不稳定。这就引出了**限界上下文**（Bounded Context）的概念——它划定了"某套词汇与模型有效"的边界。

文中肯定了 TDD 等技术有助于发现正确的命名、抽象与边界。进而连接到敏捷价值观，以及领域驱动设计（DDD）中的**统一语言**（Ubiquitous Language）——一种由开发者与领域专家共同构建、并在可工作的软件中持续检验的共享语言。

## 编程语言作为思维工具

通过代码构建词汇，需要**主动参与代码的书写与重塑**，而不仅仅是被动地审阅 LLM 生成的代码。编程语言是思维工具——Go 的 channel、Java 的面向对象模型、Rust 的所有权模型——都塑造着我们看待问题的方式。

**Java 中 Future API 的组合示例：**

```java
var future1 = action1();
future1.thenCompose(val1 -> action2(val1))
       .thenCompose(val2 -> action3(val2))
```

作者评论道：理解函数式编程的概念与词汇，对于良好地实现这个 API 至关重要；不懂这些概念，得到的将是笨拙的实现与使用方式。

**快照隔离（snapshot isolation）的伪形式规约示例：**

```
Begin(T, coord):
  R(T) := HLC(coord).now()
  writeSet(T) := {}


Read(T, N, key):
    N.HLC.tick(R(T)) //HLC 推进。任何在此之后的写或提交都有更高时间戳
    return 最新已提交版本且 ts <= R(T) 的 key


Write(T, N, key, value):
    N.HLC.tick(R(T))
    if LatestCommittedVersion(key).ts > R(T):
        abort T
    place provisional intent for (key, value)
    writeSet(T) := writeSet(T) union {key}
```

作者指出，这段伪形式化规约帮助厘清了思路，并为后续的讨论、实现和基于测试的验证提供了良好基础。

## 与 LLM 协作

LLM 在文本与代码的语料上训练而成，它学到的是**名字、API、库、框架、惯用法、设计模式与实现结构之间反复出现的关系**。如果我们的提示词使用模糊或不一致的语言，模型就只能猜测我们想要的设计。**精确、一致的、被代码所体现的词汇**，能让 LLM 更可靠地映射我们的意图。

## 认知债务

文中引入了**认知债务**（cognitive debt）一词——当团队成员在**未真正理解**的情况下使用词汇、抽象与结构时，这种债务便会累积。LLM 通过快速生成看似合理的代码，放大了这种风险。**问题不在于 LLM 生成了代码；问题在于代码引入新词汇的速度，远远超过了开发者建立理解的速度。**

## 代码作为共享概念模型

参照其先前一篇文章 *Designing Abstractions with LLMs*，作者指出：写代码包含两个深度交织的活动——**发现抽象**与**应用抽象**。强抽象、可执行行为、测试、类型、不变量，都有助于**约束模型**并使其输出更有用。作者提到在使用 PlantUML 配合 LLM 时取得过成功，因为 LLM 本质上就擅长做词汇的映射。

## 代码本身即 Harness 与上下文

作者认为，当前关于"上下文工程"（context engineering）与"harness 工程"的很多讨论，将代码当作黑箱。**事实上，一段结构良好、抽象构成清晰词汇的代码，本身就充当了 harness 与上下文的最重要部分。** 良好的设计让团队可以自由选择不同的 LLM 模型，而不必担心 prompt 准确度。

## 结论

随着 LLM 让代码生成变得更廉价，**机械地书写指令**这一行为的中心地位正在下降。变得更加重要的，是让概念模型变得显式，是发现正确的词汇，并通过迭代、领域专业知识和反馈去打磨这套词汇。**代码仍然是给机器的指令。但它同时也是一份理解模型。在 LLM 时代，第二种角色反而变得更加重要。**

## 致谢

作者感谢 Rebecca Parsons 和 Martin Fowler 对初稿的反馈。其他审阅人包括 Margaret Story、Max Kanat-Alexander、Premanand Chandrasekaran、Nate Schutta、Kavi Sekhon、Misma Silfver、Ricardo Piccoli 和 Vinod Kumaar R。文稿润色与语言优化借助了 Gemini 与 ChatGPT。

重要修订：2026 年 5 月 12 日：发布。

</section>
</details>

## 摘要

本文是 Thoughtworks 杰出工程师 Unmesh Joshi 发表于 Martin Fowler 网站的一篇纲领性短文，针对 LLM 时代"代码是否还有价值"这一尖锐问题给出回答。文章的核心论点是：**代码一直承担两种角色——给机器执行的指令 + 问题域的概念模型。LLM 时代被商品化的是前者，后者反而成为更稀缺的资产。** 围绕这一两分法，Joshi 借 DDD 的"限界上下文""统一语言"、TDD、PlantUML、Spring 等工具链，构建出一套"代码即词汇表"的论述：开发者最重要的能力是**为问题域发现并维护一套精确、共享、可被 LLM 理解的词汇**，并通过 TDD、测试套件与可执行规约持续校验它。文中还引入 Margaret-Anne Storey 的"认知债务"概念，警告 LLM 编程"扩张词汇的速度 > 团队建立理解的速度"的危险。结论颇具挑衅：**在 LLM 时代，代码就是最重要的 harness。**

## 术语表

| 术语 | 全称 | 解释 |
| :--- | :--- | :--- |
| LLM | Large Language Model（大型语言模型） | 在大规模文本与代码语料上训练的概率语言模型，是文章讨论的核心背景。 |
| Bounded Context | 限界上下文 | Eric Evans《领域驱动设计》中的核心模式，划定"某套词汇与模型有效"的边界——同一术语在不同上下文内含义不同。 |
| Ubiquitous Language | 统一语言 / 通用语言 | DDD 中的核心实践，开发者与领域专家共建一套共享语言，并在可工作的软件中持续检验。 |
| Domain-Driven Design (DDD) | 领域驱动设计 | Eric Evans 2003 年提出的方法论，强调以业务领域为软件建模的中心。 |
| Cognitive Debt | 认知债务 | Margaret-Anne Storey 在 arXiv 2603.22106 中提出的概念，指**团队共享理解的逐步侵蚀**——其论文核心机制是"AI 生成代码的速度超过团队建立理解的速度"。 |
| TDD | Test-Driven Development（测试驱动开发） | Kent Beck 推广的开发循环：先写失败测试、再写最小实现使其通过、再重构。在本文中被视为"在边界内迭代发现本地抽象"的认识论方法。 |
| Harness | （测试 / 上下文）框架 / 工具体系 | 在 LLM 工程语境中，指"包裹"模型、负责提供上下文、约束与反馈的系统或工具集。 |
| Spring Framework | Spring 框架 | Java 生态主流企业级框架。文中被 Joshi 称为"被编码化的词汇表"（非标准用法）。 |
| HLC | Hybrid Logical Clock（混合逻辑时钟） | 分布式系统中同时承载物理时钟与逻辑时钟的混合时间戳机制。文中用其说明"概念模型需要下钻到具体实现细节"。 |
| Snapshot Isolation | 快照隔离 | 数据库事务的隔离级别之一。事务开始时获取一致性快照，期间所有读都看到快照版本。 |
| PlantUML | – | 用文本描述生成 UML 图的开源工具。文中以其说明"代码即模型 / 词汇"。 |
| Functional Programming | 函数式编程（FP） | 强调不可变性、纯函数与组合性的编程范式。文中以 Java 的 `CompletableFuture.thenCompose` 为例。 |

## 深度解读

### 一、核心论点评估：清晰的两分法，但论证偏轶事

**最强洞察**：Joshi 将代码的"指令性"与"概念模型性"两分，清晰刻画了 LLM 时代软件工程中一个被长期混淆的事实——**可执行性只是代码的充分条件，**可理解性**才是它跨人、跨团队、跨模型流动的工作能力**。LLM 让两者的分离前所未有地可见：写指令已经廉价，但**让 LLM、让新成员、让未来的你**都理解代码的意图，是另一回事。

**论证的弱点**：整篇文章几乎完全建立在作者个人经验之上——Java 的 `Future.thenCompose`、snapshot isolation 伪规约、PlantUML——都是 Joshi 自己工作流中的片段。**没有一手数据**。诸如"LLM 正在把指令层商品化"被当作公理使用，但未界定程度。事实上 2026 年的 LLM 在长上下文、跨文件重构、并发正确性、类型推导上仍频繁失败，**商品化是修辞而非分析**。

最弱的一步是结尾的"**code is the most important part of the harness**"：Joshi 承认 prompt、specs、静态校验、测试都重要，随即宣称代码超越这一切。这是被自己结论说服的滑坡——见下文"亮点与盲点"。

### 二、思想谱系：高水平的旧酒新瓶

这篇文章**不是原创**，是一次高水平的**合成**。Joshi 的新增价值，是**把多支思想传统重新粘合到 LLM 语境**：

- **Peter Naur (1985)《Programming as Theory Building》**：Joshi 的"概念模型"几乎就是 Naur 所说的 **theory**——程序员共享的心智模型是项目最重要的资产，源代码只是它的次要表达。**Joshi 未引用 Naur 是明显疏漏**。
- **Fred Brooks (1975/1986)《人月神话》**：essential vs accidental complexity 是 Joshi 两分法的直系前辈。
- **Eric Evans《DDD》(2003)**：Bounded Context 与 Ubiquitous Language 撑起文章后半段的方法论骨架。
- **Kent Beck 的 TDD**：被引用为"词汇发现的迭代机制"——这是 Beck 一直坚持但常被忽视的一面：TDD 是**关于命名与边界的认识论方法**。

因此，对经历过 DDD 浪潮的资深工程师，文章是熟悉的回响；对只读过 prompt engineering 教程的初学者，它是一扇门。**瓶子对，酒也对**——只是对 DDD 老人来说，30 年前他们已经推过同一扇门。

### 三、"词汇"作为隐喻：得与失

**vocabulary 隐喻**是本文最成功的修辞，做对了两件事：

1. 把代码的**共享性**显性化（人之间、人与 LLM 之间、模块之间都需要共享词汇）。
2. 把 DDD 几十年的工作直接迁移到 LLM 工程实践，降低学习成本。

**但它至少遗漏了三层关键内容**：

- **代码是约束系统，不只是命名系统**。类型、不变量、断言、状态机在做"词汇做不到的事"——它们在**编译期或运行期强制**某种不可能性。当 LLM 写出语法正确但语义不可能的代码时，真正起拦截作用的是这些"非词汇"结构。
- **代码是运行时行为，不是文本**。词汇是静态的；FP 的代数效应、反应式架构的背压、分布式一致性边界，**词汇无法捕获**。文中的 snapshot isolation 例子正是反例，但 Joshi 没有把这一观察抽象化。
- **词汇隐喻掩盖了重命名很难**。DDD 文献反复警告：**bounded context 重构是昂贵操作**。这与"随时让 LLM 帮你换名字"的现代乐观主义正面冲突——一个 5 年积淀的领域词汇，被 LLM 改个名可能引发数周连锁修改。

**结论：词汇是必要视角，把它当充分视角是一种简化。**

### 四、LLM 相关论断的具体评估

| 主张 | 强度 | 评估 |
| :--- | :--- | :--- |
| LLM 放大认知债 (cognitive debt) | **强** | 引自 Margaret-Anne Storey 2026 年 3 月 arXiv 2603.22106（《From Technical Debt to Cognitive and Intent Debt》），学术分量足。Storey 提出 Triple Debt Model（technical / cognitive / intent），Joshi 将 cognitive debt 与 DDD vocabulary 挂钩是有创意的延伸。 |
| "代码本身是最好的 harness" | **中等偏弱** | 经验上正确（良好抽象比 prompt 工程更稳健），但缺乏比较证据。Joshi 没讨论 docs、ADRs、issue tracker、type stubs、PR descriptions 这些同样作为 harness 的载体。 |
| 精确词汇提升 LLM 输出 | **合理但属轶事** | 符合 prompt engineering 共识，无 benchmark。PlantUML 例子偏弱——它成功部分是因为 LLM 在训练数据中见过大量 PlantUML，**不是"外部 DSL 天然适合 LLM"**。 |
| "可以用任何 LLM 模型" | **过度自信** | 不同模型对同一 vocabulary 的响应差异巨大，会被事实反驳。 |

### 五、亮点与盲点

**亮点**：

- 把 DDD 本地词汇传统与 LLM 工具结合，是**真正可操作的桥梁**，比绝大多数 prompt engineering 文章站得高。
- 强调"写代码是思考的一部分"，抵抗"让 LLM 写、你 review"的懒惰分工。
- 明确把 cognitive debt 作为 LLM 时代的关键风险。
- Java `Future.thenCompose` 与 snapshot isolation 伪规约两个例子，跨抽象层次下钻得很好。

**盲点与高估**：

- **忽略非业务代码**：并发、性能、可观测性、安全、缓存一致性——这些 hard tech 领域里，vocabulary 不稀有也不困难，真正的难点在物理与硬件边界。Joshi 的论点主要在 CRUD + DDD 成立。
- **compositionality 假设过强**：词汇预设概念可像单词一样组合，但 OOP 继承、trait 约束、生命周期、副作用规则严重限制了组合的清洁度。`Future.thenCompose` 在 FP 世界自然，在多线程+异常+取消语义下立刻变得不自然。
- **没区分：个人理解 vs 团队共享**。作者把 understanding 当作团队属性，但 cognitive debt 的实际载体是**个体头脑**——Storey 论文点明了这一点，Joshi 模糊了。
- **缺少可观测信号**：如何检测 cognitive debt？没有 commit 模式、PR review 时长、bug 分布这类可观察指标，这个概念停留在感性层面。
- **没讨论 vocabulary lock-in**——一旦建立，迁移成本可能比纯代码更高。

### 六、给工程师与管理者的 3 条具体建议

1. **把 code review 改为 vocabulary review**。PR 阶段问：新引入的类型/方法，名字是否在已有 domain vocabulary 内？是否需要新词汇？如果需要，是否被业务方与团队共同命名并记录？这是把 DDD 实践**翻译为 LLM 时代动作**的最具体一步。

2. **在生成代码前,先冻结概念**。让 LLM 实现 feature 之前，先写 1–2 页：相关 bounded context、关键概念、关系、不变量、失败模式——Joshi 的 snapshot isolation 伪形式 spec 是这种做法的范例。**让 LLM 看到的不只是 prompt，还有概念骨架**；骨架本身就该进入仓库（README / ADL / wiki），直接回应 Storey 提出的 "intent debt"。

3. **警惕词汇贫乏与词汇暴涨两种病态**。前者是"util/helper/manager/service"，LLM 缺少结构可利用；后者是"AI 一周生成了 200 个新类"，认知债暴涨。**设词汇增长率**作为团队可观察指标（如每月新增 domain 类型数、公共命名空间深度），比工时/行数都更贴近"概念模型"这一真正资产。

### 真实性评估

| 声明 / 事实 | 验证状态 | 说明 |
| :--- | :--- | :--- |
| 作者 Unmesh Joshi 是 Thoughtworks 杰出工程师，位于印度浦那 | **已验证** | 与作者先前合著文章（"Conversation: LLMs and Building Abstractions"，2025-08-26）的署名一致。 |
| Unmesh Joshi 著有 *Patterns of Distributed Systems* | **已验证** | Addison-Wesley Professional 2023-11-14 出版。 |
| "What Is Code?" 发表于 Martin Fowler 网站 2026-05-12 | **已验证** | 直接抓取文章页面确认。 |
| Bounded Context 概念来自 Eric Evans 2003 年《Domain-Driven Design》 | **已验证** | Martin Fowler 自己的 bliki 文章（2014-01-15）也确认并指向 Evans 原书。 |
| Ubiquitous Language 来自 DDD，强调"在可工作的软件中持续检验" | **已验证** | 这是 Evans 2003 著作的核心定义。 |
| Spring Framework 是 "codified vocabulary"（被编码化的词汇表） | **部分验证** | Spring 确为 Java 主流企业框架；但**"codified vocabulary"是 Joshi 自创的非标准描述**，spring.io 官方将其描述为"a comprehensive programming and configuration model for modern Java-based enterprise applications"。该比喻在文章语境下可以成立，但应归于 Joshi 的解释。 |
| arXiv 2603.22106 关于 Cognitive Debt | **已验证（需注意细节）** | 论文全名："From Technical Debt to Cognitive and Intent Debt: Rethinking Software Health in the Age of AI"，作者 Margaret-Anne Storey，2026-03 提交。论文确实讨论 cognitive debt，**但其核心机制是"AI 生成代码的速度 > 团队建立理解的速度"**，而 Joshi 文中表述的"words and abstractions used without understanding"是对原文的**解释性延伸**。 |
| 之前文章 *Designing Abstractions with LLMs* | **部分验证（标题有误）** | 该文章实际标题是 "Conversation: LLMs and Building Abstractions"（2025-08-26），作者为 Unmesh Joshi 与 Martin Fowler。**Joshi 在新文章中将标题拼错或简称了**，这是一个引用瑕疵。 |
| `CompletableFuture.thenCompose` 是 Java 真实 API | **已验证** | Java SE 21 官方文档确认 `CompletionStage.thenCompose` 存在，链式调用模式正确。 |
| Thoughtworks 是 Martin Fowler 任 Chief Scientist 的全球技术公司 | **已验证** | Fowler 的 aboutMe 页面说明他 2000 年加入 Thoughtworks；公司创立于 1993 年芝加哥。 |
| **缺失引用：Peter Naur (1985) "Programming as Theory Building"** | **学术疏漏** | Joshi 的"概念模型"几乎就是 Naur 所说的"theory"，但全文未引用 Naur，是显眼的学术疏漏。 |

### 总结

Joshi 真正做对的事，是**把 Peter Naur 1985 年的"Programming as Theory Building"用 2026 年的语言重新讲了一遍，并嫁接到 DDD 与 LLM**；他没能做对的事，是**为这个老观点提供任何经验性证据，并在"code as harness"上滑向了自我应验的修辞**。对一个想从 LLM 编程中真正获益的团队，文章的真正价值不在它的结论，而在它提供的一组可执行词汇：**Bounded Context、Ubiquitous Language、Cognitive Debt、code as vocabulary**——你拿走这些词，比接受"代码就是 harness"这种口号更有用。

**关键要点：**

- **代码 = 机器指令 + 概念模型**。LLM 时代前者被商品化，后者成为更稀缺的资产。
- **词汇是 DDD × LLM 的真正桥梁**：Bounded Context + Ubiquitous Language 让团队与 LLM 共享同一套语义。
- **认知债务（cognitive debt）是 LLM 编程的最大风险**：代码词汇扩张的速度 > 团队建立理解的速度。
- **vocabulary 是必要视角，但非充分视角**——别忘了类型、不变量、运行时行为。
- **可执行动作**：把 PR 改成 vocabulary review；生成代码前先冻结概念；监控词汇增长率。
- **学术疏漏**：Joshi 未引用 Naur (1985)——这是他"概念模型"思想真正的前辈。

## 参考资料

- [What Is Code? — Unmesh Joshi (12 May 2026)](https://martinfowler.com/articles/what-is-code.html) — 解读原文。
- [Conversation: LLMs and Building Abstractions — Unmesh Joshi & Martin Fowler (26 Aug 2025)](https://martinfowler.com/articles/convo-llm-abstractions.html) — Joshi 引用为 "Designing Abstractions with LLMs" 的前作（**实际标题不同，是文中的引用瑕疵**）。
- [BoundedContext — Martin Fowler (15 Jan 2014)](https://martinfowler.com/bliki/BoundedContext.html) — Bounded Context 概念的可信出处。
- [From Technical Debt to Cognitive and Intent Debt — Margaret-Anne Storey (arXiv 2603.22106, 2026-03)](https://arxiv.org/abs/2603.22106) — Cognitive Debt 概念的学术源头。
- [Patterns of Distributed Systems — Unmesh Joshi (Addison-Wesley, 14 Nov 2023)](https://www.informit.com/store/patterns-of-distributed-systems-9780138221980) — 作者身份佐证。
- [Thoughtworks — About Us](https://thoughtworks.com/en-us/about-us) — 作者所属公司背景。
- [Martin Fowler — aboutMe](https://martinfowler.com/aboutMe.html) — Fowler 在 Thoughtworks 角色佐证。
- [Spring Framework — project page](https://spring.io/projects/spring-framework) — 验证 Spring 是 Java 框架；"codified vocabulary"是 Joshi 自创非标准描述。
- [Oracle Java SE 21 — CompletableFuture API](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/CompletableFuture.html) — 验证 `thenCompose` 是真实 API。
- *未引用但相关*：**Peter Naur (1985) "Programming as Theory Building", *Communications of the ACM*** — Joshi "概念模型" 概念的真正思想前辈。
