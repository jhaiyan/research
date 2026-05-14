# Enterprise 2.0 + 矩阵式组织 多租户 SaaS 系统设计

> 本文整合行业最佳实践（Workday / SAP SuccessFactors / Salesforce / Microsoft Entra / Atlassian Cloud / ServiceNow / Notion Enterprise / Slack Enterprise Grid / Google Workspace），并参考 Google Zanzibar、SCIM 2.0、ActivityStreams 2.0、Cedar、OPA（开放策略引擎）等开放标准。

---

## 术语与缩写速查

| 缩写 | 全称 | 中文说明 |
|------|------|---------|
| SaaS | Software as a Service | 软件即服务，通过网络交付的订阅制软件 |
| DDD | Domain-Driven Design | 领域驱动设计，以业务领域为核心拆分系统边界 |
| IAM | Identity and Access Management | 身份与访问管理，负责"我是谁"和"我能做什么" |
| RBAC | Role-Based Access Control | 基于角色的访问控制，用户→角色→权限的三层模型 |
| ABAC | Attribute-Based Access Control | 基于属性的访问控制，根据主体/资源/环境属性动态判定 |
| ReBAC | Relationship-Based Access Control | 基于关系的访问控制，权限来源于对象间的关系图 |
| SSO | Single Sign-On | 单点登录，一次认证即可访问所有授权系统 |
| SAML | Security Assertion Markup Language | 安全断言标记语言，企业 SSO 的 XML 标准协议（v2.0） |
| OIDC | OpenID Connect | 开放身份连接协议，基于 OAuth 2.0 的现代身份标准 |
| SCIM | System for Cross-domain Identity Management | 跨域身份管理系统，自动化用户/组的增删改同步标准（v2.0） |
| MFA | Multi-Factor Authentication | 多因素认证，登录需提供两种以上凭证 |
| TOTP | Time-based One-Time Password | 基于时间的一次性密码，如 Google Authenticator |
| WebAuthn | Web Authentication | 网页认证标准，使用生物识别/硬件密钥替代密码 |
| BYOK | Bring Your Own Key | 自带密钥，客户自管加密密钥，不依赖 SaaS 厂商 |
| KMS | Key Management Service | 密钥管理服务，统一管理加密密钥的生命周期 |
| CMK | Customer Managed Key | 客户管理密钥，BYOK 场景下由客户控制的主密钥 |
| HRIS | Human Resource Information System | 人力资源信息系统，如 Workday、BambooHR |
| HR | Human Resources | 人力资源 |
| IdP | Identity Provider | 身份提供商，负责颁发身份令牌，如 Okta、Azure AD |
| ACL | Access Control List | 访问控制列表，记录"谁对什么有什么权限"的清单 |
| UGC | User-Generated Content | 用户生成内容，Wiki、评论、标签等由用户创作的内容 |
| JWT | JSON Web Token | JSON 网络令牌，携带用户身份声明的无状态令牌 |
| DLP | Data Loss Prevention | 数据防泄漏，检测并阻止敏感数据外流 |
| CQRS | Command Query Responsibility Segregation | 命令查询职责分离，写操作与读操作走不同数据模型 |
| CTE | Common Table Expression | 公共表表达式，SQL 中用 WITH 子句定义的临时结果集 |
| DFS | Depth-First Search | 深度优先搜索，图遍历算法 |
| M&A | Mergers and Acquisitions | 并购 |
| RLS | Row Level Security | 行级安全，数据库层面按行过滤，防止跨租户数据泄漏 |
| OLTP | Online Transaction Processing | 在线事务处理，面向高并发读写的关系型数据库使用场景 |
| SOC 2 | Service Organization Control 2 | 服务组织控制 2 型，北美 SaaS 安全合规认证标准 |
| GDPR | General Data Protection Regulation | 通用数据保护条例，欧盟数据隐私法规 |
| HIPAA | Health Insurance Portability and Accountability Act | 美国健康数据隐私合规标准 |
| ISO 27001 | Information Security Management Standard | 信息安全管理国际标准 |
| LDAP | Lightweight Directory Access Protocol | 轻量级目录访问协议，企业目录服务标准（如 AD） |
| AD | Active Directory | 活动目录，微软的企业用户目录服务 |
| API | Application Programming Interface | 应用程序接口 |
| LLM | Large Language Model | 大语言模型，如 GPT-4、Claude |
| OU | Organizational Unit | 组织单元，组织结构中的节点 |
| OPA | Open Policy Agent | 开放策略引擎，通用 ABAC 策略评估框架 |
| AWS | Amazon Web Services | 亚马逊云服务 |
| GCP | Google Cloud Platform | 谷歌云平台 |

---

## 先把 Enterprise 2.0 说清楚

很多团队把 "Enterprise 2.0" 直接等同于"现代企业级 SaaS（软件即服务）"，这是误解。

**Enterprise 2.0** 由 Andrew McAfee 在 2006 年 *MIT Sloan Management Review* 提出，是把 Web 2.0 的社会化协作机制带进企业内部。McAfee 用 **SLATES** 概括其核心：

| 字母 | 含义 | 对系统设计的要求 |
|------|------|---------------|
| **S**earch（搜索） | 全员可搜索 | 跨域索引、权限感知搜索 |
| **L**inks（互链） | 内容互链 | 资源是图，引用是一等公民 |
| **A**uthoring（创作） | 人人可创作 | UGC（用户生成内容）、版本、协作编辑 |
| **T**ags（标签） | 自创分类（folksonomy 民间分类法） | Tag/Tagging 由用户产生，而非 IT 预定义 |
| **E**xtensions（扩展） | 推荐与扩展 | 个性化、推荐、Activity Stream（活动流） |
| **S**ignals（信号） | 订阅/推送 | Follow（关注）、Notification（通知）、Webhook |

后续社区扩展为 **FLATNESSES**（Free-form 自由形式 / Links 互链 / Authorship 创作 / Tagging 标签 / Network-oriented 网络导向 / Extensions 扩展 / Signals 信号 / Search 搜索 / Emergence 涌现 / Social 社交）。

**对系统设计的实际影响：**

1. **组织结构是涌现的（Emergent）**——不能只用自上而下的 HR 树来表达；Collaboration（协作）与 Social（社交）域必须与 HR 域并列，而不是附属模块。
2. **打破部门墙**——跨 Org（组织）、跨 Tenant（租户）的协作（Connect/Federation 联邦）是核心能力。
3. **Social Graph（社交图谱）是一等公民**——Follow / Mention / Endorsement 不是"社交插件"，而是企业知识流转的载体。
4. **Knowledge（知识）由用户生成**——Wiki、Tag、Activity 必须建模为领域实体。

**矩阵式组织（Matrix Organization）** 是组织建模层面的要求：一名员工同时向多人汇报、跨多个项目分配工时、有 solid line（实线，行政汇报）与 dotted line（虚线，业务/职能汇报）之分。这要求组织从**树（Tree）**升级为**图（Graph）**，并把 **Position（岗位）** 作为 User 与 Org 之间的中介节点。

---

## 一、核心设计原则

### 1.1 Tenant（租户）≠ Organization（组织）——最常见的根本性错误

```text
Tenant       = Identity（身份）/ Billing（计费）/ Data Isolation（数据隔离）边界
Organization = HR（人力资源）/ Reporting（汇报）/ Cost Center（成本中心）边界
```

为什么不能混：

- 一个集团（Tenant）下有多个法人实体（Legal Entity）；
- 一个用户可以同属多个 Org（矩阵组织特性）；
- 外包/合作伙伴不属于任何正式 Org，但要进 Tenant；
- M&A（并购）期间组织临时合并；
- Slack Enterprise Grid / Microsoft 365 Tenant 都把这两层显式分开。

### 1.2 三层身份：User / Position / Assignment

```text
User（用户）      —— 平台身份（账号，跨租户唯一）
Position（岗位）  —— 岗位定义（隶属 Org，与人无关，可空缺）
Assignment（分配）—— 用户在某个时间段对某岗位的占用（含 allocation 时间投入比例）
```

这是 SAP/Workday 的标准建模，是矩阵组织的基础。绝不要把 `departmentId` 直接挂到 User 上。

### 1.3 权限分层：RBAC（角色控制）⊂ ABAC（属性控制）⊂ ReBAC（关系控制）

| 层 | 全称 | 解决的问题 | 实现 |
|----|------|----------|------|
| RBAC | Role-Based Access Control（基于角色的访问控制） | 角色到权限的稳定映射 | Role / Permission |
| ABAC | Attribute-Based Access Control（基于属性的访问控制） | 基于属性的动态判定（部门、级别、地理） | Policy（Cedar / OPA） |
| ReBAC | Relationship-Based Access Control（基于关系的访问控制） | "我在那个项目里"——基于关系的判定 | Zanzibar tuples（SpiceDB / OpenFGA） |

**Enterprise 2.0 的协作场景必然走到 ReBAC**，因为权限来源是关系而非角色。

### 1.4 组织是图（Graph），不是树（Tree）

```text
不要：Department.parentDepartmentId  （树结构，无法表达矩阵）
不要：User.departmentId              （用户直属部门，无法支持多岗位）
要：  OrganizationRelation(fromOrgId, toOrgId, relationType)  （关系图）
要：  ReportingLine(subordinateAssignmentId, managerAssignmentId, type)  （汇报图）
```

### 1.5 时间维度是一等公民

矩阵组织变动频繁：重组、合并、调岗、临时项目。系统必须能回答"**2026-03-01 那一刻** Alice 向谁汇报？"——这要求 Assignment / OrgChange 都带 `effectiveAt`（生效时间） / `endAt`（结束时间），不能就地覆盖历史记录。

### 1.6 Modular Monolith First（模块化单体优先）

IAM（身份与访问管理）、Org Graph（组织图）、Authorization（授权）三件套的内部一致性极强；过早拆微服务（Microservices）会造成跨服务事务/缓存噩梦。先做 DDD（领域驱动设计）模块化单体，等边界稳定再拆。

---

## 二、领域划分（Bounded Context 限界上下文）

```text
Platform Domain（平台域）         —— 租户、订阅、Region（区域）、集成、特性开关
Identity & Access Domain（IAM 域）—— 登录身份、会话、机器身份、MFA（多因素认证）
People Domain（人员域）           —— 员工档案、技能、职级（HR 静态数据）
Organization Domain（组织域）     —— OU（组织单元）图、岗位、汇报、成本中心、组织变更
Authorization Domain（授权域）    —— RBAC + ABAC + ReBAC（建议独立服务）
Collaboration Domain（协作域）    —— 工作区、项目、参与、活动流、知识、标签
Social Domain（社交域）           —— 关注、@提及、点赞、背书（Enterprise 2.0 特有）
Governance Domain（治理域）       —— 审计、审批、委派、合规、保留、法务保全
Integration Domain（集成域）      —— Webhook、SCIM、HRIS、Event Bus（事件总线）
Notification Domain（通知域）     —— 通道、偏好、模板
AI / Agent Domain（AI 域）        —— Agent（智能体）、Skill（工具技能）、KnowledgeBase（知识库）、AgentPolicy（智能体策略）
```

> **People 与 Identity 分开**是行业标准（Workday HCM（人力资本管理） vs Microsoft Entra ID）：Identity 关心"能不能登进来"，People 关心"这个员工是谁、在哪个职级、会什么技能"。

---

## 三、各域实体清单

### 3.1 Platform Domain（平台域）

**Tenant（租户）** — SaaS 系统的顶级隔离单元，代表一个订阅客户（公司/团队）

```text
- id              全局唯一标识符（UUID）
- slug            URL 友好短名（如 acme-corp），用于子域名路由（acme-corp.app.com）
- displayName     对外显示名称（如 Acme Corporation）
- plan            订阅套餐（starter | growth | enterprise | custom）
- region          数据存储区域，关联 Region 实体（如 us-east-1）
- status          租户状态（active 活跃 | suspended 暂停 | terminated 已注销）
- settings        租户级全局配置（JSONB，存储主题色、默认语言、密码策略等）
- createdAt       租户创建时间戳
```

**Subscription（订阅）** — 租户的计费合同，记录当前套餐与用量配额

```text
- tenantId        所属租户
- planId          订阅套餐 ID，关联定价表
- quota           用量配额（JSONB，如 {seats: 500, storage_gb: 1000, api_calls_per_month: 10000000}）
- billingCycle    计费周期（monthly 月付 | annual 年付）
- paymentStatus   付款状态（current 正常 | past_due 逾期 | canceled 已取消）
```

**FeatureFlag（特性开关）** — 租户/用户级功能灰度开关，无需发版即可控制功能可见性

```text
- tenantId        所属租户（空表示全局默认）
- key             功能标识键（如 enable_ai_assistant、new_org_chart_ui）
- enabled         是否开启（boolean）
- rolloutPolicy   灰度策略（JSONB，如 {percentage: 20} 表示 20% 用户开启）
- variants        A/B 测试变体配置（JSONB）
```

**Region（区域）** — 数据驻留（Data Residency）配置，满足数据主权合规要求

```text
- id              区域唯一 ID
- code            云服务区域码（如 eu-west-1、ap-southeast-1、cn-north-1）
- provider        云服务商（AWS | Azure | GCP | 阿里云 | 私有化部署）
- complianceZone  合规区域（GDPR（欧盟数据保护）| HIPAA（美国医疗） | SOC2 | CN（中国等保））
```

**EncryptionKey（加密密钥）** — BYOK（自带密钥）支持，客户自管加密主密钥

```text
- tenantId        所属租户
- keyAlias        密钥别名（如 tenant-acme-primary）
- kmsProvider     KMS（密钥管理服务）提供商（AWS KMS | Azure Key Vault | GCP KMS | HashiCorp Vault）
- kmsKeyArn       KMS 中的密钥 ARN（Amazon Resource Name）或资源 ID
- rotationPolicy  密钥轮换策略（JSONB，如 {rotate_every_days: 90}）
- status          密钥状态（active 活跃 | pending_rotation 轮换中 | disabled 已禁用）
```

**AuditConfiguration（审计配置）** — 不同租户对审计的颗粒度要求不同，需可配置

```text
- tenantId        所属租户
- enabledActions  需要记录的操作类型列表（如 ["login", "data_export", "role_change", "delete"]）
- retentionDays   审计日志保留天数（如 365、2555 表示 7 年）
- externalSink    外部日志接收端（如 Splunk、Datadog、AWS S3，用于 SIEM（安全信息与事件管理）对接）
```

**IntegrationConnector（集成连接器）** — 与外部 HR 系统、目录服务的对接入口

```text
- tenantId        所属租户
- type            连接器类型（SCIM（跨域身份同步）| HRIS（人力资源系统）| LDAP（目录协议）| Webhook）
- config          连接配置（JSONB，加密存储，含 endpoint、credential 等）
- syncStatus      同步状态（idle 空闲 | syncing 同步中 | error 错误）
- lastSyncAt      最近一次同步时间戳
```

---

### 3.2 Identity & Access Domain（身份与访问管理域，IAM）

**User（用户）** — 平台账号，代表一个可登录的主体；不等于员工档案

```text
- id              全局唯一用户 ID（UUID，跨租户唯一）
- primaryEmail    主邮箱（用于通知和账号恢复）
- phone           手机号（可选，用于 SMS MFA）
- status          账号状态（active | suspended | deleted | pending_verification 待验证）
- createdAt       账号创建时间
```

> User 是平台身份，员工信息（姓名、职级、部门）在 People Domain 的 EmployeeProfile 中。

**Identity（身份凭据）** — 记录用户通过哪种 IdP（身份提供商）登录，支持多种认证方式

```text
- userId          关联的 User ID
- provider        认证方式（saml（企业 SSO）| oidc（现代 SSO）| password 密码 | passkey 无密码 | social 社交登录）
- externalId      IdP 侧的用户 ID（如 Okta User ID、Azure Object ID）
- credentials     凭据（JSONB，加密存储，含 hashed_password、saml_name_id 等）
- lastLoginAt     最近登录时间
```

**Group（用户组）** — SCIM（跨域身份管理）标准的一等公民；LDAP/AD 的基础，缺少 Group 的 IAM 必然踩坑

```text
- tenantId        所属租户
- id              组 ID
- name            组名称（如 Engineering、Product Managers）
- type            组类型（static 手动维护 | dynamic 按规则自动计算 | synced 从 SCIM/LDAP 同步）
- membershipRule  动态组规则（仅 dynamic 类型，如 "department == 'Engineering' AND level >= 'L3'"）
```

**GroupMember（组成员）** — Group 与成员的多对多关系，支持组嵌套

```text
- groupId         所属组 ID
- principalType   成员类型（user | group（嵌套组）| serviceAccount（服务账号））
- principalId     成员 ID
```

**Membership（成员关系）** — User 与 Tenant 的关系，记录用户以何种身份加入租户

```text
- tenantId        所属租户
- userId          用户 ID
- type            成员类型（employee 员工 | contractor 外包 | partner 合作伙伴 | guest 访客）
- joinedAt        加入时间
- status          关系状态（active | suspended | offboarded 已离职）
```

**ServiceAccount（服务账号）** — 机器身份，用于 API 集成、CI/CD 流水线、自动化脚本

```text
- tenantId        所属租户
- name            服务账号名称（如 github-actions-deployer、billing-webhook-receiver）
- type            用途类型（integration 外部集成 | automation 自动化 | agent AI 智能体）
- ownerId         责任人 User ID（离职时需要交接）
- rotationPolicy  密钥轮换策略（JSONB，如 {rotate_every_days: 90, notify_days_before: 7}）
```

**APIKey（API 密钥）** — ServiceAccount 的访问凭据

```text
- serviceAccountId  所属服务账号
- keyHash           密钥哈希值（原始密钥只在创建时展示一次，存储哈希）
- scopes            权限范围列表（如 ["read:projects", "write:comments"]）
- expiresAt         过期时间（强制要求短生命周期，如 90 天）
- lastUsedAt        最近使用时间（用于检测僵尸密钥）
```

**Session（登录会话）** — 记录当前登录态，授权系统必须感知 Session，支持强制登出和异常检测

```text
- userId          登录用户 ID
- tenantId        当前活跃租户
- deviceId        设备指纹（用于识别可信设备）
- ip              登录来源 IP 地址
- mfaVerified     是否已完成 MFA（多因素认证）验证（boolean）
- expiresAt       会话过期时间
- riskScore       风险分（0.0–1.0，异常登录检测，如异地登录触发二次认证）
```

