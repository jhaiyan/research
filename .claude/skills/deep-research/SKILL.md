---
name: deep-research
description: |
  Deep research on IT technologies, software engineering concepts, AI terms, development tools, frameworks, libraries, protocols, methodologies, or technical products. Trigger this skill when the user asks to "deeply research", "深度研究", "thoroughly investigate", "系统调研", "comprehensively analyze a technology", "研究某项技术", "深度调研", or "技术调研" any software engineering, software development, AI, machine learning, DevOps, cloud computing, programming language, database, or IT-related term, concept, product, tool, or framework. Also applies when the user asks for a "技术报告", "技术白皮书", "technical report", "research report on X", or wants to understand a technical concept in depth. Use this skill for single-topic deep dives that require multi-source verification and structured synthesis.
disable-model-invocation: true
---

# Deep Research on IT Technologies

Perform rigorous, multi-agent deep research on a single IT/technology topic and produce a structured, cross-verified report.

## When to Use

Activate this skill when the user asks for in-depth research on any IT-related topic. Typical triggers:
- "深度研究一下 XXX"
- "thoroughly research the technology behind XXX"
- "帮我调研一下 XXX"
- "给我写一份关于 XXX 的技术报告"
- "What is XXX and how does it work in detail?"
- "深度分析一下 XXX 的原理和应用"
- "Compare XXX with alternatives in depth"
- User names a specific technology, framework, tool, protocol, concept, or product and asks for comprehensive information

## Phase 0: Cache Check & Iterative Multi-Agent Source Mining

Before launching research subagents, check the cache and if no valid cache exists, perform exhaustive source discovery.

### Step 0.0: Cache Check

1. **Check Cache File**: Attempt to read `.temp/deep-research-data-sources.md` from the project root.
2. **Cache Hit Detection**: If the file exists, search within it for the current topic (case-insensitive partial match on section header `## {topic}` or `## {kebab-case-topic}`).
3. **Timestamp Validation**: Extract the timestamp from the section header line (format: `## {topic} @ {YYYY-MM-DD}`). If the timestamp is older than 7 days (calculated from today), treat the cache as stale. If no timestamp exists, treat as stale.
4. **Cache Validation**: Verify the discovered sources section contains at least 5 entries. If fewer, treat as stale cache.
5. **Decision**:
   - If **valid cache found** (recent timestamp ≤7 days AND ≥5 entries) → Skip Phase 0.1–0.3 entirely. Load the cached sources as the master source list and proceed directly to **Phase 0.4: Research Dimension Definition**.
   - If **no cache or stale cache** → Proceed to Phase 0.1.

### Step 0.1: Topic Disambiguation & Initialization

1. **Disambiguation**: Identify the exact topic. If ambiguous (e.g., "React" could mean the library or the native framework), determine which one the user means or briefly ask for clarification.
2. **Topic Type Classification**: Classify the topic into one of the following types, as this determines research direction:
   - **Term/Concept**: An abstract idea, methodology, or named pattern. Focus on origin, definitions, evolution, proponents, and practical applications.
   - **Product/Tool**: A specific commercial or open-source product with a vendor. Focus on vendor, release history, features, pricing, competitive landscape, and user reviews.
   - **Technology/Framework**: A technical implementation with source code. Focus on architecture, API design, performance, ecosystem, and adoption.
   - **Ambiguous (may contain both)**: A term that could refer to both a concept and a product. When this occurs, research MUST clearly distinguish and separate:
     - Label each finding with its type: `[概念]` or `[产品]` or `[技术]`
     - Never conflate different types in the same section
     - Acknowledge the ambiguity explicitly in the report
3. **Initialize**: Create an empty master source list. Set `round = 1`, `max_rounds = 10`.
4. **Generate the output filename prefix** using kebab-case of the topic name.
5. **Identify Aliases**: If the topic is a named concept/term, identify:
   - Possible alternative names or spellings
   - Keywords that are NOT the topic (homonyms — products or concepts that share the same name but are different)
   - The original/coined spelling and capitalization of the term

### Step 0.2: Iterative Source Mining Loop

Run a loop with a hard maximum of **10 rounds**. In each round, launch **5 independent `general-purpose` agents** in parallel to mine for authoritative sources. The loop terminates early if a round discovers **zero new sources**.

**Round Execution:**

For each round `R` (from 1 to 10):

1. **Prepare Context**: Pass to all 5 subagents:
   - The research topic
   - The current master source list (URLs already discovered in rounds 1 to R-1)
   - Source category guidance (see below)
