# AI 趋势与落地架构研究：从通用智能前沿到 Ontology 驱动的企业应用

> 整理日期：2026-11-09（Asia/Shanghai）。
> 研究对象：希望选择研究方向、产品方向与创业方向的软件开发从业者。
> 文档性质：对本轮讨论及其中已检索的一手资料进行综合整理；本次写入没有重新逐项实测产品。产品版本、可用性和功能属于检索时点快照。

## 1. 研究目标与主要判断

本研究最初从“当前热门模型、产品和技术”出发，随后将关注范围扩展到通用智能的关键能力，最终聚焦于一个更适合软件开发者长期投入的问题：**如何用可复用的架构与方法，把模型能力连接到业务知识、决策、执行和反馈。**

三个观察层次应当同时保留：

| 层次 | 核心问题 | 典型对象 | 对发展判断的作用 |
|---|---|---|---|
| 智能能力与增长机制 | AI 如何理解世界、学习新技能、创造知识、改进自身？ | 持续学习、世界模型、自博弈、自动化科研、递归自我改进 | 判断长期技术边界及其变化 |
| 应用与产品形态 | AI 能接手哪些工作，怎样交付结果？ | 个人助理、云端执行器、AI 工程师、行业工作流 | 观察用户需求、使用入口和商业交付 |
| 落地架构与方法论 | 怎样组织业务表示、数据、逻辑、动作、权限和反馈？ | Ontology、Context Graph、语义层、流程智能、持久执行 | 建立可复用的软件基础与行业能力 |

主要判断：

1. AI 的应用范围正在从内容生成和问答，扩展到持续执行任务与交付成果；实际可靠性取决于模型、运行系统、业务数据和验收机制的共同作用。
2. 通向更通用智能的关键研究包括持续学习、自主探索、世界模型、自动化科研与自我改进。目前已经出现局部成果，尚不能据此推导完整 AGI 或无限能力增长已经实现。
3. 对企业应用，模型需要接入明确的业务对象、指标口径、规则、动作和权限。**Ontology 是本轮讨论中最重要的架构锚点。**
4. 有长期价值的产品有机会积累客户关系、领域模型、业务集成、可信反馈与交付能力；仅依赖某一代模型短板的产品，需要持续检查竞争力。
5. “前沿”“热门”“适合创业”是不同维度。下文排序是综合判断，不是按流量、销量或融资规模统计的榜单。

## 2. 行业主线：开发者需要掌握的基础地图

### 2.1 值得跟踪的十条主线

| 方向 | 主要变化 | 开发者应掌握的内容 |
|---|---|---|
| Agent／智能体 | 模型通过观察、行动、反馈循环执行任务 | 工具、状态、终止条件、失败恢复、人工接管 |
| Agentic Coding | 开发辅助扩展到理解仓库、修改、测试和交付 | 需求、架构约束、测试、代码审查与发布 |
| Context Engineering | 系统管理做决策所需的信息环境 | 检索、记忆、资料时效、权限、上下文压缩 |
| Evals／评估 | 将输出质量与任务成功变为可测量对象 | 真实任务集、失败分类、回归检查、端到端验收 |
| 推理与推理时计算 | 通过搜索、反复求解和检查投入更多计算 | 质量、延迟、计算预算与验证强度的匹配 |
| 多模态与实时交互 | 语音、图像、视频和界面成为工作入口 | 输入理解、交互延迟、工具调用与交接 |
| 开放权重与推理优化 | 部署方式和模型规模更丰富 | 许可、硬件、量化、缓存、路由、单位成本 |
| 后训练与合成数据 | 用示例、反馈和验证器塑造能力 | SFT、RLVR、蒸馏、数据筛选与污染控制 |
| 世界模型与具身智能 | 预测环境变化并连接物理行动 | 仿真、规划、感知、动作与现实泛化 |
| AI for Science | 自动化部分假说、实验与验证过程 | 研究问题、实验有效性、可复现与专业评价 |

上下文工程的代表性方法见 [Anthropic 工程文章][context-engineering]。RAG 是上下文管理的组成部分；长上下文窗口提供容量，仍需判断信息的相关性、时效和访问范围。

### 2.2 模型与产品的观察样本

以下名称用于记录检索快照，不构成性能排名，也不代表完整市场覆盖。

| 模型系列 | 本轮检索涉及的代表版本 | 适合观察的维度 |
|---|---|---|
| OpenAI | GPT-6 Astra、GPT-6.1 Sol／Terra、GPT-6 Luna | 复杂工作、工具使用、不同能力档位的成本取舍 |
| Anthropic | Claude Opus／Sonnet／Haiku 5.5 | 编程、知识工作、任务规模与模型分工 |
| Google | Gemini 4 系列 | 多模态、智能体及工具生态 |
| DeepSeek | V4 系列 | 开放权重、长上下文及部署经济性 |
| Qwen | Qwen3.7 等系列 | 编码、工具调用与业务自动化 |