**MFADevice（多因素认证设备）** — 用户绑定的 MFA（多因素认证）设备

```text
- userId          所属用户
- type            设备类型（TOTP（时间一次性密码，如 Authenticator App）| WebAuthn（生物识别/硬件密钥）| SMS（短信验证码）| Hardware（硬件令牌如 YubiKey））
- status          设备状态（active | revoked 已吊销）
- enrolledAt      绑定时间
```

**Invitation（邀请）** — 用户邀请机制，支持跨租户邀请（Enterprise 2.0 的"打破边界"特征）

```text
- tenantId        发起邀请的租户
- inviterUserId   邀请人 User ID
- email           被邀请人邮箱
- scope           邀请目标（JSONB，如 {resource_type: "workspace", resource_id: "ws-123", role: "editor"}）
- expiresAt       邀请链接过期时间
- status          邀请状态（pending 待接受 | accepted | expired | revoked 已撤回）
```

---

### 3.3 Authorization Domain（授权域）——建议独立服务

**Role（角色）** — RBAC（基于角色的访问控制）的核心，定义一组权限的集合

```text
- tenantId   所属租户（null 表示系统内置角色）
- key        角色标识键（如 org_admin、project_editor、read_only）
- name       显示名称（如 组织管理员、项目编辑者）
- scope      角色作用域（tenant 租户级 | org 组织级 | workspace 工作区级 | project 项目级）
```

**Permission（权限）** — 原子权限单元，表达"对某类资源可以做什么操作"

```text
- resource   资源类型（如 project、document、org_chart、user）
- action     操作类型（如 read、write、delete、export、admin）
```

**RoleBinding（角色绑定）** — RBAC 的授权关系；将角色授予某主体，可限定在特定资源上

```text
- roleId          授予的角色 ID
- principalType   被授权主体类型（user | group | serviceAccount）
- principalId     被授权主体 ID
- resourceType    限定的资源类型（可为空，表示全范围）
- resourceId      限定的资源 ID（可为空，表示全范围）
```

**Policy（策略）** — ABAC（基于属性的访问控制）策略，用 Cedar / OPA 编写，支持基于上下文的动态判定

```text
- subject     主体条件（如 user.department == resource.department）
- resource    资源条件（如 resource.classification == 'confidential'）
- action      操作（如 download）
- condition   附加条件（如 time_of_day between 09:00 and 18:00）
- effect      判定结果（allow | deny）
```

**RelationTuple（关系元组）** — ReBAC（基于关系的访问控制）的核心存储单元，对应 Google Zanzibar 模型；由 SpiceDB / OpenFGA 管理

```text
- namespace         对象命名空间（如 project、org、document）
- objectId          对象 ID
- relation          关系类型（如 editor、viewer、owner、member）
- subjectNamespace  主体命名空间（如 user、group）
- subjectId         主体 ID
- subjectRelation   主体内部关系（如 group:engineering#member，表示 engineering 组的所有成员）

示例：project:alpha#editor@group:engineering#member
      （engineering 组的所有成员对 alpha 项目有 editor 权限）
```

> **AccessGrant** 与 **RoleBinding / RelationTuple** 概念重合，建议合并——RoleBinding 负责 RBAC 视角，RelationTuple 负责 ReBAC 视角，避免概念冗余。

---

### 3.4 People Domain（人员域）——HR 静态数据，与 Identity 分离

**EmployeeProfile（员工档案）** — 员工的 HR 档案，关注"这个人是谁"

```text
- userId            关联的 User ID（1:1）
- tenantId          所属租户
- employeeNumber    工号（HR 系统唯一标识，如 EMP-10042）
- displayName       显示名称（如 张三 / Alice Zhang）
- pronouns          代词偏好（如 she/her、he/him，体现 DEI（多元包容））
- bio               个人简介（UGC，E2.0 社交特征）
- avatarUrl         头像 URL
- hireDate          入职日期
- terminationDate   离职日期（为空表示在职）
- locale            语言地区（如 zh-CN、en-US，影响 UI 和通知语言）
- timezone          时区（如 Asia/Shanghai，影响提醒时间）
```

**JobFamily（职能族）** — 定义职位族与级别体系，是 Workday / SAP 的 HR 标准

```text
- tenantId   所属租户
- name       职能族名称（如 Engineering（工程）| Product（产品）| Sales（销售）| Design（设计））
- levels     级别序列（数组，如 ["L1", "L2", "L3", "Staff", "Principal", "Distinguished"]）
```

**JobGrade（职级）** — 某个职能族内具体级别的详细定义

```text
- jobFamilyId           所属职能族 ID
- level                 级别标识（如 L3、Staff、P7）
- salaryBand            薪酬范围（JSONB，加密存储，如 {min: 200000, max: 300000, currency: "CNY"}）
- competencyFrameworkId 关联胜任力框架 ID（定义该级别需要哪些技能和行为）
```

**Skill（技能）** — 系统定义的技能标签，是 E2.0 知识图谱的基础

```text
- tenantId   所属租户
- name       技能名称（如 Kubernetes、产品设计、财务建模）
- category   技能分类（如 技术 | 管理 | 领域知识）
```

**UserSkill（用户技能）** — 员工拥有某项技能的记录，是 E2.0 中背书（Endorsement）的作用对象

```text
- userId             用户 ID
- skillId            技能 ID
- proficiency        熟练度（beginner 初学 | intermediate 中级 | expert 专家）
- endorsementsCount  被同事背书次数（E2.0 社交信号，类似 LinkedIn Endorsement）
```

---

### 3.5 Organization Domain（组织域）——矩阵式组织核心

**OrganizationUnit（组织单元）** — 组织结构的节点，可以是任意类型的组织层级

```text
- id          组织单元唯一 ID
- tenantId    所属租户
- type        组织类型（division 事业部 | department 部门 | team 小组 | tribe 部落（Spotify 模型）|
              squad 小队（Spotify 模型）| chapter 章节（职能横切）| guild 行会（社区）|
              legalEntity 法人实体 | region 地区）
- name        组织名称
- code        组织编码（如 ENG-PLATFORM-001，用于 HR 系统对接）
- status      状态（active | archived 已归档）
- effectiveAt 生效时间（时间维度，支持历史回溯）
- endAt       结束时间（为空表示当前有效）
```

**OrganizationRelation（组织关系）** — 组织之间的关系边，**这是用图取代树的核心实体**

```text
- fromOrgId      起始组织单元 ID
- toOrgId        目标组织单元 ID
- relationType   关系类型（parent_of 上下级 | manages 管理 | collaborates_with 协作 |
                 funds 资金支持 | dotted_line_to 虚线汇报 | reports_to 实线汇报 | belongs_to 归属）
- effectiveAt    关系生效时间
- endAt          关系结束时间（为空表示当前有效）
```

**Position（岗位）** — 岗位定义，与具体的人无关；可以空缺（Headcount 还未填满）

```text
- id           岗位唯一 ID
- orgId        归属组织单元 ID
- title        岗位名称（如 Senior Engineering Manager、产品负责人）
- jobGradeId   关联职级 ID（决定薪酬范围和汇报期望）
- costCenterId 归属成本中心 ID（财务维度）
- headcount    核定人数（如 1 表示该岗位只能有一人，2 表示双编）
- status       岗位状态（open 空缺招聘中 | filled 已填满 | frozen 冻结）
```

**Assignment（岗位分配）** — User 占用 Position 的关系，是矩阵组织时间分配（allocation）的核心实体

```text
- tenantId    所属租户
- userId      用户 ID
- positionId  岗位 ID
- allocation  时间投入比例（0.0–1.0，如 0.5 表示 50% 工时投入此岗位）
- isPrimary   是否主岗位（true 表示这是决定 HR 主汇报线的岗位）
- startAt     分配开始时间
- endAt       分配结束时间（为空表示当前有效）
- status      分配状态（active 在岗 | on_leave 请假中 | terminated 已离职）
```

**ReportingLine（汇报线）** — 汇报关系，与 Assignment 关联而非 User，支持矩阵组织的多汇报线

```text
- subordinateAssignmentId  下属的 Assignment ID（某人在某岗位上）
- managerAssignmentId      上级的 Assignment ID（上级在其对应岗位上）
- type                     汇报线类型（solid 实线（行政上级）| dotted 虚线（业务上级）|
                           functional 职能汇报 | project 项目汇报）
```

**CostCenter（成本中心）** — 财务维度，记录各组织单元的预算归属

```text
- tenantId    所属租户
- code        成本中心编码（如 CC-ENG-001，与财务系统对接的唯一标识）
- ownerOrgId  负责该成本中心的组织单元 ID
- currency    记账货币（如 CNY、USD）
```

**ExternalWorker（外部用工）** — 外包/派遣/实习生，有独立的合规要求和自动失效访问

```text
- tenantId         所属租户
- userId           关联 User ID
- agencyId         派遣机构 ID（如 外包公司）
- contractType     合同类型（contractor 项目外包 | vendor 供应商 | intern 实习生）
- contractStartAt  合同开始日期
- contractEndAt    合同结束日期
- accessExpiresAt  系统访问权限自动过期时间（通常等于合同结束日，合规要求）
```

**OrgChange（组织变更记录）** — 组织结构变动历史，支持时间旅行查询（"查看某时间点的组织结构"）

```text
- tenantId     所属租户
- changeType   变更类型（created 新建 | restructured 重组 | merged 合并 | dissolved 解散 | hired 入职 | terminated 离职）
- effectiveAt  变更生效时间
- snapshot     变更时刻的完整组织快照（JSONB，用于历史回放）
- requestedBy  发起变更的 User ID
- approvalId   关联审批流程 ID（大型组织变更需要审批）
```

---

### 3.6 Collaboration Domain（协作域）

**Workspace（工作区）** — 逻辑协作空间，是 Project 的容器

```text
- tenantId    所属租户
- name        工作区名称
- visibility  可见性（public 租户内可见 | private 仅成员可见）
```

**Project（项目）** — 核心协作单元，可跨组织、跨人员

```text
- workspaceId       所属工作区 ID
- ownerOrgId        负责组织单元 ID（承担资源和决策）
- visibility        可见性（public | private | restricted 受限）
- classificationId  数据分级 ID，关联 DataClassification（影响 DLP 数据防泄漏策略）
```

**TeamSpace（临时团队空间）** — 跨组织的临时项目团队，生命周期与项目绑定

```text
- projectId   关联项目 ID
- lifecycle   生命周期阶段（draft 规划中 | active 进行中 | archived 已归档）
```

**Participation（参与关系）** — 记录某个主体（用户/组/机器）以何种角色参与某资源

```text
- principalType  参与者类型（user | group | serviceAccount）
- principalId    参与者 ID
- resourceType   资源类型（project | workspace | teamspace）
- resourceId     资源 ID
- role           参与角色（owner 所有者 | editor 编辑者 | viewer 查看者 | commenter 评论者）
- joinedAt       加入时间
```

**SharedSpace（共享空间）** — 跨租户协作，类似 Slack Connect / Microsoft Teams 外部协作

```text
- hostTenantId   主机租户 ID（资源所有方）
- guestTenantId  访客租户 ID（被邀请方）
- resourceType   共享的资源类型（project | workspace）
- resourceId     共享的资源 ID
- status         协作状态（pending 待接受 | active | revoked 已撤销）
```

**Activity（活动记录）** — 活动流（Activity Stream），遵循 ActivityStreams 2.0 标准，是 E2.0 的标志性能力

```text
- actorId           操作发起者 ID
- verb              操作动词（created 创建 | updated 更新 | commented 评论 | liked 点赞 | joined 加入 | mentioned @提及）
- objectType        被操作对象类型（document | task | comment 等）
- objectId          被操作对象 ID
- target            操作发生的上下文（如 "在 Project Alpha 中"）
- contextResourceId 上下文资源 ID
- timestamp         操作发生时间
```

**Knowledge（知识条目）** — UGC（用户生成内容）形式的 Wiki 知识，是 E2.0 "Authoring 人人可创作" 的体现

```text
- workspaceId       所属工作区
- title             标题
- content           正文（Markdown 或富文本）
- version           版本号（支持版本历史，每次修改递增）
- classificationId  数据分级（影响谁可以看到这条知识）
```

**Tag（标签）** — Folksonomy（民间分类法）标签，由用户自创，而非 IT 预定义的分类体系

```text
- tenantId    所属租户
- name        标签名称（如 kubernetes、季度OKR、待讨论）
- createdBy   创建者 User ID
```

**Tagging（标签关联）** — 将标签附加到任意资源上

```text
- tagId        标签 ID
- resourceType 被标记资源类型（project | document | knowledge | task 等）
- resourceId   被标记资源 ID
- taggedBy     打标签的 User ID
```

---

### 3.7 Social Domain（社交域）——Enterprise 2.0 特有，非附加功能

**Follow（关注）** — 用户关注其他用户/团队/话题，构建企业内社交图谱

```text
- followerUserId  关注发起者 User ID
- followeeType    被关注对象类型（user | org | tag | project）
- followeeId      被关注对象 ID
```

**Mention（@提及）** — 记录 @提及关系，触发通知并建立内容间的社交连接

```text
- sourceType      提及来源类型（comment | knowledge | activity）
- sourceId        来源内容 ID
- mentionedUserId 被提及的 User ID
```

**Endorsement（技能背书）** — 员工为同事的技能背书，体现 E2.0 的社交信任传播

```text
- endorserUserId  背书人 User ID
- userSkillId     被背书的 UserSkill ID（某人的某项技能）
```

**Reaction（表情回应）** — 对内容的快速情感反馈，低成本参与机制

```text
- resourceType  被回应内容类型（comment | activity | knowledge）
- resourceId    被回应内容 ID
- userId        回应者 User ID
- type          表情类型（like 点赞 | celebrate 庆祝 | insightful 有见地 | curious 好奇）
```

---

### 3.8 Governance Domain（治理域）

**AuditLog（审计日志）** — 不可篡改的操作记录，Enterprise 合规的根基

```text
- tenantId      所属租户
- actorType     操作发起者类型（user | service_account | agent AI 智能体）
- actorId       操作发起者 ID
- action        操作描述（如 role.assigned、document.exported、user.terminated）
- resourceType  操作对象类型
- resourceId    操作对象 ID
- before        操作前状态快照（JSONB，用于变更追溯）
- after         操作后状态快照（JSONB）
- ip            操作来源 IP 地址
- userAgent     客户端标识（浏览器/API/Agent）
- timestamp     操作时间戳（不可修改）
```

**ApprovalWorkflow（审批流程）** — 企业内需要多级审批的操作（如大规模组织变更、敏感权限授予）

```text
- tenantId      所属租户
- type          审批类型（org_restructure 组织重组 | role_escalation 权限升级 | offboarding 离职交接 等）
- initiator     发起人 User ID
- approvers     审批人策略（JSONB，如 [{role: "cto", required: true}, {group: "hr-ops"}]）
- currentStep   当前所在审批步骤
- state         流程状态（pending 待审批 | approved 已批准 | rejected 已拒绝 | expired 已过期）
- slaDueAt      SLA（服务级别协议）截止时间
```

**ApprovalStep（审批步骤）** — 审批流程中的单个步骤记录

```text
- workflowId      所属审批流程 ID
- stepIndex       步骤序号（0 开始）
- approverPolicy  该步骤的审批人策略（JSONB）
- decision        审批决定（approved | rejected | delegated 已委派他人）
- decidedAt       决定时间
```

**Delegation（委派）** — 授权委派，A 在一段时间内将特定权限委派给 B 代为行使（如出差、休假）

```text
- delegatorId   委派人 User ID
- delegateeId   被委派人 User ID
- scope         委派范围（JSONB，如 {resource_type: "project", resource_id: "prj-001", roles: ["editor"]}）
- startAt       委派开始时间
- endAt         委派结束时间（到期自动失效）
```

**DataRetentionPolicy（数据保留策略）** — 定义各类数据的保留期限和到期处理方式

```text
- tenantId      所属租户
- resourceType  适用的资源类型（如 audit_log、message、document）
- retentionDays 保留天数（如 365、2555 表示 7 年）
- action        到期后动作（archive 归档 | delete 删除 | anonymize 匿名化）
```

**LegalHold（法务保全）** — 诉讼/调查期间冻结特定数据，临时优先级高于 DataRetentionPolicy

```text
- tenantId    所属租户
- name        保全案件名称（如 "2026Q1-诉讼-供应商纠纷"）
- custodians  数据保管人 User ID 列表（需要保留其所有相关数据）
- scope       保全数据范围描述（JSONB，如 {date_range: "2024-01-01 to 2025-12-31", types: ["email", "document"]}）
- issuedBy    发起人 User ID（通常是法务团队）
- issuedAt    发起时间
- status      保全状态（active 生效中 | released 已解除）
- releaseAt   解除时间（为空表示未解除）
```

**DataClassification（数据分级）** — 定义数据敏感度级别，支撑 DLP（数据防泄漏）策略

```text
- tenantId         所属租户
- level            分级（public 公开 | internal 内部 | confidential 机密 | restricted 受限）
- label            分级标签（如 "仅限HR查看"、"外部可共享"）
- handlingPolicy   处理规范（JSONB，如 {can_export: false, requires_approval: true, watermark: true}）
```

**ComplianceFramework（合规框架）** — 记录租户所遵循的合规标准及控制项

```text
- tenantId      所属租户
- standard      合规标准（SOC 2（北美 SaaS 安全）| GDPR（欧盟数据保护）| HIPAA（美国医疗）| ISO 27001（信息安全））
- controls      控制项清单（JSONB，各标准的具体条款映射）
- lastAuditAt   最近一次审计时间
- status        合规状态（compliant 已合规 | in_progress 整改中 | non_compliant 不合规）
```

---

### 3.9 Integration Domain（集成域）

**Webhook（网络钩子）** — 向外部系统推送事件，实现实时集成

```text
- tenantId      所属租户
- url           接收端 URL
- events        订阅的事件类型列表（如 ["user.created", "org.restructured", "role.assigned"]）
- secret        签名密钥（用于接收端验证消息合法性，HMAC-SHA256）
- status        状态（active | disabled）
- retryPolicy   重试策略（JSONB，如 {max_attempts: 5, backoff: "exponential"}）
```

**EventLog（事件日志）** — Webhook 推送记录，基于 Outbox（发件箱）模式保证至少一次投递

