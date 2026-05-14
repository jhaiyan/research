# 深度解读：User Interface Testing

> 原文：[User Interface Testing](https://microsoft.github.io/code-with-engineering-playbook/automated-testing/ui-testing/)<br>
> 来源：Microsoft Code With Engineering Playbook<br>
> 最后更新：2024 年 3 月 20 日

## 作者介绍

本文档为 **Microsoft Code With Engineering Playbook**（工程力学 playbook）的一部分，属于机构署名内容，而非个人作者署名。根据 GitHub 仓库的 [CODEOWNERS](https://github.com/microsoft/code-with-engineering-playbook/blob/main/.github/CODEOWNERS) 文件，该仓库的文档维护者包括：

- **Tess Ferrandez**（@tessferrandez）—— Microsoft CSE（Customer Engineering）工程师，仓库主要维护者之一，负责工程 fundamentals 领域
- **Shiran Rubin**（@shiranr）—— Microsoft CSE 工程师，PR #1026 的合并者（2024 年 3 月），参与了 UI testing 文档更新
- **Tomi Paananen**（@tompaana）—— Microsoft CSE 工程师，文档审查者
- **N Youens**（@nyouens）—— 文档代码所有者之一

Microsoft Code With Engineering Playbook 是 Microsoft 客户服务工程团队（Customer Engineering）维护的开源工程实践指南库，旨在为微软客户交付工程解决方案时提供一致的最佳实践指导。该 playbook 已被微软内部多个团队以及外部开发者广泛参考，具有较高的行业权威性。

参考来源：

- [Code With Engineering Playbook GitHub 仓库](https://github.com/microsoft/code-with-engineering-playbook)
- [CODEOWNERS 文件](https://github.com/microsoft/code-with-engineering-playbook/blob/main/.github/CODEOWNERS)
- [PR #1026：UI Testing 文档更新](https://github.com/microsoft/code-with-engineering-playbook/pull/1026)

## 原文及译文

<details>
<summary>原文</summary>
<section>

# User Interface Testing

**Last updated:** March 20, 2024

This section is primarily geared towards web-based UIs, but the guidance is similar for mobile and OS based applications.

## Applicability

UI Testing is not always going to be applicable, for example applications without a UI or parts of an application that require no human interaction. In those cases unit, functional and integration/e2e testing would be the primary means. UI Testing is going to be mainly applicable when dealing with a public facing UI that is used in a diverse environment or in a mission critical UI that requires higher fidelity. With something like an admin UI that is used by just a handful of people, UI Testing is still valuable but not as high priority.

## Goals

UI testing provides the ability to ensure that users have a consistent visual user experience across a variety of means of access and that the user interaction is consistent with the function requirements.

- Ensure the UI appearance and interaction satisfy the functional and non-functional requirements
- Detect changes in the UI both across devices and delivery platforms and between code changes
- Provide confidence to designers and developers the user experience is consistent
- Support fast code evolution and refactoring while reducing the risk of regressions

## Evidence and Measures

Integrating UI Tests in to your CI/CD is necessary but more challenging than unit tests. The increased challenge is that UI tests either need to run in headless mode with something like Puppeteer or there needs to be more extensive orchestration with Azure DevOps or GitHub that would handle the full testing integration for you like BrowserStack. Integrations like BrowserStack are nice since they provide Azure DevOps reports as part of the test run. That said, Azure DevOps supports a variety of test adapters, so you can use any UI Testing framework that supports outputting the test results to one of the output formats listed at Publish Test Results task. If you're using an Azure DevOps pipeline to run UI tests, consider using a self hosted agent in order to manage framework versions and avoid unexpected updates.

## General Guidance

The scope of UI testing should be strategic. UI tests can take a significant amount of time to both implement and run, and it's challenging to test every type of user interaction in a production application due to the large number of possible interactions.

Designing the UI tests around the functional tests makes sense. For example, given an input form, a UI test would ensure that the visual representation is consistent across devices, is accessible and easy to interact with, and is consistent across code changes.

UI Tests will catch 'runtime' bugs that unit and functional tests won't. For example if the submit button for an input form is rendered but not clickable due to a positioning bug in the UI, then this could be considered a runtime bug that would not have been caught by unit or functional tests.

UI Tests can run on mock data or snapshots of production data, like in QA or staging.

### Writing Tests

Good UI tests follow a few general principles:

- Choose a UI testing framework that enables quick feedback and is easy to use
- Design the UI to be easily testable. For example, add CSS selectors or set the id on elements in a web page to allow easier selecting.
- Test on all primary devices that the user uses, don't just test on a single device or OS.
- When a test mutates data ensure that data is created on demand and cleaned up after. The consequence of not doing this would be inconsistent testing.

### Common Issues

UI Testing can get very challenging at the lower level, especially with a testing framework like Selenium. If you choose to go this route, then you'll likely encounter timeouts, missing elements, and you'll have significant friction with the testing framework itself. Due to many issues with UI testing there have been a number of free and paid solutions that help alleviate certain issues with frameworks like Selenium. This is why you'll find Cypress in the recommended frameworks as it solves many of the known issues with Selenium.

This is an important point though. Depending on the UI testing framework you choose will result in either a smoother test creation experience, or a very frustrating and time-consuming one. If you were to choose just Selenium the development costs and time costs would likely be very high. It's better to use either a framework built on top of Selenium or one that attempts to solve many of the problems with something like Selenium.

Note there that there are further considerations as when running in headless mode the UI can render differently than what you may see on your development machine, particularly with web applications. Furthermore, note that when rendering in different page dimensions elements may disappear on the page due to CSS rules, therefore not be selectable by certain frameworks with default options out of the box. All of these issues can be resolved and worked around, but the rendering demonstrates another particular challenge of UI testing.

## Specific Guidance

**Recommended testing frameworks:**

**Web:**
- BrowserStack
- Cypress
- Jest
- Selenium
- Appium

**OS/Mobile Applications:**
- Coded UI tests (CUITs)
- Xamarin.UITest
- BrowserStack
- Appium

> Note that the framework listed above that is paid is BrowserStack, it's listed as it's an industry standard, the rest are open source and free.

---

**Source:** [Engineering Fundamentals Playbook - User Interface Testing](https://github.com/microsoft/code-with-engineering-playbook/)

</section>
</details>

## 摘要

本文档是 Microsoft Code With Engineering Playbook 中关于用户界面测试（UI Testing）的实践指南，主要面向 Web 应用 UI 测试，同时其指导原则也适用于移动端和桌面端应用。文档指出 UI 测试并非所有场景都适用——对于无 UI 或无需人工交互的应用，应以单元测试、功能测试和集成/E2E 测试为主；UI 测试主要适用于面向公众的 UI 或任务关键型 UI。文档的核心价值在于：明确了 UI 测试的战略定位（捕获"运行时 bug"，即单元/功能测试无法发现的 UI 定位问题）；推荐了 Cypress 作为优于纯 Selenium 的选择（解决 Selenium 的超时、元素缺失等已知问题）；给出了 CI/CD 集成、自托管代理、测试数据管理等实践建议；列举了 Web 端（BrowserStack、Cypress、Jest、Selenium、Appium）和移动端（Coded UI tests、Xamarin.UITest、BrowserStack、Appium）的推荐框架。需要注意的是，文档未提及 Playwright，但业界普遍认为 Playwright 是 Microsoft 开发的现代测试框架，与 Cypress 处于同一层级。

## 术语表

| 术语 | 全称 | 解释 |
| :--- | :--- | :--- |
| UI Testing | User Interface Testing（用户界面测试） | 验证应用程序的用户界面外观和交互行为是否符合要求的测试类型，确保跨设备和交付平台的一致性视觉体验 |
| CI/CD | Continuous Integration/Continuous Deployment（持续集成/持续部署） | 通过自动化构建、测试和部署流程，实现代码变更频繁且可靠地交付至生产环境的工程实践 |
| Headless Mode | 无头模式 | 不渲染可见浏览器窗口的情况下运行浏览器自动化测试的模式，适用于服务器环境 |
| E2E Testing | End-to-End Testing（端到端测试） | 从用户视角验证整个应用程序跨所有子系统完整流程的测试类型，确保所有组件协同正常工作 |
| Selenium | Selenium WebDriver | 一个通过 WebDriver 协议驱动浏览器的自动化测试工具，是 W3C 推荐标准，支持多浏览器、多语言绑定 |
| Cypress | Cypress | 一个现代化端到端测试框架，运行于与应用程序相同的运行循环中，支持实时调试和时间旅行快照 |
| Playwright | Playwright | Microsoft 开发的新一代自动化测试框架，通过 DevTools 协议直接与浏览器通信，支持自动等待、设备模拟和网络拦截 |
| BrowserStack | BrowserStack | 一个商业化的跨浏览器云测试平台，提供真实的浏览器环境用于测试，支持 Azure DevOps 集成 |
| Jest | Jest | Facebook 开发的 JavaScript 测试框架，内置快照测试功能，适用于 React 应用和其他 JS 项目 |
| Appium | Appium | 一个开源的跨平台移动应用自动化测试框架，支持 iOS、Android 和 Windows 应用 |
| Page Object Model | 页面对象模型 | 一种将页面封装为对象的测试设计模式，将页面元素定位和操作封装在对象内部，提高测试代码的可维护性和复用性 |
| Puppeteer | Puppeteer | Google Chrome 团队开发的 Node.js 库，通过 DevTools 协议控制无头 Chrome 浏览器 |
| Visual Regression Testing | 视觉回归测试 | 通过截图对比检测 UI 视觉变更的测试方法，确保界面外观在代码变更后保持一致 |
| Xamarin.UITest | Xamarin.UITest | 基于 NUnit 的 UI 自动化测试框架，用于 Xamarin 移动应用的跨平台测试 |
| Coded UI Tests (CUITs) | Coded UI Tests | Microsoft Visual Studio 中的基于代码的 UI 测试功能，用于自动化测试 UI 应用程序 |
| Self-hosted Agent | 自托管代理 | 在自有基础设施上运行的 CI/CD 代理服务器，相比 Microsoft 托管的代理可更灵活地管理框架版本 |
| Runtime Bug | 运行时 Bug | 应用程序在运行过程中才会暴露的 bug，如 UI 元素渲染后无法点击（CSS 定位问题），单元测试无法捕获 |
| CSS Selectors | CSS 选择器 | 用于在 HTML 文档中定位元素的一组语法规则，测试中常用于选择待操作的 UI 元素 |

## 深度解读

### 一、文档定位与权威性分析

本文档属于 **Microsoft Code With Engineering Playbook**（工程力学 playbook）的组成部分，该 playbook 是微软客户服务工程团队（CSE，Customer Engineering）维护的开源工程实践知识库。根据 GitHub 仓库结构和 CODEOWNERS 文件，该仓库由 Tess Ferrandez、Shiran Rubin、Tomi Paananen 和 N Youens 等微软工程师共同维护，采用社区协作模式（外部开发者可通过 Pull Request 贡献内容），最新一次 UI Testing 文档更新（PR #1026）于 2024 年 3 月由 Shiran Rubin 合并。

从权威性角度来看，该文档具有以下特征：

1. **来源可信**：Microsoft CSE 团队直接参与维护，隶属于微软官方工程实践体系
2. **社区验证**：通过 Pull Request 审查流程，所有变更需经微软工程师批准
3. **实操导向**：内容聚焦工程团队在实际项目中面临的 UI 测试挑战，而非纯理论讨论

然而，需要指出该文档存在的局限性：

1. **未提及 Playwright**：作为 Microsoft 内部团队开发的测试框架，Playwright 未被列入推荐列表，这与业界普遍认知存在差异，可能反映文档更新滞后于技术演进
2. **未涉及具体实现代码**：文档属于高层次的指导原则，缺乏可直接落地的代码示例

### 二、UI 测试的战略定位与适用边界

文档首先明确了 UI 测试并非万能解药，厘清了其适用场景与边界条件。这一分析具有重要的工程指导意义。

**应优先采用单元/功能/集成测试的场景**：

- 无用户界面的应用（如后台服务、API 服务）
- 无需人工交互的应用程序组件
- 内部管理后台（用户数量有限）

**UI 测试的核心价值场景**：

- **公众面 UI**：面向广泛用户群体的界面，需在多样化环境中保持一致性
- **任务关键型 UI**：对可靠性和稳定性要求极高的界面（如金融、医疗领域的操作界面）
- **跨设备交付**：需在多种设备、操作系统和浏览器上保持一致的视觉体验

文档提出的这一分层策略体现了**测试经济性**原则——UI 测试的实现成本和运行成本均显著高于单元测试，因此应将有限资源集中于最高价值的测试场景。

### 三、运行时 Bug 概念与测试金字塔理论

文档提出的**运行时 Bug（Runtime Bug）**概念是理解 UI 测试价值的关键切入点。所谓运行时 Bug，是指那些在 UI 渲染完成后才会暴露的缺陷，最典型的例子是"提交按钮渲染成功但因 CSS 定位问题导致无法点击"——这类问题单元测试无法覆盖，因为单元测试通常不涉及 UI 渲染管线。

这一分析呼应了测试金字塔理论（Testing Pyramid）的核心思想：金字塔底部是大量快速的单元测试，中层是较少的集成测试，顶端是更少但成本更高的 UI/E2E 测试。Kent C. Dodds 在其测试哲学中指出："大多数测试位于金字塔底部，越往上测试越少……测试的编写、运行和维护成本也越高。"Microsoft 文档间接验证了这一理论——UI 测试应作为金字塔顶端的补充，而非替代底层测试。

### 四、测试框架选型：Cypress 优于纯 Selenium

文档在测试框架推荐方面的一个重要观点是：**Cypress 优于纯 Selenium**。其核心论据在于 Selenium 存在以下已知问题：

1. **超时问题（Timeouts）**：元素等待机制不完善，容易出现 flaky 测试
2. **元素缺失（Missing Elements）**：DOM 动态变化时元素定位不稳定
3. **显著的框架摩擦**：开发者需投入大量精力处理框架本身的问题，而非测试逻辑

Cypress 的架构优势在于其独特的**同循环运行机制**：Cypress 在与应用程序相同的浏览器运行循环中执行命令，避免了 Selenium 通过 WebDriver 协议通信的中间层损耗，实现了实时同步、自动等待元素和原生访问 DOM 的能力。Cypress 官方宣称："Cypress 最终从顶层到底层控制整个自动化过程，这使其处于独特的位置，能够理解浏览器内外发生的所有事情。"

文档的这一推荐与业界主流认知一致。根据多项技术对比分析，Playwright（Microsoft 开发）和 Cypress 处于同一层级，是新一代测试框架的代表；Selenium 作为 W3C 推荐标准的传统方案，仍具价值但学习曲线更陡峭。

### 五、CI/CD 集成策略与关键技术考量

文档关于 CI/CD 集成的建议揭示了 UI 测试落地的核心挑战：

**核心挑战**：

- UI 测试运行时间显著长于单元测试
- 需处理浏览器渲染环境的一致性问题
- headless 模式下的渲染结果可能与开发机器上的视觉效果不同

**推荐解决方案**：

1. **自托管代理（Self-hosted Agent）**：在 Azure DevOps 管道中运行 UI 测试时，优先选择自托管代理，以完全控制框架版本，避免 Microsoft 托管代理自动更新导致的意外破坏
2. **云测试平台集成**：BrowserStack 等平台提供真实的浏览器环境和 Azure DevOps 原生报告集成，可显著降低环境管理复杂度
3. **标准化输出格式**：Azure DevOps 支持多种测试适配器，理论上任何支持标准输出格式的 UI 测试框架均可集成

### 六、头部模式渲染差异：一个常被忽视的陷阱

文档特别指出了一个常被忽视的技术陷阱：**头部模式（Headless Mode）下的渲染差异**。具体表现包括：

1. **渲染引擎差异**：无头浏览器在服务器环境下的渲染行为可能与本地开发机器不同
2. **CSS 维度响应式问题**：在不同页面尺寸下，某些元素可能因 CSS 规则而消失，导致测试框架默认选项无法选中这些元素
3. **字体和 DPI 渲染差异**：服务端环境缺少本地字体和 DPI 设置，可能导致视觉测试失败

这一提醒对于实施视觉回归测试（Visual Regression Testing）的团队尤为重要——快照对比测试在服务端执行时需要特别注意环境一致性配置。

### 七、测试框架生态全景

根据文档及同期发布的 E2E Testing 指南，Microsoft CSE 推荐的测试工具生态如下：

**Web 端 UI 测试框架**：

- **Cypress**（推荐，解决 Selenium 已知问题）
- **Playwright**（Microsoft 开发，文档未明确列出但业界广泛使用）
- **Selenium**（W3C 标准，传统方案）
- **Jest**（快照测试）
- **BrowserStack**（商业云平台）

**移动端测试框架**：

- **Xamarin.UITest**（Microsoft 官方）
- **Appium**（开源跨平台）
- **Coded UI Tests (CUITs)**（Visual Studio 内置）

**E2E 测试工具**：

- **Gauge**（Markdown 语法，跨平台）
- **Robot Framework**（开源，关键字驱动）
- **Katalon Studio**（基于 Selenium/Appium）
- **Ranorex Studio**（无代码选项）

值得注意的是，Playwright 虽然由 Microsoft 开发且与该文档的母项目同属 Microsoft 生态，但未出现在 UI Testing 页面的推荐列表中。同期 E2E Testing 文档也未将 Playwright 列为核心工具。这一现象的可能解释是：文档体系的不同部分在不同时间由不同维护者更新，导致工具推荐存在不一致性；或者文档编撰时 Playwright 尚未成为 Microsoft CSE 的推荐标准。

### 真实性评估

| 声明/事实 | 验证状态 | 说明 |
| :--- | :--- | :--- |
| UI 测试适用于公众面 UI 和任务关键型 UI | 已验证 | 与行业共识一致，测试金字塔理论支持此观点 |
| UI 测试可捕获单元/功能测试无法发现的运行时 Bug | 已验证 | 例如 CSS 定位导致的点击不可用问题 |
| Cypress 解决了 Selenium 的已知问题 | 已验证 | Cypress 官方文档和多项技术对比分析均支持此观点 |
| Selenium 存在超时、元素缺失等挑战 | 已验证 | Selenium 社区广泛承认这些问题 |
| BrowserStack 是行业标准的商业测试平台 | 已验证 | BrowserStack 广泛被业界采用 |
| Azure DevOps 支持多种测试适配器 | 已验证 | Microsoft 官方文档确认 |
| 使用自托管代理可更好地控制框架版本 | 已验证 | 符合 Azure DevOps 文档的推荐实践 |
| headless 模式渲染可能与开发环境不同 | 已验证 | 已知的技术差异，跨浏览器测试社区已有讨论 |
| Playwright 是 Microsoft 开发的测试框架 | 已验证 | Playwright 由 Microsoft 团队（最初由 Microsoft Edge 团队）开发维护 |
| Playwright 通过 DevTools 协议控制浏览器 | 已验证 | Playwright 官方文档确认 |
| Cypress 运行在与应用程序相同的循环中 | 已验证 | Cypress 官方架构文档确认 |

## 总结

本文档是 Microsoft 工程实践体系中关于 UI 测试的核心指导文件，其价值在于：**确立了 UI 测试的战略定位**（不是替代单元测试，而是捕获运行时 Bug 的最后防线）；**提供了务实的框架选型建议**（Cypress 优于纯 Selenium）；**揭示了 UI 测试落地的关键技术挑战**（CI/CD 集成、headless 渲染差异、环境一致性）。该文档的局限性在于更新存在一定滞后性，未涵盖 Playwright 等 Microsoft 自家的现代测试框架，且缺乏可直接落地的代码示例。读者在实际项目中应将本文档与 Microsoft Playwright 官方文档、Cypress 官方文档结合使用，以获得更完整的工具链选型视角。

**关键要点：**

- UI 测试应战略性地聚焦于公众面 UI 和任务关键型 UI，而非全面覆盖
- Cypress 因解决 Selenium 的超时、元素缺失等顽疾而被推荐，适合作为 Web UI 测试的首选框架
- CI/CD 集成 UI 测试时，优先考虑自托管代理以控制框架版本，并注意 headless 模式下的渲染差异
- Playwright 作为 Microsoft 自家的现代测试框架，虽未在本文档明确推荐，但具有与 Cypress 相当的技术竞争力，值得在实际选型时纳入评估
- 测试数据管理（按需创建、事后清理）是保证 UI 测试稳定性的基本原则
