---
name: ai-trends
description: 研究指定时间范围内的 AI 重要进展，产出高信噪比、可追溯来源的 AI 前沿动态简报。通过分层漏斗流程控制检索与验证成本，保证每个结论都可回溯到原始来源。
disable-model-invocation: true
allowed-tools: Agent, WebSearch, WebFetch, Bash, Write, Read, Edit
---

# AI 前沿动态简报

## 0. 参数与铁律

### 参数

| 参数 | 说明 | 默认值 |
| ---- | ---- | ------ |
| `query_time_range` | 检索时间范围 | `last 2 weeks` |
| `mode` | 运行档位：`fast`、`standard`、`deep` | `standard` |
| `output_path` | 报告输出路径 | `./ai-trends/YYYY-MM-DD.md` |

`last 2 weeks` 指从两周前的周一开始到当前日期。档位决定预算，`standard` 之外的档位只在用户明确要求时使用。

### 铁律（任何情况下不得违反）

1. **禁止嵌套代理**：任何子代理都不得再派生子代理，也不得再调用 Agent 工具。
2. **禁止凑数**：没有足够证据的概念就不写，宁可本期概念数为 0。
3. **单一候选池**：所有代理读取同一份 `deduped.jsonl` 与 `evidence.jsonl`，不得各自另建候选集。
4. **预算优先**：达到预算 80% 时停止扩展搜索，只完成已选条目；达到 100% 时基于现有证据交付报告。
5. **失败不重跑**：单个来源或条目失败只影响该条目，不得重跑整批。
6. **证据唯一真源**：报告中每条数据都必须能对应 `evidence.jsonl` 中的一条记录。
7. **禁止读取运行中代理的原始记录**：只用完成通知获取结果，不得对运行中的代理调用会返回原始转录的工具。

### 预算来源

`.claude/skills/ai-trends/budgets.json` 是预算唯一真源。执行前读取 `modes[mode]`，并把关键上限写入本次工作计划。

---

## 1. 工作区与证据库

每次执行使用独立工作目录，所有中间产物落盘，避免多代理重复抓取：

```text
generated/ai-trends/.work/YYYY-MM-DD/
├── candidates.jsonl      # 采集原始候选
├── deduped.jsonl         # 合并后的候选池
├── selected.json         # 筛选代理产出的入选清单
├── evidence.jsonl        # 已核验证据（唯一事实来源）
├── failures.jsonl        # 失败与缺口
└── metrics.json          # 实际消耗指标
```

缓存目录：`generated/ai-trends/.cache/`，按 `budgets.json` 的 `cache_ttl_hours` 复用，避免重复抓取。

证据对象结构见 `.claude/skills/ai-trends/schemas/evidence.schema.json`，用脚本校验：

```bash
python3 .claude/skills/ai-trends/scripts/evidence.py validate --file <工作目录>/evidence.jsonl
```

---

## 2. 第一步：确定性采集

优先使用脚本抓取已知来源，**不要用搜索引擎发现已知站点**。

```bash
python3 .claude/skills/ai-trends/scripts/collect.py \
  --sources .claude/skills/ai-trends/sources.json \
  --since YYYY-MM-DD --until YYYY-MM-DD \
  --out <工作目录>/candidates.jsonl \
  --stats-out <工作目录>/collect-stats.json \
  --cache generated/ai-trends/.cache
```

规则：

- 默认只启用 A 级来源；B 级来源按预算选取一组并逐周轮换；C 级来源只在出现明确缺口时手工抓取。
- 脚本失败时，先看 `collect-stats.json`，对失败的 A 级来源用 WebFetch 补抓一次，失败即记录到 `failures.jsonl` 并跳过。
- A 级来源若在时间窗内没有产出任何带日期条目，说明索引页未暴露日期，必须对该来源用 WebFetch 补抓一次再判定为空。
- 脚本默认保留 A 级来源的无日期条目（标记 `date_confidence=unknown`），交由筛选代理判断，避免 JS 渲染的索引页漏掉重大公告；B 级无日期条目默认丢弃。
- GitHub 榜单的 Stars 与增量必须来自 `scripts/collect.py` 或 GitHub API 实测，禁止凭记忆、截图或估算填写。
- 需要额外保留 B 级无日期条目时显式加 `--include-undated`，并在报告中说明其日期不确定。
- 采集后必须运行去重：

