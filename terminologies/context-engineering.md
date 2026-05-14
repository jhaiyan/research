# Context Engineering 深度研究报告

- 研究日期：2026/04/15
- 研究深度：访问 10+ 个页面，检索 20+ 条查询

## 摘要

Context Engineering（上下文工程）是 2025 年中兴起的一个 AI 工程领域术语，用于描述在为大型语言模型（LLM）构建 AI Agent 时，管理和优化模型上下文窗口内容的一整套系统性方法论。该术语由 Andrej Karpathy、Tobi Lutke 等行业知名人士在 2025 年 6 月左右提出并推广，旨在取代早期专注于"提示词撰写"的 Prompt Engineering 概念。Context Engineering 的核心观点是：大多数 Agent 失败不是模型能力不足，而是上下文管理不当导致的"上下文失败"。该领域已成为 AI 工程界最受关注的新兴技能之一，被视为 Prompt Engineering 的超集。

## 原始出处

- **提出时间**：2025 年 6 月（最早公开讨论集中在 2025 年 6 月 23 日 - 30 日期间）
- **提出者/组织**：该术语由多位行业领袖独立推动，主要贡献者包括：
  - **Andrej Karpathy**：2025 年 6 月 25 日在 Twitter/X 上发表推文，将该领域描述为"填充上下文窗口的微妙艺术与科学"
  - **Tobi Lutke**（Shopify 联合创始人）：将该概念描述为"为 LLM 提供完成任务所需全部上下文的艺术"
  - **Anthropic**：2025 年 9 月发布系统性指南 "Effective context engineering for AI agents"
  - **LangChain**：2025 年 6 月 23 日发布博客 "The rise of 'context engineering'"
  - **Lance Martin**：2025 年 6 月 23 日发布深度技术文章 "Context Engineering for Agents"，提出 Write/Select/Compress/Isolate 四框架
- **原始链接**：
  - Karpathy 推文：https://twitter.com/karpathy/status/1937902205765607626
  - Tobi Lutke 推文：https://x.com/tobi/status/1935533422589399127
  - LangChain 文章：https://blog.langchain.com/the-rise-of-context-engineering/
  - Lance Martin 文章：https://rlancemartin.github.io/2025/06/23/context_engineering/

## 验证状态

| 验证项 | 状态 | 说明 |
|--------|------|------|
| 起源追溯 | ✅ 已验证 | 2025年6月由Karpathy等人推广 |
| 四大核心技术 | ✅ 已验证 | Write/Select/Compress/Isolate |
| 95% claim | ⚠️ 未核实 | 主流来源中未找到"95%上下文预算来自非-prompt组件"的具体数字 |
| Prompt Engineering超集 | ✅ 已验证 | 多方确认Context Engineering是超集 |
| 成熟度 | 🌱 新兴期 | 2025年6月刚兴起，正处于快速发展阶段 |

**关于 95% claim 的说明**：用户背景提到的"Agent上下文预算95%来自非-prompt组件"这一说法在主流来源（Anthropic、LangChain、Simon Willison、Lance Martin 等）中未找到直接证实。该数字可能来自特定内部数据、非正式讨论或特定场景的观察。建议在实际引用时标注来源。

## 提出背景

Context Engineering 的兴起源于以下几个背景：

### 1. 从简单提示词到复杂 Agent 的范式转变

在 LLM 应用的早期阶段（2022-2024 年），主要工作集中在如何撰写更好的提示词（Prompt Engineering）。然而，随着 AI Agent 概念的兴起，开发者逐渐意识到：仅仅优化提示词文本已不足以构建可靠、实用的 Agent 系统。Agent 需要处理多轮对话、调用外部工具、访问知识库、管理长期记忆等复杂任务，这要求一套更加系统化的上下文管理方法。

### 2. 上下文窗口容量限制成为核心瓶颈