版本依据：[OpenAI 官方文档][openai-models]、[Anthropic 模型发布][anthropic-models]、[Gemini 官方页][gemini]、[DeepSeek V4 发布][deepseek-v4]、[Qwen3.7 发布][qwen37]。

开放权重、完整开源、可以本地部署、允许商业使用是不同属性，需要对具体版本分别查验。

选型应建立自己的真实任务集，测量任务成功率、人工修改时间、耗时与单次成功的总成本。排行榜只能作为补充。METR 的“任务时间跨度”使用人类专家完成任务所需的时间衡量难度，不能直接解释为 AI 可以稳定自主运行那么久。[METR 方法说明][metr]

## 3. 通向通用智能的 20 个前沿方向

本节按与通用性、持续学习、自主探索和智能增长机制的相关程度排列。基础思想的提出时间与当前研究前沿程度并不相同。

| 排名 | 方向 | 核心课题 | 代表工作 | 当前边界 |
|---:|---|---|---|---|
| 1 | 递归自我改进 RSI | AI 改进模型、算法及研究流程，提升下一轮改进能力 | [Sakana RSI Lab][sakana-rsi]、[Anthropic RSI 研究][anthropic-rsi] | 完整、自主、持续的递归提升尚未证实 |
| 2 | 自主 AI 研究员 | 自动提出假说、设计实验、执行与验证 | [Agentic Scientist][agentic-scientist] | 研究判断力、实验可靠性和开放选题仍有限 |
| 3 | 持续／终身学习 | 从部署后的经历中获得持久能力并保留旧能力 | [Nested Learning][nested-learning]、[Sleep Framework][sleep-framework] | 遗忘、错误积累和长期稳定性待解决 |
| 4 | 世界模型／JEPA | 学习状态变化与行动后果，支持预测和规划 | [V-JEPA 2][vjepa] | 局部有效，长期预测与陌生环境泛化仍困难 |
| 5 | 开放式学习与自博弈 | 自主生成挑战、课程和探索机会 | [Absolute Zero Reasoner][absolute-zero]、[Digital Red Queen][sakana-rsi] | 进步受环境、奖励和验证条件约束 |
| 6 | 测试时训练 TTT | 在求解当前问题时更新可学习状态或参数 | [TTT-Discover][ttt-discover]、[TTT-Consolidate][ttt-consolidate] | 对当前任务的适应未必形成可迁移的长期能力 |
| 7 | 元学习与学习型优化器 | 学习如何更有效地学习、更新模型 | [μLO][mulo] | 大规模模型和跨任务迁移仍是难点 |
| 8 | 潜空间推理与循环深度 | 在内部表示中迭代，为难题分配更多计算 | [Recurrent Depth][recurrent-depth] | 尚未证明普遍优于既有推理方式 |
| 9 | 神经动力学计算 | 利用内部时间演化的神经活动进行计算 | [Continuous Thought Machines][ctm] | 研究原型，尚未证明可替代前沿通用模型 |
| 10 | 可验证推理与定理证明 | 将推理结果交给形式系统检查 | [形式证明搜索][formal-search]、[Lean 形式化研究][formalization] | 仍需核对形式命题是否准确表达原问题 |
| 11 | 可扩展监督与自动化对齐 | 研究如何指导和评价能力超过监督者的系统 | [Automated Alignment Researchers][alignment-researchers] | 局部任务成果不等于解决通用对齐 |
| 12 | 机械可解释性 | 识别内部表示、计算电路及因果作用 | [Anthropic 可解释性研究][interpretability] | 距离完整理解大型模型仍远 |
| 13 | 生成式交互世界 | 生成可行动、可反馈的探索和训练环境 | [Genie 4][genie] | 长期一致性、物理可信度和复杂交互有限 |
| 14 | 通用具身智能／VLA | 将感知、语言、规划与物理动作结合 | [Gemini Robotics 2][robotics] | 数据、硬件与真实环境泛化限制明显 |
| 15 | 陌生环境中的高效适应 | 用少量探索发现规则并学会新技能 | [ARC-AGI-3][arc3] | 单一基准只能测量通用性的部分侧面 |
| 16 | 原生实时交互模型 | 连续接收多模态信息，同时思考与行动 | [Interaction Models][interaction-models] | 实时交互不自动意味着长期学习或自主性 |
| 17 | 长程自主智能体 | 长期保持目标、管理状态、恢复失败 | [长程 Agent 工程研究][anthropic-engineering] | 开放任务中的目标漂移和验收仍困难 |
| 18 | 多智能体／集体智能 | 通过分工、并行探索和审查提高系统能力 | [多智能体研究系统][multiagent-research] | 协调成本、相关错误和预算开销突出 |
| 19 | 扩散语言模型 | 探索逐 Token 自回归之外的文本生成路径 | [Mercury 3][mercury] | 速度优势需结合质量、硬件和具体任务比较 |
| 20 | 原生计算机操作智能体 | 从屏幕理解到操作软件，形成数字行动能力 | [Fara1.5][fara] | 长尾任务、异常恢复和复杂操作仍受限 |

