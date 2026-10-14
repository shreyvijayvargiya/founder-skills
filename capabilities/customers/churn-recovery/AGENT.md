---
name: churn-recovery
description: Diagnose why customers cancel or go inactive, and create win-back, save-offer, and prevention plays. Use when churn or cancellations are hurting MRR.
---

# Churn Recovery

## Mission

Explain why customers leave and recover the revenue that is still recoverable.

Use when the user asks:

- Why are customers cancelling?
- How do I win back churned users?
- What should my cancellation flow do?

## Input

Required:

- Cancellation reasons, churned-customer list, or description of the churn problem

Optional:

- Plan, tenure, usage before cancel
- Billing data (failed payments)
- Existing cancel flow and emails

## Workflow

### 1. Split Churn Types

- Involuntary (failed payment) → dunning fix
- Voluntary: never activated / outgrew / switched / price / project ended

Treat them separately; involuntary is usually the cheapest win.

### 2. Find Patterns

Compare churned vs retained: tenure, plan, early usage, acquisition channel. Note the earliest warning signal.

### 3. Plays

- Dunning: retry schedule, card-update emails
- Cancel flow: one-question reason capture, pause/downgrade offer matched to the reason
- Win-back: segmented emails by reason, timed 14 / 30 / 90 days
- Prevention: health signals to watch, proactive founder outreach triggers

### 4. Measure

Define churn rate, recovered MRR, and save rate; state the baseline needed first.

## Output

- Churn breakdown by type and reason
- Earliest-warning-signal hypothesis
- Prioritized plays with draft copy (cancel survey, win-back emails)
- One experiment and the metric that decides it

## Quality Rules

- Do not assume reasons; use stated reasons plus behavior.
- Small cohorts: say the sample is too small to conclude.
- Never recommend dark patterns that block cancellation.
