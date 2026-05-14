# Harness Engineering（驾驭式工程）🔥

- **研究日期**：2026/04/15
- **研究深度**：分析 4 个主要来源（Martin Fowler, Mitchell Hashimoto, OpenAI, LangChain），交叉验证 8+ 个独立来源

## 摘要

Harness Engineering 是 2026 年初兴起的一个 AI Agent 工程概念，指围绕 AI Coding Agent 构建约束机制、反馈回路和持续改进循环的系统工程实践。其核心公式为 **Agent = Model + Harness**，其中 Model 是通用商品，而 Harness（即除模型本身以外的一切：工具链、验证机制、架构约束、工作流控制）才是真正的差异化竞争力。多项独立实验表明，仅改变 Harness 而不修改模型权重，编码基准分数可从 6.7% 跃升至 68.3%。

---

## 详细深度报告

### 1. 起源追溯

- **提出者/组织**：**Mitchell Hashimoto**（HashiCorp 联合创始人、Terraform 创作者）
- **首次提出时间**：2026 年 2 月 5 日
- **原始出处**：[My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey)
- **原始措辞**：
  > "I don't know if there is a broad industry-accepted term for this yet, but I've grown to calling this 'harness engineering.' It is the idea that anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that mistake again."

- **系统性扩展**：
  - **Martin Fowler / Birgitta Böckeler**（Thoughtworks）于 2026 年 4 月 2 日发表 [Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html)，提出 Guides（引导/前馈）和 Sensors（传感器/反馈）的双框架
  - **LangChain** 博客定义了核心公式：**Agent = Model + Harness**
  - **OpenAI** 工程博客记录了 Codex 的完整 Harness 工程实践

### 2. 提出背景

**解决的核心问题**：如何让 AI Coding Agent 在生产环境中可靠运行，减少人工监督负担？

**之前怎么做**：
- 开发者与 Agent 反复交互，每次出错人工修正
- 无系统性反馈机制，Agent 重复犯同类错误
- 缺乏架构约束，代码随时间自然腐化

**现在怎么做**：
- 每当 Agent 犯错，将解决方案工程化为 Harness（如 Linter 规则、AGENTS.md 条款、测试套件）
- 建立前馈（Guides）+ 反馈（Sensors）双回路控制系统
- 架构约束机械化执行，文档即规则

### 3. 核心原理

#### 3.1 双回路控制系统

| 组件 | 类型 | 作用时机 | 示例 |
|------|------|----------|------|
| **Guides（引导）** | 前馈控制 | Agent 行动之前 | AGENTS.md、架构文档、codemods 脚本 |
| **Sensors（传感器）** | 反馈控制 | Agent 行动之后 | 测试、Linter、AI 代码审查、日志分析 |

#### 3.2 计算型 vs. 推理型控制

- **计算型**：确定性，毫秒级执行，测试/Linter/类型检查
- **推理型**：非确定性，GPU 执行，AI 代码审查/"LLM as Judge"

#### 3.3 三大调节维度

1. **可维护性 Harness**：代码质量、结构、风格（当前最成熟）
2. **架构适应性 Harness**：Fitness Functions（性能、可观测性约束）
3. **行为 Harness**：功能正确性验证（当前最难，开放问题）

### 4. 关键实践