### 3.1 判断“自我改进”时应区分的层次

| 层次 | 改变什么 | 可以支持的结论 |
|---|---|---|
| 当前任务反思 | 答案、计划或推理过程 | 一次求解中的纠错 |
| 运行系统优化 | 提示、工具、记忆策略、Agent 代码 | 执行系统可以通过反馈改善 |
| 模型优化 | 数据、权重、架构或学习算法 | 部分模型开发可以自动化 |
| 研究过程优化 | 选题、实验设计、评价和发现方法 | 开始触及递归改进的核心 |

[Darwin Gödel Machine][dgm] 展示了 Agent 修改自身代码并通过实验选择改进的路径。要证明更强的递归增长，还需观察改进是否跨任务迁移、多轮累积，以及是否提高后续研究效率。

[《Welcome to the Era of Experience》][era-experience] 提供了一个重要研究视角：智能系统可能越来越依靠与环境的长期交互获得能力。这是路线主张，不能视为已经验证的通用智能方案。Absolute Zero 的“零数据”也不代表基础模型从未使用人类数据，或环境和验证规则无需设计。

## 4. 应用层的 20 种解决方案

本节关注实际工作怎样被组织与交付。工作流是可设计的落地示例，具体能力取决于产品、集成和配置；产品提供能力不代表默认可以全自动完成整条流程。

| 排名 | 应用方案 | 典型工作流与交付 | 代表产品／项目 | 可切入方向及主要门槛 |
|---:|---|---|---|---|
| 1 | 持续运行的个人助理 | 接入消息、文件和日历，定时或按指令执行，返回结果和待决事项 | [OpenClaw][openclaw] | 职业助理；长期记忆、主动触发、跨应用执行 |
| 2 | 自主实验与研发优化 | 给定代码、预算和指标，修改、实验、比较、保留改进 | [autoresearch][autoresearch]、[Agentic Scientist][agentic-scientist] | 算法与性能优化；可信实验和验收 |
| 3 | 人类与 AI 员工共同工作空间 | 为 Agent 配置职责，在群聊中分配任务、共享材料、追踪交付 | [GenTeam][genteam] | 行业 AI 岗位；交接、共享状态和知识积累 |
| 4 | 持久云电脑任务执行器 | 描述目标，使用云端环境执行，交付文件、应用或持续服务 | [Manus Cloud Computer][manus-cloud] | 数据采集、监测、报表；恢复和运行成本 |
| 5 | 可委派的 AI 软件工程师 | 接收需求，理解仓库、修改、检查并提交可审查变更 | [Devin][devin] | 特定技术栈迁移、修复和测试维护 |
| 6 | 机器人任务执行系统 | 接收自然语言任务，感知现场、规划并操作 | [Gemini Robotics 2][robotics] | 结构化场地单任务；需要硬件及现场资源 |
| 7 | AI 应用构建平台 | 从需求生成界面、数据、登录和业务逻辑并发布 | [Lovable][lovable] | 行业应用；补齐权限、迁移、维护与验收 |
| 8 | AI 值班与故障调查 | 关联监控、部署、代码和历史故障，提出带证据的根因假设 | [incident.io AI SRE][incident] | 特定基础设施排障；证据质量和系统覆盖 |
| 9 | 自主安全测试 | 在授权范围内探索、验证漏洞，交付复现证据 | [XBOW][xbow] | API 与业务逻辑测试；修复、复测闭环 |
| 10 | 网页业务机器人 | 查找、填写和跨页面操作，完成线上事务 | [Browser Use][browser-use] | 缺少 API 的后台；脚本与 Agent 配合 |
| 11 | 成品交付型办公助手 | 阅读材料、调用程序，输出文档、表格和报告 | [Claude Cowork][cowork] | 招投标、分析、交付；模板和专业检查 |
| 12 | 企业知识与行动入口 | 按权限检索企业资料并执行配置好的任务 | [Glean Agents][glean] | 岗位知识工作流；权限、时效和集成 |
| 13 | AI 数据分析师 | 查询、编写分析代码、绘图，交付可追溯分析应用 | [Hex][hex] | 行业指标、数据质量与可复现分析 |
| 14 | 实时语音事务 Agent | 理解语音，查询资料、调用接口，处理预约和查询 | [ElevenAgents][elevenagents] | 行业服务；延迟、业务接口和转人工 |
| 15 | 客户服务 Agent | 读取政策和订单，执行授权操作并记录处理结果 | [Sierra][sierra] | 复杂售后、退换和订阅服务；真实解决率 |
| 16 | 内容生产流水线 | 串联图像、视频、音频生成和处理，输出多版本素材 | [Runway Workflows][runway] | 品牌审核、版本管理、投放实验 |
| 17 | 法律专业工作流 | 分析材料、比较条款、检索并生成专业审阅成果 | [Harvey Agents][harvey] | 单一法律流程；依据、模板和审阅 |
| 18 | 临床对话到文书 | 提取诊疗信息，生成结构化草稿并进入医护审核 | [Abridge][abridge] | 术语、系统集成、评估与行业合作 |
| 19 | 销售研究与客户数据运营 | 补全、研究、筛选客户数据并生成沟通草稿 | [Clay][clay] | 垂直行业客户识别；CRM 和反馈数据 |
| 20 | Agent 与固定流程结合的自动化 | 事件触发，明确步骤按流程执行，判断和例外交给 Agent | [n8n Agents][n8n] | 跨系统订单、采购和材料流程；异常处理 |