```text
- webhookId       关联 Webhook ID
- eventType       事件类型（如 user.created）
- payload         事件载荷（JSONB）
- deliveryStatus  投递状态（pending 待发送 | delivered 已送达 | failed 失败）
- attempts        已尝试次数
- nextRetryAt     下次重试时间
```

**SCIMSync（SCIM 同步记录）** — 跟踪 SCIM 2.0（跨域身份管理）同步状态，与 Okta、Azure Entra ID 等 IdP 对接

```text
- tenantId             所属租户
- connectorId          关联 IntegrationConnector ID
- resourceType         同步资源类型（User | Group）
- externalId           IdP 侧的资源 ID
- lastSyncAt           最近同步时间
- syncStatus           同步状态（synced 已同步 | pending 待同步 | conflict 冲突）
- conflictResolution   冲突解决策略（system_wins 以本系统为准 | scim_wins 以 IdP 为准）
```

---

### 3.10 Notification Domain（通知域）

**NotificationChannel（通知通道）** — 用户配置的通知接收通道

```text
- tenantId  所属租户
- userId    用户 ID
- type      通道类型（email | slack | webhook | in-app 站内 | dingtalk 钉钉 | wecom 企业微信）
- config    通道配置（JSONB，如 {email: "alice@acme.com"} 或 {slack_channel: "#alerts"}）
- enabled   是否启用（boolean）
```

**NotificationPreference（通知偏好）** — 用户对不同事件类型的通知偏好配置

```text
- userId      用户 ID
- eventType   事件类型（如 mention 被@提及 | approval_required 待审批 | org_change 组织变动）
- channelId   选用的通知通道 ID
- frequency   通知频率（realtime 实时 | digest 汇总（如每日摘要）| off 关闭）
```

**NotificationTemplate（通知模板）** — 各事件类型的通知内容模板，支持多语言

```text
- tenantId    所属租户（null 为系统默认模板）
- eventType   适用事件类型
- locale      语言地区（如 zh-CN、en-US）
- subject     通知标题（支持模板变量，如 "{{actor}} 邀请您加入 {{project}}"）
- body        通知正文（支持 HTML 和纯文本双版本）
```

---

### 3.11 AI / Agent Domain（AI 与智能体域）——Agent-as-Principal

> **核心原则：Agent（AI 智能体）必须作为 Principal（主体）进入 Authorization（授权系统）与 AuditLog（审计日志）。** 否则 LLM（大语言模型）触发跨权限调用后无法追责，将成为下一代生产事故主因。

**Agent（智能体）** — 自主执行任务的 AI 实体，可代表用户或组织执行操作

```text
- tenantId   所属租户
- name       智能体名称（如 HR Onboarding Bot、Code Review Assistant）
- ownerId    责任人 User ID（谁为该 Agent 的行为负责）
- modelRef   所使用的 LLM（大语言模型）引用（如 claude-opus-4-7、gpt-4o）
- status     状态（active | suspended | deprecated）
```

**AgentIdentity（智能体身份）** — Agent 在授权系统中的身份主体，继承自 ServiceAccount

```text
- agentId      关联 Agent ID
- principalId  在 Authorization Domain（授权域）中的 Principal ID（用于权限绑定）
```

**ToolSkill（工具技能）** — Agent 可调用的工具/函数定义（注：命名为 ToolSkill 以区别 People Domain 中的 Skill）

```text
- agentId   所属 Agent ID
- toolKey   工具唯一标识（如 search_documents、update_org_chart、send_notification）
- schema    工具参数 Schema（JSONB，OpenAPI / JSON Schema 格式）
```

**KnowledgeBase（知识库）** — Agent 的检索增强（RAG）知识源

```text
- tenantId          所属租户
- name              知识库名称（如 HR Policy、Technical Docs）
- indexBackend      索引后端（如 OpenSearch、pgvector、Pinecone）
- classificationId  数据分级 ID（决定哪些 Agent 可以访问此知识库）
```

**ContextPolicy（上下文策略）** — 控制 Agent 在执行任务时可以感知哪些上下文，防止敏感信息泄漏给 LLM

```text
- agentId        所属 Agent ID
- scope          允许访问的上下文范围（JSONB，如 {can_read_user_profile: true, can_read_salary: false}）
- redactionRules 脱敏规则（JSONB，如 {fields: ["email", "phone"], method: "mask"}）
```

**AgentSession（智能体会话）** — Agent 执行一次任务的完整会话，关联追踪链路

```text
- agentId                关联 Agent ID
- initiatorPrincipalId   发起者 ID（谁触发了这次 Agent 执行）
- startedAt              会话开始时间
- endedAt                会话结束时间
- traceId                分布式追踪 ID（关联所有子操作，用于 Debug 和 Audit）
```

**AgentAction（智能体操作）** — Agent 在会话中执行的每个具体操作，全部写入 AuditLog

```text
- agentSessionId  所属 AgentSession ID
- actionType      操作类型（tool_call 调用工具 | knowledge_query 查询知识库 | api_call 调用外部 API）
- resourceRef     操作涉及的资源引用（如 project:alpha、user:alice）
- result          操作结果摘要（成功/失败/返回值）
```

---

## 四、矩阵组织：实现要点

### 4.1 标准查询：递归 CTE（公共表表达式）

```sql
-- 查询某用户的全部上行汇报链（包含 solid line 实线和 dotted line 虚线）
WITH RECURSIVE chain AS (
  -- 基础：找到该用户所有 active（在岗）的 Assignment（岗位分配）
  SELECT a.id AS assignment_id,
         rl.manager_assignment_id,
         rl.type,
         0 AS depth
  FROM assignments a
  JOIN reporting_lines rl ON rl.subordinate_assignment_id = a.id
  WHERE a.user_id = :user_id
    AND a.status = 'active'

  UNION ALL

  -- 递归：沿汇报线向上追溯
  SELECT rl2.subordinate_assignment_id,
         rl2.manager_assignment_id,
         rl2.type,
         chain.depth + 1
  FROM reporting_lines rl2
  JOIN chain ON rl2.subordinate_assignment_id = chain.manager_assignment_id
  WHERE chain.depth < 12   -- 防止环（Cycle）导致爆栈，12 层足够覆盖任何企业层级
)
SELECT * FROM chain;
```

### 4.2 防环检测（Cycle Detection）

写入 `OrganizationRelation` / `ReportingLine` 时必须做环检测——否则一次错误的 dotted line（虚线汇报）录入即可让全公司查询陷入无限递归。常用做法：

- **写入前 DFS（深度优先搜索）**：在内存中跑一次，验证新增边不会形成环。
- **PostgreSQL 触发器 + 递归 CTE**：在 DB 层校验，路径中不能存在反向边。

### 4.3 时间点回放（Temporal Query）

`Assignment`（岗位分配）/ `OrganizationRelation`（组织关系）/ `ReportingLine`（汇报线）都带 `effectiveAt / endAt`。任何 t 时刻的组织结构 = 这三张表里所有满足 `effectiveAt ≤ t < endAt` 的记录。**绝不就地覆盖历史**——这是合规与审计的硬要求。

### 4.4 读写分离（CQRS——命令查询职责分离）

矩阵组织 + ReBAC（基于关系的访问控制）的读放大极高（一次"我能看到哪些 project"的查询会展开到几百条 RelationTuple）。生产实践：

- **写**：PostgreSQL（Org / Assignment / RelationTuple 写主库）。
- **读**：派生 Read Model（读模型）到 Redis / OpenSearch / 物化视图（预计算"我向谁汇报"、"我管的人"、"我能看到的 Project 列表"）。
- 通过 Outbox（发件箱）模式 + 事件流（EventLog）保持最终一致。

---

## 五、权限：Zanzibar ReBAC Schema 范例

```text
definition user {}

definition service_account {}

definition group {
  relation member: user | service_account
}

definition organization {
  relation admin: user
  relation member: user | group#member
}

definition project {
  relation owner: organization
  relation editor: user | group#member
  relation viewer: user | group#member | organization#member

  permission edit = editor + owner->admin
  permission view = viewer + edit
}
```

对应的 RelationTuple（关系元组）示例：

```text
project:alpha#editor@user:alice                        -- alice 是 alpha 项目的编辑者
project:alpha#editor@group:engineering#member          -- engineering 组的所有成员是 alpha 项目的编辑者
organization:platform#admin@user:bob                   -- bob 是 platform 组织的管理员
project:alpha#owner@organization:platform              -- platform 组织拥有 alpha 项目
```

**为什么不用自研 ACL（访问控制列表）：** 一旦出现 `editor + owner->admin` 这样的派生权限、Group 嵌套、多 Tenant 隔离，自研系统的 corner case（边界情况）会爆炸。SpiceDB / OpenFGA 把这类问题的工程化沉淀到了通用引擎里。

---

## 六、多租户隔离策略

| 策略 | 适用场景 | 优势 | 劣势 |
|------|----------|------|------|
| Shared DB + tenant_id（+ RLS 行级安全兜底） | 中小客户、SaaS 主干 | 成本低、运维简单 | 隔离弱，需严格的 RLS |
| Schema-per-tenant（每租户独立 Schema） | 中型企业客户、迁移友好 | 隔离更好、可独立备份还原 | 连接池和 schema 数量需控制 |
| Dedicated DB（独立数据库） | 大型 Enterprise | 强隔离、合规友好 | 成本与运维复杂度高 |
| Dedicated Cluster + BYOK + 区域专属 | 金融、政务、跨国合规 | 物理隔离 + 数据主权 | 成本极高 |

**默认主力**：Shared DB + tenant_id + RLS（行级安全）。

```sql
-- 开启行级安全（RLS），数据库层面防止跨租户数据泄漏
ALTER TABLE projects ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation ON projects
  USING (tenant_id = current_setting('app.current_tenant_id')::uuid);
```

应用层每个连接 / 事务前执行 `SET LOCAL app.current_tenant_id = '...'`，即使代码忘了带 `tenant_id` 条件，DB（数据库）层也能兜住。**这一行 RLS 兜底防住的事故，过去十年里救过无数 SaaS。**

---

## 七、关键基础设施推荐

| 能力 | 推荐 | 理由 |
|------|------|------|
| OLTP（在线事务处理）主库 | PostgreSQL | RLS（行级安全）、JSONB、递归 CTE、分区（Partitioning） |
| ReBAC（关系访问控制）引擎 | SpiceDB / OpenFGA | Google Zanzibar 工业级实现，开源 |
| ABAC（属性访问控制）策略 | Cedar / OPA | 标准化、可审计、可单元测试 |
| 全文搜索 | OpenSearch | 权限感知索引（Search-as-a-Service 模式） |
| 分析 / OLAP | ClickHouse | 审计日志查询、活动流聚合分析 |
| 事件流 / Outbox（发件箱） | Kafka / Redpanda | Webhook 推送、跨域事件驱动 |
| 缓存 / Read Model（读模型） | Redis | 汇报链展开、ACL（访问控制列表）缓存 |
| KMS（密钥管理服务） | AWS KMS / GCP KMS（BYOK 暴露 CMK） | 合规加密，支持 BYOK（自带密钥） |
| Identity（身份认证）平台 | Auth0 / Entra ID / Keycloak | SSO/SAML/OIDC/SCIM 不要自研 |

---

## 八、Enterprise-grade 必须支持的能力清单

| 域 | 必备能力 |
|----|---------|
| Identity（身份） | SAML 2.0（企业 SSO）、OIDC（现代 SSO）、SCIM 2.0（用户同步）、MFA（多因素认证，含 WebAuthn）、JIT Provisioning（即时开通）、Session（会话）管控 |
| People & Org（人员与组织） | 矩阵汇报、多 Position（多岗位）、Allocation（工时分配）、临时分配、外部用工、组织变更历史 |
| Authorization（授权） | RBAC + ABAC + ReBAC、委派（Delegation）、Tenant-scoped & Org-scoped 角色 |
| Governance（治理） | AuditLog（不可篡改）、ApprovalWorkflow（审批流）、Delegation（委派）、Retention（数据保留）、LegalHold（法务保全）、DataClassification（数据分级） |
| Platform（平台） | BYOK（自带密钥）、Region（区域）、Data Residency（数据主权）、租户级特性开关、Sandbox（沙箱）租户 |
| Integration（集成） | SCIM（用户同步）、Webhook（事件推送）、HRIS（HR 系统）connector、Event Bus（事件总线） |
| Notification（通知） | 多通道（邮件/钉钉/企微/Slack）、偏好配置、模板、本地化 |
| Collaboration（协作） | Workspace、Project、跨租户 SharedSpace（Connect-like）、Activity Stream（活动流）、UGC（用户生成）Wiki、Tag |

---

## 九、最终实体结构总览

```text
Platform（平台域）
 ├── Tenant                   租户
 ├── Subscription             订阅
 ├── FeatureFlag              特性开关
 ├── Region                   数据驻留区域
 ├── EncryptionKey            BYOK 加密密钥
 ├── AuditConfiguration       审计配置
 └── IntegrationConnector     集成连接器

Identity & Access（IAM 身份与访问域）
 ├── User                     平台账号
 ├── Identity                 登录凭据/IdP 绑定
 ├── Group / GroupMember      用户组 / 组成员
 ├── Membership               用户与租户关系
 ├── ServiceAccount           机器身份
 ├── APIKey                   API 密钥
 ├── Session                  登录会话
 ├── MFADevice                多因素认证设备
 └── Invitation               邀请（含跨租户）

Authorization（授权域）
 ├── Role                     RBAC 角色
 ├── Permission               原子权限
 ├── RoleBinding              角色绑定（RBAC）
 ├── Policy                   ABAC 策略（Cedar/OPA）
 └── RelationTuple            关系元组（ReBAC，SpiceDB/OpenFGA）

People（人员域）
 ├── EmployeeProfile          员工档案
 ├── JobFamily                职能族
 ├── JobGrade                 职级
 ├── Skill                    技能标签
 └── UserSkill                用户技能

Organization（组织域）
 ├── OrganizationUnit         组织单元
 ├── OrganizationRelation     组织关系图
 ├── Position                 岗位
 ├── Assignment               岗位分配
 ├── ReportingLine            汇报线
 ├── CostCenter               成本中心
 ├── ExternalWorker           外部用工
 └── OrgChange                组织变更快照

Collaboration（协作域）
 ├── Workspace                工作区
 ├── Project                  项目
 ├── TeamSpace                临时团队空间
 ├── Participation            参与关系
 ├── SharedSpace              跨租户协作空间
 ├── Activity                 活动流（ActivityStreams 2.0）
 ├── Knowledge                UGC 知识条目
 └── Tag / Tagging            用户自创标签

Social（社交域）                Enterprise 2.0 特征
 ├── Follow                   关注
 ├── Mention                  @提及
 ├── Endorsement              技能背书
 └── Reaction                 表情回应

Governance（治理域）
 ├── AuditLog                 审计日志
 ├── ApprovalWorkflow         审批流程
 ├── ApprovalStep             审批步骤
 ├── Delegation               权限委派
 ├── DataRetentionPolicy      数据保留策略
 ├── LegalHold                法务保全
 ├── DataClassification       数据分级
 └── ComplianceFramework      合规框架

Integration（集成域）
 ├── Webhook                  事件推送钩子
 ├── EventLog                 推送记录（Outbox 模式）
 └── SCIMSync                 SCIM 同步记录

Notification（通知域）
 ├── NotificationChannel      通知通道
 ├── NotificationPreference   通知偏好
 └── NotificationTemplate     通知模板

AI / Agent（AI 与智能体域）
 ├── Agent                    智能体
 ├── AgentIdentity            智能体 Principal 身份
 ├── ToolSkill                工具技能
 ├── KnowledgeBase            知识库
 ├── ContextPolicy            上下文策略
 ├── AgentSession             智能体会话
 └── AgentAction              智能体操作记录
```

---

## 十、行业里最容易失败的点（务必避开）

1. **Tenant 与 Organization 耦合**——后期想拆开几乎要重写整个数据模型。
2. **用树表达矩阵组织**——一旦出现 dotted line（虚线汇报）/ 跨部门项目就崩。
3. **User 直接挂 departmentId / role**——失去多 Position（多岗位）、临时分配、历史回放能力。
4. **把权限塞进 JWT（JSON 网络令牌）**——Enterprise 权限是动态的，JWT 只能放 Principal Identity（主体身份）；Authorization（授权）必须实时查询。
5. **自研复杂 ACL（访问控制列表）**——Group 嵌套 + 派生权限 + 多 Tenant 维度，自研系统的 corner case 永远修不完。
6. **一开始就微服务**——IAM（身份访问管理）/ Org / Authz 跨服务事务是地狱，先做模块化单体（Modular Monolith）。
7. **HR 与 Identity 不分**——以后想接外部 IdP（身份提供商，如 Okta、Entra ID）会改到怀疑人生。
8. **Activity / Tag / Follow 当作"社交插件"**——它们恰恰是 Enterprise 2.0（麦卡菲 2006 年定义的企业协作进化）的核心，而非附加功能。
9. **不给 Org / Assignment 加时间维度**——审计、追溯、合规一刀切，且无法支持时间点组织结构查询。
10. **Agent 不是 Principal（主体）**——LLM（大语言模型）Agent 跨权限调用后无法追责，将成为下一代生产事故主因。

---

## 十一、推荐实施顺序（90 天蓝图）

| 阶段 | 周次 | 内容 |
|------|------|------|
| 1. 地基 | W1–W3 | Tenant、User、Identity、Membership、Session、RLS（行级安全） |
| 2. 组织 | W4–W6 | OrganizationUnit + OrganizationRelation + Position + Assignment + ReportingLine |
| 3. 授权 | W7–W9 | Role/RoleBinding（RBAC）+ 接 SpiceDB（ReBAC）+ Policy（ABAC） |
| 4. 协作 | W10–W11 | Workspace / Project / Participation / Activity（活动流） |
| 5. 治理 | W12 | AuditLog + ApprovalWorkflow + DataClassification |
| 6. 集成 | 持续 | SCIM（用户同步）、Webhook（事件推送）、HRIS（HR 系统）Connector |
| 7. 社会化 & AI | 持续 | Follow/Tag/Knowledge（Enterprise 2.0 核心）、Agent-as-Principal（智能体主体化） |

> 1–3 是 Enterprise 准入门票；4–5 是付费门槛；6–7 是 Enterprise 2.0 的差异化与未来增长点。

---