#### AGENTS.md / CLAUDE.md
- 每一行规则对应一次历史 Agent 失败
- 放在仓库根目录，Agent 每次会话自动读取
- 示例：[Ghostty 项目的 AGENTS.md](https://github.com/ghostty-org/ghostty/blob/ca07f8c3f775fe437d46722db80a755c2b6e6399/src/inspector/AGENTS.md)

#### 架构约束机械化执行
- 文档不够，必须 Linter + 结构测试强制执行
- 错误消息直接包含修复指令（"正向 Prompt 注入"）

#### 熵管理（垃圾回收）
- 定期运行后台 Agent 扫描漂移，发起清理 PR
- 吞吐量与代码生成吞吐量成比例扩展

### 5. 成熟度评估：🔥 爆发期

**判断依据**：
- 2026 年 2 月至 4 月期间，多个独立来源快速涌现
- Mitchell Hashimoto（2/5）、Martin Fowler/Böckeler（4/2）、OpenAI 工程博客、Anthropic 长时间运行 Agent 研究、Stripe Minions 系统
- 多组独立实验数据支撑（Can.ac: 6.7%→68.3%；Pi Research: 15 个 LLM 提升）
- 社区讨论活跃（WeChat 多篇中文解读、知乎深度分析）

### 6. 交叉验证

| 来源 | 核心观点 | 一致性 |
|------|----------|--------|
| Mitchell Hashimoto | 每次 Agent 犯错 = 一次 Harness 改进机会 | 原始定义 |
| Martin Fowler/Böckeler | Guides + Sensors 双框架，三大调节维度 | 完全一致，系统化 |
| OpenAI Codex | 5 个月 100 万行代码，10 倍效率 | 验证了生产可行性 |
| Anthropic | 长时间 Agent 需要进度持久化 + 生成/评估分离 | 补充具体实现 |
| Stripe Minions | 每周 1300+ PR 无人值守，Blueprint 编排 | 验证规模化路径 |
| LangChain | Agent = Model + Harness | 概念公式化 |
| Pi Research | 改变 Harness 在一个下午提升 15 个 LLM | 实验数据支撑 |

### 7. 争议与质疑

#### 支持观点
- **"模型是商品，Harness 才是护城河"**：改变 Harness 而不改模型，基准分数可跃升 10 倍
- **模型越强，Harness 越重要**：Anthropic 发现 Opus 4.5→4.6 升级后，旧的约束拆掉，但新的更高阶约束空间打开

#### 主要质疑

**1. "Bitter Lesson"阵营（OpenAI 研究员 Noam Brown）**：
> "Harness 就像一根拐杖，我们终将超越它。"

- 推理模型出现后，许多 Agentic 系统（路由器、编排器）一夜之间过时
- 算力增长会碾平复杂 Harness 的价值

**2. 前期投入成本**：
- OpenAI 花了 5 个月构建自定义 Linter、结构测试、文档系统
- 大多数团队没有这样的资源

**3. 遗留代码库问题**：
- 所有成功案例均为绿地项目
- 遗留代码库如何引入 Harness Engineering：**零方法论**

**4. 功能行为验证困境**：
- AI 生成的测试套件质量存疑
- METR 数据：自动评分器高估 Agent 能力约 7 倍

### 8. 相关概念

- **Context Engineering**（上下文工程）：Harness Engineering 的子集，专注于上下文管理
- **Prompt Engineering**：单次输入优化，Harness Engineering 的子集
- **Agent Memory**：Agent 管理系统中短期/长期记忆的机制
- **MCP（Model Context Protocol）**：Anthropic 推出的上下文管理协议标准
- **Fitness Functions**：架构适应性 Harness 的具体实现

### 9. 参考资料

- [My AI Adoption Journey - Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey) - 术语首次提出（2026-02-05）
- [Harness engineering for coding agent users - Martin Fowler](https://martinfowler.com/articles/harness-engineering.html) - 系统性框架（2026-04-02，作者 Birgitta Böckeler）
- [OpenAI: Harness Engineering](https://openai.com/index/harness-engineering/) - Codex 生产实践
- [The Anatomy of an Agent - LangChain](https://blog.langchain.com/the-anatomy-of-an-agent-harness/) - Agent = Model + Harness 公式来源
- [Anthropic: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) - 长时间运行 Agent 研究
- [Stripe Minions: One-shot End-to-End Coding Agents](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents) - 无人值守规模化案例
- [AGENTS.md 标准](https://agents.md/) - Agent 规范文档最佳实践
- [Ghostty AGENTS.md 示例](https://github.com/ghostty-org/ghostty/blob/ca07f8c3f775fe437d46722db80a755c2b6e6399/src/inspector/AGENTS.md) - Mitchell Hashimoto 实际案例
