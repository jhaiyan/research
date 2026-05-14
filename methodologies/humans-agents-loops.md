# 深度解读：Humans and Agents in Software Engineering Loops（人与智能体：软件工程中的循环）

> 原文：[Humans and Agents in Software Engineering Loops](https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html)<br>
> 作者：Kief Morris（Thoughtworks）<br>
> 日期：2026-03-04

---

## 原文及译文

<details>
<summary>原文（English）</summary>
<section>

# Humans and Agents in Software Engineering Loops

**Author:** Kief Morris
**Date:** 04 March 2026

*This article is part of "Exploring Gen AI" — a series capturing Thoughtworks technologists' explorations of using gen ai technology for software development.*

---

Should humans stay out of the software development process and vibe code, or do we need developers in the loop inspecting every line of code? I believe the answer is to focus on the goal of turning ideas into outcomes. The right place for us humans is to build and manage the working loop rather than either leaving the agents to it or micromanaging what they produce. Let's call this "on the loop."

## The Why and How Loops

As software creators we build an outcome by turning our ideas into working software and iterating as we learn and evolve our ideas. This is the "why loop." Until the AI uprising comes humans will run this loop because we're the ones who want what it produces.

The process of building the software is the "how loop." The how loop involves creating、selecting、and using intermediate artefacts like code、tests、tools、and infrastructure. It may also involve documentation like technical designs and ADRs. We're used to seeing many of these as deliverables, but intermediate artefacts are really just a means to an end.

*Figure 1: The why loop iterates over ideas and software, the how loop iterates on building the software.*

In reality the how loop contains multiple loops. The outermost how loop specifies and delivers the working software for the why loop. The innermost loop generates and tests code. Loops in between break down higher levels of work into smaller tasks for the lower loops to implement, then validate the results.

*Figure 2: The how loop has multiple levels of inner loops that work on smaller increments of the full implementation.*

These loops may follow practices like design reviews and test stages. They might build systems by applying architectural approaches and design patterns like microservices or CUPID. Like the intermediate artefacts that pop out of these practices and patterns, they are all a means of achieving the outcome we actually care about.

But maybe we don't care about the means that are used to achieve our goals? Maybe we can just let the LLMs run the how loop however they like?

## Humans Outside the Loop

Plenty of people have discovered the joy of letting humans stick to the why loop, and leaving the how loop for the agents to deal with. This is the common definition of "vibe coding". Some interpretations of Spec Driven Development (SDD) are much the same, with humans investing effort in writing the outcome we want, but not dictating how the LLM should achieve it.

*Figure 3: Human runs the why loop, agent runs the how loop.*

The appeal of humans staying out of the how loop is that the why loop is the one we really care about. Software development is a messy domain that inevitably bogs down into over-engineered processes and coping with technical debt. And every new LLM model so far has gotten better at taking a user prompt and spitting out working software. If you're not satisfied with what it spits out, tell the LLM and it'll give you another iteration.

If the LLMs can write and change code without us, do we care whether the code is "clean"? It doesn't matter whether a variable name clearly expresses its purpose as long as an LLM can figure it out. Maybe we don't even need to care what language the software is written in?

We care about external quality, not internal quality for its own sake. External quality is what we experience as a user or other stakeholder of the software. Functional quality is a must, the system needs to work correctly. And for production software we also care about non-functional, operational quality. Our system shouldn't crash, it should run quickly, and we don't want it posting confidential data to social media sites. We don't want to run up massive cloud hosting bills, and in many domains we need to pass compliance audits.

We care about internal quality when it affects external outcomes. When human coders were crawling through the codebase, adding features and fixing bugs, they could do it more quickly and reliably in a clean codebase. But LLMs don't care about developer experience, do they?

In theory our LLM agents can extrude a massively overcomplicated spaghetti codebase, test and fix it by running ad-hoc shell commands, and eventually produce a correct, compliant, high-performing system. We just get our swarms Ralph Wiggumming on it, running in data centers that draw energy from the boiling oceans they float on, and eventually we'll get there. [1]

In practice, a cleanly-designed, well-structured codebase has externally important benefits over a messy codebase. When LLMs can more quickly understand and modify the code they work faster and spiral less. We do care about the time and cost of building the systems we need.