2. **Launch 5 Mining Subagents**: Each subagent independently discovers new sources using `WebSearch` and `WebFetch`.
3. **Collect & Deduplicate**: The main agent collects all outputs, deduplicates URLs, and checks accessibility (skip 404s).
4. **Update Master List**: Add all new, unique, accessible sources to the master list.
5. **Termination Check**:
   - If **zero new sources** were added this round → **break the loop immediately**.
   - Else if `R == 10` → stop (max rounds reached).
   - Else → increment `R` and continue.

**Instructions for each Source Mining Subagent:**

Your sole task is to discover as many **new, high-quality, authoritative sources** as possible for the given topic. You MUST NOT perform deep content analysis — only discover and catalog sources.

**Input you receive:**
- Research topic
- Known sources list (URLs already found in previous rounds)
- Source category guidance

**What you MUST do:**

1. **Origin-First Discovery (CRITICAL for Concept/Methodology Topics)**: When the topic is a concept, methodology, or named pattern:
   - First priority: discover the ORIGINAL publication that COINED or DEFINED the concept
   - Search for: "{topic} origin", "{topic} first proposed", "{topic} coined by", "{topic} defined as"
   - If multiple sources share the topic name as a product/framework name, identify which is the ORIGINAL concept source vs. a product that implements the concept
   - Track the semantic lineage: origin → propagation → implementations
   - **Date Verification (CRITICAL)**: For any source suspected to be the origin, MUST fetch the actual page and verify the publication date shown on the page — do NOT trust dates from search results or citations
   - **Semantic Confirmation (CRITICAL)**: Before marking a source as potential origin, read its content and confirm it discusses the **same domain/topic** as the research query (not a homonym with the same name but different meaning)
2. **Independent Search**: Use `WebSearch` to search for authoritative sources related to the topic. Do NOT rely solely on the known list — conduct your own independent searches with varied keywords, including the topic name combined with terms like:
   - "official documentation", "getting started", "tutorial"
   - "architecture", "design", "internals"
   - "best practices", "methodology", "comparison"
   - "GitHub", "source code", "changelog"
   - "criticism", "limitations", "vs alternative"
   - "Hacker News", "Reddit discussion", "Stack Overflow"
   - "paper", "whitepaper", "RFC", "specification"
   - "engineering blog", "case study", "performance benchmark"
3. **Source Categories to Cover**: Ensure you discover sources across ALL these categories:
   - **Official & Primary**: Official documentation, homepages, release notes, API references, READMEs
   - **Tech Media**: InfoQ, The New Stack, Ars Technica, TechCrunch, Wired, The Register
   - **Forums & Communities**: Stack Overflow, Hacker News, Reddit (r/programming, r/webdev, etc.), Dev.to, Medium, 知乎, V2EX
   - **Academic**: arXiv, ACM, IEEE, Google Scholar, DBLP, Semantic Scholar
   - **Engineering Blogs**: Personal technical blogs from practitioners (this is often where concepts are FIRST coined)
   - **Open Source**: GitHub official repos, GitHub Discussions, GitHub Issues (for known problems)
   - **Industry Analysis**: Gartner, Forrester, IDC, Statista
   - **Chinese Media**: CSDN, 掘金 (Juejin), 开源中国 (OSChina), InfoQ 中文, 博客园
   - **Standards Bodies**: W3C, IETF, ISO, ECMA, OWASP, CNCF
   - **Video & Courses**: YouTube (official channels, conference talks), Coursera, Udemy, Pluralsight
   - **Books & References**: O'Reilly, Manning, No Starch Press, Safari Books Online
   - **Newsletters & Podcasts**: Relevant tech newsletters, podcast episodes
4. **Exclusion Rule**: DO NOT include any URL that is already in the known sources list. Focus on discovering sources NOT yet found.
   - **HOWEVER**: If the topic is a concept and you find a product/tool that shares the topic name, do NOT exclude it — instead, clearly label it as a potential IMPLEMENTATION of the concept, not the origin
5. **Accessibility Check**: For each candidate URL, verify it is accessible (does not return 404). Use `WebFetch` if unsure. Discard inaccessible URLs.
6. **Credibility Annotation**: Rate each discovered source:
   - **Tier 1 (Primary)**: Original concept papers, personal blogs where concept was first coined, original definitions
   - **Tier 2 (Authoritative)**: Reputable tech media, established engineering blogs, academic publications, analyst reports
   - **Tier 3 (Community)**: Developer forums, community wikis, well-known individual blogs, Q&A sites
7. **No Deep Reading**: You are a SOURCE MINER, not a content analyst. Only collect URLs, titles, types, and credibility ratings. Do NOT read full articles or extract content — but DO note if a source appears to be the origin of the concept.

**Return Format:**

Return ONLY a markdown table of newly discovered sources. NO other text.

```markdown
| URL | 标题/描述 | 来源类型 | 可信度等级 | 备注 |
| :--- | :--- | :--- | :--- | :--- |
| {URL} | {简要标题} | {官方文档/技术媒体/论坛/学术/工程博客/开源/行业分析/中文媒体/标准/视频/书籍/其他} | {Tier 1/2/3} | {简要说明相关性} |
```

