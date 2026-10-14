# Founder OS — Repository Documentation

Founder OS is an **AI agent skill** for SaaS founders. It does not run as traditional code. It is a set of markdown instructions that teach an AI agent how to research, decide, and act on founder questions.

Think of it like this:

- **SKILL.md** = the boss (parent agent)
- **capabilities/** = specialist employees (SEO, launch, pricing, etc.)
- **framework/** = the boss's playbook (how to plan, pick specialists, check work, and reply)

---

## How a request flows (simple)

```
Founder asks a question
        ↓
SKILL.md (parent agent understands the goal)
        ↓
planner.md          → What do we need to find out?
        ↓
capability-registry → Which specialists exist?
router.md           → Which specialist(s) should run?
        ↓
capabilities/*/AGENT.md → Specialists do the work
        ↓
context-compressor.md → Shrink results so the next step stays focused
        ↓
evaluator.md        → Is this enough, or do we need more research?
decision-framework  → BUILD / TEST / WAIT / KILL (when it's a build decision)
        ↓
synthesizer.md      → One clear answer for the founder
```

The parent agent runs only the steps it needs. It does not run every capability every time.

---



## Why the `framework/` folder exists

**Capabilities know their job. The framework knows how to coordinate them.**

Without `framework/`, the parent agent would either:

- run too many capabilities (slow, noisy), or
- give vague answers with no structure, or
- pass huge reports between steps and lose focus.

Each file in `framework/` is one step in the **operating loop**. Together they turn Founder OS from a pile of skills into an **orchestrator**.


| File                     | One-line job                  | Plain English                                                          |
| ------------------------ | ----------------------------- | ---------------------------------------------------------------------- |
| `planner.md`             | Break the question into steps | "What evidence do we actually need before we can answer?"              |
| `capability-registry.md` | List all specialists          | "Here are all the skills we can call, and when to use each."           |
| `router.md`              | Pick the right specialist(s)  | "For this question, run launch-foundation-audit — not saas-launch."    |
| `context-compressor.md`  | Shrink reports between steps  | "Don't forward 20 pages — pass only facts, risks, and open questions." |
| `evaluator.md`           | Stop or continue              | "Do we have enough to answer, or is something still missing?"          |
| `decision-framework.md`  | Classify build decisions      | "Should they BUILD, TEST, WAIT, MODIFY, or KILL this idea?"            |
| `synthesizer.md`         | Final founder-facing answer   | "Turn all research into one recommendation + next steps."              |




### Framework files in order (when they run)

1. **Planner** — Understand the objective and list required evidence.
2. **Registry + Router** — Choose minimum capabilities and execution order.
3. **Capabilities execute** — Domain experts produce findings.
4. **Context compressor** — Pass compact context to the next capability (if any).
5. **Evaluator** — Enough evidence? Contradictions? Run another capability?
6. **Decision framework** — Only when the founder is deciding whether to build/launch/pivot.
7. **Synthesizer** — Single clear response: recommendation, evidence, next actions.

---



## Repository structure

```
founderos/
├── SKILL.md                 ← Parent agent (main entry point)
├── README.md                ← Skill library index + roadmap
├── docs.md                  ← This file
├── LICENSE
├── framework/               ← Orchestration playbook
├── CONTRIBUTING.md          ← How to add a skill
├── templates/               ← AGENT.template.md for new skills
├── scripts/                 ← package-for-claude-ai.sh, sync-registry.py
└── capabilities/            ← Specialist skills
    ├── build/               ← Validate, scope, position, price
    ├── grow/                ← Launch, directories, outreach, weekly report
    ├── seo/                 ← Audits, content, links, AI search
    └── customers/           ← Leads, voice, interviews, feedback, onboarding, churn
```

---



## Complete file reference

Every file in the repository, what it is, and who uses it.

### Root


| File        | Type          | Used by      | Purpose                                                                                                   |
| ----------- | ------------- | ------------ | --------------------------------------------------------------------------------------------------------- |
| `SKILL.md`  | Parent skill  | Cursor agent | Main instructions: operating loop, evidence rules, how to load capabilities. **This is the entry point.** |
| `README.md` | Documentation | Humans       | Skill library index, roadmap, how to add skills.                                                          |
| `docs.md`   | Documentation | Humans       | Repository map and plain-language guide (this file).                                                      |
| `LICENSE`   | Legal         | Humans       | MIT license.                                                                                              |




### `framework/` — orchestration


| File                               | Type     | Used by               | Purpose                                                                                     |
| ---------------------------------- | -------- | --------------------- | ------------------------------------------------------------------------------------------- |
| `framework/planner.md`             | Protocol | Parent agent          | Turn a vague founder ask into a concrete objective, required evidence, and execution steps. |
| `framework/capability-registry.md` | Catalog  | Parent agent + router | Table of all capabilities with descriptions and launch/SEO routing hints.                   |
| `framework/router.md`              | Protocol | Parent agent          | Select minimum capabilities, set order, parallel vs sequential, avoid redundant research.   |
| `framework/context-compressor.md`  | Protocol | Parent agent          | Compress capability output into facts, findings, risks, confidence — not full reports.      |
| `framework/evaluator.md`           | Protocol | Parent agent          | Decide if the objective is answered, find gaps/contradictions, suggest next capabilities.   |
| `framework/decision-framework.md`  | Protocol | Parent agent          | Map evidence to BUILD / MODIFY / TEST / WAIT / KILL recommendations.                        |
| `framework/synthesizer.md`         | Protocol | Parent agent          | Format the final founder response: recommendation, findings, why it matters, next steps.    |


### `capabilities/` — skills by category

See the generated skill tables in [README.md](./README.md#skills) (source of truth: each `AGENT.md` frontmatter). Categories: `build`, `grow`, `seo`, `customers`.

---

## Capability quick-pick (common founder questions)


| Founder asks…                               | Start with                                                                 |
| ------------------------------------------- | -------------------------------------------------------------------------- |
| Should I build this?                        | `market-intelligence` → `competitor-intelligence` → `pricing-intelligence` |
| What is this product / who is the customer? | `saas-discovery`                                                           |
| What SEO pages should I create?             | `seo-opportunity`                                                          |
| My site is live — is Google indexing it?    | `launch-foundation-audit`                                                  |
| Pre-launch — what SEO am I missing?         | `saas-seo-discovery`                                                       |
| How do I launch on Product Hunt?            | `saas-launch`                                                              |
| Where should I list my SaaS?                | `directory-launch`                                                         |
| Am I visible in ChatGPT / AI search?        | `geo-aeo-audit`                                                            |
| Write me an SEO page                        | `seo-page-generator`                                                       |
| My blog traffic is dropping                 | `content-decay-recovery`                                                   |


---



## Adding a new capability (checklist)

1. Create `capabilities/<category>/<name>/AGENT.md` (start from `templates/AGENT.template.md`)
2. Add YAML frontmatter:
  ```yaml
   ---
   name: your-capability-name
   description: One sentence — what it does and when to use it.
   ---
  ```
3. Run `python3 scripts/sync-registry.py` (updates README + registry tables)
4. If it overlaps with existing capabilities, add routing hints to `framework/router.md`

You do **not** need to change `SKILL.md` unless the parent operating loop itself changes.

---

## Key design rules

- **Minimum capabilities** — Run only what the question needs.
- **Evidence over assumptions** — Separate facts, findings, assumptions, recommendations.
- **No fake data** — Do not invent Search Console stats, traffic, or indexing numbers.
- **Founder-facing output** — One clear answer, not raw capability dumps.
- **Capabilities are read-only** — Parent agent loads `AGENT.md`; it does not rewrite them unless asked.

