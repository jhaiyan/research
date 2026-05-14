# Spec-Driven Development 深度研究报告

- 研究日期：2026-04-13
- 研究深度：访问 8 个页面，检索 6 条查询

## 摘要

Spec-Driven Development（SDD）是一种软件开发方法论，其核心特征是以形式化、机器可读的规范（specification）作为唯一真实来源（source of truth），实现、测试和文档均从该规范派生而来。该方法论可追溯至 1960 年代 NASA 的工作流程和早期形式化方法，但在学术上于 2004 年由 Ostroff、Makalsky 和 Paige 正式提出。随着 2020 年代大语言模型（LLM）驱动的智能体工作流程兴起，SDD 迎来了新一轮关注，被视为 AI 辅助工程的基础框架。

## 原始出处

- **提出时间**：2004 年（学术正式定义）；其思想根源可追溯至 1960 年代 NASA 工作流程
- **提出者/组织**：Ostroff、Makalsky 和 Paige 于 2004 年在 Lecture Notes in Computer Science 上发表论文 "Agile Specification-Driven Development"
- **原始链接**：<https://link.springer.com/chapter/10.1007/978-3-540-25937-4_9>

## 提出背景

> **重要说明**：经过对 Martin Fowler、Simon Willison、Chip Huyen、Robert C. Martin、Kent Beck、Andrej Karpathy 等权威技术专家博客的广泛搜索，**"Spec-Driven Development" 作为一个独立术语在这些博客中并未被直接使用**。更接近的知名概念是 **"Specification By Example"**（由 Martin Fowler 于 2004 年提出，Gojko Adzic 为主要推动者和《Specification by Example》一书的作者）。因此，"Spec-Driven Development" 可能是一个较少使用或较新的术语。

Spec-Driven Development 的提出旨在解决传统软件开发中需求、实现与测试之间容易出现不一致的问题。在 TDD（测试驱动开发）和 BDD（行为驱动开发）的基础上，SDD 进一步将规范提升至核心地位，试图建立一种更高层次的抽象，使得软件开发的各个阶段都围绕一个权威的规范文档展开。

其思想根源可追溯至 1960 年代 NASA 的工作流程和早期的形式化方法（formal methods），这些方法强调在编码之前进行逻辑验证。随着敏捷开发的兴起，研究者尝试将形式化方法的严谨性与敏捷的灵活性相结合，最终在 2004 年形成了正式的学术定义。

## 详细解释

### 定义

Spec-Driven Development 是一种软件开发方法论，其中形式化、机器可读的规范作为权威真实来源和主要制品（primary artifact），实现、测试和文档均从该规范派生。规范以结构化格式（如 OpenAPI 或 Markdown）编写，在编码开始之前完成定义。

### 核心原理

SDD 的核心原则是"**spec-as-source**"（规范即源代码）：规范被视作主要制品，而实现代码则成为规范维护的副产品，架构被视为可执行的控制平面。

### 关键特征

1. **机器可读规范**：使用形式化语言（如 OpenAPI）编写规范，确保规范可被工具解析和处理
2. **规范优先**：在编码之前先定义规范，规范驱动整个开发过程
3. **自动化派生**：实现、测试和文档从规范自动生成，而非手动编写
4. **版本控制**：规范如同代码一样进行版本管理

### 发展脉络

| 时间 | 里程碑 |
|------|--------|
| 1960 年代 | NASA 工作流程和形式化方法的早期实践 |
| 2004 年 | Ostroff、Makalsky、Paige 正式提出"Agile Specification-Driven Development" |
| 2020 年代 | LLM 驱动的智能体工作流程兴起，SDD 迎来复兴 |

## 应用现状与趋势

### 应用场景

1. **API 设计与开发**：使用 OpenAPI 规范先定义 API 结构，再生成服务器骨架和客户端库
2. **AI 辅助编程**：作为 LLM 智能体的工作框架，确保 AI 生成的代码符合预定义规范
3. **跨团队协作**：规范作为不同团队（前端、后端、测试）之间的共识基础
4. **形式化验证**：在安全关键系统中，使用规范进行逻辑验证

### 应用趋势

SDD 在 2020 年代经历了由 LLM 驱动的复兴。传统的"vibe coding"（直觉编码）模式难以保证 AI 生成代码的一致性，而 SDD 提供了一种结构化的框架来约束和引导 AI 辅助开发过程。Tessl 等平台的出现，将 SDD 理念应用于 AI 智能体技能管理，为智能体提供版本化、经过评估的技能和上下文。

