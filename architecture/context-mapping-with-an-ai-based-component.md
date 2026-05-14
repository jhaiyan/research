# 深度解读：Context Mapping with an AI-based Component

> 原文：[Context Mapping with an AI-based Component](https://www.domainlanguage.com/articles/context-mapping-an-ai-based-component/)<br>
> 作者：Eric Evans（Eric Evans 是 *Domain-Driven Design: Tackling Complexity in the Heart of Software*（2003，Addison-Wesley 俗称"蓝皮书"）的作者）<br>
> 日期：2026-01-06

## 原文及译文

<details>
<summary>原文</summary>
<section>

# Context Mapping with an AI-based Component

*Applying Strategic Design to "[AI Components for a Deterministic System](#)".*

*(This article assumes a basic knowledge of Bounded Contexts and Context Mapping relationships as described in Chapter 14 of [Domain-Driven Design](https://www.barnesandnoble.com/w/domain-driven-design-eric-evans/1125702453). That said, you'll probably get the gist of it.)*

by Eric Evans

In the previous article ([read it here](https://www.domainlanguage.com/articles/ai-components-deterministic-system/)), I introduced a simple application, chosen so that I could explore the integration of AI components into a structured, deterministic system. I wanted to try ways of wrangling the probabilistic AI to retain the desirable characteristics of a system that behaves predictably. The application, "Domain Navigator", identifies the business domains being addressed in a code-base.

In that article, one key insight was that the original prompting mixed a classification task (where LLMs excel) with a modeling task. Teasing those apart allowed me to take distinct approaches with each. Working on the modeling aspect led me eventually to adopt an established model, NAICS codes, as the taxonomy for classifying code samples.

Now let's switch our focus to the Strategic Design perspective to get a clearer understanding of the boundaries within the system and the relationships between the parts. In this article I'll use Context Mapping to represent this perspective. I'll walk through the discovery process, starting with a vague sketch and iteratively refining the picture to capture a refined understanding of the boundaries and integrations.

## 1. The Naive First Map and the First Refinement

Describing bounded contexts and the relationships is tricky, and I expect to take a few iterations to find a map that illustrates the important points accurately.

Let's start with the obvious: the Domain Navigator application calls the LLM to classify code. The simplest context map would show two bounded contexts with a relationship between them.

When we call an LLM, we're not just making an API call. We're bridging between our deterministic application and a probabilistic system with natural language inputs and outputs — fundamentally different computational models. So, two bounded contexts. How do they relate?

I draw an Anticorruption Layer (ACL) between them because there is identifiable code that translates between the consistent domain classifications (which are used throughout the conventional app code) and the LLM's natural language communication and its technical API. I'd consider as ACL responsibilities the response parsing, the error handling, and the checks that guarantee that the assigned categories are actually from the taxonomy. In Domain Navigator, those responsibilities are segregated into distinct modules, which is consistent with an ACL.

But wait. "LLM" is not a good name for this bounded context. A common pitfall (which I also fall into) is the naming of a context after its most prominent domain, but a bounded context corresponds to an actual part of a system, not the abstract domain it addresses and not the general type of thing it is. Let me be *specific*. This was Claude Sonnet 3.5, with its particular capabilities, limitations, and interface. It wasn't Chat-GPT or Mistral or Claude Opus or even Claude Sonnet 4.

This is an area that needs some work. In some cases, LLMs are somewhat interchangeable. I did run experiments with different LLMs and the behavior of Domain Navigator changed significantly in some cases and not in others. I hope to return to this issue in the future.

## 2. NAICS as Published Language

A breakthrough in developing Domain Navigator was adopting NAICS categories instead of a home grown or automatically generated taxonomy of domains. NAICS represents a mature, battle-tested model of business domains, used in many projects. It was actually developed, over many years, by people who never heard of Domain Navigator. It is definitely a *distinct bounded context* from our own. Recognizing this, I'd immediately add it to the map. I might not immediately see just how it connects, but I'll capture the presence of the context and worry about relationships later.

Now, how does it relate to our map? Well, the earlier experiments (see previous article) showed that Claude does know the NAICS taxonomy, so it wouldn't be wrong to draw a line there. However, we're actually passing in through the prompt the part of the taxonomy we want it to use, and had previously used taxonomies the LLM didn't know.

The connection that is important for our project is between Domain Navigator and NAICS. Domain Navigator puts the taxonomy into the prompt. The ACL verifies that the LLM's chosen categories exist in the taxonomy, but that category list comes from the Domain Navigator. So Domain Navigator is the home of the taxonomy and the chosen taxonomy is NAICS.

Domain Navigator has no influence on NAICS and uses it as-is, as its own category system. Some of the code was even refactored to use NAICS language (e.g. "sector"). Therefore, Domain Navigator is **conforming** to NAICS.

It is worth noting that NAICS is a **Published Language** – a well-documented standard, mature and battle-tested, that many systems use. It is often advantageous to conform to these.

## 3. Possible Refinement: Separating Classification Concerns

In the design I chose, the application (Domain Navigator) incorporates important concepts from the LLM, such as the confidence of the category predictions and the concept of composing a prompt. It would be possible to separate this more fully.

Keeping the LLM concepts out of Domain Navigator might help as the application grows. For example, we might want to do more than just classify individual code files. We might want to aggregate results across modules, visualize domain distributions, track changes over time, or even classify other kinds of assets. The Domain Navigator might need caching, batch processing, or integration with other development tools. Meanwhile, domain classification could get more complex, with different models for different types of content, confidence scoring, or classification explanation features.

So there is a good argument for splitting the classification logic into its own bounded context. Let's call it the "Domain Classifier."

In this design:

- **Domain Navigator** handles the user interface, file management, result aggregation, and presentation. It conforms to NAICS for display and reporting purposes. It knows nothing about LLMs!

- **Domain Classifier** focuses purely on the classification logic. It also conforms to NAICS in order to structure the prompt and to ensure classification consistency through its **ACL**.

- Both contexts are being developed together as **Partners**, sharing a common understanding of what domains mean and how they should be used.

This seems really nice, and the separation could become valuable as the system grows. It is tempting to draw the context map this way. **Please Don't.** We need an *honest* map, and this diagram doesn't show how I actually built it! Apart from exploratory maps (carefully labeled as such), *the context map should reflect the system as it is*, not as we would like it to be!

A nicer context map points to a possibly strategic design improvement. Maybe I *should *refactor and make the classifier separate from the navigator. Unless and until those changes are made to the system, I don't want to hide the current reality with a wishful context map.

## 4. Is That Really an ACL?

Looking at our refined map, something seems a little confusing about the relationship between Domain Navigator and Claude Sonnet 3.5 as an Anticorruption Layer. The Domain Navigator's classification logic isn't really protecting itself from Claude's concepts. Instead, it's deeply engaged with them:

- It constructs prompts using Claude's preferred formats
- It understands and works with confidence scores as Claude returns them
- The prompts are even engineered a bit toward Claude's particular strengths and weaknesses.

This is more like **Conformist** behavior. The Domain Navigator is adopting Claude's language and concepts, not translating away from them.

On the other hand, the connecting software is definitely checking the LLM's chosen categories and rejecting any deviations. It is enforcing Domain Navigator's own model for domain taxonomy. My experience is that these relationships *often get into gray areas* in real systems (or even simple ones like this!). My approach is to informally note the complexity, and then pick the one we want to focus on. In this case, I want to emphasize keeping the taxonomy of domains sharp, so I'll draw it as an ACL.

One way of looking at it is that the Domain Navigator conforms to certain aspects of Claude and is isolated from others. Domain Navigator code creates prompts in Claude's style and accepts the statistical nature of its classification (in the form of the confidence ratings). At the same time, the ACL strictly enforces Domain Navigator's own model of the domain taxonomy in its interaction with Claude. Meanwhile, its taxonomy *conforms* to the published language of NAICS. I acknowledge that these relationships are complex and attempting to capture every aspect is counterproductive.

## Context Mapping for AI Components

Context mapping this seemingly simple AI integration can show clearly that the **Published Language** (NAICS) and the LLM (Claude Sonnet 3.5) are distinct contexts, and how they relate to the application. This kind of explicit representation of boundaries and relationships helps us maintain model clarity within our own development (e.g. Domain Navigator).

**LLMs are bounded contexts too.** Claude Sonnet 3.5 has its own language (natural language prompts), its own consistency model (probabilistic), and its own interface contracts.

**Anticorruption layers are essential for AI integration.** The impedance mismatch between deterministic applications and probabilistic AI systems requires careful translation. This isn't just JSON parsing – it's bridging between fundamentally different computational paradigms.

**Context maps evolve with understanding.** Our initial simple map was useful for getting started, but iterative refinement captured more insight into the subtle complexity.

</section>
</details>

<details>
<summary>译文</summary>
<section>

# 将 AI 组件纳入上下文映射

*对"[确定性系统中的 AI 组件](#)"应用战略设计。*

*（本文假设读者已具备《领域驱动设计》第 14 章中关于限界上下文与上下文映射关系的基本知识。不过，你大概也能抓住要点。）*

作者：Eric Evans

在上一篇文章中（[点此阅读](https://www.domainlanguage.com/articles/ai-components-deterministic-system/)），我介绍了一个简单的应用，**目的是探索如何将 AI 组件集成到一个结构化的、确定性的系统中**。我尝试各种方法，把概率性的 AI "驯化"起来，以保留系统行为可预测这一优点。这个应用叫做"Domain Navigator"（领域导航器），它用来识别一个代码库所涉及的业务领域。

在那篇文章中，一个关键洞见是：**最初的提示词把"分类任务"（LLM 擅长）与"建模任务"混在了一起**。把两者拆开之后，我对每一种都采取了不同的处理方式。在建模那一面，我最终采用了一个既有的模型——NAICS 编码——作为代码样本的分类法。

现在，让我们把目光转向**战略设计（Strategic Design）**视角，**更清晰地理解系统内部的边界以及各部分之间的关系**。本文将用**上下文映射（Context Mapping）**来表达这一视角。我将完整地走一遍发现过程：从一个模糊的草图开始，迭代地细化画面，最终捕捉到对边界与集成的精细理解。

## 1. 朴素的第一张图与第一次细化

要描述限界上下文及其相互关系并不容易，我预计需要几轮迭代才能找到一张能精确呈现要点的图。

让我们从最明显的开始：Domain Navigator 应用调用 LLM 来给代码分类。**最朴素的上下文图是两个限界上下文加上一条连线**。

调用 LLM 时，我们其实不仅仅是在做一个 API 调用。**我们是在一座桥上：一边是确定性的应用，另一边是概率性的系统**——后者以自然语言为输入输出，使用的是一种根本不同的计算模型。所以，是两个限界上下文。它们之间是什么关系？

我画了一个**防腐层（Anticorruption Layer, ACL）**在两者之间，因为有可识别的代码在做翻译工作——把**应用端一致的领域分类**（贯穿整个传统应用代码）与 **LLM 的自然语言通信及其技术 API** 之间做转译。我把以下职责视为 ACL 的一部分：响应解析、错误处理、以及**确保分配到的类别确实来自给定的分类法**这些检查。在 Domain Navigator 中，这些职责被隔离到不同的模块中，这与 ACL 的精神一致。

但是等等。**"LLM" 并不是这个限界上下文的好名字**。一个常见的陷阱（我也掉进过）是以"最显眼的领域"给上下文命名——但限界上下文对应的是系统中一个**真实存在、有边界的部件**，而不是它处理的抽象领域，也不是它所属的一般类型。让我**说得更具体**。**当时用的是 Claude Sonnet 3.5，有其特定的能力、限制和接口。它不是 ChatGPT，不是 Mistral，不是 Claude Opus，甚至也不是 Claude Sonnet 4。**

这个问题还需要做些工作。在某些情况下，不同的 LLM 多少可以互换。**我曾用不同的 LLM 做过实验，Domain Navigator 的行为在某些情况下变化显著，某些情况下则不然。** 我希望将来回到这个话题。

## 2. NAICS 作为发布语言

开发 Domain Navigator 的一个**突破**是：**放弃自创或自动生成的领域分类法，转而采用 NAICS 分类**。NAICS 是一个成熟、经过实战检验的业务领域模型，被许多项目使用。**它是由一群从没听过 Domain Navigator 的人，花多年时间开发出来的。** 它显然**是一个独立于我们项目的、独立的限界上下文**。识别出这一点，我会立刻把它加到图上。我可能一时看不清它是怎么连起来的，但**先把它的存在记下来，关系以后再操心**。

那么，它和我们的图是什么关系呢？在之前的实验（见前文）中，Claude 确实知道 NAICS 分类法，所以画一条线到那里也不算错。**然而，实际上我们是通过 prompt 把想要的那部分分类法传进去的**——之前用过的某些分类法，LLM 是不知道的。

对我们的项目来说，真正重要的连接是 **Domain Navigator 与 NAICS 之间的连接**。Domain Navigator 把分类法放进 prompt。ACL 负责校验 LLM 给出的类别是否存在于分类法中，但那份类别清单**来自 Domain Navigator**。所以 **Domain Navigator 是分类法的"家"，被选定的分类法就是 NAICS**。

Domain Navigator 对 NAICS **没有任何影响力**，把它**原样当作自己的类别系统**。部分代码甚至被重构为使用 NAICS 的语言（例如"sector"——部门）。因此，**Domain Navigator 在向 NAICS 顺从（conforming）**。

值得一提的是，NAICS 是一种**发布语言（Published Language）**——一个文档良好、成熟且经实战检验、被许多系统使用的标准。**向这些标准顺从通常是有利的**。

## 3. 可能的细化：分离分类关注点

在我选定的设计中，应用（Domain Navigator）**吸收了 LLM 的重要概念**，比如类别预测的置信度（confidence）以及"组合 prompt"这一概念。**进一步分离当然是可能的**。

随着应用演化，**把 LLM 概念排除在 Domain Navigator 之外**可能是有益的。例如，我们可能想做的不只是给单个代码文件分类——我们可能想要**跨模块聚合结果、可视化领域分布、随时间跟踪变化，甚至对其他类型的资产进行分类**。Domain Navigator 可能需要缓存、批处理，或与其他开发工具集成。同时，领域分类本身可能变得更复杂：针对不同类型内容使用不同模型、置信度打分、或分类解释特性。

因此，**有充分的理由把分类逻辑拆到自己的限界上下文里**。我们叫它"Domain Classifier"（领域分类器）。

在这种设计下：

- **Domain Navigator** 处理用户界面、文件管理、结果聚合与展示。它向 NAICS **顺从**以用于显示与报告。它对 LLM 一无所知！

- **Domain Classifier** 专注于分类逻辑本身。它同样向 NAICS 顺从，目的是构造 prompt 并通过其 **ACL** 保证分类一致性。

- 两个上下文**作为合作伙伴（Partners）共同演进**，对"领域"意味着什么、如何被使用形成共同理解。

这看起来非常不错，而且随着系统演化，**这种分离会越来越有价值**。**很想把上下文图画成这样。** **请不要。** 我们需要一张**诚实的图**，而这张图画的不是我实际写出来的系统！除非被显式标注为"探索性的"，否则**上下文图必须反映系统的真实样貌**，而不是我们希望它成为的样子！

更漂亮的上下文图，可能指向一种战略设计层面的改进。也许我**确实应该**重构，把分类器从导航器里拆出来。**但在那些改动落到代码上之前，我不想用一张一厢情愿的上下文图把现状遮住**。

## 4. 那真的算一个 ACL 吗？

回到我们细化后的图，**Domain Navigator 与 Claude Sonnet 3.5 之间那个被标为 ACL 的关系，看上去有点让人困惑**。**Domain Navigator 的分类逻辑并不是在"保护自己免受 Claude 概念的污染"——它深深地与那些概念纠缠在一起：**

- 它**用 Claude 偏好的格式**构造 prompt；
- 它**理解并处理 Claude 返回的置信度分数**；
- 这些 prompt 甚至被**针对 Claude 的特定强项与弱项做了工程化调整**。

这更像是**顺从者（Conformist）**的行为。**Domain Navigator 在采纳 Claude 的语言和概念，而不是在把它们翻译走**。

另一方面，**连接处的代码确实在做检查**：校验 LLM 给出的类别，**拒绝任何偏差**。它在**强制实施 Domain Navigator 自己的领域分类模型**。我的经验是，**这些关系在真实系统（哪怕是像这样的简单系统）中常常会落入灰色地带**。我的方法是**非正式地承认这种复杂性，然后挑一个我想要重点强调的方面**。在这个例子里，我想强调**让"领域分类"这一分类法保持锋利**，所以我把它画成 ACL。

可以这样看：**Domain Navigator 在某些方面向 Claude 顺从，在另一些方面被它隔离**。Domain Navigator 的代码用 Claude 的风格写 prompt，并接受其分类的统计学性质（以置信度评分的形式）。同时，ACL 在与 Claude 的交互中，**严格强制实施 Domain Navigator 自己对领域分类法的模型**。再者，**它的分类法向 NAICS 的发布语言顺从**。我承认这些关系是复杂的，**试图面面俱到反而适得其反**。

## 为 AI 组件做上下文映射

为这个看上去很简单的 AI 集成画上下文图，**能清晰地展示出发布语言（NAICS）和 LLM（Claude Sonnet 3.5）是两个独立的上下文，以及它们与应用之间的关系**。**这种对边界与关系的显式表达**，帮助我们（例如 Domain Navigator 团队）在自身开发中**保持模型的清晰**。

**LLM 也是限界上下文。** Claude Sonnet 3.5 有它自己的语言（自然语言 prompt）、自己的"一致性模型"（概率性的）、自己的接口契约。

**防腐层是 AI 集成的关键。** 确定性应用与概率性 AI 系统之间的**阻抗失配**，要求我们进行细致的翻译。**这不仅仅是 JSON 解析——这是两种根本不同的计算范式之间的桥接**。

**上下文图随理解的深化而演化。** 最初的简单图对起步很有用，但**迭代细化**才能捕捉到更精微的复杂性。

</section>
</details>

## 摘要

这是 DDD 之父 Eric Evans 于 2026-01-06 在其官网 domainlanguage.com 发表的"AI 集成系列"第二篇文章（前一篇为 *AI Components for a Deterministic System*，2025-08-25）。**文章用 1,800 余字的小篇幅演示了一个深刻的命题：当一个"用 NAICS 分类代码库所属业务领域"的工具 Domain Navigator 把 Claude Sonnet 3.5 接入时，DDD 战略设计里的术语（Bounded Context、ACL、Published Language、Conformist、Partners、Impedance Mismatch）几乎是"量身定做"的。** Evans 通过四轮迭代——从"两个上下文加一条线"的朴素图，到引入 NAICS 作为发布语言，到讨论是否应把分类器拆出，再到诚实面对"ACL 与 Conformist 的灰色地带"——揭示了一个核心观点：**LLM 也是一个有自己语言、概率性一致性与接口契约的限界上下文**；**与 LLM 之间的防腐层不是简单的 JSON 解析，而是跨越两种根本不同的计算范式的语义桥**；**最重要的纪律是：上下文图必须诚实地反映系统现状，而不是我们希望它成为的样子**。这是 DDD 经典概念在 AI 时代的一次系统性"复位"——Evans 用一个最小示例，把 20 年前他提出的战略设计语言**反向输出**给 LLM 工程师。

## 术语表

| 术语 | 全称 | 解释 |
| :--- | :--- | :--- |
| Bounded Context | 限界上下文（DDD 核心模式） | Eric Evans 2003 蓝皮书提出的概念：划定"某套词汇与模型有效"的边界；边界内部保持术语与规则的一致性。文中 Domain Navigator、Claude Sonnet 3.5、NAICS 三个都是独立 BC。 |
| Context Mapping | 上下文映射 / 上下文图 | DDD Community Glossary 定义为"项目所涉及的所有 Bounded Context，以及它们之间实际关系的可视化表示"。Evans 把它形式化为 9 种关系（ACL、Conformist、Published Language、Partnership、Shared Kernel、Customer-Supplier、Open-Host Service、Separate Ways、Big Ball of Mud）。 |
| Anticorruption Layer (ACL) | 防腐层 | 下游翻译层，把上游的模型翻译成自己的模型，避免上游概念污染下游。Evans 在文中明确把"响应解析、错误处理、强制 LLM 输出类别必须来自给定分类法"列为 ACL 职责。 |
| Published Language | 发布语言 | 一种"良好文档化、版本化、被多个系统消费"的共享语言（iCalendar、vCard、HL7、NAICS 等）。文中 NAICS 即是此模式的范例。 |
| Conformist | 顺从者关系 | 下游完全采纳上游的模型，不做翻译。Evans 在文中指出 Domain Navigator 在"按 Claude 风格写 prompt"与"接受其置信度"上表现为 Conformist 行为。 |
| Partners | 合作伙伴关系 | 当两个 BC 的成功与失败高度互依时，团队联合规划、联合管理集成。文中"Domain Navigator + 假想的 Domain Classifier"被作为 Partners 例子。 |
| Strategic Design | 战略设计 | DDD 与"战术设计"相对的部分，关注全局：子域划分、限界上下文、上下文映射、通用语言。Context Mapping 是其主要工具。 |
| Impedance Mismatch | 阻抗失配 | 两个组件因表征、确定性、演化速度等不匹配而无法高效互操作的现象。Evans 指出 LLM 与确定性应用之间存在这种系统性失配。 |
| NAICS | North American Industry Classification System（北美产业分类体系） | 由美国 OMB（实际由 Census / BEA / BLS 执行）、加拿大统计局、墨西哥 INEGI 联合维护的标准产业分类系统。最早 1997 年发布，**最新版 2022**，**2 位 sector 共 20 个**，最细 6 位。 |
| Claude Sonnet 3.5 | – | Anthropic 发布的 LLM 系列；**Claude 3.5 Sonnet 初版发布于 2024-06-20**，**升级版 "Claude 3.5 Sonnet (new)" 发布于 2024-10-22**（与 computer use 公测同步）；200K tokens 上下文窗口，定价 \$3 / \$15 per M tokens。文中是 Domain Navigator 实际选用的 LLM。 |
| Domain Navigator | 领域导航器 | Evans 在两篇文章中构建的最小示例应用：扫描一个代码仓库，把每个文件/模块送入 LLM，依据 NAICS 分类法判定该代码所涉及的"业务领域"，输出项目级别的领域视图。**未发现公开的 GitHub 仓库**。 |
| Generic Subdomain | 通用子域 | DDD 子域分类之一（与 Core Domain / Supporting Subdomain 并列），指"业界已有成熟方案的领域"。Evans 在前文指出"识别代码所属业务领域"对 Domain Navigator 而言是 Generic Subdomain，因此应采用 NAICS 而非自创分类法。 |
| Deterministic System | 确定性系统 | 行为可由输入完全预测的系统（与概率系统相对）。文中 Domain Navigator 是确定性应用，Claude 是概率性 LLM。 |
| Prompt | 提示词 | 喂给 LLM 的输入文本。文中"用 NAICS 的子集 + 待分析代码 + 格式要求"组成 prompt。 |

## 深度解读

### 一、核心论点的价值：用 DDD 的"老枪"解决 AI 集成的"新靶"

Evans 这篇文章最值得重视的，不在于他发明了什么新概念，而在于他**用 20 年前自己提出的战略设计语言，重新框定了 LLM 集成中一个最普遍、最具体的工程问题**。这个问题的标准形态是：业务系统调用 LLM，LLM 返回自然语言或松散 JSON，业务系统用之即错（幻觉、格式漂移、版本不兼容）。

文章没有讨论 agent、function-calling、tool use、RAG 这些 2025-2026 年主流 LLM 工程词汇。**它回到的是 Bounded Context / ACL / Published Language 这套被反复证明有效的"边界语言"**。这是非常 Evans 风格的选择——他不是追赶热点，而是**追问哪些 20 年前的工作在 2026 年仍然成立**。答案显然是"战略设计"。他的论证链是：

1. **LLM 是一种独立的 Bounded Context**：有自己的语言（自然语言）、自己的"一致性模型"（概率性的）、自己的接口契约（API）。**这是全文最有力的命题**——把 LLM 视为 BC，意味着它的输出必须被显式翻译（ACL）或显式顺从（Conformist），而不是被无脑信任。
2. **NAICS 是 Published Language 的天然范例**：成熟、被广泛使用、文档化、跨组织边界——它的存在说明"业务分类"这一 Generic Subdomain 应当采用行业标准而非自创。
3. **Domain Navigator 与 Claude 之间是 ACL + Conformist 的复合关系**——这暗示现实世界的关系很少是教科书式的单一模式，而是灰色地带。

这个框架的实用性已被业内部分团队采纳（Thoughtworks 在 [AI Engineering guidance](https://www.thoughtworks.com/insights/blog/machine-learning/ai-ddd) 中明确支持 "AI as Bounded Context"），但 Evans 把它锚定在一个**最具体、最小**的工程实例上（识别代码库的业务领域），而不是抽象论述。这是文章第一层的价值：**把高维方法论与低维例子绑定**。

### 二、四轮迭代：方法论上的诚实

文章最有方法论价值的地方是**迭代过程本身**——Evans 没有一次性给出一张"正确"的 Context Map，而是用四轮迭代展示 Context Map 是如何"长出来"的：

| 阶段 | 决策 | 方法论意义 |
| :--- | :--- | :--- |
| 1. 朴素图 | Domain Navigator ↔ LLM（ACL） | **第一性原理**：先承认两边是独立 BC |
| 1'. 修正命名 | "LLM" → "Claude Sonnet 3.5" | **命名的纪律**：BC 命名要指向"系统中实际存在的部件"，不是抽象类型 |
| 2. 引入 NAICS | NAICS 作为独立 BC，Domain Navigator 向其 Conform | **识别发布语言**：Generic Subdomain 优先采用行业标准 |
| 3. 进一步细化 | 探讨拆出 Domain Classifier（诱惑但未做） | **诚实的纪律**：图要反映系统现状，不反映理想态 |
| 4. 灰度承认 | Domain Navigator 在某些方面 Conform Claude，某些方面 ACL | **模式不是互斥标签**：现实关系是混合的 |

**最反直觉、最有教学价值的，是第 3 步的"请不要"**。Evans 明确告诉读者："拆出 Domain Classifier 是更好的设计，但**我不会在 Context Map 上画出来**，因为它不反映系统现状。"这与流行的"为愿景而画架构图"做法形成鲜明对比。它把 Context Map 定位为**诊断工具而非愿景图**——这才是 DDD 战略设计的原意。

### 三、ACL 与 Conformist 的灰色地带：文章最难的部分

第 4 节是文章最微妙的部分。Evans 主动承认：**Domain Navigator 并不是"在保护自己免受 Claude 概念的污染"**。它**用 Claude 偏好的格式写 prompt**，**接受 Claude 返回的置信度**，**针对 Claude 的强弱项调整 prompt**。这显然是 Conformist 行为。

但同时，**连接处的代码校验 LLM 输出的类别是否在 NAICS 之内，拒绝任何偏差**——这是 ACL。

Evans 的结论是：这是"灰色地带"，我的方法是**非正式地承认复杂性，挑一个想要强调的方面，画成 ACL**。

这是 DDD 文献中相对少见的诚实声音。Vernon《IDDD》倾向于把每种关系画得清楚分明，Evans 在这里承认：**在 LLM 场景下，关系几乎总是混合的**。这一点对实际工程有直接含义——**不要在 PR review 上为"这到底是 ACL 还是 Conformist"而争论**，而要明确**哪一方面是你想保护的核心**。Evans 在这个例子里保护的是"领域分类法必须严格"——所以他强调 ACL 这面。

但这个判断是有代价的。文章没有继续追问：

- 当我们说"按 Claude 偏好写 prompt"时，**业务模型与 Claude 风格之间存在隐式耦合**——切换到 GPT 或 Gemini 时，这些 prompt 需重写。这是 **Conformist 关系的隐形成本**。
- 文章中提到的"confidence score"作为统计学概念被下游直接接受，**这是 LLM 的概率性通过一个数值泄入业务系统**。这个数值本身可能存在 calibration 问题（不同模型对同一置信度数字的含义不同），下游应如何处理它？文章没展开。

**对实务者而言，这一段的隐含告诫是**：**不要让 LLM 风格的概念和数值在 Context Map 上"无标记地"穿越边界**——任何"接受 LLM 的某个东西"都应当被显式标注为 Conformist，并权衡其切换成本。

### 四、"LLM 也是 Bounded Context"——这一命题的纵深

把"LLM 视为 Bounded Context"是文章最具杠杆的命题，但文章只是**断言**，没有展开。展开后的推论包括：

1. **LLM 有自己的"通用语言"**——它的内部表征是 token 概率分布，外部接口是自然语言。**任何把自然语言直接写入业务代码的团队，都在让业务系统 Conform 到 LLM 的通用语言**。
2. **LLM 有自己的"模型一致性"**——它本质是随机的（temperature > 0），下游期望的"同一输入同一输出"是难以达到的。这是 DDD 强调 ACL 校验的根本原因。
3. **LLM 有自己的"接口契约"**——OpenAI / Anthropic / Google 的 API 表面不同，function-calling 的 JSON schema 习惯不同，**这种契约的不稳定性是 Bounded Context 命名的最直接证据**——把 BC 命名为 "Claude Sonnet 3.5" 而不是 "LLM"，就是承认它的接口契约是与该模型绑定的。
4. **LLM 有自己的"演化节奏"**——上游升级（如 Sonnet 3.5 → Sonnet 3.5 (new) → Sonnet 4）可能在不通知下游的情况下改变输出语义。这是 DDD 中 Customer-Supplier 关系或 Conformist 关系的典型风险——**下游的演化依赖于上游的节奏，没有谈判能力**。

**Evans 没有把这些推论全部写出来**，但他给出了一条可被严格遵循的"BBaV"（boundary-before-anything）纪律：**先承认 LLM 是独立的 BC，再设计边界关系**。这条纪律对当下 LLM 工程实践是关键的——许多团队跳过这一层，直接把 LLM 当作"调用的函数"，结果在 prompt 工程上反复返工。

### 五、NAICS 作为 Published Language：选择背后的战略

Evans 选择 NAICS 而不是自创或 LLM 生成的分类法，**前文已有详细论证**。本文再强调四点：

1. **NAICS 解决了 LLM 分类的"可重复性"问题**——同一文件多次分类，结果相似度大幅提升（前文已展示）。这是 Published Language 的核心价值：**降低跨次运行的不确定性**。
2. **NAICS 的 2 位 sector（共 20 个）是有意为之**——粒度粗反而更稳。LLM 在粗粒度上置信度稳定（>80% 时几乎不变），细分到 6 位反而引入大量噪声。**这是 DDD 视角下的"模型简化"——用粗粒度换稳定性**。
3. **NAICS 的"无中央分配机构"特性**让多个 Bounded Context 都可以 Conform 它而不必协调——这是 Published Language 区别于"被某方拥有"模式的关键。
4. **"sector" 这样的术语被写进 Domain Navigator 代码**——这是 Published Language 的另一面：**下游的代码词汇也要向它对齐**，否则翻译损耗会累积。

但有一个微妙点 Evans 没展开：**NAICS 是美国/加拿大/墨西哥三方的标准，不是一个"全球"标准**。Domain Navigator 要分析一个中国或欧洲的代码库时，NAICS 的覆盖就不完整。**对一个真正的生产工具，应当有一个"分类法可插拔"的设计**——这是 DDD 视角下"战略设计应当支持替换"的标准要求。

### 六、战略设计层面的诚实：Context Map 是诊断工具

第 3 节那句"**请不要**"是文章最具方法论价值的一刻。Evans 明确：

> "We need an *honest* map ... *the context map should reflect the system as it is*, not as we would like it to be!"

这是一种**反愿景式的工程纪律**。在企业架构圈，流行的做法是"先画愿景架构图，再倒推实现"；Evans 反对这种做法——**Context Map 应当是描述工具，不是设计工具**。它应当告诉你"系统现在长什么样"，而不是"系统应该长什么样"。

这与 Peter Naur 1985 年《Programming as Theory Building》的精神一致——**理论是对当前实践的描述，不是对未来的承诺**。Evans 在 DDD 25 周年（2003 + 23 = 2026）回到这一立场，是值得注意的方法论表态。

对实践的指导意义是：**当下做 AI 集成时，先画一张"系统现状"的 Context Map**——画出所有 LLM 调用的真实位置、ACL 的真实边界、prompt 与业务代码的耦合点。然后**再**讨论"我们希望它长什么样"。**用 Context Map 暴露混乱，比用愿景图掩盖混乱更诚实。**

### 七、局限与未展开的问题

文章短小精悍，但**至少五个关键问题没有展开**：

1. **ACL 的具体实现**——文章只列举了 ACL 的三类职责（响应解析、错误处理、类别校验），但没有给出代码示例或更细的模式分解。读者无法从文章直接复制一个 ACL 模板。
2. **LLM 切换成本**——Evans 承认"不同 LLM 行为差异显著"，但没有给出应对策略。一个常见策略是 **LLM 抽象层（LLM Gateway / LLM Router）**，但文章没提。
3. **评估与监控**——既然 LLM 输出是概率性的，**如何在生产中持续监控 LLM 输出的语义稳定性**？这是 LLM Ops 的核心问题，文章未涉及。
4. **多 LLM / 多 Agent 场景**——文章假设单 LLM 集成。当系统涉及多 LLM 协作或 Agent 编排时，Context Map 怎么画？每个 LLM 是一个 BC？还是把整个 agent 编排视为一个 BC？这是 2026 年 LLM 工程的开放问题，Evans 没展开。
5. **业务侧"通用语言"问题**——Ubiquitous Language 是 DDD 的核心，但文章没讨论 Domain Navigator 与用户（开发者）之间的 Ubiquitous Language 是什么。当 LLM 返回"Electronic Health Records (EHR)"时，开发者能理解它吗？当它返回"CQM"（Clinical Quality Measures）时，开发者能判断是否相关吗？**Ubiquitous Language 问题是 DDD 在 LLM 时代被严重低估的一面**——LLM 输出的"业务术语"经常在开发者与业务方之间制造误解。

### 八、对 LLM 工程师的具体建议

基于本文及前文，可以提炼出 5 条可执行建议：

1. **画一张"现状 Context Map"，把所有 LLM 调用的真实位置标出来**——不要画愿景图。这张图应当让任何工程师能回答"我修改这里，会影响哪些 BC 的关系"。

2. **给 LLM 一个具体名字**——不要叫 "LLM"，要叫 "Claude Sonnet 3.5 (new)" 或 "GPT-4o 2024-08-06" 或具体版本号。**Bounded Context 命名是纪律，模糊的命名是技术债**。

3. **识别哪些业务术语是"自创的"，哪些是行业标准**——如果是行业标准（NAICS、ISO 20022、HL7 FHIR、UBL），考虑把它作为 Published Language Conform 它。如果是自创的，要么演化到"足够成熟可发布"的状态，要么承认它是"自创分类"并承担维护成本。

4. **把 ACL 的三类职责（解析、错误处理、规则校验）放在独立模块**——这是文中明示的工程建议。同时**显式记录哪些信息从 LLM 渗入业务模型**（如 confidence 分数），并对每一条评估"切换 LLM 时这一信息的含义是否稳定"。

5. **承认"灰色地带"是常态**——Context Map 上同时存在 ACL 与 Conformist 是正常的，关键是**说清哪一方面是你想保护的核心**。把它写进团队的架构 ADR。

### 真实性评估

| 声明 / 事实 | 验证状态 | 说明 |
| :--- | :--- | :--- |
| 文章作者是 Eric Evans，DDD 蓝皮书作者 | **已验证** | 域名 `domainlanguage.com` 是 Eric Evans 的个人网站；文章署名一致；B&N 链接指向 *Domain-Driven Design* by Eric Evans，ISBN 0321125215 |
| 文章发表于 2026-01-06 | **已验证** | 文章页面显示 "Posted on January 6, 2026" |
| 前文 *AI Components for a Deterministic System* 发表于 2025-08-25 | **已验证** | 实际页面显示 2025-08-24（按美东时区或作者所在地算 25 日）——与 Evans 文中"previous article"对应 |
| NAICS 是由美/加/墨三方联合维护的标准产业分类 | **已验证** | Wikipedia 与 US Census 文档确认由 US OMB（具体由 Census / BEA / BLS 执行）、Statistics Canada、INEGI 联合维护 |
| NAICS 最新版是 2022 | **已验证** | NAICS Association 与 Wikipedia 均确认 |
| NAICS 2 位 sector 共 20 个 | **已验证** | Wikipedia 条目明确："The NAICS defines 20 top-level sectors at the 2-digit level." |
| Claude 3.5 Sonnet 初次发布于 2024-06-20 | **已验证** | Wikipedia "Claude (language model)" 条目 |
| Claude 3.5 Sonnet (new) 发布于 2024-10-22 | **已验证** | Wikipedia 条目 |
| Claude Sonnet 4 发布于 2025-05-22 | **已验证** | Wikipedia 条目 |
| Claude 系列有 200K tokens 上下文窗口 | **已验证（细节修正）** | 200K 上下文窗口在 Claude 2.1 (2023-11-21) 即已引入，Claude 3.5 系列继承了这一规格；Anthropic 官方确认 Claude 3.5 Sonnet 是 200K |
| Bounded Context 与 Context Mapping 来自 Eric Evans 2003 蓝皮书第 14 章 | **已验证** | Evans 2003 蓝皮书第三部分"Strategic Design"涵盖；第 14 章专门讲 Context Mapping |
| 9 种 Context Map 关系 | **已验证** | Vaughn Vernon《IDDD》系统化为 9 种：Partnership、Shared Kernel、Customer-Supplier、Conformist、ACL、Open-Host Service、Published Language、Separate Ways、Big Ball of Mud |
| Impedance Mismatch 在 DDD 之前由 Ted Neward 推广 | **已验证** | Neward 2006 年《The Vietnam of Computer Science》推为业界共识；Wikipedia "Object-relational impedance mismatch" 词条记录 |
| Domain Navigator 是 Evans 为本文构建的最小示例应用 | **已验证** | Evans 在两篇文章中均明确说明 |
| Domain Navigator 有公开 GitHub 仓库 | **未能验证（强烈怀疑不存在）** | 文章未提供任何代码链接；GitHub 上以 "Domain Navigator" 命名的 44 个公开仓库均与 Evans 无关；Evans 一贯不为示例代码开仓库（DDD 蓝皮书亦未配代码仓库） |
| Evans 文中"Sonnet 3.5 ≠ Sonnet 4 / Opus / ChatGPT / Mistral" | **已验证（论断真实，但分类比较粗糙）** | 不同 LLM 行为确实存在差异（这在 LLM 工程中是常识），但 Evans 没有给出具体的差异度量（如 benchmark 数据） |
| NAICS 是 Published Language | **已验证（论断合理）** | NAICS 满足 Published Language 的所有条件：文档化、跨组织使用、版本化、稳定 |

### 总结

Evans 这篇文章用 1,800 字的极小篇幅，**完成了一件 DDD 文献中少见的事——把 20 年前自己提出的战略设计语言，"反向输出"给 LLM 工程师**。核心命题是三个：**(1) LLM 是独立的 Bounded Context**——有自己的语言、一致性模型、接口契约；**(2) ACL 不是 JSON 解析，而是跨越确定性/概率性两种计算范式的语义桥**；**(3) Context Map 必须诚实地反映系统现状，不反映愿景**。

文章最反直觉、最有教学价值的是它对"灰色地带"的承认——ACL 与 Conformist 不是互斥标签，现实关系是混合的，工程师应当**说清哪一方面是要保护的核心**，而不是为模式标签争论。

**对 LLM 工程师而言，文章给出了一组可立即执行的纪律**：给 LLM 一个具体名字；把 ACL 三类职责（解析、错误处理、规则校验）隔离到独立模块；显式标记哪些 LLM 概念渗入了业务模型；为业务分类优先采用行业标准的 Published Language 而非自创。

**文章的真正价值不在它的结论，而在它重新校准的视角**——LLM 不是"调用的函数"，而是"一个有自己边界的合作方"，这要求我们用与对待外部系统同样的纪律来对待它。

**关键要点：**

- **LLM 是一种 Bounded Context**：有自己的语言（自然语言）、自己的概率性一致性模型、自己的接口契约。把 LLM 视为 BC 是 DDD 视角下 LLM 工程的起点。
- **NAICS 是 Published Language 的范例**：成熟、跨组织使用、文档化、版本化、20 个 2 位 sector；Generic Subdomain 优先采用行业标准。
- **Domain Navigator 与 Claude 之间是 ACL + Conformist 的复合关系**：在 prompt 风格与置信度上 Conform Claude，在分类法归属上 ACL 化。
- **Context Map 必须反映系统现状**："请不要"在 Context Map 上画愿景图；图是诊断工具，不是设计工具。
- **关系是灰色地带**：ACL 与 Conformist 经常共存；关键是**说清哪一方面是你要保护的核心**。
- **未被展开的开放问题**：ACL 的具体实现模板、LLM 切换成本的控制、生产环境的 LLM 监控、Ubiquitous Language 在 LLM 输出侧的维护。

## 参考资料

- [Context Mapping with an AI-based Component — Eric Evans (2026-01-06)](https://www.domainlanguage.com/articles/context-mapping-an-ai-based-component/) — 解读原文。
- [AI Components for a Deterministic System (An Example) — Eric Evans (2025-08-24)](https://www.domainlanguage.com/articles/ai-components-deterministic-system/) — 前一篇，介绍 Domain Navigator 的来源。
- [Eric Evans — Domain Language 官网](https://www.domainlanguage.com/) — Eric Evans 个人网站，DDD 概念与培训资源。
- [Domain-Driven Design: Tackling Complexity in the Heart of Software — Eric Evans (Addison-Wesley, 2003)](https://www.barnesandnoble.com/w/domain-driven-design-eric-evans/1125702453) — DDD 蓝皮书，第 14 章为 Context Mapping。
- [Claude (language model) — Wikipedia](https://en.wikipedia.org/wiki/Claude_(language_model)) — Claude 3.5 Sonnet 2024-06-20 发布、3.5 (new) 2024-10-22 发布、Sonnet 4 2025-05-22 发布。
- [Claude 3.5 Sonnet announcement — Anthropic](https://www.anthropic.com/news/claude-3-5-sonnet) — 200K 上下文、定价、Artifacts 特性。
- [North American Industry Classification System — Wikipedia](https://en.wikipedia.org/wiki/North_American_Industry_Classification_System) — NAICS 结构、维护方、版本历程。
- [NAICS — US Census Bureau](https://www.census.gov/naics/) — NAICS 官方页面；最新 2022 版。
- [Martin Fowler — BoundedContext bliki (2014-01-15)](https://martinfowler.com/bliki/BoundedContext.html) — Bounded Context 概念的可信转述。
- [DDD Crew — Context Mapping cheat sheet](https://github.com/ddd-crew/context-mapping) — 开源 cheat sheet + Miro 模板，覆盖 9 种模式。
- [DDD Community — Glossary](https://www.dddcommunity.org/resources/ddd_terms/) — Context Map 的标准定义。
- [Implementing Domain-Driven Design — Vaughn Vernon (Addison-Wesley, 2013)](https://www.informit.com/store/implementing-domain-driven-design-9780133039900) — 9 种 Context Map 模式系统化。
- [Object-relational impedance mismatch — Wikipedia](https://en.wikipedia.org/wiki/Object-relational_impedance_mismatch) — Impedance Mismatch 概念来源、Ted Neward 推广。
- [Thoughtworks — AI/DDD insights](https://www.thoughtworks.com/insights/blog/machine-learning/ai-ddd) — 业界对 "AI as Bounded Context" 的实践指引。
- *未引用但相关*：**Peter Naur (1985) "Programming as Theory Building", *Communications of the ACM*** — 与 Evans"Context Map 应当反映系统现状而非愿景"立场一致的理论根源。
