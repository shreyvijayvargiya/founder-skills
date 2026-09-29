# Installing Founder OS

Founder OS is one parent skill (`SKILL.md`) plus specialist instructions under `capabilities/` and orchestration under `framework/`. Install the **whole repository** as a single skill folder.

Repository: https://github.com/shreyvijayvargiya/founder-skills

---

## Requirements

- Valid `SKILL.md` at the skill folder root (included in this repo)
- A **new agent session** after install so skills are discovered

---

## Claude Code (personal — all projects)

```bash
git clone https://github.com/shreyvijayvargiya/founder-skills.git ~/.claude/skills/founder-os
```

Start a new Claude Code session, then:

- Run `/founder-os` to invoke directly, or
- Ask a founder question; Claude may auto-load the skill when the task matches the description.

Verify:

```bash
head ~/.claude/skills/founder-os/SKILL.md
```

You should see YAML frontmatter between `---` lines with `name: founder-os`.

---

## Claude Code (project — this repo only)

From your project root:

```bash
mkdir -p .claude/skills
git clone https://github.com/shreyvijayvargiya/founder-skills.git .claude/skills/founder-os
```

Commit `.claude/skills/founder-os` if you want the skill shared with your team.

---

## Cursor (personal)

```bash
git clone https://github.com/shreyvijayvargiya/founder-skills.git ~/.cursor/skills/founder-os
```

Restart Cursor or start a new Agent chat so the skill is picked up.

---

## Cursor (project)

From your project root:

```bash
mkdir -p .cursor/skills
git clone https://github.com/shreyvijayvargiya/founder-skills.git .cursor/skills/founder-os
```

---

## Update an existing install

```bash
cd ~/.claude/skills/founder-os   # or ~/.cursor/skills/founder-os, or .claude/skills/founder-os
git pull origin main
```

Start a new session after updating.

---

## Example prompts

- “Should I build [idea]? Use Founder OS.”
- “Research https://example.com — product, ICP, and competitors.”
- “My SaaS is live — audit launch foundations and indexing.”
- “What SEO pages should we create for [product]?”

---

## What gets installed

| Path | Role |
|------|------|
| `SKILL.md` | Parent agent (entry point) |
| `framework/` | Planner, router, evaluator, synthesizer, etc. |
| `capabilities/` | 21 specialist agents (`AGENT.md` per capability) |

Individual capabilities are **not** separate installable skills; the parent skill loads them as needed.

---

## Troubleshooting

**Skill does not appear**

- Confirm path ends with `founder-os/SKILL.md`, not a nested subfolder.
- Open a **new** session after install.

**YAML / skill validation errors**

- Frontmatter must be exactly: opening `---`, `name` and `description`, closing `---`, then markdown body.
- Do not put decorative dash lines inside the frontmatter block.

**More detail**

- See [docs.md](./docs.md) for architecture and capability list.
- See [README.md](./README.md) for the full parent skill instructions.
