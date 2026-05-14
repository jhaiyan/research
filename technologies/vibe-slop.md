# 深度研究报告：Vibe Slop

- 报告生成时间：2026-05-29 10:21
- 主题类型：概念、术语

## 概述

- 提出方：TechStartups（Daniel Levi）
- 提出时间：2025年9月19日
- 领域：软件工程、人工智能辅助编程

Vibe Slop（氛围式代码垃圾）是指在 AI 辅助编程（vibe coding）过程中，由于过度依赖 AI 生成代码而未严格执行代码质量、测试和架构规范，导致技术债务和混乱状态不断累积的现象。其核心特征包括：代码膨胀、逻辑错误、未经验证的依赖包、安全漏洞累积等。该概念由 Daniel Levi 于 2025 年 9 月正式提出，旨在警示业界 AI 加速编程带来的隐性成本和长期风险。Vibe Slop 与"vibe coding"（氛围式编程）密切相关——后者由 Andrej Karpathy 于 2025 年 2 月首次提出，描述使用自然语言提示词让 AI 生成代码、开发者不再逐行阅读代码的编程方式；前者则是后者失控后产生的混乱状态，是因果关系中的"果"。

## 提出背景/解决的核心问题

### 背景起源

2024 年至 2025 年间，AI 编程助手（如 Cursor、GitHub Copilot、Windsurf 等）迅速普及，开发者通过自然语言提示词即可快速生成代码。这种新兴开发模式被称为"vibe coding"（氛围式编程），由 Andrej Karpathy（OpenAI 联合创始人、前特斯拉 AI 负责人）于 2025 年 2 月首次在社交媒体推广，描述一种"完全沉浸于氛围、拥抱指数级增长、遗忘代码本身存在"的编程方式。

2025 年 3 月，Daniel Levi 在 TechStartups 发表《When Vibe Coding Goes Wrong》，首次系统记录 AI 编程助手的质量问题：代码变得臃肿、重复、混乱；用户陷入模糊修复循环；安全漏洞增加；学习能力退化；仅适合玩具项目而非生产系统。

然而，随着 AI 生成代码的规模迅速扩大，工程师们开始观察到一系列问题：

1. **代码质量问题**——AI 生成的代码虽然能运行，但缺乏架构设计，重复性强，难以维护
2. **安全漏洞增加**——AI 可在代码中引入 OWASP Top 10 类型的漏洞，且难以察觉
3. **技术债务累积**——快速生成的代码中充斥"临时修复"和 TODO 注释，生产环境变成维护噩梦
4. **依赖幻觉**——AI 可能"幻觉"出不存在的软件包名称，攻击者可注册这些假包注入恶意代码（slop squatting）

2025 年 9 月 19 日，Daniel Levi 在 TechStartups 发表《"Vibe Slopping"：TechStartups 为氛围式编程的混乱邪恶双胞胎赋予名称》，首次系统性地将这一现象命名为"vibe slopping"，用于描述 vibe coding 失控后产生的技术债务和代码质量崩塌状态。

### 解决的核心问题

Vibe Slop 概念的提出旨在解决以下问题：

1. **技术债务隐性累积问题**：AI 生成代码的速度远超人工审查能力，技术债务以指数级而非线性的速度累积（垃圾复合效应）
2. **安全漏洞透视问题**：AI 生成代码中存在大量幻觉依赖包（slop squatting），攻击者可利用这些假包名注入恶意代码
3. **质量与速度的平衡问题**：业界过度追求编程速度而忽视长期软件可靠性和工程纪律

## 发展历程