## Humans in the Loop

Some developers believe that the only way to maintain internal quality is to stay closely involved in the lowest levels of the how loop. Often, when an agent spirals over some broken bit of code a human developer can understand and fix it in seconds. Human experience and judgement still exceeds LLMs in many situations.

*Figure 4: Human runs the why loop and the how loop.*

When people talk about "humans in the loop", they often mean humans as a gatekeeper within the innermost loop where code is generated, such as manually inspecting each line of code created by an LLM.

The challenge when we insist on being too closely involved in the process is that we become a bottleneck. Agents can generate code faster than humans can manually inspect it. Reports on developer productivity with AI show mixed results, which may be at least partly because of humans spending more time specifying and reviewing code than they save by getting LLMs to generate it.

We need to adopt classic "shift left" thinking. Once upon a time we wrote all of our code, passed it to a QA team to test, and then tried to fix enough bugs to ship a release. Then we discovered that when developers write and run tests as we work we find and fix issues right away, which makes the whole process faster and more reliable.

What works for humans can work for agents as well. Agents produce better code when they can gauge the quality of the code they produce themselves rather than relying on us to check it for them. We need to instruct them on what we're looking for, and give them guidance on the best ways to achieve it.

## Humans on the Loop

Rather than personally inspecting what the agents produce, we can make them better at producing it. The collection of specifications, quality checks, and workflow guidance that control different levels of loops inside the how loop is the agent's harness. The emerging practice of building and maintaining these harnesses, Harness Engineering, is how humans work on the loop.

*Figure 5: Human defines the how loop and the agent runs it.*

Something like the on the loop concept has also been described as the "middle loop," including by participants of The Future of Software Development Retreat. The middle loop refers to moving human attention to a higher-level loop than the coding loop.

> "The difference between in the loop and on the loop is most visible in what we do when we're not satisfied with what the agent produces"

The "in the loop" way is to fix the artefact, whether by directly editing it, or by telling the agent to make the correction we want. The "on the loop" way is to change the harness that produced the artefact so it produces the results we want.

We continuously improve the quality of the outcomes we get by continuously improving the harness. And then we can take it to another level.

## The Agentic Flywheel

The next level is humans directing agents to manage and improve the harness rather than doing it by hand.

*Figure 6: Human directs agent to build and improve the how loop.*

We build the flywheel by giving the agents the information they need to evaluate the performance of the loop. A good starting point is the tests and evaluations already included in the harness. The flywheel becomes more powerful as we feed it richer signals. Add pipeline stages that measure performance and validate failure scenarios. Feed operational data from production, user journey logs, and commercial results to broaden the scope and depth of what the agents can analyze.

For each step of the workflow we have the agent review the results and recommend improvements to the harness. The scope includes improvements to any of the upstream parts of the workflow that could improve those results. What we have now is an agent harness that generates recommendations for improving itself.

We start by considering the recommendations interactively, prompting the agents to implement specific changes. We can also have the agents add their recommendations to the product backlog, so we can prioritize and schedule them for the agents to pick up, apply, and test as part of the automated flow.

As we gain confidence, the agents can assign scores to their recommendations, including the risks, costs, and benefits. We might then decide that recommendations with certain scores should be automatically approved and applied.

> "At some point this might look a lot like humans out of the loop, old-school vibe coding."

I suspect that will be true for standard types of work that are done often as the improvement loops reach diminishing returns. But by engineering the harness we won't just get one-off, "good enough" solutions, we'll get robust, maybe even anti-fragile systems that continuously improve themselves.

---

**Notes:**

[1] These days "ralph loop" is often used colloquially to mean just firing up a bunch of agents and leaving them to keep looping until (hopefully) they finish their task. But as originally described the operator plays an important role in steering agents as they ralph.

</section>
</details>

<details>
<summary>译文（中文）</summary>
<section>

# 人与智能体：软件工程中的循环

**作者：** Kief Morris
**日期：** 2026 年 3 月 4 日

*本文是「探索生成式 AI」系列的一部分——该系列记录了 Thoughtworks 技术人员对将生成式 AI 应用于软件开发的探索。*