If you find ZERO new sources not already in the known list, explicitly state: "本轮未发现新数据源。"

### Step 0.3: Final Source List Compilation

After the loop terminates, the main agent must:

1. **Master List Deduplication**: Ensure zero duplicate URLs in the final list.
2. **Accessibility Audit**: Re-verify that all Tier 1 and Tier 2 sources are accessible. Flag any that return errors.
3. **Credibility Sorting**: Sort the master list by credibility tier (Tier 1 first, then Tier 2, then Tier 3).
4. **Count & Report**: Record the total number of unique sources discovered and the number of rounds executed.
5. **Save to Cache**: Append the discovered sources to `.temp/deep-research-data-sources.md` using the format:
   ```markdown
   ## {Topic Name (Original Case)} @ {YYYY-MM-DD}

   - [{Title}]({URL}) - {Description}
   ```
   The `@ {YYYY-MM-DD}` timestamp is generated from `date +"%Y-%m-%d"`. This timestamp is used for cache expiry validation.
   If the file does not exist, create it with the header:
   ```markdown
   # Deep Research Data Sources

   ## {Topic Name} @ {YYYY-MM-DD}

   - [{Title}]({URL}) - {Description}
   ```
   If the topic section already exists, replace it entirely with fresh data (including new timestamp).

### Step 0.4: Research Dimension Definition

Based on the topic type and the discovered source richness, define key research dimensions:

- For a **technology/framework**: origin, core principles, architecture, API design, performance characteristics, ecosystem, adoption trends
- For a **concept/term**: definition, historical evolution, theoretical foundations, practical applications, related concepts
- For a **product/tool**: vendor, release history, key features, pricing model, competitive landscape, user reviews
- For a **methodology**: principles, process steps, benefits, limitations, success stories, industry adoption

## Phase 1: Parallel Independent Research

Launch **5 independent `general-purpose` agents** to research the topic in parallel. **CRITICAL: Each subagent MUST be given the EXACT SAME task prompt — same objectives, same instructions, same topic. DO NOT assign different focus areas, angles, or specialized roles to different subagents.** 

**EACH SUBAGENT MUST RESEARCH THE ENTIRE TOPIC, NOT A SUBSET OF IT.** For example, do NOT have one agent research "origin", another research "tool ecosystem", and another research "AI trends" — all 5 agents must independently research ALL aspects (origin, development history, technical details, use cases, ecosystem, criticisms, trends, etc.) and return comparable complete reports. Their independence must come from independent execution of the **identical** task. This is essential for meaningful cross-verification.

**The following is the EXACT prompt to send to each of the 5 subagents. The research task must be identical for all agents — do NOT assign different focus areas or roles. The ONLY per-agent substitution allowed is replacing `{SubagentNumber}` with 1, 2, 3, 4, or 5 respectively:**

``````markdown
**Research Task: {Topic Name}**

**Research Dimensions (investigate ALL of these):**
- Development history: inception, key milestones, evolution
- Origin: who proposed it, when, where, original context
- Definition and core concepts
- Technical details and architecture
- Use cases and applications
- Ecosystem and related tools/projects
- Criticisms, limitations, and controversies
- Current state and future trends

**Critical Requirements:**

1. **Read the sources for this topic** from `.temp/deep-research-data-sources.md` in the project root — locate the section with header `## {Topic Name}` and read only that section as your starting point
2. **Follow links in sources** — when a source mentions another article/paper/person, immediately visit that link to verify
3. **Verify all facts independently** — do not assume a claim is true just because a source says it. Cross-check with multiple authoritative sources.
4. **Verify dates** — if a source says something was published on date X, visit the actual page and check the displayed date. Dates in sources are frequently wrong.
5. **Format all references as hyperlinks** — every external source mentioned must be a valid, accessible URL (not 404 or broken)
6. **Do NOT trust AI-generated content blindly** — apply critical judgment to all claims, including those from AI agents
7. **All major claims must have source citations** with credibility assessment (High/Medium/Low)

**Output format:**

Read the report template instructions from `.claude/skills/deep-research/REPORT_TEMPLATE.md` and output your findings in the EXACT same format as specified in that template. Save your complete findings to `.temp/{kebab-case-topic}-deep-research-{YYYYMMDDHHmmss}-{SubagentNumber}.md` in the project root, where `{YYYYMMDDHHmmss}` is generated by the `date +"%Y%m%d%H%M%S"` command.

Your output MUST follow the template structure exactly — same sections, same requirements, same quality standards.
``````

**End of Subagent Prompt** — the following is for the main agent to handle synthesis.

## Phase 2: Synthesis and Cross-Validation

