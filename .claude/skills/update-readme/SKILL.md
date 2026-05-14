---
name: update-readme
description: |
  Scan all Skills under .claude/skills/ and all git-tracked markdown reports in the project,
  then update README.md with the Skills documentation and a reports table (ToC).
  Trigger when: Skills are added/removed/modified, or new reports are generated.
disable-model-invocation: true
---

# Update README Skill

This skill updates the project README.md to reflect the current state of available Skills and generated reports.

## When to Use

- A new Skill is added, removed, or modified
- A new report is generated and should be listed in the README
- The user asks to "update README" or "sync README"

## Workflow

### Phase 1: Collect Skills Information

Scan all subdirectories under `.claude/skills/` and read each `SKILL.md` file. Extract:
- `name`: The skill identifier (from frontmatter)
- `description`: The skill description (from frontmatter)

For each skill, determine:
- **Function & Value**: 用产品说明书风格撰写，客观陈述 skill 的功能，不出现"当你..."、"需要..."、"帮助..."等面向用户的措辞，也不提及实现细节
- **Trigger Conditions**: What user phrases or requests activate this skill (from description)
- **Usage Example**: A code block showing how to invoke the skill

### Phase 2: Collect Generated Reports

Scan all git-tracked markdown files in the project, excluding:
- `.claude/` directory (and all subdirectories)
- `.git/` directory
- `node_modules/`
- `.temp/` directory
- `generated/` directory
- `ai-trends/` directory
- Any other paths covered by `.gitignore`

For each markdown file, extract:
- **分类 (Category)**: Derive from the file's parent directory (e.g., `agent-skills/` → `Agent Skill`, `ai-engineering/` → `AI Engineering`). Translate to Chinese unless the term is a professional abbreviation or technical term (e.g., AI、Linux、Shell、Kubernetes、CI/CD、API 等保持英文)
- **标题 (Title)**: Extract from the first `#` heading line in the file (e.g., `# 深度解读：XXX` → `深度解读：XXX`). Title must not exceed 50 characters. Full-width characters (CJK characters, Emoji, full-width symbols) count as 2 characters each. If the title exceeds this limit, either simplify (e.g., remove redundant translations, drop full expanded names of abbreviations) or truncate with `...`
- **时间 (Time)**: Extract from the file content using this priority:
  1. `生成时间：{YYYY-MM-DD HH:mm}` or `报告生成时间：{YYYY-MM-DD HH:mm}`
  2. `研究时间：{YYYY-MM-DD}`
  3. `日期：{YYYY-MM-DD}` (article original date)
  4. If none found, leave empty

### Phase 3: Generate README.md

Read the current README.md to check if it already has the required structure. Then write the updated content with this exact structure:

``````markdown
# 研究

## 目录

- [研究报告](#研究报告)
- [Skills 使用说明](#skills-使用说明)

---

## 研究报告

| 分类 | 标题 | 时间 |
| :--- | :--- | :---: |
| {分类} | [{标题}]({相对路径}) | {YYYY-MM-DD 或留空} |
| ... | ... | ... |

---

## Skills 使用说明

### {skill-name-1}

**功能与作用**: {一句话描述 skill 的功能，不涉及实现细节}

**触发条件**: {一句话描述在什么情况下触发该 skill}

```markdown
/{skill-name} {使用示例}
```

---

### {skill-name-2}

... (repeat for each skill)

...
``````

## Implementation Notes

- **Title extraction**: Use the first `#` heading line, strip leading `#` and whitespace, use as-is
- **Time format**: Normalize to `YYYY-MM-DD` (drop time component if present, as it may not be reliable)
- **Path format**: Use path relative to project root (e.g., `agent-skills/file.md`)
- **Category derivation**: Use directory name, convert kebab-case to Title Case (e.g., `agent-skills` → `Agent Skill`, `ai-engineering` → `AI Engineering`)
- **Skills order**: List skills in alphabetical order by name
- **Reports order**: Sort by category (alphabetically), then by time descending (newest first), then by title. Items with no time at the end of their category
- **DO NOT fabricate** any title or time — only use what is actually present in the file content

## Quality Checklist

- [ ] All skills under `.claude/skills/` are documented
- [ ] All git-tracked markdown files (excluding ignored paths) are listed in the reports table
- [ ] Title is extracted from the first `#` heading in each file
- [ ] Time is extracted from content using the priority order specified above
- [ ] Table columns are: 分类 | 标题 | 时间
- [ ] Skills section has: 功能与作用, 触发条件, 代码示例
- [ ] No fabricated or placeholder content
- [ ] Reports sorted by category, then time descending, then title
- [ ] Category names are translated to Chinese (except professional abbreviations/technical terms)
- [ ] Title does not exceed 50 half-width characters (full-width characters count as 2)