## 十二、TypeScript 类型定义

> 以下类型覆盖全部 11 个域。`UUID` 为 `string` 别名；`ISODateString` 为 ISO 8601 时间字符串；JSONB 字段用具体接口或 `Record<string, unknown>` 表示。

```typescript
// ────────────────────────────────────────────────
// 公共基础类型
// ────────────────────────────────────────────────
type UUID = string;                  // 全局唯一标识符（格式：xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx）
type ISODateString = string;         // ISO 8601 时间字符串（如 "2026-05-09T08:00:00Z"）

// 所有被授权的主体类型（Principal）
type PrincipalType = 'user' | 'group' | 'serviceAccount' | 'agent';

// ────────────────────────────────────────────────
// Platform Domain（平台域）
// ────────────────────────────────────────────────
type TenantPlan   = 'starter' | 'growth' | 'enterprise' | 'custom';
type TenantStatus = 'active' | 'suspended' | 'terminated';

/**
 * 租户（Tenant）
 * SaaS 系统的顶层隔离单元，代表一个订阅客户（公司/组织）。
 * 同时承担三个边界：身份边界（所有 User 通过 Membership 加入）、
 * 计费边界（Subscription 挂在 Tenant 上）、数据隔离边界（所有多租户表都带 tenant_id）。
 * 注意：Tenant ≠ Organization，前者是平台概念，后者是 HR 概念。
 */
interface Tenant {
  id:          UUID;
  slug:        string;            // URL 友好短名（如 "acme-corp"）
  displayName: string;            // 显示名称（如 "Acme Corporation"）
  plan:        TenantPlan;
  regionId:    UUID;              // 关联 Region
  status:      TenantStatus;
  settings:    TenantSettings;   // JSONB 配置
  createdAt:   ISODateString;
}

/**
 * 租户配置（TenantSettings）
 * Tenant 的全局可配置项，以 JSONB 内嵌在 Tenant 中。
 * 控制该租户下所有用户的默认语言、时区、密码策略等行为。
 */
interface TenantSettings {
  locale?:         string;        // 默认语言地区（如 "zh-CN"）
  timezone?:       string;        // 默认时区（如 "Asia/Shanghai"）
  passwordPolicy?: PasswordPolicy;
  themeColor?:     string;        // 主题色（十六进制）
}

/**
 * 密码策略（PasswordPolicy）
 * 嵌套在 TenantSettings 中，定义该租户下密码的复杂度规则。
 * 影响所有使用 password provider 登录的 User。
 */
interface PasswordPolicy {
  minLength:          number;     // 最小密码长度
  requireUppercase:   boolean;    // 是否要求大写字母
  requireSpecialChar: boolean;    // 是否要求特殊字符
  expiryDays?:        number;     // 密码过期天数（null = 永不过期）
}

/**
 * 订阅（Subscription）
 * 租户当前的计费合同，记录套餐与资源配额。
 * 驱动功能门控（超出配额时禁用功能）和超量提示。
 * 一个 Tenant 在同一时刻只有一条有效 Subscription。
 */
interface Subscription {
  id:            UUID;
  tenantId:      UUID;
  planId:        UUID;
  quota:         SubscriptionQuota;
  billingCycle:  'monthly' | 'annual';
  paymentStatus: 'current' | 'past_due' | 'canceled';
}

/**
 * 订阅配额（SubscriptionQuota）
 * 嵌套在 Subscription 中，定义该租户的资源用量上限。
 */
interface SubscriptionQuota {
  seats:               number;   // 最大用户席位数
  storageGb:           number;   // 存储配额（GB）
  apiCallsPerMonth:    number;   // 每月 API 调用上限
}

/**
 * 特性开关（FeatureFlag）
 * 功能灰度开关，无需发版即可为特定 Tenant 或用户开启/关闭功能。
 * tenantId 为 null 时表示全局默认值；支持 A/B 测试变体配置。
 */
interface FeatureFlag {
  id:           UUID;
  tenantId:     UUID | null;      // null = 全局默认
  key:          string;           // 功能标识键（如 "enable_ai_assistant"）
  enabled:      boolean;
  rolloutPolicy?: RolloutPolicy;
  variants?:    Record<string, unknown>;  // A/B 测试变体
}

/**
 * 灰度策略（RolloutPolicy）
 * 嵌套在 FeatureFlag 中，定义功能灰度的范围和方式。
 * 支持按比例、白名单用户、白名单组织三种灰度模式。
 */
interface RolloutPolicy {
  percentage?: number;            // 百分比灰度（0–100）
  userIds?:    UUID[];            // 白名单用户
  orgIds?:     UUID[];            // 白名单组织
}

type CloudProvider  = 'AWS' | 'Azure' | 'GCP' | 'Aliyun' | 'on_premise';
type ComplianceZone = 'GDPR' | 'HIPAA' | 'SOC2' | 'CN' | 'none';

/**
 * 数据驻留区域（Region）
 * 记录云服务商和合规区域，是 Data Residency（数据主权）的基础配置。
 * 每个 Tenant 关联一个 Region，决定其数据存储在哪个地理位置、满足哪套合规标准。
 */
interface Region {
  id:              UUID;
  code:            string;        // 云区域码（如 "eu-west-1"）
  provider:        CloudProvider;
  complianceZone:  ComplianceZone;
}

type EncryptionKeyStatus = 'active' | 'pending_rotation' | 'disabled';

/**
 * 加密密钥（EncryptionKey）
 * BYOK（自带密钥）场景下，客户在自己的 KMS 中管理的加密主密钥记录。
 * 系统不存储密钥明文，仅存储 KMS 中的密钥引用（ARN/ID），满足 Enterprise 合规要求。
 */
interface EncryptionKey {
  id:             UUID;
  tenantId:       UUID;
  keyAlias:       string;         // 密钥别名（如 "tenant-acme-primary"）
  kmsProvider:    string;         // KMS 提供商（如 "AWS KMS"）
  kmsKeyArn:      string;         // KMS 资源 ARN 或 ID（已加密存储）
  rotationPolicy: KeyRotationPolicy;
  status:         EncryptionKeyStatus;
}

/**
 * 密钥轮换策略（KeyRotationPolicy）
 * 嵌套在 EncryptionKey / ServiceAccount 中，定义密钥定期轮换的规则。
 */
interface KeyRotationPolicy {
  rotateEveryDays:   number;      // 轮换周期（天）
  notifyDaysBefore:  number;      // 提前几天发通知
}

/**
 * 审计配置（AuditConfiguration）
 * 租户级审计行为的可配置项，不同 Tenant 对审计颗粒度的要求不同。
 * 控制哪些操作写入 AuditLog、日志保留多久、是否实时推送到外部 SIEM 系统。
 */
interface AuditConfiguration {
  id:             UUID;
  tenantId:       UUID;
  enabledActions: string[];       // 需要记录的操作类型列表
  retentionDays:  number;         // 日志保留天数
  externalSink?:  ExternalSinkConfig;  // 外部 SIEM 接收端
}

/**
 * 外部日志接收端配置（ExternalSinkConfig）
 * 嵌套在 AuditConfiguration 中，定义将审计日志推送到外部 SIEM 工具的连接信息。
 */
interface ExternalSinkConfig {
  type:        'splunk' | 'datadog' | 's3' | 'elastic';
  endpoint:    string;
  credentials: Record<string, string>;  // 已加密存储
}

type IntegrationConnectorType = 'SCIM' | 'HRIS' | 'LDAP' | 'Webhook';
type SyncStatus               = 'idle' | 'syncing' | 'error' | 'disabled';

/**
 * 集成连接器（IntegrationConnector）
 * 与外部 HR 系统（Workday、BambooHR）、目录服务（AD、LDAP）的对接配置入口。
 * 负责管理连接凭据（加密）和同步状态，是 SCIM 自动化用户同步的底层配置实体。
 */
interface IntegrationConnector {
  id:         UUID;
  tenantId:   UUID;
  type:       IntegrationConnectorType;
  config:     Record<string, unknown>;  // 连接配置（加密存储）
  syncStatus: SyncStatus;
  lastSyncAt?: ISODateString;
}

// ────────────────────────────────────────────────
// Identity & Access Domain（IAM 域）
// ────────────────────────────────────────────────
type UserStatus = 'active' | 'suspended' | 'deleted' | 'pending_verification';

/**
 * 平台账号（User）
 * 代表一个可登录系统的主体，是平台层面的身份。
 * 注意：User ≠ 员工，员工的姓名、工号、职级等 HR 信息存放在 People Domain 的 EmployeeProfile 中。
 * 一个 User 可以通过 Membership 加入多个 Tenant，在不同 Tenant 中扮演不同角色。
 */
interface User {
  id:           UUID;
  primaryEmail: string;
  phone?:       string;
  status:       UserStatus;
  createdAt:    ISODateString;
}

type IdentityProvider = 'saml' | 'oidc' | 'password' | 'passkey' | 'social';

/**
 * 登录凭据（Identity）
 * 记录 User 通过哪种 IdP（身份提供商）登录，支持同一 User 绑定多种认证方式。
 * 是 SSO（单点登录）、SAML、OIDC、Passkey 等协议的数据载体。
 */
interface Identity {
  id:           UUID;
  userId:       UUID;
  provider:     IdentityProvider;
  externalId:   string;           // IdP 侧的用户 ID
  credentials:  Record<string, unknown>;  // 加密存储
  lastLoginAt?: ISODateString;
}

type GroupType = 'static' | 'dynamic' | 'synced';

/**
 * 用户组（Group）
 * SCIM 2.0 标准的一等公民，是大规模权限管理的基础。
 * 缺少 Group 的 IAM 设计，必然导致逐用户授权的运维噩梦。
 * 支持三种类型：静态（手动维护成员）、动态（按规则自动计算成员）、同步（从 LDAP/SCIM 同步）。
 */
interface Group {
  id:               UUID;
  tenantId:         UUID;
  name:             string;
  type:             GroupType;
  membershipRule?:  string;       // 仅 dynamic 类型，如 "department == 'Eng'"
}

/**
 * 组成员（GroupMember）
 * Group 与其成员之间的关联记录，支持 User、嵌套 Group、ServiceAccount 作为成员。
 * 通过组嵌套可以构建层次化用户组（如 "全公司工程师" 包含多个子组）。
 */
interface GroupMember {
  id:            UUID;
  groupId:       UUID;
  principalType: PrincipalType;
  principalId:   UUID;
}

type MembershipType   = 'employee' | 'contractor' | 'partner' | 'guest';
type MembershipStatus = 'active' | 'suspended' | 'offboarded';

/**
 * 租户成员关系（Membership）
 * 记录 User 以何种身份加入某个 Tenant，是用户在租户内存在的凭证。
 * 区分员工、外包、合作伙伴、访客，对应不同的默认权限范围和合规处理方式。
 */
interface Membership {
  id:       UUID;
  tenantId: UUID;
  userId:   UUID;
  type:     MembershipType;
  joinedAt: ISODateString;
  status:   MembershipStatus;
}

type ServiceAccountType = 'integration' | 'automation' | 'agent';

/**
 * 服务账号（ServiceAccount）
 * 机器身份，用于 API 集成、CI/CD 流水线、自动化脚本等非人类访问场景。
 * 区别于 User 的人类身份；必须有责任人（ownerId），以便在密钥泄露时快速定位和轮换。
 */
interface ServiceAccount {
  id:             UUID;
  tenantId:       UUID;
  name:           string;
  type:           ServiceAccountType;
  ownerId:        UUID;           // 责任人 User ID
  rotationPolicy: KeyRotationPolicy;
}

/**
 * API 密钥（APIKey）
 * ServiceAccount 的访问凭据，用于程序化调用 API。
 * 安全原则：仅存哈希值（原文只在创建时展示一次），必须设置过期时间（短生命周期）。
 */
interface APIKey {
  id:               UUID;
  serviceAccountId: UUID;
  keyHash:          string;       // 仅存哈希，原文只展示一次
  scopes:           string[];     // 权限范围（如 ["read:projects"]）
  expiresAt:        ISODateString;
  lastUsedAt?:      ISODateString;
}

/**
 * 登录会话（Session）
 * 记录用户当前的登录态，授权系统必须感知 Session 才能支持强制登出、异常检测。
 * riskScore 用于识别异地登录、暴力破解等异常行为，触发二次认证或封禁。
 */
interface Session {
  id:          UUID;
  userId:      UUID;
  tenantId:    UUID;
  deviceId?:   string;
  ip:          string;
  mfaVerified: boolean;           // 是否已完成 MFA 验证
  expiresAt:   ISODateString;
  riskScore:   number;            // 风险分 0.0–1.0（异常登录检测）
}

type MFADeviceType   = 'TOTP' | 'WebAuthn' | 'SMS' | 'Hardware';
type MFADeviceStatus = 'active' | 'revoked';

/**
 * 多因素认证设备（MFADevice）
 * 用户绑定的 MFA 设备记录，支持 TOTP（Authenticator App）、WebAuthn（生物识别/硬件密钥）、
 * SMS（短信验证码）、硬件令牌（YubiKey）等多种形式。
 */
interface MFADevice {
  id:         UUID;
  userId:     UUID;
  type:       MFADeviceType;
  status:     MFADeviceStatus;
  enrolledAt: ISODateString;
}

type InvitationStatus = 'pending' | 'accepted' | 'expired' | 'revoked';

/**
 * 邀请（Invitation）
 * 邀请他人加入 Tenant 或特定资源的记录，支持跨租户邀请（B2B 协作场景）。
 * 是 Enterprise 2.0 "打破部门墙、跨边界协作" 特征的数据载体。
 */
interface Invitation {
  id:            UUID;
  tenantId:      UUID;
  inviterUserId: UUID;
  email:         string;
  scope:         InvitationScope;
  expiresAt:     ISODateString;
  status:        InvitationStatus;
}

/**
 * 邀请范围（InvitationScope）
 * 嵌套在 Invitation 中，明确被邀请人接受邀请后进入的目标资源和初始角色。
 */
interface InvitationScope {
  resourceType: string;
  resourceId?:  UUID;
  role:         string;
}

// ────────────────────────────────────────────────
// Authorization Domain（授权域）
// ────────────────────────────────────────────────
type RoleScope = 'tenant' | 'org' | 'workspace' | 'project';

/**
 * 角色（Role）
 * RBAC（基于角色的访问控制）的角色定义，表示一组权限的集合。
 * tenantId 为 null 表示系统内置角色（如 super_admin）；tenantId 有值则为租户自定义角色。
 * scope 控制该角色可以在哪个资源粒度上被授予。
 */
interface Role {
  id:       UUID;
  tenantId: UUID | null;          // null = 系统内置角色
  key:      string;               // 标识键（如 "org_admin"）
  name:     string;
  scope:    RoleScope;
}

/**
 * 原子权限（Permission）
 * 权限系统的最小粒度单元，表达"对某类资源可以执行什么操作"。
 * Role 由若干 Permission 组成，Permission 本身不直接授予给用户。
 */
interface Permission {
  id:       UUID;
  resource: string;               // 资源类型（如 "project"）
  action:   string;               // 操作类型（如 "delete"）
}

/**
 * 角色绑定（RoleBinding）
 * RBAC 的授权关系，将 Role 授予某主体（User / Group / ServiceAccount）。
 * 可限定在特定资源上（resourceType + resourceId），实现细粒度的"在 ProjectA 上是 editor"。
 * resourceType / resourceId 为空时表示作用于全范围。
 */
interface RoleBinding {
  id:            UUID;
  roleId:        UUID;
  principalType: PrincipalType;
  principalId:   UUID;
  resourceType?: string;          // 限定的资源类型（空 = 全范围）
  resourceId?:   UUID;            // 限定的资源 ID（空 = 全范围）
}

type PolicyEffect = 'allow' | 'deny';

/**
 * ABAC 策略（Policy）
 * 基于属性的访问控制策略，用 Cedar / OPA 语法描述。
 * 解决 RBAC 无法动态处理的场景：如"只有与资源同部门的员工才能访问"、"只在工作时间允许导出"。
 */
interface Policy {
  id:         UUID;
  tenantId:   UUID;
  subject:    string;             // Cedar/OPA 主体条件表达式
  resource:   string;             // 资源条件表达式
  action:     string;
  condition?: string;             // 附加条件（如时间、IP 范围）
  effect:     PolicyEffect;
}

/**
 * ReBAC 关系元组（RelationTuple）
 * 基于关系的访问控制的核心数据结构，对应 Google Zanzibar 的 tuple 模型。
 * 表达"谁对什么有什么关系"（如 group:eng#member → project:alpha#editor）。
 * 生产环境中由 SpiceDB / OpenFGA 管理，此处为关系型数据库的备份/同步副本。
 */
interface RelationTuple {
  namespace:        string;       // 对象命名空间（如 "project"）
  objectId:         string;
  relation:         string;       // 关系（如 "editor"）
  subjectNamespace: string;       // 主体命名空间（如 "group"）
  subjectId:        string;
  subjectRelation?: string;       // 主体内部关系（如 "member"）
}

// ────────────────────────────────────────────────
// People Domain（人员域）
// ────────────────────────────────────────────────

/**
 * 员工档案（EmployeeProfile）
 * 员工的 HR 静态信息，关注"这个人是谁"（姓名、工号、入职日期等）。
 * 与 Identity（如何登录）解耦，遵循 Workday HCM 的分层设计标准。
 * 1:1 关联 User，但归属 HR 域而非 IAM 域，以便独立对接 HRIS 系统。
 */
interface EmployeeProfile {
  id:               UUID;
  userId:           UUID;
  tenantId:         UUID;
  employeeNumber:   string;       // 工号（如 "EMP-10042"）
  displayName:      string;
  pronouns?:        string;       // 代词偏好（如 "she/her"）
  bio?:             string;       // 个人简介（UGC）
  avatarUrl?:       string;
  hireDate:         ISODateString;
  terminationDate?: ISODateString; // 为 null 表示在职
  locale:           string;       // 如 "zh-CN"
  timezone:         string;       // 如 "Asia/Shanghai"
}

/**
 * 职能族（JobFamily）
 * 定义职位类别与级别序列，是 Workday / SAP SuccessFactors 的 HR 标准建模。
 * 如"工程"族包含 L1–L3、Staff、Principal 等级别，用于结构化职业发展路径。
 */
interface JobFamily {
  id:       UUID;
  tenantId: UUID;
  name:     string;               // 职能族名（如 "Engineering"）
  levels:   string[];             // 级别序列（如 ["L1","L2","L3","Staff","Principal"]）
}

/**
 * 职级（JobGrade）
 * 某职能族内某个具体级别的详细定义，关联薪酬范围（加密存储）和胜任力框架。
 * Position 通过 jobGradeId 关联到 JobGrade，从而确定岗位的薪酬范围和能力要求。
 */
interface JobGrade {
  id:                    UUID;
  jobFamilyId:           UUID;
  level:                 string;  // 级别（如 "L3"）
  salaryBand?:           SalaryBand;  // 加密存储
  competencyFrameworkId?: UUID;
}

/**
 * 薪酬范围（SalaryBand）
 * 嵌套在 JobGrade 中，定义该职级的薪酬区间，必须加密存储。
 */
interface SalaryBand {
  min:      number;
  max:      number;
  currency: string;               // 如 "CNY"、"USD"
}

type SkillProficiency = 'beginner' | 'intermediate' | 'expert';

/**
 * 技能标签（Skill）
 * 系统级技能标签库，是 Enterprise 2.0 知识图谱和 Endorsement（背书）的基础。
 * 由租户管理员预定义，员工通过 UserSkill 声明自己拥有哪些技能。
 */
interface Skill {
  id:       UUID;
  tenantId: UUID;
  name:     string;
  category: string;               // 如 "技术"、"管理"、"领域知识"
}

/**
 * 用户技能（UserSkill）
 * 员工声明自己拥有某项技能的记录，是 E2.0 技能图谱的核心节点。
 * endorsementsCount 由 Social Domain 的 Endorsement 事件累计驱动，体现社交信任传播。
 */
interface UserSkill {
  id:               UUID;
  userId:           UUID;
  skillId:          UUID;
  proficiency:      SkillProficiency;
  endorsementsCount: number;      // 被同事背书次数
}

// ────────────────────────────────────────────────
// Organization Domain（组织域）
// ────────────────────────────────────────────────
type OrgUnitType =
  | 'division'    // 事业部
  | 'department'  // 部门
  | 'team'        // 小组
  | 'tribe'       // 部落（Spotify 模型）
  | 'squad'       // 小队（Spotify 模型）
  | 'chapter'     // 章节（职能横切）
  | 'guild'       // 行会（社区）
  | 'legalEntity' // 法人实体
  | 'region';     // 地区

type OrgUnitStatus = 'active' | 'archived';

/**
 * 组织单元（OrganizationUnit）
 * 组织结构图中的节点，可以是任意类型的组织层级（部门、小队、法人实体等）。
 * 携带 effectiveAt / endAt 时间维度，支持历史时间点的组织结构回溯查询。
 * 节点之间的关系由 OrganizationRelation 表达，而非 parentId（避免树结构局限）。
 */
interface OrganizationUnit {
  id:          UUID;
  tenantId:    UUID;
  type:        OrgUnitType;
  name:        string;
  code:        string;            // 编码（如 "ENG-PLATFORM-001"）
  status:      OrgUnitStatus;
  effectiveAt: ISODateString;
  endAt?:      ISODateString;     // 为 null 表示当前有效
}

type OrgRelationType =
  | 'parent_of'        // 上下级
  | 'manages'          // 管理
  | 'collaborates_with'// 协作
  | 'funds'            // 资金支持
  | 'dotted_line_to'   // 虚线汇报
  | 'reports_to'       // 实线汇报
  | 'belongs_to';      // 归属

/**
 * 组织关系（OrganizationRelation）
 * OrganizationUnit 之间的有向关系边，用图结构（Graph）而非树结构（Tree）表达组织。
 * 这是矩阵式组织建模的核心——同一个 OU 可以同时是多个其他 OU 的子节点、协作方或资金来源。
 * 同样携带时间维度，记录关系的起止时间。
 */
interface OrganizationRelation {
  id:           UUID;
  fromOrgId:    UUID;
  toOrgId:      UUID;
  relationType: OrgRelationType;
  effectiveAt:  ISODateString;
  endAt?:       ISODateString;
}

type PositionStatus = 'open' | 'filled' | 'frozen';

/**
 * 岗位（Position）
 * 岗位的抽象定义，与具体人员无关，可以空缺（Headcount 未填满）。
 * 是矩阵组织 User ↔ Org 解耦的关键中间层：User 通过 Assignment 占用 Position，而非直接属于 Org。
 * 参考 SAP / Workday 的 Position Management 标准。
 */
interface Position {
  id:           UUID;
  orgId:        UUID;
  title:        string;           // 岗位名称（如 "Senior Engineering Manager"）
  jobGradeId?:  UUID;
  costCenterId?: UUID;
  headcount:    number;           // 核定人数
  status:       PositionStatus;
}

type AssignmentStatus = 'active' | 'on_leave' | 'terminated';

/**
 * 岗位分配（Assignment）
 * 用户在某个时间段占用某个岗位的记录，是矩阵组织工时分配的核心实体。
 * allocation 字段（0.0–1.0）表达工时拆分：allocation=0.5 意味着员工 50% 时间投入该岗位。
 * isPrimary 标记主岗位，决定员工的 HR 主汇报线（solid line）。
 */
interface Assignment {
  id:         UUID;
  tenantId:   UUID;
  userId:     UUID;
  positionId: UUID;
  allocation: number;             // 时间投入比例 0.0–1.0
  isPrimary:  boolean;            // 是否主岗位（决定 HR 主汇报线）
  startAt:    ISODateString;
  endAt?:     ISODateString;
  status:     AssignmentStatus;
}

type ReportingLineType = 'solid' | 'dotted' | 'functional' | 'project';

/**
 * 汇报线（ReportingLine）
 * 记录下属与上级之间的汇报关系，与 Assignment 关联（而非 User），支持矩阵组织的多汇报线。
 * solid（实线）= 行政上级；dotted（虚线）= 业务/职能上级；project = 临时项目汇报。
 * 这是矩阵组织与传统树形组织最核心的区别所在。
 */
interface ReportingLine {
  id:                       UUID;
  subordinateAssignmentId:  UUID;  // 下属的 Assignment ID
  managerAssignmentId:      UUID;  // 上级的 Assignment ID
  type:                     ReportingLineType;
}

/**
 * 成本中心（CostCenter）
 * 财务维度的组织单元，记录各 OrganizationUnit 的预算归属和记账货币。
 * Position 通过 costCenterId 关联成本中心，实现人力成本的精确核算。
 */
interface CostCenter {
  id:         UUID;
  tenantId:   UUID;
  code:       string;             // 财务编码（如 "CC-ENG-001"）
  ownerOrgId: UUID;
  currency:   string;             // 如 "CNY"、"USD"
}

type ContractType = 'contractor' | 'vendor' | 'intern';

/**
 * 外部用工（ExternalWorker）
 * 外包、派遣、实习生等非正式员工的合规记录，有独立的合同管理和访问权限生命周期。
 * accessExpiresAt 字段实现合同到期时系统访问权限自动失效，满足外部用工的合规要求。
 */
interface ExternalWorker {
  id:               UUID;
  tenantId:         UUID;
  userId:           UUID;
  agencyId?:        UUID;
  contractType:     ContractType;
  contractStartAt:  ISODateString;
  contractEndAt:    ISODateString;
  accessExpiresAt:  ISODateString; // 系统访问权限自动失效时间
}

type OrgChangeType = 'created' | 'restructured' | 'merged' | 'dissolved' | 'hired' | 'terminated';

/**
 * 组织变更记录（OrgChange）
 * 每次组织结构变动时生成的完整快照记录，实现"时间旅行"查询能力。
 * 通过 snapshot（JSONB）保存变更时刻的完整组织状态，可回答"2025 年 Q3 的组织结构是什么"。
 * 禁止直接修改历史记录，变动只能通过新增 OrgChange 来追加。
 */
interface OrgChange {
  id:          UUID;
  tenantId:    UUID;
  changeType:  OrgChangeType;
  effectiveAt: ISODateString;
  snapshot:    Record<string, unknown>;  // 该时刻组织快照（JSONB）
  requestedBy: UUID;
  approvalId?: UUID;
}

// ────────────────────────────────────────────────
// Collaboration Domain（协作域）
// ────────────────────────────────────────────────
type Visibility         = 'public' | 'private' | 'restricted';
type TeamSpaceLifecycle = 'draft' | 'active' | 'archived';
type ParticipationRole  = 'owner' | 'editor' | 'viewer' | 'commenter';
type SharedSpaceStatus  = 'pending' | 'active' | 'revoked';
type ActivityVerb       = 'created' | 'updated' | 'commented' | 'liked' | 'joined' | 'mentioned';

/**
 * 工作区（Workspace）
 * 逻辑协作空间，是 Project 的容器，对应 Notion Workspace 或 Slack Workspace 的概念。
 * 在 Tenant 内提供进一步的命名空间隔离，不同团队可以有独立的 Workspace。
 */
interface Workspace {
  id:         UUID;
  tenantId:   UUID;
  name:       string;
  visibility: Visibility;
}

/**
 * 项目（Project）
 * 核心协作单元，可跨组织、跨团队参与，是权限管理和协作的主要资源容器。
 * ownerOrgId 决定谁负责该项目的资源和决策；classificationId 关联数据分级，影响 DLP 策略。
 */
interface Project {
  id:               UUID;
  workspaceId:      UUID;
  ownerOrgId:       UUID;
  visibility:       Visibility;
  classificationId?: UUID;        // 关联 DataClassification
}

/**
 * 临时团队空间（TeamSpace）
 * 跨组织的临时团队协作容器，生命周期与 Project 绑定。
 * 用于项目内需要临时组建跨部门团队的场景，项目归档后 TeamSpace 随之归档。
 */
interface TeamSpace {
  id:        UUID;
  projectId: UUID;
  lifecycle: TeamSpaceLifecycle;
}

/**
 * 参与关系（Participation）
 * 记录某主体（User / Group / ServiceAccount）以何种角色参与某资源。
 * 是细粒度访问控制的入口：通过 Participation + RelationTuple 共同决定"谁能对什么做什么"。
 */
interface Participation {
  id:            UUID;
  principalType: PrincipalType;
  principalId:   UUID;
  resourceType:  string;
  resourceId:    UUID;
  role:          ParticipationRole;
  joinedAt:      ISODateString;
}

/**
 * 跨租户共享空间（SharedSpace）
 * 允许两个 Tenant 之间共享特定资源，类似 Slack Connect / Microsoft Teams 外部协作。
 * 是 Enterprise 2.0 "打破边界、跨组织协作" 特征在多租户架构中的实现。
 * hostTenantId 拥有资源，guestTenantId 被邀请访问。
 */
interface SharedSpace {
  id:            UUID;
  hostTenantId:  UUID;            // 资源所有租户
  guestTenantId: UUID;            // 被邀请租户
  resourceType:  string;
  resourceId:    UUID;
  status:        SharedSpaceStatus;
}

/**
 * 活动记录（Activity）
 * 活动流（Activity Stream）的单条记录，遵循 ActivityStreams 2.0 标准。
 * 记录"谁对什么做了什么"，是 Enterprise 2.0 知识流转时间轴的核心，也是个性化推送的数据源。
 */
interface Activity {
  id:                UUID;
  actorId:           UUID;
  verb:              ActivityVerb;
  objectType:        string;
  objectId:          UUID;
  target?:           string;      // 上下文描述（如 "在 Project Alpha 中"）
  contextResourceId?: UUID;
  timestamp:         ISODateString;
}

/**
 * 知识条目（Knowledge）
 * 用户生成内容（UGC）形式的 Wiki 文档，是 Enterprise 2.0 "Authoring 人人可创作" 特征的数据载体。
 * version 字段支持版本历史；classificationId 决定谁有权查看。
 */
interface Knowledge {
  id:               UUID;
  workspaceId:      UUID;
  title:            string;
  content:          string;       // Markdown 或富文本
  version:          number;       // 每次修改递增
  classificationId?: UUID;
}

/**
 * 标签（Tag）
 * Folksonomy（民间分类法）标签，由用户自创而非 IT 预定义分类体系。
 * 是 Enterprise 2.0 "Tags 自创分类" 特征的核心实体，体现知识的自组织涌现。
 */
interface Tag {
  id:        UUID;
  tenantId:  UUID;
  name:      string;
  createdBy: UUID;
}

/**
 * 标签关联（Tagging）
 * 将 Tag 附加到任意资源（Project / Knowledge / Activity 等）上的关联记录。
 * 通过 resourceType + resourceId 的多态关联，实现跨域的 folksonomy 分类体系。
 */
interface Tagging {
  id:           UUID;
  tagId:        UUID;
  resourceType: string;
  resourceId:   UUID;
  taggedBy:     UUID;
}

// ────────────────────────────────────────────────
// Social Domain（社交域）
// ────────────────────────────────────────────────

/**
 * 关注关系（Follow）
 * 用户关注其他用户、组织、标签或项目的记录，构建企业内部的社交图谱。
 * 是 Activity Stream 个性化推送的信号来源：只推送你关注的人/项目的动态。
 */
interface Follow {
  id:             UUID;
  followerUserId: UUID;
  followeeType:   'user' | 'org' | 'tag' | 'project';
  followeeId:     UUID;
}

/**
 * @提及（Mention）
 * 记录某内容中 @了哪个用户，触发被提及人的即时通知，并在内容间建立显式的人际连接。
 * 是 Enterprise 2.0 协作感知（谁在关注我的工作）的基础信号。
 */
interface Mention {
  id:               UUID;
  sourceType:       string;       // 来源类型（如 "comment"）
  sourceId:         UUID;
  mentionedUserId:  UUID;
}

/**
 * 技能背书（Endorsement）
 * 员工为同事的 UserSkill 做背书的记录，是 Enterprise 2.0 社交信任传播机制。
 * 每次背书会累加 UserSkill.endorsementsCount，形成可信赖的技能声誉系统（类似 LinkedIn）。
 */
interface Endorsement {
  id:              UUID;
  endorserUserId:  UUID;
  userSkillId:     UUID;          // 被背书的 UserSkill
}

/**
 * 表情回应（Reaction）
 * 对内容的轻量级情感反馈（点赞、庆祝等），提供低成本的内容互动机制。
 * 是 E2.0 Extensions（推荐与扩展）特征的体现，用于驱动 Activity Stream 的相关性排序。
 */
interface Reaction {
  id:           UUID;
  resourceType: string;
  resourceId:   UUID;
  userId:       UUID;
  type:         'like' | 'celebrate' | 'insightful' | 'curious';
}

// ────────────────────────────────────────────────
// Governance Domain（治理域）
// ────────────────────────────────────────────────
type AuditActorType  = 'user' | 'service_account' | 'agent';
type WorkflowState   = 'pending' | 'approved' | 'rejected' | 'expired';
type ApprovalDecision = 'approved' | 'rejected' | 'delegated';
type RetentionAction = 'archive' | 'delete' | 'anonymize';
type LegalHoldStatus = 'active' | 'released';
type ClassificationLevel = 'public' | 'internal' | 'confidential' | 'restricted';
type ComplianceStatus = 'compliant' | 'in_progress' | 'non_compliant';

/**
 * 审计日志（AuditLog）
 * 不可篡改的操作记录，是 Enterprise 合规、法务取证、安全审计的根基。
 * 所有 Principal（User / ServiceAccount / Agent）的高风险操作都必须写入 AuditLog。
 * before / after 字段保存操作前后的状态快照，支持精确的变更追溯。
 * 注意：生产环境中应通过 DB RULE 禁止 UPDATE / DELETE（参见 SQL DDL 章节）。
 */
interface AuditLog {
  id:           UUID;
  tenantId:     UUID;
  actorType:    AuditActorType;
  actorId:      UUID;
  action:       string;           // 如 "role.assigned"、"document.exported"
  resourceType: string;
  resourceId:   UUID;
  before?:      Record<string, unknown>;  // 操作前快照
  after?:       Record<string, unknown>;  // 操作后快照
  ip?:          string;
  userAgent?:   string;
  timestamp:    ISODateString;    // 不可修改
}

/**
 * 审批流程（ApprovalWorkflow）
 * 高风险操作（组织重组、权限升级、离职交接）的多级审批容器，支持 SLA 超时控制。
 * approvers 定义每步需要谁审批；currentStep 跟踪当前进行到第几步。
 */
interface ApprovalWorkflow {
  id:          UUID;
  tenantId:    UUID;
  type:        string;            // 如 "org_restructure"、"role_escalation"
  initiator:   UUID;
  approvers:   ApproverPolicy[];
  currentStep: number;
  state:       WorkflowState;
  slaDueAt?:   ISODateString;
}

/**
 * 审批人策略（ApproverPolicy）
 * 嵌套在 ApprovalWorkflow 中，定义某个审批步骤需要哪个角色/组/具体用户审批，以及是否必须通过。
 */
interface ApproverPolicy {
  role?:     string;
  groupId?:  UUID;
  userId?:   UUID;
  required:  boolean;
}

/**
 * 审批步骤记录（ApprovalStep）
 * ApprovalWorkflow 中每个步骤的独立记录，保存该步骤的决定和时间戳。
 * 支持审批历史的完整追溯，满足合规审计对决策链路的要求。
 */
interface ApprovalStep {
  id:             UUID;
  workflowId:     UUID;
  stepIndex:      number;
  approverPolicy: ApproverPolicy;
  decision?:      ApprovalDecision;
  decidedAt?:     ISODateString;
}

/**
 * 权限委派（Delegation）
 * 允许用户 A 在特定时间段内将部分权限委派给用户 B 代为行使（如出差、休假场景）。
 * endAt 时间到期后自动失效，无需人工撤回；scope 精确限定委派范围，避免过度授权。
 */
interface Delegation {
  id:           UUID;
  delegatorId:  UUID;
  delegateeId:  UUID;
  scope:        DelegationScope;
  startAt:      ISODateString;
  endAt:        ISODateString;    // 到期自动失效
}

/**
 * 委派范围（DelegationScope）
 * 嵌套在 Delegation 中，精确定义本次委派涉及的资源类型、资源 ID 和角色列表。
 */
interface DelegationScope {
  resourceType?: string;
  resourceId?:   UUID;
  roles:         string[];
}

/**
 * 数据保留策略（DataRetentionPolicy）
 * 定义各类数据的生命周期和到期处理方式，满足 GDPR / HIPAA 等合规法规的数据最小化原则。
 * LegalHold 处于 active 状态时，相关数据的 RetentionPolicy 自动暂停执行。
 */
interface DataRetentionPolicy {
  id:           UUID;
  tenantId:     UUID;
  resourceType: string;
  retentionDays: number;
  action:       RetentionAction;
}

/**
 * 法务保全（LegalHold）
 * 在诉讼调查期间冻结特定数据，防止被删除或修改，优先级临时高于 DataRetentionPolicy。
 * custodians 列出数据保管人（其所有相关数据都需要保留）；releaseAt 记录解除时间。
 */
interface LegalHold {
  id:         UUID;
  tenantId:   UUID;
  name:       string;
  custodians: UUID[];             // 数据保管人列表
  scope:      Record<string, unknown>;
  issuedBy:   UUID;
  issuedAt:   ISODateString;
  status:     LegalHoldStatus;
  releaseAt?: ISODateString;
}

/**
 * 数据分级（DataClassification）
 * 为资源（Project / Document / Knowledge 等）打上敏感度标签，是 DLP（数据防泄漏）策略的基础。
 * handlingPolicy 定义该分级下的具体处理规范（是否可导出、是否需审批、是否加水印）。
 */
interface DataClassification {
  id:              UUID;
  tenantId:        UUID;
  level:           ClassificationLevel;
  label:           string;
  handlingPolicy:  HandlingPolicy;
}

/**
 * 数据处理规范（HandlingPolicy）
 * 嵌套在 DataClassification 中，定义该分级数据的具体操作限制。
 */
interface HandlingPolicy {
  canExport:        boolean;
  requiresApproval: boolean;
  watermark:        boolean;
  allowedRegions?:  string[];     // 限定可存储的 Region
}

/**
 * 合规框架（ComplianceFramework）
 * 记录租户所遵循的合规标准（SOC 2 / GDPR / HIPAA / ISO 27001）及其控制项的当前状态。
 * 用于向企业客户展示合规进度，也是销售 Enterprise 版本时的重要凭证。
 */
interface ComplianceFramework {
  id:           UUID;
  tenantId:     UUID;
  standard:     'SOC2' | 'GDPR' | 'HIPAA' | 'ISO27001';
  controls:     Record<string, unknown>;  // 控制项清单
  lastAuditAt?: ISODateString;
  status:       ComplianceStatus;
}

// ────────────────────────────────────────────────
// Integration Domain（集成域）
// ────────────────────────────────────────────────

/**
 * Webhook（事件推送钩子）
 * 将系统内部事件实时推送到外部系统（如 Jira、飞书、Zapier）的出站集成机制。
 * secret 用于生成 HMAC-SHA256 签名，接收端可验证消息来源合法性，防止伪造请求。
 */
interface Webhook {
  id:          UUID;
  tenantId:    UUID;
  url:         string;
  events:      string[];          // 如 ["user.created","org.restructured"]
  secret:      string;            // HMAC-SHA256 签名密钥
  status:      'active' | 'disabled';
  retryPolicy: RetryPolicy;
}

/**
 * Webhook 重试策略（RetryPolicy）
 * 嵌套在 Webhook 中，定义推送失败时的重试行为，防止因网络抖动丢失事件。
 */
interface RetryPolicy {
  maxAttempts: number;            // 最大重试次数
  backoff:     'linear' | 'exponential';
}

type DeliveryStatus = 'pending' | 'delivered' | 'failed';

/**
 * 事件推送记录（EventLog）
 * 基于 Outbox 模式（事务发件箱）保证至少一次投递的推送记录。
 * 记录每次推送的状态和重试计划，支持失败重推和推送审计，是集成可靠性的基础。
 */
interface EventLog {
  id:             UUID;
  webhookId:      UUID;
  eventType:      string;
  payload:        Record<string, unknown>;
  deliveryStatus: DeliveryStatus;
  attempts:       number;
  nextRetryAt?:   ISODateString;
}

type SCIMSyncStatus      = 'synced' | 'pending' | 'conflict';
type ConflictResolution  = 'system_wins' | 'scim_wins';

/**
 * SCIM 同步记录（SCIMSync）
 * 跟踪从 Okta / Azure Entra ID 等 IdP 通过 SCIM 2.0 协议同步的 User / Group 状态。
 * conflictResolution 定义当 IdP 数据与本系统数据冲突时以哪一方为准，
 * 是自动化用户生命周期管理（入职/离职自动开通/吊销权限）的基础。
 */
interface SCIMSync {
  id:                   UUID;
  tenantId:             UUID;
  connectorId:          UUID;
  resourceType:         'User' | 'Group';
  externalId:           string;   // IdP 侧 ID
  lastSyncAt?:          ISODateString;
  syncStatus:           SCIMSyncStatus;
  conflictResolution:   ConflictResolution;
}

// ────────────────────────────────────────────────
// Notification Domain（通知域）
// ────────────────────────────────────────────────
type NotificationChannelType = 'email' | 'slack' | 'webhook' | 'in_app' | 'dingtalk' | 'wecom';
type NotificationFrequency   = 'realtime' | 'digest' | 'off';

/**
 * 通知通道（NotificationChannel）
 * 用户配置的通知接收渠道，支持邮件、Slack、钉钉、企业微信、站内信等。
 * 每个用户可以配置多个通道，不同事件类型可以路由到不同通道（由 NotificationPreference 控制）。
 */
interface NotificationChannel {
  id:       UUID;
  tenantId: UUID;
  userId:   UUID;
  type:     NotificationChannelType;
  config:   Record<string, unknown>;  // 如 {email: "alice@acme.com"}
  enabled:  boolean;
}

/**
 * 通知偏好（NotificationPreference）
 * 用户对特定事件类型的通知偏好配置：通过哪个渠道、以什么频率（实时/摘要/关闭）接收。
 * 解耦事件触发（由业务域负责）与通知路由（由 Notification Domain 负责）。
 */
interface NotificationPreference {
  id:        UUID;
  userId:    UUID;
  eventType: string;              // 如 "mention"、"approval_required"
  channelId: UUID;
  frequency: NotificationFrequency;
}

/**
 * 通知模板（NotificationTemplate）
 * 各事件类型的消息模板，支持多语言（locale），解耦消息格式与事件逻辑。
 * tenantId 为 null 时为系统默认模板；租户可以自定义模板覆盖默认值。
 * subject / body 支持 Mustache 风格的模板变量（如 {{actor}}、{{project}}）。
 */
interface NotificationTemplate {
  id:       UUID;
  tenantId: UUID | null;          // null = 系统默认模板
  eventType: string;
  locale:   string;               // 如 "zh-CN"
  subject:  string;               // 支持模板变量（如 "{{actor}} 邀请您加入 {{project}}"）
  body:     string;               // HTML + 纯文本双版本
}

// ────────────────────────────────────────────────
// AI / Agent Domain（AI 与智能体域）
// ────────────────────────────────────────────────
type AgentStatus    = 'active' | 'suspended' | 'deprecated';
type AgentActionType = 'tool_call' | 'knowledge_query' | 'api_call';

/**
 * AI 智能体（Agent）
 * 代表一个由 LLM 驱动、可自主执行任务的智能体实体。
 * 必须有责任人（ownerId），以便在 Agent 行为异常时快速定位人工负责人。
 * 每个 Agent 都会关联一个 AgentIdentity，使其能够作为 Principal 参与权限系统。
 */
interface Agent {
  id:       UUID;
  tenantId: UUID;
  name:     string;
  ownerId:  UUID;                 // 责任人 User ID
  modelRef: string;               // 使用的 LLM（如 "claude-opus-4-7"）
  status:   AgentStatus;
}

/**
 * 智能体身份（AgentIdentity）
 * Agent 在授权系统中的 Principal 身份记录，使 Agent 能够被 RoleBinding 和 RelationTuple 引用。
 * 这是"Agent-as-Principal"设计的关键——Agent 必须像 User / ServiceAccount 一样被授权和审计。
 */
interface AgentIdentity {
  id:          UUID;
  agentId:     UUID;
  principalId: UUID;              // 在授权域的 Principal ID
}

/**
 * 工具技能（ToolSkill）
 * Agent 可以调用的工具/函数的定义，用 JSON Schema 描述入参结构。
 * 是 Agent 能力边界的显式声明，防止 Agent 调用未授权的工具。
 * 命名为 ToolSkill 以区别 People Domain 中的人类 Skill。
 */
interface ToolSkill {
  id:       UUID;
  agentId:  UUID;
  toolKey:  string;               // 工具标识（如 "search_documents"）
  schema:   Record<string, unknown>;  // JSON Schema / OpenAPI 格式
}

/**
 * 知识库（KnowledgeBase）
 * Agent 的 RAG（检索增强生成）知识源，存储结构化和非结构化的参考文档。
 * classificationId 关联数据分级，控制哪些数据可以被哪些 Agent 检索，防止敏感信息泄漏给 LLM。
 */
interface KnowledgeBase {
  id:               UUID;
  tenantId:         UUID;
  name:             string;
  indexBackend:     string;       // 如 "pgvector"、"OpenSearch"
  classificationId?: UUID;
}

/**
 * 上下文策略（ContextPolicy）
 * 定义 Agent 在执行任务时可以感知哪些上下文信息，是防止敏感数据泄漏给 LLM 的护栏。
 * redactionRules 对传入 LLM 的数据进行脱敏处理（遮码/删除/哈希）。
 */
interface ContextPolicy {
  id:             UUID;
  agentId:        UUID;
  scope:          Record<string, unknown>;   // 允许访问的上下文范围
  redactionRules: RedactionRule[];
}

/**
 * 脱敏规则（RedactionRule）
 * 嵌套在 ContextPolicy 中，定义哪些字段在传给 LLM 之前需要做脱敏处理。
 */
interface RedactionRule {
  fields: string[];               // 需脱敏的字段名
  method: 'mask' | 'remove' | 'hash';
}

/**
 * 智能体会话（AgentSession）
 * Agent 执行一次完整任务的会话容器，携带分布式追踪 ID，关联该会话内所有 AgentAction。
 * initiatorPrincipalId 记录是谁触发了这次 Agent 执行，用于责任归属。
 */
interface AgentSession {
  id:                   UUID;
  agentId:              UUID;
  initiatorPrincipalId: UUID;
  startedAt:            ISODateString;
  endedAt?:             ISODateString;
  traceId:              string;   // 分布式追踪 ID
}

/**
 * 智能体操作记录（AgentAction）
 * Agent 在会话中执行的每个具体操作的日志，是 Agent 行为可追溯的最小单元。
 * 所有 AgentAction 都必须写入 AuditLog（带 traceId 关联），使 Agent 的每步行为都可审计。
 */
interface AgentAction {
  id:             UUID;
  agentSessionId: UUID;
  actionType:     AgentActionType;
  resourceRef?:   string;         // 如 "project:alpha"
  result:         Record<string, unknown>;
}
```

