# 深度解读：Fault Injection Testing（故障注入测试）

> 原文：[Fault Injection Testing](https://microsoft.github.io/code-with-engineering-playbook/automated-testing/fault-injection-testing/)<br>
> 作者：Microsoft ISE Engineering Fundamentals（机构署名，无个人作者）<br>
> 日期：2026-08-19 18:08

> 注：本文为机构署名文档（Microsoft ISE Engineering Fundamentals），页面未标注个人作者，故省略【作者介绍】一节。

## 原文及译文

<details>
<summary>原文</summary>
<section>

# Fault Injection Testing

**Source:** Microsoft Engineering Fundamentals Playbook (ISE Engineering Fundamentals)
**Last updated:** August 22, 2024
**Author:** Not specified on page

Fault injection testing deliberately introduces errors and faults into a system to validate and harden its [stability and reliability](../../non-functional-requirements/reliability/). The goal is to improve the system's design for resiliency and performance under intermittent failure conditions over time.

## When To Use

### Problem Addressed

Systems must be resilient to conditions that cause production disruptions. Modern applications depend on infrastructure, platform, network, third-party software, and APIs, which increases the risk of impact from dependency disruptions. Each dependent component may fail, and its interactions with other components may propagate the failure.

Fault injection methods increase coverage and validate software robustness and error handling at build-time or run-time, with the intention of "embracing failure" as part of the development lifecycle. These methods help engineering teams design and continuously validate for failure, accounting for known and unknown failure conditions, architecting for redundancy, and employing retry and back-off mechanisms.

### Applicable to

- **Software** — Error handling code paths, in-process memory management.
  - *Example tests:* Edge-case unit/integration tests and/or [load tests](../performance-testing/load-testing/) (i.e., stress and soak).
- **Protocol** — Vulnerabilities in communication interfaces such as command line parameters or APIs.
  - *Example tests:* [Fuzzing](https://owasp.org/www-community/Fuzzing) provides invalid, unexpected, or random data as input to assess the protocol stability of a component.
- **Infrastructure** — Outages, networking issues, hardware failures.
  - *Example tests:* Causing faults in underlying infrastructure, such as shutting down VM instances, crashing processes, expiring certificates, or introducing network latency. This level of testing relies on statistical metric observations over time and measuring deviations in observed behavior during fault, or its recovery time.

## How to Use

### Architecture

#### Terminology

- **Fault** — The adjudged or hypothesized cause of an error.
- **Error** — That part of the system state that may cause a subsequent failure.
- **Failure** — An event that occurs when the delivered service deviates from correct state.
- **Fault-Error-Failure cycle** — A key mechanism in [dependability](https://en.wikipedia.org/wiki/Dependability): A fault may cause an error. An error may cause further errors within the system boundary; therefore each new error acts as a fault. When error states are observed at the system boundary, they are termed failures.

#### Fault Injection Testing Basics

Fault injection is an advanced testing form where the system is subjected to different [failure modes](https://en.wikipedia.org/wiki/Failure_mode_and_effects_analysis). The testing engineer may know the expected outcome in advance (as in release validation tests), or use it as an exploration to find potential issues in the product that should be mitigated.

#### Fault Injection and Chaos Engineering

Fault injection testing is a specific approach that introduces a failure into a system to validate its robustness. Chaos engineering, coined by Netflix, is a practice for generating new information. The terms overlap in concerns and often in tooling; chaos engineering frequently uses fault injection to introduce the required effects into the system.

### High-level Step-by-Step

#### Fault Injection Testing in the Development Cycle

Fault injection is an effective way to find security bugs in software. The [Microsoft Security Development Lifecycle](https://www.microsoft.com/en-us/securityengineering/sdl/practices) requires fuzzing at every untrusted interface of every product, plus penetration testing that introduces faults to uncover potential vulnerabilities from coding errors, system configuration faults, or operational deployment weaknesses.

Automated fault injection coverage in a CI pipeline promotes a [Shift-Left](https://en.wikipedia.org/wiki/Shift-left_testing) approach of testing earlier in the lifecycle. Examples during the development lifecycle:

- Using fuzzing tools in CI.
- Executing existing end-to-end scenario tests (integration or stress tests) augmented with fault injection.
- Writing regression and acceptance tests based on issues found and fixed, or on resolved service incidents.
- Ad-hoc (manual) fault validations in the dev environment for new features.

#### Fault Injection Testing in the Release Cycle

Like [Synthetic Monitoring Tests](../synthetic-monitoring-tests/), fault injection in the release cycle is part of the [Shift-Right testing](https://learn.microsoft.com/en-us/devops/deliver/shift-right-test-production) approach, using safe methods to test in production or pre-production environments. Distributed cloud applications are very difficult to simulate outside production, so testers are encouraged to run tests on a live system with customer traffic.

Fault injection tests rely on metrics observability and are usually statistical. High-level steps for practicing fault injection and chaos engineering:

- Measure and define a steady (healthy) state for the system's interoperability.
- Create hypotheses based on predicted behavior when a fault is introduced.
- Introduce real-world fault-events to the system.
- Measure the state and compare it to the baseline state.
- Document the process and the observations.
- Identify and act on the result.

#### Fault Injection Testing in Kubernetes

As Kubernetes (k8s) becomes the infrastructure platform, fault injection testing in k8s is essential to ensure reliable behavior during faults or failures. Clusters run diverse workloads (microservices, web apps, scheduled jobs) written in different languages, so fault injection must work across all workload types. K8s clusters are managed differently from traditional infrastructure, so tools must be compatible with k8s. Required characteristics:

- Ease of injecting fault into kubernetes pods.
- Support for faster tool installation within the cluster.
- Support for YAML based configurations which works well with kubernetes.
- Ease of customization to add custom resources.
- Support for workflows to deploy various workloads and faults.
- Ease of maintainability of the tool.
- Ease of integration with telemetry.

## Best Practices and Advice

Production testing runs against a live system with real user traffic, building confidence in graceful error handling — but it risks customer pain if a test fails. Considering the **Blast Radius** of a failed test beforehand is a crucial step. Practices to minimize risk:

- Run tests in a non-production environment first, using synthetic workload, before risking customer traffic.
- Use fault injection as gates in different stages through the CD pipeline.
- Deploy and test on Blue/Green and Canary deployments. Use traffic shadowing (a.k.a. [Dark Traffic](https://cloud.google.com/blog/products/gcp/cre-life-lessons-what-is-a-dark-launch-and-what-does-it-do-for-me)) to get customer traffic to the staging slot.
- Balance collecting actual result data while affecting as few production users as possible.
- Use defensive design principles such as circuit breaking and the bulkhead patterns.
- Agree on a budget (in terms of Service Level Objective (SLO)) as an investment in chaos and fault injection.
- Grow the risk incrementally — start with hardening the core and expand out in layers, locking in progress with automated regression tests.

## Fault Injection Testing Frameworks and Tools

### Fuzzing

- [OneFuzz](https://github.com/microsoft/onefuzz) — Microsoft open-source, self-hosted fuzzing-as-a-service platform, easy to integrate into CI pipelines.
- [AFL](https://lcamtuf.coredump.cx/afl/) and [WinAFL](https://github.com/googleprojectzero/winafl) — Popular fuzz tools by Google's Project Zero team, used locally to target binaries on Linux or Windows.
- [WebScarab](https://github.com/OWASP/OWASP-WebScarab) — A web-focused fuzzer owned by OWASP, found in [Kali Linux](https://tools.kali.org/web-applications/webscarab) distributions.

### Chaos

- [Azure Chaos Studio](https://learn.microsoft.com/en-US/azure/chaos-studio/chaos-studio-overview) — In-preview tool for orchestrating controlled fault injection experiments on Azure resources.
- [Chaos Toolkit](https://chaostoolkit.org/) — Declarative, modular chaos platform with many extensions, including the [Azure actions and probes kit](https://github.com/chaostoolkit-incubator/chaostoolkit-azure).
- [Kraken](https://github.com/openshift-scale/kraken) — OpenShift-specific chaos tool, maintained by Red Hat.
- [Chaos Monkey](https://github.com/netflix/chaosmonkey) — The Netflix platform that popularized chaos engineering (doesn't support Azure out of the box).
- [Simmy](https://github.com/Polly-Contrib/Simmy) — .NET library for chaos testing and fault injection, integrated with the [Polly](https://github.com/App-vNext/Polly) resilience library.
- [Litmus](https://github.com/litmuschaos/litmus) — CNCF open-source tool for chaos testing and fault injection in Kubernetes clusters.
- [This ISE dev blog post](https://devblogs.microsoft.com/ise/build-test-resilience-dotnet-functions/) provides code snippets for using Polly and Simmy to implement a hypothesis-driven approach to resilience and chaos testing.

## Conclusion

From the principles of chaos: "The harder it is to disrupt the steady-state, the more confidence we have in the behavior of the system." If a weakness is uncovered, it becomes a target for improvement before that behavior manifests in the system at large.

Fault injection techniques increase resilience and confidence in shipped products and are used across the industry to validate applications and platforms before and during delivery. Fault injection is powerful and should be used with caution. The [Cloudflare 30-minute global outage](https://blog.cloudflare.com/cloudflare-outage/) — caused by deploying code meant to be "dark launched" — highlights the importance of curtailing the blast radius during experiments.

## Resources

- [Mark Russinovich's fault injection and chaos engineering blog post](https://azure.microsoft.com/en-au/blog/advancing-resilience-through-chaos-engineering-and-fault-injection/)
- [Cindy Sridharan's Testing in production blog post](https://medium.com/@copyconstruct/testing-in-production-the-safe-way-18ca102d0ef1)
- [Cindy Sridharan's Testing in production blog post cont.](https://medium.com/@copyconstruct/testing-in-production-the-hard-parts-3f06cefaf592)
- [Fault injection in Azure Search](https://azure.microsoft.com/es-es/blog/inside-azure-search-chaos-engineering/)
- [Azure Architecture Framework — Chaos engineering](https://learn.microsoft.com/en-us/azure/architecture/framework/resiliency/chaos-engineering)
- [Azure Architecture Framework — Testing resilience](https://learn.microsoft.com/en-us/azure/architecture/framework/resiliency/testing)
- [Landscape of Software Failure Cause Models](https://www.researchgate.net/publication/301839557_The_landscape_of_software_failure_cause_models)

</section>
</details>

<details>
<summary>译文</summary>
<section>

# 故障注入测试（Fault Injection Testing）

**来源：** Microsoft 工程基础手册（ISE Engineering Fundamentals）
**最后更新：** 2024 年 8 月 22 日
**作者：** 页面未标注

故障注入测试通过故意向系统引入错误和故障，来验证并强化其[稳定性与可靠性](../../non-functional-requirements/reliability/)。其目标是在间歇性故障条件下，持续改进系统在弹性（Resiliency）和性能方面的设计。

## 何时使用

### 解决的问题

系统必须能够抵御导致生产环境中断的各种状况。现代应用依赖基础设施、平台、网络、第三方软件和 API，这增加了依赖中断带来影响的风险。每个依赖组件都可能发生故障，而它与其他组件的交互又可能将故障传播开来。

故障注入方法在构建期或运行期扩大测试覆盖范围，验证软件的健壮性和错误处理能力，其意图是将“拥抱失败（Embracing Failure）”作为开发生命周期的一部分。这些方法帮助工程团队为故障进行设计和持续验证，兼顾已知和未知的故障条件，为冗余进行架构设计，并采用重试（Retry）和退避（Back-off）机制。

### 适用对象

- **软件（Software）** —— 错误处理代码路径、进程内内存管理。
  - *示例测试：* 边界情况的单元/集成测试，和/或[负载测试](../performance-testing/load-testing/)（即压力测试和浸泡测试）。
- **协议（Protocol）** —— 通信接口（如命令行参数或 API）中的漏洞。
  - *示例测试：* [模糊测试（Fuzzing）](https://owasp.org/www-community/Fuzzing)提供无效、意外或随机的数据作为输入，以评估组件的协议稳定性。
- **基础设施（Infrastructure）** —— 宕机、网络问题、硬件故障。
  - *示例测试：* 在底层基础设施中制造故障，例如关闭虚拟机实例、使进程崩溃、使证书过期，或引入网络延迟。这一层级的测试依赖于对统计指标的长期观测，并测量故障期间观测行为的偏差，或其恢复时间。

## 如何使用

### 架构

#### 术语

- **故障（Fault）** —— 被判定或假设为错误的原因。
- **错误（Error）** —— 系统状态中可能导致后续失效的部分。
- **失效（Failure）** —— 当交付的服务偏离正确状态时发生的事件。
- **故障-错误-失效循环（Fault-Error-Failure cycle）** —— [可信性（Dependability）](https://en.wikipedia.org/wiki/Dependability)中的一个关键机制：故障可能导致错误，错误可能在系统边界内引发更多错误，因此每个新错误又充当一个故障。当错误状态在系统边界被观测到时，它们被称为失效。

#### 故障注入测试基础

故障注入是一种高级测试形式，让系统经受不同的[失效模式（Failure Modes）](https://en.wikipedia.org/wiki/Failure_mode_and_effects_analysis)。测试工程师可能事先知道预期结果（如发布验证测试），也可能将其作为一种探索手段，以发现产品中应当被缓解的潜在问题。

#### 故障注入与混沌工程

故障注入测试是一种向系统引入故障以验证其健壮性的具体方法。混沌工程（Chaos Engineering）由 Netflix 提出，是一种生成新信息的实践。这两个术语在关注点和工具上常有重叠；混沌工程经常使用故障注入来向系统引入所需的效果。

### 高层分步指南

#### 开发周期中的故障注入测试

故障注入是发现软件安全漏洞的有效方法。[Microsoft 安全开发生命周期（Security Development Lifecycle，SDL）](https://www.microsoft.com/en-us/securityengineering/sdl/practices)要求在每个产品的每个不受信任接口进行模糊测试，此外还要进行渗透测试，通过引入故障来发现编码错误、系统配置故障或运维部署薄弱环节所导致的潜在漏洞。

在 CI 流水线中实现自动化的故障注入覆盖，有助于推动[左移（Shift-Left）](https://en.wikipedia.org/wiki/Shift-left_testing)的测试方法，即在生命周期更早阶段进行测试。开发生命周期中的示例包括：

- 在 CI 中使用模糊测试工具。
- 执行现有的端到端场景测试（集成或压力测试），并辅以故障注入。
- 基于已发现并修复的问题，或已解决的服务事故，编写回归测试和验收测试。
- 在开发环境中对新功能进行临时（手动）的故障验证。

#### 发布周期中的故障注入测试

与[合成监控测试（Synthetic Monitoring Tests）](../synthetic-monitoring-tests/)类似，发布周期中的故障注入是[右移（Shift-Right）测试](https://learn.microsoft.com/en-us/devops/deliver/shift-right-test-production)方法的一部分，使用安全的方法在生产或预生产环境中进行测试。分布式云应用很难在生产环境之外进行模拟，因此鼓励测试人员在承载客户流量的真实系统上运行测试。

故障注入测试依赖指标可观测性，通常是统计性的。实践故障注入和混沌工程的高层步骤：

- 测量并定义系统互操作性的稳定（健康）状态。
- 基于引入故障时的预测行为创建假设。
- 向系统引入真实世界的故障事件。
- 测量状态并与基线状态进行比较。
- 记录过程和观测结果。
- 识别结果并采取行动。

#### Kubernetes 中的故障注入测试

随着 Kubernetes（k8s）成为基础设施平台，k8s 中的故障注入测试对于确保故障或失效期间的可靠行为至关重要。集群运行着用不同语言编写的多样化工作负载（微服务、Web 应用、定时任务），因此故障注入必须适用于所有工作负载类型。k8s 集群的管理方式与传统基础设施不同，因此工具必须与 k8s 兼容。所需特性包括：

- 易于向 Kubernetes Pod 注入故障。
- 支持在集群内更快地安装工具。
- 支持与 Kubernetes 良好配合的基于 YAML 的配置。
- 易于定制以添加自定义资源。
- 支持部署各种工作负载和故障的工作流。
- 工具易于维护。
- 易于与遥测（Telemetry）集成。

## 最佳实践与建议

生产环境测试针对承载真实用户流量的实时系统运行，能够建立对优雅错误处理的信心——但如果测试失败，则存在损害客户体验的风险。事先考虑失败测试的**爆炸半径（Blast Radius）**是至关重要的一步。最小化风险的实践包括：

- 先在非生产环境使用合成工作负载运行测试，再冒险使用客户流量。
- 在 CD 流水线的不同阶段将故障注入作为门禁（Gate）。
- 在蓝绿（Blue/Green）和金丝雀（Canary）部署上进行部署和测试。使用流量镜像（又称[暗流量（Dark Traffic）](https://cloud.google.com/blog/products/gcp/cre-life-lessons-what-is-a-dark-launch-and-what-does-it-do-for-me)）将客户流量引导到暂存槽位。
- 在收集真实结果数据的同时，尽可能少地影响生产用户。
- 使用防御性设计原则，如熔断（Circuit Breaking）和舱壁（Bulkhead）模式。
- 就预算达成一致（以服务等级目标 SLO 计），作为对混沌和故障注入的投资。
- 逐步增加风险——从强化核心开始，逐层向外扩展，用自动化回归测试锁定进展。

## 故障注入测试框架与工具

### 模糊测试（Fuzzing）

- [OneFuzz](https://github.com/microsoft/onefuzz) —— Microsoft 开源的、自托管的模糊测试即服务（Fuzzing-as-a-Service）平台，易于集成到 CI 流水线。
- [AFL](https://lcamtuf.coredump.cx/afl/) 和 [WinAFL](https://github.com/googleprojectzero/winafl) —— Google Project Zero 团队开发的流行模糊测试工具，用于在本地针对 Linux 或 Windows 上的二进制文件。
- [WebScarab](https://github.com/OWASP/OWASP-WebScarab) —— 由 OWASP 拥有的面向 Web 的模糊测试工具，可在 [Kali Linux](https://tools.kali.org/web-applications/webscarab) 发行版中找到。

### 混沌（Chaos）

- [Azure Chaos Studio](https://learn.microsoft.com/en-US/azure/chaos-studio/chaos-studio-overview) —— 用于在 Azure 资源上编排受控故障注入实验的预览版（In-preview）工具。
- [Chaos Toolkit](https://chaostoolkit.org/) —— 声明式、模块化的混沌平台，拥有众多扩展，包括 [Azure actions and probes kit](https://github.com/chaostoolkit-incubator/chaostoolkit-azure)。
- [Kraken](https://github.com/openshift-scale/kraken) —— 由 Red Hat 维护的 OpenShift 专用混沌工具。
- [Chaos Monkey](https://github.com/netflix/chaosmonkey) —— 使混沌工程流行起来的 Netflix 平台（开箱即用不支持 Azure）。
- [Simmy](https://github.com/Polly-Contrib/Simmy) —— 用于混沌测试和故障注入的 .NET 库，与 [Polly](https://github.com/App-vNext/Polly) 弹性库集成。
- [Litmus](https://github.com/litmuschaos/litmus) —— CNCF 开源的、用于 Kubernetes 集群混沌测试和故障注入的工具。
- [这篇 ISE 开发博客文章](https://devblogs.microsoft.com/ise/build-test-resilience-dotnet-functions/)提供了使用 Polly 和 Simmy 实现假设驱动的弹性和混沌测试方法的代码片段。

## 结论

源自混沌的原则：“稳态越难以被扰乱，我们对系统行为的信心就越强。”如果发现了一个薄弱环节，它就会在该行为大规模显现于系统之前成为改进的目标。

故障注入技术提高了已发布产品的弹性和信心，并在整个行业中被用于在交付前和交付过程中验证应用和平台。故障注入功能强大，应谨慎使用。[Cloudflare 30 分钟全球宕机](https://blog.cloudflare.com/cloudflare-outage/)——由部署本应“暗发布”的代码引起——凸显了在实验期间控制爆炸半径的重要性。

## 资源

- [Mark Russinovich 的故障注入与混沌工程博客文章](https://azure.microsoft.com/en-au/blog/advancing-resilience-through-chaos-engineering-and-fault-injection/)
- [Cindy Sridharan 的《在生产环境测试》博客文章](https://medium.com/@copyconstruct/testing-in-production-the-safe-way-18ca102d0ef1)
- [Cindy Sridharan 的《在生产环境测试》博客文章（续）](https://medium.com/@copyconstruct/testing-in-production-the-hard-parts-3f06cefaf592)
- [Azure Search 中的故障注入](https://azure.microsoft.com/es-es/blog/inside-azure-search-chaos-engineering/)
- [Azure 架构框架 —— 混沌工程](https://learn.microsoft.com/en-us/azure/architecture/framework/resiliency/chaos-engineering)
- [Azure 架构框架 —— 测试弹性](https://learn.microsoft.com/en-us/azure/architecture/framework/resiliency/testing)
- [软件失效原因模型全景](https://www.researchgate.net/publication/301839557_The_landscape_of_software_failure_cause_models)

</section>
</details>

## 摘要

本文是 Microsoft 工程基础手册（Code With Engineering Playbook）中关于“故障注入测试（Fault Injection Testing）”的实践指南，由 ISE（Industry Solutions Engineering）工程基础团队维护，最后更新于 2024 年 8 月 22 日。文章系统阐述了故障注入测试的定义、适用对象（软件、协议、基础设施三个层面）、理论基础（Fault-Error-Failure 循环与可信性 Dependability 概念）、与混沌工程（Chaos Engineering）的关系，以及在开发周期（Shift-Left）和发布周期（Shift-Right）中的落地方法，并特别讨论了 Kubernetes 环境下的工具选型要求。文章还给出了最小化“爆炸半径（Blast Radius）”的最佳实践清单，以及模糊测试（Fuzzing）和混沌（Chaos）两大类工具框架的推荐列表。其核心主张是：通过主动、持续地“拥抱失败”，工程团队能够在故障真正影响用户之前发现并修复系统的薄弱环节，从而提升已发布产品的弹性与信心。

## 术语表

| 术语 | 全称 | 解释 |
| :--- | :--- | :--- |
| Fault / Error / Failure | - | 故障 / 错误 / 失效。源自 Avizienis、Laprie 等人提出的可信计算分类法：Fault（故障）是被判定或假设为错误之“原因”的缺陷；Error（错误）是系统状态中可能导致后续失效的部分；Failure（失效）是交付服务偏离正确状态的事件。三者构成因果链，是故障注入测试的理论基石。 |
| Fault-Error-Failure cycle | - | 故障-错误-失效循环。故障被激活后产生错误，错误在系统内传播并可能引发更多错误（每个新错误又充当故障），当错误状态在系统边界被观测到时即成为失效；而一个系统的失效又会成为上层系统的故障，如此递归。 |
| Dependability | - | 可信性 / 可靠性。Avizienis 与 Laprie 提出的整合性概念，指“交付可被合理信赖的服务的能力”，由威胁（fault/error/failure）、属性（可用性、可靠性、安全性等）与手段（故障预防、容忍、消除、预测）三部分构成。 |
| FMEA | Failure Mode and Effects Analysis | 失效模式与影响分析。一种系统化的主动风险分析方法，依据严重度、发生频度、可检测度三个因素对失效排序（得到风险优先数 RPN），用于在失效发生前加以缓解。 |
| Chaos Engineering | - | 混沌工程。由 Netflix 提出的学科，指“在分布式系统上进行实验，以建立对系统在生产环境中抵御动荡条件之能力的信心”。常使用故障注入来引入所需效果。 |
| Fuzzing | - | 模糊测试。一种自动化测试技术，向程序输入无效、意外或随机数据并监控其是否崩溃或出现异常，主要用于发现安全漏洞。术语由 Barton Miller 教授于 1988 年首创。 |
| Shift-Left / Shift-Right Testing | - | 左移 / 右移测试。左移指将测试提前到开发阶段尽早发现缺陷；右移指在生产环境本身进行测试（如金丝雀发布、混沌工程、可观测性）。两者互补形成反馈闭环。 |
| Blast Radius | - | 爆炸半径。借自军事工程术语，指某组件失效或变更时受影响的服务、用户、系统或组件的集合，用于评估故障影响传播的范围。 |
| Blue/Green / Canary Deployment | - | 蓝绿 / 金丝雀部署。蓝绿部署同时运行两套相同环境实现零停机切换与快速回滚；金丝雀部署将更新逐步发布给一小部分用户再全量发布，以限制爆炸半径。 |
| Dark Traffic / Dark Launch | - | 暗流量 / 暗发布。将新的后端行为部署到生产环境并用真实流量调用，但用户无法察觉其运行，用于在公开宣布前评估负载与性能影响。 |
| Circuit Breaking / Bulkhead | - | 熔断 / 舱壁模式。熔断是状态机（Closed→Open→Half-Open），当下游失败率超阈值时快速失败以避免级联故障；舱壁将资源池分区隔离，防止一个失效依赖耗尽共享容量。 |
| SLO | Service Level Objective | 服务等级目标。由 SLI（服务等级指标）衡量的服务等级目标值，是内部设定的可靠性目标；区别于与用户签订、含违约后果的 SLA。 |
| Synthetic Monitoring Tests | - | 合成监控测试。使用自动化脚本模拟真实用户交互并按固定间隔运行，以主动验证可用性、功能与性能，属于右移测试范畴。 |
| Kubernetes（k8s） | - | Kubernetes。开源的容器编排平台，已成为云原生基础设施的事实标准，故障注入工具需与其工作负载类型和 YAML 配置方式兼容。 |
| CNCF | Cloud Native Computing Foundation | 云原生计算基金会。Linux 基金会旗下的开源基金会，托管 Kubernetes、Litmus 等云原生项目。 |
| SDL | Security Development Lifecycle | 安全开发生命周期。Microsoft 提出的软件开发安全流程，要求在每个产品的每个不受信任接口进行模糊测试。 |

## 深度解读

### 核心论点与论证逻辑

文章的核心主张可以概括为一句话：**故障是不可避免的，因此工程团队应当主动、持续地“拥抱失败（Embracing Failure）”，把故障注入作为开发生命周期的一部分，而非事后补救。** 这一主张建立在一条清晰的因果链上：现代应用依赖基础设施、平台、网络、第三方软件和 API，依赖越多，中断风险越高；而每个依赖组件都可能失效，且失效会通过组件间的交互传播。因此，与其被动等待故障发生，不如主动注入故障来验证系统的健壮性和错误处理能力。

论证逻辑的严谨之处在于，它没有把故障注入测试当作孤立的“测试技巧”，而是将其锚定在可信计算（Dependable Computing）的理论框架之上——即 Avizienis 等人提出的 Fault-Error-Failure 循环。这一理论框架赋予了“故障”“错误”“失效”三个词精确的、可区分的含义，使文章后续关于“在构建期或运行期验证健壮性”的论述有了坚实的学理支撑。同时，文章通过区分“故障注入测试”与“混沌工程”两个易混淆概念（前者是引入故障验证健壮性的具体方法，后者是生成新信息的实践），避免了术语上的含混。

不过，文章的论证也存在一个隐含的张力：它一方面强调故障注入“功能强大”，另一方面又反复警告其风险（“应谨慎使用”“考虑爆炸半径”）。这种张力恰恰是文章最有价值的地方——它没有把故障注入包装成无风险的银弹，而是诚实地指出生产环境测试可能“损害客户体验”，并据此给出了一整套风险控制实践。

### 技术维度：故障注入与混沌工程的关系

文章对“故障注入测试”与“混沌工程”的区分值得深入辨析。按文章的定义，故障注入测试是“向系统引入故障以验证其健壮性的具体方法”，而混沌工程是“由 Netflix 提出、用于生成新信息的实践”。两者的关系是：**混沌工程经常使用故障注入作为手段，但混沌工程的目标更宽——它不只是验证已知的健壮性，而是通过实验生成关于系统行为的新知识。**

这一区分在业界有据可查。Netflix 的混沌工程实践（以 Chaos Monkey 为代表）正是从“故障注入测试（Failure Injection Testing，FIT）”演化而来：Netflix 在 2008 年从数据中心迁移到云端后，实例不稳定事件增多，团队开发了 Chaos Monkey 在生产环境随机终止虚拟机实例，迫使工程师设计出能承受单实例故障的服务。2015 年 Casey Rosenthal 组建正式混沌工程团队，2016 年 Netflix 团队在 IEEE Software 发表论文正式确立该学科。因此，故障注入可以视为混沌工程的“技术底座”，而混沌工程则是在此基础上叠加了“稳态假设”“生产环境实验”“持续自动化”等方法论。

文章还正确地点出了两者的共同方法论骨架——即“测量稳态 → 建立假设 → 注入真实故障 → 对比基线 → 记录并行动”这六步。这与混沌工程社区公认的“混沌工程原则（Principles of Chaos Engineering）”高度一致，说明文章的方法论并非微软自创，而是对业界共识的准确转述。

### 实践维度：Shift-Left 与 Shift-Right 的双向落地

文章最具实操价值的部分，是它把故障注入测试放进了完整的软件交付生命周期，并区分了“开发周期（Shift-Left）”与“发布周期（Shift-Right）”两种落地场景。

在开发周期，故障注入与 Microsoft 安全开发生命周期（SDL）绑定——SDL 要求在每个产品的每个不受信任接口进行模糊测试，并辅以渗透测试。文章给出的四个落地示例（CI 中使用模糊测试工具、端到端场景测试辅以故障注入、基于事故写回归/验收测试、开发环境手动故障验证）覆盖了从自动化到手动、从预防到回归的完整光谱，体现了“左移”的核心思想：在缺陷进入生产前尽早发现。

在发布周期，文章明确将故障注入归入“右移测试”范畴，并给出了一个关键判断：**分布式云应用很难在生产环境之外模拟，因此应鼓励在承载真实客户流量的系统上运行测试。** 这一判断与 Cindy Sridharan 的经典文章《Testing in Production》一脉相承——生产环境拥有测试环境无法复制的真实流量、真实依赖和真实故障模式。但文章同时清醒地指出，生产测试“如果失败则存在损害客户体验的风险”，因此“事先考虑爆炸半径是至关重要的一步”。

这种“左移 + 右移”的双向视角，是文章区别于许多只谈单一测试阶段的资料之处。它隐含的工程哲学是：左移无法复现真实生产条件，右移是被动的（问题发生后才能发现），最强团队应当两者并用，形成“生产事故（右移观察）→ 回归测试（左移门禁）”的反馈闭环。

### 工具生态与现状：部分信息已过时

文章在“故障注入测试框架与工具”一节列出了模糊测试和混沌两大类共 10 余个工具。经交叉核验，**其中若干工具的状态描述已经过时**，这是本文最值得读者注意的时效性问题：

- **Azure Chaos Studio**：文章标注为“In-preview（预览版）”，但该服务已于 **2023 年 11 月 1 日正式发布（GA）**，在 17 个生产区域可用。文章“最后更新于 2024 年 8 月 22 日”的标注与这一事实不符，说明该页面在工具状态上存在滞后。
- **OneFuzz**：文章将其列为 Microsoft 开源的模糊测试平台，但该仓库已于 **2023 年 11 月 1 日归档**，转为只读，官方说明因团队规模不足以同时维护开源版与内部版而停止开源维护。
- **WebScarab**：文章将其列为 OWASP 的 Web 模糊测试工具，但该仓库已于 **2024 年 4 月 4 日归档**，官方推荐改用其继任者 OWASP ZAP。
- **AFL**：原版已归档，活跃继任者是社区驱动的 AFL++；WinAFL 仍在积极维护。
- **Simmy**：自 Polly v8.3.0 起已并入 Polly 核心库，术语由“Monkey”改为“Chaos”，原独立库不再是主要开发方向。
- **Chaos Monkey 对 Azure 的支持**：文章称其“开箱即用不支持 Azure”，经核验，Chaos Monkey 通过 Spinnaker 间接支持 Azure，但官方仅对 AWS、GCE、Kubernetes 做过专门测试，文章的说法基本成立但不够精确。

这一发现提示读者：**在采用文章推荐的工具前，务必核对工具的最新状态**，因为故障注入/混沌工程工具生态迭代极快，归档、合并、GA 是常态。

### 影响与意义：从“测试技巧”到“工程文化”

文章的真正价值，不在于它罗列了多少工具或步骤，而在于它把故障注入测试从一种“测试技巧”提升为一种“工程文化”。文章结尾引用混沌工程的原则——“稳态越难以被扰乱，我们对系统行为的信心就越强”——点明了故障注入的终极目标不是“找到 bug”，而是“建立信心”。

这一视角与 Google SRE 的“错误预算（Error Budget）”理念、以及业界“可靠性是特性（Reliability is a feature）”的共识一脉相承。文章建议“就预算达成一致（以 SLO 计），作为对混沌和故障注入的投资”，实际上是把可靠性工程从“成本中心”重新定位为“投资”——团队应当像投资功能开发一样，为可靠性预留明确的预算和资源。

同时，文章用 Cloudflare 2019 年 7 月 2 日的全球宕机事故作为反面教材，强调“控制爆炸半径”的重要性。这一案例的选择极具说服力：Cloudflare 的宕机正是由一条以“模拟（simulate）”模式（一种暗发布形式）部署的 WAF 规则引发的——该规则中的正则表达式导致灾难性回溯，耗尽全球所有处理 HTTP/HTTPS 流量的 CPU 核心。这个案例的深刻之处在于：**即使是“暗发布”这种本应安全的实验手段，如果爆炸半径失控，也可能酿成全球性事故。** 它印证了文章反复强调的核心教训——故障注入“功能强大，应谨慎使用”。

### 真实性评估

| 声明/事实 | 验证状态 | 说明 |
| :--- | :--- | :--- |
| “Chaos engineering”术语由 Netflix 提出 | 已验证 | 2014 年 InfoQ 报道称该术语“recently coined by Netflix”，2015 年 Netflix 官方博客《Chaos Engineering Upgraded》正式确立该学科，2016 年 IEEE Software 发表同名论文。 |
| Cloudflare 曾发生 30 分钟全球宕机，由暗发布代码引起 | 部分验证 | 官方事后分析给出的宕机时长为约 27 分钟（13:42 至 14:09 UTC），非精确 30 分钟；根因是 WAF 规则的正则表达式灾难性回溯。该规则确实以“simulate”（暗发布）模式部署，但问题在于暗发布模式本身未能阻止故障，而非“本应暗发布却未暗发布”。 |
| Microsoft SDL 要求在每个产品的每个不受信任接口进行 fuzzing | 已验证 | Microsoft Research 官方博客明确表述“Microsoft Security Development Lifecycle requires fuzzing at every untrusted interface of every product”，与声明完全一致。 |
| Mark Russinovich 写过 fault injection 和 chaos engineering 的博客 | 已验证 | Mark Russinovich（Azure CTO）是 2020 年 7 月 Azure 官方博客《Advancing resilience through chaos engineering and fault injection》的作者，另有多篇 Chaos Studio 相关博客。 |
| Cindy Sridharan 写过“Testing in production”博客 | 已验证 | Cindy Sridharan（@copyconstruct）撰写了《Testing in Production, the safe way》（2018）和《Testing in Production: the hard parts》（2019）等经典文章。 |
| Azure Chaos Studio 是“In-preview”工具 | 有误（已过时） | Azure Chaos Studio 已于 2023 年 11 月 1 日正式发布（GA），在 17 个生产区域可用，GA API 版本为 `2023-11-01`。 |
| Chaos Monkey“开箱即用不支持 Azure” | 部分验证 | Chaos Monkey 通过 Spinnaker 间接支持 Azure，但官方仅对 AWS、GCE、Kubernetes 做过专门测试，文章说法基本成立但不够精确。 |
| OneFuzz 是 Microsoft 开源的模糊测试平台 | 部分验证（已过时） | OneFuzz 仓库已于 2023 年 11 月 1 日归档，转为只读，不再接受提交。 |

### 总结

本文是一份质量扎实、方法论严谨的故障注入测试实践指南，其价值在于将故障注入测试锚定在可信计算的理论框架之上，并贯通了开发周期（Shift-Left）与发布周期（Shift-Right）的完整落地路径，同时诚实地揭示了生产环境测试的风险与应对策略。文章的主要不足在于工具生态信息存在时效性滞后——Azure Chaos Studio 已 GA、OneFuzz 与 WebScarab 已归档、Simmy 已并入 Polly，这些变化均未反映在“最后更新于 2024 年 8 月”的页面中。总体而言，文章适合作为故障注入测试与混沌工程的入门与框架性参考，但读者在采纳具体工具建议时需自行核对最新状态。

**关键要点：**

- 故障注入测试通过主动引入故障来验证系统健壮性，其理论基础是 Fault-Error-Failure 循环与可信性（Dependability）概念，目标是“拥抱失败”而非事后补救。
- 故障注入是混沌工程的技术底座，混沌工程由 Netflix 提出，两者共享“测量稳态 → 建立假设 → 注入故障 → 对比基线 → 行动”的方法论骨架。
- 故障注入应贯通开发周期（Shift-Left，与 Microsoft SDL 的 fuzzing 要求绑定）与发布周期（Shift-Right，在真实生产流量上测试），两者互补形成反馈闭环。
- 生产环境测试的核心风险控制手段是“控制爆炸半径”，Cloudflare 2019 年宕机事故（约 27 分钟，由暗发布模式的 WAF 规则引发）是这一教训的典型反面教材。
- 文章推荐的工具中，Azure Chaos Studio 已 GA、OneFuzz 与 WebScarab 已归档、Simmy 已并入 Polly，读者采纳前需核对最新状态。

## 参考资料

- [Fault Injection Testing（Microsoft Code With Engineering Playbook）](https://microsoft.github.io/code-with-engineering-playbook/automated-testing/fault-injection-testing/) — 本文解读的原文。
- [Basic Concepts and Taxonomy of Dependable and Secure Computing（IEEE TDSC，2004）](https://doi.org/10.1109/tdsc.2004.2) — Fault/Error/Failure 与 Dependability 概念的权威来源。
- [Principles of Chaos Engineering](https://principlesofchaos.org/) — 混沌工程原则的官方站点。
- [Chaos Engineering Upgraded（Netflix Tech Blog）](https://netflixtechblog.com/chaos-engineering-upgraded-878d341f15fa) — Netflix 确立混沌工程学科的官方博客。
- [Details of the Cloudflare outage on July 2, 2019（Cloudflare 官方博客）](https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/) — Cloudflare 宕机事故的官方事后分析。
- [A brief introduction to fuzzing（Microsoft Research）](https://www.microsoft.com/en-us/research/blog/a-brief-introduction-to-fuzzing-and-why-its-an-important-tool-for-developers/) — Microsoft SDL 要求 fuzzing 的官方依据。
- [Advancing resilience through chaos engineering and fault injection（Microsoft Azure Blog，2020）](https://azure.microsoft.com/en-us/blog/advancing-resilience-through-chaos-engineering-and-fault-injection/) — Mark Russinovich 的混沌工程与故障注入博客。
- [Testing in Production, the safe way（Cindy Sridharan）](https://copyconstruct.medium.com/testing-in-production-the-safe-way-18ca102d0ef1) — 生产环境测试的经典文章。
- [Azure Chaos Studio 文档（Microsoft Learn）](https://learn.microsoft.com/en-us/azure/chaos-studio/) — Azure Chaos Studio 已 GA 的官方依据。
- [microsoft/onefuzz（GitHub）](https://github.com/microsoft/onefuzz) — OneFuzz 归档状态的依据。
- [OWASP/OWASP-WebScarab（GitHub）](https://github.com/OWASP/OWASP-WebScarab/) — WebScarab 归档状态的依据。
- [Polly 官方文档：Chaos engineering](https://www.pollydocs.org/chaos/) — Simmy 并入 Polly 的依据。
- [Litmus（CNCF）](https://www.cncf.io/projects/litmus/) — Litmus 作为 CNCF 项目的依据。
