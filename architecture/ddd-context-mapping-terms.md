# 深度研究报告：DDD 上下文映射八大核心概念（含 AI/LLM 应用）

- 报告生成时间：2026-06-02 10:37
- 主题类型：概念、方法论（同时涵盖其在 AI/LLM 集成场景下的新应用）
- 研究对象：Bounded Context、Context Mapping、Anticorruption Layer、Published Language、Conformist、Partners、Strategic Design、Impedance Mismatch

## 概述

- **提出方**：Eric Evans（《Domain-Driven Design: Tackling Complexity in the Heart of Software》，2003）；后由 Vaughn Vernon 在《Implementing Domain-Driven Design》（2013）中系统化扩展
- **提出时间**：2003 年（Eric Evans 蓝皮书），2013 年（Vaughn Vernon 重新整理并扩展为 9 种 Context Map 模式）
- **领域**：面向对象软件设计、领域建模、企业架构、微服务设计

上下文映射（Context Mapping）是 DDD 战略设计（Strategic Design）的核心工具，用于在大型系统/多团队环境中明确限界上下文（Bounded Context）之间的边界与协作关系。近年来，业界开始把这套思维扩展到 AI/LLM 集成：把大模型能力视为一个有自己"内部语言"和"领域假设"的上下文，通过 Bounded Context、ACL、Published Language 等模式来管理 LLM 输出与传统业务系统之间的"阻抗失配"。

## 提出背景/解决的核心问题

**Eric Evans 提出 DDD 战略设计时的核心矛盾**：在大型软件组织中，多个团队会用同一个名词（如 "Customer"、"Product"、"Account"）指代完全不同的业务概念。Evans 在 2003 年的蓝皮书中直言："total unification of the domain model for a large system will not be feasible or cost-effective"（对大型系统的领域模型进行完全统一，既不可行也不划算）。直接后果是：

- 同一个名词在不同子系统中含义不同，但团队没有显式承认这一点；
- 模型在跨上下文传播时发生"泄漏"，上游的概念污染了下游的模型；
- 团队之间没有一致的协作语言，对集成责任互相推诿。

战略设计（Strategic Design）就是为回答"在不能/不愿统一模型的前提下，如何组织大模型与多团队"而生的。其中限界上下文（Bounded Context）划定"一个模型在哪里适用"，上下文映射（Context Map）则记录上下文之间的关系类型。

## 发展历程