---

人类到底应该彻底退出软件开发流程、靠"氛围编程"（vibe coding）放手让 AI 干，还是必须留在循环（in the loop）里逐行审查 AI 写的每一行代码？本文的答案是：把目光聚焦在"把想法变成结果"这个目标上。人类最恰当的位置，是构建并管理工作循环本身——既不能把一切丢给智能体（agent），也不能对它们的产出事无巨细地微观管理。我们把这种角色称为"在循环之上"（on the loop）。

## 目标循环（why loop）与手段循环（how loop）

作为软件的创造者，我们通过把想法转化为可工作的软件来构建结果，并随着认知的演进而迭代——这就是"目标循环"。在 AI 接管一切之前，**这个循环必须由人类来运行**，因为我们才是那个真正"想要"产出的人。

"如何把软件做出来"的过程就是"手段循环"。它涉及代码、测试、工具、基础设施等中间产物的创建、选择与使用；也包括技术设计与架构决策记录（ADR）等文档。我们过去习惯把这些中间产物视为可交付成果，但说到底，它们只是达成最终目标的手段。

*图 1：目标循环在"想法"和"软件"之间迭代；手段循环在"如何构建软件"上迭代。*

现实中，手段循环内部嵌套着多个子循环。最外层为"目标循环"规约并交付可工作的软件；最内层是代码的生成与测试；中间的循环则把上层工作拆解成下层可执行的小任务，然后验证其结果。

*图 2：手段循环内部有多层嵌套子循环，逐层处理越来越小的实现单元。*

这些子循环会遵循设计评审、阶段性测试等实践；也会借助微服务、CUPID 等架构方法与设计模式。和从这些实践与模式中冒出来的中间产物一样，它们都只是通往我们真正在意的那个结果的手段。

但话说回来——我们真的不在乎达成目标所用的手段吗？真的可以完全放手让 LLM 想怎么跑就怎么跑吗？

## 人类退到循环之外

已经有很多人体验到了"人类只跑目标循环、让智能体处理手段循环"的快感——这就是"氛围编程"（vibe coding）的常见定义。规范驱动开发（Spec Driven Development, SDD）的某些解读也类似：人类投入精力写清楚自己想要的结果，但不规定 LLM 该如何实现。

*图 3：人类运行目标循环，智能体运行手段循环。*

这种"人类退出手段循环"的吸引力在于：我们真正在意的是目标循环。软件开发本就是一个混乱的领域，总会被过度工程的流程和技术债拖垮。而每一代新的 LLM 模型都在变得更强——你给它一个用户提示，它就能吐出能跑的软件。不满意？告诉它，它就给你下一个版本。

如果 LLM 可以替我们写代码、改代码，我们还需要在乎代码"干不干净"吗？只要 LLM 能看懂，变量名是否清楚地表达其意图，似乎也没那么重要了。甚至我们可能都不必关心软件是用什么语言写的。

我们关心的是外部质量，而非内部质量本身。外部质量是我们作为用户或利益相关方能感知到的：功能正确性是底线，系统必须正确工作；对生产级软件而言，我们还关心非功能性的运维质量——系统不能崩、要跑得快，不能把机密数据发到社交媒体上，不能产生天价云账单，在很多领域还必须通过合规审计。

我们之所以也关心内部质量，是因为它最终会反映在外部结果上。过去人类开发者穿行在代码库里、加功能、修 bug 时，整洁的代码库能让他们加得更快、改得更稳。但 LLM 又不 care 开发者体验，对吧？

理论上，LLM 智能体完全可以吐出一坨巨复杂的"意大利面"代码库，跑一通临时拼凑的 shell 命令测一测、修一修，最终交付一个正确、合规、高性能的系统。我们只需要"放出一群 Ralph Wiggum 上去"——在漂浮在被煮沸的海洋上的数据中心里永不停歇地跑——总能跑出来。[1]

但实际上，整洁、结构良好的代码库相对混乱的代码库有显著的外部收益。当 LLM 能更快地理解与修改代码时，它跑得更快，也更少陷入"螺旋下坠"。我们仍然在乎构建系统所需的时间与成本。