```bash
python3 .claude/skills/ai-trends/scripts/dedup.py \
  --in <工作目录>/candidates.jsonl --out <工作目录>/deduped.jsonl \
  --stats-out <工作目录>/dedup-stats.json
```

### 缺口查询

只有在脚本采集之后仍存在明确缺口时才使用 WebSearch：

- 查询条目来自 `references/search-queries.md` 的「缺口查询集」；
- 数量不超过 `max_discovery_queries`；
- 每次查询必须写明要填补的缺口，重复查询同一站点视为浪费；
- 优先用 `site:` 定向到已知域名，或直接抓取该域名的索引页。

---

## 3. 第二步：统一筛选

**只允许一个筛选代理**，且该代理不得使用 Agent 工具。

筛选代理读取 `deduped.jsonl`，按四个维度打分：

| 维度 | 判断标准 |
| ---- | -------- |
| 影响力 | 是否影响行业格局、能力边界或监管方向 |
| 新颖性 | 是否为本期新事件，而非旧闻重复 |
| 证据可得性 | 是否存在可直接引用的原始来源 |
| 相关性 | 是否属于本简报覆盖的技术与产业主线 |

产出 `selected.json`：

```json
{
  "events": [
    {
      "id": "候选 ID",
      "title": "标题",
      "published_at": "YYYY-MM-DD",
      "kind": "model|research|product|company|policy|safety|community|ecosystem|hardware",
      "why": "入选理由",
      "verification_need": "routine|extraordinary",
      "source_urls": ["已知线索链接"]
    }
  ],
  "concept_candidates": [
    {"term": "术语", "evidence_urls": ["链接"], "note": "为什么可能是新概念"}
  ]
}
```

上限：`max_verified_events` 条事件、`max_concepts` 个概念。筛选代理必须同时给出被淘汰的重要候选及原因，避免下一阶段重新拾取。

---

## 4. 第三步：按证据需求验证

验证强度由事实类型决定，**不是每个事实都需要多源交叉**。

| 事实类型 | 验证要求 | 允许来源数 |
| -------- | -------- | ----------: |
| 官方功能、定价、发布日期 | 官方原文 | 1 |
| 厂商基准与性能数字 | 官方原文，标注“官方自报” | 1 |
| 论文方法与结果 | 原论文，标注预印本或同行评审 | 1 |
| 融资、并购、监管、重大事故 | 原始文件＋1 个独立可靠来源 | 2 |
| 异常、颠覆性或争议主张 | 至少 2 个独立来源，并写明争议 | 2 |
| 新兴概念起源 | 原始提出者＋1 个独立采用证据 | 2 |

执行方式：

- 启动 **1 个事实验证代理**，覆盖 `selected.json` 中的全部事件，逐条写入 `evidence.jsonl`；
- 启动 **0 至 `max_concepts` 个概念验证代理**，每个概念一个代理，规则见 `references/concept-verification.md`；
- 代理总数不得超过 `max_agents`，且不得嵌套；
- 每个代理的超时为 `agent_timeout_seconds`，超时后用 `TaskStop` 终止，记录失败并继续其余条目；
- 每完成一条证据立即落盘，避免因中断丢失结果。

代理输出要求：只返回条目 ID、成功／失败与计数；**不得在回复中重复完整报告**，细节一律写入 `evidence.jsonl`。

---

## 5. 第四步：可靠性标注