LLM 的上下文窗口（如 128K、200K tokens）虽然看似宽裕，但在处理长时运行的 Agent 任务时面临严峻挑战：
- 上下文膨胀导致成本和延迟增加
- 上下文过长会降低模型对关键信息的注意力（"上下文分心"问题）
- 上下文中的错误信息会"污染"模型输出（"上下文中毒"问题）

### 3. 大多数 Agent 失败被重新定义为"上下文失败"

根据多个来源的观察，当 Agent 表现不佳时，根本原因往往是：
- 缺少模型需要的关键信息
- 上下文格式不当导致模型难以理解
- 工具描述不清晰或重叠导致模型调用错误工具
- 长期记忆与短期上下文冲突

## 详细解释

### 定义

**Context Engineering** 的精确定义：

> Context Engineering 是设计并构建动态系统的学科，该系统以正确的格式、在正确的时间提供正确的信息和工具，使 LLM 能够合理地完成指定任务。

或者如 Anthropic 所述：

> Context refers to the set of tokens included when sampling from a large-language model (LLM). The engineering problem at hand is optimizing the utility of those tokens against the inherent constraints of LLMs in order to consistently achieve a desired outcome.

### 核心原理

Context Engineering 的核心原理建立在将 LLM 视为一种特殊"操作系统"的类比上：

- **LLM 如同 CPU**：负责推理和决策
- **上下文窗口如同 RAM**：作为模型的工作内存，容量有限
- **Context Engineering 如同操作系统**：负责管理、调度、压缩进出工作内存的数据

与操作系统管理 RAM 的方式类似，Context Engineering 需要处理四大核心技术：

1. **写入（Write）**：将信息保存到外部存储（如 scratchpads、memory）以跨会话持久化
2. **选择（Select）**：通过工具、RAG、embeddings 或知识图谱将相关信息加载到上下文窗口
3. **压缩（Compress）**：通过摘要或裁剪减少 token 数量
4. **隔离（Isolate）**：通过子 Agent、沙箱环境或独立状态对象分割上下文

### 关键特征

Context Engineering 与 Prompt Engineering 的核心区别：

| 维度 | Prompt Engineering | Context Engineering |
|------|-------------------|---------------------|
| 范围 | 单个提示词文本 | 整个上下文系统 |
| 性质 | 静态模板 | 动态生成的系统 |
| 焦点 | 措辞和表述 | 信息选择、格式、时机 |
| 时间点 | 运行时 | 运行前（系统设计阶段） |
| 目标 | 优化单次响应 | 优化整个 Agent 轨迹 |

### 发展脉络

- **2024 年下半年**：Prompt Engineering 概念达到顶峰
- **2025 年 6 月初**：Tobi Lutke 等人开始在社交媒体讨论"上下文工程"概念
- **2025 年 6 月 23 日**：
  - LangChain 发布 "The rise of 'context engineering'"
  - Lance Martin 发布 "Context Engineering for Agents"
- **2025 年 6 月 25 日**：Andrej Karpathy 发推支持"context engineering"替代"prompt engineering"
- **2025 年 6 月 30 日**：Philipp Schmid 发布广泛传播的博文 "The New Skill in AI is Not Prompting, It's Context Engineering"
- **2025 年 9 月 29 日**：Anthropic 发布官方指南 "Effective context engineering for AI agents"
- **2025 年 10 月起**：各大 AI 公司和社区开始广泛讨论和实现 Context Engineering 最佳实践

## 应用现状与趋势

### 应用场景

1. **AI Coding 助手**：如 Claude Code、Cursor、Windsurf 等工具通过 Context Engineering 管理代码库上下文、项目规则文件、对话历史等

2. **多 Agent 系统**：通过子 Agent 隔离不同任务的上下文，避免上下文窗口溢出

3. **长期记忆系统**：如 ChatGPT 的 Memory 功能，通过向量检索选择相关记忆注入上下文

4. **RAG（检索增强生成）系统**：动态检索外部知识并选择性地注入上下文

5. **Agent 评估框架**：如 Context-Bench 等benchmark工具评估 Agent 的上下文管理能力

