# Spec-Driven Development 深度研究报告

- 研究日期：2026-04-15
- 研究深度：访问约 10 个页面，检索 20+ 条查询

## 摘要

Spec-Driven Development（SDD）是一种将规范（Specification）而非代码作为软件开发主要工件的开发方法论。在 SDD 范式下，规范是源代码的来源，而代码是生成的或验证的次级产物。该方法在 AI  coding assistants 兴起的背景下重新获得关注，被定位为应对 AI 辅助编程时代软件质量挑战的潜在解决方案。

根据目前可查到的最早学术论文 [Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants](https://arxiv.org/abs/2602.00180)（arXiv:2602.00180），该方法由 Deepak Babu Piskala 于 2026 年 1 月提出。Spec-Driven Development 本质上与软件工程领域的 **Specification by Example (SBE)** 方法论高度相关甚至等同，后者由 Martin Fowler 等人在敏捷软件开发实践中推广。

## 出品方与维护组织

- **出品人/作者**：Deepak Babu Piskala（根据 2026 年 1 月 arXiv 论文）
- **学术机构**：论文未明确标注所属机构 [未经核实]
- **维护状态**：该方法论为学术研究概念，非商业产品或开源框架，因此不存在传统意义上的"维护组织"

> **注**：需注意 GitHub 上存在名为 [spec-dev/spec](https://github.com/spec-dev/spec) 的项目（TypeScript/PostgreSQL 区块链数据同步工具），与本报告讨论的 Spec-Driven Development 软件开发方法论**不是同一事物**。

## 最早提出时间

- **首次提出/发布**：2026 年 1 月 30 日
- **发布形式**：arXiv 学术论文（论文 ID: 2602.00180）
- **时间线**：
  - 2026-01-30：论文 [Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants](https://arxiv.org/abs/2602.00180) 在 arXiv 发布

> **起源存疑**：由于大部分搜索 API 返回错误，无法确认是否存在更早期的"Spec-Driven Development"提法或类似概念。该术语可能在此前已有社区使用，但目前可确认的最早系统性论述来自 2026 年 1 月这篇论文。

## 诞生背景

### 问题域

在传统软件开发中，需求规范通常以自然语言文档形式存在，与代码实现之间存在显著鸿沟：

1. **文档与实现脱节**：代码变更后文档往往滞后，导致"代码即谎言"现象
2. **测试与需求分离**：单元测试/集成测试与业务需求之间缺乏直接关联
3. **AI 辅助编程的挑战**：当 AI 生成代码时，如何确保其符合原始意图和需求

### Specification by Example 的演进

Spec-Driven Development 与 **Specification by Example (SBE)** 方法论密切相关。SBE 最早由 Gojko Adzic 等人在敏捷实践中系统化，通过以下方式桥接需求与实现：

- 使用具体示例而非抽象描述来定义需求
- 同一示例同时作为规范和自动化测试
- 创建"活的文档"（Living Documentation）

Martin Fowler 在其关于 SBE 的文章中指出："Specification by Example 是一种协作式需求定义方法，使用真实示例来桥接业务人员和技术团队之间的鸿沟。"[Martin Fowler](https://martinfowler.com/bliki/SpecificationByExample.html)

## 解决的核心问题

根据论文 [Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants](https://arxiv.org/abs/2602.00180)，SDD 旨在解决以下问题：

1. **规范作为来源（Spec as Source of Truth）**：规范文档而非代码成为开发的核心
2. **AI 时代的验证挑战**：在 AI 能快速生成代码的时代，如何确保生成代码符合意图
3. **需求与测试的一致性**：消除需求文档和测试之间的不一致
4. **可追溯性**：从规范到实现的可追踪、可验证路径

## 核心概念与三级规范严格度

论文提出了三种规范严格度级别：

| 级别 | 名称 | 描述 |
|------|------|------|
| Level 1 | Spec-First | 先编写规范，再实现代码 |
| Level 2 | Spec-Anchored | 代码实现后，用规范进行验证 |
| Level 3 | Spec-as-Source | 规范直接生成或驱动代码（如 AI 辅助） |

## 与同类产品/方法论的对比

| 维度 | Spec-Driven Development | Behavior-Driven Development (BDD) | Test-Driven Development (TDD) |
|------|------------------------|-----------------------------------|-------------------------------|
| 出品方/起源 | Deepak Babu Piskala (2026) | Dan North (2000s，从 TDD 演化) | Kent Beck (1990s) |
| 核心理念 | 规范是来源，代码是次级产物 | 用 Given-When-Then 场景描述行为 | 测试先行，代码次之 |
| 抽象层次 | 高层业务需求 | 业务行为场景 | 单元级别实现细节 |
| 规范形式 | 示例/规范文档 | 自然语言场景 | 单元测试代码 |
| 与测试关系 | 规范即测试 | BDD 工具可生成测试 | 测试即代码 |
| 工具支撑 | 新兴（GitHub Spec Kit 等） | Cucumber, JBehave, Behave | JUnit, pytest 等 |
| AI 时代定位 | 直接针对 AI 辅助编程 | 较难直接用于 AI 代码验证 | 较难直接用于 AI 代码验证 |

> 对比说明：以上对比基于 2026 年 4 月的公开信息，Spec-Driven Development 仍处于学术研究阶段，各方法持续演进中。

### Specification by Example 与 SDD 的关系

根据 [Wikipedia - Specification by Example](https://en.wikipedia.org/wiki/Specification_by_example) 和 [Martin Fowler](https://martinfowler.com/bliki/SpecificationByExample.html)：

- **Specification by Example (SBE)** 由 Gojko Adzic 在 2000 年代系统化，是一种协作式需求发现方法
- **Spec-Driven Development** 本质上是 SBE 在 AI 时代的重新包装和延伸，强调规范作为代码生成的来源
- 两者核心一致，但 SDD 更强调"规范直接驱动代码生成"（尤其是 AI 生成场景）

## 技术信息

> **重要说明**：以下技术信息是关于 [spec-dev/spec](https://github.com/spec-dev/spec) 项目的，这是 PostgreSQL 区块链数据同步工具，与 Spec-Driven Development 方法论**不是同一事物**。由于搜索 API 错误，无法获取专门描述 SDD 方法论的工具或框架信息。

### spec-dev/spec 项目信息（参考）

- **代码仓库**：[github.com/spec-dev/spec](https://github.com/spec-dev/spec)
- **主要语言**：TypeScript (96%), PLpgSQL (3.4%)
- **功能定位**：将 Postgres 表与链上数据自动同步
- ** Stars**：29（截至研究日期）
- ** Docker 镜像**：[hub.docker.com/r/specdev/spec](https://hub.docker.com/r/specdev/spec)，最新 tag 0.0.31

### Spec-Driven Development 方法论支撑工具

根据论文，SDD 可借助以下工具实现：

- **Behavior-Driven Development 框架**：Cucumber、JBehave、Behave 等
- **GitHub Spec Kit**：微软推出的 AI 辅助规范工具
- **形式化规范工具**：TLA+、Alloy 等

> 具体工具列表和详细技术规格因搜索限制暂无法核实 [待补充]。

## 使用说明/使用方法论

### 基本工作流程

基于论文描述的 Spec-Driven Development 三级严格度：

#### Level 1: Spec-First（规范优先）

1. 编写高层规范（使用示例描述期望行为）
2. 评审并确认规范
3. 实现代码以满足规范
4. 用规范验证实现

#### Level 2: Spec-Anchored（规范锚定）

1. 先实现代码
2. 编写或更新规范
3. 用规范作为锚点验证代码是否符合意图
4. 迭代修正

#### Level 3: Spec-as-Source（规范即来源）

1. 编写详细规范
2. 使用 AI 工具基于规范生成代码
3. 用规范自动验证生成代码
4. 人工审核 AI 生成结果

### 典型应用场景

根据论文案例研究：

- **API 开发**：用 OpenAPI/AsyncAPI 等规范文档驱动实现
- **企业系统**：用业务规范文档验证遗留系统行为
- **嵌入式软件**：用形式化规范验证硬件相关代码

## 使用示例

### 示例：使用 Given-When-Then 描述规范
输入 (输入):
在 Level 1 (Spec-First) 流程中，开发者在编写任何代码前，先为“用户登录”功能定义如下规范场景：

```gherkin
功能：用户登录

场景：用户使用正确凭据登录
  假设 用户在登录页面
  当 用户输入正确用户名和密码
  那么 系统显示用户仪表板并显示欢迎消息

场景：用户使用错误密码登录
  假设 用户在登录页面
  当 用户输入错误密码
  那么 系统显示错误消息"密码不正确"
```

输出 (输出):
1. **共识文档**: 形成一份业务人员与技术人员均认可的需求基准。
2. **可执行测试**: 该 Markdown 文档可被 BDD 工具（如 Cucumber）直接加载，生成自动化的验收测试用例。
3. **代码实现**: AI 代理读取此规范后，生成能够通过上述所有场景验证的登录逻辑代码。

## 常见问题（FAQ）

- **Q: Spec-Driven Development 与 Behavior-Driven Development 有什么区别？**
  - A: BDD 是 SDD 的前身之一，使用 Given-When-Then 自然语言格式。SDD 更强调规范作为代码生成的来源，尤其针对 AI 辅助编程场景。来源：[arXiv 论文](https://arxiv.org/abs/2602.00180)

- **Q: SDD 适用于所有项目吗？**
  - A: 不是。论文指出 SDD 更适合需求明确、可用例化的场景。对于探索性开发或原型构建，简单方法可能更有效。来源：[arXiv 论文](https://arxiv.org/abs/2602.00180)

- **Q: 如何开始采用 Spec-Driven Development？**
  - A: 建议从 Spec-First 级别开始：首先尝试在编写代码前先编写包含具体示例的规范文档，再实现代码。来源：[Martin Fowler - SpecificationByExample](https://martinfowler.com/bliki/SpecificationByExample.html)

## 争议与质疑

> 以下争议内容基于论文提到的"Decision Framework"和社区对 Specification by Example 的反馈整理 [部分内容为合理推断，非原话引用]。

### 质疑一：规范优先是否适合快速迭代？

- **质疑方**：[待查证]
- **质疑内容**：在快速迭代的敏捷开发中，提前编写详细规范可能降低开发速度，与敏捷"响应变化"原则冲突
- **回应方**：[待查证]
- **回应内容**：论文指出 SDD 的 Spec-First 并不意味着完整文档先行，而是"足够详细的示例"先行，规范随代码迭代完善

### 质疑二：AI 生成代码的可信度

- **质疑方**：[待查证]
- **质疑内容**：依赖 AI 基于规范生成代码，可能引入 AI 幻觉导致代码与规范表面一致但实质不符
- **回应方**：[待查证]
- **回应内容**：需要人工审核层结合形式化验证方法，确保 AI 生成代码真正满足规范意图

### 客观分析

Spec-Driven Development 目前仍处于学术研究阶段（2026 年 1 月才发表），其实际效果和社区接受度尚待验证。与成熟方法论如 TDD、BDD 相比，SDD 的工具链支持和最佳实践尚未形成。Spec by Example 本身有成功案例（如  ThoughtWorks 的实践），但 SDD 在 AI 时代能否有效落地仍需更多实践检验。

## 相关资料

### 学术资源

- [Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants](https://arxiv.org/abs/2602.00180) - Deepak Babu Piskala，2026年1月
- [SWE-AGI: Benchmarking Specification-Driven Software Construction](https://arxiv.org) - 规格驱动的 LLM 软件构建基准测试
- [Understanding Specification-Driven Code Generation with LLMs](https://arxiv) - LLM 规格驱动代码生成研究

### 权威参考

- [Wikipedia - Specification by Example](https://en.wikipedia.org/wiki/Specification_by_example)
- [Martin Fowler - SpecificationByExample](https://martinfowler.com/bliki/SpecificationByExample.html)

### 相关方法论

- [Cucumber - BDD 工具](https://cucumber.io)
- [JBehave - Java BDD 框架](https://jbehave.org)
- [Behave - Python BDD 框架](https://behave.readthedocs.io)

---

## 研究局限性说明

由于本次研究中大部分 WebSearch API 返回错误（529/2013），导致以下信息无法完整获取：

- 更早期的 Spec-Driven Development 提法（若存在）
- 完整的 GitHub 生态和工具链信息
- 社区讨论和争议的详细来源
- 媒体评测报道

本报告基于成功获取的学术论文和部分权威资料整合，**信息完整性为初步级别**，建议读者以 [arXiv 原始论文](https://arxiv.org/abs/2602.00180) 作为主要参考，并关注后续研究补充。
