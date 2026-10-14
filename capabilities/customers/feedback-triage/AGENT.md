---
name: feedback-triage
description: Turn raw customer feedback (emails, support chats, reviews, DMs) into ranked themes, bug vs feature requests, and a small what-to-build-next list. Use when feedback is piling up.
---

# Feedback Triage

## Mission

Convert a pile of unstructured feedback into a ranked, decision-ready list a solo founder can act on this week.

Use when the user asks:

- What should I build next based on this feedback?
- Sort these support emails / reviews / DMs
- Which requests are noise?

## Input

Required:

- Raw feedback (pasted text, exported file, or a list of sources)

Optional:

- Customer plan / revenue per account
- Product roadmap or current focus
- Time period

## Workflow

### 1. Normalize

One row per distinct piece of feedback: source, date, customer, plan, verbatim.

### 2. Classify

Bug · Missing feature · UX friction · Pricing/billing · Docs/onboarding · Praise · Out of scope.

### 3. Cluster And Weigh

Group duplicates into themes. Score each theme:

- Frequency (distinct customers, not messages)
- Revenue at stake (paying vs free)
- Severity (blocks use / annoys / nice-to-have)
- Effort guess (S / M / L, labelled as a guess)

### 4. Decide

Rank by (frequency × revenue × severity) ÷ effort. Separate "fix now", "queue", "ignore with reason".

## Output

| Theme | Type | Customers | Revenue at stake | Severity | Effort | Action |
|-------|------|-----------|------------------|----------|--------|--------|

- Top 3 to ship this week
- Reply drafts for the customers behind the top themes (so they hear back)
- Patterns worth a follow-up interview (hand to `customer-interview-guide`)

## Quality Rules

- Count customers, not messages.
- Do not let the loudest user outrank paying majority signal.
- Keep verbatim quotes short and real.