这些产品可以用来研究工作如何被重新组织。机会判断需要进一步核实真实使用、重复需求、交付成本和付费意愿。

## 5. Ontology：企业 AI 落地的架构锚点

### 5.1 通用本体与 Palantir 实现

广义的本体用于明确一个领域的概念、关系和约束。Palantir 将这一思想扩展为运营层，连接业务对象、状态、逻辑、动作与权限。**通用本体概念和 Palantir 的具体产品实现需要分别理解。**

Palantir 的架构明确整合 Data、Logic、Action、Security；逻辑可以来自规则、优化算法、传统模型或 LLM。[Ontology 架构][palantir-ontology]、[AIP 架构][aip-architecture]

| 组成 | 制造企业示例 | 系统意义 |
|---|---|---|
| 对象与状态 | 订单、工厂、设备、库存及当前状态 | 围绕真实业务实体工作 |
| 关系 | 订单依赖物料，由指定产线生产 | 跨系统追踪依赖和影响 |
| 逻辑与约束 | 产能、交期预测、库存规则 | 为方案比较提供业务依据 |
| 动作 | 调拨库存、调整计划、创建采购申请 | 将判断连接到实际操作 |
| 权限与记录 | 执行身份、条件、审批与操作结果 | 支持受控执行和追踪 |

以供应商延迟交货为例，可设计的完整流程是：

1. 识别受影响订单、物料与产线。
2. 查询替代库存、产能和供应来源。
3. 按交期、成本、合同与生产约束比较方案。
4. 由有权限的人或 Agent 执行动作。
5. 写回业务系统，跟踪结果并保留决策证据。

预测、优化、权限与外部连接都需要具体实现；本体定义本身不会自动产生这些能力。

### 5.2 与相邻架构的关系

以下是常见职责侧重点，各类方案可以组合，实际产品可能跨越多个范围。

| 架构 | 主要回答的问题 |
|---|---|
| Ontology | 有哪些业务对象、状态、关系和可执行动作？ |
| Context Graph | 在什么证据、政策、例外和审批下做出了什么决定？ |
| 语义层 | 字段、指标和关联具体代表什么，应怎样计算？ |
| 知识图谱／GraphRAG | 哪些实体和资料存在关联，如何据此查找与综合证据？ |
| 流程智能 | 工作实际上经过哪些步骤，在哪里出现异常？ |
| 记忆系统 | 哪些事实和经历应保留，在什么时间有效？ |
| 持久执行 | 任务如何在故障、等待和重试中继续推进？ |
| RAG | 如何检索与当前任务相关的外部资料，供模型使用？ |

Ontology 特别适用于多系统、多对象、规则复杂、需要改变业务状态的场景。简单生成或单一任务不一定需要承担完整建模成本。

### 5.3 对产品与创业的意义

值得验证的产品假设是：**把行业知识沉淀为可复用对象、规则和动作，让多个 AI 应用共享同一套业务基础。**

例如风险预警、采购建议、排产和订单跟踪，可以复用订单、库存、供应商及操作定义。创业时可以从一个足够小的业务本体和一条决策执行流程入手，随后根据真实复用需求扩展。

主要门槛：业务口径统一、实体标识、数据时效、写回一致性、权限和版本演进，以及客户实施成本。商业价值需要由具体流程的改善证明。

## 6. 20 个具有架构与方法论价值的 AI 落地方案

本节是研究重心。选择标准是能否提供可复用设计，组织业务知识、数据、决策、执行与反馈。各项覆盖不同层次，可以互相组合；排名不代表功能优劣或发明时间。