### 实践案例

- **Tessl**：agent 使能平台，作为"agent 技能的包管理器"，为编码智能体提供结构化、版本化的上下文
- **Kiro**：Spec-Driven Development 相关工具
- **GitHub Spec Kit**：GitHub 推出的规范相关工具包

## 各方评价与争议

### 支持观点

- **结构化约束**：为 AI 辅助开发提供必要的结构约束，避免"vibe coding"带来的不一致性
- **一致性保证**：规范作为唯一真实来源，确保各制品之间的一致性
- **跨工具一致性**：Tessl 等平台强调"智能体在不同工具和项目中表现一致"

### 质疑/反对观点

- **BDD/Cucumber 的失败教训**：有评论指出"20 年前我们被告知 Cucumber 是 spec-driven development 的柏拉图式理想，但有人记得结果如何吗？"——暗示这种范式并未兑现承诺
- **XMPP 的失败案例**：XMPP 的规范驱动开发模型被认为是一个失败案例，因为实际实现往往先于标准化，规范难以约束真实实现
- **灵活性不足**：有观点认为行业正在向更灵活的 AI 辅助工作流程转变，开发者"在早期阶段更深入地挖掘需求"进行原型设计和探索性设计，而规范驱动的框架可能限制这种灵活性

### 对质疑的回应

SDD 的支持者认为，传统工具和实践的失败并不意味着范式本身有问题，而是工具和实施方式需要改进。LLM 驱动的智能体工作流程为 SDD 提供了新的技术基础，有望克服以往的工具局限性。

### 客观分析

Spec-Driven Development 代表了一种有价值的理念——通过形式化规范来驱动开发。然而，从历史经验看，规范驱动的方法在实施层面面临挑战：规范的编写和维护本身需要投入大量精力，规范与实现之间的迭代可能变得繁琐。SDD 的现代复兴是否能克服这些历史障碍，还有待观察。

## 交叉验证

| 来源 | 核心观点 | 与本报告的一致/差异 |
|------|----------|----------------------|
| Thoughtworks | 将 SDD 定义为以规范为核心的开发方法 | 一致：规范作为 source of truth |
| Baeldung | SDD 是 TDD 和 Design by Contract 的融合 | 一致：2004 年正式定义，与形式化方法的关联 |
| Lobsters 社区 | BDD/Cucumber 和 XMPP 的 spec-driven 模型均告失败 | 差异：强调了历史失败案例，本报告更侧重于方法论本身 |
| Tessl | 将 SDD 理念应用于 LLM 智能体技能管理 | 一致：确认 2020 年代 SDD 的 AI 驱动复兴 |

## 相关概念与术语

- **TDD（Test-Driven Development）**：测试驱动开发，SDD 使用规范生成初始测试，而非 TDD 的实现级正确性
- **BDD（Behavior-Driven Development）**：行为驱动开发，SDD 提供 BDD 场景必须满足的结构和架构不变量
- **Design by Contract**：契约式设计，SDD 继承了其形式化验证的思想
- **Specification By Example**：更广为人知的相关概念，由 Martin Fowler 于 2004 年提出，Gojko Adzic 为主要推动者
- **LLM Agentic Workflows**：LLM 驱动的智能体工作流程，SDD 为其提供结构化框架
- **OpenAPI Specification**：常用的机器可读规范格式

## 参考资料

- [Agile Specification-Driven Development (Ostroff et al., 2004)](https://link.springer.com/chapter/10.1007/978-3-540-25937-4_9) - 学术论文，SDD 的原始出处
- [Tessl.io](https://tessl.io) - agent 技能管理平台，SDD 理念的现代实践
- [Baeldung - Spec-Driven Development](https://www.baeldung.com/cs/spec-driven-development) - 方法论解释和与 TDD/BDD 的比较
- [Thoughtworks Insights - Spec-Driven Development](https://www.thoughtworks.com/insights/blog/spec-driven-development) - 方法论概述
- [Martin Fowler - Specification By Example](https://martinfowler.com/bliki/SpecificationByExample.html) - Specification By Example 的原始定义
- [Lobsters Discussion - Spec-Driven Development](https://lobste.rs/search?q=spec+driven+development) - 社区批评和争议讨论
