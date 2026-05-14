# 深度解读：Test planning（测试规划）

> 原文：[Test planning](https://microsoft.github.io/code-with-engineering-playbook/automated-testing/test-planning/)<br>
> 作者：Microsoft（微软）— Engineering Fundamentals Playbook（ISE 团队）<br>
> 日期：2026-08-19 14:34

## 原文及译文

<details>
<summary>原文</summary>
<section>

# Test planning

**Organization:** Microsoft — Engineering Fundamentals Playbook (ISE)
**Source:** [code-with-engineering-playbook](https://github.com/microsoft/code-with-engineering-playbook)
**Last update:** April 17, 2025

## Test planning

We should be intentional when we think about how to test our applications. One way to make sure that we are testing the right things is to build test plans for various scenarios and work out test cases at the design stage of a user story.

This content aims to show some ways we can think about planning and give some examples using a web site with a login portal as an example.

## Building test cases for a user story

As we design the code for a user story we can start by defining a set of test cases that will ensure that all acceptance criteria are met.

This can be done as an exercise that includes both the developers and other stakeholders. Some of the test cases may initially be manual, and some may be planned for automation, depending on the situation.

Going through this exercise doesn't only produce test cases, it also helps clarify the acceptance criteria and informs how we should build the solution.

1. **Understand the Acceptance Criteria** — Thoroughly read and understand the acceptance criteria for the story. Clarify any ambiguities with the product owner or stakeholders.
2. **Identify Test Scenarios** — Consider both positive and negative scenarios (happy paths, and error cases) to cover edge cases. Determine what is in and out of scope, i.e. do we only test functional requirements, or are non-functional requirements such as security, accessibility, reliability etc. in scope for testing?
3. **Define Test Cases** — For each test scenario, define detailed test cases. Each test case should be documented with:
   - **TestCase Title:** What is being tested
   - **Preconditions:** Any setup or test data required before executing the test
   - **Test Steps:** Step-by-step instructions to execute the test
   - **Expected Result:** The expected outcome of the test

   The test can be described in the Given-When-Then format to make it clear and concise:
   **Given** the initial context or state, **When** the action or event, **Then** the precise outcome
4. **Automate where Possible** — If feasible, automate the test cases. Focus on automating hot paths, and critical areas.
5. **Review and Refine** — Review the test cases with peers or stakeholders to ensure that we have covered everything we want to cover, and that expected outcomes are correct. Refine the test cases based on feedback.

### Examples of Test Cases using the Given-When-Then Format

**User Login (Positive Test Case)**

- **Title:** Verify user login with valid credentials
- **Preconditions:** User is on the login page
- **Test Steps:** Given the user is on the login page, when the user enters valid credentials and clicks the login button, then the user should be redirected to the dashboard
- **Expected Result:** User is successfully logged in and redirected to the dashboard

**User Login with Invalid Credentials (Negative Test Case)**

- **Title:** Verify user login with invalid credentials
- **Preconditions:** User is on the login page
- **Test Steps:** Given the user is on the login page, when the user enters invalid credentials and clicks the login button, then the user should see an error message indicating invalid username or password
- **Expected Result:** Error message is displayed and the user remains on the login page

**Security Testing for Login Page (Non-Functional Requirement)**

- **Title:** Verify that the login page is protected against SQL injection attacks
- **Preconditions:** User is on the login page
- **Test Steps:** Given the user is on the login page, when the user enters a SQL injection string (e.g. `' OR '1'=1`) in the username field and clicks the login button, then the system should not allow login and should display an error message
- **Expected Result:** The system prevents login and displays an error message

**Usability Testing for Form Validation (Non-Functional Requirement)**

- **Title:** Verify that the registration form provides clear error messages for invalid inputs
- **Preconditions:** User is on the registration page
- **Test Steps:** Given the user is on the registration page, when the user enters invalid data (e.g. incorrect email format) and submits the form, then the system should display a clear and specific error message indicating the issue
- **Expected Result:** Clear and specific error message is displayed

**Reliability Testing for System Uptime (Non-Functional Requirement)**

- **Title:** Verify that the system maintains 99.9% uptime over a month
- **Preconditions:** System is monitored over a month
- **Test Steps:** Given the system is up and running, when the system is monitored for uptime over a month, then the system should maintain 99.9% uptime
- **Expected Result:** System maintains 99.9% uptime over the monitored period

## Grouping Test Cases into Test Plans

We can create different test plans, such as a full regression test plan, a smoke test plan, a functional test plan etc. and organize the test cases under these test plans.

A few benefits of creating test plans are:

- We can make sure that all aspects of the application are tested, including functional, non-functional and edge cases
- They provide clear objectives and scope, which helps developers understand what needs to be tested
- They help manage and execute tests systematically, i.e. we have a suite of tests to run validate integration etc.
- By identifying and prioritizing test cases based on risk, test plans help us focus on the most critical areas of the application
- In some industries they are required for compliance with standards and regulation
- They help us understand what tests are most important to automate

### Common Test Plans

#### Full Regression Test plan

- **Purpose:** To verify that recent changes have not adversely affected existing functionality
- **Test Cases Included:**
  - All functional test cases
  - All integration test cases
  - All system test cases
  - All previously reported bugs that have been fixed
- **Example:**
  - Test001: Verify user login with valid credentials
  - Test002: Verify user registration with valid details
  - Test003: Verify password reset functionality

#### Smoke Test plan

- **Purpose:** To perform a quick check to ensure that the most critical functionalities of the application are working
- **Test Cases Included:**
  - Basic functionality test cases
  - High-priority test cases that cover the core features
- **Example:**
  - Test001: Verify user login with valid credentials
  - Test004: Verify adding an item to the shopping cart
  - Test005: Verify search functionality with a valid keyword

#### Functional Test Plan

- **Purpose:** To verify that each function of the software application conforms to the specification
- **Test Cases Included:**
  - Test cases that validate specific functionality
  - Test cases that cover user interactions and business logic
- **Example:**
  - Test002: Verify user registration with valid details
  - Test006: Verify user login with invalid credentials
  - Test005: Verify user registration with missing requirement fields

#### Area Regression Test Plan

- **Purpose:** To verify that changes in a specific area of the application have not affected other parts of the application
- **Test Cases Included:**
  - Test cases related to the specific area where changes were made
  - Test cases that cover the integration points of the affected area
- **Example:** If changes were made to the user profile model
  - Test008: Verify password reset functionality with an invalid email address
  - Test009: Verify updating user profile information
  - Test010: Verify changing user password

### Other Test Plan Examples

#### Integration Test Plan

To verify that different modules or services of the application work together as expected

- Test cases that validate the interaction between different modules
- Test cases that check data flow between integrated components

#### User Acceptance Test (UAT) Plan

To ensure the system meets the business requirements and is ready for production use

- Test cases based on real-world scenarios and user stories
- Test cases that validate end-to-end business processes

#### Load Test Plan

To determine how the system performs under heavy load conditions

- Test cases that simulate high user traffic
- Test cases that measure response times and system behavior under load

#### Security Test Plan

To identify and mitigate security vulnerabilities in the application

- Test cases that check for common security issues like SQL injection, XSS, and CSRF
- Test cases that validate user authentication and authorization mechanisms

#### Compatibility Test Plan

To ensure the application works across different devices, browsers, and operating systems

- Test cases that validate functionality on various devices and browsers
- Test cases that check for consistent user experiences across platforms

#### Recovery Test Plan

To verify the system's ability to recover from crashes, hardware failures, or other catastrophic problems

- Test cases that simulate system failures and recovery processes
- Test cases that validate data integrity after recovery

#### Localization Test Plan

To ensure the application is correctly adapted for different languages and regions

- Test cases that validate language translations
- Test cases that check for region specific content

### How to Group Test Cases into a Test Plan

1. **Identify the Scope:** Determine the scope of each test plan based on testing objectives
2. **Select Relevant Test Cases:** Choose test cases that align with the scope and objectives of each test plan
3. **Organize Test Cases:** Group the selected test cases into the respective test plans
4. **Review and Validate:** Review the grouped test cases to ensure they cover all necessary aspects and validate them with stakeholders if needed
5. **Document the Test Plans:** Clearly document each test plan, including the purpose, scope, and list of test cases

## Resources

- [The One Page Test Plan](https://www.ministryoftesting.com/articles/the-one-page-test-plan)
- [One-Page Test Plan | Write your Plan in Minutes](https://www.youtube.com/watch?v=BYN6AFhR4GE)

</section>
</details>

<details>
<summary>译文</summary>
<section>

# 测试规划

**组织**：微软（Microsoft）— Engineering Fundamentals Playbook（ISE 团队）
**来源**：[code-with-engineering-playbook](https://github.com/microsoft/code-with-engineering-playbook)
**最后更新**：2025 年 4 月 17 日

## 测试规划

在思考如何测试我们的应用程序时，我们应当是有意为之的。确保我们测试了正确内容的一种方法，就是针对各种场景构建测试计划，并在用户故事的设计阶段就制定出测试用例。

本文旨在展示一些关于测试规划的思考方式，并以一个带有登录门户的网站为例给出示例。

## 为用户故事构建测试用例

当我们为用户故事设计代码时，可以首先定义一组测试用例，以确保所有验收标准都得到满足。

这可以作为一项由开发人员和其他利益相关者共同参与的练习来完成。根据具体情况，部分测试用例最初可能是手动的，部分则可能计划用于自动化。

进行这项练习不仅会产生测试用例，还有助于澄清验收标准，并指导我们应当如何构建解决方案。

1. **理解验收标准**——彻底阅读并理解该用户故事的验收标准。与产品负责人或利益相关者澄清任何歧义。
2. **识别测试场景**——同时考虑正向与负向场景（快乐路径与错误情况），以覆盖边界情况。确定哪些在范围内、哪些在范围外，即我们是只测试功能需求，还是将安全、可访问性、可靠性等非功能需求也纳入测试范围？
3. **定义测试用例**——针对每个测试场景，定义详细的测试用例。每个测试用例都应记录以下内容：
   - **测试用例标题**：正在测试什么
   - **前置条件**：执行测试前所需的任何设置或测试数据
   - **测试步骤**：执行测试的分步说明
   - **预期结果**：测试的预期结果

   测试可以用 Given-When-Then 格式来描述，使其清晰简洁：
   **Given**（给定）初始上下文或状态，**When**（当）动作或事件发生时，**Then**（则）产生精确的结果
4. **尽可能自动化**——如果可行，将测试用例自动化。重点自动化热路径和关键区域。
5. **评审与完善**——与同事或利益相关者一起评审测试用例，确保我们已覆盖所有想覆盖的内容，且预期结果正确。根据反馈完善测试用例。

### 使用 Given-When-Then 格式的测试用例示例

**用户登录（正向测试用例）**

- **标题**：验证使用有效凭据的用户登录
- **前置条件**：用户位于登录页面
- **测试步骤**：给定用户位于登录页面，当用户输入有效凭据并点击登录按钮时，则用户应被重定向到仪表盘
- **预期结果**：用户成功登录并被重定向到仪表盘

**使用无效凭据的用户登录（负向测试用例）**

- **标题**：验证使用无效凭据的用户登录
- **前置条件**：用户位于登录页面
- **测试步骤**：给定用户位于登录页面，当用户输入无效凭据并点击登录按钮时，则用户应看到一条提示用户名或密码无效的错误消息
- **预期结果**：显示错误消息，用户停留在登录页面

**登录页面的安全测试（非功能需求）**

- **标题**：验证登录页面能够抵御 SQL 注入攻击
- **前置条件**：用户位于登录页面
- **测试步骤**：给定用户位于登录页面，当用户在用户名字段中输入 SQL 注入字符串（例如 `' OR '1'=1`）并点击登录按钮时，则系统不应允许登录，并应显示错误消息
- **预期结果**：系统阻止登录并显示错误消息

**表单验证的可用性测试（非功能需求）**

- **标题**：验证注册表单对无效输入提供清晰的错误消息
- **前置条件**：用户位于注册页面
- **测试步骤**：给定用户位于注册页面，当用户输入无效数据（例如错误的邮箱格式）并提交表单时，则系统应显示一条清晰且具体的错误消息，指出问题所在
- **预期结果**：显示清晰且具体的错误消息

**系统正常运行时间的可靠性测试（非功能需求）**

- **标题**：验证系统在一个月内保持 99.9% 的正常运行时间
- **前置条件**：系统在一个月内受到监控
- **测试步骤**：给定系统已启动并运行，当系统在一个月内被监控正常运行时间时，则系统应保持 99.9% 的正常运行时间
- **预期结果**：系统在监控期间保持 99.9% 的正常运行时间

## 将测试用例分组为测试计划

我们可以创建不同的测试计划，例如完整的回归测试计划、冒烟测试计划、功能测试计划等，并将测试用例组织到这些测试计划之下。

创建测试计划的一些好处包括：

- 我们可以确保应用程序的所有方面都得到测试，包括功能、非功能和边界情况
- 它们提供了明确的目标和范围，帮助开发人员理解需要测试什么
- 它们有助于系统地管理和执行测试，即我们拥有一套用于验证集成等的测试套件
- 通过基于风险识别和优先排序测试用例，测试计划帮助我们聚焦于应用程序最关键的区域
- 在某些行业中，它们是满足标准和法规合规性所必需的
- 它们帮助我们理解哪些测试最值得自动化

### 常见测试计划

#### 完整回归测试计划

- **目的**：验证最近的变更未对现有功能产生不利影响
- **包含的测试用例**：
  - 所有功能测试用例
  - 所有集成测试用例
  - 所有系统测试用例
  - 所有此前已报告并已修复的缺陷
- **示例**：
  - Test001：验证使用有效凭据的用户登录
  - Test002：验证使用有效信息的用户注册
  - Test003：验证密码重置功能

#### 冒烟测试计划

- **目的**：执行快速检查，确保应用程序最关键的功能正常工作
- **包含的测试用例**：
  - 基本功能测试用例
  - 覆盖核心功能的高优先级测试用例
- **示例**：
  - Test001：验证使用有效凭据的用户登录
  - Test004：验证向购物车添加商品
  - Test005：验证使用有效关键词的搜索功能

#### 功能测试计划

- **目的**：验证软件应用程序的每个功能都符合规格说明
- **包含的测试用例**：
  - 验证特定功能的测试用例
  - 覆盖用户交互和业务逻辑的测试用例
- **示例**：
  - Test002：验证使用有效信息的用户注册
  - Test006：验证使用无效凭据的用户登录
  - Test005：验证缺少必填字段的用户注册

#### 区域回归测试计划

- **目的**：验证应用程序特定区域的变更未影响应用程序的其他部分
- **包含的测试用例**：
  - 与发生变更的特定区域相关的测试用例
  - 覆盖受影响区域集成点的测试用例
- **示例**：如果对用户资料模型进行了变更
  - Test008：验证使用无效邮箱地址的密码重置功能
  - Test009：验证更新用户资料信息
  - Test010：验证修改用户密码

### 其他测试计划示例

#### 集成测试计划

验证应用程序的不同模块或服务是否按预期协同工作

- 验证不同模块之间交互的测试用例
- 检查集成组件之间数据流的测试用例

#### 用户验收测试（UAT）计划

确保系统满足业务需求并已准备好投入生产使用

- 基于真实场景和用户故事的测试用例
- 验证端到端业务流程的测试用例

#### 负载测试计划

确定系统在重负载条件下的表现

- 模拟高用户流量的测试用例
- 测量响应时间和负载下系统行为的测试用例

#### 安全测试计划

识别并缓解应用程序中的安全漏洞

- 检查 SQL 注入、XSS 和 CSRF 等常见安全问题的测试用例
- 验证用户认证和授权机制的测试用例

#### 兼容性测试计划

确保应用程序在不同设备、浏览器和操作系统上都能正常工作

- 验证在各种设备和浏览器上功能的测试用例
- 检查跨平台一致用户体验的测试用例

#### 恢复测试计划

验证系统从崩溃、硬件故障或其他灾难性问题中恢复的能力

- 模拟系统故障和恢复过程的测试用例
- 验证恢复后数据完整性的测试用例

#### 本地化测试计划

确保应用程序针对不同语言和地区进行了正确适配

- 验证语言翻译的测试用例
- 检查地区特定内容的测试用例

### 如何将测试用例分组为测试计划

1. **确定范围**：根据测试目标确定每个测试计划的范围
2. **选择相关测试用例**：选择与每个测试计划的范围和目标相一致的测试用例
3. **组织测试用例**：将选定的测试用例分组到相应的测试计划中
4. **评审与验证**：评审分组后的测试用例，确保它们覆盖所有必要方面，并在需要时与利益相关者一起验证
5. **记录测试计划**：清晰地记录每个测试计划，包括目的、范围和测试用例列表

## 参考资料

- [The One Page Test Plan](https://www.ministryoftesting.com/articles/the-one-page-test-plan)
- [One-Page Test Plan | Write your Plan in Minutes](https://www.youtube.com/watch?v=BYN6AFhR4GE)

</section>
</details>

## 摘要

本文是微软 Engineering Fundamentals Playbook（工程基础手册）中“自动化测试”章节下的一篇工程实践指南，主题为“测试规划”。文章主张在用户故事的设计阶段就着手构建测试计划与测试用例，并给出了一套五步流程：理解验收标准、识别测试场景、定义测试用例、尽可能自动化、评审与完善。文章以带登录门户的网站为例，示范了如何用 Given-When-Then 格式编写正向、负向及非功能（安全、可用性、可靠性）测试用例，随后系统梳理了完整回归、冒烟、功能、区域回归等常见测试计划，以及集成、UAT、负载、安全、兼容性、恢复、本地化等专项测试计划，最后给出将测试用例分组为测试计划的五步方法。全文是一份面向工程团队的、以实践为导向的测试规划入门指南。

## 术语表

| 术语 | 全称 | 解释 |
| :--- | :--- | :--- |
| Acceptance Criteria（验收标准） | Acceptance Criteria（AC） | 产品、用户故事或工作增量必须满足、才能被客户或产品负责人接受的条件集合，具有“通过/不通过”的二元性质，描述“做什么”而非“怎么做”。它与“完成定义”（Definition of Done）不同：前者针对单个待办项，后者是适用于所有待办项的通用质量清单。 |
| User Story（用户故事） | User Story | 从用户视角出发、对软件功能的一段简短描述，常用模板为“作为（某类用户），我希望（做某事），以便（获得某种收益）”。它本质上是“指向需求的指针”，遵循“卡片、对话、确认”三要素模型。 |
| Given-When-Then（GWT 格式） | Given-When-Then | 由 Dan North 与 Chris Matts 在行为驱动开发（BDD）中提出的、用规格说明方式描述系统行为的模板，将场景拆分为 Given（前置状态）、When（动作）、Then（可观察结果）三段，常配合 Cucumber 的 Gherkin 语言使用。 |
| Happy Path（快乐路径） | Happy Path | 系统在无错误、无异常情况下按预期执行的默认路径；与之相对的是负向测试（Negative Testing），即以非预期方式使用系统，验证其在无效输入下不会崩溃或产生不良结果。 |
| Edge Cases（边界情况） | Edge Cases | 仅在操作参数处于极端值（最大或最小值）时才会出现的问题或情形，单元测试常围绕这些边界条件编写。与之相关但不同的是“角落情况”（Corner Case），指多个环境条件同时处于极端水平时才出现的问题。 |
| Non-functional Requirements（非功能需求） | Non-functional Requirements（NFR） | 用于评判系统“运行质量”的标准（如性能、安全、可用性），与定义“系统做什么”的功能需求相对，常被称为“质量属性”或“ilities”。ISO/IEC 25010 标准提供了定义与度量非功能需求的权威框架。 |
| SQL Injection（SQL 注入） | SQL Injection（SQLi） | 攻击者通过客户端输入向应用程序注入 SQL 查询、从而影响预定义 SQL 命令执行的注入攻击。在 OWASP Top 10:2025 中位列 A05，首选防御手段是使用预编译语句（参数化查询）。 |
| XSS（跨站脚本） | Cross-Site Scripting | 攻击者将恶意脚本注入可信网站、使其在受害者浏览器中执行的注入攻击，可窃取 Cookie、会话令牌等敏感信息，分为反射型、存储型与基于 DOM 的三类。 |
| CSRF（跨站请求伪造） | Cross-Site Request Forgery | 攻击者诱使已认证用户在其不知情的情况下执行非预期操作的攻击，主要针对改变状态的请求，常见防御手段包括 CSRF Token、SameSite Cookie 等。 |
| Regression Test（回归测试） | Regression Testing | 对已测试过的程序在修改后重新进行的测试，以确保变更未在未变更区域引入缺陷，属于“变更相关测试”，与仅重跑失败用例的“复测”（Re-testing）不同。 |
| Smoke Test（冒烟测试） | Smoke Test | 覆盖组件或系统主要功能、用于在正式测试前判断其是否可正常工作的测试套件，同义词包括“健全性测试”（Sanity Test）等，名称源于硬件测试中通电检查电路板是否冒烟的做法。 |
| Functional Test（功能测试） | Functional Testing | 为评估组件或系统是否满足功能需求而执行的测试，关注系统“做什么”，与非功能测试相对。 |
| Integration Test（集成测试） | Integration Testing | 为暴露已集成组件或系统之间接口与交互中的缺陷而执行的测试，在 ISTQB 框架中属于“测试级别”，分为组件集成测试与系统集成测试两个层次。 |
| User Acceptance Test（用户验收测试） | User Acceptance Testing（UAT） | 为确定目标用户是否接受系统而执行的一种验收测试，由客户或最终用户执行，是产品发布前验证系统是否满足真实用户需求的最终检查。 |
| Load Test（负载测试） | Load Testing | 一种性能测试，用于在负载不断增加的情况下评估组件或系统的行为，以确定其能承受的负载水平，与压力测试、尖峰测试等同属性能测试范畴。 |
| Security Test（安全测试） | Security Testing | 为确定组件或系统安全性而执行的测试，相关技术包括渗透测试与模糊测试，ISTQB 设有专门的 Security Test Engineer 认证大纲。 |
| Compatibility Test（兼容性测试） | Compatibility Testing | 针对“兼容性”这一质量特性（组件或系统与其他组件交换信息、并在共享环境时执行所需功能的能力）的非功能测试，相关子概念包括互操作性与共存性。 |
| Recovery Test（恢复测试） | Recovery Testing | 为确定软件产品可恢复性而执行的测试，可恢复性指软件在发生故障时重新建立指定性能水平并恢复受影响数据的能力，是可靠性的子特性。 |
| Localization Test（本地化测试） | Localization Testing（l10n Testing） | 验证软件能否在特定语言与地理区域正确使用的测试，本地化（l10n）指将已国际化的软件适配到特定区域或语言，国际化（i18n）则指设计软件使其无需工程改动即可适配多种语言与区域。 |
| Product Owner（产品负责人） | Product Owner（PO） | Scrum 团队中负责最大化产品价值、并对产品待办列表进行有效管理的角色，是单一的个人而非委员会，只有产品负责人有权取消 Sprint。 |
| Hot Path（热路径） | Hot Path | 程序中执行频率最高的代码路径，与之相对的是很少执行的“冷路径”。根据帕累托原则，约 80% 至 90% 的执行时间集中在 10% 至 20% 的代码上，优化热路径能带来最大性能收益。 |
| 99.9% Uptime（可用性） | Availability（99.9% Uptime） | 系统在约定时间内可正常使用的时间比例，99.9% 可用性（“三个九”）意味着每年允许约 8 小时 45 分钟的停机时间，通常通过 SLI、SLO、SLA 三个层次来定义与管理。 |

## 深度解读

### 核心论点：测试规划应当前置到设计阶段

本文最核心的主张，是把测试规划从“编码完成之后”提前到“用户故事的设计阶段”。文章开篇即强调“我们应当是有意为之的”（We should be intentional），并明确指出“在用户故事的设计阶段就制定出测试用例”是确保“测试了正确内容”的方法。

这一主张背后是软件工程中一个被反复验证的共识：缺陷发现得越早，修复成本越低。测试用例的编写过程本身会反向澄清需求——文章特别点出，这项练习“不仅会产生测试用例，还有助于澄清验收标准，并指导我们应当如何构建解决方案”。这意味着测试规划在这里被赋予了双重职能：既是质量保障手段，也是需求澄清与设计工具。这与行为驱动开发（BDD）的理念一脉相承——BDD 主张在编码前先用 Given-When-Then 等自然语言描述行为，让业务、开发、测试三方在“做什么”上先达成一致。

值得注意的是，文章将这项练习定位为“由开发人员和其他利益相关者共同参与”的协作活动，而非测试人员的专属工作。这反映了现代敏捷团队中“质量是全员责任”（Quality is everyone's responsibility）的取向，也与微软自身在 DevOps 与“Shift-Left Testing”（测试左移）上的实践一致。

### 方法论维度：Given-When-Then 与测试用例的结构化

文章给出的测试用例结构——标题、前置条件、测试步骤、预期结果——是业界通用的测试用例四要素，而 Given-When-Then 则是其“测试步骤”字段的推荐表达方式。

Given-When-Then 的价值在于其“规格说明”性质：它用接近自然语言的、可读性极强的三段式结构，把“前置状态—触发动作—预期结果”的因果链条表达清楚。这一格式由 Dan North 与 Chris Matts 在提出 BDD 时创建，Martin Fowler 在其 Bliki 中确认它是对“四阶段测试”（Setup、Exercise、Verify、Teardown）与 Arrange-Act-Assert 模式的重构。文章中的五个示例（正向登录、负向登录、SQL 注入防护、表单校验、99.9% 可用性）恰好覆盖了功能、安全、可用性、可靠性四类需求，示范了同一格式如何统一表达不同性质的测试意图。

一个值得注意的细节是，文章把 SQL 注入、表单校验、99.9% 可用性都明确标注为“非功能需求”（Non-Functional Requirement）测试。这纠正了一个常见误区：非功能需求（性能、安全、可靠性、可用性）同样可以、也应当被写成可执行的测试用例，而非停留在模糊的“系统要快、要安全”的口号层面。把“99.9% 可用性”写成一条 Given-When-Then 用例，正是把 SLA 目标转化为可验证、可度量的测试断言的具体示范。

### 测试计划的分类逻辑：从“变更相关”到“质量属性”

文章对测试计划的梳理，实际上隐含了一套清晰的分类逻辑：

- **按变更范围划分**：完整回归测试计划（全量）、区域回归测试计划（局部）、冒烟测试计划（快速核心检查）。这三者对应的是“变更相关测试”的不同粒度——从“改了什么就测什么”到“全量兜底”。
- **按测试级别划分**：功能测试计划、集成测试计划、用户验收测试计划，对应 ISTQB 框架中的测试级别（组件、集成、系统、验收）。
- **按质量属性划分**：负载（性能）、安全、兼容性、恢复（可靠性）、本地化，对应 ISO/IEC 25010 中的非功能质量特性。

这套分类与 ISTQB 官方术语表高度吻合。ISTQB 将“测试级别”（Component、Integration、System、Acceptance）与“测试类型”（Functional、Non-functional、Black-box、White-box）作为正交维度区分，而文章中的“完整回归、冒烟、功能、区域回归”以及“集成、UAT、负载、安全、兼容性、恢复、本地化”正是这两个维度的具体落地。这说明文章并非微软自创的一套术语，而是对国际公认测试标准（ISTQB、ISO 25010）的工程化转述，具有较高的权威性与通用性。

### 实践指导价值：一份可操作的入门清单

本文的实践价值在于其“可操作性”。它没有停留在抽象原则，而是给出了：

1. 一套五步的测试用例构建流程（理解验收标准 → 识别测试场景 → 定义测试用例 → 自动化 → 评审）；
2. 五个可直接套用的 Given-When-Then 示例；
3. 十一种测试计划的“目的 + 包含用例 + 示例”模板；
4. 一套五步的用例分组方法。

对于刚接触测试规划的工程团队，这几乎是一份“照着做即可”的清单。文章末尾推荐的两个资源——Ministry of Testing 的《The One Page Test Plan》与 Daniel Knott 的《One-Page Test Plan | Write your Plan in Minutes》——进一步强化了其“轻量、务实”的取向：主张用一页纸的篇幅让忙碌的干系人真正阅读测试计划，而非堆砌冗长的文档。

不过，也需指出本文的边界：它是一份“入门级”指南，聚焦于“如何组织测试用例与测试计划”这一规划层面，并未深入讨论测试自动化框架选型、测试数据管理、测试环境治理、测试度量与覆盖率等更进阶的工程议题。读者应将其视为测试规划的起点，而非终点。

### 真实性评估

| 声明/事实 | 验证状态 | 说明 |
| :--- | :--- | :--- |
| 本文出自微软官方“Code With Engineering Playbook” | 已验证 | 该仓库位于微软官方 GitHub 组织 `microsoft/` 下，正式名称为“Engineering Fundamentals Playbook”，由微软 ISE（Industry Solutions Engineering）团队维护，约 2677 stars、679 forks，创建于 2018 年 7 月。 |
| Given-When-Then 是公认的 BDD 标准格式 | 已验证 | 由 Dan North 与 Chris Matts 在提出 BDD 时创建，Martin Fowler 的 Bliki 与 Cucumber 官方文档（Gherkin）均确认其为标准格式。 |
| Smoke / Regression / UAT / Load 等是 ISTQB 认可的标准测试类型 | 已验证 | 均为 ISTQB 官方术语表（v3.7/v4.2/v4.5）收录的标准术语，定义与文章用法一致。 |
| SQL 注入、XSS、CSRF 是常见 Web 安全漏洞 | 已验证 | 均为 OWASP 官方文档收录的经典 Web 攻击类型，SQL 注入在 OWASP Top 10:2025 中位列 A05。 |
| 99.9% 可用性（“三个九”）是常见 SLA 目标 | 已验证 | IBM 官方文档与 uptime.is 均确认 99.9% 可用性意味着每年约 8 小时 45 分钟停机时间。 |
| 文章引用的《The One Page Test Plan》资源真实可信 | 已验证 | 出自知名测试社区 Ministry of Testing，原作者 Claire Reckless（2016 年），后由 Ady Stokes 审校更新（2025 年）。 |
| 文章引用的 YouTube 视频《One-Page Test Plan》真实可信 | 已验证 | 作者为 Daniel Knott（频道“Adventures in QA”），16 年以上测试经验，现任德国 TK 公司 Head of Product Engineering，持有 ISTQB 认证。 |

### 总结

本文是微软 Engineering Fundamentals Playbook 中一篇以实践为导向的测试规划入门指南，其核心价值在于把“测试规划前置到设计阶段”这一理念，转化为一套可操作的流程、模板与示例。文章使用的术语（Given-When-Then、冒烟测试、回归测试、UAT、负载测试等）均与国际公认标准（ISTQB、ISO 25010、OWASP）高度一致，引用的外部资源也真实可信，整体权威性与可靠性较高。其局限在于聚焦规划层面、未深入自动化与度量等进阶议题，适合作为工程团队建立测试规划能力的起点。

**关键要点：**

- 测试规划应前置到用户故事的设计阶段，测试用例的编写过程本身能反向澄清验收标准、指导设计。
- Given-When-Then 是表达测试用例的公认标准格式，可统一表达功能与非功能（安全、可用性、可靠性）测试意图。
- 测试计划可按“变更范围”（回归/冒烟）、“测试级别”（功能/集成/UAT）、“质量属性”（负载/安全/兼容性/恢复/本地化）三个维度分类，与 ISTQB、ISO 25010 标准一致。
- 文章是一份权威、可信、可操作的入门指南，但未覆盖测试自动化框架、测试度量等进阶议题。

## 参考资料

- [Microsoft：code-with-engineering-playbook（GitHub 仓库）](https://github.com/microsoft/code-with-engineering-playbook) — 本文所属的微软官方工程实践手册仓库。
- [Microsoft：Engineering Fundamentals Playbook 发布站点](https://microsoft.github.io/code-with-engineering-playbook/) — 本文所在手册的官方发布站点。
- [Martin Fowler：GivenWhenThen](https://martinfowler.com/bliki/GivenWhenThen.html) — 确认 Given-When-Then 格式的起源与定义。
- [Cucumber：Gherkin](https://cucumber.io/docs/gherkin/) — Given-When-Then 作为可执行规格语言的官方说明。
- [ISTQB：Standard Glossary of Terms](https://www.ctqb.org/en/downloads/istqb.html?file=files%2Fcontent%2Fctqb%2Fdownloads%2Fistqb%2FGlossary-terms-version-3.7.pdf) — 冒烟测试、回归测试、UAT、负载测试等术语的权威定义。
- [OWASP：SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection) — SQL 注入攻击的权威说明。
- [Ministry of Testing：The One Page Test Plan](https://www.ministryoftesting.com/articles/the-one-page-test-plan) — 文章引用的“一页测试计划”资源。
- [Daniel Knott：One-Page Test Plan | Write your Plan in Minutes（YouTube）](https://www.youtube.com/watch?v=BYN6AFhR4GE) — 文章引用的“一页测试计划”视频资源。