## 人类留在循环之内

一些开发者认为，要维持内部质量，唯一的办法是深度介入手段循环的最底层。当智能体在某段坏掉的代码上"螺旋"打转时，人类开发者往往几秒钟就能看懂并修好。人类的经验与判断力在很多场景下仍然胜过 LLM。

*图 4：人类同时运行目标循环和手段循环。*

当人们谈论"humans in the loop"时，他们通常指人类作为最内层循环（代码生成）的一道关卡——比如逐行审阅 LLM 写的代码。

但当我们坚持深度介入时，自身就成了瓶颈。智能体生成代码的速度远超人类逐行审阅的速度。关于"AI 提升开发者生产力"的报告呈现出喜忧参半的结果，部分原因很可能就是：人类花在"写规格 + 审代码"上的时间，反而比让 LLM 生成代码所省下的时间还多。

我们需要采用经典的"左移"（shift left）思维。过去我们写完全部代码后丢给 QA 团队测试，再在发版前疯狂修 bug。后来我们发现，开发者边写边测，问题能立刻被发现并修掉，整个过程变得更快、更可靠。

对人类有效的方法，对智能体同样有效。智能体能自己评估产出代码的质量时，往往能写出更好的代码——而不是依赖我们去替它检查。我们需要告诉它我们在意什么，并引导它用最佳方式达成。

## 人类站在循环之上

与其亲自去审智能体的产出，不如让智能体更擅长产出。**掌控手段循环各层级的规格、质量检查、工作流指引的集合，就是智能体的"工具链"（harness）。** 构建并维护这些工具链的实践——即新兴的"Harness Engineering"——就是人类"在循环之上"工作的方式。

*图 5：人类定义手段循环，智能体运行手段循环。*

类似"on the loop"的概念，也被一些同行称为"中循环"（middle loop），"软件开发的未来"研讨会（The Future of Software Development Retreat）的与会者就使用过这一说法。中循环指的是：把人类的注意力从编码循环提升到一个更高层级的循环。

> "in the loop 与 on the loop 的差别，最明显地体现在——当我们不满意智能体产出时，我们会做什么。"

**"in the loop"的方式**是修补产物本身——要么直接编辑，要么告诉智能体做你想要的修正。**"on the loop"的方式**则是去改造产出该产物的"工具链"，让它下次产出你想要的结果。

我们通过持续改进工具链来持续提升产出的质量。然后我们还可以更进一步。

## 智能体飞轮

下一层级是：让人类指挥智能体去管理和改进工具链本身，而不是亲自动手。

*图 6：人类指挥智能体构建并改进手段循环。*

我们构建飞轮的方式是：给智能体提供评估循环表现所需的信号。一个很好的起点是工具链里已有的测试和评估。随着我们喂入更丰富的信号，飞轮会越来越强——加入衡量性能、验证失败场景的流水线阶段；把生产环境的运营数据、用户旅程日志、商业结果都喂进去，从而拓宽智能体能分析的广度与深度。

针对工作流的每一步，我们让智能体回顾结果并给出对工具链的改进建议。范围可以延伸到上游任何能改进结果的部分。到这一步，我们拥有的是一个会"自己给自己提改进建议"的智能体工具链。

一开始，我们交互式地审视这些建议，并指挥智能体去实现具体的修改。也可以让智能体把建议塞进产品待办列表里，便于我们排期，让智能体在自动化流程里领取、实现、测试。

随着信心增强，智能体可以给自己的建议打分——风险、成本、收益都包含在内。然后我们可以决定：分数达到一定阈值的建议，可以被自动批准并执行。

> "到了某个节点，这看起来就很像人类彻底退出循环、回到老派的氛围编程。"

我推测这对于那些经常做的标准化工作是成立的——当改进循环触及收益递减的拐点时就是。但通过工程化地构建工具链，我们得到的不是一次性"差不多就行"的方案，而是稳健的、甚至可能是**反脆弱的**（anti-fragile）系统——它们能持续自我改进。

---

**注释：**

