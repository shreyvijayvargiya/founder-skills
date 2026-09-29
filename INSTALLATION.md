# Installing Founder OS

Founder OS is **one skill** named `founder-os`: a root `SKILL.md`, plus `capabilities/` (validate, build, launch, grow) and `framework/` (planner, router, etc.). Install the **whole tree** — not individual capability folders.

Repository: https://github.com/shreyvijayvargiya/founder-skills

---

## Claude.ai (web) — use ZIP upload, not git

**Claude.ai cannot install this skill by running `git clone` or SSH inside a chat.** There is no shell access to your machine or to GitHub keys from the browser app. Installation is always: **build a ZIP on your computer → upload in Settings**.

### Prerequisites

- [Code execution enabled](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) (Skills depend on it for bundled files)
- Folder name **`founder-os`** must match `name: founder-os` in `SKILL.md`
- ZIP must contain **`founder-os/` as the root entry**, with `SKILL.md` inside that folder

Correct layout inside the ZIP:

```
founder-os/
├── SKILL.md
├── framework/
├── capabilities/
└── …
```

Wrong (upload will fail or skill won’t load):

```
SKILL.md          ← files at ZIP root, no folder wrapper
founder-skills-main/   ← GitHub “Download ZIP” default name (rename first)
```

### Option A — Package from this repo (recommended)

On your Mac/Linux terminal (not inside claude.ai):

```bash
git clone https://github.com/shreyvijayvargiya/founder-skills.git
cd founder-skills
chmod +x scripts/package-for-claude-ai.sh
./scripts/package-for-claude-ai.sh
```

This writes **`founder-os-claude-ai.zip`** in the repo root (no `.git` inside the skill folder).

### Option B — You already zipped `founder-os/` yourself

If your ZIP matches the layout above and excludes `.git`, you can upload it as-is. Verify:

```bash
unzip -l your-archive.zip | head -15
```

You should see `founder-os/SKILL.md`, not only `SKILL.md` at the top level.

### Option C — GitHub “Download ZIP” (HTTPS, no git/SSH)

1. Open https://github.com/shreyvijayvargiya/founder-skills/archive/refs/heads/main.zip (browser download, no SSH).
2. Unzip — you get a folder like **`founder-skills-main`**.
3. **Rename** that folder to **`founder-os`**.
4. Zip **the folder**, not loose files:

```bash
cd /path/to/parent
zip -r founder-os-claude-ai.zip founder-os
```

5. Confirm: `unzip -l founder-os-claude-ai.zip` shows `founder-os/SKILL.md`.

### Upload and enable on claude.ai

1. Go to [claude.ai](https://claude.ai) → **Settings** → **Capabilities** or **Customize** → **Skills**.
2. Click **Upload skill** and select your `.zip` file.
3. **Toggle the skill ON** (upload alone does not activate it).
4. Start a **new chat** and try: *“Use Founder OS: should I build [idea]?”*

### If Claude in chat tries to `git clone` for you

Stop that approach on claude.ai. Tell Claude the skill is **already uploaded in Settings**, or paste a short task and ask it to follow **`SKILL.md`** from your enabled skill. Do not ask the web app to run git or SSH to install skills.

### Claude.ai troubleshooting

| Symptom | Fix |
|--------|-----|
| “Could not find SKILL.md” | Re-zip so the path is `founder-os/SKILL.md`, not `SKILL.md` at ZIP root. |
| Upload / YAML error | Ensure frontmatter is `---`, `name`, `description`, closing `---` (see repo `SKILL.md`). |
| Skill never triggers | Turn skill **ON**; shorten prompt to mention SaaS founder / validate / launch / SEO; check description in `SKILL.md` (claude.ai limit ~200 characters). |
| “Internal server error” on upload | Retry later; confirm ZIP size and structure; see [Anthropic status](https://status.anthropic.com/). |

---

## Claude Code (personal — all projects)

Uses **HTTPS or SSH on your machine**, not claude.ai:

```bash
git clone https://github.com/shreyvijayvargiya/founder-skills.git ~/.claude/skills/founder-os
```

Start a new Claude Code session, then run `/founder-os` or ask a founder question.

---

## Claude Code (project)

```bash
mkdir -p .claude/skills
git clone https://github.com/shreyvijayvargiya/founder-skills.git .claude/skills/founder-os
```

---

## Cursor (personal)

```bash
git clone https://github.com/shreyvijayvargiya/founder-skills.git ~/.cursor/skills/founder-os
```

---

## Cursor (project)

```bash
mkdir -p .cursor/skills
git clone https://github.com/shreyvijayvargiya/founder-skills.git .cursor/skills/founder-os
```

---

## Update an existing install

**Claude.ai:** Build a fresh ZIP (Option A or C) and upload again, or replace via Skills settings if your plan supports updates.

**Claude Code / Cursor (git install):**

```bash
cd ~/.claude/skills/founder-os   # or ~/.cursor/skills/founder-os
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

Capabilities are loaded by the parent skill; you do not upload them as separate skills.

---

## More detail

- [docs.md](./docs.md) — architecture and capability list  
- [README.md](./README.md) — full parent skill instructions  
- [Claude custom skills help](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