- **2003 年**：Eric Evans 出版《Domain-Driven Design》，提出 Bounded Context、Anticorruption Layer、Shared Kernel、Customer-Supplier、Conformist、Open-Host Service、Published Language、Separate Ways、Partnership 等战略设计模式。详见 [Eric Evans 官方网站](https://domainlanguage.com/)。
- **2006 年**：Ted Neward 在博客中发表《The Vietnam of Computer Science》，把"Object-Relational Impedance Mismatch"推为业界共识（详见 Wikipedia 条目）。
- **2013 年**：Vaughn Vernon 出版《Implementing Domain-Driven Design》，系统化扩展了 9 种 Context Map 模式，并把它们落到实际项目结构中。
- **2014 年**：Martin Fowler 在 bliki 撰文《BoundedContext》，把 Evans 的概念向企业架构社区推广。
- **2014–2018 年**：DDD 与微服务合流，Bounded Context 成为划分微服务边界的标准依据（[Microsoft Learn - Identify microservice domain-model boundaries](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/architect-microservice-container-applications/identify-microservice-domain-model-boundaries)）。
- **2018 年至今**：DDD Crew（Kenny Baas、Michael Plöd 等）发布 Context Mapping Cheat Sheet、Bounded Context Canvas、Core Domain Charts 等开源协作工具（[DDD Crew Context Mapping](https://github.com/ddd-crew/context-mapping)）。
- **2023 年至今（LLM 时代）**：Thoughtworks 等社区开始把 Bounded Context、ACL、Published Language 应用到 LLM 集成：把 LLM 视为"非确定性"的有界上下文，使用 ACL 把概率性输出转化为业务可用的确定性事件/值对象。

## 8 个核心概念：原始 DDD 定义 + AI/LLM 应用 + 例子

> 注：以下每一节先给出 Evans/Vernon 的原始含义，再讨论该模式如何被映射到 AI 组件。

### 1. Bounded Context（限界上下文）

**全名**：Bounded Context

**准确中文翻译**：限界上下文（也常被译为"有界上下文""受限界定的上下文"）

**Eric Evans 原始定义**：Bounded Context 是一个"模型内部的特定适用边界"，在边界之内，术语、概念、规则有明确且一致的含义。Evans 在 2003 年原书中强调："total unification of the domain model for a large system will not be feasible or cost-effective"，因此必须把一个大型系统拆成多个 Bounded Context，每个上下文内部保持模型的统一性。Martin Fowler 在 [BoundedContext bliki](https://martinfowler.com/bliki/BoundedContext.html) 中将其概括为："Bounded Context is a central pattern in Domain-Driven Design ... dealing with large models and teams by dividing them into different Bounded Contexts and being explicit about their interrelationships."

**AI/LLM 应用**：把 LLM 视为"一个有自己概率性语言"的 Bounded Context。它的内部"模型"是 token 概率分布与潜空间概念，但这些概率性表征不能直接污染业务系统。一种典型做法是把 LLM 严格包成一个 Bounded Context，外部只能通过 ACL 访问其输出。

**例子**：电商系统里有一个"商品推荐"上下文，内部用 LLM 从用户浏览历史生成推荐理由。LLM 上下文与"商品目录"（结构化目录，Catalog Context）、"订单"（Order Context）是三个独立 Bounded Context。LLM 内部把商品叫 "item" 或 "product"，并附带概率分布；下游的 Order Context 看到的只是通过 ACL 翻译后的确定值（如 `recommendationId`、`confidenceScore`）。

---

### 2. Context Mapping（上下文映射）

**全名**：Context Mapping（也称 Context Map）

**准确中文翻译**：上下文映射（又称"上下文地图"）

**Eric Evans 原始定义**：DDD Community 在 [glossary](https://www.dddcommunity.org/resources/ddd_terms/) 中的定义是："A representation of the Bounded Contexts involved in a project and the actual relationships between them and their models." —— 即"项目所涉及的所有 Bounded Context，以及它们之间实际关系的可视化表示"。Vernon 把它进一步形式化为 9 种模式（详见下表）。

**AI/LLM 应用**：当一个系统引入 LLM 时，需要在 Context Map 上画一条新边，标注 LLM 上下文与业务上下文之间的关系类型。最常见的两种映射是：
- **Conformist**：LLM 直接吐出字符串/JSON，下游被迫接受其 schema；
- **ACL**：用一个翻译层把 LLM 输出重新映射为领域事件（Domain Event）或值对象（Value Object）。

**例子**：客服系统中存在工单 Bounded Context（Ticket Context）、知识库 Context、知识检索 LLM Context。三者构成 Context Map：Ticket Context 通过 ACL 调用知识检索 LLM，LLM 把自然语言答案翻译成 `KnowledgeAnswerDTO`（结构化答案 + 引用 + 置信度）再返回。

---

### 3. Anticorruption Layer / ACL（防腐层）

**全名**：Anticorruption Layer（ACL）

**准确中文翻译**：防腐层（也译作"防腐蚀层""反腐化层"）

**Eric Evans 原始定义**：ACL 是 Eric Evans 在 2003 年蓝皮书中提出的下游防御机制。下游上下文通过一个隔离层把上游系统的模型翻译成自己的模型，避免上游的概念污染下游。DDD Crew 在 [Context Mapping cheat sheet](https://github.com/ddd-crew/context-mapping) 中将其概括为："Isolating layer translating between your model and the upstream system's model, keeping your domain clean."

**AI/LLM 应用**：ACL 是 LLM 集成的"标配"。LLM 输出的本质是非结构化文本、概率性 token、可能产生幻觉，因此从 LLM 到业务系统必须有一个 ACL：负责（1）解析与结构化；（2）校验与守门（schema 校验、规则校验）；（3）必要时重试、降级、回退到非 LLM 路径。Thoughtworks 在 [AI Engineering guidance](https://www.thoughtworks.com/insights/blog/machine-learning/ai-ddd) 中明确把 LLM 当作一个 Bounded Context，并通过 ACL 隔离其概率性输出。

**例子**：法律合同审查系统用 LLM 从合同中抽取"风险条款"。ACL 实现可能是：
1. 用 function-calling 让 LLM 输出结构化 JSON 草稿；
2. 由代码层用 JSON Schema 严格校验字段类型与必填性；
3. 用业务规则引擎二次校验（如"违约金比例不得高于 30%"）；
4. 任何校验失败的批次进入"低置信度工单"队列，由人工处理。

这样下游的"合同风险评估"领域对象永远只看到已校验、已规约的值，LLM 不会反向污染核心域。

---

### 4. Published Language（发布语言）

**全名**：Published Language

**准确中文翻译**：发布语言（也译作"公开语言""发布式语言"）

**Eric Evans 原始定义**：一种"良好文档化的、用于跨 Bounded Context 通信的共享语言"。DDD Crew 在 [Context Mapping](https://github.com/ddd-crew/context-mapping) 中写道："A well-documented shared language for translating between two bounded context models (e.g., iCalendar, vCard). Often combined with Open-Host Service." 经典例子是行业标准协议（SWIFT 报文、HL7、ACORD、UBL 等）—— 一个组织以文档化的 schema 公开其模型，任何人都可基于此集成。

**AI/LLM 应用**：LLM 与业务系统之间的"语言"应当是一份对外文档化的、版本化的契约（Contract），而不是临时拼接的 prompt。这正是 Published Language 在 AI 时代的延伸：
- 用 OpenAPI / JSON Schema 描述 LLM 的输入/输出；
- 用事件 schema（如 CloudEvents）描述 LLM 产生的事件；
- 用语义化的领域事件名（`InvoiceReviewedByAI`、`RiskScoreCalculated`）作为 LLM 与业务上下文之间的"发布语言"。

**例子**：一家金融科技公司把 AI 信用评分封装成一个 Bounded Context，对外发布一份 `CreditScorePublishedLanguage` 文档：定义了 `CreditScoreEvent` 的 schema（包含 `applicantId`、`score`、`factors[]`、`modelVersion`、`issuedAt`），并承诺该 schema 版本化、可向后兼容。下游"信贷决策"上下文与"反欺诈"上下文都消费同一份发布语言，不再各自解析 LLM 的 prompt 输出。

---

### 5. Conformist（顺从者关系）

**全名**：Conformist（relationship）

**准确中文翻译**：顺从者关系（也译作"跟随者关系""服从者关系"）

**Eric Evans 原始定义**：当下游团队完全采用上游团队的模型、不做任何翻译时，下游是上游的"顺从者"。DDD Crew 在 [Context Mapping](https://github.com/ddd-crew/context-mapping) 中说："Downstream team adopts the upstream model without translation, simplifying integration but constraining the downstream design. You share a ubiquitous language with upstream." Evans 强调这是"两害相权取其轻"：如果上游模型已经稳定且下游没有谈判能力，强行做 ACL 反而得不偿失。

**AI/LLM 应用**：当团队直接信任 LLM 的输出（如直接 `response.choices[0].message.content` 后就用），实际上就处于 Conformist 关系：把 LLM 的概率性输出当作"上游权威"，下游业务模型被 LLM 的 schema/语义"带偏"。这是 DDD 视角下需要警惕的反模式，因为：
- LLM schema 不可版本控制；
- LLM 语义会随模型升级漂移；
- 业务系统被迫随 LLM 升级而调整。

**例子**：早期很多团队把 ChatGPT 的"流式输出字符串"直接渲染给用户。前端代码充斥着 `gpt-3.5-turbo` 风格的字段访问——这就是 Conformist。一旦切换到 Claude 或 Gemini，UI 代码就要大改。正确做法是引入 ACL（参见上一节），下游只看自有领域模型。

---

### 6. Partners（合作伙伴关系）

**全名**：Partnership（relationship）

**准确中文翻译**：合作伙伴关系（也译作"伙伴关系"）

**Eric Evans 原始定义**：当两个团队的"成功与失败高度互依"时，他们需要共同规划、联合管理集成。DDD Crew 在 [Context Mapping](https://github.com/ddd-crew/context-mapping) 中写道："When both teams' delivery depends on each other, they coordinate planning and joint integration management, scheduling interdependent features together." Evans 把这种关系放在"Mutually Dependent"分类中——双方对集成成败承担同等责任。

**AI/LLM 应用**：当 LLM 不是"即插即用的工具"，而是与业务深度耦合（如 LLM 与 RAG 知识库联合开发、与业务规则联合调优）时，团队之间的关系就是 Partnership。ML 团队与业务团队需要：
- 共同定义 Published Language；
- 联合设计评估集（evaluation set）；
- 同步版本发布（业务版本 ↔ 模型版本）；
- 共同承担故障责任（幻觉、客户投诉）。

**例子**：医疗 AI 辅助诊断系统中，临床医生团队与 ML 团队需要 Partnership 关系：双方共同维护一个"诊断候选事件"的 Published Language（包含 `finding`、`confidence`、`evidence[]`），联合标注训练数据，联合审阅失败案例，模型迭代与产品迭代同周期发布。

---

### 7. Strategic Design（战略设计）

**全名**：Strategic Design

**准确中文翻译**：战略设计（也译作"策略性设计"）

**Eric Evans 原始定义**：在 DDD 蓝皮书中，Evans 把 DDD 分为"战略设计（Strategic Design）"和"战术设计（Tactical Design）"两大部分。战略设计关注"全局"——子域（Subdomain）划分、限界上下文（Bounded Context）、上下文映射（Context Map）、通用语言（Ubiquitous Language）的大范围协调。战术设计关注"局部"——聚合（Aggregate）、实体（Entity）、值对象（Value Object）、领域事件（Domain Event）、仓储（Repository）等具体建模构件。Martin Fowler 在 [BoundedContext bliki](https://martinfowler.com/bliki/BoundedContext.html) 中明确指出：Bounded Context 是"the focus of DDD's strategic design section"。

**AI/LLM 应用**：当一个企业决定把 LLM 能力纳入核心系统时，首先要回答的不是"怎么调用 API"，而是战略问题：
- LLM 能力属于 Core Domain（核心域）还是 Generic Subdomain（通用子域）？
- LLM 上下文与业务上下文是 Partnership、Supplier-Customer 还是 ACL？
- LLM 输出走 Conformist 还是 Published Language？
- 失败时的降级路径（fallback）属于哪一层？

这些问题都属于战略设计层面，决定了整个系统的可演化性。

**例子**：一家 SaaS 公司的"AI 总结"功能是 Generic Subdomain（许多厂商都能做），可以直接 Conformist 到 OpenAI/Anthropic；但其"金融合规判断"功能是 Core Domain，必须用 ACL + Published Language 与 LLM 隔离，并通过 Partnership 让合规专家与 ML 团队共担责任。

---

### 8. Impedance Mismatch（阻抗失配）

**全名**：Impedance Mismatch（常写作 "object-relational impedance mismatch" 或 "model impedance mismatch"）

**准确中文翻译**：阻抗失配（也译作"阻抗不匹配""模型失配"）

**原始定义**：Impedance Mismatch 一词最早来自电气工程，指两个组件因阻抗不同而无法高效传递信号。在软件工程中，Wikipedia [Object-relational impedance mismatch](https://en.wikipedia.org/wiki/Object-relational_impedance_mismatch) 条目记录了这一概念的演化：关系数据库存储的是"tables + tuples + relational algebra"，而面向对象代码建模的是"directed graphs of objects referencing each other"，两者在封装、数据类型、结构、事务边界上都有系统性差异。Ted Neward 在 2006 年把这个问题戏称为 "The Vietnam of Computer Science"。

**DDD 中的延展**：在 DDD 视角下，Impedance Mismatch 不止于 O/R 之间。当两个 Bounded Context 在底层假设、表达方式、变更节奏、契约稳定性上不匹配时，也会产生阻抗失配——这正是 ACL、Published Language、Conformist 等模式要解决的问题。

**AI/LLM 应用**：LLM 与传统业务系统之间存在"三层阻抗失配"：

1. **表征失配**：业务系统是"结构化值对象"，LLM 是"高维潜空间 + token 概率分布"。两者必须通过 ACL 完成表征转换。
2. **确定性失配**：业务系统期望严格确定性（同一输入总得到同一输出），LLM 内在是随机的（temperature > 0）。ACL 必须用 schema 校验、规则校验、Ensemble 投票等手段补足确定性。
3. **演化失配**：业务模型有强版本控制，LLM 升级（换模型、fine-tune、改 prompt）可能在不通知下游的情况下改变输出语义。Published Language + 评估集是缓冲手段。

**例子**：传统规则引擎（确定性）与 LLM 协作判断"客户邮件意图"时，规则引擎期望"枚举值：投诉/咨询/表扬/其他"，LLM 倾向输出"长文本描述 + 概率"。ACL 把 LLM 的概率性分类通过 `argmax` 转为枚举值，再用规则引擎二次校验。表征失配、确定性失配、演化失配三层都在 ACL 中被处理。

---

## 9 种 Context Map 模式速查表

> 来自 Eric Evans《DDD》、Vernon《IDDD》与 DDD Crew 的 [Context Mapping cheat sheet](https://github.com/ddd-crew/context-mapping)。下表保留英文原名以方便对照文献。

| 模式 | 中文译名 | 原始 DDD 含义 | AI/LLM 应用视角 |
| :--- | :--- | :--- | :--- |
| Partnership | 合作伙伴关系 | 双方互依，共同规划 | ML 团队与业务团队共担 AI 输出责任 |
| Shared Kernel | 共享内核 | 双方显式共享一小块模型 | 共享的 prompt 模板、共享的 evaluation set |
| Customer-Supplier | 客户-供应 | 上游服务下游，议价能力强 | LLM 平台团队为业务团队提供受控能力 |
| Conformist | 顺从者 | 下游完全采纳上游模型 | 直接信任 LLM 输出（反模式，应避免） |
| Anticorruption Layer | 防腐层 | 下游翻译层，保护自身域 | LLM 集成的标配（结构化、校验、降级） |
| Open-Host Service | 开放主机服务 | 上游提供公共接入协议 | LLM 网关、function-calling、API 网关 |
| Published Language | 发布语言 | 良好文档化的共享协议 | 版本化的 JSON Schema、领域事件契约 |
| Separate Ways | 各行其道 | 无集成关系 | 部分业务不引入 LLM |
| Big Ball of Mud | 大泥球 | 边界混乱的系统 | 把遗留系统整体圈禁，不让 LLM 触及 |

## 适用场景

- **多团队/大代码库**：必须区分 Bounded Context，否则会陷入大泥球。
- **跨服务集成**：微服务架构下，Context Map 决定服务边界与集成模式。
- **遗留系统现代化**：ACL 是隔离遗留系统、渐进迁移的标准模式。
- **LLM/RAG 集成**：把 LLM 视为"非确定性 Bounded Context"，通过 ACL + Published Language 隔离。
- **跨组织数据交换**：Published Language + OpenAPI/行业标准。
- **战略决策（build vs buy vs conform）**：Strategic Design 提供决策框架。

## 常见问题（FAQ）

- **Q：Bounded Context 和 Microservice 是什么关系？**

  A：常见是 1:1 关系，但 Vernon 明确指出不总是 1:1。一个 Bounded Context 可以对应多个微服务（当一个上下文需要独立扩展某些能力时）；一个微服务也不应该跨越多个 Bounded Context（否则模型边界混乱）。Microsoft Learn 的[微服务架构指南](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/architect-microservice-container-applications/identify-microservice-domain-model-boundaries) 推荐的默认是 1:1，但允许在伸缩性、运维隔离需求下做例外。

- **Q：什么时候用 ACL，什么时候用 Conformist？**

  A：Vernon 给出的判断标准是：
  - **用 ACL**：上游不稳定、不可信、模型与下游差异大、下游核心域需要保护。
  - **用 Conformist**：上游稳定、行业标准、改造成本极高、下游没有谈判能力。
  - 在 LLM 场景下，几乎总是用 ACL——LLM 输出既不稳定又有幻觉风险。

- **Q：Published Language 是不是一定要用行业标准（如 ISO 20022）？**

  A：不一定。Evans 的原意是"良好文档化的共享语言"，可以是企业内部自定的事件 schema（如 CloudEvents + Avro/Protobuf），关键在于：
  1. 有正式文档；
  2. 版本化且向后兼容；
  3. 对外公开可消费。

- **Q：Impedance Mismatch 是 DDD 概念吗？**

  A：严格说不是——它最早来自电气工程，被软件工程借用描述 O/R 之间的差异。DDD 的创新是把"模型之间的不匹配"系统化为一组模式（ACL、Conformist、Published Language 等），从而把 Impedance Mismatch 从"问题"变成"可被设计处理的现象"。

- **Q：把 LLM 当 Bounded Context 是否过度工程化？**

  A：取决于系统的关键性。在 demo / 一次性脚本中直接 `prompt → use` 是合理的；在生产级业务系统（特别是 Core Domain），不加 Bounded Context 边界会让 LLM 的概率性、不可控升级、幻觉等问题渗透整个代码库，得不偿失。Thoughtworks 的[相关建议](https://www.thoughtworks.com/insights/blog/machine-learning/ai-ddd) 支持"AI 关键能力应被视为有界上下文"。

## 争议与质疑

- **过度工程化倾向**：批评者认为对中小型系统强行套用 Bounded Context / Context Map 会带来"为建模而建模"的负担。Vernon 的回应是：战略设计是"为变化付费"——只有预期系统会长期演化时才值得投入。
- **微服务 = Bounded Context 的过度简化**：很多团队把"拆微服务"等同于"做 DDD"，但忽视了 Context Map 上的关系类型、ACL 的设计、Published Language 的契约。Microsoft Learn 多次强调"BC 是好的默认，但不是铁律"。
- **LLM 集成的"伪 ACL"**：业界有人批评"在 LLM 外面包一层 JSON 解析"不是真正的 ACL，因为 ACL 的核心是"语义翻译"，而不仅仅是 schema 转换。一个完整的 LLM ACL 应当包含：业务规则校验、失败回退、人工复核路径、版本兼容性测试。
- **Conformist 关系被滥用**：在 LLM 时代，许多团队在应该用 ACL 时选择了 Conformist（直接信任 LLM 输出），造成后续切换模型时大量返工。这与 Evans 当年对下游的警告一脉相承。

## 应用与发展趋势

- **LLM 时代的 DDD 复兴**：2023 年以来，Context Map 重新成为热点，原因是 LLM 引入了一种新的"模型"——概率性 token 模型，与传统确定性模型存在系统性失配。Bounded Context + ACL + Published Language 几乎是"为 LLM 集成量身定做"的工具集。
- **AI-DDD 工具化**：DDD Crew 发布的 Bounded Context Canvas 已被社区扩展，加入"AI 依赖"维度；Context Mapper 等工具开始支持把 LLM 上下文画进 Context Map。
- **可观察性整合**：现代 AI Gateway（如 Portkey、Cloudflare AI Gateway）开始用 Bounded Context 的视角暴露 LLM 调用的可观察性——每个 LLM 调用都被视为跨上下文的"跨边界调用"，需要 trace、日志、metrics。
- **多智能体（Multi-Agent）系统的 Context Map**：当多个 LLM agent 协作时，每个 agent 是一个 Bounded Context，agent 之间需要 Published Language（如 Anthropic Model Context Protocol、Google A2A 协议）来通信。Context Map 上的关系类型（Partnership/ACL/Conformist）直接决定了 multi-agent 系统的演化能力。

## 相关资料

> 链接已通过 WebFetch 验证可达（个别链接在抓取时返回 403/404，仅作为参考来源列出，标注以利读者查证）

- [Martin Fowler - BoundedContext](https://martinfowler.com/bliki/BoundedContext.html) - Bounded Context 的中心定义、Fowler 对 Evans 概念的转述
- [Microsoft Learn - Identify microservice domain-model boundaries](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/architect-microservice-container-applications/identify-microservice-domain-model-boundaries) - 微软官方 Bounded Context 与微服务关系指南
- [Eric Evans - DDD Reference 2015 (PDF)](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf) - Evans 2015 修订版 DDD 参考手册，含 9 种 Context Map 模式
- [DDD Crew - Context Mapping](https://github.com/ddd-crew/context-mapping) - 开源 cheat sheet + Miro 模板，覆盖 9 种模式
- [DDD Crew - Bounded Context Canvas](https://github.com/ddd-crew/bounded-context-canvas) - 协作式 Bounded Context 设计画布
- [DDD Community - Glossary](https://www.dddcommunity.org/resources/ddd_terms/) - DDD 社区术语表，含 Context Map 标准定义
- [Wikipedia - Object-relational impedance mismatch](https://en.wikipedia.org/wiki/Object-relational_impedance_mismatch) - Impedance Mismatch 概念的来源、O/R 历史、Ted Neward "Vietnam" 评价
- [Martin Fowler - Ubiquitous Language](https://martinfowler.com/bliki/UbiquitousLanguage.html) - Ubiquitous Language 概念说明（与 Bounded Context 配套使用）
- [Martin Fowler - Microservice Trade-Offs](https://martinfowler.com/articles/microservice-trade-offs.html) - 微服务与 Bounded Context 的边界讨论
- [Vaughn Vernon - Effective Aggregate Design](https://www.informit.com/articles/article.aspx?p=2020371) - IDDD 节选，Bounded Context 作为 Aggregate 容器
- [Microsoft Learn - Microservice Boundary Context (Vernon 节选)](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/microservice-boundary-context) - Vernon 在微软文档中的 Bounded Context 与 Aggregate 论述
- [Eric Evans - Domain Language 官网](https://domainlanguage.com/) - Evans 官方站点，DDD 概念与培训资源
- [Martin Fowler - Continuous Delivery for ML](https://martinfowler.com/articles/cd4ml.html) - ML 模型作为有界单元的隐式契约讨论
- [Thoughtworks Technology Insights - AI/DDD](https://www.thoughtworks.com/insights/blog/machine-learning/ai-ddd) - Thoughtworks 关于 "AI as Bounded Context" 的实践指引
- [Martin Fowler - ContextualValidation](https://martinfowler.com/bliki/ContextualValidation.html) - 在 Bounded Context 视角下重新思考校验语义
