# 深度解读：Consumer-Driven Contract Testing (CDC)

> 原文：[Consumer-Driven Contract Testing (CDC)](https://microsoft.github.io/code-with-engineering-playbook/automated-testing/cdc-testing/)<br>
> 作者：Microsoft（ISE Engineering，机构署名，无个人作者）<br>
> 日期：2024-08-22

## 原文及译文

<details>
<summary>原文</summary>
<section>

# Consumer-Driven Contract Testing (CDC)

**Source:** Engineering Fundamentals Playbook (Microsoft, code-with-engineering-playbook)
**Author:** Not specified on page
**Organization:** Microsoft (ISE Engineering)
**Last update:** August 22, 2024

---

## Consumer-Driven Contract Testing (CDC)

Consumer-driven Contract Testing (or CDC for short) is a software testing methodology used to test components of a system in isolation while ensuring that provider components are compatible with the expectations that consumer components have of them.

### Why Consumer-Driven Contract Testing

CDC tries to overcome the several painful drawbacks of automated E2E tests with components interacting together:

- E2E tests are slow
- E2E tests break easily
- E2E tests are expensive and hard to maintain
- E2E tests of larger systems may be hard or impossible to run outside a dedicated testing environment

Although testing best practices suggest to write just a few E2E tests compared to the cheaper, faster and more stable integration and unit tests as pictured in the testing pyramid, experience shows many teams end up writing too many E2E tests. A reason for this is that E2E tests give developers the highest confidence to release as they are testing the "real" system.

CDC addresses these issues by testing interactions between components in isolation using mocks that conform to a shared understanding documented in a "contract". Contracts are agreed between consumer and provider, and are regularly verified against a real instance of the provider component. This effectively partitions a larger system into smaller pieces that can be tested individually in isolation of each other, leading to simpler, fast and stable tests that also give confidence to release.

Some E2E tests are still required to verify the system as a whole when deployed in the real environment, but most functional interactions between components can be covered with CDC tests.

CDC testing was initially developed for testing RESTful API's, but the pattern scales to all consumer-provider systems and tooling for other messaging protocols besides HTTP does exist.

### Consumer-Driven Contract Testing Design Blocks

In a consumer-driven approach the consumer drives changes to contracts between a consumer (the client) and a provider (the server). This may sound counterintuitive, but it helps providers create APIs that fit the real requirements of the consumers rather than trying to guess these in advance. The CDC building blocks ordered by their occurrence in the development cycle:

#### Consumer Tests with Provider Mock

The consumers start by creating integration tests against a provider mock and running them as part of their CI pipeline. Expected responses are defined in the provider mock for requests fired from the tests. Through this, the consumer essentially defines the contract they expect the provider to fulfill.

#### Contract

Contracts are generated from the expectations defined in the provider mock as a result of a successful test run. CDC frameworks like Pact provide a specification for contracts in json format consisting of the list of request/responses generated from the consumer tests plus some additional metadata.

Contracts are not a replacement for a discussion between the consumer and provider team. This is the moment where this discussion should take place (if not already done before). The consumer tests and generated contract are refined with the feedback and cooperation of the provider team. Lastly the finalized contract is versioned and stored in a central place accessible by both consumer and provider.

Contracts are complementary to API specification documents like OpenAPI. API specifications describe the structure and the format of the API. A contract instead specifies that for a given request, a given response is expected. An API specifications document is helpful in writing an API contract and can be used to validate that the contract conforms to the API specification.

#### Provider Contract Verification

On the provider side tests are also executed as part of a separate pipeline which verifies contracts against real responses of the provider. Contract verification fails if real responses differ from the expected responses as specified in the contract. The cause of this can be:

1. Invalid expectations on the consumer side leading to incompatibility with the current provider implementation
2. Broken provider implementation due to some missing functionality or a regression

Either way, thanks to CDC it is easy to pinpoint integration issues down to the consumer/provider of the affected interaction. This is a big advantage compared to the debugging pain this could have been with an E2E test approach.

### CDC Testing Frameworks and Tools

- **Pact** — an implementation of CDC testing that allows mocking of responses in the consumer codebase, and verification of the interactions in the provider codebase, while defining a specification for contracts. Originally written in Ruby but has available wrappers for multiple languages. Pact is the de-facto standard to use when working with CDC.
- **Spring Cloud Contract** — an implementation of CDC testing from Spring, and offers easy integration in the Spring ecosystem. Support for non-Spring and non-JVM providers and consumers also exists.

### Conclusion

CDC has several benefits that make it an approach worth considering when dealing with systems composed of multiple components interacting together.

Maintenance efforts can be reduced by testing consumer-provider interactions in isolation without the need of a complex integrated environment, specially as the interactions between components grow in number and become more complex.

Additionally, a close collaboration between consumer and provider teams is strongly encouraged through the CDC development process, which can bring many other benefits. Contracts offer a formal way to document the shared understanding how components interact with each other, and serve as a base for the communication between teams. In a way, the contract repository serves as a live documentation of all consumer-provider interactions of a system.

CDC has some drawbacks as well. An extra layer of testing is added requiring a proper investment in education for team members to understand and use CDC correctly.

Additionally, the CDC test scope should be considered carefully to prevent blurring CDC with other higher level functional testing layers. Contract tests are not the place to verify internal business logic and correctness of the consumer.

### Resources

- Testing pyramid from Kent C. Dodd's blog
- Pact, a code-first consumer-driven contract testing tool with support for several different programming languages
- Consumer-driven contracts from Ian Robinson
- Contract test from Martin Fowler
- A simple example of using Pact consumer-driven contract testing in a Java client-server application
- Pact dotnet workshop

</section>
</details>

<details>
<summary>译文</summary>
<section>

# 消费者驱动契约测试（CDC）

**来源：** 工程基础手册（Microsoft，code-with-engineering-playbook）
**作者：** 页面未注明
**组织：** Microsoft（ISE Engineering）
**最后更新：** 2024 年 8 月 22 日

---

## 消费者驱动契约测试（CDC）

消费者驱动契约测试（Consumer-Driven Contract Testing，简称 CDC）是一种软件测试方法论，用于在隔离状态下测试系统的各个组件，同时确保提供方（Provider）组件与消费方（Consumer）组件对它们的期望相兼容。

### 为什么需要消费者驱动契约测试

CDC 试图克服组件相互交互的自动化端到端（E2E）测试所带来的若干痛苦缺陷：

- E2E 测试速度慢
- E2E 测试容易失败
- E2E 测试昂贵且难以维护
- 较大系统的 E2E 测试可能难以或无法在专用测试环境之外运行

尽管测试最佳实践建议，如测试金字塔所示，与更便宜、更快、更稳定的集成测试和单元测试相比，只编写少量 E2E 测试，但经验表明，许多团队最终编写了过多的 E2E 测试。原因之一是 E2E 测试测试的是“真实”系统，因此能给开发人员最高的发布信心。

CDC 通过使用符合“契约”中记录的共享理解的 Mock，在隔离状态下测试组件之间的交互，从而解决这些问题。契约由消费方和提供方共同商定，并定期针对提供方组件的真实实例进行验证。这有效地将较大的系统划分为更小的部分，这些部分可以彼此隔离地单独测试，从而产生更简单、快速、稳定的测试，同时也能带来发布信心。

仍然需要一些 E2E 测试来验证部署在真实环境中的系统整体，但组件之间的大多数功能交互都可以用 CDC 测试来覆盖。

CDC 测试最初是为测试 RESTful API 而开发的，但该模式可扩展到所有消费方-提供方系统，并且除了 HTTP 之外，其他消息传递协议的工具也确实存在。

### 消费者驱动契约测试的设计构件

在消费者驱动的方法中，消费方驱动消费方（客户端）与提供方（服务器）之间契约的变更。这听起来可能违反直觉，但它有助于提供方创建符合消费方真实需求的 API，而不是试图提前猜测这些需求。CDC 构件按其在开发周期中出现的顺序排列：

#### 带提供方 Mock 的消费方测试

消费方首先针对提供方 Mock 创建集成测试，并将其作为 CI 流水线的一部分运行。在提供方 Mock 中为测试发出的请求定义预期响应。通过这种方式，消费方实质上定义了他们期望提供方履行的契约。

#### 契约

契约是在测试成功运行后，从提供方 Mock 中定义的期望生成的。像 Pact 这样的 CDC 框架提供了 JSON 格式的契约规范，包含从消费方测试生成的请求/响应列表以及一些额外的元数据。

契约不能替代消费方和提供方团队之间的讨论。这是应该进行这种讨论的时刻（如果之前还没有进行过的话）。消费方测试和生成的契约会根据提供方团队的反馈和合作进行完善。最后，最终确定的契约会被版本化，并存储在消费方和提供方都可访问的中心位置。

契约与 OpenAPI 等 API 规范文档是互补的。API 规范描述 API 的结构和格式。而契约则规定，对于给定的请求，期望得到给定的响应。API 规范文档有助于编写 API 契约，并可用于验证契约是否符合 API 规范。

#### 提供方契约验证

在提供方一侧，测试也作为独立流水线的一部分执行，该流水线针对提供方的真实响应验证契约。如果真实响应与契约中规定的预期响应不同，契约验证就会失败。其原因可能是：

1. 消费方一侧的期望无效，导致与当前提供方实现不兼容
2. 提供方实现因某些功能缺失或回归而损坏

无论哪种情况，得益于 CDC，都可以轻松地将集成问题定位到受影响交互的消费方/提供方。与 E2E 测试方法可能带来的调试痛苦相比，这是一个巨大的优势。

### CDC 测试框架和工具

- **Pact** —— 一种 CDC 测试实现，允许在消费方代码库中 Mock 响应，在提供方代码库中验证交互，同时定义契约规范。最初用 Ruby 编写，但有多种语言的封装。Pact 是使用 CDC 时的事实标准。
- **Spring Cloud Contract** —— 来自 Spring 的 CDC 测试实现，在 Spring 生态系统中提供轻松集成。也支持非 Spring 和非 JVM 的提供方和消费方。

### 结论

CDC 有几个好处，使其成为处理由多个相互交互的组件组成的系统时值得考虑的方法。

通过在隔离状态下测试消费方-提供方交互，无需复杂的集成环境，可以降低维护工作量，尤其是当组件之间的交互数量增长并变得更加复杂时。

此外，CDC 开发过程强烈鼓励消费方和提供方团队之间的密切协作，这可以带来许多其他好处。契约提供了一种正式的方式来记录组件之间如何交互的共享理解，并作为团队之间沟通的基础。在某种程度上，契约仓库充当了系统所有消费方-提供方交互的活文档。

CDC 也有一些缺点。增加了一层额外的测试，需要适当投资于团队成员的教育，以正确理解和使用 CDC。

此外，应仔细考虑 CDC 测试范围，以防止 CDC 与其他更高层次的功能测试层混淆。契约测试不是验证消费方内部业务逻辑和正确性的地方。

### 资源

- Kent C. Dodd 博客中的测试金字塔
- Pact，一种代码优先的消费者驱动契约测试工具，支持多种编程语言
- Ian Robinson 的消费者驱动契约
- Martin Fowler 的契约测试
- 在 Java 客户端-服务器应用中使用 Pact 消费者驱动契约测试的简单示例
- Pact dotnet workshop

</section>
</details>

## 摘要

本文是 Microsoft 工程基础手册（Engineering Fundamentals Playbook）中关于消费者驱动契约测试（CDC）的入门指南。文章指出，传统端到端（E2E）测试存在速度慢、易失败、昂贵难维护等痛点，而 CDC 通过“契约”这一共享理解，在隔离状态下用 Mock 测试组件间交互，从而将大系统拆分为可独立测试的小块，兼顾测试的稳定性与发布信心。文章系统介绍了 CDC 的三大设计构件——带提供方 Mock 的消费方测试、契约的生成与版本化、提供方契约验证，并对比了 Pact 与 Spring Cloud Contract 两大主流工具。文章强调契约与 OpenAPI 规范互补、契约不能替代团队沟通，同时提醒 CDC 存在学习成本与测试范围边界问题。作为官方工程实践手册，本文定位为方法论入门，权威性高但深度有限，适合作为团队引入 CDC 的起点。

## 术语表

| 术语 | 全称 | 解释 |
| :--- | :--- | :--- |
| Consumer-Driven Contract Testing（CDC） | Consumer-Driven Contract Testing | 消费者驱动契约测试，一种面向服务（尤其微服务）的集成测试方法，核心是由消费者定义并驱动契约，而非由提供者单方面规定。消费者用 Mock 记录实际依赖的请求与响应，汇总成契约后由提供者据此验证实现。该模式由 Martin Fowler 与 Ian Robinson 于 2006 年提出。 |
| End-to-End（E2E）Testing | End-to-End Testing | 端到端测试，从用户视角让整个系统（含所有真实依赖）整体运行，验证完整业务流程。位于测试金字塔顶端，数量最少、最慢、最脆弱，CDC 正是为减少对其依赖而出现。 |
| Testing Pyramid | Test Automation Pyramid | 测试金字塔，由 Mike Cohn 在 2009 年著作《Succeeding with Agile》中提出的分层模型，主张底层单元测试最多最快，顶层 E2E 测试最少最慢。契约测试通常定位在中间的服务/集成层。 |
| Unit Tests / Integration Tests | Unit Tests / Integration Tests | 单元测试针对最小可测试单元在隔离环境验证行为；集成测试验证多组件协作。契约测试是一种特殊集成测试，在“隔离”与“集成”间取得平衡。 |
| Contract | Contract（软件测试语境） | 契约，指两个系统间关于交互方式的明确约定，如请求路径、方法、参数及对应响应。Martin Fowler 将其描述为“对服务交互期望的封装”，是 CDC 的核心产物。 |
| Provider Mock | Provider Mock | 提供者模拟，消费者侧契约测试中替代真实提供者的测试替身。消费者让 Mock 返回预设响应，在隔离环境验证客户端代码，Pact 据此记录请求与期望响应并生成契约。 |
| CI Pipeline | Continuous Integration Pipeline | 持续集成流水线，代码提交后自动触发的构建与测试步骤。是契约测试落地的关键载体：消费者侧生成并发布契约，提供者侧拉取契约执行验证。 |
| Pact | Pact（非缩写） | 代码优先的契约测试工具，CDC 领域事实上的标准工具。消费者侧用 Mock 生成契约文件，提供者侧重放请求比对响应。支持 Ruby、JS、JVM、Go、.NET、Python 等语言，配套 Pact Broker 管理契约。 |
| RESTful API | Representational State Transfer API | REST 风格 API，遵循 Roy Fielding 2000 年博士论文提出的 REST 架构约束，以资源为中心、通过 HTTP 方法操作资源。是 CDC 最常见的契约测试对象。 |
| OpenAPI | OpenAPI Specification（OAS） | 与语言无关的 HTTP API 接口描述标准，前身为 Swagger 2.0，由 OpenAPI Initiative 维护。描述提供者“文档化”的完整契约，与 CDC 关注的“实际使用”契约互补。 |
| Spring Cloud Contract | Spring Cloud Contract | Spring 生态中实现契约测试的框架，前身为 Codearte 的 Accurest。契约通常由提供者侧编写，构建时生成验证测试并产出 WireMock 桩，深度集成 Spring 技术栈。 |
| Spring Ecosystem / JVM | Spring Ecosystem / Java Virtual Machine | JVM 是运行 Java 字节码的虚拟机，也是 Kotlin、Groovy、Scala 的运行平台；Spring 生态是构建于 JVM 之上的企业级开发框架体系。Spring Cloud Contract 正是为 JVM/Spring 技术栈定制的方案。 |

## 深度解读

### 核心论点与论证逻辑

文章的核心论点是：**CDC 是替代过度依赖 E2E 测试的更优方案**。其论证逻辑清晰且层层递进——先指出 E2E 测试的四大痛点（慢、易碎、昂贵、环境依赖），再解释为何团队仍倾向写过多 E2E 测试（因为测试“真实”系统带来最高发布信心），最后提出 CDC 通过“契约 + Mock + 隔离测试”在保留发布信心的同时规避 E2E 的缺陷。

这一论证的力度在于抓住了问题的本质：E2E 测试之所以被滥用，是因为它提供了其他测试层级无法提供的“集成信心”。CDC 的巧妙之处在于，它把这种信心从“运行整个真实系统”转移到了“验证契约是否被满足”上，从而在成本与信心之间找到了新的平衡点。文章用“将大系统划分为可独立测试的小块”这一比喻，准确传达了 CDC 的核心价值。

不过，文章对“CDC 能带来发布信心”的论证略显简略，未深入说明契约测试为何能提供与 E2E 相当的信心——这实际上依赖于“契约忠实反映了消费者真实使用方式”这一前提，而该前提的成立又依赖于消费者测试的质量。

### 技术原理：CDC 的工作机制

CDC 的运作可概括为“**消费者定义期望 → 生成契约 → 提供者验证契约**”的三步闭环，对应文章所述的三大设计构件：

1. **带提供方 Mock 的消费方测试**：消费者在 CI 流水线中针对 Mock 编写集成测试，Mock 返回预设响应。这一步的关键在于，消费者“实质上定义了他们期望提供方履行的契约”——契约不是凭空设计，而是从消费者真实代码中“长”出来的。
2. **契约的生成与版本化**：测试成功后，Pact 等框架自动生成 JSON 格式的契约，包含请求/响应列表与元数据。文章特别强调契约“不能替代团队讨论”，契约应经双方协商后版本化存储于中心位置。
3. **提供方契约验证**：提供方在独立流水线中针对真实响应重放契约，若响应不符则验证失败，从而精确定位是消费者期望错误还是提供方实现回归。

这一机制的精髓在于**“消费者驱动”**：由消费者（而非提供者）定义契约，看似反直觉，实则让提供方 API 贴合真实需求，避免“提前猜测”。这与 Ian Robinson 2006 年奠基文章的核心思想一脉相承——契约应由消费者的期望汇聚而成，而非由提供者单方面规定。

### 背景与语境：从 SOA 到微服务的契约测试演进

理解本文需要把握 CDC 的历史脉络。消费者驱动契约这一**概念**最早由 ThoughtWorks 的 Ian Robinson 于 2006 年在 martinfowler.com 发表的文章《Consumer-Driven Contracts: A Service Evolution Pattern》中提出，彼时语境是 SOA 与 XML Schema、WS-Policy，而非 RESTful API。而 CDC 的**主流工具** Pact 则诞生于 2013 年，由 realestate.com.au（REA）团队为 Ruby 微服务架构开发，此时才真正进入 RESTful 微服务语境。

这一时间差揭示了一个值得注意的事实：文章声称“CDC 测试最初是为测试 RESTful API 而开发的”，实际上混淆了概念与工具两个层面（详见“真实性评估”）。CDC 概念源于 SOA 时代，而 Pact 工具才真正面向 RESTful 微服务。这一演进轨迹也解释了为何 CDC 在微服务浪潮中重新流行——微服务将单体拆分为大量相互依赖的服务，使服务间契约的显式化、可验证化成为刚需。ThoughtWorks 技术雷达在 2016 年将消费者驱动契约测试列为“Adopt（采纳）”级别，标志着其从边缘实践走向主流。

### 实践指导价值

对工程团队而言，本文的实践价值主要体现在三点：

**其一，提供了清晰的落地路径。** 文章按开发周期顺序列出三大构件，读者可据此搭建 CDC 流水线：消费者侧用 Pact 生成契约并发布到 Pact Broker，提供者侧拉取契约执行验证。文章末尾的 Resources 提供了 Pact 官方 workshop（Java、.NET 等）作为上手入口。

**其二，划定了 CDC 的边界。** 文章明确提醒两点：契约测试“不是验证消费方内部业务逻辑和正确性的地方”，且应防止 CDC 与更高层功能测试混淆。这避免了团队将契约测试误用为万能测试的常见陷阱。

**其三，强调了契约的“社会属性”。** 文章反复强调契约不能替代团队沟通，契约仓库是“活文档”。这提醒读者：CDC 不仅是技术工具，更是一种促进消费方与提供方协作的组织实践。

### 争议与局限

文章对 CDC 的局限着墨不多，但结合业界讨论，存在以下值得注意的争议点：

**其一，CDC 的额外成本。** 文章承认 CDC“增加了一层额外的测试”，需要教育投入。实践中，契约测试的维护成本（契约版本管理、Broker 运维、跨团队协调）可能被低估，尤其当消费者数量众多时，契约的并集管理会变得复杂。

**其二，契约测试的“信心”边界。** 契约测试验证的是“接口兼容性”，而非“业务正确性”。即使契约全部通过，仍可能存在契约未覆盖的集成问题（如数据语义、性能、并发），因此文章也承认“仍需要一些 E2E 测试”。

**其三，工具选择的权衡。** 文章并列介绍 Pact 与 Spring Cloud Contract，但未深入对比。实际上两者理念有差异：Pact 是纯消费者驱动，契约由消费者生成；Spring Cloud Contract 则支持消费者驱动与生产者驱动两种模式，契约常由提供者侧编写。团队需根据技术栈与协作模式选择。

### 真实性评估

| 声明/事实 | 验证状态 | 说明 |
| :--- | :--- | :--- |
| CDC 测试最初是为测试 RESTful API 而开发的 | 存疑 | 混淆了概念与工具：CDC 概念源于 2006 年 Ian Robinson 的 SOA/XML 语境文章，未涉及 RESTful API；而 Pact 工具（2013 年）才真正面向 RESTful 微服务。 |
| Pact 最初用 Ruby 编写，有多种语言封装 | 已验证 | Pact 官方历史文档确认其 2013 年由 REA 团队用 Ruby 编写，后经 pact-jvm 扩展至 Java，最终演化为 Rust 参考实现 + FFI 的多语言封装。 |
| Pact 是使用 CDC 时的事实标准 | 部分验证 | Pact 官网未自称“事实标准”，该措辞属主观评价；但 Pact 确为 CDC 领域最流行、社区最活跃的工具，业界广泛引用此说法。 |
| Spring Cloud Contract 是 Spring 出品的 CDC 实现 | 已验证 | Spring 官方文档确认其为 Spring Cloud 生态项目，前身为 Codearte 的 Accurest，支持消费者驱动与生产者驱动契约测试。 |
| 测试金字塔概念（文中引用 Kent C. Dodd 博客） | 已验证 | 测试金字塔由 Mike Cohn 在 2009 年《Succeeding with Agile》中提出；文中“Kent C. Dodd”为拼写错误，正确为 Kent C. Dodds。 |
| CDC 核心思想：消费者定义契约、提供者验证契约 | 已验证 | 与 Ian Robinson 奠基文章核心观点一致：契约应由消费者期望汇聚而成，而非提供者单方面规定。 |

### 总结

本文作为 Microsoft 官方工程实践手册的入门指南，以清晰的结构和准确的定位，为读者提供了理解与落地 CDC 的可靠起点。其核心价值在于：用“契约”这一概念，将服务间隐式的集成耦合显式化、可验证化，从而在测试成本与发布信心之间找到平衡。文章权威性高（官方手册 + 引用 Fowler、Robinson 等奠基者文献），但深度有限，且存在一处事实表述不严谨（CDC 起源的表述混淆了概念与工具）。总体而言，本文适合作为团队引入 CDC 的入门读物，深入实践仍需结合 Pact 官方文档与 workshop。

**关键要点：**

- CDC 通过“消费者定义契约 → 生成契约 → 提供者验证契约”的闭环，在隔离状态下验证服务间兼容性，替代过度依赖的 E2E 测试。
- 契约是 CDC 的核心产物，由消费者测试自动生成，与 OpenAPI 规范互补而非对立，且不能替代团队沟通。
- Pact 与 Spring Cloud Contract 是两大主流工具，前者纯消费者驱动，后者支持双模式且深度集成 Spring 生态。
- 文章存在一处事实不严谨：CDC 概念源于 2006 年 SOA 语境，而非“最初为 RESTful API 开发”；后者实为 Pact 工具（2013 年）的语境。
- CDC 有额外学习成本与测试范围边界，契约测试验证接口兼容性而非业务正确性，仍需少量 E2E 测试兜底。

## 参考资料

- [Consumer-Driven Contracts: A Service Evolution Pattern（martinfowler.com）](https://martinfowler.com/articles/consumerDrivenContracts.html) — Ian Robinson 与 Martin Fowler 合著的 CDC 奠基文章，是理解 CDC 概念源头的权威文献。
- [Martin Fowler：Contract Test bliki](https://martinfowler.com/bliki/ContractTest.html) — 契约测试术语的权威定义，区分了提供者契约、消费者契约与消费者驱动契约。
- [Martin Fowler：Test Pyramid](https://martinfowler.com/bliki/TestPyramid.html) — 测试金字塔概念的权威考证，确认其由 Mike Cohn 提出。
- [Pact 官方文档：Introduction](https://docs.pact.io/) — Pact 框架的官方说明，CDC 领域事实标准工具。
- [Pact 官方文档：History](https://docs.pact.io/history) — 记载 Pact 的起源（2013 年 Ruby）与演进，用于核验文章事实。
- [Spring Cloud Contract Reference Documentation](https://docs.spring.io/spring-cloud-contract/reference/) — Spring Cloud Contract 官方文档，确认其出处与双模式支持。
- [ThoughtWorks Technology Radar：Consumer-driven contract testing](https://www.thoughtworks.com/en-us/radar/techniques/consumer-driven-contract-testing) — 佐证 CDC 在业界的采纳程度。
- [Kent C. Dodds：Write tests. Not too many. Mostly integration.](https://kentcdodds.com/blog/write-tests) — 文章 Resources 中引用的测试金字塔博客（原文拼写有误，正确为 Kent C. Dodds）。
- [OpenAPI Specification](https://spec.openapis.org/oas/latest) — OpenAPI 规范的官方说明，用于解释契约与 API 规范的关系。