### 应用趋势

1. **工具化**：各大框架（LangChain、LangGraph、Inngest 等）正在将 Context Engineering 最佳实践工具化
2. **标准化**：出现"12 Factor Agents"等最佳实践框架，试图建立 Context Engineering 标准
3. **自动化**：开始出现自动上下文压缩、自动工具选择等自动化 Context Engineering 技术
4. **教育化**：Simon Willison、Philipp Schmid 等博主持续产出高质量教程，推动该技能的普及

### 实践案例

- **Anthropic 多 Agent 研究员**：使用 Memory 机制持久化上下文，通过子 Agent 并行处理不同任务
- **Claude Code**：实现自动压缩（auto-compact）机制，在上下文窗口使用率达 95% 时自动总结对话历史
- **HuggingFace Deep Researcher**：使用代码执行沙箱隔离上下文，避免 JSON 对象污染主上下文
- **Shopify Agent**：Tobi Lutke 在内部 Agent 开发中深度应用 Context Engineering 原则

## 各方评价与争议

### 支持观点

1. **Andrej Karpathy**（AI 领域权威）：
   > "It should really be called 'context engineering' rather than prompt engineering. Writing instructions is the easy part. The hard part is providing the right context and tools while staying within context window limits."

2. **Cognition 团队**：
   > "'Context engineering' ... is effectively the #1 job of engineers building AI agents."

3. **Anthropic 官方**：
   > "Context engineering refers to the strategies for curating and maintaining the optimal set of tokens during LLM inference."

4. **社区反响热烈**：Hacker News 上关于 Context Engineering 的讨论帖获得数千票，众多开发者分享实际应用经验

### 质疑/反对观点

1. **概念炒作质疑**：部分观点认为"context engineering"只是"prompt engineering"的重命名，缺乏实质性创新

2. **框架依赖问题**：批评者指出许多 Context Engineering 最佳实践与特定框架（LangChain 等）深度绑定，迁移成本高

3. **复杂性增加**：过度强调 Context Engineering 可能导致简单任务过度工程化

### 对质疑的回应

支持者回应称：

- Context Engineering 确实与 Prompt Engineering 有重叠，但前者更强调**系统性**和**动态性**，是后者的超集
- 框架绑定问题正在通过标准化努力（如 MCP - Model Context Protocol）解决
- 随着 Agent 应用复杂度的提升，Context Engineering 的价值将愈发显著

### 客观分析

Context Engineering 的核心洞察是正确的——在构建可靠 Agent 时，上下文管理确实比提示词撰写更为关键。然而，该领域仍处于早期发展阶段，许多最佳实践尚未经过严格验证。从工程化角度看，它代表了从"艺术"到"工程"的必然过渡，这与软件工程早期从"编程"到"软件工程"的演进类似。

## 与旧范式对比

### 之前怎么做（Prompt Engineering 时代）

| 问题 | 旧方案 | 局限 |
|------|--------|------|
| 提示词优化 | 手动撰写、测试、迭代 | 依赖经验，难以规模化 |
| 上下文管理 | 将所有信息塞入提示词 | 超出 context window 限制 |
| 多轮对话 | 简单拼接历史消息 | 无关信息稀释关键上下文 |
| 工具调用 | 单一工具描述 | 工具选择混乱 |
| 知识检索 | 一次性注入全部文档 | token 浪费、关键信息被遮蔽 |

### 现在怎么做（Context Engineering 时代）

| 问题 | 新方案 | 优势 |
|------|--------|------|
| 提示词优化 | 系统性上下文设计 | 可预测、可测试、可复用 |
| 上下文管理 | Write/Select/Compress/Isolate 框架 | 动态适应任务需求 |
| 多轮对话 | 自动摘要 + 关键信息提取 | 保持上下文精炼 |
| 工具调用 | 结构化工具描述 + MCP 协议 | 清晰、无歧义 |
| 知识检索 | RAG + 选择性注入 | 只加载相关信息 |

