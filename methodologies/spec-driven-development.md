# Spec-Driven Development 最佳实践

> 适用于：Node.js + TypeScript + ESM + Nest.js + Fastify + Vitest + SWC + PostgreSQL + Prisma + DDD + 微服务 + RESTful + Mono Repo (pnpm)

---

## 目录

1. [Specification 的本质](#1-specification-的本质)
2. [Spec 文件格式规范](#2-spec-文件格式规范)
3. [实施步骤](#3-实施步骤)
4. [版本管理策略](#4-版本管理策略)
5. [证明 Agent 产出正确性](#5-证明-agent-产出的正确性)
6. [需求追加与变更](#6-需求追加与变更)
7. [测试策略](#7-测试策略)
8. [线上错误跟踪](#8-线上错误跟踪)
9. [自动化错误处理流程](#9-自动化错误处理流程)

---

## 1. Specification 的本质

### 1.1 核心定义

**Specification（规格）是"机器可读的契约"，而非人类可读的文档。**

| 维度 | 传统文档 | Specification |
|------|----------|---------------|
| 格式 | 自由格式 Markdown | 结构化 Schema + 机器校验 |
| 角色 | 人类阅读 | 人类阅读 + Agent 解析 |
| 验证 | 人工审查 | 自动 lint + 人工审查 |
| 版本 | 可选 | 必须版本化 |
| 可执行性 | 不可执行 | 可派生代码/测试 |

Specification 是**源头（Source of Truth）**，而非生成物。代码和测试都应从 Spec 派生，而非反过来。

### 1.2 Specification 与相关概念的区别

```
需求文档（Requirements）
    │
    ├── 描述"做什么"
    ├── 人类语言
    └── 是 Spec 的输入

Meta-Spec（规格规范）
    │
    ├── 描述"Spec 应该长什么样"
    ├── 格式约束 + Schema 定义
    └── 是 Spec 的元数据

Specification
    │
    ├── 描述"系统应该如何构建"
    ├── 结构化 + 机器可校验
    ├── 是代码/测试/文档的共同源头
    └── 必须版本化

用户故事（User Story）
    │
    ├── 描述"用户想要什么"
    ├── 通常在 Spec 之前定义
    └── 是 Spec 的输入之一
```

### 1.3 各 AI 回答的交叉验证

| 问题 | ChatGPT | Claude | DeepSeek | Gemini | Grok | 一致结论 |
|------|---------|--------|----------|--------|------|----------|
| Spec 本质 | Machine-readable Contract | 源头 + 活文档 | 第一类制品 | SSOT | 活的规格 | ✅ Spec 是源头，不是生成物 |
| Markdown 定位 | 容器，不是规范 | 人类可读层 | 可用但需 DSL 约束 | 需结构化 | 模板化 Markdown | ✅ Markdown 需配合 Schema |
| 是否需要 Plan 层 | 必须 | 隐式 | 需 DAG | 三阶段 | 需 Tasks 层 | ✅ Plan 是 Spec 到 Code 的必经层 |

---

## 2. Spec 文件格式规范

### 2.1 双层架构

```
┌─────────────────────────────────────────────────────────────┐
│  Layer 1: Spec DSL（强约束层）                               │
│  ├── 格式：YAML / JSON + frontmatter                         │
│  ├── 必须有 Schema 校验（Zod / JSON Schema）                  │
│  └── 用于 Agent 解析和自动处理                                │
├─────────────────────────────────────────────────────────────┤
│  Layer 2: 人类可读层（Markdown）                              │
│  ├── 格式：Markdown + frontmatter                             │
│  ├── 用于人类审查、推理、决策                                   │
│  └── 解释上下文，而非规范本身                                  │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Spec 文件标准模板

```yaml
---
version: "1.0.0"
feature: user-authentication
domain: auth
status: draft | review | approved | locked
owner: @username
created: 2026-04-15
updated: 2026-04-15
---

# 概述
[业务目标、成功标准]

# 用户故事
- As a: [角色]
  I want: [功能]
  So that: [价值]

# 验收标准（Acceptance Criteria）
- AC-001: [标准描述]
  Given: [前置条件]
  When: [操作]
  Then: [预期结果]

# 数据模型
entities:
  - name: User
    fields:
      - name: id
        type: string
        format: uuid
      - name: email
        type: string
        format: email
      - name: passwordHash
        type: string

# API 契约
paths:
  - /auth/login
    method: POST
    request:
      body:
        - username: string
        - password: string
    response:
      200:
        body:
          - token: string

# 约束条件
constraints:
  - password must be hashed with bcrypt
  - token expires in 24h

# 测试策略
test_cases:
  - name: valid login
    input: { username: "a", password: "b" }
    expect: { status: 200, token: non-empty }
  - name: invalid password
    input: { username: "a", password: "wrong" }
    expect: { status: 401 }

# 假设与开放问题
assumptions:
  - A-001: 第三方 OAuth 暂不考虑
open_questions:
  - OQ-001: 是否需要 MFA？
```

### 2.3 项目级 Spec 结构（Mono Repo）

```
spec/
├── meta/
│   ├── meta-spec.yaml          # Meta-Spec 规范定义
│   └── schema/
│       ├── feature.schema.yaml
│       ├── api.schema.yaml
│       └── test-case.schema.yaml
├── domain/
│   └── auth/
│       ├── v1/
│       │   ├── spec.yaml       # 正式版 Spec
│       │   ├── spec.md         # 人类可读版
│       │   └── changelog.md
│       └── v2/
├── api/
│   └── user-management/
│       ├── spec.yaml
│       └── openapi.yaml        # 派生的 OpenAPI
└── shared/
    └── common-types/
        └── spec.yaml
```

---

## 3. 实施步骤

### 3.1 标准流程概览

```
┌──────────────────────────────────────────────────────────────────┐
│                      Spec-Driven Development 流程                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐        │
│  │   Specify    │────▶│    Plan     │────▶│    Tasks    │        │
│  │  (规格生成)   │     │  (技术规划)  │     │  (任务拆解)  │        │
│  └─────────────┘     └─────────────┘     └─────────────┘        │
│         │                                       │                 │
│         ▼                                       ▼                 │
│  ┌─────────────┐                         ┌─────────────┐        │
│  │    Lint     │                         │  Implement   │        │
│  │  (自动校验)  │                         │   (实现)      │        │
│  └─────────────┘                         └─────────────┘        │
│         │                                       │                 │
│         ▼                                       ▼                 │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐        │
│  │   Review    │────▶│    E2E     │◀────│     CI      │        │
│  │ (人工评审)   │     │  (黑盒测试) │     │  (自动测试)  │        │
│  └─────────────┘     └─────────────┘     └─────────────┘        │
│                                                                   │
└──────────────────────────────────────────────────────────────────┘
```

### 3.2 详细步骤说明

---

#### Step 1: 编写需求文档（Requirements Authoring）

| 属性 | 说明 |
|------|------|
| **执行方** | 人类（产品/BA） |
| **输入** | 业务目标、用户反馈、现有系统约束 |
| **输出** | `requirements/*.md`（用户故事 + 验收标准） |
| **格式** | Markdown（固定模板：User Story + AC） |
| **注意事项** | 需求应无歧义、可验证；每个用户故事对应明确的验收标准 |

**需求模板示例：**

```markdown
## 用户故事

- **ID**: US-001
- **作为**: 注册用户
- **我想要**: 通过邮箱密码登录系统
- **以便**: 访问我的个人数据

## 验收标准

| ID | 场景 | Given | When | Then |
|----|------|-------|------|------|
| AC-001 | 正常登录 | 用户已注册 | 输入正确邮箱和密码 | 返回 JWT Token |
| AC-002 | 密码错误 | 用户已注册 | 输入正确邮箱但错误密码 | 返回 401 |
| AC-003 | 用户不存在 | 无 | 输入未注册邮箱 | 返回 404 |
```

---

#### Step 2: 编写 Meta-Spec（格式规范定义）

| 属性 | 说明 |
|------|------|
| **执行方** | 人类（架构师/技术 lead） |
| **输入** | 项目技术栈、架构约束 |
| **输出** | `spec/meta/meta-spec.yaml` + Zod Schema |
| **格式** | YAML + JSON Schema / Zod Schema |
| **注意事项** | Meta-Spec 一旦确定，不频繁变更；定义 Spec 的 mandatory fields |

**Zod Schema 示例：**

```typescript
// spec/meta/schema/feature.schema.ts
import { z } from 'zod';

export const FeatureSpecSchema = z.object({
  version: z.string(),
  feature: z.string(),
  domain: z.string(),
  status: z.enum(['draft', 'review', 'approved', 'locked']),
  overview: z.string(),
  userStories: z.array(z.object({
    id: z.string(),
    asA: z.string(),
    iWant: z.string(),
    soThat: z.string(),
  })),
  acceptanceCriteria: z.array(z.object({
    id: z.string(),
    name: z.string(),
    given: z.string(),
    when: z.string(),
    then: z.string(),
  })),
  entities: z.array(z.object({
    name: z.string(),
    fields: z.array(z.object({
      name: z.string(),
      type: z.string(),
      format: z.string().optional(),
      constraints: z.array(z.string()).optional(),
    })),
  })).optional(),
  paths: z.array(z.object({
    path: z.string(),
    method: z.string(),
    request: z.object({
      body: z.array(z.object({
        name: z.string(),
        type: z.string(),
        required: z.boolean().optional(),
      })),
    }),
    response: z.record(z.string(), z.object({
      body: z.array(z.object({
        name: z.string(),
        type: z.string(),
      })),
    })),
  })).optional(),
  constraints: z.array(z.string()).optional(),
  testCases: z.array(z.object({
    name: z.string(),
    input: z.record(z.string(), z.unknown()),
    expect: z.record(z.string(), z.unknown()),
  })).optional(),
  assumptions: z.array(z.string()).optional(),
  openQuestions: z.array(z.string()).optional(),
});

export type FeatureSpec = z.infer<typeof FeatureSpecSchema>;
```

---

#### Step 3: 生成 Spec 草稿（Spec Generation）

| 属性 | 说明 |
|------|------|
| **执行方** | Agent（Spec Generator Agent） |
| **输入** | Requirements + Meta-Spec + 项目上下文 |
| **输出** | `spec/domain/{feature}/v{n}/spec.yaml` |
| **工具** | Claude Code / Cursor + Skill（固定 Prompt 模板） |
| **注意事项** | Agent 只做补全/校验，不做自由生成；必须输出 Schema 校验通过的 YAML |

**Prompt 模板示例：**

```markdown
# Spec Generation Prompt

## 角色
你是一个 Spec 生成专家。

## 输入
- 需求文档：{requirements_path}
- Meta-Spec 规范：{meta_spec_path}
- 技术栈：Node.js + TypeScript + Nest.js + Prisma

## 输出要求
1. 严格遵循 Meta-Spec 的 YAML 格式
2. 每个 user story 必须有对应的 acceptance criteria
3. 每个 API endpoint 必须定义 request/response schema
4. 每个 entity 必须定义完整字段和约束
5. 必须标注 assumptions 和 open questions

## 校验
输出前用 Zod Schema 校验格式是否正确。

## 禁止
- 不要自由发挥添加需求文档未提及的内容
- 不要使用未定义的字段名
- 不要省略 mandatory fields
```

---

#### Step 4: Spec 自动校验（Spec Lint）

| 属性 | 说明 |
|------|------|
| **执行方** | 系统（CI 或 pre-commit hook） |
| **输入** | 生成的 Spec YAML |
| **输出** | 校验报告（通过/失败 + 详细错误） |
| **工具** | Zod + JSON Schema Validator + 自定义 lint 规则 |
| **校验内容** | 语法正确性、依赖完整性、覆盖率、闭环校验 |

**校验规则示例：**

```typescript
// spec/meta/lint/rules.ts
export const lintRules = [
  {
    id: 'AC-COVERAGE',
    description: '每个 AC 必须有对应 test case',
    check: (spec: FeatureSpec) => {
      const acIds = spec.acceptanceCriteria.map(ac => ac.id);
      const coveredAcs = spec.testCases?.map(tc => tc.acId) || [];
      const missing = acIds.filter(id => !coveredAcs.includes(id));
      return { pass: missing.length === 0, missing };
    },
  },
  {
    id: 'ENTITY-REF',
    description: 'API request/response 字段必须引用已定义 entity',
    check: (spec: FeatureSpec) => {
      // 检查逻辑
    },
  },
  {
    id: 'OPEN-QUESTIONS',
    description: 'Spec 进入 review 阶段前必须解决所有 OQ',
    check: (spec: FeatureSpec) => {
      return { pass: spec.openQuestions.length === 0 };
    },
  },
];
```

---

#### Step 5: 人工评审 Spec（Spec Review）

| 属性 | 说明 |
|------|------|
| **执行方** | 人类（技术 lead / 架构师）+ 可选 Agent 辅助 |
| **输入** | Spec YAML + Lint 报告 |
| **输出** | Approved Spec（status: approved）或要求修改 |
| **审查维度** | 语义正确性、完整性、一致性、可测试性、架构兼容性 |
| **注意事项** | 这是唯一的"刹车点"；Review 通过后 Spec 锁定 |

**Review Checklist：**

```markdown
## Spec Review Checklist

### 完整性
- [ ] 每个用户故事都有对应的 AC
- [ ] 每个 AC 都是可验证的
- [ ] 所有 API endpoint 都有完整 schema
- [ ] 所有 entity 字段类型和约束已定义
- [ ] 测试覆盖率 ≥ 80%（每条 AC 至少 1 个 test case）

### 正确性
- [ ] API 路径符合 RESTful 规范
- [ ] HTTP 方法使用正确
- [ ] 状态码定义合理
- [ ] 数据类型与 Prisma schema 兼容

### 一致性
- [ ] 与现有系统架构兼容
- [ ] 与其他 Spec 无冲突
- [ ] 命名规范统一

### 可实现性
- [ ] 无歧义的业务规则
- [ ] 约束条件可实现
- [ ] 性能要求可达成
```

---

#### Step 6: 生成技术计划（Plan Generation）

| 属性 | 说明 |
|------|------|
| **执行方** | Agent（Plan Agent） |
| **输入** | Approved Spec + 技术栈上下文 + 现有代码库 |
| **输出** | `plans/{feature}-v{n}.yaml`（任务 DAG） |
| **工具** | Claude Code（专属 Plan Skill） |
| **注意事项** | 必须生成 DAG 而非线性任务；必须标注依赖关系 |

**Plan 模板示例：**

```yaml
feature: user-authentication
version: "1"
status: planned
created: 2026-04-15

architecture:
  pattern: Hexagonal (Ports & Adapters)
  layers:
    - domain: 业务逻辑
    - application: 用例/命令
    - infrastructure: 适配器（DB, API, MQ）

tasks:
  - id: TASK-001
    name: Create User entity and Prisma schema
    type: database
    depends_on: []
    outputs:
      - src/domain/entities/user.entity.ts
      - prisma/schema.prisma

  - id: TASK-002
    name: Implement password hashing service
    type: domain-service
    depends_on: [TASK-001]
    outputs:
      - src/domain/services/password-hash.service.ts

  - id: TASK-003
    name: Create Auth module (controller, service, dto)
    type: api
    depends_on: [TASK-001, TASK-002]
    outputs:
      - src/modules/auth/auth.controller.ts
      - src/modules/auth/auth.service.ts
      - src/modules/auth/dto/login.dto.ts

  - id: TASK-004
    name: Write unit tests for auth service
    type: test
    depends_on: [TASK-003]
    test_framework: vitest
    outputs:
      - src/modules/auth/auth.service.spec.ts

  - id: TASK-005
    name: Write E2E tests for login endpoint
    type: e2e
    depends_on: [TASK-003]
    test_framework: vitest + supertest
    outputs:
      - test/e2e/auth-login.spec.ts
```

---

#### Step 7: 按任务拆解实现（Implement）

| 属性 | 说明 |
|------|------|
| **执行方** | Agent（Code Agent / Test Agent） |
| **输入** | Spec + Plan + Task |
| **输出** | 代码、测试、文档 |
| **工具** | Claude Code（分任务执行） |
| **注意事项** | 每次只执行一个 Task；Task 之间必须等待依赖完成 |

**Agent 分工：**

| Agent | 职责 | 输入 | 输出 |
|-------|------|------|------|
| Spec Agent | Spec 生成 + 校验 | Requirements + Meta-Spec | Spec YAML |
| Plan Agent | 任务拆解 | Spec + 技术栈 | Task DAG |
| Code Agent | 业务代码生成 | Spec + Task | TypeScript 代码 |
| Test Agent | 测试代码生成 | Spec + Task + Code | Vitest 测试 |
| Doc Agent | 文档生成 | Spec + Code | API 文档 |
| Debug Agent | 修复失败 | Test Report + Error | 修复后的代码 |

---

#### Step 8: CI 自动测试（Automated Testing）

| 属性 | 说明 |
|------|------|
| **执行方** | CI 系统（GitHub Actions / GitLab CI） |
| **输入** | 提交的代码 + Spec |
| **输出** | 测试报告（通过/失败 + 覆盖率） |
| **触发条件** | PR 创建/更新、代码提交 |
| **注意事项** | 人工只审计失败报告，不手动执行测试 |

**CI Pipeline 示例：**

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main, 'feat/**']
  pull_request:
    branches: [main]

jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup pnpm
        uses: pnpm/action-setup@v3

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'pnpm'

      - name: Install dependencies
        run: pnpm install

      - name: Type check
        run: pnpm exec tsc --noEmit

      - name: Lint
        run: pnpm exec eslint src --ext .ts

      - name: Run unit tests
        run: pnpm exec vitest run --reporter=verbose
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/test

      - name: Run E2E tests
        run: pnpm exec vitest run --config vitest.config.e2e.ts
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/test_e2e

      - name: Upload coverage
        uses: codecov/codecov-action@v4
```

---

#### Step 9: 黑盒测试（Playwright E2E）

| 属性 | 说明 |
|------|------|
| **执行方** | Agent（Test Agent）+ Playwright MCP |
| **输入** | User Stories + 验收标准 |
| **输出** | Playwright 测试脚本 + 执行报告 |
| **工具** | Playwright + MCP |
| **注意事项** | 黑盒测试基于 User Stories 而非代码；失败时需判断是 Spec 问题还是实现问题 |

---

#### Step 10: 文档生成（Artifact Output）

| 属性 | 说明 |
|------|------|
| **执行方** | Agent（Doc Agent） |
| **输入** | Spec + 实现的代码 |
| **输出** | API 文档、ChangeLog、README |
| **工具** | 自动化文档生成（typedoc、swagger） |
| **注意事项** | 文档必须能追溯到 Spec 的对应章节 |

---

## 4. 版本管理策略

### 4.1 需要版本管理的资源

| 资源类型 | 版本化 | 说明 |
|----------|--------|------|
| Spec 文件 | ✅ 必须 | 与代码同等重要 |
| Meta-Spec | ✅ 必须 | 规范变更需走 PR |
| 测试用例 | ✅ 必须 | 随 Spec 同步更新 |
| API Schema | ✅ 必须 | OpenAPI 等 |
| 用户故事 | ✅ 必须 | 需求变更记录 |
| CI 配置 | ✅ 必须 | 代码同步 |
| 文档 | ⚠️ 可选 | 从 Spec 派生，可再生 |

### 4.2 版本控制规范

```
spec/
├── meta/
│   └── v1.0.0/                    # Meta-Spec 版本
│       ├── meta-spec.yaml
│       └── schema/
└── domain/
    └── auth/
        ├── v1.0.0/               # Feature Spec 版本
        │   ├── spec.yaml
        │   ├── spec.md
        │   ├── spec.lock.yaml    # 锁定版（不可改）
        │   └── changelog.md
        └── v1.1.0/
```

### 4.3 Git 工作流

```bash
# 1. 从 main 创建 feature spec 分支
git checkout -b spec/auth-login-v1

# 2. 编辑 Spec 文件
vim spec/domain/auth/v1/spec.yaml

# 3. 提交 Spec 变更
git add spec/
git commit -m "feat(spec): add auth login spec v1"

# 4. 创建 PR 进行 Spec Review
gh pr create --title "feat(spec): auth login specification"

# 5. Review 通过后，合并到 main
#    CI 自动触发代码生成

# 6. Spec 锁定后，任何变更需走变更流程
```

### 4.4 Spec 变更流程

```
需求变更请求
     │
     ▼
创建 Spec 变更分支（spec/{feature}/v{n+1}）
     │
     ▼
更新 Spec + 填写变更说明
     │
     ▼
触发 Spec Lint（自动校验）
     │
     ▼
人工 Review（评估影响范围）
     │
     ├─ 拒绝：回到 Draft
     └─ 通过：
          │
          ▼
     合并到 main
          │
          ▼
     CI 自动重新生成受影响的代码/测试
          │
          ▼
     运行完整测试套件
          │
          ├─ 失败：Debug Agent 修复
          └─ 通过：合并
```

---

## 5. 证明 Agent 产出的正确性

### 5.1 验证策略

| 策略 | 说明 | 适用场景 |
|------|------|----------|
| Schema 校验 | Zod/JSON Schema 校验输出格式 | 所有 Agent 输出 |
| 单元测试 | 对生成的代码/逻辑写测试 | 关键业务逻辑 |
| 契约测试 | 验证 API 实现是否符合契约 | API endpoint |
| E2E 测试 | 完整业务流程验证 | 用户故事 |
| 覆盖率检查 | 确保测试覆盖关键路径 | 所有生成代码 |
| 回归测试 | Spec 变更后验证未破坏现有功能 | CI 自动触发 |

### 5.2 Harness（确定性）保障

为确保 Agent 产出可复现，必须固定以下要素：

```yaml
# .claude/harness-config.yaml
harness:
  model: claude-opus-4-6
  temperature: 0
  max_tokens: 4096

  input_fixed:
    - requirements_path
    - meta_spec_path
    - project_context

  prompt_version: "1.0.0"      # 固定版本
  schema_version: "1.0.0"       # 固定 Schema
  tool_version:                 # 固定工具链版本
    node: "20"
    pnpm: "9"
    typescript: "5.4"
    vitest: "1.5"
```

### 5.3 多 Agent 协作验证

```
┌──────────────┐    生成 Spec     ┌──────────────┐
│  Spec Agent  │───────────────▶│  Plan Agent  │
└──────────────┘                └──────────────┘
       │                               │
       ▼                               ▼
┌──────────────┐    验证 Schema   ┌──────────────┐
│  Lint Agent  │◀───────────────│  Code Agent  │
└──────────────┘                └──────────────┘
       │                               │
       ▼                               ▼
┌──────────────┐    运行测试      ┌──────────────┐
│  Test Agent  │───────────────▶│  Debug Agent │
└──────────────┘   失败则修复     └──────────────┘
```

### 5.4 证明正确的标准

| 证明维度 | 验证方法 | 通过标准 |
|----------|----------|----------|
| 格式正确 | Zod Schema 校验 | 0 errors |
| 逻辑正确 | 单元测试覆盖率 | ≥ 80% |
| 契约正确 | API 契约测试 | 100% pass |
| 集成正确 | E2E 测试 | 100% pass |
| 回归安全 | 完整测试套件 | 100% pass |

---

## 6. 需求追加与变更

### 6.1 变更处理流程

```
需求追加/变更请求
     │
     ▼
评估影响范围
     │
     ├─ 范围小：直接修改当前版本 Spec
     │
     └─ 范围大：创建新版本 Spec（v{n+1}）
               │
               ▼
更新 Spec（status: draft）
     │
     ▼
Spec Lint（自动校验）
     │
     ▼
Spec Review（人工评审）
     │
     ├─ 拒绝：返回 Draft
     └─ 通过：
          │
          ▼
锁定新版本 Spec（status: locked）
     │
     ▼
CI 自动重新生成受影响的代码/测试
     │
     ▼
运行完整测试套件
     │
     ├─ 失败：Debug Agent 修复
     └─ 通过：Code Review + Merge
```

### 6.2 变更类型与处理

| 变更类型 | 影响范围 | 处理方式 |
|----------|----------|----------|
| Bug 修复 | 代码层 | 直接修复 + 测试 |
| 小功能追加 | 当前版本 Spec | 原地修改 + Review |
| 大功能变更 | 新版本 Spec | 创建新版本 + 完整流程 |
| 架构调整 | Meta-Spec + Spec + Code | 跨版本协调 |

### 6.3 双向同步机制

```typescript
// 当代码变更时，检测是否需要更新 Spec
// tools/spec-sync.ts

export async function checkSpecSync() {
  const codeChanges = await getUncommittedChanges();
  const specChanges = codeChanges.filter(f => f.path.startsWith('spec/'));

  if (specChanges.length > 0 && codeChanges.length > 0) {
    // 人类决策：这是 Spec 驱动的变更还是临时 bug 修复？
    const shouldUpdateSpec = await promptUser(`
      代码和 Spec 都有变更。
      是否将代码变更同步回 Spec？
      这会确保 Spec 是真正的 SSOT。
    `);

    if (shouldUpdateSpec) {
      await syncCodeToSpec(codeChanges, specChanges);
    }
  }
}
```

---

## 7. 测试策略

### 7.1 测试分层

```
┌─────────────────────────────────────────────────────────────┐
│                    测试金字塔                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                         E2E Tests                           │
│                    (Playwright + User Stories)              │
│                           ▲                                 │
│                          /|\                                │
│                         / | \                               │
│                        /  |  \                              │
│                       /   |   \                             │
│                      /    |    \                            │
│                   Integration Tests                          │
│                (Vitest + Supertest + DB)                    │
│                           ▲                                 │
│                          /|\                                │
│                         / | \                               │
│                        /  |  \                              │
│                       /   |   \                             │
│                    Contract Tests                           │
│               (API Schema 验证)                              │
│                           ▲                                 │
│                          /|\                                │
│                         / | \                               │
│                        /  |  \                              │
│                       /   |   \                             │
│                   Unit Tests                                │
│               (Vitest + Mock + SWC)                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 7.2 各层测试职责

| 测试层 | 框架 | 执行时机 | 产出 |
|--------|------|----------|------|
| **Unit Tests** | Vitest + SWC | 每次 PR | `*.spec.ts` |
| **Contract Tests** | Pact / 自定义 | 每次 PR | API 契约验证 |
| **Integration Tests** | Vitest + SuperTest | 每次 PR | 数据库操作验证 |
| **E2E Tests** | Playwright | 每次合并到 main | 完整用户流程验证 |

### 7.3 测试代码生成（Test Agent）

```typescript
// spec/domain/auth/v1/test-generation.ts
// Test Agent 根据 Spec 自动生成测试

export const testGenerationPrompt = `
# 任务
根据以下 Spec 为 {feature} 功能生成测试代码。

## Spec
{spec_content}

## 技术栈
- 测试框架：Vitest
- HTTP 测试：Supertest
- 数据库：Prisma + Testcontainers

## 输出要求
1. 每个 acceptance criteria 至少 1 个测试用例
2. 正常路径 + 异常路径都要覆盖
3. 使用 describe/it 结构化组织
4. 必须有清晰的断言消息

## 测试模板
\`\`\`typescript
import { describe, it, expect, beforeAll, afterAll } from 'vitest';
import supertest from 'supertest';
import { app } from '../../../src/app';
import { prisma } from '../../../src/infrastructure/database/prisma';

describe('Feature: {feature_name}', () => {
  // Test cases derived from acceptance criteria
});
\`\`\`
`;
```

### 7.4 Vitest 配置示例

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config';
import swc from 'unplugin-swc-vite';

export default defineConfig({
  plugins: [
    swc.vite({
      module: { type: 'module' },
    }),
  ],
  test: {
    globals: true,
    environment: 'node',
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      include: ['src/**/*.ts'],
      exclude: ['src/**/*.d.ts'],
    },
    setupFiles: ['./vitest.setup.ts'],
    pool: 'forks',
    poolOptions: {
      forks: {
        singleFork: true,
      },
    },
  },
});
```

### 7.5 黑盒测试（Playwright）

```typescript
// test/e2e/user-login.spec.ts
// 基于 User Stories 编写，不依赖内部实现

import { test, expect } from '@playwright/test';

test.describe('User Authentication', () => {
  test('AC-001: Successful login with valid credentials', async ({ page }) => {
    // Given: I am on the login page
    await page.goto('/login');

    // When: I enter valid email and password
    await page.fill('[name="email"]', 'test@example.com');
    await page.fill('[name="password"]', 'validPassword123');
    await page.click('[type="submit"]');

    // Then: I should be redirected to dashboard
    await expect(page).toHaveURL('/dashboard');
    await expect(page.locator('.user-name')).toContainText('test@example.com');
  });

  test('AC-002: Failed login with wrong password', async ({ page }) => {
    await page.goto('/login');
    await page.fill('[name="email"]', 'test@example.com');
    await page.fill('[name="password"]', 'wrongPassword');
    await page.click('[type="submit"]');

    // Then: I should see error message
    await expect(page.locator('.error-message')).toContainText('Invalid credentials');
    await expect(page).toHaveURL('/login');
  });
});
```

### 7.6 测试与 Spec 的追溯性

```yaml
# spec/domain/auth/v1/spec.yaml 中的测试追溯
test_cases:
  - id: TC-001
    name: valid login
    ac_id: AC-001              # 追溯到验收标准
    spec_section: "#login-api"  # 追溯到 Spec 章节
    generated_from: Test Agent
    test_file: test/e2e/auth-login.spec.ts
    test_line: 10
```

---

## 8. 线上错误跟踪

### 8.1 错误分类

| 类型 | 来源 | 处理方式 |
|------|------|----------|
| **代码 Bug** | 实现错误 | Debug Agent 修复 + 回归测试 |
| **Spec Bug** | 规格错误 | 更新 Spec + 重新生成 |
| **环境问题** | 基础设施 | 告警 + 人工介入 |
| **性能问题** | 资源不足 | 告警 + 自动扩缩容 |

### 8.2 错误跟踪集成

```typescript
// src/infrastructure/error tracking/error-handler.ts
import { Sentry } from '@sentry/node';
import { NodeTracerProvider } from '@opentelemetry/sdk-trace-node';

export function setupErrorTracking() {
  // Sentry 集成
  Sentry.init({
    dsn: process.env.SENTRY_DSN,
    tracesSampleRate: 1.0,
    environment: process.env.NODE_ENV,
  });

  // OpenTelemetry 集成
  const provider = new NodeTracerProvider();
  provider.register();

  // 错误自动上报
  process.on('uncaughtException', (error) => {
    Sentry.captureException(error);
    // 触发告警
    triggerAlert('critical', error.message);
  });
}
```

### 8.3 错误自动分类

```typescript
// tools/error-classifier.ts
export async function classifyError(error: Error, context: ErrorContext) {
  const classification = await ai.analyze(`
    分析以下错误，判断类型并建议修复方案：

    Error: ${error.message}
    Stack: ${error.stack}
    Context: ${JSON.stringify(context)}

    类型选项：
    1. CODE_BUG - 代码实现错误
    2. SPEC_BUG - 规格定义错误
    3. ENVIRONMENT - 环境/基础设施问题
    4. PERFORMANCE - 性能问题
  `);

  return classification;
}
```

---

## 9. 自动化错误处理流程

### 9.1 完整自动化闭环

```
                    ┌─────────────────────────────────────────┐
                    │           线上环境监控                   │
                    │  (Sentry + OpenTelemetry + Alerts)      │
                    └──────────────────┬──────────────────────┘
                                       │
                                       ▼
                    ┌─────────────────────────────────────────┐
                    │           错误检测与分类                  │
                    │  Error Classifier Agent                   │
                    └──────────────────┬──────────────────────┘
                                       │
                    ┌──────────────────┼──────────────────┐
                    │                  │                  │
                    ▼                  ▼                  ▼
            ┌───────────┐      ┌───────────┐      ┌───────────┐
            │ CODE_BUG  │      │ SPEC_BUG │      │  ENV     │
            └─────┬─────┘      └─────┬─────┘      └─────┬─────┘
                  │                  │                  │
                  ▼                  ▼                  ▼
          ┌───────────┐      ┌───────────┐      ┌───────────┐
          │ Debug     │      │ Spec     │      │ DevOps   │
          │ Agent     │      │ Update   │      │ Team     │
          │ 修复代码   │      │ Agent    │      │ 介入      │
          └─────┬─────┘      └─────┬─────┘      └───────────┘
                │                  │
                ▼                  ▼
          ┌───────────┐      ┌───────────┐
          │ 创建 PR   │      │ 更新 Spec │
          │ + Review │      │ + Review  │
          └─────┬─────┘      └─────┬─────┘
                │                  │
                └────────┬─────────┘
                         ▼
                ┌───────────────────┐
                │    CI Pipeline    │
                │ (测试 + 部署验证)   │
                └─────────┬─────────┘
                          │
              ┌───────────┴───────────┐
              │                       │
              ▼                       ▼
        ┌───────────┐          ┌───────────┐
        │   通过    │          │   失败    │
        │  自动合并 │          │ Debug修复 │
        └───────────┘          └───────────┘
```

### 9.2 Agent 任务定义

| Agent | 触发条件 | 任务 | 输出 |
|-------|----------|------|------|
| **Monitor Agent** | 告警触发 | 收集错误上下文 | 错误报告 |
| **Classifier Agent** | 错误报告 | 分类错误类型 | 分类结果 + 修复建议 |
| **Debug Agent** | CODE_BUG | 定位 + 修复 | PR + 代码修复 |
| **Spec Agent** | SPEC_BUG | 更新 Spec | PR + Spec 更新 |
| **Review Agent** | PR 创建 | Code Review | Review 报告 |
| **Deploy Agent** | CI 通过 | 部署到环境 | 部署确认 |

### 9.3 自动化实现示例

```typescript
// tools/automated-error-loop.ts
export async function handleProductionError(error: Error, alertId: string) {
  // 1. 收集上下文
  const context = await ErrorCollector.collect(error, {
    include: ['stack', 'request', 'user', 'database', 'cache'],
  });

  // 2. 分类错误
  const classification = await classifyError(error, context);

  if (classification.type === 'CODE_BUG') {
    // 3. Debug Agent 尝试修复
    const fix = await DebugAgent.fix(error, context);

    // 4. 创建 PR
    await createPullRequest({
      title: `fix: resolve ${classification.issueType}`,
      description: `## Error\n${error.message}\n\n## Fix\n${fix.explanation}`,
      changes: fix.codeChanges,
    });

    // 5. 触发 CI
    await triggerCI();

    // 6. Code Review
    await ReviewAgent.review(prId);
  } else if (classification.type === 'SPEC_BUG') {
    // Spec 错误需要人工介入
    await notifyHuman('Spec 需要更新', classification);
  }
}
```

### 9.4 CI/CD Pipeline 集成

```yaml
# .github/workflows/auto-fix.yml
name: Auto Fix Pipeline

on:
  issue_comment:
    types: [created]

jobs:
  classify-and-fix:
    if: github.event.comment.body == '/fix'
    runs-on: ubuntu-latest
    steps:
      - name: Collect error context
        run: |
          gh api repos/{owner}/{repo}/issues/${{ github.event.issue.number }}/comments

      - name: Run Debug Agent
        id: debug
        run: |
          # Debug Agent 分析错误并生成修复
          echo "debug_output=${{ steps.debug.outputs.result }}" >> $GITHUB_OUTPUT

      - name: Create Fix PR
        if: steps.debug.outputs.success == 'true'
        run: |
          gh pr create \
            --title "fix: auto-resolve issue #${{ github.event.issue.number }}" \
            --body "Automated fix for issue"

      - name: Notify on failure
        if: steps.debug.outputs.success == 'false'
        run: |
          gh issue comment ${{ github.event.issue.number }} \
            --body "需要人工介入：${{ steps.debug.outputs.reason }}"
```

---

## 附录：关键检查清单

### Spec 编写检查清单

- [ ] 有明确的用户故事
- [ ] 每个用户故事有对应的验收标准
- [ ] 所有 API 有完整的 request/response schema
- [ ] 所有 entity 有完整的字段定义
- [ ] 测试用例覆盖所有验收标准
- [ ] 已标注 assumptions 和 open questions
- [ ] 通过 Zod Schema 校验

### Spec Review 检查清单

- [ ] 业务逻辑正确无歧义
- [ ] 技术实现可行
- [ ] 与现有系统兼容
- [ ] 命名规范统一
- [ ] 约束条件可达成
- [ ] 测试覆盖率 ≥ 80%
- [ ] 无未解决的 open questions

### 代码生成检查清单

- [ ] 遵循项目架构模式（DDD + Hexagonal）
- [ ] 遵循 Nest.js 模块化结构
- [ ] 使用 Prisma 正确操作数据库
- [ ] 错误处理完整
- [ ] 有完整的类型注解
- [ ] 通过 lint 检查
- [ ] 通过 type 检查
- [ ] 有单元测试覆盖

### 部署检查清单

- [ ] 所有测试通过
- [ ] 覆盖率未下降
- [ ] API 文档已更新
- [ ] ChangeLog 已记录
- [ ] 监控告警已配置