[1] 如今 "ralph loop" 在坊间常被用来指代"放出一堆智能体让它们循环到（希望）完成任务"的玩法。但 Ralph 最初被描述时，操作者其实在引导智能体的方向上扮演着关键角色。

</section>
</details>

---

## 摘要

本文由 Thoughtworks 的 Kief Morris 撰写，发表于 Martin Fowler 网站的「探索生成式 AI」系列。文章针对当下 Gen AI 编码智能体浪潮中一个核心组织问题：**人类在软件开发循环中应该处于什么位置？** 作者用"目标循环"（why loop，即把想法变成业务结果）与"手段循环"（how loop，即把软件做出来的过程）的二分法作为骨架，并借用控制论（cybernetics）的层级反馈循环视角，把"完全放手 vibe coding"与"逐行审 in the loop"两种极端都判为次优解；进而提出"在循环之上"（on the loop）——人类应站在更高的层级去设计与维护智能体的"工具链"（harness）。最后，文章把视角推演到"智能体飞轮"：让智能体自己推荐并实施对工具链的改进，使整个系统逼近 Taleb 意义上的"反脆弱"。

## 术语表

| 术语 | 全称 | 解释 |
| :--- | :--- | :--- |
| Gen AI | Generative AI（生成式人工智能） | 泛指能生成文本、代码、图像等内容的大模型，文中特指用于软件开发的 LLM 智能体。 |
| LLM | Large Language Model（大语言模型） | 通过海量文本预训练、具备自然语言与代码生成能力的基础模型，是当代编码智能体的内核。 |
| Vibe coding | 氛围编程 / 凭感觉编程 | 由 Andrej Karpathy 于 2025 年 2 月提出的概念：完全凭自然语言提示让 LLM 生成代码、接受结果、不再 review。Simon Willison 进一步收窄定义："用 LLM 写软件但不审它写的代码"。 |
| SDD | Spec-Driven Development（规范驱动开发） | 以可执行规范为主产物、由 AI 智能体直接生成实现的开发方法（如 GitHub 的 `spec-kit`）；与 vibe coding 形成对照。 |
| Why loop | 目标循环 | 在"想法 ↔ 软件"之间迭代的高层循环，由人类驱动，关注业务价值。 |
| How loop | 手段循环 | "如何把软件做出来"的循环，由代码生成、测试、工具、基础设施等子循环嵌套组成。 |
| In the loop | 循环之内 | 人类在代码生成的最内层把关——逐行审阅、逐处纠错，常因速度跟不上而成为瓶颈。 |
| On the loop | 循环之上 | 人类不直接审产物，而是设计、维护"工具链"（harness）让智能体自我约束与改进。 |
| Middle loop | 中循环 | 团队级别的迭代循环（PR 评审、CI、集成、交付），在"个人内循环"与"产品生命周期外循环"之间。文中意指人类应把注意力从"逐行编码"上移到这一层。 |
| Ralph loop | Ralph 循环 | Geoffrey Huntley 于 2025 年 7 月提出的智能体编码模式：`while :; do cat PROMPT.md \| claude-code; done`，让智能体在 shell 循环中持续推进。名字取自《辛普森一家》的 Ralph Wiggum——"在不确定的世界中确定性地笨"。 |
| Harness | 智能体工具链 / 壳 | 包裹在模型外部的所有引导与反馈机制：规格、prompt、AGENTS.md、测试、检查器、CI 步骤等。LangChain 的经典公式：**Agent = Model + Harness**。 |
| Harness Engineering | 工具链工程 | Thoughtworks 的 Birgitta Böckeler 在相邻文章中提出的新兴实践——把编码智能体的"外壳"作为工程对象来设计与维护。文中是 on-the-loop 工作的具体形态。 |
| Shift left | 左移 | 由 Larry Smith 于 2001 年在 *Dr. Dobb's Journal* 提出的测试理念：把质量活动从流程后端前移到开发早期。文中类比：与其事后审，不如让智能体尽早自我评估。 |
| ADR | Architecture Decision Records（架构决策记录） | Michael Nygard 于 2011 年推广的轻量文档形式，记录一条架构决策的上下文、理由、备选与后果。 |
| CUPID | Composable, Unix philosophy, Predictable, Idiomatic, Domain-based | Dan North 于 2022 年提出的"愉悦编码"五属性，被视为对 SOLID 的另一种视角——不强调规则，而强调"好代码长什么样"。 |
| Flywheel | 飞轮 | 借用 Jim Collins 的商业概念：随着每一次改进，系统的自我强化能力进一步加速——此处指工具链的递归自我改进。 |
| Anti-fragile | 反脆弱 | Nassim Taleb 在 2012 年同名书中提出的概念：能从波动、压力、错误中**获益**的系统，超越"robust/resilient"。 |
| Vibe coding 与 SDD 的关系 | 范式光谱 | 文章把它们放在同一光谱上：vibe coding 是"几乎不约束如何做"，SDD 是"在规范层严约束、但仍不限制实现手段"，两者都不要求人类深入编码细节。 |

