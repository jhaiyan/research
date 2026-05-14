# 深度解读：IBM 科普文《What Is Human In The Loop (HITL)?》

> 原文:[What Is Human In The Loop (HITL)? | IBM](https://www.ibm.com/think/topics/human-in-the-loop)<br>
> 作者:Cole Stryker(IBM Think 频道撰稿人)<br>
> 日期:2025-07-08(原文标注)/ 2026-06-02(本解读发布)

## 原文及译文

<details>
<summary>原文(English)</summary>
<section>

### What is human-in-the-loop?

Human-in-the-loop (HITL) refers to a system or process in which a human actively participates in the operation, supervision or decision-making of an automated system. In the context of AI, HITL means that humans are involved at some point in the AI workflow to ensure accuracy, safety, accountability or ethical decision-making.

Machine learning (ML) has made astonishing strides in recent years, but even the most advanced deep learning models can struggle with ambiguity, bias or edge cases that deviate from their training data. Human feedback can help both improve models and serve as a safeguard for when AI systems perform at insufficient levels. HITL inserts human insight into the "loop," the continuous cycle of interaction and feedback between AI systems and humans.

The goal of HITL is to allow AI systems to achieve the efficiency of automation without sacrificing the precision, nuance and ethical reasoning of human oversight.

### Benefits of HITL

Human-in-the-loop machine learning allows humans to provide oversight and input into AI workflows. Here are the primary benefits of human-in-the-loop:

- **Accuracy and reliability**
- **Ethical decision-making and accountability**
- **Transparency and explainability**

The goal of automating workflows is to minimize the amount of time and effort humans have to spend managing them. However, automated workflows can go wrong in many ways. Sometimes models encounter edge cases that their training has not equipped them to handle. An HITL approach allows humans to fix incorrect inputs, giving the model the opportunity to improve over time. Humans may be able to identify anomalous behaviors using their subject matter expertise, which can then be incorporated into the model's understanding.

In high-stakes applications, humans can impose alerts, human reviews and failsafes to help ensure that autonomous decisions are verified. They can catch biased or misleading outputs, preventing negative downstream outcomes. Continuous human feedback helps AI models to adapt to changing environments.

Bias is an ongoing concern in machine learning, and although human intelligence is known for being quite biased at times, an additional layer of human involvement can help identify and mitigate bias that is embedded into the data and algorithms themselves, which encourages fairness in AI outputs.

When a human is involved in approving or overriding AI outputs, responsibility doesn't rest solely on the model or its developers.

Some decisions require ethical reasoning that may be beyond the capabilities of a model. For example, an algorithmic hiring platform's recommendations might disadvantage certain historically marginalized groups. While ML models have made major strides over the last few years in their ability to incorporate nuance in their reasoning, sometimes human oversight is still the best approach. HITL allows humans, who have better understanding of norms, cultural context and ethical gray areas, to pause or override automated outputs in the event of complex dilemmas.

A human-in-the-loop approach can provide a record of why a decision was overturned with an audit trail that supports transparency and external reviews. This documentation allows for more robust legal defense, compliance auditing and internal accountability reviews.

Some AI regulations mandate certain levels of HITL. For example, the EU AI Act's Article 14 says that "High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use."

According to the regulation, this oversight should prevent or minimize risks to health, safety or fundamental rights, with methods including manual operation, intervention, overriding and real-time monitoring. The humans involved must be "competent" to do so, understanding the system's capabilities and limitations, trained in its proper use and with authority to intervene when necessary. This oversight is intended to encourage the avoidance of harm and proper functioning.

By catching errors before they cause harm, HITL acts as a safety net, especially in high-risk or regulated sectors like healthcare or finance. HITL approaches help to mitigate the "black box" effect where the reasoning behind AI outputs is unclear. Embedding human oversight and control into development and deployment processes helps practitioners identify and mitigate risk, whether that's technical, ethical, legal or operational risk.

### Drawbacks to HITL

HITL is a great approach for enhancing the performance of machine learning systems, but it's not without its drawbacks.

- **Scalability and cost**
- **Human error and inconsistency**
- **Privacy and security**

Human annotation can be slow and expensive, especially for large datasets or iterative feedback loops. As the volume of data or system complexity increases, relying on humans can become a bottleneck. Labeling millions of images for a computer vision model with high precision, for example, may require thousands of hours of human labor. Some domains like medicine or law might require even more expensive subject matter experts in the loop. A mis-labelled tumor on a medical imagine scan could result in a serious mistake.

While humans can provide greater accuracy, in some ways they can be more biased and error prone than machines. Humans may interpret data or tasks differently, especially in domains with no clear right or wrong answer. Human annotators, being human, can get tired, distracted or confused when labelling data. They also hold various perspectives on subjective problems, which can lead to inconsistencies in labelling.

Involving humans in internal review processes can raise privacy concerns, and even well-intentioned annotators might unintentionally leak or misuse sensitive data they access during feedback.

### How does HITL work?

Introducing targeted, high-quality human feedback before, during and after training creates a feedback loop that accelerates learning and makes machine learning models more robust, interpretable and aligned with real-world needs. Here are a few ways that human interaction can be embedded into AI workflows.

- **Supervised learning**
- **RLHF**
- **Active learning**

**Supervised learning** applications require data scientists to correctly label data. This data annotation results in datasets then used to train a machine learning algorithm. This is a workflow where human input is essential and foremost.

For example, a supervised approach in a natural language processing context might involve humans labeling text "spam" or "not spam" in order to teach a machine to successfully make such distinctions. In a computer vision use case, a supervised approach could involve humans labeling a series of images "car" or "bus" or "motorcycle," so that a model can perform object detection tasks.

**RLHF (reinforcement learning from human feedback)** uses a "reward model" trained with direct human feedback, which is then used to optimize the performance of an artificial intelligence agent through reinforcement learning. RLHF is uniquely suited for tasks with goals that are complex, ill-defined or difficult to specify.

**Active learning**: the model identifies uncertain or low-confidence predictions and requests human input only where needed. This concentrates labeling effort on the hardest or most ambiguous examples, leading to faster and more accurate learning.

</section>
</details>

<details>
<summary>译文(中文)</summary>
<section>

### 什么是"人在回路"(HITL)?

**人在回路(Human-in-the-loop,HITL)** 是指人类主动参与自动化系统的运行、监督或决策的系统或流程。在人工智能(AI)语境下,HITL 意味着人类会在 AI 工作流的某些环节中参与其中,以确保准确性、安全性、可问责性(Accountability)或符合伦理的决策。

机器学习(Machine Learning,ML)近年来取得了惊人的进步,但即便是最先进的**深度学习(Deep Learning)** 模型,在面对偏离其训练数据的**模糊性、偏差或边缘案例(Edge Cases)** 时也常常力不从心。人类反馈既有助于改进模型,也能在 AI 系统表现不达标时充当安全屏障。HITL 将人类的洞察力注入"**回路(Loop)**"——即 AI 系统与人类之间持续不断的交互与反馈循环。

HITL 的目标是让 AI 系统在不牺牲人类监督所具备的精确性、细腻度与伦理判断力的前提下,获得自动化带来的效率。

### HITL 的优势

人在回路的机器学习允许人类对 AI 工作流进行监督与介入。以下是人在回路的主要优势:

- **准确性与可靠性**
- **合乎伦理的决策与可问责性**
- **透明度与可解释性**

工作流自动化的目标是尽可能减少人类在管理上所耗费的时间与精力。然而,自动化工作流在很多方面都可能出错。有时模型会遇到训练过程中未曾覆盖的边缘案例。HITL 方法允许人类修正错误的输入,从而让模型有机会随着时间推移不断改进。人类可以凭借其领域专长识别出异常行为,并将其纳入模型的理解之中。

在高风险应用中,人类可以设置**告警、人工审核与失效保护(Failsafe)** 机制,以确保自主决策得到验证。他们能够识别带有偏见或误导性的输出,从而避免负面的下游结果。持续的人类反馈有助于 AI 模型适应不断变化的环境。

偏见是机器学习中长期存在的隐患。尽管人类智能本身也常常带有偏见,但**额外增加一层人工介入,有助于识别和缓解嵌入在数据与算法内部的偏见**,从而推动 AI 输出的公平性。

当人类参与 AI 输出的审批或否决时,**责任便不再完全落在模型或其开发者一方**。

某些决策需要伦理推理,而这可能超出模型的能力范围。例如,一个算法驱动的招聘平台,其推荐结果可能对某些历史上处于弱势地位的群体不利。虽然 ML 模型近年来在融合细微差别的推理能力上取得了重大进展,但在某些情况下,人类监督仍然是最佳选择。HITL 允许对规范、文化背景与伦理灰色地带理解更深的人类,在面对复杂困境时**暂停或推翻自动化输出**。

人在回路方法可以留下一条决策被推翻原因的记录,辅以支持透明度和外部审查的**审计跟踪(Audit Trail)**。这些文档为更稳健的法律辩护、合规审计和内部问责审查提供了支撑。

一些 AI 法规强制要求特定级别的人在回路介入。例如,**欧盟《AI 法案》第 14 条**规定:"高风险 AI 系统的设计与开发,包括其适当的人机界面工具,应当确保在其使用期间能够由自然人(Natural Persons)进行有效监督。"

根据该法规,这种监督应预防或最小化对健康、安全或基本权利的风险,所采用的方法包括**手动操作、介入干预、否决覆盖(Overriding)与实时监控**。参与其中的人类必须具备相应的"能力",理解系统的能力与局限,接受过正确使用的培训,并拥有在必要时进行干预的权限。这种监督旨在促进对危害的规避和系统的正常运行。

通过在错误造成危害之前将其捕获,HITL 充当了一张安全网,在**医疗或金融等高风险或受严格监管的领域**尤其如此。HITL 方法有助于缓解**"黑箱(Black Box)"效应**——即 AI 输出背后的推理过程不甚清晰的问题。将人类监督与控制嵌入到开发与部署流程中,有助于从业者识别和降低**技术、伦理、法律或运营层面**的风险。

### HITL 的缺点

HITL 是提升机器学习系统性能的有效方法,但它也并非没有缺点。

- **可扩展性与成本**
- **人为错误与不一致**
- **隐私与安全**

人工标注可能既缓慢又昂贵,尤其是在大规模数据集或迭代式反馈循环中。随着数据量或系统复杂度的增加,依赖人类可能成为瓶颈。例如,为计算机视觉模型高精度地标注数百万张图片,可能需要数千小时的人力劳动。某些领域(如医学或法律)甚至需要更昂贵的领域专家参与其中。**对医学影像扫描中的肿瘤标注错误,可能会导致严重后果**。

虽然人类能够提供更高的准确性,但在某些方面,他们反而可能比机器更容易出错、也更容易带有偏见。人类对数据或任务的解读可能各不相同,尤其是在没有明确对错的领域。作为人类,人工标注者在标注数据时也会感到疲倦、分心或困惑。他们对主观性问题也持有不同的看法,这会导致标注结果的不一致。

将人类纳入内部审核流程可能引发隐私方面的担忧,即便出于善意的标注者,也可能无意识地泄露或误用其在反馈过程中接触到的敏感数据。

### HITL 是如何工作的?

在训练前、训练中与训练后引入有针对性的、高质量的人类反馈,能够构建一个**加速学习的反馈循环**,使机器学习模型更加稳健、更具可解释性,并与现实世界需求保持一致。以下是一些将人类互动嵌入 AI 工作流的方式。

- **监督学习(Supervised Learning)**
- **基于人类反馈的强化学习(RLHF)**
- **主动学习(Active Learning)**

**监督学习**应用要求数据科学家对数据进行正确标注。这些**数据标注(Data Annotation)** 所产生的标注数据集随后被用于训练机器学习算法。这是一种人类输入至关重要且居于首位的工作流。

例如,在**自然语言处理**场景中,监督式方法可能涉及人类将文本标注为"垃圾"或"非垃圾",以教会机器成功做出此类区分。在**计算机视觉**用例中,监督式方法可能涉及人类将一系列图像标注为"汽车"、"公交车"或"摩托车",以便模型能够执行目标检测任务。

**RLHF(Reinforcement Learning from Human Feedback,基于人类反馈的强化学习)** 使用一个由直接人类反馈训练而成的**"奖励模型(Reward Model)"**,然后通过强化学习来优化 AI 智能体(AI Agent)的性能。RLHF 尤其适用于目标复杂、定义不清或难以明确指定的任务。

**主动学习**:模型会识别出不确定性较高或置信度较低的预测,仅在需要时请求人类输入。这将标注精力集中在最难或最模糊的样本上,从而实现更快、更准确的学习。

</section>
</details>

## 摘要

这篇文章是 IBM Think 频道发布的 HITL(Human-in-the-loop,人在回路)概念科普文,作者 Cole Stryker,2025年7月8日发布。全文约 7,500 字符,系统性地介绍了 HITL 的定义、产生背景、三大优势(准确性/可靠性、合乎伦理的决策与可问责性、透明度/可解释性)、三大缺点(可扩展性与成本、人为错误与不一致、隐私与安全),以及三种典型实现方式(监督学习、RLHF、主动学习)。文章以欧盟《AI 法案》第 14 条的原文引用作为合规层面的关键支撑,体现了从工程实践到法律要求的演变。整体结构清晰,适合作为 AI 治理、责任 AI(Responsible AI)与可信赖 AI(Trustworthy AI)领域的入门读物。

## 术语表

| 术语 | 全称 | 解释 |
| :--- | :--- | :--- |
| **HITL** | Human-in-the-loop(人在回路) | 一种 AI/ML 系统设计范式,要求人类在模型训练、预测或决策的关键环节进行监督、纠正或确认。欧盟 HLEG《可信 AI 伦理指南》(2019)将其定义为"人类在系统的每个决策周期中均可介入"。HITL 是实现"人类监督"(Human Oversight)三种模式之一,另两种为 HOTL(人在回路上,只监控)与 HIC(人在指挥,只决策)。 |
| **RLHF** | Reinforcement Learning from Human Feedback(基于人类反馈的强化学习) | 一种将人类偏好作为奖励信号训练 AI 的技术:先收集人类对模型输出的偏好/排名数据,再用这些数据以监督方式训练"奖励模型",最后用奖励模型通过强化学习算法(如 PPO)优化目标模型。是 ChatGPT、Claude 等大语言模型对齐(Alignment)的核心技术。 |
| **Active Learning** | 主动学习 | 一种 ML 策略:学习算法主动挑选"最有价值"的未标注样本请求人类标注,以最少标注成本获得最大模型提升。典型策略为"不确定性采样"(Uncertainty Sampling)——选择模型最不确定的样本请求标注。文章所述"模型识别低置信度预测并请求人类输入"即对应此策略。 |
| **Supervised Learning** | 监督学习 | 使用**带标签训练数据**(输入-输出对)训练模型映射关系的 ML 范式。常见任务包括分类与回归。HITL 中的人在此阶段扮演"标注者"角色。 |
| **EU AI Act** | Regulation (EU) 2024/1689(欧盟人工智能法案) | 欧盟 2024 年通过的世界首部综合性 AI 法规。**Article 14 "Human oversight"** 强制要求高风险 AI 系统必须设计成可被**自然人**有效监督。Article 14 是 HITL 概念在法律层面的核心载体,使其从"最佳实践"升级为"法律义务"。 |
| **Black Box** | AI 黑箱问题 | 描述 AI/神经网络系统**内部决策过程不透明、不可解释**的特性,导致无法追溯"为什么得出该结论"。理论根源可追溯到 W. Ross Ashby(1956)与 Norbert Wiener(1961)的控制论。需注意 "black box effect" 并非标准化术语,业界更常用 "black box problem"。 |
| **Edge cases** | 边缘案例 | 发生在系统**极端(最大/最小)运行参数**下的问题或情形。在 ML 中常指**训练数据分布之外**、模型未曾见过的罕见但合法的输入,是 HITL 介入的典型场景。 |
| **Algorithmic bias** | 算法偏见 | 计算化社会技术系统中**系统性、可重复的有害倾向**,导致对某些群体产生不公平结果。来源包括:预存偏见(训练数据反映历史不平等)、ML 偏见(数据不平衡、标签偏见)、技术偏见(设计局限)、涌现偏见(反馈循环)。典型案例:COMPAS、亚马逊招聘 AI。 |
| **Natural persons** | 自然人 | 法律术语:指**有法律人格的个体人类**,与"法人"(legal person,即公司、组织等法律实体)相对。在 EU AI Act Article 14 中出现,强调监督必须由**真实人类**执行,**不能由其他自动化系统替代**。 |
| **Data annotation** | 数据标注 | 为数据集(图像、音频、视频、文本)**添加标签或元数据**的过程,使机器能够解读信息。是监督学习的基础工序,典型方法包括图像分类、边界框、语义分割、关键点标注等。是 HITL 的主要人类活动。 |
| **Reward model** | 奖励模型 | 在 RLHF 中,**接受一段文本/序列作为输入,输出一个标量"奖励"** 的函数。模型通过学习人类反馈判断"什么是好的行为",在训练阶段替代人类提供奖励信号。 |
| **Deep Learning** | 深度学习 | ML 的子领域:使用**多层(深层)人工神经网络**逐层提取抽象特征(从像素到边缘到形状再到对象),完成分类、回归、表示学习等任务。典型架构:CNN、RNN、Transformer、GAN。模型越复杂,越需要 HITL 介入以确保可控性。 |
| **Audit Trail** | 审计跟踪 | 对系统决策过程的完整、可追溯记录,记录谁在何时基于什么原因做了什么决策。在 HITL 上下文中,主要用于法律辩护、合规审计和内部问责审查。 |
| **Failsafe** | 失效保护 | 在系统发生故障或产生危险输出时,自动或手动触发以避免危害的安全机制。HITL 中表现为"紧急停止按钮"、人工否决权等。 |
| **IBM** | International Business Machines Corporation(国际商业机器公司) | 美国跨国科技公司,昵称"Big Blue",1911 年成立,总部位于纽约 Armonk。是 AI 研究的先驱(1956 年 Arthur Samuel 在 IBM 704 上实现首个 ML 跳棋程序;2011 年 Watson 赢得 *Jeopardy!*;2024 年开源 Granite 模型)。IBM Research 是全球最大工业研究组织。 |

## 深度解读

### 一、HITL 三角:三种人类角色的本质区别

文章列举了三种 HITL 实现方式——监督学习、RLHF、主动学习,但未明确指出三者在"人类角色"上的本质差异。**这是文章结构上最值得深挖的一个盲点**。

- **监督学习中的人是"教师"(Teacher)**:人类的核心动作是**为大量数据打标签**,模型从这些标签中学习输入-输出映射。这种 HITL 是"批量化、低成本、规模化"的人类劳动,适合数据预处理阶段。
- **RLHF 中的人是"裁判员"(Judge/Annotator)**:人类的核心动作是**对模型输出做偏好比较**(A 比 B 好),用这些偏好训练"奖励模型"再去微调目标模型。这种 HITL 是"高价值、低数量"的人类判断,适合模型对齐阶段。
- **主动学习中的人是"专家"(Oracle)**:人类的核心动作是**只标注模型"最不确定"的样本**,模型主动查询。这种 HITL 是"精确制导、按需调用"的人类智慧,适合标注预算有限的场景。

**解读价值**:理解这三种角色的差异,有助于企业根据业务场景(数据预处理、模型对齐、增量学习)选择合适的 HITL 模式,避免"什么场景都用 RLHF"或"什么场景都靠人工标注"的资源错配。文章把这三者并列罗列,容易让读者误以为它们是平替关系,实际上它们是 HITL 在机器学习流水线不同阶段的**互补工具**。

### 二、文章标题的"概念性折扣":HITL ≠ 人类监督

文章将 EU AI Act Article 14 等同于 HITL 的法律要求,这一表述值得商榷。

经独立验证(详见下表):

- **EU AI Act Article 14 的官方标题是 "Human oversight"**(人类监督),**不是 "Human-in-the-loop"**。
- 欧盟 HLEG 2019《可信 AI 伦理指南》明确区分了三种人类监督模式:
  - **HITL(Human-in-the-loop)**:人类在**每个决策周期中**均可介入(如批准/否决 AI 的每一次输出)。
  - **HOTL(Human-on-the-loop)**:人类在 AI 运行时**持续监控**,在异常时介入(如自动驾驶中的安全员)。
  - **HIC(Human-in-command)**:人类只在**总体目标和伦理边界**层面监督,日常决策完全交给 AI。

**解读价值**:Article 14 实际是**对"人类监督"的总要求**,HITL 只是其中一种最严格的实现方式。**IBM 文章把 Article 14 直接简化为"HITL 法规"是一种概念窄化**,会让读者低估合规的灵活性。例如,某些高风险 AI 系统(如智能客服的次要决策)采用 HOTL 已足够合规,不必每次都让人类逐条审批。文章的这一简化对工程实践可能产生误导。

### 三、HITL 的"成本悖论":免费的安全网与昂贵的速度税

文章列举了 HITL 的三大缺点:**可扩展性、人为错误、隐私**。但有一个隐含矛盾未充分展开——

**HITL 既是最便宜的安全网,也是最昂贵的速度税**。

- **作为安全网**:一次人类否决可以阻止一次医疗误诊、一次算法歧视、一次财务损失。这种"事前成本"远低于"事后代价"。这是 HITL 的"安全价值"。
- **作为速度税**:在需要毫秒级响应的场景(高频交易、实时风控、工业控制),HITL 的"等待人类审批"会直接拖垮系统性能。**HITL 与实时性存在天然张力**。

**解读价值**:文章没有点出这个张力,但在实际工程中,**HITL 的部署策略应区分"决策可逆性"**:
- **可逆决策**(推荐内容、搜索排序):可以低 HITL,甚至用 HOTL/HIC 替代。
- **不可逆决策**(贷款拒绝、医疗诊断、招聘筛选):必须高 HITL。

IBM 文章在"高风险应用"中提到的医疗和金融,恰好是典型的"不可逆决策"领域。这种"决策可逆性 → HITL 强度"的对应关系,是文章没有清晰传达的实务要点。

### 四、监管驱动:HITL 从工程实践到法律义务的范式跃迁

文章引用 EU AI Act Article 14 是全文最"硬"的内容,也是理解 HITL 当前战略意义的关键。

**关键时间表**(经验证):

| 日期 | 里程碑 |
|:---|:---|
| 2024-03-13 | 欧洲议会通过 |
| 2024-05-21 | 理事会正式通过 |
| 2024-07-12 | 公布于欧盟官方公报 |
| 2024-08-01 | 法案正式生效 |
| 2025-02-02 | 不可接受风险条款开始适用 |
| 2026-08-02 | 大多数规定(包含通用 AI 模型治理)开始适用 |
| 2027-08-02 | Annex III 列举的高风险 AI 系统条款适用(医疗、教育、就业等) |
| 2028-08-02 | 嵌入产品的高风险系统条款适用 |

**解读价值**:**文章发布于 2025-07-08,正是 EU AI Act 进入"实质合规期"的前夜**。文章把 HITL 放在监管驱动的语境下,实际上是在为 IBM 企业级客户(尤其是金融、医疗、跨境电商)发出信号:
- **2026-08-02 之后**,在欧盟市场部署 AI 系统的企业必须证明其"人类监督机制"符合 Article 14。
- HITL 不再只是"AI 治理最佳实践",而是进入"AI 治理合规清单"。
- 企业应从现在起就建立**可审计、可追溯、有据可查的 HITL 工作流**,否则将面临高额罚款(违规最高可处 7% 全球营业额)和产品下架。

**文章的战略意图**:IBM 作为企业 AI 解决方案提供商(尤其是 watsonx、Granite 系列),发布此文的时机显然与 EU AI Act 实施节奏紧密相关。这不是一篇中性的科普文,而是带有**市场教育**性质的合规预警。

### 五、"黑箱"与"可解释性"——文章没有展开的哲学命题

文章用"black box effect"一词,提到 HITL 有助于缓解 AI 推理过程不透明的问题。但这是文章**最薄弱的一笔**。

- "Black box" 本身是控制论(cybernetics)经典概念,Ashby、Wiener、Bunge 等学者均有系统论述。
- 但 "black box effect" 并不是标准化术语。**业界更准确的表达是 "black box problem"**(黑箱问题)或 "opacity problem"(不透明问题)。
- 文章没有区分:
  - **内在不透明**(Intrinsic Opacity):深度神经网络的复杂非线性导致即使设计者也难以解释某个具体决策。
  - **故意不透明**(Intentional Opacity):商业 AI 服务(如商业推荐系统)出于商业秘密考虑拒绝披露机制。
  - **事后不可解释**(Post-hoc Unexplainability):理论上可解释但解释成本极高的情形。

**解读价值**:HITL 在"内在不透明"问题上**只能缓解,不能根治**——人类在回路中看到的是输入和输出,中间过程仍是黑箱。HITL 真正的作用是**建立"责任可追溯性"**(即使推理过程不透明,出错时有人负责、有记录可查)。文章没有清晰传达这一区分,可能让读者高估 HITL 的"可解释性"贡献。

### 六、真实性评估

以下是对文章关键事实的独立验证结果(由专门 Agent 通过 WebSearch + WebFetch 完成):

| 声明/事实 | 验证状态 | 说明 |
| :--- | :--- | :--- |
| **EU AI Act Article 14 原文引用** "High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use." | **已验证** | 逐字与欧盟官方法律文本(Regulation (EU) 2024/1689, Article 14(1))一致。但需注意:该条款标题是 **"Human oversight"**(人类监督),**不是 "Human-in-the-loop"**。文章将 Article 14 等同于 HITL 的法律定义,存在**概念窄化**问题。 |
| **EU AI Act 时间线** 法案的通过、签署、公布、适用日期 | **已验证** | 2024-03-13 议会通过、2024-05-21 理事会通过、2024-07-12 公布、2024-08-01 生效、2025-02-02 不可接受风险条款适用、2026-08-02 大多数规定适用、2027-08-02 Annex III 高风险系统适用。 |
| **HITL 标准定义** Human-in-the-loop 的学术与工业界定义 | **已验证** | 欧盟 HLEG 2019《可信 AI 伦理指南》定义为"Human intervention in every decision cycle of the system"。但该指南同时区分 HITL/HOTL/HIC 三种模式,文章未提此区分。 |
| **RLHF 技术原理** "reward model trained with direct human feedback, used to optimize AI agent through reinforcement learning" | **已验证** | 准确对应 OpenAI 2019 论文及 Stiennon et al. 2020 *Learning to summarize with human feedback* 中的标准三步流程(收集人类偏好→训练奖励模型→用 PPO 微调策略)。 |
| **Active learning 工作方式** "the model identifies uncertain or low-confidence predictions and requests human input only where needed" | **已验证** | 准确对应 Settles (2009) 经典综述中的 "uncertainty sampling"(不确定性采样)策略。但文章未提及 active learning 还有其他采样策略(如 diversity sampling、query-by-committee)。 |
| **"Black box" 现象** 在 AI 领域是公认概念 | **部分验证** | "Black box" 本身是公认概念(控制论术语,Ashby 1956、Wiener 1961、Bunge 1963)。但文章用 "black box effect" **并非标准化术语**,严谨度略嫌不足。 |
| **作者 Cole Stryker 的身份** | **无法验证** | 多个权威来源(colestryker.com、LinkedIn、Britannica、Goodreads、IBM 作者页)检索失败或返回 403/404。存在同名作家(*Hacking the Future*,2012),但与 IBM 当前撰文的关系未能确认。 |
| **HITL 概念三角**(监督学习/RLHF/主动学习)的并列方式 | **存疑/简化过度** | 三者在 ML 流水线中处于不同阶段(数据预处理/模型对齐/增量学习),角色不同(教师/裁判员/专家)。文章并列罗列,容易让读者误以为是平替关系。 |
| **"AI 法规强制要求 HITL"** 的笼统表述 | **部分验证** | EU AI Act 强制要求的是 "Human oversight",HITL 只是其中最严格的一种实现。文章表述存在概念简化。 |

### 七、对从业者的实务启示

1. **不要简单地把 Article 14 等同于 HITL**:在 EU AI Act 合规设计中,应区分 HITL/HOTL/HIC 三种模式,选择与决策可逆性、响应延迟要求相匹配的人类监督方式。
2. **HITL 不是万能解**:它的核心价值是**"责任可追溯"**,而不是"解决黑箱问题"。在不可逆决策(医疗、招聘、信贷)中是必须的;在可逆决策(推荐、排序)中可以是可选的。
3. **HITL 的"成本-价值"权衡应分阶段设计**:
   - 训练阶段:优先用监督学习(规模化)+ 主动学习(降本),只在关键样本上用专家。
   - 对齐阶段:用 RLHF 解决"价值观对齐"问题,而不是"性能优化"问题。
   - 部署阶段:用 HOTL/HIC + Failsafe 应对"决策可逆性"问题。
4. **建立可审计的 HITL 工作流**:在 2026-08-02 之前,企业应建立**带时间戳、责任人、决策依据的审计日志系统**,为 Article 14 合规做好准备。
5. **关注"自然人"含义**:Article 14 强调"natural persons",意味着监督**不能由另一个 AI 系统替代**。企业不能用 "AI 监督 AI" 应对合规要求。

### 总结

这篇文章是 IBM 为企业客户撰写的 HITL 概念入门读物,时机精准(在 EU AI Act 实质合规期前夜)、结构清晰、覆盖面广。但作为深度分析材料,它存在三个主要不足:**(1)把 Article 14 等同于 HITL 的概念窄化;(2)把三种 HITL 实现方式并列罗列,未澄清角色差异;(3)对"黑箱"和"可解释性"的处理过于简化**。尽管如此,文章作为"快速建立 HITL 概念地图"的入门资料,对企业 AI 治理团队、产品经理、合规官仍有较高的实用价值。

**关键要点:**

- HITL 是 AI 系统设计范式,而非单一技术。文章列举的监督学习、RLHF、主动学习是三种典型实现,人类角色分别是"教师/裁判员/专家"。
- EU AI Act Article 14 强制要求的是"Human oversight"(人类监督),HITL 是其中最严格的一种。文章将两者等同存在概念窄化。
- 文章发布于 EU AI Act 实质合规期前夜(2025-07-08),具有"市场教育"性质的合规预警价值。
- HITL 的核心价值是"责任可追溯",而不是"解决黑箱问题"。在不可逆决策中是必须的,在可逆决策中可以灵活选择 HITL/HOTL/HIC。
- "Black box effect" 并非标准化术语,严谨的工程表达应为 "black box problem" 或 "opacity problem"。

## 参考资料

- [What Is Human In The Loop (HITL)? | IBM](https://www.ibm.com/think/topics/human-in-the-loop) — 本文解读的原文
- [EU AI Act, Article 14 - Human oversight(artificialintelligenceact.eu)](https://artificialintelligenceact.eu/article/14/) — EU AI Act 第 14 条官方解读
- [Ethics Guidelines for Trustworthy AI(欧盟 HLEG,2019)](https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai) — HITL/HOTL/HIC 三种模式区分的权威来源
- [Reinforcement learning from human feedback(Wikipedia)](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback) — RLHF 技术原理与 OpenAI 2019 论文引用
- [Active Learning Literature Survey(Settles, 2009, University of Wisconsin–Madison)](https://research.cs.wisc.edu/techreports/2009/TR1648.pdf) — Active learning 不确定性采样策略的经典综述
- [EU AI Act implementation timeline(artificialintelligenceact.eu)](https://artificialintelligenceact.eu/implementation-timeline/) — EU AI Act 关键时间节点
- [Algorithmic bias(Wikipedia)](https://en.wikipedia.org/wiki/Algorithmic_bias) — 算法偏见的四类来源与典型案例
- [Black box(Wikipedia)](https://en.wikipedia.org/wiki/Black_box) — 黑箱概念在控制论与 AI 中的经典定义
- [Data annotation(Wikipedia)](https://en.wikipedia.org/wiki/Data_annotation) — 数据标注方法与 HITL 关系
- [IBM(Wikipedia)](https://en.wikipedia.org/wiki/IBM) — IBM 公司背景与 AI 研究历史
- [EU AI Act 欧洲议会专题页](https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence) — 欧洲议会官方对 AI Act 的说明
- [Natural person(Wikipedia)](https://en.wikipedia.org/wiki/Natural_person) — "自然人"法律术语在欧盟法规中的含义
