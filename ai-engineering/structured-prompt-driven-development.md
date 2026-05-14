# SPDD（Structured-Prompt-Driven Development，结构化 Prompt 驱动开发）深度解读

> 原文：[Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/)<br>
> 作者：Wei Zhang（张伟，Thoughtworks 全球 IT 服务部 AI 辅助交付专家）、Jessie Jie Xia（夏洁，Thoughtworks 全球 CIO）<br>
> 编辑贡献：Martin Fowler<br>
> 发布日期：2026 年 4 月 28 日<br>
> 配套工具：[openspdd](https://github.com/gszhangwei/open-spdd) | 示例项目：[token-billing](https://github.com/gszhangwei/token-billing)

---

## 目录

1. [核心定义](#1-核心定义)
2. [REASONS Canvas：七部分结构化 Prompt 模板](#2-reasons-canvas七部分结构化-prompt-模板)
3. [SPDD 工作流：六步闭环](#3-spdd-工作流六步闭环)
4. [openspdd CLI：工具命令详解](#4-openspdd-cli工具命令详解)
5. [完整实战案例：Token 计费引擎增强](#5-完整实战案例token-计费引擎增强)
6. [三大核心技能](#6-三大核心技能)
7. [SPDD 与 SDD 的关系](#7-spdd-与-sddspec-driven-development-规范驱动开发的关系)
8. [适用场景评估](#8-适用场景评估)
9. [ROI 分析：收益与投入](#9-roi-分析收益与投入)
10. [Q&A 核心问答精粹](#10-qa-核心问答精粹)
11. [理论背景：从 SDD 探索到 SPDD 落地](#11-理论背景从-sdd-探索到-spdd-落地)
12. [CIO 休假实习：SPDD 的一手实践验证](#12-cio-休假实习spdd-的一手实践验证)
13. [Martin Fowler Fragments 关联讨论](#13-martin-fowler-fragments-关联讨论)
14. [关键概念速查表](#14-关键概念速查表)
15. [术语对照表](#15-术语对照表)

---

## 1. 核心定义

**SPDD（Structured-Prompt-Driven Development，结构化 Prompt 驱动开发）** 是一种将 **Prompt（提示词）视为一等交付物（first-class delivery artifact）** 的工程方法。Prompt 与代码一同进行版本控制、评审、复用和持续改进。

SPDD 解决的核心问题：AI 编码助手（如 Claude Code、Cursor、Copilot）极大提升了个人开发速度，但在团队层面制造了新的摩擦——模糊的需求被高速放大、代码评审难以应对 AI 生成量、"生成出来了"不代表"对齐了意图"。Thoughtworks 将此称为从 **"个人效率"到"组织能力"的鸿沟**。

SPDD 的两个核心组件：
- **REASONS Canvas**：七部分结构化 Prompt 模板，将意图锁定在代码生成之前
- **SPDD 工作流**：闭环迭代流程，核心规则是 **"当现实偏离时，先修复 Prompt，再更新代码"（When reality diverges, fix the prompt first — then update the code）**

SPDD 将代码评审的重心从"找 bug"转向 **"核验意图是否对齐"（check the intent）**。评审对象从散乱的聊天记录变为单一的 Canvas 工件。成功的模式积累为可复用的 Prompt 库，支撑 AIFSD（AI-First Software Delivery，AI 优先的软件交付）。

---

## 2. REASONS Canvas：七部分结构化 Prompt 模板

**REASONS** 是一个助记缩写，代表七个维度，分为三个层次：

### 抽象层（Abstract Layer）——意图与设计

| 维度 | 英文 | 含义 |
|------|------|------|
| **R** | Requirements（需求） | 正在解决的问题 + 完成定义（Definition of Done） |
| **E** | Entities（实体） | 领域实体及其关系 |
| **A** | Approach（方法） | 满足需求的策略 |
| **S** | Structure（结构） | 变更在系统中的位置：涉及哪些组件、哪些依赖 |

### 执行层（Specific Layer）——具体实施

| 维度 | 英文 | 含义 |
|------|------|------|
| **O** | Operations（操作） | **具体的、可测试的实现步骤**，将抽象策略分解为精确到方法签名、参数类型和执行步骤的指令 |

### 治理层（Common Standards）——跨领域标准

| 维度 | 英文 | 含义 |
|------|------|------|
| **N** | Norms（规范） | 跨领域的工程标准：命名约定、可观测性（observability）、防御性编码（defensive coding）等 |
| **S** | Safeguards（安全边界） | 不可协商的硬约束：不变量（invariants）、性能上限、安全规则等 |

### Canvas 的核心哲学：将不确定性左移（shift uncertainty to the left）

在代码生成之前锁定意图和边界。抽象层定义"做什么"和"为什么"，执行层定义"怎么做"，治理层定义"不能违反什么"。这使得：(1) LLM 在一个明确定义的边界内操作，大幅减少幻觉；(2) 评审者审查单一工件而非散乱的聊天记录；(3) 领域知识和设计判断在迭代中**复利积累（compound across iterations）** 而非在每次对话后丢失。

---

## 3. SPDD 工作流：六步闭环

### 核心原则：闭环同步（Closed-Loop Synchronization）

SPDD 的闭环在两个尺度上运作：

- **迭代内闭环**：逻辑修正（先更新 Prompt 再生成代码）和重构（先改代码再同步回 Prompt），确保双方不会悄悄偏离
- **跨迭代闭环**：积累的 Prompt 资产作为下一次增强的起点上下文

### 六步工作流

```
业务输入 → Step 1 创建需求 → Step 2 澄清分析 → Step 3 生成分析上下文
         → Step 4 生成结构化 Prompt → Step 5 生成代码 → Step 6 生成单元测试
         → 验证 → 发布
```

#### Step 1：创建初始需求（/spdd-story）
- 可选步骤，将大型需求分解为符合 INVEST 原则的用户故事
- 故事包含：背景、业务价值、范围（Scope In/Out）、验收标准（Acceptance Criteria，Given/When/Then 格式）
- 通常由 PO（Product Owner，产品负责人）或 BA（Business Analyst，业务分析师）与开发者结对完成

#### Step 2：澄清分析
开发者从三个维度审查故事：
1. **核心逻辑**：业务规则和路由策略
2. **范围边界**：明确不做什么
3. **完成定义**：具体的验证场景（正常/边界/错误）

#### Step 3：生成分析上下文（/spdd-analysis）
- 从需求中提取领域关键词，扫描相关代码
- 产出分析文档，覆盖：领域概念（已有 vs 新增）、关系、业务规则、策略方法（含设计决策和权衡）、风险（含边界情况和缺口）
- 开发者审查 AI 分析与自身理解的**对齐度**，关注：设计模式选择是否恰当、OOP 原则遵循、边界情况处理、技术风险

#### Step 4：生成结构化 Prompt（/spdd-reasons-canvas）
- 读取分析输出和代码库状态，产出完整的七维度设计规格
- Operations 部分**精确到方法签名、参数类型和执行步骤**
- 评审方式：检查 AI 如何将共享理解转化为 Canvas 结构——从策略到抽象到具体细节，这是**更深层次的意图对齐**
- 如需修改：使用对话式迭代而非手动编辑——指出差距，提供缺失意图，让 AI 仅更新受影响部分

#### Step 5：生成代码（/spdd-generate + /spdd-api-test）
- `/spdd-generate`：严格按 Operations/Norms/Safeguards 逐任务生成，"不即兴发挥，不超出规格定义的功能"
- 代码评审三优先：架构（是否遵循预期的分层架构？）→ 业务逻辑（Service 层是否匹配初始意图？）→ 范围（修改是否限定在定义边界内？）
- **关键原则**："不要担心犯错"——小的代码异味可以稍后处理，先验证核心功能
- `/spdd-api-test`：生成 cURL 测试脚本，覆盖正常/边界/错误场景，含结构化测试用例表（预期 vs 实际对比）
- **两种调整策略**：
  - **逻辑修正（行为变更）**：用 `/spdd-prompt-update` 先更新 Prompt，再 `/spdd-generate` 进行定向 diff（非全量重新生成）
  - **重构（清理代码，不变更行为）**：先改代码，再用 `/spdd-sync` 将代码变更写回 Prompt

#### Step 6：生成单元测试
- 使用模板驱动方式：将实现细节 + 标准化测试模板结合 → 去重和精炼 → 生成单元测试代码
- **API 测试在代码评审之前、单元测试在代码评审之后**——这是有意为之的逆 TDD（Test-Driven Development，测试驱动开发）顺序：
  - API 测试先验证"系统边界层面的 what"，在投入人工评审之前快速确认
  - 代码评审再关注"逻辑、架构、权衡和非功能关注点"
  - 单元测试最后作为回归安全网，在实现通过 API 验证和评审稳定之后

---

## 4. openspdd CLI：工具命令详解

开源工具地址：https://github.com/gszhangwei/open-spdd

| 命令 | 类型 | 用途 | 输入 → 输出 |
|------|------|------|------------|
| `/spdd-story` | 可选 | 将大需求分解为 INVEST 兼容的用户故事 | 增强想法 → 用户故事文件 |
| `/spdd-analysis` | 核心 | 提取领域关键词，扫描相关代码，产出策略分析 | 需求 + 代码库 → 分析文档 |
| `/spdd-reasons-canvas` | 核心 | 生成完整 REASONS Canvas 作为可执行蓝图 | 分析文档 + 代码库 → 结构化 Prompt |
| `/spdd-generate` | 核心 | 读取 Canvas 逐任务生成代码 | Canvas → 产品代码 |
| `/spdd-api-test` | 可选 | 生成基于 cURL 的 API 测试脚本 | Canvas → 测试脚本 |
| `/spdd-prompt-update` | 核心 | 需求变更时增量更新 Canvas | 变更说明 → 更新后的 Canvas |
| `/spdd-sync` | 核心 | 将代码侧变更同步回 Canvas（code → prompt） | 代码变更 → Canvas 同步 |

### 关键设计理念

每个命令内嵌了一个**思考策略（thinking strategy）**，将输出"拉向一致的形状"。这意味着：
- **从模板驱动到策略驱动**：即使没有模板，LLM 也能遵循策略
- **更高自动化**：步骤以命令而非手工方式调用
- **更稳定输出**：产物在多次运行间"远为一致"

SPDD 设计为**模型无关（model-agnostic）**——从 Claude 3.5 Sonnet 时代即已应用。对于分析和 Canvas 生成，"Claude（尤其是 Opus）往往领先"，其次是 GPT Codex 和 Gemini 3.x Pro。不推荐使用本地离线 LLM（能力不足）。一旦意图被锁定到结构化 Prompt 中，切换模型的风险可控。

---

## 5. 完整实战案例：Token 计费引擎增强

示例项目地址：https://github.com/gszhangwei/token-billing

### 背景

一个 LLM Token 用量计费引擎，需要从静态定价过渡到灵活的多计划、多模型定价架构。

### 增强需求

- **API 增强**：`POST /api/usage` 新增必填字段 `modelId`（如 "fast-model", "reasoning-model"）
- **模型感知定价**：基于所调用 AI 模型的动态成本
- **多计划计费**：
  - **Standard Plan（标准计划）**：基于配额（quota），含模型特定的超额费率（overage rate）
  - **Premium Plan（高级计划）**：无配额，分离计费——prompt token 和 completion token 不同费率
- **架构可扩展性**：使用 Strategy/Factory 设计模式，为未来定价提供扩展点

### 验收标准（示例）

1. 无效请求（缺少 `modelId`、负数 token）→ HTTP 400
2. Standard Plan：100K 月配额，已用 90K，调用 fast-model 30K token（$0.01/1K）→ 10K 配额内 + 20K 超额 = $0.20
3. Premium Plan：reasoning-model，prompt $0.03/1K + completion $0.06/1K，10K prompt + 20K completion → $0.30 + $1.20 = $1.50

### 执行过程要点

**Step 3 — 分析审查**：AI 生成的架构分析与作者的设计意图"基本一致；实际上在某些方面，AI 的考虑甚至比我们更全面"。分析文档无需修改即可接受。

**Step 4 — Canvas 审查**：审查者关注 AI 如何将共享理解从策略层面转化到具体抽象再到操作细节。由于基础上下文已经嵌入代码库和先前的 Prompt，AI "自然地考虑了架构指南和 OOP 原则"，几乎没有重大问题。

**Step 5 — 代码生成**：
- `/spdd-generate` 产出代码严格遵循三层架构（Controller → Service → Repository）
- 首次生成的 `modelId` 字段可为空（向后兼容），经业务确认后通过 `/spdd-prompt-update` 修改
- `/spdd-api-test` 生成包含结构化测试用例表的脚本——所有功能测试通过
- 重构阶段：将 `BillingServiceImpl` 中的魔数（magic numbers）提取为常量，`/spdd-sync` 自动将代码中的详细描述写回 Prompt

### 此案例交付成果

1. **极高的意图对齐度（~99%）**：业务逻辑实现与初始意图精确匹配
2. **完整的工程透明性**：实现路径、技术决策、权衡取舍全部可追溯
3. **同步的结构化 Prompt 资产**：与代码库保持同步，为后续迭代提供起点
4. **人机协作中的复利效应**：迭代中领域知识和设计判断持续积累

完整 diff：https://github.com/gszhangwei/token-billing/compare/before-enhancement...after-enhancement
额外练习：Enterprise Plan Volume-Based Tiered Billing（企业计划基于体量的分层计费）

---

## 6. 三大核心技能

SPDD 要求开发者掌握三项核心技能（原文链接为独立文章，截至本文撰写时尚未上线）：

### 6.1 Abstraction First（抽象优先）

> "设计先于生成"（design before generation）

在代码生成之前，必须建立清晰的对象、协作关系和边界。否则：
- AI 会"在实现细节上冲刺而结构崩坏"
- 导致职责不清、逻辑重复、接口不一致
- 需要昂贵的返工

**实践要求**：在让 AI 写任何代码之前，先明确领域模型、组件边界和协作契约。

### 6.2 Alignment（对齐）

> "在写代码之前锁定意图"（lock intent before writing code）

显式约定"我们将做什么 / 不做什么"，标准和硬约束提前确立。否则：
- 团队经历"快速输出和缓慢返工"（fast output and slow rework）
- 模糊的需求被 AI 放大为更大的误解

**实践要求**：通过 REASONS Canvas 将模糊的"需要什么"转化为结构化的"范围、方法、规范和边界"。

### 6.3 Iterative Review（迭代审查）

> "将输出转化为受控循环"（turn output into a controlled loop）

AI 辅助应表现为一个工程过程，而非一次性草稿。否则：
- 团队反复打补丁直到解决方案偏离正轨
- 或完全重启，失去对成本和时间控制

**实践要求**：代码审查重心从"找 bug"转向"核验意图对齐"；每次审查都是对 Prompt 资产的增量改进。

---

## 7. SPDD 与 SDD（Spec-Driven Development，规范驱动开发）的关系

### SDD 的三个层次（Birgitta Böckeler，2025 年 10 月）

Birgitta Böckeler（Thoughtworks 杰出工程师）在 martinfowler.com 的 "Exploring Gen AI" 系列中，将 SDD 工具按规范的持久化策略分为三个层次：

| 层次 | 英文 | 含义 | 代表工具 |
|------|------|------|----------|
| **规范优先** | Spec-first | 先写好规范用于当前 AI 编码任务，任务完成后规范不维护 | Kiro |
| **规范锚定** | Spec-anchored | 规范在任务完成后持续存在，作为该功能演进和维护的参考 | Tessl（探索中） |
| **规范即源码** | Spec-as-source | 规范成为主要产物，人类直接编辑规范，永不触碰生成代码 | Tessl（愿景） |

### SPDD 在 SDD 光谱中的定位

SPDD 被归类为 **规范锚定方法（spec-anchored approach）**，但与一般 SDD 工具有以下关键区别：

| 维度 | 一般 SDD 工具（如 spec-kit） | SPDD |
|------|---------------------------|------|
| **Prompt 的角色** | 一次性规范，用完即弃 | **持续维护的资产**（maintained artifact），版本控制、双向同步 |
| **规范结构** | 自由文本规则 + checklist | 固定的七维度 REASONS Canvas 结构 |
| **意图确认** | 一次性 | 分布式——分析、Canvas、生成每一步都是一个窄决策点 |
| **同步机制** | 单向传递（handoff） | **双向闭环**（two-way sync）：需求变更 → prompt-update → 代码；代码重构 → sync → prompt |
| **团队控制** | 个体效率工具 | 可重复的团队控制——成功模式积累为 Prompt 库 |

### Böckeler 对 SDD 工具的关键质疑（SPDD 需注意的风险）

1. **一种工作流适应所有规模？** spec-kit 对一个 3-5 点的 story 生成了太多 markdown 文件，"过程感觉不成比例"。小 bug 修复被 Kiro 扩展为 4 个 user story + 16 条验收标准
2. **审查 markdown 还是审查代码？** spec-kit 产出的 markdown 文件大量重复，总体冗长度使审查变得乏味。Böckeler 直言她"宁愿审查代码也不愿审查所有这些 markdown 文件"
3. **虚假的控制感？** 尽管有大量文件、模板、工作流和 checklist，她频繁观察到 Agent "最终并没有遵循所有指令"。大上下文窗口不保证 AI 正确拾取一切
4. **功能规范与技术规范如何有效分离？** SDD 的愿景是将功能规格与技术实现分离——理论上 AI 可以填充解决方案细节甚至切换技术栈。但实践中，Böckeler 发现很难区分何时停留在功能层面、何时添加技术细节
5. **规范锚定和规范即源码——从历史中学习？** Böckeler 将 spec-as-source 与 MDD（Model-Driven Development，模型驱动开发）做了重要类比。MDD 从未在商业应用中起飞——它处于尴尬的抽象层次，创造了太多开销和约束。LLM 消除了部分开销，但代价是非确定性。她警告 spec-as-source 可能"结合了最坏的两面：**不灵活性和非确定性**（Inflexibility and non-determinism）"

### Liu Shangqi（Thoughtworks 亚太技术总监）对 SDD 的补充定义

Liu Shangqi 在 2025 年的 Thoughtworks 博客中定义了 SDD 的两个竞争解释：

- **激进观点**：规范成为唯一真相来源——代码仅仅是中间副产品
- **保守观点（Liu 的立场）**：规范是驱动代码生成的元素（类比 TDD），但可执行代码仍然是真相来源

SDD 不是回到瀑布模型（Waterfall）：
- 瀑布的问题是**过长的反馈循环**
- Vibe Coding 的问题是**过快、自发和随意**
- SDD 引入比纯 Vibe Coding **更短且更有效的反馈循环**

---

## 8. 适用场景评估

### 五星推荐（SPDD 最适配）

| 评级 | 场景 | 说明 |
|:----:|------|------|
| ★★★★★ | 规模化、标准化交付 | 高重复性业务逻辑，需要长期可维护性 |
| ★★★★★ | 高合规/硬约束 | 受监管环境：金融核心系统、多渠道部署 |

### 四星推荐（SPDD 显著有帮助）

| 评级 | 场景 | 说明 |
|:----:|------|------|
| ★★★★☆ | 团队协作/可审计性 | 多人交付，需要端到端可追溯性 |
| ★★★★☆ | 跨领域一致性工作 | 跨微服务或跨语言的复杂重构 |

### 二星（SPDD 开销大于收益）

| 评级 | 场景 | 说明 |
|:----:|------|------|
| ★★☆☆☆ | 救火热修复（hotfix） | 生产修复中速度优先于架构纪律 |
| ★★☆☆☆ | 探索性 Spike | 快速想法验证，非生产级质量 |
| ★★☆☆☆ | 一次性脚本 | 用完即弃，SPDD 开销不合理 |

### 一星（SPDD 不适配）

| 评级 | 场景 | 说明 |
|:----:|------|------|
| ★☆☆☆☆ | 上下文黑洞 | 领域定义不清、业务规则模糊 |
| ★☆☆☆☆ | 纯创意/视觉工作 | 美学驱动的任务如 UI 视觉探索 |

### 关于热修复的补充说明

热修复的 1 星是指**事件期间的前置适配不合适**——"停下写 Canvas 是错误的决定"。但治理是延迟的，不是跳过的：
- 如果有上下文覆盖（先前已存在结构化 Prompt），使用压缩版 SPDD 循环
- 如果是遗留代码，直接修复后"将修复内容、故障模式和相关上下文合成为新文档资产"作为事后复盘

---

## 9. ROI 分析：收益与投入

### 收益

| 收益 | 程度 | 时间线 | 说明 |
|------|:----:|--------|------|
| **确定性（Determinism）** | 高 | 即时 | 精确规格减少幻觉 |
| **可追溯性（Traceability）** | 高 | 即时 | 变更可追溯至 Prompt 的具体段落 |
| **更快的评审（Faster Reviews）** | 高 | 短期 | 代码到达时更接近标准 |
| **可解释性（Explainability）** | 中高 | 渐进 | 意图在自然语言层面可见 |
| **更安全的演进（Safer Evolution）** | 高 | 长期 | 明确定义的边界使变更风险更低 |

### 前期投入

| 投入 | 程度 | 说明 |
|------|:----:|------|
| **思维转变** | 高（持续培训） | 从"代码优先"转向"设计优先" |
| **资深专业能力前置** | 中高（每功能） | 将业务规则翻译为清晰的抽象 |
| **自动化工具** | 中（基础设施搭建） | 没有 openspdd 等工具，吞吐量会达到上限，一致性也会受损 |

---

## 10. Q&A 核心问答精粹

> SPDD 文章发布后"产生了巨大的流量和大量问题"，Martin Fowler Fragments (2026-05-05) 记录了这一反响。作者随后追加了约 10 余个问答。以下为核心问题精粹。

### Q1：SPDD 超越现有治理规则的地方是什么？

三重填补：
1. **更细粒度的意图控制**：REASONS Canvas 将问题解决步骤显式化
2. **可复用的意图资产**：版本控制的 Prompt 随代码一起演进
3. **人类学习框架**：迫使开发者与工具一起推理，"领域知识和设计判断在迭代中复利积累，而非在每次聊天后丢失"

### Q2：与传统的渐进式披露指令集有何不同？

SPDD 的 Prompt 是一个**持续维护、版本控制的文件**（maintained, version-controlled file）：
- 固定的 Canvas 结构而非自由文本规则
- 分析命令先于代码（intent-before-code）
- Operations 级别的任务分解（方法级细节）
- **双向同步而非单向传递**：业务规则变更 → prompt-update 流向需求→Prompt→代码；代码重构 → sync 流向代码→Prompt

### Q3：决策背后的"为什么"是由 SPDD 闭环还是由人类承担？

SPDD 没有一个封闭的 AI 学习循环——它是**"半自动化、人类主导的"（semi-automated, human-led）**。但"为什么"被捕获为 Canvas 中的一等产物：
- R 和 A 部分记录理由和权衡
- 版本控制使其跨人员和跨时间持久
- 双向同步保持其时效性
- 每次迭代从积累的资产开始——评审者从找 bug 转向核验意图，因为**"意图现在在他们可以检查的地方"**

### Q4：两个开发者不会产出不同的 Canvas 吗？SPDD 只是把差异上移了一层吧？

作者承认这是"对今天状态的公平描述"。Canvas 相比自由形式的 Prompt **缩小了差异但未消除**。每个 openspdd 命令内嵌思考策略"将输出拉向一致的形状"，为经验不足的实践者提高了下限。但"在资产层的自动验证成熟之前，**人类判断仍然是负荷承载的（load-bearing）**"。

### Q5：SPDD 如何跨多项目、多领域扩展——瓶颈在 AI 能力还是问题界定？

"主要在问题侧，而非模型侧。"三个原因：
1. **分解是必需的**：大范围必须拆成小单元
2. **不清晰的边界封顶成功率**："更强大的 AI 不能修复这一点；它只是更自信地失败"
3. **决策资产随时间提供帮助**：在积累足够历史上下文之前，组合级工作不会自主交接

### Q6：SPDD 是模型无关的吗？模型变更会引入 Prompt 漂移吗？

SPDD 设计为模型无关，从 Claude 3.5 Sonnet 时代即已应用。一旦意图被锁定到结构化 Prompt 中，切换模型的风险可控。本地离线 LLM 不推荐（能力不足）。SPDD"不保证绝对确定性"，但将随机性保持在可控范围内。

### Q7：LLM 能力提升后 SPDD 有什么变化？

方法本身没有根本改变——"核心循环仍然一样"。改变的是多少手工努力可以移交给工具：
1. **从模板驱动到策略驱动**：命令内嵌思考策略，"即使没有模板 LLM 也能遵循策略"
2. **更高自动化**：步骤以命令调用而非手工操作
3. **更稳定输出**：产物"多次运行间远为一致"

### Q8：如何判断何时需要额外的 Prompt Engineering？

三个触发器：
1. **行为不匹配**：功能测试中输出偏离验收标准
2. **过于复杂的逻辑**：暗示 Approach 或 Operations 规格不足
3. **指令失败**：AI 违反 Norm 或 Safeguard——信号约束需要更突出

### Q9：为什么六步而不是更简单的"先计划再编码"？

**认知负荷（Cognitive Load）**："意图确认必须被分发，因为将其压缩到单一审查中会把太多东西堆在审查者面前。"每个检查点保持在足够小的规模以能真正参与其中。"重点不是为了步骤本身而增加步骤；而是每步更窄的决策"。

### Q10：为什么 API 测试在代码评审之前但单元测试在之后——TDD 的逆序？

故意的。
- API 测试在评审之前："在投入人工评审之前，快速验证系统边界层面的 'what'"
- 代码评审："关注逻辑、架构、权衡和非功能关注点"
- 单元测试最后：作为"回归安全网，在实现通过 API 验证和评审稳定之后"

### Q11：SPDD 的下一步是什么——如何降低对个人专业知识的依赖？

四个方向：
1. 更多工作流捕获为命令
2. **资产层自动验证**（分析、Canvas、Prompt 产物——而非代码）
3. 逐步提高 Harness 内的自动化比例
4. **"决策记忆"机制**（decision memory）：让历史决策作为持久上下文，"而非每次都重新发现"

### Q12：SPDD 当前是否将门槛设得太高（"专家专属"）？

作者承认 SPDD 目前在抽象和建模方面设置了高门槛，"似乎为资深架构师保留"。正在通过可复用的 SPDD 资产和更多机器可读的业务规则降低这一门槛，目标是"无论你是资深专家还是刚入门，都应该能够交付高质量、标准化的成果。"

---

## 11. 理论背景：从 SDD 探索到 SPDD 落地

### 时间线

| 时间 | 事件 | 作者/来源 |
|------|------|-----------|
| 2025 年 | Thoughtworks 刘尚奇发表博客，将 SDD 定义为"2025 年关键的 AI 辅助工程实践之一" | [Thoughtworks](https://www.thoughtworks.com/en-es/insights/blog/agile-engineering-practices/spec-driven-development-unpacking-2025-new-engineering-practices) |
| 2025 年 10 月 15 日 | Birgitta Böckeler 在 martinfowler.com 发表 "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl"，建立 SDD 三层模型 | [martinfowler.com](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) |
| 2025 年 11 月 | Thoughtworks Technology Radar Vol.33 收录 SDD，宣告 AI "从探索跨越到工程" | [Thoughtworks Radar](https://www.thoughtworks.com/radar) |
| 2026 年 4 月 28 日 | Wei Zhang & Jessie Jie Xia 发表 SPDD，Martin Fowler 编辑——SDD 的方法论落地 | [martinfowler.com](https://martinfowler.com/articles/structured-prompt-driven/) |
| 2026 年 5 月 5 日 | Martin Fowler Fragments 记录 SPDD 文章引发的巨大反响和 Q&A 追加 | [martinfowler.com](https://martinfowler.com/fragments/2026-05-05.html) |

### Böckeler 的 SDD 探索：核心发现

Birgitta Böckeler 测试了三个 SDD 工具（Kiro、spec-kit、Tessl），主要发现：

- **Kiro**（最轻量）：三步工作流（Requirements → Design → Tasks），主要停留在 spec-first 层次。还有 "steering" 概念（相当于 memory bank），默认文件为 product.md / structure.md / tech.md
- **spec-kit**（GitHub）：最可定制。工作流为 Constitution → [Specify → Plan → Tasks] 迭代。Constitution 是"不可变的"高层原则，贯穿所有变更。单个 spec 可生成 8 个文件（data-model, plan, tasks, spec, research, api, component）。但每个 spec 创建新分支，暗示规范仅在变更请求的生命周期内存在——仍是 spec-first
- **Tessl**（私有 Beta）：唯一明确追求 spec-anchored 甚至 spec-as-source。代码文件可标 `// GENERATED FROM SPEC - DO NOT EDIT`。目前 1:1 spec 到代码文件的映射。Böckeler 观察到同一 spec 多次生成代码时存在非确定性——增加 spec 具体性可提高重复性，这让她想起编写无歧义完整规范的挑战

### 重要的历史类比：MDD（Model-Driven Development，模型驱动开发）

Böckeler 提出了一个关键的批判性视角：**spec-as-source 的真正历史类比不是 TDD/BDD，而是 MDD**。

在 MDD 中：
- 模型本质上是规范，用定制 UML 或文本 DSL 表达
- 定制代码生成器将模型翻译成代码
- MDD 从未在商业应用中起飞——处于尴尬的抽象层次，创造了太多开销和约束

LLM 的差异：
- **优势**：不需要预定义的、可解析的规范语言或精心制作的代码生成器
- **代价**：LLM 的非确定性
- **失去的优势**：旧的可解析结构为编写有效、完整和一致的规范提供了工具支持

Böckeler 警告："规范锚定和规范即源码可能结合了最坏的两面：**不灵活性和非确定性**。"

---

## 12. CIO 休假实习：SPDD 的一手实践验证

Jessie Jie Xia（夏洁，Thoughtworks 全球 CIO）在 20 年领导力生涯后，选择成为 Thoughtworks 武汉 GITS Hub（全球 IT 服务交付中心）的"编程实习生"。她的经历为 SPDD 提供了一手验证。

### 三阶段学习路径

| 阶段 | 英文 | 含义 |
|------|------|------|
| 1 | **Sandbox（沙箱）** | 有护栏的 AI 安全探索——理解 AI 编码工具的基本行为 |
| 2 | **Copilot（副驾驶）** | AI 辅助下的独立编码——AI 生成代码，人类审查和调整 |
| 3 | **Pilot（驾驶）** | 整合 SPDD 方法论——用结构化 Prompt 系统性地驱动 AI 输出 |

### 关键数据点

- 约 **5 倍生产力提升**
- **超过 55% 的时间花在"磨刀"（分析与设计）阶段**——代码生成后几乎零返工
- SPDD 将代码从"一面无法翻越的墙"转变为可解决的逻辑谜题
- CI/CD 流水线（包括代码质量检查和安全扫描）在 SPDD 工作流中自动执行

### 意义

CIO 亲自验证了 SPDD 的两个核心主张：(1) 意图对齐的高确定性（分析阶段投入的时间在代码生成阶段回收）；(2) 方法可学习——即使对 20 年未曾亲手编码的人来说，SPDD 将 AI 辅助编程从"运气"变成了"可重复的工程过程"。

---

## 13. Martin Fowler Fragments 关联讨论

### 2026 年 5 月 5 日 Fragments

SPDD 之外的重要关联洞察：

**Jessica Kerr：双重反馈循环（Double Feedback Loops）**
- **开发循环**（build-and-check）：写 Prompt → 生成代码 → 验证
- **元层次循环**（meta-level loop）：当感到"挫败、乏味、烦躁"时，这可能是关于**过程本身是否在起作用的信号**——需要改变的不是正在构建的东西，而是**构建的方式**
- Fowler 将此连接到他称为"内部可重编程性（Internal Reprogrammability）"的概念——这种乐趣在 Smalltalk 和 Lisp 时代之后大部分丧失，但现正通过 Agent 重新发现

**Kent Beck："Genie in the Tar Pit"（焦油坑里的精灵）**
- 用 Fred Brooks 的经典隐喻警告：AI 编码 Agent "天然生活在糊泥巴的左侧和下方"——即使代码不能运行也声称成功
- "复杂性堆积在复杂性之上，直到精灵也无法假装取得进展"
- 衍生辩论：**内部代码质量在 Agentic 编程时代还重要吗？**
  - 观点 A：好的命名和结构帮助 AI 理解代码（"开发者体验和 Agent 体验的维恩图是一个圆"）
  - 观点 B：未来的 LLM 将能导航任何意大利面代码

**本地模型 vs 云端巨头**
- Willem van den Ende：开源本地模型已经"跨越了足够用于日常编码 Agent 工作的临界点"
- "**Harness（驾驭系统）的质量——编码 Agent 加上 Skills 和扩展——可能与模型本身一样重要**"
- Apple 战略（10% 收入用于 AI 基础设施 vs 50%+ 的竞争对手）——赌端侧 AI 将像 Apple II 对大型机一样胜出

---

## 14. 关键概念速查表

| 概念 | 定义 | 在 SPDD 中的角色 |
|------|------|-----------------|
| **Prompt as First-Class Artifact**（Prompt 作为一等产物） | Prompt 与代码一同版本控制、评审、复用和改进 | SPDD 的核心哲学——Prompt 不是一次性聊天记录 |
| **Intent Alignment**（意图对齐） | 确保 AI 理解并忠实执行设计意图 | 通过 Canvas 在生成代码前锁定意图 |
| **Closed-Loop Synchronization**（闭环同步） | Prompt 和代码双向同步，不悄悄偏离 | 逻辑修正改 Prompt → 代码，重构改代码 → Prompt |
| **Decision Assets**（决策资产） | 积累的历史上下文、架构选择、规范模式 | 每轮迭代的 Canvas 成为下一轮的起点 |
| **Spec-Anchored Development**（规范锚定开发） | 规范在任务完成后持续存在并维护 | SPDD 在 SDD 光谱中的位置 |
| **Uncertainty Shift-Left**（不确定性左移） | 在流程早期（代码生成前）解决歧义 | REASONS Canvas 的设计目标 |
| **Cognitive Load Distribution**（认知负荷分发） | 将意图确认分发到多个小检查点 | 六步工作流的理由 |
| **Harness Engineering**（驾驭工程） | 围绕 AI 模型构建约束和编排系统 | SPDD 是 Harness 在 Prompt 层面的体现 |
| **Vibe Coding**（随心编码） | 向 LLM 描述需求后以最少审查接受输出（Andrej Karpathy，2025 年 2 月） | SPDD 试图系统化取代的方法 |
| **Context Engineering**（上下文工程） | 设计动态系统以在正确时间以正确格式交付正确信息和工具（Phil Schmid，2025） | SPDD 的 REASONS Canvas 是上下文工程的一种结构化实现 |

---

## 15. 术语对照表

| 缩写/英文 | 全称 | 中文翻译 |
|-----------|------|----------|
| **SPDD** | Structured-Prompt-Driven Development | 结构化 Prompt 驱动开发 |
| **SDD** | Spec-Driven Development | 规范驱动开发 |
| **AIFSD** | AI-First Software Delivery | AI 优先的软件交付 |
| **REASONS** | Requirements, Entities, Approach, Structure, Operations, Norms, Safeguards | 七维度结构化 Prompt 模板 |
| **TDD** | Test-Driven Development | 测试驱动开发 |
| **BDD** | Behavior-Driven Development | 行为驱动开发 |
| **MDD** | Model-Driven Development | 模型驱动开发 |
| **DSL** | Domain-Specific Language | 领域特定语言 |
| **MCP** | Model Context Protocol | 模型上下文协议（Anthropic） |
| **A2A** | Agent-to-Agent | Agent 到 Agent 协议（Google） |
| **INVEST** | Independent, Negotiable, Valuable, Estimable, Small, Testable | 用户故事质量原则 |
| **OOP** | Object-Oriented Programming | 面向对象编程 |
| **SRP** | Single Responsibility Principle | 单一职责原则 |
| **ISP** | Interface Segregation Principle | 接口隔离原则 |
| **PO** | Product Owner | 产品负责人 |
| **BA** | Business Analyst | 业务分析师 |
| **CIO** | Chief Information Officer | 首席信息官 |
| **SME** | Subject Matter Expert | 领域专家 |
| **PR** | Pull Request | 拉取请求 |
| **ROI** | Return on Investment | 投资回报率 |
| **CICD** | Continuous Integration / Continuous Deployment | 持续集成/持续部署 |

---

## 主要参考来源

- [Structured-Prompt-Driven Development — Martin Fowler (Wei Zhang & Jessie Jie Xia, 2026-04-28)](https://martinfowler.com/articles/structured-prompt-driven/)
- [Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl — Martin Fowler (Birgitta Böckeler, 2025-10-15)](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)
- [Martin Fowler Fragments: May 5, 2026](https://martinfowler.com/fragments/2026-05-05.html)
- [How a sabbatical transformed a CIO into a coding intern — Thoughtworks (Jessie Jie Xia, 2026)](https://www.thoughtworks.com/insights/blog/careers-at-thoughtworks/Rethinking-leadership-cio-journey-as-a-coding-intern)
- [Spec-driven development: Unpacking one of 2025's key new AI-assisted engineering practices — Thoughtworks (Liu Shangqi, 2025)](https://www.thoughtworks.com/en-es/insights/blog/agile-engineering-practices/spec-driven-development-unpacking-2025-new-engineering-practices)
- [Promptware Engineering: Software Engineering for Prompt-Enabled Systems — ACM TOSEM 2026 (Chen et al.)](https://dl.acm.org/doi/abs/10.1145/3796535)
- [openspdd CLI — GitHub](https://github.com/gszhangwei/open-spdd)
- [Token Billing 示例项目 — GitHub](https://github.com/gszhangwei/token-billing)
