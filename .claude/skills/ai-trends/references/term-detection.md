# Emerging Term Detection Rules

This file defines the complete rules and steps for term mining from collected content.

## 1. Build Corpus

From retrieved pages, extract and aggregate the following into a raw text list:

- Title of each article
- First paragraph or summary (first 2-3 sentences) of each article
- Hacker News / Reddit hot post titles and high-vote comments
- GitHub Trending project names and descriptions

> Full article body is not needed, only title-level text

## 2. Time Slice Comparison (if publication date available)

- Divide corpus into `last 7 days` and `previous 8-30 days` two slices
- Identify phrases with significantly increased relative frequency (>3x), or phrases appearing multiple times in recent slice but never in earlier slice

## 3. Pattern-Based Extraction (MUST execute)

Extract candidate terms matching these patterns:

- `X engineering` (e.g., context engineering, vibe engineering)
- `X-first development` / `X-first AI` (e.g., prompt-first, agent-first)
- `post-X AI` / `beyond X` (e.g., post-RLHF, beyond prompts)
- `what is X` / `why X matters` / `introducing X` (extract X)
- `"Quoted phrases"` that look like new methodology names
- `a new X paradigm` / `the new X engineering`
- `Agent = Model + X` structure or similar expressions
- Articles comparing old and new approaches and explicitly naming them
- `from X to Y` evolution narrative structure — these titles are strong signals of paradigm shifts

## 4. Filter Candidate Terms

For each candidate term, verify:

- Weight calculation: First appearance on same website scores 10 points, each additional appearance scores 2 points
- Uncommon terms: Should not be widely known AI terms (e.g., RAG, LoRA, GPT, Transformer, fine-tuning, Vibe Coding)
- Not pure product/company names: Unless discussion focuses on methodology named after them
- Time correlation: Appeared or gained attention within the specified time range

## 5. Importance Supplementary Evaluation

For candidate terms that passed above filters but have low frequency, the following signals make them worth prioritizing for deep verification (even with low frequency):

- **First post by authoritative source**: Concept first proposed or named by authoritative bloggers like Martin Fowler, Simon Willison, Andrej Karpathy, Chip Huyen
- **Clear paradigm naming**: Article title or opening uses "from X to Y" evolution narrative structure
- **Methodology systematization**: Concept has complete system (e.g., multiple articles, guides, framework implementations)
- **Tool/framework support**: Open source project named after concept on GitHub, or framework explicitly uses concept as core feature
- **Significant community attention**: HN/Reddit discussion post with more than 50 votes
- **GitHub stars burst**: Related project appears on Trending with rapid stars growth (e.g., thousands per week)

> If a concept is first posted by a single authoritative source (e.g., Simon Willison's blog series) and has a complete methodology system, include it for deep verification even with single source. Authoritative bloggers are often first posters of emerging concepts, not citees
>
> Do not merge concept A into concept B or discard A because A is considered a subfield of B. Each concept should be independently evaluated and reported, letting users judge the hierarchical relationship between concepts
>
> Concept relationships should be noted in the report, not simplified through merging

## 6. Immediate Reverse Search

For each candidate term that passed initial filtering, immediately execute the following searches to collect more evidence:

```text
"[candidate term]" AI
"[candidate term]" site:x.com
"[candidate term]" site:news.ycombinator.com
"[candidate term]" site:reddit.com
"[candidate term]" site:github.com
"[candidate term]" site:zhihu.com
```

Append search results to candidate term records (occurrence count, source domain), eliminate terms with isolated mentions.

## 7. Origin Verification (NOT Limited by Time Range)

**Important**: During origin verification, **do NOT limit by the current query time range**. Must use multiple search engines (Google, Bing, DuckDuckGo) and various sources to trace the original origin of the concept.

Use all possible means to verify the term's source (proposer, proposing organization, first appearing article or paper), record complete original source links for later use.

**Origin Tracing Priority**:
1. **First post by authoritative blogger**: Priority check of Martin Fowler, Simon Willison, Andrej Karpathy, Chip Huyen, Paul Graham blogs/sites
2. **Academic source**: First appearance time in arXiv papers
3. **GitHub history**: Earliest records in Issue, PR, Commit history
4. **Social media**: First discussion on Twitter/X, LinkedIn
5. **HN/Reddit**: Earliest related discussion post
6. **Search engines**: Use Google, Bing, DuckDuckGo respectively for different results

**Search Engine Query Templates** (use at least 2-3 different search engines for each term):
```
Google: "[term]" OR "[term English]" site:martinfowler.com OR site:simonwillison.net
Bing: "[term]" AI engineering methodology origin
DuckDuckGo: "[term]" first introduced OR coined
```

**Report Requirements**:
- Each term must record: earliest proposed date, earliest proposer/institution, original article/paper link
- If unable to find corroborating source, mark as `【未经核实】` (Unverified)
- If multiple search engine results are inconsistent, mark as `【有争议】` (Controversial) and present different viewpoints

## 8. Output Candidate List

Generate structured list for each candidate term:

| Term | Occurrences | Source URL | Earliest Detection Date | Summary |
|------|------------:|------------|:-----------------------:|---------|
| [term] | [N] | [complete link to specific page mentioning the term] | [date] | [one-sentence summary] |