- 来源层级：官方实验室公告与原始文件 ＞ 同行评审论文 ＞ 权威科技媒体 ＞ 分析师评论 ＞ 聚合博客。
- 每条表格条目都要带来源链接；每条数据都要能回溯到 `evidence.jsonl`。
- 聚合博客不得作为唯一来源。
- 无法找到佐证的结论加 `【未经核实】`；权威来源存在分歧时加 `【有争议】` 并同时给出不同观点。
- 区分“已宣布”“已发布”“预印本”“独立复现”，厂商自报数据一律显式标注。
- 只有营销口号、无可核验技术实质的公告直接丢弃，不进入报告。

---

## 6. 第五步：撰写与交付

1. 读取 `references/output-format.md` 的模板，按证据库生成报告。
2. 只写证据库中存在的条目；需要补充时回到第四步，不得凭空补写。
3. 概念数量可以为 0；不为凑数降低证据标准。
4. 链接检查（只检查报告中实际引用的链接）：

```bash
python3 .claude/skills/ai-trends/scripts/check_links.py \
  --file <报告路径> --cache generated/ai-trends/.cache \
  --out <工作目录>/link-check.json
```

1. 格式检查必须通过：

```bash
npx --yes markdownlint-cli <报告路径>
```

1. 报告末尾附上本次实际消耗：检索次数、抓取页面数、候选与入选数量、证据来源分布、失败项与覆盖缺口。

### 输出路径

默认写入仓库内已跟踪的 `./ai-trends/YYYY-MM-DD.md`（`date +%Y-%m-%d` 获取日期，必要时 `mkdir -p`）。该目录随版本库保存，避免交付物因 `generated/` 被清理而丢失；工作文件与缓存仍放在 `generated/ai-trends/` 下。`output_path` 指定时以其为准。完成后告知用户文件路径与覆盖缺口。

---

## 7. 失败与降级

| 情况 | 处理 |
| ---- | ---- |
| 单个来源抓取失败 | 用 WebFetch 补抓一次，仍失败则记录到 `failures.jsonl` 并继续 |
| 同一域名连续失败达到 `failure_circuit_breaker` | 跳过该域名剩余请求 |
| 子代理超时 | 终止该代理，保留已完成证据，继续其余条目 |
| 概念证据不足 | 放弃该概念，概念数可以少于上限 |
| 达到预算 100% | 立即基于现有证据生成报告，并在覆盖缺口中说明未覆盖范围 |
| 采集结果为空 | 报告“本期无可靠新增”，不得编造 |

降级时的报告必须显式列出未覆盖的来源与原因，而不是静默省略。

---

## 8. 数据源维护（不在常规运行内）

数据源分层、轮换与清理规则见 `references/data-sources.md`。新发现的权威来源应先记入报告的「新发现的数据源」一节，再由人工复核后并入 `sources.json` 与 `references/data-sources.md`。常规运行不做来源清理，避免把预算花在低价值维护上。

---

## 附录：常用命令

```bash
# 采集（默认启用 A、B 层；只跑 A 层用 --tiers A）
python3 .claude/skills/ai-trends/scripts/collect.py --sources .claude/skills/ai-trends/sources.json \
  --since 2026-11-09 --until 2026-11-24 --out <工作目录>/candidates.jsonl \
  --stats-out <工作目录>/collect-stats.json --cache generated/ai-trends/.cache --tiers A,B

# 去重
python3 .claude/skills/ai-trends/scripts/dedup.py --in <工作目录>/candidates.jsonl --out <工作目录>/deduped.jsonl

# 证据校验与统计
python3 .claude/skills/ai-trends/scripts/evidence.py validate --file <工作目录>/evidence.jsonl
python3 .claude/skills/ai-trends/scripts/evidence.py summary --file <工作目录>/evidence.jsonl

# 链接检查与格式检查
python3 .claude/skills/ai-trends/scripts/check_links.py --file <报告路径> --cache generated/ai-trends/.cache
npx --yes markdownlint-cli <报告路径>
```
