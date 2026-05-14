# 深度解读：Smoke Testing（冒烟测试）

> 原文：[Smoke Testing](https://microsoft.github.io/code-with-engineering-playbook/automated-testing/smoke-testing/)<br>
> 作者：Microsoft（机构署名，页面未标注具体作者）<br>
> 日期：2022-08-17（页面标注的最后更新日期）

## 原文及译文

<details>
<summary>原文</summary>
<section>

### Smoke Testing

Smoke tests, sometimes named **_Sanity_**, **_Acceptance_**, or **_Build/Release Verification_** tests, are a sub-type of system/functional tests that are usually used as gates that verify the application's readiness as a preliminary step. If an application passes the smoke tests, it is acceptable, or in a stable-enough state, for the next stages of testing or deployment.

## When To Use

### Problem Addressed

Smoke tests are meant to find, as early as possible, if an application is working or not. The goal of smoke tests is to save time; if the current version of the application does not pass smoke tests, then the rest of the integration or deployment chain for it can be abandoned. Smoke tests do not aim to provide full functionality coverage but instead focus on a few quick acceptance invocations for which the application should, at all times, respond correctly to.

### ROI Tipping Point

Smoke tests cover only the most critical application path, and should not be used to actually test the application's behavior, keeping execution time and complexity to minimum. The tests can be formed of a subset of the application's integration or e2e tests, and they cover as much of the functionality with as little depth as required.

The golden rule of a good smoke test is that it saves time on validating that the application is acceptable to a stage where better, more thorough testing will begin.

### Applicable to

- **Local dev desktop** - _Example:_ Applying manual smoke testing to verify that the application is OK.
- **Build pipelines** - _Example:_ Running a small set of the integration test suite before running the full coverage of tests, which may take a long time.
- **Non-production and Production deployments** - _Example:_ Running a curl command to the product's API and asserting the response is 200 before running load test which consume resources.
- **PR Validation** - _Example:_ - Deploying the application chart to a test namespace and validating the release is successful and no immediate regressions are merged.

## Conclusion

Smoke testing is a low-effort, high-impact step to ship more reliable software. It should be considered amongst the first stages to implement when planning continuously integrated and delivered systems.

## Resources

- [Wikipedia - Smoke Testing](https://en.wikipedia.org/wiki/Smoke_testing_\(software\))
- [Google SRE Book - System Tests](https://landing.google.com/sre/sre-book/chapters/testing-reliability/#system-tests)

</section>
</details>

<details>
<summary>译文</summary>
<section>

### 冒烟测试（Smoke Testing）

冒烟测试，有时也被称为**健全性测试（Sanity）**、**验收测试（Acceptance）**或**构建/发布验证测试（Build/Release Verification）**，是系统/功能测试的一个子类型，通常作为门禁（Gate）使用，用于在初步阶段验证应用程序的就绪状态。如果应用程序通过了冒烟测试，就说明它处于可接受、或足够稳定的状态，可以进入下一阶段的测试或部署。

## 何时使用

### 解决的问题

冒烟测试旨在尽早发现应用程序是否正常工作。冒烟测试的目标是节省时间；如果当前版本的应用程序未能通过冒烟测试，那么后续的集成或部署链路就可以被放弃。冒烟测试并不追求完整的功能覆盖，而是聚焦于少数几个快速的验收调用，应用程序在任何时候都应当对这些调用做出正确响应。

### ROI 拐点

冒烟测试只覆盖最关键的应用程序路径，不应被用于真正测试应用程序的行为，从而将执行时间和复杂度降到最低。这些测试可以由应用程序集成测试或端到端（E2E）测试的一个子集构成，它们以尽可能小的深度覆盖尽可能多的功能。

一个好的冒烟测试的黄金法则是：它能在验证应用程序是否达到“可以开始更完善、更彻底测试”这一阶段时节省时间。

### 适用场景

- **本地开发桌面** —— 示例：应用手动冒烟测试来验证应用程序是否正常。
- **构建流水线** —— 示例：在运行可能耗时很长的完整测试覆盖之前，先运行一小部分集成测试套件。
- **非生产与生产环境部署** —— 示例：在运行会消耗资源的负载测试之前，先对产品 API 执行 curl 命令并断言响应为 200。
- **PR 验证** —— 示例：将应用程序 Chart 部署到测试命名空间，验证发布成功且没有立即的回归被合并。

## 结论

冒烟测试是发布更可靠软件的一个低成本、高影响的步骤。在规划持续集成与持续交付系统时，应当将其作为最先实施的阶段之一来考虑。

## 资源

- [维基百科 - 冒烟测试](https://en.wikipedia.org/wiki/Smoke_testing_\(software\))
- [Google SRE Book - 系统测试](https://landing.google.com/sre/sre-book/chapters/testing-reliability/#system-tests)

</section>
</details>

## 摘要

本文是 Microsoft 官方工程实践手册（Engineering Fundamentals Playbook）中关于冒烟测试（Smoke Testing）的一篇短篇指南。文章将冒烟测试定义为系统/功能测试的子类型，通常作为验证应用就绪状态的门禁（Gate）使用，并指出其核心目标是“节省时间”——一旦当前版本未通过冒烟测试，后续的集成或部署链路即可放弃。文章强调冒烟测试只覆盖最关键路径、不追求完整功能覆盖，并给出了“黄金法则”：好的冒烟测试能在验证应用是否达到“可开始更彻底测试”这一阶段时节省时间。最后，文章列举了本地开发、构建流水线、非生产/生产部署、PR 验证四类适用场景，并得出结论：冒烟测试是发布更可靠软件的低成本、高影响步骤，应作为持续集成与持续交付系统中最先实施的阶段之一。

## 术语表

| 术语 | 全称 | 解释 |
| :--- | :--- | :--- |
| Smoke Testing | - | 冒烟测试。覆盖组件或系统“最重要功能”的一组测试用例，用于在正式测试开始前判断该构建是否“基本可用、值得继续深入测试”。ISTQB 术语表将其定义为“覆盖组件或系统主要功能、以判断其在计划测试开始前能否正常工作的测试套件”。其词源来自硬件测试：给新电路板通电，若“冒烟”则立即断电，无需进一步测试。 |
| Sanity Testing | - | 健全性测试（又称理智测试）。对程序功能“非常简短的走查”，用于确认系统某部分或方法大致按预期工作，从而判断是否可能且合理继续进一步测试。业界通常将其理解为“窄而深”的检查：在某个 Bug 修复或补丁之后，验证该特定改动是否正确且未破坏邻近功能，常被视为回归测试的子集。 |
| Acceptance Testing | - | 验收测试。一个“测试级别”（Test Level），焦点是“决定是否接受该系统”。通常在发布前由最终用户、客户或业务方执行，验证系统是否满足业务需求，是发布前的最后一道关卡。其子类型包括用户验收测试（UAT）、Alpha 测试、Beta 测试等。 |
| Build/Release Verification Testing | BVT / RVT | 构建验证测试/发布验证测试。一组在新构建上运行的高优先级、短小的测试，用于判断该构建是否“稳定到足以进入更深入的测试阶段”，充当“守门人”角色，通常在每日构建产出后立即自动运行。 |
| System Testing | - | 系统测试。一个“测试级别”，焦点是“验证系统作为一个整体满足规定需求”。它针对完整集成的产品，在接近生产的环境中进行。 |
| Functional Testing | - | 功能测试。一个“测试类型”（Test Type），焦点是“评估组件或系统是否满足功能需求”，回答“我们是否把产品做对了”，属于黑盒测试。 |
| Integration Testing | - | 集成测试。一个“测试级别”，焦点是“组件或系统之间的交互”。Martin Fowler 区分了窄集成测试（仅测试与外部服务交互的代码，速度快）与宽集成测试（需要所有服务的真实版本，他更愿称为系统测试或端到端测试）。 |
| End-to-End Testing | E2E | 端到端测试。贯穿应用大部分组件的测试，覆盖所有子系统、网络依赖、服务和数据库，在类生产环境中运行，从最终用户视角验证完整业务流程。位于测试金字塔顶端，因脆弱、昂贵、运行慢而应保持最少数量。 |
| ROI Tipping Point | - | ROI 拐点。本文中指冒烟测试“投入产出比”的临界判断：冒烟测试只覆盖最关键路径、以最小深度换取最大覆盖，从而在“验证应用是否可进入更彻底测试”这一环节上实现时间节省的最大化。 |
| Build Pipeline | - | 构建流水线。持续集成/持续交付（CI/CD）中自动化执行构建、测试、部署等步骤的流水线。 |
| PR Validation | - | Pull Request 验证。在代码合并前对 Pull Request 进行的自动化验证，本文指将应用 Chart 部署到测试命名空间以验证发布成功。 |
| CI/CD | Continuous Integration / Continuous Delivery | 持续集成/持续交付。一种软件开发实践，通过自动化构建、测试与部署，实现频繁、可靠的软件交付。 |
| SRE | Site Reliability Engineering | 站点可靠性工程。Google 提出的一套将软件工程方法应用于运维的实践体系，其《SRE Book》是本文引用的权威来源之一。 |
| curl | - | 一个命令行工具，用于通过 URL 语法传输数据，常用于对 HTTP API 发起请求并检查响应状态码，是冒烟测试最常用的实现手段之一。 |
| Load Test | - | 负载测试。一种性能测试，测量系统在预期或峰值并发下的表现是否可接受。本文中冒烟测试通常先于负载测试执行，以避免在不可用系统上浪费性能测试资源。 |
| Application Chart | - | 应用 Chart。指 Helm Chart，Kubernetes 的包管理格式，用于定义、安装和升级应用及其依赖。本文中用于将应用部署到测试命名空间进行 PR 验证。 |

## 深度解读

### 核心论点与论证逻辑

本文的核心论点可以概括为一句话：**冒烟测试是一种“低成本、高影响”的软件质量门禁，其价值不在于测试本身，而在于“尽早、快速地失败”所节省的时间**。

文章的论证逻辑是清晰的递进结构：先给出定义（系统/功能测试的子类型、作为门禁使用），再说明其要解决的问题（尽早发现应用是否可用、节省时间），接着用“ROI 拐点”一节论证其投入产出比的合理性（只覆盖最关键路径、以最小深度换取最大覆盖），然后落到四类具体适用场景，最后以结论收束。这一结构体现了工程手册的典型写法——**先讲“是什么”和“为什么”，再讲“在哪里用”**，而非学术论文式的严密论证。

值得注意的是，文章反复强调一个反直觉的观点：冒烟测试“不应被用于真正测试应用程序的行为”（should not be used to actually test the application's behavior）。这实际上是在划定冒烟测试的边界——它回答的是“这个构建是否值得继续测试/部署”这一元问题，而非“这个功能是否正确”这一具体问题。这一边界意识是本文最有价值的思想内核，也是许多团队在实践中容易迷失的地方。

### 术语辨析：文章对“同义词”的表述不够精确

文章开篇将冒烟测试与**健全性测试（Sanity）**、**验收测试（Acceptance）**、**构建/发布验证测试（Build/Release Verification）**并列为“有时被称为”的同义词。经多方权威来源交叉验证，这一表述**部分准确、部分存在概念混淆**，需要辨析：

- **冒烟测试 ≈ 构建验证测试（BVT）**：这一等同关系是成立的。维基百科明确将“build verification test（BVT）”和“build acceptance test”列为冒烟测试的同义词 [🔗](https://en.wikipedia.org/wiki/Smoke_testing_(software) "Wikipedia: Smoke testing (software)")。二者都指“新构建上快速、浅层的稳定性检查”。

- **冒烟测试与健全性测试（Sanity）**：存在术语层面的分歧。ISTQB 官方术语表将 sanity test 直接列为 smoke test 的同义词 [🔗](https://istqb-glossary.page/smoke-test/ "ISTQB Glossary: Smoke Test")；但业界通行实践（TechTarget、Semaphore、CloudBees 等）普遍区分二者——冒烟测试“宽而浅、面向新构建”，健全性测试“窄而深、面向特定修复”，前者认证“构建”，后者认证“变更” [🔗](https://www.techtarget.com/searchsoftwarequality/tip/Smoke-testing-vs-sanity-testing-explainer-on-key-differences "TechTarget: Smoke testing vs sanity testing")。

- **冒烟测试与验收测试（Acceptance）**：这是最需要澄清的一点。维基百科列出的同义词是“build acceptance test”（构建验收测试），**而非**“acceptance testing”（验收测试）这一更宽泛的测试级别。验收测试是发布前由用户执行的、全面的、面向业务需求的最终关卡，与冒烟测试在范围、深度、执行者、时机上均不同 [🔗](https://istqb-glossary.page/acceptance-testing/ "ISTQB Glossary: Acceptance Testing")。因此，将“冒烟测试”与“验收测试”直接等同属于概念混淆。

这一辨析并非吹毛求疵，而是有实际工程意义的：如果团队把“冒烟测试”误当作“验收测试”来设计，就可能要么把冒烟测试做得过重（套件膨胀、失去快速反馈），要么把验收测试做得过轻（遗漏业务需求验证）。理解这些术语的精确边界，是正确落地冒烟测试的前提。

### 冒烟测试在 CI/CD 中的定位与门禁机制

文章将冒烟测试定位为“门禁（Gate）”，这一概念在业界有充分共识，但文章未展开其机制细节。综合多个权威来源，冒烟测试作为门禁的核心逻辑是**快速 go/no-go 检查，且失败必须真正阻断流水线**。Harness 明确指出：“只有当失败真正阻止构建前进时，冒烟测试才有效” [🔗](https://www.harness.io/harness-devops-academy/integrating-smoke-testing-into-your-ci-cd-pipeline-what-devops-needs-to-know "Harness: Integrating Smoke Testing into Your CI/CD Pipeline")；CloudBees 同样强调“将失败视为硬性阻断” [🔗](https://www.cloudbees.com/blog/smoke-testing "CloudBees: Smoke Testing")。

在流水线中的典型位置，业界共识包括：提交代码前（本地 Git 钩子）、端到端/验收测试之前、部署之前、部署之后 [🔗](https://semaphore.io/community/tutorials/smoke-testing "Semaphore: Smoke Testing Keeps Your Delivery Pipeline Safe and Sound")。Martin Fowler 的建议更为激进——“在部署流水线的每个步骤之前运行冒烟测试”，并在“部署到生产环境时”也运行 [🔗](https://martinfowler.com/bliki/SmokeTest.html "Martin Fowler: SmokeTest")。这与 Jez Humble 在《Continuous Delivery》中列出的“Smoke test your deployments”实践一致 [🔗](https://www.continuousdelivery.com/implementing/patterns/ "Continuous Delivery: Patterns")。

文章列举的四类场景（本地开发、构建流水线、非生产/生产部署、PR 验证）与业界实践高度吻合，其中“生产环境部署后对 API 执行 curl 并断言返回 200”是最典型、也最容易被低估的场景——它用一行命令的成本，在负载测试等昂贵环节之前拦截了“根本跑不起来”的系统。

### “低成本、高影响”的实质：快速失败的时间杠杆

文章结论中“low-effort, high-impact”（低成本、高影响）的定性，其背后的经济学逻辑值得深挖。冒烟测试的 ROI 并非来自“发现了多少 Bug”，而是来自**“快速失败”所避免的沉没成本**。Semaphore 的表述最为精炼：“冒烟测试的价值在于能够极快地失败” [🔗](https://semaphore.io/community/tutorials/smoke-testing "Semaphore: Smoke Testing Keeps Your Delivery Pipeline Safe and Sound")。

具体而言，这一杠杆体现在两个层面：

1. **时间维度**：业界共识是冒烟测试套件只需 5–10 个核心检查、运行时间控制在 3–7 分钟（Harness 建议整套 5 分钟内完成） [🔗](https://www.harness.io/harness-devops-academy/integrating-smoke-testing-into-your-ci-cd-pipeline-what-devops-needs-to-know "Harness: Integrating Smoke Testing into Your CI/CD Pipeline")。用几分钟的成本，避免在“根本跑不起来”的构建上浪费数小时乃至数天的完整测试与部署资源。

2. **资源维度**：Microsoft Research 的论文《The Art of Testing Less without Sacrificing Quality》提出的测试选择策略（THEO）在三个 Microsoft 产品上实现了 50% 的测试执行量削减、每年节省数百万美元，同时保持质量 [🔗](https://www.microsoft.com/en-us/research/publication/the-art-of-testing-less-without-sacrificing-quality/ "Microsoft Research: The Art of Testing Less without Sacrificing Quality")。这从侧面印证了“用更少、更快的测试换取同等质量”的 ROI 逻辑。

需要指出的是，这一“高影响”是有前提的：冒烟测试必须**自动化**。CloudBees 明确论断“手动冒烟测试耗时、测试者之间结果不一致、且无法扩展” [🔗](https://www.cloudbees.com/blog/smoke-testing "CloudBees: Smoke Testing")。文章在“本地开发桌面”场景中提到了“手动冒烟测试”，这更多是作为开发者的个人快速自检，而非流水线中的正式门禁——二者不应混淆。

### 术语起源与历史背景

“冒烟测试”一词的起源，是理解其本质的一把钥匙。权威软件测试著作 Kaner、Bach 与 Pettichord 的《Lessons Learned in Software Testing》（Wiley，2002）明确写道：“The phrase smoke test comes from electronic hardware testing” [🔗](https://en.wikipedia.org/wiki/Smoke_testing_(software) "Wikipedia: Smoke testing (software)")。其类比是：给新电路板通电，若看到冒烟就立即断电，无需再做进一步测试。这一“通电看是否冒烟”的意象，精准地传达了冒烟测试的精髓——**用最廉价的信号，在最早期判断“是否值得继续”**。

不过，严格的历史考证显示该术语可能更早可追溯到管道工程：维基百科“Smoke testing (electrical)”词条指出，该表达“probably was first used in plumbing”（可能最早用于管道工程），用于检测管道裂缝与泄漏，后来才被隐喻性地扩展到电子领域 [🔗](https://en.wikipedia.org/wiki/Smoke_testing_(electrical) "Wikipedia: Smoke testing (electrical)")。Thoughtworks 的一篇博客也指出，不同团队对“冒烟测试”的理解会因所知的起源故事不同而产生分歧 [🔗](https://www.thoughtworks.com/en-us/insights/blog/origin-smoke-testing-and-confusion-it-can-cause "Thoughtworks: The origin of Smoke Testing and the confusion it can cause")。这一历史细节本身，恰恰印证了本文“术语辨析”一节所揭示的现象——冒烟测试的边界在业界长期存在模糊地带。

### 争议与不同观点

围绕本文主题，业界存在几处值得关注的争议与分歧：

1. **冒烟测试与健全性测试是否同义**：如前所述，ISTQB 官方术语表将二者视为同义词，而 TechTarget、Semaphore、CloudBees 等实践派来源则坚持区分。这一分歧的根源在于“术语标准化”与“工程实践”之间的张力——标准化追求简洁统一，实践则更看重语义的精确分工。

2. **冒烟测试是否应覆盖 UI**：Harness 建议优先 API 级断言，因为“API 级检查通常更快、更可靠” [🔗](https://www.harness.io/harness-devops-academy/integrating-smoke-testing-into-your-ci-cd-pipeline-what-devops-needs-to-know "Harness: Integrating Smoke Testing into Your CI/CD Pipeline")；但部分团队仍坚持在冒烟测试中加入少量 UI 冒烟用例。这一分歧本质上是“速度”与“覆盖真实用户路径”之间的权衡。

3. **冒烟测试与金丝雀发布的关系**：Google SRE 材料较少直接使用“smoke test”一词，但其“金丝雀发布”（Canary）概念承担了类似的早期检测职能 [🔗](https://sre.google/workbook/canarying-releases/ "Google SRE Workbook: Canarying Releases")。有观点认为，在云原生时代，部署后的冒烟测试与金丝雀发布存在功能重叠，二者如何分工是实践中的开放问题。

### 真实性评估

| 声明/事实 | 验证状态 | 说明 |
| :--- | :--- | :--- |
| 冒烟测试是系统/功能测试的子类型，通常作为门禁使用 | 已验证 | 与 ISTQB 术语表、Martin Fowler、Google SRE Book 的定义一致 [🔗](https://istqb-glossary.page/smoke-test/ "ISTQB Glossary: Smoke Test") [🔗](https://martinfowler.com/bliki/SmokeTest.html "Martin Fowler: SmokeTest") |
| 冒烟测试又称 Sanity、Acceptance、Build/Release Verification 测试 | 部分验证 | 冒烟测试 ≈ BVT ≈ 构建验收测试成立；但“验收测试（Acceptance Testing）”是独立的、更全面的测试级别，不能与冒烟测试等同；Sanity 在 ISTQB 中为同义词，但业界实践普遍区分二者 [🔗](https://en.wikipedia.org/wiki/Smoke_testing_(software) "Wikipedia: Smoke testing (software)") [🔗](https://istqb-glossary.page/acceptance-testing/ "ISTQB Glossary: Acceptance Testing") |
| 冒烟测试的目标是节省时间，失败后可放弃后续集成/部署链路 | 已验证 | 与 Semaphore“快速失败”、CloudBees“几分钟而非几小时”等业界共识一致 [🔗](https://semaphore.io/community/tutorials/smoke-testing "Semaphore: Smoke Testing Keeps Your Delivery Pipeline Safe and Sound") |
| 冒烟测试只覆盖最关键路径，不追求完整功能覆盖 | 已验证 | 与 Martin Fowler“运行极快但完全不追求全面覆盖”的定义一致 [🔗](https://martinfowler.com/bliki/SmokeTest.html "Martin Fowler: SmokeTest") |
| 冒烟测试是“低成本、高影响”的步骤 | 已验证 | 为 Microsoft 官方定性，且与 Harness（5 分钟内完成）、Microsoft Research（测试削减 50%）等来源的量化佐证一致 [🔗](https://www.harness.io/harness-devops-academy/integrating-smoke-testing-into-your-ci-cd-pipeline-what-devops-needs-to-know "Harness: Integrating Smoke Testing into Your CI/CD Pipeline") |
| 冒烟测试术语源自硬件/电子工程（通电看是否冒烟） | 已验证（有补充） | 软件测试语境下为权威解释（Kaner 等《Lessons Learned in Software Testing》）；但严格历史考证显示该术语更早可追溯到管道工程 [🔗](https://en.wikipedia.org/wiki/Smoke_testing_(electrical) "Wikipedia: Smoke testing (electrical)") |
| 引用的 Google SRE Book 链接有效 | 已验证（需更新） | 原 `landing.google.com` 地址已 301 永久重定向至 `sre.google`，现地址为 [sre.google/sre-book/testing-reliability/](https://sre.google/sre-book/testing-reliability/ "Google SRE Book: Testing for Reliability") |
| 引用的维基百科冒烟测试词条有效 | 已验证 | 词条明确定义了软件冒烟测试并追溯术语起源 [🔗](https://en.wikipedia.org/wiki/Smoke_testing_(software) "Wikipedia: Smoke testing (software)") |

### 总结

本文是一篇短小精悍的工程实践指南，其价值不在于信息量，而在于**用最简洁的语言抓住了冒烟测试的本质——一种以“快速失败”换取“时间节省”的低成本质量门禁**。文章对冒烟测试的定义、ROI 逻辑和四类适用场景的概括，与业界权威来源（ISTQB、Martin Fowler、Google SRE Book、Harness、CloudBees 等）高度一致，可信度较高。唯一需要读者留意的是开篇对“同义词”的表述不够精确——冒烟测试与构建验证测试（BVT）基本可互换，但与“验收测试”是不同层级的概念，与“健全性测试”在业界实践中也存在明确分工。对于正在规划 CI/CD 体系的团队而言，本文是一份值得作为起点、但需结合更深入资料补充细节的入门参考。

**关键要点：**

- 冒烟测试是系统/功能测试的子类型，作为验证应用就绪状态的门禁（Gate）使用，核心目标是“尽早、快速地失败”以节省时间。
- 冒烟测试只覆盖最关键路径、不追求完整功能覆盖，其“黄金法则”是在验证应用是否达到“可开始更彻底测试”这一阶段时节省时间。
- 文章将冒烟测试与 Sanity、Acceptance、BVT 并列为同义词的表述不够精确：冒烟测试 ≈ BVT 成立，但与“验收测试”是不同测试级别，与“健全性测试”在业界实践中也有明确分工。
- 冒烟测试的“低成本、高影响”建立在自动化与“失败必须硬性阻断流水线”的前提之上，业界共识是 5–10 个核心检查、5 分钟内完成。
- 冒烟测试术语源自硬件测试（通电看是否冒烟），但严格历史考证显示其更早可追溯到管道工程。

## 参考资料

- [Microsoft Engineering Fundamentals Playbook: Smoke Testing](https://microsoft.github.io/code-with-engineering-playbook/automated-testing/smoke-testing/) — 本文原文。
- [GitHub: microsoft/code-with-engineering-playbook](https://github.com/microsoft/code-with-engineering-playbook) — 本文所属的官方开源工程实践手册仓库，用于核实文档性质与维护状态。
- [Wikipedia: Smoke testing (software)](https://en.wikipedia.org/wiki/Smoke_testing_(software)) — 冒烟测试的权威定义与同义词辨析。
- [Wikipedia: Smoke testing (electrical)](https://en.wikipedia.org/wiki/Smoke_testing_(electrical)) — 冒烟测试术语的电子/管道工程起源。
- [ISTQB Glossary: Smoke Test](https://istqb-glossary.page/smoke-test/) — 冒烟测试的标准化定义。
- [ISTQB Glossary: Acceptance Testing](https://istqb-glossary.page/acceptance-testing/) — 验收测试的标准化定义，用于辨析其与冒烟测试的区别。
- [Martin Fowler: SmokeTest](https://martinfowler.com/bliki/SmokeTest.html) — 冒烟测试的精炼定义与流水线使用建议。
- [Martin Fowler: TestPyramid](https://martinfowler.com/bliki/TestPyramid.html) — 测试金字塔模型，用于定位冒烟测试在测试体系中的位置。
- [Google SRE Book: Testing for Reliability](https://sre.google/sre-book/testing-reliability/) — 本文引用的 Google SRE Book 测试章节（原 landing.google.com 地址已迁移至此）。
- [Harness: Integrating Smoke Testing into Your CI/CD Pipeline](https://www.harness.io/harness-devops-academy/integrating-smoke-testing-into-your-ci-cd-pipeline-what-devops-needs-to-know) — 冒烟测试门禁机制、放置点与时限的最佳实践。
- [CloudBees: Smoke Testing](https://www.cloudbees.com/blog/smoke-testing) — 冒烟测试自动化价值与“硬性阻断”原则。
- [Semaphore: Smoke Testing Keeps Your Delivery Pipeline Safe and Sound](https://semaphore.io/community/tutorials/smoke-testing) — 冒烟测试的四个放置点与“快速失败”价值。
- [TechTarget: Smoke testing vs sanity testing](https://www.techtarget.com/searchsoftwarequality/tip/Smoke-testing-vs-sanity-testing-explainer-on-key-differences) — 冒烟测试与健全性测试区别的权威解释。
- [Microsoft Research: The Art of Testing Less without Sacrificing Quality](https://www.microsoft.com/en-us/research/publication/the-art-of-testing-less-without-sacrificing-quality/) — 测试削减 ROI 的量化佐证。
- [Thoughtworks: The origin of Smoke Testing and the confusion it can cause](https://www.thoughtworks.com/en-us/insights/blog/origin-smoke-testing-and-confusion-it-can-cause) — 冒烟测试术语起源的争议与混淆。
- [Continuous Delivery: Patterns (Jez Humble)](https://www.continuousdelivery.com/implementing/patterns/) — “Smoke test your deployments”实践。
