---

name: founder-os-router
description: Select the minimum relevant Founder OS capabilities and determine their execution order.
-----------------------------------------------------------------------------------------------------

# Router

The Router decides **which capabilities should execute**.

It must not automatically select every capability related to the topic.

---

# Inputs

Receive:

* Objective
* Planner output
* Available capabilities
* Project context
* Previous findings
* Unknowns

---

# Selection Rules

Select a capability only when it materially contributes to the objective.

For every selected capability, identify:

* Capability name
* Reason
* Required input
* Expected output
* Dependencies
* Priority

---

# Prefer Specificity

If the objective is:

> "Find Reddit acquisition opportunities."

Use:

```text
Reddit Growth
```

Do not automatically run:

```text
X Growth
LinkedIn Growth
YouTube Growth
```

---

# Launch Routing

If the objective is about launching or SEO setup, pick one primary capability.

| Objective signal | Route to |
|------------------|----------|
| Site is live; indexing, Search Console, sitemap, analytics, GBP, listings | `launch-foundation-audit` |
| Pre-launch SEO baseline; missing pages and quick wins | `saas-seo-discovery` |
| Product Hunt, channels, launch timeline, launch assets | `saas-launch` |
| Directory submissions and listing copy | `directory-launch` |
| Keyword/content SEO growth strategy | `seo-opportunity` |
| AI answer-engine visibility (ChatGPT, Perplexity, etc.) | `geo-aeo-audit` |

Do not route `saas-launch` for "why isn't Google indexing my site?"

Do not route `launch-foundation-audit` for "create my Product Hunt launch plan."

See `framework/capability-registry.md` for the full catalog.

---

# Prefer Evidence Chains

When one capability produces information required by another, create a dependency.

Example:

```text
Market Intelligence
        ↓
Competitor Intelligence
        ↓
Pricing Intelligence
```

---

# Parallel Execution

Capabilities may execute in parallel when they do not depend on each other.

Example:

```text
                ┌── Reddit Growth
                │
Customer Plan ──┼── LinkedIn Growth
                │
                └── Outbound
```

---

# Avoid Redundant Research

Do not select a capability when:

* The required information is already sufficiently known.
* The same research was recently completed.
* The capability would not change the decision.
* Another selected capability already provides the required evidence.

---

# Routing Priority

Prioritize:

1. Capabilities that answer critical unknowns
2. Capabilities that can invalidate the current assumption
3. Capabilities with strong evidence potential
4. Capabilities required by downstream steps
5. Nice-to-have research last

---

# Re-routing

The Router may be called again after evaluation.

Example:

```text
Initial plan
    ↓
Market Intelligence
    ↓
Evaluator
    ↓
Missing:
Willingness to pay
    ↓
Router
    ↓
Pricing Intelligence
```

Do not reuse the exact same capability unless the new execution has a materially different objective or input.

---

# Router Output

```yaml
routes:
  - capability: ""
    reason: ""
    priority: 1
    depends_on: []
    input_context:
      objective: ""
      relevant_findings: []
      open_questions: []

execution:
  parallel_groups:
    - []
  sequential_steps:
    - []
```

The Router should optimize for **minimum sufficient execution**.