| 排名 | 方案／架构范式 | 核心思想 | 解决的问题 | 代表产品／项目及阶段 | 创业机会与关键门槛 |
|---:|---|---|---|---|---|
| 1 | 运营本体 Operational Ontology | 共享业务对象、关系、状态、逻辑、动作和权限 | 跨系统数据缺少统一业务含义和操作接口 | [Palantir Ontology＋AIP][palantir-ontology]；商业平台 | 行业本体与操作组件；领域建模、同步与实施成本 |
| 2 | 决策上下文图 Context Graphs | 连接决策的证据、政策版本、例外、审批和结果，形成组织先例 | 结果可查，决策依据却散落在沟通和经验中 | [原始主张][context-graphs]、[Tacnode 工程讨论][tacnode]；早期方向，定义尚未统一 | 退款、报价审批等例外密集流程；需在决策发生时捕获可信状态与依据 |
| 3 | 反馈驱动的 AI 程序优化 | 用评价、轨迹和文字反馈搜索提示与模块配置 | 人工调提示难积累，模型变化后难系统优化 | [DSPy／GEPA][gepa]；开源方法和工具 | 行业任务持续优化；可信评价、独立测试与防过拟合 |
| 4 | 流程智能／对象中心流程挖掘 | 从业务事件重建对象间的实际流转过程 | SOP 与实际行为不一致，跨系统瓶颈难定位 | [Celonis PI Graph][celonis]；商业平台 | 采购、应收、理赔诊断与干预；事件关联和效果归因 |
| 5 | 仿真驱动决策／数字孪生 | 用现场状态和仿真，在执行前测试方案后果 | 现实试错昂贵，物理后果难凭文字预测 | [NVIDIA Omniverse][omniverse]；工业开发平台 | 仓储、设备和机器人仿真；校准、现场数据与现实偏差 |
| 6 | 时序知识与有状态记忆 | 保存事实、关系、有效时间和来源，处理更新并按任务取回 | 失忆、过时事实、历史与当前状态混淆 | [Zep／Graphiti][graphiti]、[Letta][letta]；服务与开放工具 | 客户、项目、设备长期记忆；消歧、冲突、删除和权限 |
| 7 | AI 语义层／Semantic Views | 明确定义实体、指标、关系、同义词和计算口径 | SQL 正确但业务含义错误，指标口径不一致 | [Snowflake Semantic Views][semantic-views]、[Genie Ontology][genie-ontology]；平台能力，范围各异 | 行业指标模型和验证；业务专家参与及口径维护 |
| 8 | LLM＋约束求解器的决策智能 | 模型辅助理解和建模，优化器计算可行方案 | 排产、配送等存在硬约束，建议可能不可执行 | [OptiGuide／OptiMind][optiguide]；研究与工具 | 排班、配载、采购优化；正确约束、数据和求解规模 |
| 9 | 持久执行／Agentic Workflows | 保存状态，支持恢复、重试和等待；对外部动作设计幂等和补偿 | 中断丢进度，重试重复操作，审批等待难管理 | [Temporal][temporal]、[LangGraph Persistence][langgraph-persistence]；生产基础设施与框架 | 跨天跨系统业务任务；副作用、一致性和版本升级 |
| 10 | 复合 AI 系统 Compound AI Systems | 组合模型、检索器、代码、工具和验证器，分别优化组件 | 单模型难兼顾质量、实时性、成本和控制 | [Berkeley 方法论][compound-ai]、[LangChain／LangGraph][langchain-patterns]；方法与工具生态 | 专用求解流水线；错误传播、预算分配和端到端评价 |
| 11 | Agent Harness／可执行工作环境 | 统一规划、文件、上下文、代码执行、子任务和检查机制 | 简单工具循环难处理长任务和大量材料 | [Deep Agents][deep-agents]；开源框架 | 研发、审计、设计工作环境；隔离、上下文与验收 |
| 12 | 事件驱动的主动 Agent | 通过实时事件触发判断与行动，结合状态和流处理 | 依赖人发现问题，批处理错过干预时机 | [Confluent Streaming Agents][streaming-agents]；平台实现 | 库存、订单、设备异常；重复事件、误触发与动作冲突 |
| 13 | 图增强检索 GraphRAG | 用实体关系、遍历和社区摘要组织证据 | 相似片段检索易漏掉多跳关系与整体模式 | [GraphRAG／LazyGraphRAG][graphrag]；研究路线，原仓库主要维护 | 调查、技术情报和工程文档；抽取质量、更新成本与基线比较 |
| 14 | 规划式检索 Agentic Retrieval | 规划子查询，选择来源，并行检索、重排和合并 | 单次搜索难覆盖多条件、多来源问题 | [Azure AI Search][agentic-retrieval]；服务含预览能力 | 尽调、售前和行业研究；覆盖率、引用与延迟 |
| 15 | 带证据定位的文档到对象流水线 | 理解版面，再按业务 Schema 提取，保留原文位置并校验 | OCR 结果难入业务系统，错误字段难追溯 | [LandingAI ADE Gen2][ade]；商业产品；模式名为本研究归纳 | 合同、报关、理赔材料；跨页关联、复杂文档和复核成本 |
| 16 | 工具与 Agent 互操作架构 | 统一暴露能力、交换任务状态和交付物；MCP 与 A2A 覆盖不同交互 | 接入重复开发，跨厂商系统难协作 | [MCP][mcp]、[A2A][a2a]；开放协议 | 行业连接器、目录、网关和测试；鉴权、语义与版本兼容 |
| 17 | 专业能力包／可执行 SOP | 将说明、脚本、模板和检查步骤版本化、按需加载 | 专业流程散落，难复用与维护 | [Agent Skills][skills]；开放格式和生态 | 带工具与验证流程的行业能力包；任务成功率、维护和渠道 |
| 18 | 策略即代码／执行时授权 | 将访问、操作和审批规则独立成可测试策略，在执行边界检查 | 提示中的限制难强制执行，权限随状态变化 | [OPA＋Formal][opa-formal]；引擎与治理实现 | 跨系统授权审计；身份映射、策略冲突和执行覆盖 |
| 19 | 评价驱动交付／生产反馈闭环 | 将真实轨迹与失败变成回归用例，连接人工评价、验证和发布 | 演示不代表可靠，变更后业务退化难发现 | [Braintrust][braintrust]；商业平台 | 行业验收集、评分器和交付标准；与真实价值保持一致 |
| 20 | 规范驱动开发 Spec-Driven Development | 保存可审查的需求、约束、设计、任务与验收，再驱动实现 | 对话需求漂移，实现难核对原始意图 | [Kiro Specs][kiro]；商业工具与方法 | 行业软件交付流程；规范代码同步和可测试验收 |