## 深度解读

### 一、核心论点：跳出"in vs. out"二元对立，提出"on the loop"

文章最大的洞察不在于某个具体技巧，而在于它**重新定义人类在 AI 时代的位置**。过去半年业界最常见的争论是："人类到底要不要审 AI 写的代码？"——这一争论默认了"人类 ↔ 智能体"之间只有两个角色：要么放手（vibe coding），要么逐字逐句把关（in the loop）。

Morris 的反对意见是：**这种二元提问本身就是错的**。如果把软件开发看成一个控制论意义上的反馈系统（cybernetic feedback system），那么人类最有效的介入点不是"循环内"也不是"循环外"，而是**循环之上**——设计循环本身。这就是"on the loop"概念的精髓：**人类从"做循环里的工作"升级到"做让循环变好的工作"**。

这是从体力劳动到管理劳动、再到设计劳动的层级跃迁，对应 Don Reinertsen 产品开发流理论中的"层级抽象"思想。

### 二、"目标—手段"二分法：一种重要的概念解耦

文章最精炼的术语贡献是 **why loop / how loop** 的二分：

- **目标循环**：业务想法 → 业务结果。**必须**由人类运行，因为只有人类知道自己"想要什么"。
- **手段循环**：从规约到代码的工程过程。可以也应该越来越多地交给智能体。

这一解耦的价值在于：它把"AI 是否会取代程序员"这种无谓的争论，**翻译**成"人类应该把哪些层级的决策拿在自己手里"——一个真正可操作的工程问题。

注意这里隐含的"手段独立性"思想：手段循环内部的目标（代码可工作、可测试、可维护）相对于 why loop 的目标（业务价值）是**派生**的。这呼应了 Dan North 的 CUPID、Simon Brown 的 C4 等"代码即手段"的思想——但 Morris 把它系统化了。

### 三、内在与外部质量的实用主义区分

文章在反驳"反正 LLM 看得懂，代码丑点无所谓"时引入了**外部质量** vs **内部质量**的区分，并给出了一个反直觉但务实的论断：

> 内部质量之所以重要，**不是因为代码本身美**，而是因为它影响外部结果（速度、成本、可靠性）。

这一论证路径绕过了"代码美学"的抽象之争，直接用经济与运营语言重新包装了整洁代码的价值——这对在管理层面前为工程实践辩护的人来说，是一个很有用的论据。

### 四、关键论证：智能体不能完全自给自足，但人类也不能逐行审

文章最锋利的一段是关于 "in the loop" 的反诘：

> 当人类坚持深度介入最内层时，**自己就成了瓶颈**。智能体生成代码的速度远超人类逐行审阅的速度。

并引用了 AI 生产力研究的"喜忧参半"现状——这指向 METR 在 2025 年发表的随机对照研究：开源开发者使用 AI 工具在自家代码库上的实际速度**反而慢了约 19%**。后续的 2026 年 5 月 METR 自我报告调查（349 名技术工作者）则显示 1.4–2x 提升，但报告本身也强调了对幅度的怀疑。

**这一矛盾正是文章整个论点的实证基础**：盲目的 vibe coding 不灵，逐行审 in the loop 也不灵；那么剩下的就是"on the loop"——让智能体带着更聪明的工具链去自管理。

### 五、"反脆弱"的飞轮愿景：AI 时代的"持续改进"