- **2025 年 2 月**：Andrej Karpathy 首次提出"Vibe Coding"概念，描述完全依赖 AI 生成代码的编程实践 [来源：Wikipedia](https://en.wikipedia.org/wiki/Vibe_coding)
- **2025 年 3 月**：Merriam-Webster 将"vibe coding"列为"slang & trending"（俚语与流行语）；Daniel Levi 在 TechStartups 发表《When Vibe Coding Goes Wrong》，首次系统记录 AI 编程助手质量问题 [来源：TechStartups](https://techstartups.com/2025/03/26/when-vibe-coding-goes-wrong/)
- **2025 年 9 月 19 日**：Daniel Levi 在 TechStartups 发表文章，首次提出"Vibe Slopping"概念，定义为 vibe coding 失控后产生的混乱状态 [来源：TechStartups](https://techstartups.com/2025/09/19/vibe-slopping-techstartups-coins-the-term-for-the-chaotic-evil-twin-of-vibe-coding/)
- **2025 年 10 月**：Gene Kim 和 Steve Yegge 出版《Vibe Coding》一书，Dario Amodei（Anthropic CEO）撰写序言，进一步系统化 vibe coding 方法论 [来源：Lobsters](https://lobste.rs/s/tuqscr)
- **2025 年 11 月**：Collins Dictionary 将"vibe coding"命名为年度词汇（Word of the Year 2025）[来源：Agent 4 报告]
- **2025 年 12 月**：CodeRabbit 分析发现 AI 协作代码的问题数量是纯人工代码的 1.7 倍 [来源：Agent 4 报告]
- **2026 年 3 月**：安全研究人员记录至少 35 个新 CVE 条目与 AI 生成代码直接相关；约 45% 的 AI 生成代码包含常见安全漏洞 [来源：Studio Global AI](https://www.studioglobal.ai/zh-cn/discover/answers/search-6a1076a4aebd9ec36509a9ba)
- **2026 年 5 月 22 日**：Mario Zechner 和 Armin Ronacher（OpenClaw 项目工程师）通过华尔街日报发出联合警告，称 AI 虽提升编码速度，却正批量输出低质量代码 [来源：DoNews](https://www.donews.com/news/detail/8/6568775.html)、[Toolhunt](https://toolhunt.io/the-ai-superstars-who-say-a-vibe-slop-crisis-is-coming/)
- **2026 年 5 月 24 日**：American Bazaar Online 分析 vibe slop 对 OpenAI 和 Anthropic 等公司 IPO 的潜在影响 [来源：American Bazaar Online](https://americanbazaaronline.com/2026/05/24/how-vibe-slop-and-fragile-economics-could-impact-mega-ipo-for-openai-and-anthropic-481441/)

## 适用场景

Vibe Slop 现象在以下场景中尤为突出：

1. **快速原型开发**：团队为追求速度而在无充分代码审查的情况下接受 AI 生成代码
2. **非专业开发者使用 AI 编程**：缺乏代码审查和安全验证能力，完全依赖 AI 编程助手构建系统
3. **技术债务累积已严重的遗留系统**：AI 被用于在混乱基础上继续构建，形成"债务复合"效应
4. **依赖 AI 生成代码进行关键系统开发**：安全敏感的金融、医疗、基础设施领域
5. **AI copilot 成为"事实上的 CTO"**：所有决策都依赖 AI 而非人工判断，TODO 直接进入生产环境

## 技术信息

### 核心概念定义

| 术语 | 定义 | 提出者 | 提出时间 |
| :--- | :--- | :--- | :--- |
| Vibe Coding | 使用自然语言提示词通过 AI 工具生成软件的开发风格，强调直觉和流程而非传统工程规范 | Andrej Karpathy | 2025年2月 |
| Vibe Slop/Slopping | Vibe coding 失控后的混乱状态——代码膨胀、未经重构、胶水代码修补、临时修复硬化为技术债务 | Daniel Levi / TechStartups | 2025年9月19日 |
| Slop Squatting | AI 幻觉出虚假软件包名称，攻击者注册这些包并注入恶意代码的安全攻击手法 | TestRigor | 2025年12月 |

### 关键技术特征

Vibe Slop 的典型技术特征包括：

- **代码膨胀**：未经重构的臃肿函数，AI 多次修改后累积而成，包含 100 行以上的辅助函数
- **错误假设**：AI 对业务逻辑的假设未被验证，沉默的逻辑错误被固化
- **硬编码值**：配置和常数硬编码，缺乏可维护性
- **依赖幻觉（Hallucinated Dependencies）**：AI 建议不存在的软件包，攻击者可注册同名恶意包
- **测试不完整**：单元测试覆盖率不足，AI 生成的测试仅表面通过
- **Happy-Path Software**：仅在理想条件下功能正常，在真实环境中易发生故障
- **技术债务复合**：AI 工具在已有问题代码上继续构建，形成指数级而非线性的债务增长

### 安全统计数据

| 数据 | 数值 | 来源 | 可信度 |
| :--- | :--- | :--- | :--- |
| AI 生成代码中含安全漏洞的比例 | 约45% | Studio Global AI（平台汇总） | 中等 |
| AI 辅助提交暴露凭证比例 | 3.2%（vs 纯手动提交1.5%） | Studio Global AI（平台汇总） | 中等 |
| 2026年3月直接由 AI 生成代码引起的 CVE 条目 | 至少35个 | Studio Global AI | 中等 |
| AI 协作代码问题数量 vs 纯人工代码 | 1.7 倍 | CodeRabbit（2025年12月） | 中等 |
| OpenClaw 暴露实例数 | 21,000+ | Studio Global AI | 中等 |
| OpenClaw 插件中含凭证处理漏洞的比例 | 7.1%（283/4000） | Studio Global AI | 中等 |
| CVE-2026-25253（CVSS 8.8）影响实例 | 42,000+ | Studio Global AI | 中等 |

### 典型案例

TestRigor 提供了一个典型案例：一个团队使用 AI 构建 Python API 端点（创建客户、验证邮箱、发送欢迎邮件、记录事件），AI 生成了控制器、验证函数、100 行邮件辅助函数、硬编码 SMTP 处理器、无法控制日志级别的日志记录、静默错误吞并和未知依赖包。几个月后调试发现多处问题，清理工作花了多个工程师至少两周时间。 [来源：TestRigor](https://www.testrigor.com/blog/what-is-vibe-slopping/)

## 方法论

### 预防 Vibe Slop 的最佳实践

1. **将 AI 输出视为草稿**：任何 AI 生成的代码都必须经过人工审查后才能进入代码库
2. **强制代码审查**：建立同行审查流程，确保至少一名工程师理解每段 AI 生成代码的逻辑
3. **标准化架构**：在使用 AI 编程助手之前，先确定技术栈和架构约束，避免代码碎片化
4. **验证所有依赖**：在使用 AI 建议的软件包之前，验证其真实存在、发布时间、漏洞情况和社区信任度
5. **自动化测试**：实施持续的自动化测试（单元测试、集成测试、静态分析）以捕捉 AI 生成代码中的问题
6. **保持人工监督**：AI 适用于草稿和原型开发，正式系统仍需人工审查、测试和安全评估
7. **主动追踪和清理**：通过重构配额和质量监控主动移除 slop
8. **建立维护文化**：在追求速度的同时重视代码可维护性，而非仅仅追求速度

### Vibe Slop 的警告信号

- 代码中大量 TODO 注释被带入生产环境
- AI 生成的代码"能运行"但无人完全理解其逻辑
- 特性在数小时内完成交付，但 bug 持续数月未修复
- AI 编程助手感觉像事实上的 CTO——所有决策都依赖 AI 而非人工判断
- 技术债务以 AI 输出速度倍增
- 修复一个 bug 会引入多个新 bug
- 代码库规模迅速膨胀但功能并未相应增加

### 专家建议

Mario Zechner（OpenClaw 工程师）和 Armin Ronacher 警告："AI 仅宜用于草稿与原型开发，正式系统仍须人工审查、测试与安全评估。" 忽视此边界将使修复成本远超初期开发节省。Simon Willison 指出"专业软件工程师使用 AI 强化和加速工作"与"非程序员使用 vibe coding 创建不理解其工作原理的系统"之间存在本质差异。

## 应用与发展趋势

### 当前应用现状

Vibe Slop 概念已在以下领域产生实际影响：

1. **安全研究领域**：安全研究人员开始系统性地研究 AI 生成代码的安全漏洞，OpenClaw 研究记录了大规模暴露实例和凭证处理漏洞
2. **IPO 影响分析**：American Bazaar Online 将 vibe slop 与 AI 公司（如 OpenAI 和 Anthropic）的 IPO 联系起来，分析指出"一旦这些公司上市，问题将不再是它们能生成什么，而是生成后什么真正有价值"
3. **行业分化**：专业软件工程师与非程序员之间的差距拉大，前者将 AI 视为增强工具，后者则可能陷入 vibe coding 的陷阱
4. **新兴职业角色**：出现"vibes cleanup specialist"（氛围清理专家）这一新兴角色，专门负责修复 AI 生成代码带来的问题

### 未来发展趋势

1. **治理需求增长**：行业将需要更强的代码治理、改进的审查实践和更有经验的人工监督
2. **安全标准提升**：随着 AI 生成代码引发的安全事件增多，企业将被迫建立更严格的 AI 代码审查流程
3. **价值与速度的博弈**：业界将面临"最大化快速输出"与"保持工艺性、可维护性和长期稳定性"之间的更深入博弈
4. **开发者技能转型**：从"编写代码"向"审查和引导 AI 生成代码"的能力转变
5. **AI 审查工具兴起**："AI 审查"作为新兴质量保障手段正在兴起

## 与同类方案的对比

### 概念定义对比

| 术语 | 提出者 | 提出时间 | 核心含义 |
| :--- | :--- | :--- | :--- |
| Vibe Coding | Andrej Karpathy | 2025年2月 | 完全依赖 AI 生成代码的编程实践，强调直觉和流程 |
| Vibe Slopping | Daniel Levi / TechStartups | 2025年9月19日 | vibe coding 失控后累积的技术债务和混乱 |
| LLM Slop | 社区通用术语 | 较早 | AI 生成的低质量内容（更广泛的内容领域） |
| Technical Debt | Ward Cunningham | 1992年 | 仓促开发导致的长期维护成本 |
| AI Slop | 社区通用术语 | 较早 | AI 生成的低质量内容（文本、图像、代码等） |

### Vibe Slop vs. 传统技术债务

| 对比维度 | 传统技术债务 | Vibe Slop |
| :--- | :--- | :--- |
| 产生来源 | 设计决策、业务压力、时间紧迫 | AI 加速生成 + 人工审查不足 |
| 增长速度 | 线性或多项式 | 指数级（因为 AI 在既有 slop 基础上继续构建） |
| 可见性 | 通常在重构或故障时显现 | 初期"看似正常"、规模化后才暴露 |
| 根因 | 有意识的权衡决策 | 无意识累积 + 幻觉依赖 |
| 防范难度 | 需要架构纪律 | 需要额外的 AI 使用治理 |

### Vibe Slop vs. 健康 AI 辅助开发

| 维度 | Vibe Slop（失控） | 健康 AI 辅助开发 |
| :--- | :--- | :--- |
| 代码审查 | 无或极简 | 强制人工审查 |
| 架构控制 | 无规划，被动救火 | 先设计架构，再使用 AI |
| 测试覆盖 | 不足或缺失 | 完整测试套件 |
| 依赖管理 | AI 幻觉包，未经核实 | 验证来源后再使用 |
| 技术债务 | 指数级累积 | 持续重构和控制 |
| 人员技能 | 依赖 AI 替代学习 | 工程师使用 AI 强化自身能力 |

## 常见问题（FAQ）

- **Q：Vibe Slop 和 Vibe Coding 有什么区别？**

  A：Vibe Coding（氛围式编程）是一种使用自然语言提示词让 AI 生成代码的编程方式，强调创造力和速度。Vibe Slop 则是 vibe coding 失控后产生的混乱状态——代码臃肿、充满技术债务和安全漏洞。Vibe Coding 是因，Vibe Slop 是果。

- **Q：Vibe Slop 和普通技术债务有什么区别？**

  A：普通技术债务通常是开发团队在时间压力下主动做出的权衡决定；而 Vibe Slop 是 AI 以极高速度生成代码、人类难以跟上审核节奏而被动累积的债务，且呈指数级复合增长（垃圾复合效应）。

- **Q：Vibe Slop 是否意味着不应该使用 AI 编程工具？**

  A：不。Vibe Slop 的本质是警示而非全盘否定。AI 辅助编程本身具有显著的生产力提升价值，但需要配合人工审查、测试和架构思考。关键在于将 AI 视为"工具"而非"替代者"，保持人在环（human-in-the-loop）监督。

- **Q：什么是 Slop Squatting？**

  A：Slop Squatting 是一种攻击手法，攻击者利用 AI 幻觉出不存在的包名，注册这些假包名并注入恶意载荷。当开发者信任 AI 生成的依赖包并直接安装时，就会中招。

- **Q：如何判断自己是否正在产生 Vibe Slop？**

  A：警示信号包括：代码中 TODO 数量持续增长但从未完成；没有人真正理解某些代码模块的工作原理；AI 生成的依赖包难以追溯来源；修复一个 bug 会引入多个新 bug；代码库规模迅速膨胀但功能并未相应增加。

- **Q：修复 Vibe Slop 的成本有多高？**

  A：一个团队曾花费两周修复不到一小时生成的代码。清理 AI 代码往往比手动编写更困难，因其倾向于冗长和不一致。

## 争议与质疑

1. **是否是新一轮道德恐慌**：部分技术人员认为"vibe slop"是又一轮对新技术的道德恐慌，如同历史上对汇编语言、"goto 语句"、面向对象编程的批评一样，最终会被证明是过度反应 [来源：Lobsters](https://lobste.rs/search?q=vibe+coding)

2. **定义边界模糊**：有观点认为"vibe slop"过于模糊，不同人对"vibe coding"的接受程度和定义存在差异，"vibe slop"、"vibe coding"、"LLM slop"等术语界限模糊

3. **问题根源的争论**：批评者指出 Vibe Slop 的根源不在于 AI 本身，而在于开发者的使用方式——规范使用 AI 辅助工具不会导致此问题

4. **与 IPO 关联的争议**：American Bazaar 将 vibe slop 与 OpenAI、Anthropic 的 IPO 前景关联被部分评论者认为逻辑跳跃，AI 生成代码的耐久性与公司估值之间的因果链尚未得到充分论证

5. **技能退化的担忧**：长期依赖 AI 编程可能导致开发者基础技能减弱，对代码的理解深度下降，在 AI 工具失效时难以独立解决问题

6. **AI 公司 IPO 影响**：公开市场已开始关注"能生成多少"与"生成内容能否规模化和持久"之间的平衡，American Bazaar 指出 AI 公司的长期价值将不再取决于"能生成多少"，而是"生成的内容在规模化后有多少能持续产生价值"

## 相关资料

- [TechStartups - "Vibe Slopping" coined term](https://techstartups.com/2025/09/19/vibe-slopping-techstartups-coins-the-term-for-the-chaotic-evil-twin-of-vibe-coding/) - Daniel Levi 于 2025 年 9 月 19 日首次提出"vibe slopping"概念
- [TechStartups - When Vibe Coding Goes Wrong](https://techstartups.com/2025/03/26/when-vibe-coding-goes-wrong/) - Daniel Levi 于 2025 年 3 月 26 日记录 vibe coding 的早期问题
- [TestRigor - What Is "Vibe Slopping"?](https://www.testrigor.com/blog/what-is-vibe-slopping/) - 详细分析 vibe slop 的定义、成因和预防策略，包含真实案例
- [Wikipedia - Vibe coding](https://en.wikipedia.org/wiki/Vibe_coding) - Vibe coding 维基百科条目，包含术语起源、历史和争议
- [Lobste.rs - vibe coding discussion](https://lobste.rs/search?q=vibe+coding) - 社区讨论，提炼了"vibe slop"的核心含义
- [Hacker News - vibe slop search](https://hn.algolia.com/?type=story&q=vibe%20slop) - HN 用户评论中提及"vibe coded slop"、"LLM slop"等表达
- [DoNews - 工程师警示AI编程致'vibe slop'风险加剧](https://www.donews.com/news/detail/8/6568775.html) - 中文媒体对 Mario Zechner 和 Armin Ronacher 警告的报道
- [Toolhunt - The AI Superstars Who Say a "Vibe Slop" Crisis is Coming](https://toolhunt.io/the-ai-superstars-who-say-a-vibe-slop-crisis-is-coming/) - 引用 Mario Zechner 和 Armin Ronacher 等工程师的观点
- [American Bazaar Online - Vibe Slop and IPO impact](https://americanbazaaronline.com/2026/05/24/how-vibe-slop-and-fragile-economics-could-impact-mega-ipo-for-openai-and-anthropic-481441/) - 分析 vibe slop 对 AI 公司 IPO 的影响
- [Studio Global AI - AI"氛围式编程"危机](https://www.studioglobal.ai/zh-cn/discover/answers/search-6a1076a4aebd9ec36509a9ba) - 分析 vibe coding 带来的安全和债务危机，包含安全研究数据
- [LinkedIn - Vibe Slop: Why AI Pioneers Are Warning](https://www.linkedin.com/pulse/vibe-slop-why-ai-pioneers-warning-your-favorite-coding-nantha-kumar-l-lcuxc) - AI 专家对 vibe slop 风险的警告