### 6.1 组合示例：供应链异常处理

1. **Ontology**：统一订单、库存、供应商、产线与调拨动作。
2. **事件驱动**：发现延迟、缺货或设备状态变化。
3. **Context Graph**：查询历史例外、审批和采用过的依据。
4. **决策智能**：用优化求解器比较调度方案。
5. **持久工作流**：完成审批、执行、写回和失败恢复。
6. **评价闭环**：跟踪交期、成本、人工介入和实际结果。

这是一种可设计的组合示例，不表示必须同时采购上述产品，也不表示所有场景都需要完整组合。

## 7. 研究、创业与职业发展的行动框架

### 7.1 根据背景选择切入口

| 背景 | 优先研究 | 可以验证的具体问题 |
|---|---|---|
| 后端／分布式系统 | 持久执行、事件驱动、业务动作 | 重试和恢复后，是否重复操作或产生状态不一致？ |
| 数据工程 | 本体、语义层、时序知识、检索 | 数据含义、时效和权限明确后，任务成功率提升多少？ |
| 算法／机器学习 | 后训练、程序优化、验证器 | 同等预算下，反馈优化是否在独立任务上有效？ |
| 基础设施 | Harness、运行隔离、推理路由 | 在满足质量要求时，能否降低单次成功的总成本？ |
| 行业软件 | 流程智能、决策智能、专业能力包 | 哪段工作最昂贵，能否形成可复用行业组件？ |

默认情况下，适合个人或小团队的起点是：**熟悉行业中的高频流程，加上可获得的输入、可检查的结果和明确付费方。**

优先考察是否有人负责并拥有预算、数据能否获取、用户是否反复使用、结果能否验收、实施是否可重复，以及错误和例外能否被控制。

### 7.2 值得优先验证的五组方向

| 方向 | 产品起点 | 有机会形成的积累 | 主要风险 |
|---|---|---|---|
| 行业 Ontology＋工作流 | 一个订单、采购或售后流程 | 领域对象、动作、连接器与客户流程 | 定制实施过重，模型难复用 |
| Context Graph＋例外决策 | 报价、退款、升级处理 | 带依据的决策先例 | 捕获不完整、证据不可信、权限复杂 |
| 语义层＋行业分析 | 固定业务指标与分析任务 | 口径、数据映射和评价集 | 业务专家依赖及平台竞争 |
| 决策智能＋执行 | 排班、配载、调度 | 约束模型、优化经验与系统接入 | 数据不足、约束难表达、现场执行偏差 |
| 持久 Agent＋专业环境 | 能跨天完成的一类任务 | 工具、恢复策略、验收和反馈 | 总成本高，人工接管频繁 |

### 7.3 90 天验证计划

**第 1—30 天：建立能力与失败基线。** 使用两种编程 Agent 完成一个需要测试、部署和维护的项目。选择一个真实业务流程，记录输入、状态、人工步骤、失败类型和成本。掌握工具调用、结构化输出、检索与基本评价。

