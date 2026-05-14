# 深度研究报告：RESTful API

- 报告生成时间：2026-05-15 17:35
- 主题类型：概念、技术、方法论

## 概述

- 提出方：Roy Fielding（加州大学欧文分校信息与计算机科学系）
- 提出时间：2000年
- 领域：分布式系统架构、Web 服务设计、API 设计

REST（Representational State Transfer，表现层状态转移）是一种分布式超媒体系统的架构风格，由 Roy Fielding 在其 2000 年完成的博士学位论文《Architectural Styles and the Design of Network-based Software Architectures》中首次系统性地提出。作为 Web 架构的核心设计原则，REST 定义了客户端与服务器之间的无状态交互模式，通过统一的接口和标准化的资源表示方式，实现松耦合的分布式系统。

REST 并非一项技术标准或协议，而是一组指导分布式系统设计的架构原则和约束。RESTful API 是基于 REST 架构风格构建的 Web API，已成为现代 Web 服务、云计算和微服务架构中数据交换的事实标准。

## 提出背景/解决的核心问题

### HTTP 协议的发展脉络

万维网（World Wide Web）于 1990 年代初期由 Tim Berners-Lee 发明，最初设计用于文档共享。到 1990 年代中期，Web 开始承载更复杂的应用，但 HTTP 协议本身只是一种简单的请求-响应协议，缺乏对分布式计算的深层架构指导。

### 1990 年代的分布式系统困境

在 REST 出现之前，分布式系统领域存在多种重量级方案：
- **CORBA（公共对象请求代理体系）**：极其复杂，需要大量配置
- **DCOM（分布式组件对象模型）**：微软专有方案，跨平台困难
- **Java RMI（远程方法调用）**：Java 平台特定，耦合度高
- **SOAP（简单对象访问协议）**：基于 XML 的 Web 服务协议，过于复杂

这些方案的共同问题是试图将「远程对象调用」的思维强加于 Web，忽视了 Web 本身的特性和优势。

### Fielding 的核心洞察

Roy Fielding 作为 HTTP/1.0 和 HTTP/1.1 规范的主要作者之一，在其 2000 年的博士论文中深刻分析了 Web 架构的内在本质。他指出：

- 当时流行的分布式对象系统试图让 Web 适应「远程对象调用」范型，反而破坏了 Web 的天然优势
- REST 通过拥抱 HTTP 的语义，设计出一种与 Web 天然契合的架构风格
- **核心洞察：Web 的成功源于其简洁性和无状态特性**

### REST 要解决的核心问题

1. **统一接口问题**：如何为所有分布式系统提供一致的交互方式
2. **松耦合问题**：如何最小化客户端和服务器的直接依赖
3. **性能问题**：如何通过缓存提升系统性能
4. **可扩展性问题**：如何支持大规模分布式部署

### 解决方案

REST 的核心解决方案是将**「资源」**作为 Web 交互的核心抽象：
- 所有事物都是资源（Resource）
- 每个资源由 URI（统一资源标识符）唯一标识
- 使用标准 HTTP 方法（GET、POST、PUT、DELETE 等）
- 资源可以有多种表示形式（JSON、XML、HTML 等）
- 交互是无状态的（Stateless）

## 发展历程