文章最后一节引入"智能体飞轮"——一个递归自改进的系统：

```
测试/评估结果 → 智能体分析 → 推荐工具链改进 → 人类审批 → 智能体实施 → 新一轮循环
```

当飞轮转得足够多时，**整个系统会逼近 Taleb 意义上的"反脆弱"**：不只是 robust（抗住冲击）或 resilient（受冲击后恢复），而是**从冲击中变强**——每一次 prompt 失败、每一次产出偏差、每一次工具链修改，都让系统更了解自己。

这一愿景与 Thoughtworks 同事 Birgitta Böckeler 在姊妹文章《Harness Engineering for Coding Agents》中提出的 **"内/外 harness × 引导/感知"** 框架高度互补——Morris 给出"控制论循环"的心智模型，Böckeler 给出可落地的工程实现。

### 六、与 Thoughtworks 思想谱系的连贯性

本文并非孤立之作，而是 Thoughtworks 思想谱系中的一环：

- **Harness Engineering**（Böckeler）：把"工具链"作为工程对象来设计——内/外 harness、guides vs. sensors、确定性 vs. 推断性。
- **On / In / Out of the Loop**（Morris，本文）：给"工具链工程"赋予控制论的语义框架。
- **The Future of Software Development Retreat**（Fowler 主持的闭门研讨）：on-the-loop / middle-loop 概念的发源地。
- **Role of Developer Skills**（Fowler 系列）：从"技能清单"到"循环层级中的人类角色"的视角转换。

理解这一谱系，读者才能看到文章的真正价值——**它是一个更大思想运动的环节**，而非独立观点。

### 七、批判性反思：哪些论断是真正的洞察，哪些是修辞？

- **真正具有洞察的**：
  - "on the loop" 的层级跃迁思想；
  - "why loop / how loop" 的解耦——把争论从"是否取代程序员"重塑为"循环层级设计问题"；
  - 用外部质量而非内部美学为"代码整洁"正名。

- **具有修辞色彩但需谨慎对待的**：
  - "智能体飞轮 → 反脆弱"——是一个激动人心的愿景，但在工程实践中仍处早期；自动批准并应用高分数建议的设想，需要严格的安全与回滚机制。
  - "Ralpha Wiggum 漂浮在被煮沸的海洋上的数据中心"——生动的修辞，但暗含的隐喻（"能耗换取产出"）对环境成本轻描淡写。
  - "out of the loop 就是回到 vibe coding"——把"自动化"与"放手"画等号有些跳跃；中间仍有"人类监督下的智能体自治"这一中间地带。

### 八、现实意义与读者启示

对不同角色的启示：

- **架构师 / 平台工程师**：on the loop 的主要承担者——投资构建 harness 是新的高价值工程活动。
- **工程经理**：把"代码 review 量"从团队 KPI 中移走，改为"工具链质量 + 智能体产出与目标的对齐度"。
- **个体开发者**：把个人技能成长方向从"写更多代码"调整到"设计更好的循环与工具"——这才是 AI 时代不可被替代的差异化能力。
- **组织**：把"氛围编程实验"和"严苛逐行审"都视为次优解，配置资源到"工具链工程"团队。

### 真实性评估

| 声明 / 事实 | 验证状态 | 说明 |
| :--- | :--- | :--- |
| Vibe coding 由 Andrej Karpathy 于 2025 年 2 月提出 | 已验证 | 多个独立来源确认 |
| Ralph loop 由 Geoffrey Huntley 于 2025 年 7 月提出 | 已验证 | 见 ghuntley.com 原帖 |
| CUPID 由 Dan North 于 2022 年提出（5 个属性） | 已验证 | 见 dannorth.net 原帖 |
| "Shift left" 由 Larry Smith 于 2001 年在 *Dr. Dobb's Journal* 提出 | 已验证 | 维基百科与原始引用 |
| ADR 由 Michael Nygard 于 2011 年推广 | 已验证 | 业内公认 |
| "Anti-fragile" 来自 Taleb 2012 年同名书 | 已验证 | 维基百科与原书 |
| Kief Morris 是 Thoughtworks 成员 | 已验证（推断） | 他是 Thoughtworks 策划的「探索生成式 AI」系列的客座作者；O'Reilly *Infrastructure as Code* 作者 |
| Harness Engineering 是 Thoughtworks 的新兴实践（Böckeler） | 已验证 | 见 martinfowler.com 上的姊妹文章 |
| "Future of Software Development Retreat" 与 "middle loop" 概念 | 部分验证 | 概念在多篇姊妹文章中出现，但 Retreat 的公开一手资料未能直接获取 |
| AI 提升开发者生产力"喜忧参半" | 已验证 | METR 2025 年 RCT 显示反而慢 19%；METR 2026 年 5 月自报调查显示 1.4–2x 提升，但作者自承对幅度存疑 |
| Spec Driven Development（SDD）作为 vibe coding 的对照解读 | 已验证 | GitHub spec-kit 等工具的实践一致 |

