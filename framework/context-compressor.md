---
name: founder-os-context-compressor
description: Convert capability outputs into compact structured context that can safely and efficiently be passed to other capabilities.
---

# Context Compressor

The Context Compressor converts detailed capability output into reusable working context.

Its purpose is to prevent large reports from being repeatedly passed between capabilities.

---

# Core Principle

**Pass decisions and useful evidence, not entire reports.**

A downstream capability should receive only information relevant to its task.

---

# Input

Receive:

* Original objective
* Capability output
* Existing working context
* Downstream capability requirements

---

# Extract

Identify:

### Facts

Directly observed information.

### Findings

Evidence-supported conclusions.

### Opportunities

Potential actions or market opportunities.

### Risks

Potential problems or negative signals.

### Evidence

Sources, observations, data, or examples supporting findings.

### Confidence

How strongly the evidence supports the finding.

### Open Questions

Important unknowns remaining.

### Recommendations

Actions suggested by the capability.

---

# Remove

Do not carry forward:

* Repeated explanations
* Generic advice
* Irrelevant background
* Long prose
* Duplicate findings
* Unsupported speculation
* Internal reasoning
* Information unrelated to the next task

---

# Compression Format

Use:

```yaml
objective: ""

facts:
  - ""

findings:
  - ""

opportunities:
  - ""

risks:
  - ""

evidence:
  - source: ""
    supports: ""

confidence:
  overall: 0.0
  notes: ""

open_questions:
  - ""

recommendations:
  - ""

decisions_affected:
  - ""
```

---

# Relevance Filtering

When passing context to another capability, filter it.

For example:

Reddit Growth does not need the entire Pricing Intelligence report.

It may only need:

```yaml
product: ""
icp: ""
customer_problem: ""
target_market: ""
relevant_competitors: []
relevant_findings: []
```

---

# Contradictions

If new evidence conflicts with existing context:

```text
Existing:
Customers prefer monthly pricing.

New evidence:
Most interviewed customers prefer annual plans.
```

Do not silently overwrite.

Record:

```yaml
contradictions:
  - existing: ""
    new_evidence: ""
    resolution: ""
```

---

# Compression Quality

A compressed context is successful when another capability can perform its job without needing the original full report.

Prefer concise structured information over prose.

Never compress away evidence that materially affects the decision.