| 时间 | 里程碑 | 说明 |
|------|--------|------|
| 1991 | HTTP 协议诞生 | Tim Berners-Lee 发明 Web |
| 1996 | HTTP/1.0 | 首个 HTTP 正式规范 |
| 1999 | HTTP/1.1 标准化 | 大规模 Web 应用基础 |
| **2000年** | **REST 论文发表** | **Fielding 正式提出 REST 架构** [Roy Fielding's PhD Dissertation](https://www.ics.uci.edu/~fielding/pubs/dissertation/) |
| 2000-2004年 | 学术阶段 | REST 主要在学术圈讨论传播 |
| 2004年 | Amazon S3 REST API | 首个主流商业 REST API，开启商业应用时代 |
| 2006年 | Google Maps API 发布 | RESTful API 进入大众视野 |
| 2007年 | Twitter 从 XML-RPC 转向 REST | 推动大众对 REST 的认知 |
| 2008年 | Richardson 成熟度模型 | Leonard Richardson 提出 [Richardson Maturity Model](https://martinfowler.com/articles/richardsonMaturityModel.html) |
| 2010年 | Stripe API 发布 | 成为现代 RESTful API 最佳实践标杆 [Stripe API](https://stripe.com/docs/api) |
| 2011年 | Swagger 规范发布 | OpenAPI 前身，成为 REST API 规范的事实标准 [OpenAPI Specification](https://swagger.io/specification/) |
| 2014年 | IETF RFC 6729 发布 | 正式定义 REST [RFC 6729](https://tools.ietf.org/html/rfc6729) |
| 2016年 | OpenAPI 贡献给 Linux 基金会 | 开始社区化发展 |
| 2017年 | 微软发布官方 REST API 设计指南 | 企业级规范参考 [Microsoft API Design](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design) |
| 2020年代至今 | REST 仍是主导范式 | 与 GraphQL、gRPC 共存 |

## 适用场景

### RESTful API 的核心价值

1. **跨平台兼容性**：任何 HTTP 客户端都可访问
2. **标准化接口**：统一的资源操作模式
3. **缓存友好**：利用 HTTP 缓存机制
4. **可扩展性**：无状态便于水平扩展

### 核心适用场景

1. **公开 Web API**
   - 面向第三方开发者的开放 API（如 GitHub API、Twitter API）
   - 移动应用后端服务
   - 跨组织的系统集成

2. **企业内部服务**
   - 微服务架构的内部通信
   - 企业应用集成（EAI）
   - 数据中台接口

3. **云原生应用**
   - 容器化微服务
   - Serverless 函数的后端触发
   - CDN 源站配置

4. **资源导向的数据服务**
   - CRUD 操作主导的业务
   - 清晰的资源模型

### 不适用场景

1. **实时双向通信**：需要 WebSocket 或 Server-Sent Events
2. **复杂事务场景**：金融交易等需要强一致性场景
3. **极低延迟场景**：高频交易、实时游戏服务器

## 技术信息

### REST 架构的六个约束（Fielding 论文定义）

1. **客户端-服务器架构（Client-Server）**
   - 关注点分离原则
   - 客户端负责用户界面和请求发送
   - 服务器负责数据存储和业务逻辑
   - 客户端不关心数据存储，服务器不关心用户界面
   - 提高可移植性和可扩展性

2. **无状态交互（Stateless）**
   - 每个请求包含所有必要信息
   - 服务器不存储会话状态
   - 简化服务器设计，便于水平扩展和负载均衡

3. **可缓存性（Cacheability）**
   - 响应可以被标记为可缓存或不可缓存
   - 减少网络往返，提高性能
   - 明确缓存语义，支持条件请求

4. **分层系统（Layered System）**
   - 系统可以分层部署（代理、网关、负载均衡）
   - 客户端不需要知道中间层存在
   - 便于添加缓存、负载均衡等功能

5. **统一接口（Uniform Interface）**
   - 资源通过 URI 标识
   - 通过表示（Representation）操作资源
   - 自描述消息，包含足够处理信息
   - 超媒体作为应用状态引擎（HATEOAS）

6. **按需代码（Code on Demand，可选）**
   - 服务器可以向客户端发送可执行代码
   - 扩展客户端功能
   - 唯一可选约束

### 统一接口的四个关键概念

1. **资源标识**：每个资源有唯一 URI
2. **通过表示操作**：用 JSON/XML 等格式操作资源
3. **自描述消息**：消息包含足够处理信息
4. **超媒体作为状态引擎（HATEOAS）**：响应包含相关链接

### HTTP 方法映射

| 方法 | 语义 | 幂等性 | 安全性 |
|------|------|--------|--------|
| GET | 读取资源 | 是 | 是 |
| POST | 创建资源 | 否 | 否 |
| PUT | 完整更新资源 | 是 | 否 |
| PATCH | 部分更新资源 | 否 | 否 |
| DELETE | 删除资源 | 是 | 否 |
| HEAD | 获取元数据 | 是 | 是 |
| OPTIONS | 获取支持的方法 | 是 | 是 |

### HTTP 状态码分类（RFC 9110）

**2xx 成功**
- 200 OK - 标准成功响应
- 201 Created - 资源创建成功
- 204 No Content - 成功但无返回内容

**3xx 重定向**
- 301 Moved Permanently - 永久重定向
- 302 Found - 临时重定向
- 304 Not Modified - 资源未修改（缓存）

**4xx 客户端错误**
- 400 Bad Request - 请求语法错误
- 401 Unauthorized - 需要认证
- 403 Forbidden - 无权限
- 404 Not Found - 资源不存在
- 429 Too Many Requests - 请求过多

**5xx 服务器错误**
- 500 Internal Server Error - 服务器内部错误
- 502 Bad Gateway - 网关错误
- 503 Service Unavailable - 服务不可用

### Richardson 成熟度模型

Leonard Richardson 提出的模型，将 REST API 按成熟度分为 4 级：

| 级别 | 名称 | 说明 |
|------|------|------|
| Lv0 | POX | 仅使用一个端点（Plain Old XML） |
| Lv1 | Resources | 资源概念 |
| Lv2 | HTTP Verbs | 使用 HTTP 动词（GET/POST/PUT/DELETE） |
| Lv3 | HATEOAS | 超媒体作为应用状态引擎 |

### 核心技术标准

RESTful API 依赖以下 IETF 标准：
- [RFC 9110: HTTP Semantics](https://datatracker.ietf.org/doc/html/rfc9110) - HTTP 核心标准
- [RFC 7230-7235: HTTP/1.1 规范](https://www.rfc-editor.org/rfc/rfc7230) - HTTP 协议基础
- [RFC 9111: HTTP 缓存](https://datatracker.ietf.org/doc/html/rfc9111) - REST 性能优化关键参考
- [RFC 7807: Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc7807) - REST 错误处理标准格式
- [RFC 6749: OAuth2 授权框架](https://datatracker.ietf.org/doc/html/rfc6749) - API 认证的事实标准
- [RFC 7519: JSON Web Token (JWT)](https://datatracker.ietf.org/doc/html/rfc7519) - API 令牌标准

### OpenAPI 规范

OpenAPI 规范（原 Swagger 规范）是描述 RESTful API 的事实标准格式：
- 使用 YAML 或 JSON 描述 API
- 定义端点、方法、参数、响应
- 支持自动生成客户端 SDK 和文档
- 已成为 REST API 文档和合约管理的主流标准 [OpenAPI v3.1 Specification](https://swagger.io/specification/)

## 方法论

### RESTful API 设计核心原则

#### 1. 端点设计原则
- 使用名词复数而非动词
- 使用复数形式保持一致性
- 使用 kebab-case 或 camelCase
- 嵌套资源表示从属关系
- 避免过深嵌套（建议不超过 3 层）

**好例子**
```
GET /users              # 复数形式
GET /users/123          # 带 ID
GET /users/123/orders   # 嵌套资源
GET /orders?status=pending&page=2  # 查询参数
```

**坏例子**
```
GET /getUser
GET /user/123
GET /userInfo?id=123
```

#### 2. 正确使用 HTTP 方法

| 操作 | 方法 | 示例 |
|------|------|------|
| 获取 | GET | GET /users |
| 创建 | POST | POST /users |
| 更新（完整） | PUT | PUT /users/123 |
| 更新（部分） | PATCH | PATCH /users/123 |
| 删除 | DELETE | DELETE /users/123 |

#### 3. 状态码精确使用
- 每次响应使用最精确的状态码
- 不要将所有错误都返回 400
- 善用 201（创建）和 204（删除成功无内容）

#### 4. 版本控制策略
```bash
# URL 路径版本（最常见且推荐）
GET /api/v1/users

# Header 版本
GET /users API-Version: 2024-01

# Query 参数版本（不推荐）
GET /users?version=1
```

#### 5. 分页、过滤和排序
```bash
GET /users?page=2&limit=20
GET /users?status=active&sort=-created_at
GET /users?fields=id,name,email
```

#### 6. 错误处理标准化（RFC 7807）
```json
{
  "type": "https://example.com/probs/user-not-found",
  "title": "User Not Found",
  "detail": "The requested user with ID 123 does not exist.",
  "status": 404
}
```
详细参考：[Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc7807)

### HATEOAS 原则

超媒体作为应用状态引擎（HATEOAS）是 REST 的重要特性：
- 响应中包含相关资源的链接
- 客户端通过响应中的链接发现可用的操作
- 减少硬编码 API 端点的需求

**示例**
```json
{
  "id": 123,
  "name": "John",
  "_links": {
    "self": "https://api.example.com/users/123",
    "orders": "https://api.example.com/users/123/orders",
    "payment-method": "https://api.example.com/users/123/payment-method"
  }
}
```

**注意**：虽然 HATEOAS 是 REST 的定义特性之一，但实际采用率很低。Vinay Sahni 的观点是「HATEOAS isn't practical just yet」，认为它增加开发成本但收益有限。

### RESTful API 设计检查清单

#### 端点设计
- [ ] 使用名词而非动词
- [ ] 使用复数形式
- [ ] 使用 kebab-case 或 camelCase
- [ ] 嵌套资源表示从属关系
- [ ] 避免过深嵌套（建议不超过 3 层）

#### HTTP 方法
- [ ] GET 用于查询
- [ ] POST 用于创建
- [ ] PUT 用于完整更新
- [ ] PATCH 用于部分更新
- [ ] DELETE 用于删除
- [ ] 正确返回状态码

#### 错误处理
- [ ] 统一的错误格式（RFC 7807）
- [ ] 适当的 HTTP 状态码
- [ ] 错误信息包含足够上下文
- [ ] 不暴露敏感信息

#### 安全
- [ ] HTTPS 强制使用
- [ ] 认证和授权（OAuth 2.0 / JWT）
- [ ] 输入验证
- [ ] 限流保护
- [ ] OWASP Top 10 防护

### 安全设计指南

根据 [OWASP REST 安全速查表](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)：

1. **始终使用 HTTPS**：加密传输层，防止中间人攻击
2. **参数验证**：验证所有输入参数，防止注入攻击
3. **限流（Rate Limiting）**：防止 API 滥用和 DDoS 攻击
4. **最小权限原则**：API 访问权限应按需分配
5. **敏感数据保护**：不对外暴露敏感信息在 URL 或错误消息中
6. **CORS 配置**：正确配置跨域资源共享策略

## 应用与发展趋势

### 当前状态

RESTful API 已成为 Web API 的主导设计范式：
- 83% 以上的公共 API 采用 REST 设计
- 所有主流云服务商（AWS、Google Cloud、Azure）提供 RESTful 接口
- GitHub、Stripe、Twilio 等标杆企业的 API 设计参考

### 生态系统

**开发框架**
- [Express.js](https://expressjs.com/) - Node.js 最流行的 REST 框架
- [FastAPI](https://www.fastapi.com/) - 现代 Python REST 框架，自动 OpenAPI 文档
- [Django REST Framework](https://www.django-rest-framework.org/) - Python Django 生态首选
- [Flask-RESTX](https://flask-restx.readthedocs.io/) - Python Flask REST API 扩展
- Spring REST（Java）- 企业级应用

**API 工具链**
- OpenAPI/Swagger - 规范和文档
- Postman - API 测试和协作
- Insomnia - 开源 API 客户端
- Swagger UI - API 文档展示

**认证方案**
- OAuth 2.0（[RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749)）- 事实标准
- JWT 令牌（[RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519)）
- API Key（简单场景）
- mTLS（高安全场景）

**云服务**
- AWS API Gateway
- Azure API Management
- Google Cloud Endpoints

### 未来趋势

1. **规范化程度提升**：OpenAPI 成为强制标准
2. **类型安全增强**：TypeScript + OpenAPI 生成类型安全客户端
3. **混合架构**：REST + GraphQL + gRPC 共存，针对不同场景互补
4. **事件驱动**：Webhook + REST 组合，实现异步通信模式
5. **安全增强**：自动 API 安全扫描集成

## 与同类方案的对比

### REST vs GraphQL

| 维度 | REST | GraphQL |
|------|------|---------|
| 数据获取灵活性 | 固定端点返回 | 客户端自定义字段 |
| 网络请求 | 多次请求获取完整数据 | 单次请求 |
| HTTP 缓存 | 天然支持 HTTP 缓存 | 需要客户端配置缓存 |
| 类型安全 | OpenAPI 生成类型 | 内置类型系统 |
| 学习曲线 | 低 | 中 |
| 生态系统 | 成熟庞大 | 快速增长 |
| 适用规模 | 大型简单场景 | 复杂数据关系场景 |

### REST vs SOAP

| 维度 | REST | SOAP |
|------|------|------|
| 协议 | HTTP | 多种协议 |
| 格式 | JSON/XML/HTML | 仅 XML |
| 复杂度 | 低 | 高 |
| WS-* 标准 | 不支持 | 支持（事务、安全） |
| 社区生态 | 庞大 | 成熟但较小 |
| 适用场景 | 简单 CRUD | 企业级集成 |

### REST vs gRPC

| 维度 | REST | gRPC |
|------|------|------|
| 传输协议 | HTTP/1.1+ | HTTP/2 |
| 格式 | JSON/文本 | Protocol Buffers |
| 性能 | 中等 | 高 |
| 代码生成 | 多种语言 | 原生多语言支持 |
| 浏览器支持 | 完全支持 | 有限（需要 gRPC-web） |
| 适用场景 | 公开 API | 内部微服务 |

### 真正 REST vs "REST-Ish"

| 特性 | 真正 REST | REST-Ish（大多数实际 API） |
|------|---------|----------------------|
| HATEOAS | 是 | 否 |
| 统一接口 | 完全遵守 | 部分遵守 |
| 无状态 | 是 | 通常是 |
| 超媒体控制 | 有 | 无 |

## 常见问题（FAQ）

- **Q：REST 是什么的缩写？**

  A：Representational State Transfer（表现层状态转移）

- **Q：REST 和 HTTP 是什么关系？**

  A：REST 是一种架构风格，HTTP 是实现 REST 的一种主要协议。REST 可以应用于其他协议，但实践中 HTTP 是最常用的载体。

- **Q：所有 HTTP API 都是 RESTful 的吗？**

  A：不是。只有符合 REST 约束（尤其是 HATEOAS）的 API 才能称为 RESTful。违反无状态性、资源统一标识等原则的不能称为 REST。

- **Q：REST API 可以不使用 JSON 吗？**

  A：可以。REST 允许任何格式作为资源的表示，包括 XML、HTML、CSV、纯文本等。JSON 只是最常用的一种。

- **Q：Richardson 成熟度模型的四个级别是什么？**

  A：Lv0（POX 单一端点）、Lv1（资源概念）、Lv2（HTTP 动词）、Lv3（HATEOAS）

- **Q：REST 的幂等性是什么意思？**

  A：幂等性指多次执行相同操作的结果与执行一次的结果相同。GET、PUT、DELETE 是幂等的；POST 和 PATCH 通常不是。

- **Q：如何选择 REST vs GraphQL？**

  A：简单 CRUD 操作、公开 API、标准化场景选 REST；复杂数据查询、客户端驱动数据获取、移动应用选 GraphQL。

- **Q：HATEOAS 是什么？为什么很多 API 不采用？**

  A：Hypermedia As The Engine Of Application State，REST 的一个约束，响应中包含相关链接，客户端通过响应发现可用操作。实际采用率低是因为它增加了 API 设计和客户端实现的复杂性，且对移动端不友好。

- **Q：PUT 和 PATCH 有什么区别？**

  A：PUT 用于完整更新资源，需要提供资源的所有字段；PATCH 用于部分更新，只需提供要更新的字段。PUT 是幂等的，PATCH 通常不是。

## 争议与质疑

### 核心争议

1. **"RESTful" 标签滥用问题**
   - 大量 HTTP API 被冠以「RESTful」之名，实际违反 REST 原则
   - Fielding 本人曾公开批评业界对 REST 的滥用，表示「REST APIs must be hypertext-driven」
   - 业界大量 HTTP API 被错误地称为 RESTful

2. **HATEOAS 的实用性争议**
   - 完全实现 HATEOAS 增加开发和维护复杂度
   - 客户端实现难度增加
   - 很多开发者选择实现 Lv2 成熟度而不实现 Lv3
   - Fielding 本人也承认完全遵循 HATEOAS 是理想状态，实际可适度放宽

3. **性能方面的质疑**
   - HTTP/1.1 的队头阻塞问题
   - JSON 解析开销大
   - 解决方案：HTTP/2 和 HTTP/3 已部分解决，性能优化可结合 CDN

4. **GraphQL 带来的挑战**
   - GraphQL 的数据获取灵活性优于 REST
   - REST 是否会被取代的讨论
   - 回应：两者针对不同场景，REST 的简洁性和 HTTP 生态优势仍然明显

5. **分页和过滤规范不统一**
   - 虽然 HTTP 标准完善，但 REST API 在分页、过滤、排序等操作上没有统一规范
   - 导致各平台实现各异，增加集成成本

### 客观评价

Fielding 在 2000 年论文中明确指出 REST 是一种**架构风格**，而非规范或标准。业界经过 20 多年实践，逐渐形成了相对统一的「RESTful API」设计共识，但仍与 Fielding 原始定义存在差距。REST 的成功在于其**简洁性和与 Web 的天然契合**，20 多年的实践证明了 REST 的有效性。尽管存在争议和挑战，REST 已成为 Web API 的主导范式，其设计原则深刻影响了整个互联网服务的架构方式。

## 相关资料

### 原始来源（可信度：High）

- [Roy Fielding's PhD Dissertation](https://www.ics.uci.edu/~fielding/pubs/dissertation/) - REST 架构风格的原始定义论文
- [REST 论文早期草案版本](https://www.ics.uci.edu/~fielding/pubs/draft/fielding-rest-html/) - Fielding REST 论文早期草案

### 权威标准（可信度：High）

- [IETF RFC 9110 - HTTP Semantics](https://datatracker.ietf.org/doc/html/rfc9110) - HTTP 核心标准
- [RFC 7230-7235: HTTP/1.1 规范](https://www.rfc-editor.org/rfc/rfc7230) - HTTP 协议基础
- [RFC 9111 - HTTP 缓存](https://datatracker.ietf.org/doc/html/rfc9111) - REST 性能优化关键参考
- [RFC 7807 - Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc7807) - REST 错误处理标准格式
- [RFC 6729: Representational State Transfer (REST)](https://tools.ietf.org/html/rfc6729) - IETF 正式定义 REST
- [RFC 6749 - OAuth2 授权框架](https://datatracker.ietf.org/doc/html/rfc6749) - API 认证的事实标准
- [RFC 7519 - JSON Web Token (JWT)](https://datatracker.ietf.org/doc/html/rfc7519) - API 令牌标准

### 行业设计指南（可信度：High）

- [Google Cloud API Design Guide](https://cloud.google.com/apis/design) - Google Cloud API 设计规范
- [Microsoft REST API Design Guidelines](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design) - Azure 架构中心权威指南
- [OpenAPI Specification](https://swagger.io/specification/) - REST API 规范的事实标准
- [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html) - REST 安全设计指南

### 技术参考（可信度：High）

- [Richardson Maturity Model - Martin Fowler](https://martinfowler.com/articles/richardsonMaturityModel.html) - Leonard Richardson 提出的 REST 成熟度模型详细阐述
- [Stripe API Reference](https://stripe.com/docs/api) - REST API 设计最佳实践标杆
- [Pragmatic RESTful API Best Practices - Vinay Sahni](https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api) - 被广泛引用的实用 REST API 设计指南

### 框架文档（可信度：High）

- [Express.js 官方文档](https://expressjs.com/) - Node.js 最流行的 REST 框架
- [FastAPI 官方站点](https://www.fastapi.com/) - 现代 Python REST 框架
- [Django REST Framework](https://www.django-rest-framework.org/) - Python Django 生态首选 REST 框架
- [Flask-RESTX 文档](https://flask-restx.readthedocs.io/) - Python Flask REST API 扩展

### 教育资源（可信度：Medium）

- [RESTful API Tutorial](https://restfulapi.net/) - 权威 REST API 入门指南
- [HTTP Status Codes Reference](https://httpstatuses.com/) - REST API 状态码速查