## 总结

这篇文章看似在讨论一个工程组织问题（"人该站哪"），实质上**重新框定了 AI 时代软件工程的元问题**：不再是"AI 会不会取代程序员"，而是"人类该设计什么样的循环让 AI 智能体产生业务价值"。

它真正的贡献是把控制论（cybernetics）的层级反馈思想引入 Gen AI 编码讨论：**人类是循环的设计者与改进者，智能体是循环的运行单元**。这与姊妹文章《Harness Engineering》构成"理论 + 实践"的一对，共同构成 Thoughtworks 在 AI 时代软件工程方法论上的核心主张。

对读者的最大启示是：**与其争论"AI 写的代码要不要逐行审"，不如把精力投到"AI 工作的循环该如何设计"**——这是更高杠杆的工程活动，也是 AI 时代人类最不可被替代的角色。

**关键要点：**

- **重新框定问题**：不要纠结 in vs. out of the loop——人类最有效的位置是 on the loop，即设计并改进工作循环本身。
- **解耦目标与手段**：why loop（业务结果）必须由人类运行；how loop（实现过程）可以越来越多地由智能体运行。
- **以工具链工程为新主战场**：Harness Engineering 是 on-the-loop 工作的具体形态，是 AI 时代工程实践的新高地。
- **用"飞轮"思维取代"一次性产出"**：持续改进工具链、持续测量、持续优化，使系统逼近反脆弱。
- **警惕两端极端**：vibe coding 与逐行审都不如"设计更好的循环"——METR 等研究已经给出实证。

## 参考资料

- [Geoffrey Huntley — "Ralph Wiggum as a 'software engineer'"](https://ghuntley.com/ralph/) — Ralph loop 概念的最早权威阐述。
- [Dan North — "CUPID — for joyful coding"](https://dannorth.net/2022/02/10/cupid-for-joyful-coding/) — CUPID 五个属性的原始定义。
- [Birgitta Böckeler — "Harness Engineering for Coding Agents" (martinfowler.com)](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html) — 本文姊妹篇，给"工具链工程"提供工程化框架。
- [GitHub spec-kit](https://github.com/github/spec-kit) — SDD 实践的代表性开源工具。
- [Wikipedia — Vibe Coding](https://en.wikipedia.org/wiki/Vibe_coding) — Vibe coding 概念溯源。
- [Simon Willison — "Not all AI-assisted programming is vibe coding"](https://simonwillison.net/2025/Mar/19/vibe-coding/) — 对 vibe coding 的窄定义澄清。
- [Wikipedia — Shift-left testing](https://en.wikipedia.org/wiki/Shift-left_testing) — "左移"概念溯源（Larry Smith, 2001）。
- [Wikipedia — Antifragility](https://en.wikipedia.org/wiki/Antifragility) — Taleb 反脆弱概念。
- [METR — Measuring the Impact of AI on Developer Productivity](https://metr.org/) — AI 提升开发者生产力"喜忧参半"的实证依据。
- [Kief Morris — 个人站点](https://kief.com/) — 作者背景与 *Infrastructure as Code*。
- [Martin Fowler — Exploring Gen AI 系列索引](https://martinfowler.com/articles/exploring-gen-ai.html) — 本文所属系列的完整目录。
