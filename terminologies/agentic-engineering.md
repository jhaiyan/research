# Agentic Engineering 深度研究报告

- 研究日期：2026/04/15
- 研究深度：访问 5 个页面，检索 5 条查询

## 摘要

Agentic Engineering 是由技术博主 Simon Willison 于 2026 年 2 月 23 日提出的术语，指的是利用编码 Agent（如 Claude Code、OpenAI Codex）辅助软件开发的新兴工程学科。其核心特征是 Agent 能够生成并执行代码，从而独立测试和迭代代码。该术语与 Karpathy 提出的 "vibe coding" 形成对比，代表专业软件工程师利用 AI 放大自身专业能力的工程实践。当前处于快速发展期，Simon Willison 正在建立系统的 "Agentic Engineering Patterns" 指南。

## 原始出处

- **提出时间**：2026 年 2 月 23 日
- **提出者/组织**：Simon Willison（独立技术博主、DataSette 作者）
- **原始链接**：https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/

## 提出背景

### 问题

随着 LLM 能力的提升，如何有效地将 AI 编码工具整合到专业软件开发流程中？传统的 "vibe coding" 模式（完全忽视代码、由非程序员使用）已无法满足专业工程师的需求。

### 之前的解决方案

- **Vibe Coding**：Karpathy 于 2025 年 2 月提出，指完全依赖 LLM 生成代码、忽略代码本身的开发方式，主要服务于非程序员快速原型开发
- **AI 辅助编程**：早期聊天式 AI 工具（如 ChatGPT 聊天）仅能逐轮交互，无法自主执行和迭代

### 新方案

Agentic Engineering 强调专业工程师主导、人机协作的范式：工程师编排自主执行代码的 Agent，通过迭代实现目标。

## 详细解释

### 定义

> "I'm using Agentic Engineering to refer to building software using coding agents — tools like Claude Code and OpenAI Codex, where the defining feature is that they can both generate and execute code — allowing them to test that code and iterate on it independently of turn-by-turn guidance from their human supervisor."
> — Simon Willison, 2026/02/23

### 核心原理

- **Agent 定义**：软件调用 LLM 并传递工具定义，LLM 请求执行工具，结果反馈给 LLM，形成循环
- **编码 Agent 特征**：具备代码生成和执行能力，可在循环中迭代直到达成目标
- **代码执行是决定性能力**：没有代码执行能力，LLM 输出的代码价值有限；具备执行能力后，Agent 才能开始迭代

### 与 Vibe Coding 的对比

| 维度 | Vibe Coding | Agentic Engineering |
|------|-------------|---------------------|
| 提出者 | Andrej Karpathy (2025/02) | Simon Willison (2026/02) |
| 主体 | 非程序员 | 专业软件工程师 |
| 代码态度 | 完全忽视 | 积极审查和管理 |
| 人类参与 | 最低限度 | 人类编排主导 |
| 代码质量 | 原型级、未审查 | 生产级、经过审查 |

### 关键特征

1. **自主迭代**：Agent 可独立测试和修正代码
2. **人类编排**：工程师定义目标、审查结果、管理方向
3. **工程纪律**：强调模式、最佳实践（如 TDD、Git、代码审查）
4. **知识积累**：Simon Willison 正在建立 "Agentic Engineering Patterns" 指南

### 发展脉络

- **2025 年 2 月**：Karpathy 提出 "vibe coding"
- **2025 年 12 月**：Karpathy 指出"编码 Agent 基本上从 12 月才开始工作"
- **2026 年 2 月 23 日**：Simon Willison 正式提出 "Agentic Engineering" 并启动Patterns 项目
- **2026 年 3 月 15 日**：发布 "What is agentic engineering?" 指南章节
- **2026 年 3-4 月**：持续发布更多Patterns 章节（red/green TDD、subagents、Git 等）

## 应用现状与趋势

### 应用场景

1. **生产级代码开发**：专业工程师使用 Agent 构建经过审查的生产代码
2. **自动化重构**：通过编码 Agent 执行大规模代码改进
3. **实验驱动优化**：Karpathy 的 autoresearch 模式——Agent 运行数百个半自主实验
4. **工具构建**：Simon Willison 用 Agent 构建 scan-for-secrets 等工具

### 应用趋势

- Google 工程圈 AI 采用曲线：20% Agentic power users，20% 拒绝者，60% 仍使用聊天式工具
- Shopify 使用 autoresearch 模式实现 53% 解析性能提升
- 持续有初创公司和开源项目采用 Agentic Engineering 实践

### 实践案例

- **scan-for-secrets**：Simon Willison 使用 red/green TDD 模式，通过 Claude Code 构建的秘钥检测工具
- **autoresearch**：Karpathy 的实验自动化系统，用于 nanochat 训练优化
- **JSONata 重写**：$400 和 7 小时完成 Go 实现迁移

## 各方评价与争议

### 支持观点

- Karpathy 本人对编码 Agent 能力转变持积极态度（"basically didn't work before December and basically work since"）
- Simon Willison 认为这是专业工程师的全新工作方式
- Matt Webb 强调 Agent 能高效处理问题，但架构设计仍需人类

### 质疑/反对观点

- Mario Zechner 警告：Agent 会产生复合错误，建议限制 AI 生成代码的每日量
- Max Woolf 进行了详细测试，记录了编码 Agent 的能力与局限
- Thomas Ptacek 等安全研究者关注 Agent 生成代码的安全风险

### 客观分析

Agentic Engineering 目前处于快速发展阶段，实践者社区正在形成。它代表了对 vibe coding 极端化的纠正，强调工程纪律而非放弃代码审查。核心挑战在于：如何平衡自动化效率与代码质量控制。

## 交叉验证

| 来源 | 核心观点 | 与本报告的一致/差异 |
|------|----------|---------------------|
| Simon Willison 博客 | Agentic Engineering = 编码 Agent 辅助开发，专业工程师主导 | 完全一致 |
| Karpathy Twitter | 编码 Agent 在 2025 年 12 月能力突变 | 一致，提供了背景信息 |
| Simon Willison 指南 "What is agentic engineering" | 明确定义 agent、coding agent，强调代码执行是核心 | 一致 |
| Hacker News 讨论 | Agentic engineering 作为新兴实践被讨论 | 一致 |

## 相关概念与术语

- **Vibe Coding**：Karpathy 提出的极端 AI 辅助编程方式，Agentic Engineering 的对比基准
- **Coding Agent**：能够生成和执行代码的 AI 工具（Claude Code、Codex 等）
- **Agentic**：更广泛的术语，指代理性质的 AI 系统
- **Autoresearch**：Karpathy 的实验自动化模式
- **Red/Green TDD**：Simon Willison 强调的测试驱动开发模式

## 参考资料

- [Agentic Engineering Patterns - Simon Willison](https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/) - 术语首次提出
- [What is agentic engineering? - Simon Willison 指南](https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/) - 详细定义
- [Karpathy Twitter (2026/02/26)](https://twitter.com/karpathy/status/2026731645169185220) - 关于编码 Agent 能力转变
- [Simon Willison 博客 - Andrej Karpathy 引用](https://simonwillison.net/2026/Feb/26/andrej-karpathy/) - Karpathy 观点记录
- [scan-for-secrets 项目](https://simonwillison.net/2026/Apr/5/scan-for-secrets/) - Agentic Engineering 实践案例