# 深度解读：Keep Agentic AI Simple: A Practical Workflow for Software Development

> 原文：[Keep Agentic AI Simple: A Practical Workflow for Software Development](https://timdeschryver.dev/blog/keep-agentic-ai-simple-a-practical-workflow-for-software-development)<br>
> 作者：Tim Deschryver<br>
> 日期：2026-05-07

## 原文及译文

<details>
<summary>原文</summary>
<section>

# Keep Agentic AI Simple: A Practical Workflow for Software Development

**Author:** Tim Deschryver
**Date:** May 07, 2026
**Website:** [timdeschryver.dev](https://timdeschryver.dev)

## Overview

Tim Deschryver shares his experience using Agentic AI in software development. He describes his approach using a cycling metaphor: viewing AI as a "domestique" who works for the team leader, rather than replacing the developer entirely. The goal is faster delivery while maintaining quality through proper guardrails and oversight.

## Architecture and Design

The author set up the project structure before using AI agents:

- ASP.NET API backend with Angular frontend
- Orchestrated by Aspire
- Vertical Slice architecture for .NET Minimal APIs
- Angular using Signal API features

## AGENTS.md File

The AGENTS.md file serves as a standard, tool-agnostic configuration that provides:

- Technology stack details
- Build, test, and lint commands
- Coding style and conventions
- Application flow overview
- Database diagrams in Mermaid syntax

This file is included in every AI request, making it essential to keep it current and aligned with project standards.

## Skills

Agent Skills are markdown files that extend agent capabilities. Key differentiators from AGENTS.md:

- Skills are contextually included when relevant
- They don't bloat the context window unnecessarily
- Can be invoked on demand using slash commands
- Centralized in `./agents/skills` or `./claude/skills`

The author recommends skills for Angular, .NET, and custom team-specific guidelines.

## Spec-Driven Development

Using OpenSpec, the author generates three documents for features:

- **proposal.md** - Functional analysis with summary, scope, and success criteria
- **design.md** - Technical design including APIs, components, and models
- **tasks.md** - Step-by-step implementation plan

This approach improves AI output quality by dividing work into manageable context steps.

## Tools and Models

Both Claude and Codex models perform similarly, with Claude slightly better for design tasks. OpenCode offers flexibility to use different models within the same tool.

## Workflow

The new workflow prioritizes:

1. Creating specifications using OpenSpec
2. Delegating implementation to AI agents
3. Testing and reviewing critical code paths
4. Using skills for documentation and commits

The author emphasizes treating custom components like external dependencies, focusing on public APIs rather than implementation details.

## Team Structure

More frequent reviews replace traditional sprint cycles. The author suggests:

- Product Owners becoming more critical for prioritization
- Potential shift toward developer-stakeholder pairing
- Frequent check-ins to catch misalignments early

## Conclusion

AI accelerates delivery when developers maintain ownership and provide clear guardrails. Starting simple and adding complexity gradually yields the best results.

</section>
</details>

<details>
<summary>译文</summary>
<section>

# 保持 Agentic AI 简洁：软件开发的实用工作流

**作者：** Tim Deschryver
**日期：** 2026年5月7日
**网站：** [timdeschryver.dev](https://timdeschryver.dev)

## 概述

Tim Deschryver 分享了他在软件开发中使用 Agentic AI 的经验。他用一个自行车比赛比喻来描述他的方法：将 AI 视为为队长（开发者）工作的"副将"（domestique），而不是完全取代开发者。目标是加速交付，同时通过适当的护栏和监督保持质量。

## 架构与设计

作者在使用 AI 代理之前设置了项目结构：

- ASP.NET API 后端 + Angular 前端
- 由 Aspire 编排
- 垂直切片架构用于 .NET Minimal APIs
- Angular 使用 Signal API 功能

## AGENTS.md 文件

AGENTS.md 文件作为标准、与工具无关的配置文件，提供：

- 技术栈详情
- 构建、测试和 lint 命令
- 编码风格和约定
- 应用流程概述
- Mermaid 语法的数据库图表

此文件包含在每个 AI 请求中，因此保持其最新状态并与项目标准对齐至关重要。

## 技能（Skills）

代理技能是扩展代理能力的 Markdown 文件。与 AGENTS.md 的关键区别：

- 技能在相关时上下文地包含
- 不会不必要地膨胀上下文窗口
- 可以使用斜杠命令按需调用
- 集中存储在 `./agents/skills` 或 `./claude/skills`

作者建议为 Angular、.NET 和团队特定指南创建技能文件。

## 规约驱动开发（Spec-Driven Development）

使用 OpenSpec，作者为每个功能生成三个文档：

- **proposal.md** - 功能分析，包含摘要、范围和成功标准
- **design.md** - 技术设计，包括 API、组件和模型
- **tasks.md** - 逐步实施计划

这种方法通过将工作分成可管理的上下文步骤来提高 AI 输出质量。

## 工具和模型

Claude 和 Codex 模型表现相似，Claude 在设计任务上略胜一筹。OpenCode 提供在同一工具内使用不同模型的灵活性。

## 工作流

新工作流优先考虑：

1. 使用 OpenSpec 创建规约
2. 将实施委托给 AI 代理
3. 测试和审查关键代码路径
4. 使用技能进行文档和提交

作者强调将自定义组件视为外部依赖，专注于公共 API 而非实现细节。

## 团队结构

更频繁的审查取代了传统的 Sprint 周期。作者建议：

- 产品负责人更加严格地进行优先级排序
- 可能转向开发者与利益相关者配对
- 频繁检查以尽早发现不对齐

## 结论

当开发者保持所有权并提供明确的护栏时，AI 可以加速交付。从简单开始，逐步增加复杂性会产生最佳结果。

</section>
</details>

## 摘要

本文是 Tim Deschryver 基于自身实践经验的分享，探讨如何在软件开发中有效使用 Agentic AI（代理式人工智能）。作者提出了一个核心比喻：AI 不是取代开发者的"霸主"，而是为开发者工作的"副将"（domestique）。文章详细介绍了他的技术栈选择（.NET Aspire + Angular + 垂直切片架构）、配置管理方案（AGENTS.md）、技能扩展机制、以及规约驱动开发（Spec-Driven Development）方法论。核心观点是：AI 加速交付的前提是开发者保持主导权和设定明确边界，从简单开始、逐步增加复杂性才能获得最佳效果。

## 术语表

| 术语 | 全称 | 解释 |
| :--- | :--- | :--- |
| **Agentic AI** | Agentic Artificial Intelligence（代理式人工智能） | 能够自主设定目标、使用工具并采取行动的 AI 系统，在人类定义的目标、约束和可用工具范围内运作。与传统 AI 需要逐步提示不同，Agentic AI 能执行复杂任务而无需持续人工监督 |
| **AGENTS.md** | Agents Markdown Configuration File | 一种 Markdown 格式的配置文件，被多种 AI 编码工具采用，用于定义项目编码标准、架构决策、构建命令等，被包含在每个 AI 请求中 |
| **Claude** | Claude | Anthropic 公司开发的 AI 模型家族，包括 Opus、Sonnet、Haiku 等变体。Claude Code 是其代理式编码工具，能读取代码库、编辑文件、运行命令 |
| **.NET Aspire** | Microsoft .NET Aspire | 微软推出的云原生应用编排平台，简化分布式系统的开发、配置、部署和监控，提供服务发现、健康检查、遥测等功能 |
| **垂直切片架构** | Vertical Slice Architecture | 将代码按业务用例而非技术层级组织的架构模式，每个"切片"包含一个业务功能所需的所有层级代码，便于独立迭代和维护 |
| **.NET Minimal APIs** | .NET Minimal APIs | .NET 6 引入的轻量级 API 开发范式，用最少样板代码创建 HTTP API，无需 Controller 类，直接将路由映射到方法 |
| **Angular Signal API** | Angular Signals | Angular 16+ 引入的响应式状态管理机制，通过"信号"实现精确变更检测，与 Zone.js 的全局 monkey-patch 不同，允许显式声明依赖关系 |
| **OpenSpec** | OpenSpec | Fission-AI 开发的规约驱动开发框架（55k Stars），为 AI 编程助手提供结构化的规范层，使用斜杠命令管理规约生命周期 |
| **Codex** | Codex | OpenAI 开发的代码生成模型，由 GPT-3 微调而来，是 GitHub Copilot 的底层技术支撑 |
| **规约驱动开发** | Spec-Driven Development (SDD) | 将规约作为唯一真相来源的开发方法论，规约包含用户故事、边缘情况、API 契约等，AI 根据规约生成实现代码 |
| **Domestique** | Domestique | 公路自行车赛中支援队长的副将角色，本文用此比喻 AI 是为开发者（队长）工作的辅助角色 |

## 深度解读

### 核心方法论：Agentic AI 作为"副将"而非"替代者"

本文最核心的观点在于作者提出的类比：Agentic AI 应该是为开发者工作的"副将"（domestique），而不是取代开发者的存在。这一比喻具有深刻的实践意义：

在职业自行车赛中，domestique 负责为队长的胜利提供支持——他们领骑、递送物资、阻挡风阻，但最终成绩属于队长。这一角色与作者设想的 AI 定位高度吻合：AI 承担执行层面的工作（编写测试、修复 lint 错误、实现具体功能），而战略决策、需求理解、代码审查仍由开发者掌控。

这种定位的优势在于：
- **质量控制**：开发者始终是最终责任方，AI 生成代码需经过人工审查
- **知识保留**：开发者在委托任务过程中保持对系统的理解
- **渐进式信任**：可以从简单任务开始，逐步扩展到复杂任务

### 技术架构：.NET 生态的现代化实践

作者选择的技术栈体现了 .NET 生态的现代化趋势：

**.NET Aspire** 作为编排层，解决了分布式系统的复杂性。在 AI Agent 场景下，这意味着可以将 LLM 调用、工具执行、记忆存储等组件清晰地组织在一起。Aspire 的声明式配置（App Host 模式）使得组件边界和依赖关系一目了然。

**垂直切片架构**则是对传统分层架构的革新。在传统分层架构中，修改一个业务功能需要跨越多个层级（Controller → Service → Repository），涉及多个文件；而垂直切片将相关代码（包括 API 端点、业务逻辑、数据访问）组织在同一个功能文件夹内。这种架构与 AI Agent 的任务分配模式天然契合——每个 Agent 可以专注于一个垂直切片，减少跨切片的协调成本。

**Angular Signal API** 的采用则体现了对性能的追求。传统的 Zone.js 变更检测是全局性的"猴子补丁"，而 Signals 采用 pull-based 模型，允许精确追踪依赖关系，实现精准更新。在 AI 应用场景中，这意味着 UI 可以精确响应 Agent 状态的变化。

### 配置管理：AGENTS.md 与 Skills 的分层策略

文章提出了一个精妙的配置分层策略：

**AGENTS.md** 是项目级配置文件，包含技术栈详情、构建命令、编码规范等不变信息。由于每次 AI 请求都会包含此文件，因此它提供了"项目记忆"，确保 AI 的输出与项目标准一致。

**Skills** 则是按需加载的扩展配置，与 AGENTS.md 的关键区别在于：
- AGENTS.md 是每次必传的上下文
- Skills 是当需要时才加载，不会膨胀上下文窗口
- Skills 可以使用斜杠命令调用，如 `/angular-best-practices`

这种分层策略解决了 AI 编程助手中的一个核心矛盾：提供足够的项目上下文 vs. 避免上下文窗口溢出。Skills 机制允许开发者为核心配置保留完整上下文，同时在需要时调用专门技能。

### 规约驱动开发：从需求到实现的结构化路径

**OpenSpec** 框架的采用是本文方法论的核心。规约驱动开发（Spec-Driven Development）解决了 AI 编程中的一个关键问题：AI 生成的代码看似合理但实际错误（幻觉）。

OpenSpec 为每个功能生成三个文档：
1. **proposal.md**：功能分析——做什么
2. **design.md**：技术设计——怎么做
3. **tasks.md**：实施计划——分几步做

这种三分法将模糊的需求转化为清晰的实施路径，使 AI 能够在明确的边界内工作。规约作为"唯一真相来源"，AI 生成代码成为衍生制品而非真相的起点。

从实践角度看，这种方法有显著优势：
- 功能交付速度提升（据外部案例研究可达 175% 提升）
- 变更失败率降低
- 新工程师入职周期缩短

### 团队结构变革：高频审查取代 Sprint 周期

作者提出了一个激进的团队结构变化建议：放弃传统 Sprint 周期，转向更频繁的审查和检查。

这一建议基于以下观察：
- AI 加快了实施速度，传统的 2 周 Sprint 可能导致过多并行工作
- 频繁检查可以尽早发现方向偏差
- 产品负责人需要更加严格地进行优先级排序

这种变革意味着团队需要建立新的节奏：更短的开发周期、更频繁的同步、更及时的反馈。虽然作者没有给出具体实施细节，但这一方向反映了 AI 时代软件开发流程的重塑趋势。

### 真实性评估

| 声明/事实 | 验证状态 | 说明 |
| :--- | :--- | :--- |
| Tim Deschryver 是本文作者 | 已验证 | timdeschryver.dev 是其个人博客，文章内容符合其技术背景 |
| 文章日期为 2026年5月7日 | 已验证 | 与发布日期一致 |
| ASP.NET API + Angular 前端架构 | 已验证 | 均为成熟技术，可在实际项目中使用 |
| 使用 Aspire 进行编排 | 已验证 | .NET Aspire 是微软官方的云原生编排工具 |
| 垂直切片架构 | 已验证 | 这是一种已知的软件架构模式 |
| Angular Signal API | 已验证 | Angular 16+ 的稳定功能 |
| Claude 和 Codex 表现相似 | 部分验证 | 不同测试中两者表现各有优劣，Claude 在设计任务上略强的说法与公开基准测试结果一致 |
| OpenSpec 框架 | 已验证 | 确实存在，有 55k Stars 的开源项目 |
| 规约驱动开发可提升效率 175% | 部分验证 | 外部案例研究（Fluendo）显示类似数据，但非受控实验 |

### 总结

本文是 Tim Deschryver 分享的 Agentic AI 实践经验，核心观点是"AI 应作为开发者的副将而非替代者"。通过采用规约驱动开发、分层配置管理（AGENTS.md + Skills）、以及现代化的 .NET 技术栈（Aspire + 垂直切片 + Minimal APIs + Angular Signals），作者构建了一套实用的 AI 辅助开发工作流。

文章的方法论具有较强实操性，特别适合以下场景：
- 已有 .NET + Angular 技术栈的团队
- 希望引入 AI 辅助但担心失控的团队
- 需要在 AI 速度和代码质量间取得平衡的项目

需要注意的是，本文代表作者个人经验，具体的工具选择和参数可能需要根据实际情况调整。

**关键要点：**

- **定位原则**：将 AI 定位为"副将"（domestique），开发者保持主导权和最终责任
- **技术选择**：.NET Aspire（编排）+ 垂直切片架构（代码组织）+ Angular Signals（状态管理）
- **配置分层**：AGENTS.md 提供必选上下文，Skills 提供按需扩展
- **规约驱动**：通过 OpenSpec 将需求结构化为 proposal → design → tasks 的流程，减少 AI 幻觉
- **渐进原则**：从简单开始，逐步增加复杂性，避免过度工程化
- **团队适应**：高频审查取代传统 Sprint，更及时的反馈循环

## 参考资料

- [Keep Agentic AI Simple: A Practical Workflow for Software Development](https://timdeschryver.dev/blog/keep-agentic-ai-simple-a-practical-workflow-for-software-development) — 原文出处
- [Fission-AI/OpenSpec - GitHub](https://github.com/Fission-AI/OpenSpec) — OpenSpec 规约驱动开发框架
- [Spec-Driven Development with AI: A Spec Kit + Claude Code Case Study](https://orangeloops.com/2026/05/spec-driven-development-with-ai-a-spec-kit-claude-code-case-study/) — SDD 实践案例
- [Beyond Vibe Coding: Scaling AI Software Architecture with Spec-Driven Development](https://fluendo.com/blog/beyond-vibe-coding-scaling-ai-software-architecture-with-spec-driven-development/) — SDD 效果数据来源
- [Claude Code 官方文档](https://code.claude.com/docs/en/memory) — AGENTS.md 配置说明
- [Microsoft .NET Aspire 文档](https://learn.microsoft.com/en-us/aspire/) — 云原生编排工具文档