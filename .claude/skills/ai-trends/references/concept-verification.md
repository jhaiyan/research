# Concept Verification and Writing Rules

This file defines the detailed steps for verifying candidate terms and writing final entries. For each candidate term (up to 5 most promising), execute verification steps using **3 independent Subagents in parallel**. Each Subagent reads this file for detailed verification steps.

## Critical: Triple-Agent Verification Requirement

**Each concept MUST be verified by 3 independent Subagents from different perspectives:**

- **Subagent-A (Origin Tracing)**: Verify the earliest origin of the concept
- **Subagent-B (Independent Validation)**: Search for independent confirmations from different sources
- **Subagent-C (Controversy Analysis)**: Collect and analyze supporting and opposing viewpoints

Only after all 3 Subagents complete their verification, compile the results and proceed to writing the final entry.

## 1. Origin Tracing (NOT Limited by Time Range)

**Important**: During concept tracing, **do NOT limit by the current query time range**. Emerging concepts are often proposed much earlier, appearing repeatedly in academic papers, blogs, and talks. Must consult enough materials to verify the original source.

Attempt to locate the earliest public post (blog, paper, tweet, GitHub Issue) defining or popularizing the term, record date, author/source, and original wording.

**Origin Tracing Methods** (priority from high to low):
- Search the original proposer's blog/site (e.g., Martin Fowler, Simon Willison, Andrej Karpathy, Chip Huyen)
- Use Google search: `"[term]" site:martinfowler.com OR site:simonwillison.net OR site:karpathy.ai`
- Use Bing search: `"[term]" AI engineering OR methodology`
- Use DuckDuckGo search: find earliest appearance records
- Search GitHub Issue, Pull Request, Commit history
- Trace to first appearance in academic paper (arXiv)
- Find earliest discussion post on HN/Reddit

**Time Range Principle**:
- If the concept existed before the query time range, still complete full tracing
- Report should mark the concept's **earliest proposed time** and **current attention peak time**

## 2. Cross-Validation

Confirm whether there are natural discussions using the term independently (not just citing the original source):

- If results are insufficient, supplement with additional searches
- If no independent discussion exists, mark as `【未形成讨论】` (No Discussion Formed)

## 3. Compare with Old Paradigm

Answer two questions:

- What problem does it solve?
- What was the previous approach? What is the new approach now?

Create comparison table when appropriate.

## 4. Evaluate Maturity

Assign one of three maturity levels:

- 🔥 (Burning): Outbreak period, ≥3 independent sources in last 7 days, active discussion, multiple implementations
- 🌱 (Sprouting): Emerging period, 2-3 sources in last 30 days, mainly explanatory posts, discussed by early adopters
- 🧪 (Experimental): Single source or only exists in GitHub README / unpublished preprints

## 5. Write Final Entry

Place in "Concepts & Research" (for conceptual content) or "Development Paradigms" (for engineering/methodology content).

Output format for each concept:

```markdown
### [Term or Concept] [Maturity Badge]

- **Definition**: [Precise definition, sufficient and necessary.]
- **Origin Tracing**: [Institution, individual or research team that proposed the concept, try your best to trace to the most original source.]
- **Background**: [Briefly explain the concept's origin, what problem it solves, development trajectory or key driving factors.]
- **Use Cases**: [Explain the concept's main application scenarios or problems it solves.]
- **Cross-Validation**: [If multiple independent sources mention this concept, briefly explain here.]
- **Controversy & Questions**: [If there is related controversy or questions, briefly explain here.]
- **Related Links**:
  - [Link1](URL)
  - [Link2](URL)
```

## 6. Controversy Identification

For each verified concept, Subagent-C must explicitly address:
- What controversies exist around this concept?
- What are the viewpoints of different parties?
- Is there any criticism from authoritative sources?

If no controversy found, explicitly state: "No significant controversy identified from multiple sources."

## 7. Summary and Recommendations

After all 3 Subagents complete verification, compile a summary including:
- Verified origin with evidence links
- List of independent corroborating sources (minimum 3 required)
- Controversy summary with different viewpoints clearly presented
- Final maturity assessment with reasoning
- Recommendation: Include in report or exclude (with reason)