**第 31—60 天：完成一条可验收流程。** 与真实用户收集历史任务，定义成功标准，建立最小业务对象模型及必要动作。实现端到端原型，允许人工介入，并记录介入比例。只有真实失败暴露需求时再增加记忆、图或多 Agent 等组件。

**第 61—90 天：验证重复使用和付费。** 将原型用于日常工作，测量任务成功率、人工修改时间、完成耗时、异常恢复、单次成功总成本和持续使用情况。检验客户是否愿意为结果付费，是否能向第二个客户复用。

### 7.4 持续判断趋势的方法

- 每周阅读少量官方发布与原始研究，区分发布愿景、实验结果和生产能力。
- 每月用固定真实任务集复测重要模型与系统变更。
- 每季度重审方向：下一代模型更强、更便宜后，产品价值是否提高？
- 对自我学习系统检查改进是否持久、可迁移、跨多轮累积；对企业系统检查数据与动作是否真实闭环。
- 使用业务结果衡量收益，包含工具、基础设施、失败重试和人工成本。

未来一到三年的判断中，对业务集成、可靠交付、领域知识和评价能力重要性上升的信心较高；对部分软件转向承担具体任务的信心中等；对完全通用、长期无需监督的 Agent 很快普及的信心较低。这些判断应随证据更新。

## 8. 证据边界与后续研究事项

1. 厂商文档可以证明架构、公开功能和产品定位，不能独立证明所有客户的效果或投资回报。
2. 本文没有对各产品进行统一任务、统一预算和统一人工投入的比较测试。
3. Context Graph 的定义尚未统一。本文主要采用“跨实体和时间连接决策证据、例外、审批与结果”的含义；它不是模型私有思维链。Graphiti 所用的时序上下文图含义与此有交集，但不能直接视为同一完整方案。
4. 模型、记忆、工具和流程的改善需要分别测量。保存历史信息、修改提示、更新 Agent 代码与改进基础模型属于不同层次。
5. 本文的 20 项架构跨越业务表示、决策、执行和工程方法，范围大小不同。选型应围绕具体瓶颈组合，不需要全部采用。
6. 研究下一步应补充真实客户访谈、实施周期、许可与部署条件、实际费用、数据可得性和可复用性测试，再形成具体创业决策。

## 9. 一手资料索引

正文产品名和研究名可直接点击。下列链接为本轮讨论采用的公开资料，动态页面可能在后续更新。

| 主题 | 建议优先阅读的一手资料 |
|---|---|
| 企业业务表示 | [Palantir Ontology][palantir-ontology]、[AIP 架构][aip-architecture]、[Context Graphs][context-graphs]、[Tacnode 决策证据讨论][tacnode] |
| 数据与知识 | [Snowflake 语义视图][semantic-views]、[Genie Ontology][genie-ontology]、[Graphiti][graphiti]、[GraphRAG][graphrag] |
| 决策与流程 | [Celonis PI Graph][celonis]、[OptiGuide][optiguide]、[Omniverse][omniverse] |
| 执行与互操作 | [Temporal][temporal]、[Deep Agents][deep-agents]、[MCP][mcp]、[A2A][a2a]、[Agent Skills][skills] |
| 工程改进 | [Compound AI Systems][compound-ai]、[DSPy／GEPA][gepa]、[Braintrust][braintrust]、[Kiro Specs][kiro] |
| 智能增长 | [RSI Lab][sakana-rsi]、[Agentic Scientist][agentic-scientist]、[Nested Learning][nested-learning]、[Era of Experience][era-experience] |
| 产品形态 | [OpenClaw][openclaw]、[GenTeam][genteam]、[Manus 云电脑][manus-cloud]、[autoresearch][autoresearch] |

