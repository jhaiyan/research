# 深度研究报告：Agent Skills（智能体技能）

- 报告生成时间：2026-05-21 13:35
- 主题类型：概念（Concept）

## 概述

- 提出方：尚无单一明确提出方，概念源自多方研究者的逐步探索
- 提出时间：2023 年 2 月（Toolformer 论文可追溯为最早的相关开创性工作）
- 领域：人工智能、LLM Agent、大语言模型工具使用

Agent Skills 是指 AI 智能体（Agent）所拥有的离散化、可组合的能力单元。这些技能通常包括：描述（说明技能做什么）、动作/函数（可执行的逻辑或 API 调用）、参数（技能接受的输入）。这一概念从 2023 年初的工具调用研究逐步演化而来，到 2026 年已形成较为完整的技术体系。

## 提出背景/解决的核心问题

### 起源时间线

**2023 年 2 月 9 日** - **Toolformer** 论文（arXiv:2302.04761）发布，由 Timo Schick 等研究者提出。该论文首次系统性地展示了语言模型如何通过简单 API 自监督地学习使用外部工具，被广泛视为 Agent Skills 概念的奠基性工作。

> "LMs can teach themselves to use external tools via simple APIs"
> "decide which APIs to call, when to call them, what arguments to pass"

**2023 年 3 月 30 日** - **HuggingGPT** 论文（arXiv:2303.17580）发布，提出用 LLM 作为控制器管理现有 AI 模型，通过语言作为通用接口连接不同模态的 AI 模型。

**2023 年 5 月** - **Voyager** 论文（arXiv:2305.16291）发布，首次为 Minecraft 智能体引入了"不断扩展的技能库"（ever-growing skill library）概念，使用可执行代码存储和检索复杂行为。

### 核心问题

早期 AI 系统缺乏灵活调用外部工具和能力的能力。Agent Skills 概念解决了以下问题：
1. 如何让 LLM 智能体具备调用工具的能力
2. 如何组织、管理和复用智能体的能力单元
3. 如何实现技能的组合、分解和动态调用

## 发展历程

- **2023 年 2 月 9 日** - Timo Schick 等发布 [Toolformer 论文](https://arxiv.org/abs/2302.04761)，奠定工具调用基础
- **2023 年 3 月 30 日** - Yongliang Shen 等发布 [HuggingGPT 论文](https://arxiv.org/abs/2303.17580)，LLM 作为控制器
- **2023 年 5 月** - [Voyager 论文](https://arxiv.org/abs/2305.16291) 发布，首提"技能库"概念
- **2024 年** - 多项后续研究深化技能学习与技能组合评估
- **2025-2026 年** - 技能系统研究快速增长，出现 SkillSmith、MIND-Skill 等专业化框架

## 适用场景

- **自主智能体**：如 Voyager 等游戏 AI 智能体
- **工具增强型 LLM**：如 Claude、ChatGPT 等通过工具调用扩展能力
- **医疗、工作流自动化**：Agent Skills for Healthcare 研究分析了 557 个医疗技能
- **代码生成与自动化**：LOOP Skill Engine 等用于周期性智能体任务
- **安全测试**：红队测试框架（如 Proteus）验证技能安全性

## 技术信息

### 技能的基本结构

```python
# Agent Skill 的典型结构
skill = {
    "name": "web_search",
    "description": "Search the web for current information",
    "parameters": {
        "query": {"type": "string", "required": True},
        "max_results": {"type": "integer", "default": 10}
    },
    "execute": lambda params: search_web(params["query"], params["max_results"])
}
```

### 关键论文技术对比

| 论文 | 时间 | 核心贡献 |
|------|------|----------|
| Toolformer | 2023年2月 | 自监督学习工具调用 |
| HuggingGPT | 2023年3月 | LLM 作为控制器 |
| Voyager | 2023年5月 | 技能库与技能组合 |
| SkillSmith | 2026年5月 | 技能编译减少冗余 |

## 与同类方案的对比

### 概念定义流派

| 研究团队 | 定义重点 | 代表论文 |
|----------|----------|----------|
| Schick 等 (Toolformer) | 工具调用为技能核心 | Toolformer |
| Voyager 团队 | 技能库为技能组织形式 | Voyager |
| SkillSmith 团队 | 技能编译与运行时优化 | SkillSmith |

### 核心理论差异

- **Toolformer 流派**：强调工具 API 调用作为技能实现方式
- **Voyager 流派**：强调技能的存储、检索和组合机制
- **SkillSmith 流派**：强调技能编译后的运行时效率优化

## 常见问题（FAQ）

- **Q：Agent Skills 和 Tool Use有什么区别？**
  A：Tool Use（工具使用）是 Agent Skills 的技术实现方式之一。Agent Skills 是一个更高级的概念，涵盖技能的描述、发现、组合和管理。

- **Q：谁 first 提出了 Agent Skills 概念？**
  A：没有单一的"发明者"。Toolformer 论文（2023年2月）可视为概念的技术奠基，但"Agent Skills"这一术语是逐步从多个研究团队的工作中演化而来。

- **Q：Agent Skills 与传统软件模块有何不同？**
  A：Agent Skills 设计用于 LLM 智能体上下文，包含自然语言描述、参数 schema 和执行逻辑，需要考虑 LLM 的理解能力和调用机制。

## 争议与质疑

- **术语模糊性**："Agent Skills" 一词被不同研究团队用于指代不同含义，缺乏统一标准定义
- **技能过多问题**：2026 年研究发现 80% 的技能偏离声明行为，18.9% 可追溯至恶意意图
- **技能价值质疑**："When Skills Don't Help"（2605.20023）论文指出在严格验证反馈环境下，技能的边际效益会消失

## 相关资料

- [Toolformer 论文 (arXiv:2302.04761)](https://arxiv.org/abs/2302.04761) - 工具调用奠基论文
- [HuggingGPT 论文 (arXiv:2303.17580)](https://arxiv.org/abs/2303.17580) - LLM 控制器
- [Voyager 论文 (arXiv:2305.16291)](https://arxiv.org/abs/2305.16291) - 技能库概念
- [SkillSmith 论文 (arXiv:2605.15215)](https://arxiv.org/abs/2605.15215) - 技能编译框架
- [Simon Willison's Blog](https://simonwillison.net) - AI Agent 研究
- [Martin Fowler's Blog](https://martinfowler.com) - 编码智能体架构
