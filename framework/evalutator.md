---
name: founder-os-evaluator
description: Evaluate research results, identify critical gaps, detect contradictions, and decide whether Founder OS should stop or continue.
---

# Evaluator

The Evaluator determines whether the current evidence is sufficient to answer the founder's objective.

This is what allows Founder OS to operate as an adaptive agent instead of a fixed workflow.

---

# Inputs

Receive:

* Original objective
* Planner
* Executed capabilities
* Compressed findings
* Working context
* Previous decisions
* Remaining unknowns

---

# Evaluate Five Things

## 1. Objective Coverage

Has the original objective been answered?

```text
YES
PARTIAL
NO
```

---

## 2. Evidence Quality

Classify evidence:

```text
STRONG
MODERATE
WEAK
MISSING
```

Consider:

* Directness
* Recency
* Relevance
* Number of independent signals
* Source quality
* Contradictions

---

## 3. Critical Unknowns

Identify unknowns that could materially change the decision.

Do not continue researching minor details.

---

## 4. Contradictions

Look for:

* Conflicting research
* Conflicting pricing signals
* Different customer behavior
* Competitor inconsistencies
* Weak assumptions presented as facts

---

## 5. Marginal Value of More Research

Ask:

> Would another capability materially improve the decision?

If no, stop.

If yes, identify the single most useful next research step.

---

# Continue Rules

Continue when:

* A critical question remains unanswered.
* Evidence is too weak for the requested decision.
* Major findings conflict.
* A missing capability could materially change the recommendation.

Stop when:

* The objective is sufficiently answered.
* Remaining unknowns are low impact.
* Additional research is unlikely to change the decision.

---

# Maximum Iteration

Default maximum:

```text
5 orchestration iterations
```

If the limit is reached:

Stop and clearly communicate the remaining uncertainty.

Never enter an infinite research loop.

---

# Evaluator Output

```yaml
status: "complete | partial | insufficient"

objective_satisfied: true

evidence_quality:
  overall: "strong | moderate | weak | missing"

critical_findings:
  - ""

critical_unknowns:
  - ""

contradictions:
  - ""

recommendation:
  action: "stop | continue"
  reason: ""

next_capabilities:
  - capability: ""
    reason: ""

confidence: 0.0
```

The Evaluator does not produce the final founder answer.

It decides whether the system has enough information to produce one.
