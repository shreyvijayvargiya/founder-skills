#!/usr/bin/env python3
"""Regenerate skill tables from capabilities/*/*/AGENT.md frontmatter.

Run after adding or editing a skill:  python3 scripts/sync-registry.py
Rewrites the block between <!-- skills:start --> and <!-- skills:end -->
in README.md and framework/capability-registry.md.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGETS = [ROOT / "README.md", ROOT / "framework" / "capability-registry.md"]

# Order = display order. Categories not listed here are appended alphabetically.
CATEGORIES = {
    "build": ("Build", "Validate the idea, scope the MVP, position and price it."),
    "grow": ("Grow", "Launch and market: channels, directories, outreach, weekly growth."),
    "seo": ("SEO", "Audit and grow search + AI-search visibility."),
    "customers": ("Customers", "Find them, listen to them, onboard them, keep them."),
    # Next up: "investors" (fundraising), "scale" (hiring, ops, systems).
}


def frontmatter(path):
    text = path.read_text()
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    fields = dict(re.findall(r"^(\w+):\s*(.+)$", m.group(1), re.M)) if m else {}
    return fields


def build():
    cap = ROOT / "capabilities"
    dirs = {d.name for d in cap.iterdir() if d.is_dir()}
    order = [c for c in CATEGORIES if c in dirs] + sorted(dirs - set(CATEGORIES))
    out, total = [], 0
    for cat in order:
        title, blurb = CATEGORIES.get(cat, (cat.title(), ""))
        skills = sorted((cap / cat).glob("*/AGENT.md"))
        total += len(skills)
        out.append(f"### {title} ({len(skills)})\n")
        if blurb:
            out.append(f"{blurb}\n")
        out.append("| Skill | What it does |\n|-------|--------------|")
        for p in skills:
            fm = frontmatter(p)
            name = fm.get("name", p.parent.name)
            rel = p.relative_to(ROOT).as_posix()
            out.append(f"| [`{name}`]({rel}) | {fm.get('description', '')} |")
        out.append("")
    return "\n".join(out).rstrip() + "\n", total


def main():
    block, total = build()
    pat = re.compile(r"(<!-- skills:start -->\n).*?(<!-- skills:end -->)", re.S)
    for f in TARGETS:
        text = f.read_text()
        if not pat.search(text):
            print(f"skip {f.name}: markers missing")
            continue
        f.write_text(pat.sub(lambda m: m.group(1) + block + m.group(2), text))
        print(f"updated {f.relative_to(ROOT)}")
    print(f"{total} skills")


if __name__ == "__main__":
    main()