Once all 5 subagents have returned (or their files are available in `.temp/`), the main agent performs rigorous synthesis. **Discover the subagent output files using `ls .temp/{kebab-case-topic}-deep-research-*.md` and read each file to ensure complete access to all findings.**

1. **Comparative Analysis**: Place the 5 reports side-by-side. Identify:
   - Facts reported by all 5 agents (high confidence)
   - Facts reported by only 3-4 agents (requires additional verification)
   - Direct contradictions between agents
   - Gaps where all agents missed important information
2. **Fact Resolution**: For every discrepancy:
   - Perform targeted searches using `WebSearch` or `WebFetch` on authoritative sources
   - Prioritize primary sources (official docs, original papers, release notes) to resolve conflicts
   - Record the resolution and the evidence behind it
3. **Fact and Logic Error Detection (CRITICAL)**: 
   - **Dates are frequently wrong in sources.** For any date mentioned (publication date, event date, version date, etc.), verify it by fetching the actual page and checking the displayed date. Do NOT assume a cited date is correct.
   - Check for logical inconsistencies, contradictions between agents, and any claims that don't hold up under scrutiny.
   - **Never blindly trust information from the internet or from agents.** Always apply critical judgment. If something seems questionable, verify it directly.
   - If a claim cannot be verified or is found to be incorrect, flag it explicitly and remove or correct it from the final report.
4. **Source Quality Triage**:
   - **Verified**: Claims supported by primary/official sources or multiple independent authoritative sources
   - **Likely True**: Claims with strong but limited source support, no contradictions
   - **Disputed**: Claims with conflicting sources — present all sides with source attribution
   - **Unverified**: Claims found in only one low-credibility source — flag explicitly
5. **Gap Analysis**: If the 5 agents collectively missed important aspects (e.g., no one covered installation steps for a tool), perform additional targeted research to fill the gaps.
6. **Unified Narrative Construction**: Merge the verified findings into a coherent, comprehensive understanding. Ensure:
   - No internal contradictions
   - Every significant claim has source backing
   - Controversial points present multiple perspectives fairly
   - The level of detail matches the topic's complexity
7. **Concept-Implementation Separation Check (CRITICAL for Concept/Methodology Topics)**:
   - If the topic is a concept/methodology, verify that:
     - The concept's theoretical foundations, origin, and evolution are discussed SEPARATELY from its practical implementations
     - Implementations (products/frameworks) are discussed ONLY in the "适用场景" or "应用与发展趋势" sections
     - The "与同类方案的对比" section does NOT compare the concept with its implementations
   - If a product shares the same name as the concept (e.g., "Foo" could be a concept AND a product), explicitly note: "注意：[产品名] 是一款实现 [概念名] 思想的具体产品，而非 [概念名] 本身"
   - **Origin Verification**: For concepts, explicitly verify the claimed origin against the actual semantic content of sources. If multiple sources claim to be the origin, trace back to find the FIRST publication that defined/coined the concept. Verify propagation: which subsequent works cited, referenced, or built upon the original.

## Phase 3: Final Report Generation

Generate the final report and save it to `generated/{kebab-case-topic}-deep-research-{YYYYMMDDHHmmss}.md` in the project root, where `{YYYYMMDDHHmmss}` is generated by the `date +"%Y%m%d%H%M%S"` command. Create the `generated/` directory first with `mkdir -p generated` if it does not exist.

**Output the report in Chinese.** Read the report template instructions from `.claude/skills/deep-research/REPORT_TEMPLATE.md` and output the final report in the EXACT same format as specified in that template.

## Quality Checklist

- [ ] Phase 0 cache check performed
- [ ] Phase 0 iterative source mining completed (5 agents per round, up to 10 rounds, early-terminated when no new sources are found)
- [ ] Phase 1 research used 5 independent subagents with identical prompts
- [ ] Key facts are cross-verified across multiple sources
- [ ] Discrepancies between agents are resolved with documented reasoning
- [ ] The filename uses the correct kebab-case prefix and timestamp format
- [ ] Discovered sources were saved to `.temp/deep-research-data-sources.md` in the project root
- [ ] Each subagent saved their findings to `.temp/{kebab-case-topic}-deep-research-{timestamp}-{SubagentNumber}.md` in the project root

## Notes

- If the topic is ambiguous or too broad, ask the user for clarification before starting research.
- If the topic is extremely new (released within the last few months) or extremely niche, acknowledge the limited source availability explicitly in the report.
- For proprietary/closed-source products, focus on publicly available information and clearly distinguish between confirmed facts and informed speculation.
- When subagents return inconsistent information, always favor primary sources (official docs, original papers, vendor announcements) over secondary interpretations.
- Do not translate tool names, framework names, or programming language keywords into Chinese.