[openai-models]: https://developers.openai.com/api/docs/guides/latest-model
[anthropic-models]: https://www.anthropic.com/news/models
[gemini]: https://deepmind.google/models/gemini/
[deepseek-v4]: https://deepseek.com/en/news/v4-preview/
[qwen37]: https://qwen.ai/blog?id=qwen3.7
[context-engineering]: https://www.anthropic.com/research/effective-context-engineering-for-ai-agents
[metr]: https://evals.alignment.org/time-horizons/
[sakana-rsi]: https://sakana.ai/rsi-lab/
[anthropic-rsi]: https://www.anthropic.com/institute/recursive-self-improvement
[agentic-scientist]: https://pub.sakana.ai/agentic-scientist/
[nested-learning]: https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/
[sleep-framework]: https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/
[vjepa]: https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/
[absolute-zero]: https://arxiv.org/abs/2505.03335
[ttt-discover]: https://arxiv.org/abs/2601.16175
[ttt-consolidate]: https://arxiv.org/abs/2611.02104
[mulo]: https://proceedings.iclr.cc/paper_files/paper/2026/hash/66fdfe692a360dfbad1fba32f64694da-Abstract-Conference.html
[recurrent-depth]: https://proceedings.neurips.cc/paper_files/paper/2025/file/3b01972cf31e6fa0fe29e4b8b5c2a0a1-Paper-Conference.pdf
[ctm]: https://pub.sakana.ai/ctm/
[formal-search]: https://arxiv.org/abs/2605.22763
[formalization]: https://www.anthropic.com/research/formalizing-fermats-last-theorem
[alignment-researchers]: https://alignment.anthropic.com/2026/automated-alignment-researchers/
[interpretability]: https://www.anthropic.com/research/team/interpretability
[genie]: https://deepmind.google/models/genie/
[robotics]: https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/
[arc3]: https://arxiv.org/abs/2603.24621
[interaction-models]: https://thinkingmachines.ai/blog/interaction-models/
[anthropic-engineering]: https://www.anthropic.com/engineering
[multiagent-research]: https://www.anthropic.com/engineering/multi-agent-research-system
[mercury]: https://www.inceptionlabs.ai/blog/introducing-mercury-3
[fara]: https://www.microsoft.com/en-us/research/articles/fara1-5-computer-use-agent/
[dgm]: https://sakana.ai/dgm/
[era-experience]: https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf
[openclaw]: https://openclaw.ai/
[autoresearch]: https://github.com/karpathy/autoresearch
[genteam]: https://www.genspark.ai/helpcenter/genteam
[manus-cloud]: https://help.manus.im/en/articles/15392111-what-is-the-cloud-computer
[devin]: https://cognition.com/blog
[lovable]: https://lovable.dev/build/web-app-builder
[incident]: https://incident.io/solution/ai-sre
[xbow]: https://docs.xbow.com/console/get-started/introduction/
[browser-use]: https://browser-use.com/developers
[cowork]: https://claude.com/product/cowork
[glean]: https://docs.glean.com/agents/introduction
[hex]: https://hex.tech/capability/ai/
[elevenagents]: https://elevenlabs.io/docs/eleven-agents/overview
[sierra]: https://sierra.ai/
[runway]: https://docs.dev.runwayml.com/workflows/
[harvey]: https://www.harvey.ai/platform/agents
[abridge]: https://www.abridge.com/
[clay]: https://www.clay.com/faq
[n8n]: https://blog.n8n.io/introducing-n8n-agents/
[palantir-ontology]: https://www.palantir.com/docs/foundry/architecture-center/ontology-system
[aip-architecture]: https://www.palantir.com/docs/foundry/architecture-center/aip-architecture
[context-graphs]: https://foundationcapital.com/ideas/context-graphs-ais-trillion-dollar-opportunity
[tacnode]: https://www.tacnode.io/post/context-graph
[gepa]: https://dspy.ai/current/tutorials/gepa_ai_program/
[celonis]: https://www.celonis.com/news/press/celonis-pioneers-the-next-generation-of-process-intelligence-with-the-introduction-of-the-process-intelligence-graph
[omniverse]: https://www.nvidia.com/en-us/omniverse/
[graphiti]: https://www.getzep.com/platform/graphiti/
[letta]: https://docs.letta.com/v1-sdk/concepts/stateful-agents
[semantic-views]: https://docs.snowflake.com/en/user-guide/views-semantic/overview
[genie-ontology]: https://www.databricks.com/blog/how-genie-ontology-powers-product-development-databricks
[optiguide]: https://www.microsoft.com/en-us/research/project/optiguide-genai-for-supply-chain-optimization/tools/
[temporal]: https://temporal.io/solutions/ai
[langgraph-persistence]: https://docs.langchain.com/oss/python/langgraph/persistence
[compound-ai]: https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/
[langchain-patterns]: https://docs.langchain.com/oss/python/learn
[deep-agents]: https://docs.langchain.com/oss/javascript/deepagents/overview
[streaming-agents]: https://docs.confluent.io/cloud/current/ai/streaming-agents/overview.html
[graphrag]: https://www.microsoft.com/en-us/research/project/graphrag/
[agentic-retrieval]: https://learn.microsoft.com/en-us/azure/search/search-agentic-retrieval-concept
[ade]: https://landing.ai/blog/introducing-agentic-document-extraction-gen2
[mcp]: https://blog.modelcontextprotocol.io/posts/2026-07-28/
[a2a]: https://a2a-protocol.org/latest/topics/key-concepts/
[skills]: https://agentskills.io/home
[opa-formal]: https://www.openpolicyagent.org/ecosystem/entry/formal
[braintrust]: https://www.braintrust.dev/articles/llm-observability-guide
[kiro]: https://kiro.dev/docs/getting-started/first-project/
