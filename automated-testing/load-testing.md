# 深度解读：Load Testing（负载测试）

> 原文：[Load Testing](https://microsoft.github.io/code-with-engineering-playbook/automated-testing/performance-testing/load-testing/)<br>
> 作者：Microsoft（微软，机构署名）<br>
> 日期：2026-08-20 09:41

## 原文及译文

<details>
<summary>原文</summary>
<section>

# Load Testing

**Source:** Engineering Fundamentals Playbook (Microsoft, [code-with-engineering-playbook](https://github.com/microsoft/code-with-engineering-playbook))
**Last updated:** August 22, 2024

## Overview

The page opens with a definition attributed to Wikipedia: "_Load testing is performed to determine a system's behavior under both normal and anticipated peak load conditions._"

A load test verifies how a system behaves under expected normal and peak workloads, confirming whether it can handle the anticipated load level — measured as concurrent users, requests per second, or data size depending on the target system.

## Why Load Testing

The main objective is proving the system behaves normally under expected load before production release. "Behave normally" depends on your target — possibly as simple as the system staying available, but it may also include meeting response-time SLAs or error-rate thresholds. Results also feed capacity planning and scalability calculations.

## Load Testing Design Blocks

Four basic components:

1. **Production-like environment** — meaningful results require hardware and network resembling the expected deployment.
2. **User-activity simulation** — composition varies by application type (e.g., e-commerce browsing/purchasing vs. IoT device-reading streams). The simulation should mimic real activity closely, including patterns and variability; overly uniform/predictable data can skew cache/hit ratios.
3. **External load controller** — a component outside the target system that governs applied load; may need scaling to multiple agents for higher activity levels.
4. **Monitoring/logging** — not strictly required but advisable to measure impact and discover bottlenecks.

## Applying the Load Testing

### Planning

1. **Identify key scenarios** — gathered from the Product Owner to represent real-world traffic; agree on and define load test cases.
2. **Determine expected normal and peak load** — concurrent users or requests per second to size the test.
3. **Identify success criteria metrics** — testing-side (response time, error rate) and/or system-side (CPU, memory).
4. **Agree on test matrix** — which cases run for which input-parameter combinations.
5. **Select the right tool** — evaluate framework features/limitations (popular options listed below); may involve custom client development.
6. **Observability** — determine metrics for throughput, latency, resource utilization.
7. **Scalability** — size load generators, workload application, CPU, memory, and network components; cloud/Kubernetes can make testing infinitely scalable.

### Preparation

The key activity is replacing the end-user client with a test bench simulating one or more client instances. Third-party tools may only need UI configuration; custom clients require development:

1. **Custom development** — minimize overhead; capture only load-relevant features of the production client (duplicate tests OK? unique workloads required? shared user context?).
2. **Test environment** — mirror production, including platform and external systems like data sources.
3. **Security contexts** — ensure all requisite contexts exist; pipelines may need non-interactive flows (e.g., OAuth2 client credentials), and admin approval may require planning leeway.
4. **Test data strategy** — output format must be compatible with analysis tools and storage areas; consider external data collection (platform/network metrics) to correlate with application behavior; cover statistical measures, distributions, graphs.
5. **Automation** — repeatability is critical; re-run tests to verify consistency and resilience; prefer pipelines; consider load tests in the PR strategy.
6. **Test client debugging** — ensure smooth execution.
7. **Test client validation** — validate extreme input-parameter values to reduce risk during the full test matrix.

### Execution

Use an existing testing framework where possible. May require coordination with the platform operations team. Practices to follow:

- **Ramp up** slowly to desired load to replicate real-world behavior.
- **Sustain** the workload long enough to observe system stabilization.
- **Ramp down** while recording how the system slows.
- Consider **traffic origin** — different regions may better replicate real-world traffic.

> **Notes:** Check network restrictions like DDoS protection beforehand — you may need to notify administrators or apply for an exemption. Standard frameworks are preferred, but custom test clients can be advantageous for batch-oriented workloads under a single security context where test data can be reused across runs, and where a script works both interactively and non-interactively.

### Analysis

- Set aside time for collecting new test data based on load-test findings.
- Correlate application metrics with platform metrics to identify bottlenecks.
- Include business stakeholders early to validate application findings; include platform operations to validate platform findings.

### Report Writing

Summarize findings from analysis, including application and platform enhancement suggestions where applicable.

### Further Testing

Follow-on test types:

- **Soak Testing** (Endurance Testing) — extended duration to ensure long-term stability
- **Stress Testing** — gradual load increase to find system limits and maximum capacity
- **Spike Testing** — sharp short-term increases in load
- **Scalability Testing** — re-testing after horizontal/vertical expansion to measure scaling
- **Distributed Testing** — multiple machines for larger or faster tests; necessary when an optimized node alone cannot produce required load

## Load Generation Testing Frameworks and Tools

| Tool | Scenario language / notes |
|---|---|
| **Azure Load Testing** | Managed Azure platform; HTTP GET in the simple case, upload JMeter scenarios for complex cases; KeyVault secrets, private-endpoint testing, automatic run/monitor |
| **JMeter** | Built-in patterns for no-code testing; extensible with Java |
| **Artillery** | JavaScript scenarios; runs as a Node application |
| **Gatling** | Scala DSL |
| **Locust** | Python; concurrent user activity concept |
| **K6** | JavaScript; open-source Kubernetes operator, Docker image, or SaaS; good for distributed load; Prometheus integration |
| **NBomber** | C# or F#; integrates with NUnit/xUnit |
| **WebValidate** | Web request validation; end-to-end and long-running performance/availability tests |

## Sample Workload Applications

For system-focused testing where no specific workload app is provided:

- **HttpBin** ([Python](https://github.com/postmanlabs/httpbin), [GoLang](https://github.com/mccutchen/go-httpbin)) — varied endpoint types; can echo request data
- **NGSA** ([Java](https://github.com/retaildevcrews/ngsa-java), [C#](https://github.com/retaildevcrews/ngsa-java)) — built for Kubernetes platform/monitoring testing; IMDB-based CRUD endpoints; no live database connection needed
- **MockBin** ([https://github.com/Kong/mockbin](https://github.com/Kong/mockbin)) — custom endpoints for testing, mocking, and tracking HTTP requests/responses between libraries, sockets, and APIs

## Conclusion

A load test is a critical step for understanding whether a system will be reliable under expected real-world traffic. Its value depends on how well you predict expected load, so following up with further testing (stress, soak, spike, scalability, distributed) is important to understand behavior under different situations.

## Resources

- [Microsoft Azure Well-Architected Framework > Load Testing](https://learn.microsoft.com/en-us/azure/architecture/framework/scalability/load-testing)

</section>
</details>

<details>
<summary>译文</summary>
<section>

# 负载测试（Load Testing）

**来源**：工程基础手册（Engineering Fundamentals Playbook，微软，[code-with-engineering-playbook](https://github.com/microsoft/code-with-engineering-playbook)）
**最近更新**：2024 年 8 月 22 日

## 概述

页面开头引用了 Wikipedia 的定义：“负载测试用于确定系统在正常和预期峰值负载条件下的行为。”

负载测试验证系统在预期的正常和峰值工作负载下的行为，确认其能否处理预期的负载水平——根据目标系统的不同，负载以并发用户数、每秒请求数或数据大小来衡量。

## 为什么进行负载测试

主要目标是在生产发布前证明系统在预期负载下能正常运行。“正常运行”取决于你的目标——可能简单到系统保持可用，也可能包括满足响应时间 SLA 或错误率阈值。测试结果还可用于容量规划和可扩展性计算。

## 负载测试的设计模块

四个基本组件：

1. **类生产环境**——有意义的结果需要与预期部署相似的硬件和网络。
2. **用户活动模拟**——组成因应用类型而异（例如，电商的浏览/购买与 IoT 设备读取流）。模拟应尽可能贴近真实活动，包括模式和变化性；过于均匀/可预测的数据会扭曲缓存/命中率。
3. **外部负载控制器**——位于目标系统之外、控制所施加负载的组件；在更高活动水平下可能需要扩展到多个代理。
4. **监控/日志**——并非严格要求，但建议采用，以衡量影响并发现瓶颈。

## 应用负载测试

### 规划

1. **识别关键场景**——从产品负责人（Product Owner）处收集，以代表真实流量；商定并定义负载测试用例。
2. **确定预期的正常和峰值负载**——并发用户数或每秒请求数，以确定测试规模。
3. **识别成功标准指标**——测试侧（响应时间、错误率）和/或系统侧（CPU、内存）。
4. **商定测试矩阵**——哪些用例针对哪些输入参数组合运行。
5. **选择合适的工具**——评估框架的功能/局限性（下方列出常用选项）；可能涉及自定义客户端开发。
6. **可观测性**——确定吞吐量、延迟、资源利用率的指标。
7. **可扩展性**——确定负载生成器、工作负载应用、CPU、内存和网络组件的规模；云/Kubernetes 可使测试无限扩展。

### 准备

关键活动是用模拟一个或多个客户端实例的测试台替换最终用户客户端。第三方工具可能只需 UI 配置；自定义客户端需要开发：

1. **自定义开发**——最小化开销；仅捕获生产客户端中与负载相关的特性（测试是否可重复？是否需要唯一工作负载？是否共享用户上下文？）。
2. **测试环境**——镜像生产环境，包括平台和外部系统（如数据源）。
3. **安全上下文**——确保所有必需的上下文存在；流水线可能需要非交互式流程（例如 OAuth2 客户端凭证），管理员审批可能需要预留时间。
4. **测试数据策略**——输出格式必须与分析工具和存储区域兼容；考虑外部数据采集（平台/网络指标）以与应用行为关联；涵盖统计度量、分布、图表。
5. **自动化**——可重复性至关重要；重新运行测试以验证一致性和韧性；优先使用流水线；考虑在 PR 策略中加入负载测试。
6. **测试客户端调试**——确保顺利执行。
7. **测试客户端验证**——验证极端输入参数值，以降低完整测试矩阵期间的风险。

### 执行

尽可能使用现有测试框架。可能需要与平台运维团队协调。应遵循的实践：

- 缓慢**爬升**（Ramp up）到期望负载，以复现真实世界行为。
- **持续**（Sustain）工作负载足够长时间，以观察系统稳定。
- 在记录系统如何减速的同时**爬降**（Ramp down）。
- 考虑**流量来源**——不同区域可能更好地复现真实世界流量。

> 注意：提前检查网络限制（如 DDoS 防护）——你可能需要通知管理员或申请豁免。优先使用标准框架，但自定义测试客户端对于单一安全上下文下的批处理型工作负载具有优势，此时测试数据可在多次运行间复用，且脚本可同时以交互式和非交互式方式工作。

### 分析

- 预留时间根据负载测试发现收集新的测试数据。
- 将应用指标与平台指标关联，以识别瓶颈。
- 尽早引入业务利益相关者以验证应用发现；引入平台运维以验证平台发现。

### 报告撰写

总结分析发现，包括适用的应用和平台增强建议。

### 进一步测试

后续测试类型：

- **浸泡测试**（Soak Testing，又称耐久测试 Endurance Testing）——延长持续时间以确保长期稳定性
- **压力测试**（Stress Testing）——逐步增加负载以找到系统极限和最大容量
- **尖峰测试**（Spike Testing）——负载的急剧短期增加
- **可扩展性测试**（Scalability Testing）——在横向/纵向扩展后重新测试以衡量扩展效果
- **分布式测试**（Distributed Testing）——多台机器进行更大或更快的测试；当单个优化节点无法产生所需负载时必需

## 负载生成测试框架和工具

| 工具 | 场景语言/说明 |
|---|---|
| **Azure Load Testing** | 托管 Azure 平台；简单场景用 HTTP GET，复杂场景上传 JMeter 场景；KeyVault 密钥、私有端点测试、自动运行/监控 |
| **JMeter** | 内置无代码测试模式；可用 Java 扩展 |
| **Artillery** | JavaScript 场景；作为 Node 应用运行 |
| **Gatling** | Scala DSL |
| **Locust** | Python；并发用户活动概念 |
| **K6** | JavaScript；开源 Kubernetes operator、Docker 镜像或 SaaS；适合分布式负载；Prometheus 集成 |
| **NBomber** | C# 或 F#；与 NUnit/xUnit 集成 |
| **WebValidate** | Web 请求验证；端到端和长时间运行的性能/可用性测试 |

## 示例工作负载应用

对于未提供特定工作负载应用的系统级测试：

- **HttpBin**（[Python](https://github.com/postmanlabs/httpbin)、[GoLang](https://github.com/mccutchen/go-httpbin)）——多种端点类型；可回显请求数据
- **NGSA**（[Java](https://github.com/retaildevcrews/ngsa-java)、[C#](https://github.com/retaildevcrews/ngsa-java)）——为 Kubernetes 平台/监控测试构建；基于 IMDB 的 CRUD 端点；无需实时数据库连接
- **MockBin**（[https://github.com/Kong/mockbin](https://github.com/Kong/mockbin)）——用于测试、模拟和跟踪库、套接字和 API 之间 HTTP 请求/响应的自定义端点

## 结论

负载测试是理解系统在预期真实流量下是否可靠的关键步骤。其价值取决于你对预期负载的预测有多准确，因此跟进进一步测试（压力、浸泡、尖峰、可扩展性、分布式）对于理解不同情况下的行为非常重要。

## 资源

- [Microsoft Azure Well-Architected Framework > Load Testing](https://learn.microsoft.com/en-us/azure/architecture/framework/scalability/load-testing)

</section>
</details>

## 摘要

本文是微软开源工程实践手册（code-with-engineering-playbook）中关于负载测试（Load Testing）的一篇指南。文章首先给出负载测试的定义——确定系统在正常与预期峰值负载下的行为，并说明其核心目标是生产发布前验证系统能否在预期负载下正常运行，同时为容量规划与可扩展性计算提供依据。随后，文章系统阐述了负载测试的四个设计模块（类生产环境、用户活动模拟、外部负载控制器、监控/日志），并按照“规划—准备—执行—分析—报告—进一步测试”的完整流程展开，覆盖了场景识别、负载确定、成功指标、工具选型、安全上下文、测试数据策略、自动化等关键环节。文章还列举了 Azure Load Testing、JMeter、Artillery、Gatling、Locust、K6、NBomber、WebValidate 等主流负载测试工具，以及 HttpBin、NGSA、MockBin 等示例工作负载应用，最后强调负载测试的价值取决于对预期负载的预测准确度，并建议跟进压力、浸泡、尖峰、可扩展性、分布式等进一步测试。

## 术语表

| 术语 | 全称 | 解释 |
| :--- | :--- | :--- |
| Load Testing | - | 负载测试。一种性能测试类型，通过模拟预期或峰值数量的并发用户/请求，测量系统在正常与预期负载条件下的响应时间、吞吐量与资源使用情况，以验证系统能否满足性能目标。 |
| SLA | Service Level Agreement | 服务等级协议。服务提供方与客户之间就服务的可用性、性能、响应时间等可量化指标达成的正式承诺与协议，通常包含违约时的补偿条款。 |
| Soak Testing | Endurance Testing | 浸泡测试（又称耐久测试、耐力测试）。在较长一段时间内（数小时到数天）以持续负载运行系统，以发现内存泄漏、资源耗尽、性能随时间退化等只有在长期运行后才会暴露的问题。 |
| Stress Testing | - | 压力测试。通过施加超出系统正常承载能力的极端负载，确定系统的崩溃点、最大容量以及系统在过载时如何降级与恢复。 |
| Spike Testing | - | 尖峰测试（又称突发负载测试）。在极短时间内将负载骤然提升到远超正常水平再迅速回落，以验证系统能否承受突发的流量激增（如秒杀、热点事件）而不崩溃。 |
| Scalability Testing | - | 可扩展性测试。通过逐步增加负载并观察系统性能变化，确定系统在增加资源（横向/纵向扩展）后能否按比例提升处理能力。 |
| Distributed Testing | - | 分布式测试。将测试负载分散到多台机器（多个负载生成器/代理）上协同执行，以突破单台机器的资源瓶颈，模拟更大规模的并发负载。 |
| OAuth2 client credentials | - | OAuth2 客户端凭证（授权模式）。OAuth 2.0 定义的四种授权模式之一，用于机器对机器（M2M）通信：客户端使用自己的 client_id 与 client_secret 直接向授权服务器换取访问令牌，不涉及用户参与。 |
| DDoS | Distributed Denial-of-Service | 分布式拒绝服务攻击。攻击者利用大量被控制的设备（僵尸网络）同时向目标服务器发送海量请求，耗尽目标带宽或计算资源，使其无法为正常用户提供服务。 |
| Kubernetes | - | 一个开源的容器编排平台，用于自动化部署、扩展和管理容器化应用，提供服务发现、负载均衡、自愈、滚动更新等能力，常缩写为 K8s。 |
| Prometheus | - | 一个开源的系统监控与告警工具包，采用基于时间序列的数据模型和 PromQL 查询语言，通过拉取方式采集指标，广泛用于云原生环境的监控。 |
| KeyVault | Azure Key Vault | Azure 密钥保管库。微软 Azure 提供的云服务，用于安全地存储和访问机密信息，包括密钥、机密（如密码、连接字符串）和证书，并提供访问控制与审计。 |
| DSL | Domain Specific Language | 领域特定语言。为特定应用领域或问题域专门设计的计算机语言，与通用编程语言相对，通常表达力更强、更贴近领域概念，例如 SQL、正则表达式、HTML 等。 |
| CRUD | Create, Read, Update, Delete | 增删改查。对持久化数据存储的四种基本操作：创建、读取、更新、删除，是数据库与 REST API 设计中最基础的操作集合。 |
| IMDB | Internet Movie Database | 互联网电影数据库（IMDb）。收录电影、电视剧、演员、制作人员等信息的在线数据库，由 Amazon 旗下公司运营。在技术语境中，其公开的样例数据集常被用作测试数据。 |
| NUnit / xUnit | - | .NET 单元测试框架。NUnit 最初移植自 Java 的 JUnit，是 .NET 生态中最成熟的测试框架之一；xUnit（xUnit.net）由 NUnit v2 作者之一创建，是 .NET 官方模板默认支持的测试框架之一。 |

## 深度解读

### 核心论点与论证逻辑

本文的核心论点可以概括为：**负载测试是生产发布前验证系统可靠性的关键步骤，其价值取决于对预期负载的预测准确度**。文章围绕这一论点构建了清晰的论证链条：先给出定义（确定系统在正常与峰值负载下的行为），再说明目的（证明系统在预期负载下正常运行），然后拆解实现手段（四个设计模块），最后落到可操作的方法论（规划、准备、执行、分析、报告、进一步测试的完整流程）。

这一论证逻辑的突出特点是**以“预期负载”为锚点**。文章反复强调，负载测试的成败首先取决于能否准确预测真实世界的负载水平——无论是并发用户数、每秒请求数还是数据大小。这一判断与业界共识一致：负载测试本质上是对“未来生产流量”的一次建模，模型失真则测试结论失真。文章在结论部分再次呼应这一观点，指出“其价值取决于你对预期负载的预测有多准确”，并因此建议跟进压力、浸泡、尖峰、可扩展性、分布式等进一步测试，以覆盖单一负载测试无法触及的边界情况。这种“负载测试不是终点，而是性能测试组合的起点”的定位，是本文最有价值的洞见之一。

### 技术/专业维度：四个设计模块与执行实践

文章提出的四个设计模块——**类生产环境、用户活动模拟、外部负载控制器、监控/日志**——构成了负载测试的技术骨架，其中有两个细节值得深入解读。

其一，**用户活动模拟的“真实性”问题**。文章特别指出，模拟应“尽可能贴近真实活动，包括模式和变化性”，并警告“过于均匀/可预测的数据会扭曲缓存/命中率”。这是一个容易被忽视却影响深远的工程细节：如果负载测试脚本以完全均匀的节奏访问固定的一组资源，缓存命中率会异常偏高，从而掩盖真实流量下缓存失效导致的性能退化。这一提醒与性能工程中“测试数据分布必须反映生产数据分布”的原则一致，体现了文章作者对负载测试“失真风险”的清醒认识。

其二，**外部负载控制器的独立性**。文章强调负载控制器必须位于目标系统之外，且在高负载下可能需要扩展到多个代理。这一设计保证了负载的施加不会与目标系统争抢资源，从而避免“测试工具本身成为瓶颈”的经典陷阱。当单个优化节点无法产生所需负载时，就需要转向分布式测试——文章在“进一步测试”部分对此做了呼应，形成了逻辑闭环。

在执行实践层面，文章提出的“缓慢爬升—持续—爬降”三段式负载曲线，以及“考虑流量来源（不同区域）”的建议，都指向同一个目标：**让测试尽可能复现真实世界的流量形态**，而非简单地“打满压力”。这与单纯追求“最大并发数”的朴素做法形成对比，体现了成熟负载测试方法论的精细度。

### 工具生态与选型：核验发现的过时与不准确之处

文章列举了八款主流负载测试工具，并给出了简短的场景语言说明。经权威来源核验，这些工具均真实存在且用途描述总体准确，但**有若干描述已过时或不完全准确**，值得读者注意：

- **Gatling 的“Scala DSL”描述已过时**。Gatling 历史上确实起源于 Scala DSL，但当前官方 SDK 已支持 Java、JavaScript、TypeScript、Scala、Kotlin 多语言，官方文档已主推 Java 与 JavaScript SDK。若读者据此认为 Gatling 只能使用 Scala，会形成误导。
- **Artillery 的“JavaScript 场景”描述不够精确**。Artillery 的测试脚本主要用 YAML 编写（config + scenarios 结构），JavaScript/TypeScript 是可选方式。文章将其概括为“JavaScript 场景”容易让人误以为 JS 是主格式。
- **Azure Load Testing 的“上传 JMeter 场景”描述不完整**。官方现同时支持上传 Locust 脚本（不仅是 JMeter），这是对原描述的重要补充。
- **NBomber 的许可并非完全开源**。NBomber 源码公开，但许可为“个人使用免费、组织/公司使用需商业许可”，与 MIT/Apache 等完全开源许可有区别。
- **K6 的 Prometheus 集成目前标记为 experimental**（experimental-prometheus-rw），生产使用建议锁定版本。

这些核验结果提示：**工具选型不能仅依赖单一来源的静态描述**，因为负载测试工具生态迭代迅速，语言支持、许可模式、集成能力都在持续变化。文章作为 2024 年 8 月更新的指南，其工具表已出现部分滞后，读者在落地时应以各工具官方文档为准。

### 影响与意义：工程实践价值与生态定位

本文的价值首先体现在其**作为工程实践手册的定位**上。它并非学术论文或工具评测，而是微软“code-with”客户/合作伙伴项目（ISE）的工程基础手册的一部分，与敏捷开发、CI/CD、代码评审、安全、可观测性等内容并列，并配套“Engineering Fundamentals Checklist”。这意味着它的目标读者是**一线工程团队**，其价值在于提供一套可直接落地、可检查的负载测试流程清单，而非理论探讨。

其次，文章与微软 Azure 生态形成了紧密关联。文末资源指向 [Microsoft Azure Well-Architected Framework > Load Testing](https://learn.microsoft.com/en-us/azure/architecture/framework/scalability/load-testing)，工具表中 Azure Load Testing 位列首位，示例应用 NGSA 也是微软为 Kubernetes 平台测试构建的。这体现了微软将负载测试纳入其“良好架构框架”（Well-Architected Framework）可扩展性支柱的整体思路：负载测试不仅是测试活动，更是架构评审与容量规划的一环。

最后，从更宏观的视角看，本文反映了**性能测试从“一次性活动”向“持续工程实践”的演进趋势**。文章在“准备”环节强调自动化与可重复性，建议“优先使用流水线”“考虑在 PR 策略中加入负载测试”，这与当前“性能左移”（Shift-Left Performance）和“持续性能测试”（Continuous Performance Testing）的行业趋势一致——负载测试正从发布前的孤立环节，逐步融入 CI/CD 流水线，成为持续交付的一部分。

### 真实性评估

| 声明/事实 | 验证状态 | 说明 |
| :--- | :--- | :--- |
| 仓库 microsoft/code-with-engineering-playbook 为微软官方开源工程手册 | 已验证 | 仓库真实存在，官方描述为“code-with 客户/合作伙伴项目的工程基础手册”。 |
| 该仓库许可证为 MIT | 部分验证 | 实际为双许可证：文档部分 CC-BY-4.0，代码部分 MIT。 |
| 页面标题为“Load Testing”，最近更新 2024 年 8 月左右 | 已验证 | 标题正确，最近更新时间为 2024 年 8 月 22 日。 |
| 页面开头引用的 Wikipedia 定义 | 部分验证 | 引文真实（2011 年 Wikipedia 原文），但当前 Wikipedia 词条已无此句，现行定义已改为“模拟多个用户并发访问”。 |
| Gatling 场景语言为“Scala DSL” | 部分验证（已过时） | 当前官方 SDK 支持 Java、JavaScript、TypeScript、Scala、Kotlin 多语言。 |
| Artillery 场景语言为“JavaScript” | 部分验证 | 主格式为 YAML，JavaScript/TypeScript 为可选方式。 |
| Azure Load Testing 复杂场景“上传 JMeter 场景” | 部分验证 | 官方现同时支持上传 Locust 脚本，不仅是 JMeter。 |
| NGSA“无需实时数据库连接” | 部分验证 | 仅 C# 版（--in-memory 模式）支持无数据库运行；Java 版默认依赖 Azure Cosmos DB。 |
| NGSA 仓库地址为 retaildevcrews/ngsa-java | 部分验证（已迁移） | 原 retaildevcrews 组织已更名为 Azure-Samples，仓库现为 Azure-Samples/ngsa-java。 |
| MockBin 仓库地址为 Kong/mockbin | 部分验证（已更名） | 已更名为 Kong/insomnia-mockbin。 |

### 总结

本文是一篇来自微软官方工程实践手册的负载测试指南，以“预期负载”为核心锚点，系统阐述了负载测试的定义、目的、四个设计模块与“规划—准备—执行—分析—报告—进一步测试”的完整方法论，并提供了主流工具与示例应用的清单。其价值在于为一线工程团队提供了一套可直接落地、可检查的负载测试流程，同时体现了性能测试向持续工程实践演进的趋势。经核验，文章的核心方法论与工具清单总体可靠，但工具表中部分描述（如 Gatling 的 Scala DSL、Artillery 的 JavaScript 场景、NGSA 的仓库地址与“无需数据库”表述）已过时或不完全准确，读者在落地时应以各工具官方文档为准。

**关键要点：**

- 负载测试的核心是验证系统在预期正常与峰值负载下的行为，其价值取决于对预期负载的预测准确度。
- 四个设计模块（类生产环境、用户活动模拟、外部负载控制器、监控/日志）中，用户活动模拟的“真实性”与负载控制器的“独立性”是避免测试失真的关键。
- 负载测试不是终点，应跟进压力、浸泡、尖峰、可扩展性、分布式等进一步测试以覆盖边界情况。
- 工具表中部分描述已过时（Gatling 多语言 SDK、Artillery 主用 YAML、Azure Load Testing 支持 Locust、NGSA 仓库迁移、MockBin 更名），落地时应以官方文档为准。
- 文章体现了性能测试从一次性活动向持续工程实践（性能左移、持续性能测试）演进的趋势。

## 参考资料

- [Load Testing - Engineering Fundamentals Playbook](https://microsoft.github.io/code-with-engineering-playbook/automated-testing/performance-testing/load-testing/) — 本文原文。
- [microsoft/code-with-engineering-playbook（GitHub）](https://github.com/microsoft/code-with-engineering-playbook) — 源仓库，核验其性质与许可证。
- [Software load testing - Wikipedia](https://en.wikipedia.org/wiki/Software_load_testing) — 核验负载测试定义及其演变。
- [Load testing - Wikipedia](https://en.wikipedia.org/wiki/Load_testing) — 核验页面引用的 Wikipedia 定义。
- [Microsoft Azure Well-Architected Framework > Load Testing](https://learn.microsoft.com/en-us/azure/architecture/framework/scalability/load-testing) — 文章引用的官方资源。
- [Azure Load Testing 概览 - Microsoft Learn](https://learn.microsoft.com/en-us/azure/app-testing/load-testing/overview-what-is-azure-load-testing) — 核验 Azure Load Testing 描述。
- [Apache JMeter 用户手册](https://jmeter.apache.org/usermanual/) — 核验 JMeter 描述。
- [Artillery 负载测试文档](https://www.artillery.io/docs/get-started/load-testing) — 核验 Artillery 描述。
- [Gatling 官方文档](https://docs.gatling.io/) — 核验 Gatling 多语言 SDK。
- [Locust 官方文档](https://docs.locust.io/en/stable/) — 核验 Locust 描述。
- [Grafana k6 文档](https://grafana.com/docs/k6/) — 核验 K6 描述。
- [NBomber 官网](https://nbomber.com/) — 核验 NBomber 描述与许可。
- [microsoft/webvalidate（GitHub）](https://github.com/microsoft/webvalidate) — 核验 WebValidate 描述。
- [postmanlabs/httpbin（GitHub）](https://github.com/postmanlabs/httpbin) — 核验 HttpBin Python 版。
- [mccutchen/go-httpbin（GitHub）](https://github.com/mccutchen/go-httpbin) — 核验 HttpBin Go 版。
- [Azure-Samples/ngsa-java（GitHub）](https://github.com/Azure-Samples/ngsa-java) — 核验 NGSA Java 版（原 retaildevcrews/ngsa-java）。
- [Azure-Samples/ngsa（GitHub）](https://github.com/Azure-Samples/ngsa) — 核验 NGSA C# 版。
- [Kong/insomnia-mockbin（GitHub）](https://github.com/Kong/insomnia-mockbin) — 核验 MockBin（原 Kong/mockbin）。
