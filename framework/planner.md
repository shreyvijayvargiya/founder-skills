---
name: founder-os-planner
description: Create the smallest useful execution plan for a Founder OS objective before selecting capabilities.
---

# Planner

The Planner converts a founder request into an execution plan.

Its job is not to answer the request.

Its job is to determine **what must happen to answer it well**.

---

## Input

Receive:

* Founder objective
* Product/project context
* Previous findings
* Previous decisions
* Available capabilities
* Constraints

---

# Step 1 — Define the Objective

Rewrite the request as a concrete objective.

Example:

> "How do I get more users?"

Becomes:

> "Identify the highest-potential customer acquisition channels for this product and produce a prioritized acquisition plan."

---

# Step 2 — Identify the Decision

Determine what decision the founder is actually trying to make.

Common decisions:

* Build or don't build
* Which market to target
* Which customer segment to prioritize
* What to charge
* Which feature to build
* Which acquisition channel to focus on
* Whether to change positioning
* What to do next

---

# Step 3 — Identify Required Evidence

List only the information that could materially change the decision.

Example:

```text
Objective:
Should I build this SaaS?

Required evidence:

1. Customer problem
2. Existing alternatives
3. Demand
4. Monetization
5. Differentiation
6. Customer acquisition feasibility
```

Do not research information that cannot affect the decision.

---

# Step 4 — Check Existing Context

Before planning new research, identify what is already known.

Mark each requirement:

```text
KNOWN
PARTIALLY KNOWN
UNKNOWN
```

Avoid duplicating existing research.

---

# Step 5 — Build Execution Steps

Create the smallest useful sequence.

Example:

```text
Step 1
Market Intelligence

Step 2
Competitor Intelligence

Step 3
Pricing Intelligence

Step 4
Customer Acquisition Strategy

Step 5
Evaluate
```

---

# Step 6 — Identify Dependencies

A capability may depend on another capability.

Example:

```text
Market Intelligence
        ↓
Competitor Intelligence
        ↓
Pricing Intelligence
```

Independent capabilities can be grouped:

```text
              ┌── Reddit Growth
              │
Customer ─────┼── LinkedIn Growth
              │
              └── Outbound
```

---

# Step 7 — Define Success

Every plan should define what constitutes a sufficient answer.

Example:

> The objective is complete when we can recommend BUILD, MODIFY, TEST, WAIT, or KILL with reasonable confidence and clearly explain the remaining uncertainty.

---

# Planner Output

Return:

```yaml
objective: ""
decision: ""
known:
  - ""
unknown:
  - ""
required_evidence:
  - ""
steps:
  - id: 1
    purpose: ""
    capabilities: []
    depends_on: []
success_condition: ""
max_iterations: 5
```

Keep the plan concise.

The Planner should create a route, not a giant research document.
