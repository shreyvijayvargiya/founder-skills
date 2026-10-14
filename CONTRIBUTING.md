# Adding a skill

The library grows from skills actually used in real projects. A skill earns a place when it has produced a useful result at least once.

## Steps

1. **Pick the category** — `build`, `grow`, `seo`, `customers`. For a new category (e.g. `investors`, `scale`), create `capabilities/<category>/` and add it to `CATEGORIES` in `scripts/sync-registry.py`.
2. **Copy the template** — `templates/AGENT.template.md` → `capabilities/<category>/<kebab-name>/AGENT.md`.
3. **Frontmatter** — `name` matches the folder; `description` is one sentence ending in "Use when …" (the router reads this to decide).
4. **Write the workflow** — inputs, steps, a concrete output format, quality rules. Keep it under ~200 lines unless it truly needs more.
5. **Sync the index** — `python3 scripts/sync-registry.py` updates the README and `framework/capability-registry.md`.
6. **Routing hints** — if it overlaps another skill, add a row to the disambiguation tables in `framework/capability-registry.md`.
7. **Commit** — one skill per commit: `Add <name> skill`.

## Quality bar

- Single clear outcome for a solo founder; no enterprise ceremony.
- Never fabricate data, quotes, or metrics; say when evidence is thin.
- Ends with one recommended next action.
- Names the sibling skill it hands off to or receives from.