---

## 十三、SQL DDL（PostgreSQL）

> 以下 DDL 采用 PostgreSQL 语法。所有主键使用 UUID，时间字段使用 `TIMESTAMPTZ`，灵活结构字段使用 `JSONB`。`tenant_id` 列统一加 RLS（行级安全）策略防止跨租户数据泄漏。

### 准备工作

```sql
-- 启用 UUID 生成扩展
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- 所有表共用的 updated_at 自动维护触发器
CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

---

### Platform Domain（平台域）

```sql
-- ─────────────────────────────────────────────────────────────
-- 表：regions（区域）
-- 作用：记录云服务商和地理区域，是 Data Residency（数据主权）的基础配置。
--       每个 Tenant 关联一个 Region，决定其数据存储在哪个地理位置、需要满足哪套合规标准。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE regions (
  id              UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  code            VARCHAR(50) UNIQUE NOT NULL,                  -- 如 'eu-west-1'
  provider        VARCHAR(50) NOT NULL,                         -- AWS | Azure | GCP | Aliyun | on_premise
  compliance_zone VARCHAR(50) NOT NULL DEFAULT 'none',          -- GDPR | HIPAA | SOC2 | CN | none
  created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ─────────────────────────────────────────────────────────────
-- 表：tenants（租户）
-- 作用：SaaS 系统的顶层隔离单元，代表一个订阅客户（公司/组织）。
--       同时承担三个边界：身份边界、计费边界、数据隔离边界。
-- 注意：Tenant ≠ Organization；slug 一经创建不可修改（用于子域名路由）。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE tenants (
  id           UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  slug         VARCHAR(100) UNIQUE NOT NULL,                    -- URL 友好短名，不可修改
  display_name VARCHAR(255) NOT NULL,
  plan         VARCHAR(50)  NOT NULL DEFAULT 'starter'
               CHECK (plan IN ('starter','growth','enterprise','custom')),
  region_id    UUID         NOT NULL REFERENCES regions(id),
  status       VARCHAR(50)  NOT NULL DEFAULT 'active'
               CHECK (status IN ('active','suspended','terminated')),
  settings     JSONB        NOT NULL DEFAULT '{}',
  created_at   TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
  updated_at   TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_tenants_slug   ON tenants(slug);
CREATE INDEX idx_tenants_status ON tenants(status);
CREATE TRIGGER trg_tenants_updated_at
  BEFORE UPDATE ON tenants
  FOR EACH ROW EXECUTE FUNCTION set_updated_at();

-- ─────────────────────────────────────────────────────────────
-- 表：subscriptions（订阅）
-- 作用：记录租户的服务订阅状态，是计费与配额管控的核心表。
--       每个 Tenant 对应一条订阅记录，决定其可使用的功能范围、用量上限和付款状态。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE subscriptions (
  id             UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id      UUID        NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  plan_id        UUID        NOT NULL,
  quota          JSONB       NOT NULL DEFAULT '{}',
  billing_cycle  VARCHAR(20) NOT NULL CHECK (billing_cycle IN ('monthly','annual')),
  payment_status VARCHAR(20) NOT NULL DEFAULT 'current'
                 CHECK (payment_status IN ('current','past_due','canceled')),
  created_at     TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at     TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE UNIQUE INDEX idx_subscriptions_tenant ON subscriptions(tenant_id);  -- 一租户一订阅

-- ─────────────────────────────────────────────────────────────
-- 表：feature_flags（特性开关）
-- 作用：控制哪些功能对哪些租户可见，支持灰度发布和 A/B 测试。
--       tenant_id 为 NULL 时表示全局默认，按租户设置的记录优先级更高。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE feature_flags (
  id            UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id     UUID        REFERENCES tenants(id) ON DELETE CASCADE,  -- NULL = 全局默认
  key           VARCHAR(200) NOT NULL,
  enabled       BOOLEAN     NOT NULL DEFAULT FALSE,
  rollout_policy JSONB       NOT NULL DEFAULT '{}',
  variants      JSONB        NOT NULL DEFAULT '{}',
  created_at    TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE UNIQUE INDEX idx_feature_flags_tenant_key ON feature_flags(COALESCE(tenant_id, '00000000-0000-0000-0000-000000000000'), key);

-- ─────────────────────────────────────────────────────────────
-- 表：encryption_keys（加密密钥，BYOK）
-- 作用：支持客户自带密钥（Bring Your Own Key）场景，存储 KMS 密钥引用。
--       仅存储 KMS 中的密钥 ARN（资源标识符），不存储明文密钥；
--       轮换策略由 rotation_policy 字段驱动，满足企业合规要求。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE encryption_keys (
  id              UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id       UUID        NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  key_alias       VARCHAR(200) NOT NULL,
  kms_provider    VARCHAR(100) NOT NULL,
  kms_key_arn     TEXT         NOT NULL,                        -- 加密存储
  rotation_policy JSONB        NOT NULL DEFAULT '{}',
  status          VARCHAR(30)  NOT NULL DEFAULT 'active'
                  CHECK (status IN ('active','pending_rotation','disabled')),
  created_at      TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE UNIQUE INDEX idx_encryption_keys_tenant_alias ON encryption_keys(tenant_id, key_alias);
```

---

### Identity & Access Domain（IAM 域）

```sql
-- ─────────────────────────────────────────────────────────────
-- 表：users（用户，平台账号）
-- 作用：SaaS 平台的全局身份记录，代表一个真实的人（或机器代理人）。
--       注意：User 是平台概念，≠ 员工（Employee）；
--       员工信息在 Organization Domain，User 通过 Membership 加入 Tenant。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE users (
  id            UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  primary_email VARCHAR(320) UNIQUE NOT NULL,
  phone         VARCHAR(30),
  status        VARCHAR(30)  NOT NULL DEFAULT 'pending_verification'
                CHECK (status IN ('active','suspended','deleted','pending_verification')),
  created_at    TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
  updated_at    TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_users_email  ON users(primary_email);
CREATE INDEX idx_users_status ON users(status);

-- ─────────────────────────────────────────────────────────────
-- 表：identities（登录凭据）
-- 作用：一个 User 可拥有多种登录方式（SAML SSO、OIDC、密码、Passkey、第三方社交登录）。
--       每条记录绑定一个 IdP（身份提供商）及其颁发的外部 ID，支持 JIT 自动开通。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE identities (
  id          UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id     UUID        NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  provider    VARCHAR(30)  NOT NULL
              CHECK (provider IN ('saml','oidc','password','passkey','social')),
  external_id VARCHAR(500) NOT NULL,                            -- IdP 侧 ID
  credentials JSONB        NOT NULL DEFAULT '{}',               -- 加密存储
  last_login_at TIMESTAMPTZ,
  created_at  TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE UNIQUE INDEX idx_identities_provider_external ON identities(provider, external_id);
CREATE INDEX idx_identities_user ON identities(user_id);

-- ─────────────────────────────────────────────────────────────
-- 表：groups（用户组）
-- 作用：Enterprise IAM 的批量授权单元，可一次性为整组用户分配权限，避免逐人操作。
--       支持三种类型：静态组（手动管理成员）、动态组（按规则自动计算）、同步组（SCIM 2.0 从外部 IdP 导入）。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE groups (
  id               UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id        UUID        NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  name             VARCHAR(255) NOT NULL,
  type             VARCHAR(20)  NOT NULL DEFAULT 'static'
                   CHECK (type IN ('static','dynamic','synced')),
  membership_rule  TEXT,                                        -- 仅 dynamic 类型
  created_at       TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
  updated_at       TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_groups_tenant ON groups(tenant_id);
ALTER TABLE groups ENABLE ROW LEVEL SECURITY;
CREATE POLICY groups_tenant_isolation ON groups
  USING (tenant_id = current_setting('app.current_tenant_id')::uuid);

-- ─────────────────────────────────────────────────────────────
-- 表：group_members（组成员）
-- 作用：记录 Group 的成员关系，支持用户、子组、服务账号和 AI Agent 四种主体类型。
--       通过 principal_type + principal_id 的多态引用设计，保持模型的统一性。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE group_members (
  id             UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  group_id       UUID        NOT NULL REFERENCES groups(id) ON DELETE CASCADE,
  principal_type VARCHAR(30)  NOT NULL CHECK (principal_type IN ('user','group','serviceAccount','agent')),
  principal_id   UUID         NOT NULL,
  created_at     TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE UNIQUE INDEX idx_group_members_unique ON group_members(group_id, principal_type, principal_id);
CREATE INDEX idx_group_members_principal ON group_members(principal_type, principal_id);

-- ─────────────────────────────────────────────────────────────
-- 表：memberships（成员关系，User ↔ Tenant）
-- 作用：将全局 User 和具体 Tenant 绑定，记录加入时间、身份类型和当前状态。
--       一个 User 可同时属于多个 Tenant（如顾问、外包同时服务多家公司）；
--       type 区分正式员工、外包、合作伙伴、访客，影响权限范围。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE memberships (
  id          UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id   UUID        NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  user_id     UUID        NOT NULL REFERENCES users(id),
  type        VARCHAR(30)  NOT NULL DEFAULT 'employee'
              CHECK (type IN ('employee','contractor','partner','guest')),
  joined_at   TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
  status      VARCHAR(30)  NOT NULL DEFAULT 'active'
              CHECK (status IN ('active','suspended','offboarded')),
  updated_at  TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE UNIQUE INDEX idx_memberships_tenant_user ON memberships(tenant_id, user_id);
CREATE INDEX idx_memberships_user   ON memberships(user_id);
CREATE INDEX idx_memberships_tenant ON memberships(tenant_id);
ALTER TABLE memberships ENABLE ROW LEVEL SECURITY;
CREATE POLICY memberships_tenant_isolation ON memberships
  USING (tenant_id = current_setting('app.current_tenant_id')::uuid);

-- ─────────────────────────────────────────────────────────────
-- 表：service_accounts（服务账号，机器身份）
-- 作用：为 CI/CD 流水线、API 集成、自动化脚本等非人类主体提供有主的机器身份。
--       每个服务账号必须有责任人（owner_id），支持密钥轮换策略；
--       在权限系统中与 User 平等，可被授予 Role、加入 Group。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE service_accounts (
  id              UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id       UUID        NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  name            VARCHAR(200) NOT NULL,
  type            VARCHAR(30)  NOT NULL CHECK (type IN ('integration','automation','agent')),
  owner_id        UUID         NOT NULL REFERENCES users(id),
  rotation_policy JSONB        NOT NULL DEFAULT '{"rotate_every_days": 90}',
  created_at      TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE UNIQUE INDEX idx_service_accounts_tenant_name ON service_accounts(tenant_id, name);
ALTER TABLE service_accounts ENABLE ROW LEVEL SECURITY;
CREATE POLICY sa_tenant_isolation ON service_accounts
  USING (tenant_id = current_setting('app.current_tenant_id')::uuid);

-- ─────────────────────────────────────────────────────────────
-- 表：api_keys（API 密钥）
-- 作用：服务账号的访问凭证，用于机器间的 API 调用鉴权。
--       仅存储密钥哈希（key_hash），明文只在创建时返回一次；
--       scopes 限制该密钥可调用的 API 范围，expires_at 强制过期。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE api_keys (
  id                  UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  service_account_id  UUID        NOT NULL REFERENCES service_accounts(id) ON DELETE CASCADE,
  key_hash            VARCHAR(200) UNIQUE NOT NULL,             -- 仅存哈希
  scopes              TEXT[]       NOT NULL DEFAULT '{}',
  expires_at          TIMESTAMPTZ  NOT NULL,
  last_used_at        TIMESTAMPTZ,
  created_at          TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_api_keys_sa ON api_keys(service_account_id);

-- ─────────────────────────────────────────────────────────────
-- 表：sessions（登录会话）
-- 作用：记录用户的活跃登录会话，支持强制登出、异常检测和风险评分。
--       mfa_verified 标记该会话是否已完成多因素认证；
--       risk_score 由风险引擎实时更新，可触发自动锁定或降权。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE sessions (
  id           UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id      UUID        NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  tenant_id    UUID        NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  device_id    VARCHAR(200),
  ip           INET,
  mfa_verified BOOLEAN     NOT NULL DEFAULT FALSE,
  expires_at   TIMESTAMPTZ  NOT NULL,
  risk_score   NUMERIC(3,2) NOT NULL DEFAULT 0.0 CHECK (risk_score BETWEEN 0 AND 1),
  created_at   TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_sessions_user_tenant ON sessions(user_id, tenant_id);
CREATE INDEX idx_sessions_expires     ON sessions(expires_at);  -- 定期清理过期会话

-- ─────────────────────────────────────────────────────────────
-- 表：mfa_devices（MFA 设备）
-- 作用：记录用户注册的多因素认证设备，一个用户可注册多台设备。
--       支持 TOTP（如 Google Authenticator）、WebAuthn（生物识别/硬件密钥）、
--       SMS（短信）、Hardware（硬件令牌）四种类型。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE mfa_devices (
  id          UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id     UUID        NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  type        VARCHAR(20)  NOT NULL CHECK (type IN ('TOTP','WebAuthn','SMS','Hardware')),
  status      VARCHAR(20)  NOT NULL DEFAULT 'active' CHECK (status IN ('active','revoked')),
  enrolled_at TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_mfa_devices_user ON mfa_devices(user_id);
```

---

### Authorization Domain（授权域）

```sql
-- ─────────────────────────────────────────────────────────────
-- 表：roles（角色，RBAC）
-- 作用：RBAC（基于角色的访问控制）中的角色定义，是权限的命名集合。
--       tenant_id 为 NULL 时为系统内置角色（如 super_admin）；
--       scope 限定角色生效的资源粒度（租户级 / 组织级 / 项目级）。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE roles (
  id        UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id UUID        REFERENCES tenants(id) ON DELETE CASCADE,  -- NULL = 系统内置
  key       VARCHAR(100) NOT NULL,
  name      VARCHAR(200) NOT NULL,
  scope     VARCHAR(30)  NOT NULL CHECK (scope IN ('tenant','org','workspace','project')),
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE UNIQUE INDEX idx_roles_tenant_key ON roles(COALESCE(tenant_id,'00000000-0000-0000-0000-000000000000'), key);

-- ─────────────────────────────────────────────────────────────
-- 表：permissions（原子权限）
-- 作用：系统中所有可授权操作的原子定义，如 project:delete、user:suspend。
--       通常在系统启动时由代码静态注册，不由用户创建；
--       Role 通过多对多关联表引用这些原子权限。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE permissions (
  id       UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  resource VARCHAR(100) NOT NULL,   -- 如 'project'
  action   VARCHAR(100) NOT NULL,   -- 如 'delete'
  UNIQUE(resource, action)
);

-- ─────────────────────────────────────────────────────────────
-- 表：role_bindings（角色绑定，RBAC 授权关系）
-- 作用：将 Role 赋予特定主体（用户/组/服务账号/Agent）在特定资源上的具体授权记录。
--       resource_type + resource_id 为 NULL 时代表全范围授权；
--       这是现代 SaaS 的标准做法，取代了简单的 user.role = admin 字段。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE role_bindings (
  id             UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  role_id        UUID        NOT NULL REFERENCES roles(id) ON DELETE CASCADE,
  principal_type VARCHAR(30)  NOT NULL CHECK (principal_type IN ('user','group','serviceAccount','agent')),
  principal_id   UUID         NOT NULL,
  resource_type  VARCHAR(100),                                  -- NULL = 全范围
  resource_id    UUID,                                          -- NULL = 全范围
  created_at     TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_rb_principal ON role_bindings(principal_type, principal_id);
CREATE INDEX idx_rb_resource  ON role_bindings(resource_type, resource_id) WHERE resource_type IS NOT NULL;

-- ─────────────────────────────────────────────────────────────
-- 表：policies（ABAC 策略）
-- 作用：实现基于属性的访问控制（ABAC），通过 condition 表达式动态判定权限。
--       例如：允许当 user.department == resource.owner_department 时访问；
--       可与 Cedar（AWS）或 OPA（开放策略引擎）等外部引擎集成评估。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE policies (
  id         UUID  PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id  UUID  NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  subject    TEXT  NOT NULL,
  resource   TEXT  NOT NULL,
  action     TEXT  NOT NULL,
  condition  TEXT,
  effect     VARCHAR(10) NOT NULL CHECK (effect IN ('allow','deny')),
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_policies_tenant ON policies(tenant_id);
ALTER TABLE policies ENABLE ROW LEVEL SECURITY;
CREATE POLICY policies_tenant_isolation ON policies
  USING (tenant_id = current_setting('app.current_tenant_id')::uuid);

-- ─────────────────────────────────────────────────────────────
-- 表：relation_tuples（ReBAC 关系元组）
-- 作用：Google Zanzibar 风格的关系型权限记录，是 ReBAC 模型的数据底座。
--       每条记录代表一个 <object>#<relation>@<subject> 元组，如 project:alpha#editor@user:alice；
--       生产环境的权限主存放在 SpiceDB / OpenFGA，此表作为轻量备份或迁移过渡。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE relation_tuples (
  id                UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  namespace         VARCHAR(100) NOT NULL,        -- 如 'project'
  object_id         VARCHAR(500) NOT NULL,
  relation          VARCHAR(100) NOT NULL,
  subject_namespace VARCHAR(100) NOT NULL,
  subject_id        VARCHAR(500) NOT NULL,
  subject_relation  VARCHAR(100),                 -- 如 'member'（组内成员间接引用）
  created_at        TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE UNIQUE INDEX idx_rt_unique ON relation_tuples(namespace, object_id, relation, subject_namespace, subject_id, COALESCE(subject_relation,''));
CREATE INDEX idx_rt_lookup ON relation_tuples(namespace, object_id, relation);
```

---

### Organization Domain（组织域）

```sql
-- ─────────────────────────────────────────────────────────────
-- 表：organization_units（组织单元）
-- 作用：组织结构的基本节点，覆盖从事业部到小队的各类组织形态。
--       不使用 parent_id 树形结构，而是通过 organization_relations 表建图；
--       type 支持 Spotify 模型（tribe/squad/chapter/guild）和传统层级（division/department）。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE organization_units (
  id           UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id    UUID        NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  type         VARCHAR(30)  NOT NULL
               CHECK (type IN ('division','department','team','tribe','squad','chapter','guild','legalEntity','region')),
  name         VARCHAR(255) NOT NULL,
  code         VARCHAR(100),
  status       VARCHAR(20)  NOT NULL DEFAULT 'active' CHECK (status IN ('active','archived')),
  effective_at TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
  end_at       TIMESTAMPTZ,                                     -- NULL = 当前有效
  created_at   TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_ou_tenant        ON organization_units(tenant_id);
CREATE INDEX idx_ou_tenant_active ON organization_units(tenant_id) WHERE status = 'active';
ALTER TABLE organization_units ENABLE ROW LEVEL SECURITY;
CREATE POLICY ou_tenant_isolation ON organization_units
  USING (tenant_id = current_setting('app.current_tenant_id')::uuid);

-- ─────────────────────────────────────────────────────────────
-- 表：organization_relations（组织关系图）
-- 作用：用有向图表达组织单元之间的各类关系，是矩阵式组织的核心设计。
--       relation_type 覆盖父子（parent_of）、管理（manages）、虚线协作（dotted_line_to）等；
--       CHECK (from_org_id <> to_org_id) 防止自环；遍历时需用 Recursive CTE 并加深度保护。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE organization_relations (
  id            UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  from_org_id   UUID        NOT NULL REFERENCES organization_units(id),
  to_org_id     UUID        NOT NULL REFERENCES organization_units(id),
  relation_type VARCHAR(50)  NOT NULL
                CHECK (relation_type IN ('parent_of','manages','collaborates_with','funds','dotted_line_to','reports_to','belongs_to')),
  effective_at  TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
  end_at        TIMESTAMPTZ,
  CHECK (from_org_id <> to_org_id)   -- 禁止自环
);
CREATE INDEX idx_org_rel_from ON organization_relations(from_org_id);
CREATE INDEX idx_org_rel_to   ON organization_relations(to_org_id);

-- ─────────────────────────────────────────────────────────────
-- 表：positions（岗位）
-- 作用：将"职位"与"人"解耦，岗位独立存在，可以无人占用（status=open）。
--       这是 SAP / Workday 的标准 Position-based Architecture；
--       一个岗位可被多人分时占用（如产假代岗），也可由一人同时兼任多个岗位。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE positions (
  id             UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id         UUID        NOT NULL REFERENCES organization_units(id),
  title          VARCHAR(255) NOT NULL,
  job_grade_id   UUID,
  cost_center_id UUID,
  headcount      SMALLINT     NOT NULL DEFAULT 1 CHECK (headcount > 0),
  status         VARCHAR(20)  NOT NULL DEFAULT 'open' CHECK (status IN ('open','filled','frozen')),
  created_at     TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_positions_org ON positions(org_id);

-- ─────────────────────────────────────────────────────────────
-- 表：assignments（岗位分配）
-- 作用：连接 User 和 Position 的桥接表，记录"谁在什么时间以多少精力担任某岗位"。
--       allocation（0.0–1.0）表示时间投入比例，支持矩阵式的多岗兼任；
--       is_primary 标记主岗，决定汇报线和成本归属；含时间段支持时间旅行查询。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE assignments (
  id          UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id   UUID        NOT NULL REFERENCES tenants(id),
  user_id     UUID        NOT NULL REFERENCES users(id),
  position_id UUID        NOT NULL REFERENCES positions(id),
  allocation  NUMERIC(3,2) NOT NULL DEFAULT 1.0 CHECK (allocation BETWEEN 0 AND 1),
  is_primary  BOOLEAN      NOT NULL DEFAULT FALSE,
  start_at    TIMESTAMPTZ  NOT NULL,
  end_at      TIMESTAMPTZ,
  status      VARCHAR(20)  NOT NULL DEFAULT 'active' CHECK (status IN ('active','on_leave','terminated')),
  created_at  TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_assignments_user_active   ON assignments(user_id) WHERE status = 'active';
CREATE INDEX idx_assignments_position      ON assignments(position_id);
CREATE INDEX idx_assignments_tenant_period ON assignments(tenant_id, start_at, end_at);
ALTER TABLE assignments ENABLE ROW LEVEL SECURITY;
CREATE POLICY assignments_tenant_isolation ON assignments
  USING (tenant_id = current_setting('app.current_tenant_id')::uuid);

-- ─────────────────────────────────────────────────────────────
-- 表：reporting_lines（汇报线）
-- 作用：记录 Assignment 之间的上下级汇报关系，是矩阵式组织的核心实现。
--       solid（实线）为行政汇报线，dotted（虚线）为功能性汇报线；
--       汇报关系挂在 Assignment 上而非 User 上，支持同一人在不同岗位向不同人汇报。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE reporting_lines (
  id                         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  subordinate_assignment_id  UUID NOT NULL REFERENCES assignments(id),
  manager_assignment_id      UUID NOT NULL REFERENCES assignments(id),
  type                       VARCHAR(20) NOT NULL
                             CHECK (type IN ('solid','dotted','functional','project')),
  CHECK (subordinate_assignment_id <> manager_assignment_id)  -- 禁止自汇报
);
CREATE INDEX idx_rl_subordinate ON reporting_lines(subordinate_assignment_id);
CREATE INDEX idx_rl_manager     ON reporting_lines(manager_assignment_id);

-- ─────────────────────────────────────────────────────────────
-- 表：cost_centers（成本中心）
-- 作用：财务维度的组织映射，用于人力成本归属和预算管控。
--       Position 关联 CostCenter，决定员工薪酬从哪个预算池扣减；
--       支持多货币（currency），适应跨国企业场景。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE cost_centers (
  id           UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id    UUID        NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  code         VARCHAR(100) UNIQUE NOT NULL,
  owner_org_id UUID         NOT NULL REFERENCES organization_units(id),
  currency     CHAR(3)      NOT NULL DEFAULT 'CNY',
  created_at   TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_cost_centers_tenant ON cost_centers(tenant_id);
ALTER TABLE cost_centers ENABLE ROW LEVEL SECURITY;
CREATE POLICY cc_tenant_isolation ON cost_centers
  USING (tenant_id = current_setting('app.current_tenant_id')::uuid);

-- ─────────────────────────────────────────────────────────────
-- 表：org_changes（组织变更快照）
-- 作用：记录组织结构的每次变更历史，支持"时间旅行"查询（查看任意时间点的组织架构）。
--       snapshot（JSONB）存储该时刻的完整组织状态；
--       矩阵组织变动频繁，此表是合规审计和历史回溯的核心依据。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE org_changes (
  id           UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id    UUID        NOT NULL REFERENCES tenants(id),
  change_type  VARCHAR(30)  NOT NULL
               CHECK (change_type IN ('created','restructured','merged','dissolved','hired','terminated')),
  effective_at TIMESTAMPTZ  NOT NULL,
  snapshot     JSONB        NOT NULL,                           -- 该时刻完整组织快照
  requested_by UUID         NOT NULL REFERENCES users(id),
  approval_id  UUID,
  created_at   TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_org_changes_tenant_time ON org_changes(tenant_id, effective_at);
```

---

### Collaboration Domain（协作域）

```sql
-- ─────────────────────────────────────────────────────────────
-- 表：workspaces（工作区）
-- 作用：协作内容的顶层容器，在 Tenant 内划分独立的协作空间（如按产品线或部门）。
--       visibility 控制可见范围；Project 和资源都归属于某个 Workspace；
--       Enterprise 2.0 的开放协作特性要求 Workspace 之间可受控地跨边界共享。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE workspaces (
  id         UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id  UUID        NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  name       VARCHAR(255) NOT NULL,
  visibility VARCHAR(20)  NOT NULL DEFAULT 'private' CHECK (visibility IN ('public','private','restricted')),
  created_at TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_workspaces_tenant ON workspaces(tenant_id);
ALTER TABLE workspaces ENABLE ROW LEVEL SECURITY;
CREATE POLICY ws_tenant_isolation ON workspaces
  USING (tenant_id = current_setting('app.current_tenant_id')::uuid);

-- ─────────────────────────────────────────────────────────────
-- 表：projects（项目）
-- 作用：工作区内的协作单元，代表一个有边界的工作集合（如产品需求、研发任务、营销活动）。
--       owner_org_id 记录负责该项目的组织单元，用于成本归属和汇报；
--       classification_id 关联数据分级，支持 DLP（数据防泄漏）策略。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE projects (
  id                UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  workspace_id      UUID        NOT NULL REFERENCES workspaces(id) ON DELETE CASCADE,
  owner_org_id      UUID        NOT NULL REFERENCES organization_units(id),
  visibility        VARCHAR(20)  NOT NULL DEFAULT 'private' CHECK (visibility IN ('public','private','restricted')),
  classification_id UUID,
  created_at        TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_projects_workspace ON projects(workspace_id);
CREATE INDEX idx_projects_owner_org ON projects(owner_org_id);

-- ─────────────────────────────────────────────────────────────
-- 表：participation（参与关系）
-- 作用：记录主体（用户/组/服务账号/Agent）对协作资源的参与角色。
--       通用多态设计支持 Workspace、Project、TeamSpace 等多种资源类型；
--       与 role_bindings 的区别：participation 是协作语义（谁在参与），
--       role_bindings 是权限语义（谁能做什么）。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE participation (
  id             UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  principal_type VARCHAR(30)  NOT NULL CHECK (principal_type IN ('user','group','serviceAccount','agent')),
  principal_id   UUID         NOT NULL,
  resource_type  VARCHAR(50)  NOT NULL,        -- 如 'project'、'workspace'
  resource_id    UUID         NOT NULL,
  role           VARCHAR(30)  NOT NULL CHECK (role IN ('owner','editor','viewer','commenter')),
  joined_at      TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE UNIQUE INDEX idx_participation_unique ON participation(principal_type, principal_id, resource_type, resource_id);
CREATE INDEX idx_participation_resource ON participation(resource_type, resource_id);

-- ─────────────────────────────────────────────────────────────
-- 表：activities（活动流）
-- 作用：Enterprise 2.0 的标志性能力，记录系统中所有可观察的动作事件。
--       遵循 ActivityStreams 2.0 标准（actor + verb + object + target 结构）；
--       为用户提供动态 Feed、通知触发、行为分析的统一数据源。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE activities (
  id                  UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  actor_id            UUID        NOT NULL,
  verb                VARCHAR(30)  NOT NULL CHECK (verb IN ('created','updated','commented','liked','joined','mentioned')),
  object_type         VARCHAR(100) NOT NULL,
  object_id           UUID         NOT NULL,
  target              TEXT,
  context_resource_id UUID,
  timestamp           TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_activities_actor     ON activities(actor_id, timestamp DESC);
CREATE INDEX idx_activities_object    ON activities(object_type, object_id);
CREATE INDEX idx_activities_context   ON activities(context_resource_id) WHERE context_resource_id IS NOT NULL;

-- ─────────────────────────────────────────────────────────────
-- 表：tags（标签，folksonomy）
-- 作用：支持用户自创的非结构化分类标签，是 Enterprise 2.0 folksonomy（民间分类学）的核心。
--       标签由员工自由创建，而非 IT 预定义，体现涌现式知识组织；
--       通过 taggings 表与任意资源类型关联，驱动搜索和知识发现。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE tags (
  id         UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id  UUID        NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  name       VARCHAR(200) NOT NULL,
  created_by UUID         NOT NULL REFERENCES users(id),
  created_at TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE UNIQUE INDEX idx_tags_tenant_name ON tags(tenant_id, LOWER(name));
ALTER TABLE tags ENABLE ROW LEVEL SECURITY;
CREATE POLICY tags_tenant_isolation ON tags
  USING (tenant_id = current_setting('app.current_tenant_id')::uuid);

-- ─────────────────────────────────────────────────────────────
-- 表：taggings（标签关联）
-- 作用：多态关联表，将 Tag 与任意资源类型（项目、文档、人员等）绑定。
--       通过 resource_type + resource_id 的组合，一套标签体系可横跨所有业务实体；
--       支持全文搜索系统（OpenSearch）以标签为维度做内容聚合。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE taggings (
  id            UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tag_id        UUID        NOT NULL REFERENCES tags(id) ON DELETE CASCADE,
  resource_type VARCHAR(100) NOT NULL,
  resource_id   UUID         NOT NULL,
  tagged_by     UUID         NOT NULL REFERENCES users(id),
  created_at    TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE UNIQUE INDEX idx_taggings_unique ON taggings(tag_id, resource_type, resource_id);
CREATE INDEX idx_taggings_resource ON taggings(resource_type, resource_id);
```

---

### Governance Domain（治理域）

```sql
-- ─────────────────────────────────────────────────────────────
-- 表：audit_logs（审计日志，不可篡改）
-- 作用：记录系统中所有安全敏感操作，是合规审计和安全溯源的不可缺少的基础设施。
--       通过数据库 RULE 禁止 UPDATE / DELETE，确保日志不可篡改；
--       按时间范围分区（PARTITION BY RANGE），提升大表查询效率并支持按年归档。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE audit_logs (
  id            UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id     UUID        NOT NULL REFERENCES tenants(id),
  actor_type    VARCHAR(30)  NOT NULL CHECK (actor_type IN ('user','service_account','agent')),
  actor_id      UUID         NOT NULL,
  action        VARCHAR(200) NOT NULL,    -- 如 'role.assigned'、'document.exported'
  resource_type VARCHAR(100) NOT NULL,
  resource_id   UUID         NOT NULL,
  before_state  JSONB,                    -- 操作前快照
  after_state   JSONB,                    -- 操作后快照
  ip            INET,
  user_agent    TEXT,
  timestamp     TIMESTAMPTZ  NOT NULL DEFAULT NOW()
)
-- 按时间分区，提升大表查询和归档效率
PARTITION BY RANGE (timestamp);

CREATE TABLE audit_logs_2026 PARTITION OF audit_logs
  FOR VALUES FROM ('2026-01-01') TO ('2027-01-01');

-- 审计日志禁止 UPDATE / DELETE（行级强制）
CREATE RULE no_update_audit_logs AS ON UPDATE TO audit_logs DO INSTEAD NOTHING;
CREATE RULE no_delete_audit_logs AS ON DELETE TO audit_logs DO INSTEAD NOTHING;

CREATE INDEX idx_audit_logs_tenant_time   ON audit_logs(tenant_id, timestamp DESC);
CREATE INDEX idx_audit_logs_actor         ON audit_logs(actor_type, actor_id, timestamp DESC);
CREATE INDEX idx_audit_logs_resource      ON audit_logs(resource_type, resource_id);

-- ─────────────────────────────────────────────────────────────
-- 表：approval_workflows（审批流程）
-- 作用：企业操作的多级审批流，如权限申请、组织变更、合同签署等。
--       approvers（JSONB）存储审批人列表和当前步骤；
--       sla_due_at 支持 SLA（服务等级协议）超时自动升级或拒绝。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE approval_workflows (
  id           UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id    UUID        NOT NULL REFERENCES tenants(id),
  type         VARCHAR(100) NOT NULL,
  initiator    UUID         NOT NULL REFERENCES users(id),
  approvers    JSONB        NOT NULL DEFAULT '[]',
  current_step SMALLINT     NOT NULL DEFAULT 0,
  state        VARCHAR(20)  NOT NULL DEFAULT 'pending'
               CHECK (state IN ('pending','approved','rejected','expired')),
  sla_due_at   TIMESTAMPTZ,
  created_at   TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
  updated_at   TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_approval_wf_tenant_state ON approval_workflows(tenant_id, state);
ALTER TABLE approval_workflows ENABLE ROW LEVEL SECURITY;
CREATE POLICY aw_tenant_isolation ON approval_workflows
  USING (tenant_id = current_setting('app.current_tenant_id')::uuid);

-- ─────────────────────────────────────────────────────────────
-- 表：delegations（委派）
-- 作用：允许用户在特定时间段内将自己的部分权限临时转授给另一人（如出差、休假期间）。
--       scope（JSONB）限制委派的权限范围，防止过度授权；
--       CHECK (end_at > start_at) 保证时间段有效；到期自动失效，无需手动回收。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE delegations (
  id           UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  delegator_id UUID        NOT NULL REFERENCES users(id),
  delegatee_id UUID        NOT NULL REFERENCES users(id),
  scope        JSONB        NOT NULL DEFAULT '{}',
  start_at     TIMESTAMPTZ  NOT NULL,
  end_at       TIMESTAMPTZ  NOT NULL,
  CHECK (delegator_id <> delegatee_id),
  CHECK (end_at > start_at)
);
CREATE INDEX idx_delegations_delegatee ON delegations(delegatee_id, end_at);  -- 查找有效委派

-- ─────────────────────────────────────────────────────────────
-- 表：legal_holds（法务保全）
-- 作用：应法律诉讼或监管调查要求，冻结相关数据使其不可删除或修改。
--       custodians 记录数据保管人（责任人）；Legal Hold 激活期间，
--       相关数据的 DataRetentionPolicy（数据保留策略）自动挂起，即使过了保留期也不清除。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE legal_holds (
  id         UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id  UUID        NOT NULL REFERENCES tenants(id),
  name       VARCHAR(255) NOT NULL,
  custodians UUID[]       NOT NULL DEFAULT '{}',             -- 数据保管人 User ID 数组
  scope      JSONB        NOT NULL DEFAULT '{}',
  issued_by  UUID         NOT NULL REFERENCES users(id),
  issued_at  TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
  status     VARCHAR(20)  NOT NULL DEFAULT 'active' CHECK (status IN ('active','released')),
  release_at TIMESTAMPTZ
);
CREATE INDEX idx_legal_holds_tenant_status ON legal_holds(tenant_id, status);
ALTER TABLE legal_holds ENABLE ROW LEVEL SECURITY;
CREATE POLICY lh_tenant_isolation ON legal_holds
  USING (tenant_id = current_setting('app.current_tenant_id')::uuid);

-- ─────────────────────────────────────────────────────────────
-- 表：data_classifications（数据分级）
-- 作用：定义租户内的数据敏感度等级（公开 / 内部 / 机密 / 受限），支持 DLP 策略执行。
--       资源（Project、Document 等）关联此表，影响导出、分享、访问的审批流程；
--       handling_policy（JSONB）记录每个级别的具体处理规范（如禁止截图、禁止外发）。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE data_classifications (
  id               UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id        UUID        NOT NULL REFERENCES tenants(id),
  level            VARCHAR(20)  NOT NULL CHECK (level IN ('public','internal','confidential','restricted')),
  label            VARCHAR(200) NOT NULL,
  handling_policy  JSONB        NOT NULL DEFAULT '{}',
  created_at       TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_dc_tenant_level ON data_classifications(tenant_id, level);
```

---

### Integration Domain（集成域）

```sql
-- ─────────────────────────────────────────────────────────────
-- 表：webhooks（Webhook 订阅）
-- 作用：允许外部系统订阅本系统的事件推送（如用户创建、角色变更、组织重组）。
--       secret 存储 HMAC 签名密钥（加密），接收方验签确保消息未被篡改；
--       retry_policy 支持指数退避重试，配合 event_logs 实现至少一次投递（Outbox 模式）。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE webhooks (
  id           UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id    UUID        NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  url          TEXT         NOT NULL,
  events       TEXT[]       NOT NULL DEFAULT '{}',
  secret       VARCHAR(500) NOT NULL,                          -- HMAC 签名密钥（加密存储）
  status       VARCHAR(20)  NOT NULL DEFAULT 'active' CHECK (status IN ('active','disabled')),
  retry_policy JSONB        NOT NULL DEFAULT '{"max_attempts":5,"backoff":"exponential"}',
  created_at   TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_webhooks_tenant ON webhooks(tenant_id);
ALTER TABLE webhooks ENABLE ROW LEVEL SECURITY;
CREATE POLICY webhooks_tenant_isolation ON webhooks
  USING (tenant_id = current_setting('app.current_tenant_id')::uuid);

-- ─────────────────────────────────────────────────────────────
-- 表：event_logs（事件日志，Outbox 模式）
-- 作用：Webhook 的发送记录，通过 Outbox 模式保证消息至少一次送达。
--       delivery_status + next_retry_at 驱动后台重试调度；
--       attempts 记录重试次数，超限后标记 failed 并触发告警。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE event_logs (
  id              UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  webhook_id      UUID        NOT NULL REFERENCES webhooks(id) ON DELETE CASCADE,
  event_type      VARCHAR(200) NOT NULL,
  payload         JSONB        NOT NULL,
  delivery_status VARCHAR(20)  NOT NULL DEFAULT 'pending' CHECK (delivery_status IN ('pending','delivered','failed')),
  attempts        SMALLINT     NOT NULL DEFAULT 0,
  next_retry_at   TIMESTAMPTZ,
  created_at      TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_event_logs_pending    ON event_logs(next_retry_at) WHERE delivery_status = 'pending';
CREATE INDEX idx_event_logs_webhook    ON event_logs(webhook_id, created_at DESC);

-- ─────────────────────────────────────────────────────────────
-- 表：scim_syncs（SCIM 同步记录）
-- 作用：跟踪从 IdP（Okta / Azure Entra ID）通过 SCIM 2.0 协议同步的用户和组的状态。
--       external_id 是 IdP 侧的资源 ID；conflict_resolution 决定冲突时以系统数据还是 SCIM 数据为准；
--       通过此表可快速定位同步失败或数据不一致的问题。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE scim_syncs (
  id                   UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id            UUID        NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  connector_id         UUID        NOT NULL REFERENCES integration_connectors(id),
  resource_type        VARCHAR(20)  NOT NULL CHECK (resource_type IN ('User','Group')),
  external_id          VARCHAR(500) NOT NULL,
  last_sync_at         TIMESTAMPTZ,
  sync_status          VARCHAR(20)  NOT NULL DEFAULT 'pending' CHECK (sync_status IN ('synced','pending','conflict')),
  conflict_resolution  VARCHAR(20)  NOT NULL DEFAULT 'system_wins' CHECK (conflict_resolution IN ('system_wins','scim_wins')),
  created_at           TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE UNIQUE INDEX idx_scim_syncs_unique ON scim_syncs(tenant_id, connector_id, resource_type, external_id);
```

---

### AI / Agent Domain（AI 与智能体域）

```sql
-- ─────────────────────────────────────────────────────────────
-- 表：agents（AI 智能体）
-- 作用：将 AI Agent 建模为系统中的一等 Principal（主体），使其可参与权限体系和审计日志。
--       model_ref 指向所使用的 LLM（大语言模型）版本；
--       owner_id 是责任人（人类），确保每个 Agent 的行为可追溯到具体用户。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE agents (
  id         UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id  UUID        NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  name       VARCHAR(200) NOT NULL,
  owner_id   UUID         NOT NULL REFERENCES users(id),
  model_ref  VARCHAR(100) NOT NULL,   -- 如 'claude-opus-4-7'
  status     VARCHAR(20)  NOT NULL DEFAULT 'active' CHECK (status IN ('active','suspended','deprecated')),
  created_at TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_agents_tenant ON agents(tenant_id);
ALTER TABLE agents ENABLE ROW LEVEL SECURITY;
CREATE POLICY agents_tenant_isolation ON agents
  USING (tenant_id = current_setting('app.current_tenant_id')::uuid);

-- ─────────────────────────────────────────────────────────────
-- 表：agent_sessions（智能体会话）
-- 作用：记录 AI Agent 的每次任务执行会话，是 Agent 行为审计的起点。
--       initiator_principal_id 记录触发本次会话的主体（用户或另一个 Agent）；
--       trace_id 是分布式追踪 ID，将该会话的所有 agent_actions 和 audit_logs 串联起来。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE agent_sessions (
  id                      UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  agent_id                UUID        NOT NULL REFERENCES agents(id),
  initiator_principal_id  UUID        NOT NULL,
  started_at              TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
  ended_at                TIMESTAMPTZ,
  trace_id                VARCHAR(200) NOT NULL  -- 分布式追踪 ID
);
CREATE INDEX idx_agent_sessions_agent ON agent_sessions(agent_id, started_at DESC);
CREATE INDEX idx_agent_sessions_trace ON agent_sessions(trace_id);

-- ─────────────────────────────────────────────────────────────
-- 表：agent_actions（智能体操作）
-- 作用：记录 Agent 在一次会话中执行的每个具体操作（工具调用、知识查询、API 调用）。
--       所有操作同步写入 audit_logs 表（携带 trace_id），确保 Agent 行为完全可审计；
--       resource_ref 标识操作对象（如 'project:alpha'），result（JSONB）存储操作结果。
-- ─────────────────────────────────────────────────────────────
CREATE TABLE agent_actions (
  id               UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  agent_session_id UUID        NOT NULL REFERENCES agent_sessions(id),
  action_type      VARCHAR(30)  NOT NULL CHECK (action_type IN ('tool_call','knowledge_query','api_call')),
  resource_ref     VARCHAR(500),   -- 如 'project:alpha'
  result           JSONB        NOT NULL DEFAULT '{}',
  created_at       TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_agent_actions_session ON agent_actions(agent_session_id, created_at);
```

---

### RLS（行级安全）统一应用说明

```sql
-- 在应用层的连接/事务开始时执行（每个请求），
-- 所有已开启 RLS 的表都会自动按此过滤，
-- 即使业务代码忘记加 WHERE tenant_id = ?，数据库层也会兜住。
SET LOCAL app.current_tenant_id = '你的租户 UUID';

-- 验证 RLS 是否生效：
SELECT COUNT(*) FROM projects;  -- 只会返回当前租户的数据
```

---

## 十四、一句话总结

**Enterprise 2.0 的本质是把企业从"流程驱动的树"改造成"协作涌现的图"；矩阵式组织（Matrix Organization）是这张图在 HR（人力资源）维度的投影。**

设计这套 SaaS（软件即服务）的关键是把三张图建对：**组织图（Org Graph）、关系权限图（Zanzibar Tuple Graph）、活动图（Activity Stream Graph）**，并让 Tenant（租户）、Time（时间）、Principal（主体，含 AI Agent）三者贯穿其中。其余都是工程实现细节。