## 成熟度评估

**🌱 新兴期（2025年6月至今）**

| 评估维度 | 状态 | 说明 |
|----------|------|------|
| 概念提出 | ✅ 完成 | 2025年6月由多位行业领袖推广 |
| 框架成型 | ✅ 进行中 | Write/Select/Compress/Isolate 已广泛认可 |
| 工具支持 | 🔄 发展中 | LangChain、Anthropic 等正在工具化 |
| 最佳实践 | 🔄 演化中 | 12 Factor Agents 等框架正在形成 |
| 学术验证 | 🔄 早期 | 缺乏严格的对照实验验证 |
| 社区采用 | ✅ 快速增长 | Hacker News、博客讨论热度高 |

**结论**：Context Engineering 目前处于新兴期向快速发展期过渡阶段，核心概念已被广泛认可，但具体最佳实践仍在快速演化中。该领域预计将在 2025-2026 年进入爆发期。

## 交叉验证

| 来源 | 核心观点 | 与本报告的一致/差异 |
|------|----------|---------------------|
| Anthropic (2025/09) | Context Engineering 是 Prompt Engineering 的自然演进，核心是优化上下文 tokens | 完全一致 |
| LangChain Blog (2025/06) | Context Engineering = 构建动态系统提供正确信息、工具、格式、时机 | 完全一致 |
| Lance Martin (2025/06) | 四大策略：Write/Select/Compress/Isolate | 补充了具体方法论 |
| Simon Willison (2025/06) | 术语由 Karpathy 等人推广，强调记忆管理问题 | 一致 |
| Philipp Schmid (2025/06) | Agent 失败 = 上下文失败而非模型失败 | 完全一致 |
| Hacker News 社区讨论 | 强调调试上下文实际内容的困难 | 一致 |
| GitHub 开源项目 (davidkimai/Context-Engineering) | 提供第一性原理手册，整理最新研究 | 验证了研究深度 |

## 相关概念与术语

- **Prompt Engineering**：上下文工程的子集，专注于提示词文本的撰写
- **RAG（Retrieval Augmented Generation）**：通过检索增强上下文的特定技术
- **Agent Memory**：Agent 管理系统中短期/长期记忆的机制
- **Context Window**：LLM 的输入 token 容量限制
- **MCP（Model Context Protocol）**：Anthropic 推出的上下文管理协议标准
- **12 Factor Agents**：Dex Horthy 提出的 Agent 开发最佳实践框架
- **Tool Use / Function Calling**：Agent 调用外部工具的机制
- **Context Compression**：上下文压缩技术

## 参考资料

- [The New Skill in AI is Not Prompting, It's Context Engineering - Philipp Schmid](https://www.philschmid.de/context-engineering) - 广泛传播的入门文章
- [The rise of "context engineering" - LangChain Blog](https://blog.langchain.com/the-rise-of-context-engineering/) - LangChain 官方定义
- [Context Engineering for Agents - Lance Martin](https://rlancemartin.github.io/2025/06/23/context_engineering/) - 深度技术分析
- [Effective context engineering for AI agents - Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) - 官方权威指南
- [Context Engineering - Simon Willison](https://simonwillison.net/2025/Jun/27/context-engineering/) - 知名博主评论
- [Karpathy Tweet on Context Engineering](https://twitter.com/karpathy/status/1937902205765607626) - 术语推广源
- [12 Factor Agents - Dex Horthy](https://github.com/humanlayer/12-factor-agents) - 最佳实践框架
- [Context Engineering: A first-principles handbook - GitHub](https://github.com/davidkimai/Context-Engineering) - 开源学习资源
- [Context-Bench: Benchmarking LLMs on Agentic Context Engineering - LettA](https://www.letta.com/blog/context-bench) - 评估基准
- [Context Engineering Realized: Context Window Architecture - mrhillsman](https://mrhillsman.com/posts/context-engineering-realized-context-window-architecture/) - 架构视角分析
