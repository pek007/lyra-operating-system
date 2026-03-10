# A-005 — Autoresearch / Ralph Loop Note

Date: 2026-03-10
Owner: Lyra
Source report: `library/self-improvement/2026-03-10__autoresearch-ralph-loop-report.md`
Status: Active guidance note

## Verdict
Use the report as a **pattern source**, not as a blueprint to implement wholesale.

## Adopt
### 1) Externalized-state loop discipline
Adopt the principle that long-running improvement loops should keep state in artifacts, ledgers, tests, and evidence rather than growing chat context.

Why this fits us:
- already aligned with TDE/event/evidence patterns
- reduces context drift and hidden state
- makes retries safer and more auditable

### 2) Strict evaluation gates
Adopt the rule that no self-improvement change is accepted without explicit evaluation against fixed criteria.

Why this fits us:
- already aligned with `SELF_IMPROVEMENT_LOOP_V1.md`
- reduces opinion-driven changes
- supports promote/rollback discipline

### 3) Protected mutation surface
Adopt explicit allow/deny boundaries for autonomous improvement work.

Why this fits us:
- we already have strong guardrail posture
- prevents autonomous drift into governance, permissions, credentials, or broad repo churn
- is a prerequisite for safe automation

### 4) Bounded repeat-until-done loops for mechanical objectives
Adopt Ralph-style bounded retry loops only for objectives with clear completion tests.

Best initial use cases:
- validation-green loops
- CI-green loops
- deterministic repair of known low-risk failures

## Defer
### 1) General-purpose autoresearch harness
Defer a broad always-on mutation/evaluation engine until the narrow v1 loop is proven safe and useful.

Reason:
- high risk of scope drift, weak metrics, and runaway automation before the protected-surface model is mature

### 2) Portfolio-wide autonomous self-improvement
Defer broad cross-product autonomous improvement until A-005 weekly synthesis, closed-loop incident handling, and scorecards are operating reliably.

Reason:
- current governance/process base is promising but not yet mature enough for wide autonomous operation

### 3) ML-style experiment tracking platform adoption
Defer tooling such as MLflow unless the native evidence/event model becomes a bottleneck.

Reason:
- we should earn the need first; otherwise we add stack weight before proving the loop

## Reject for now
### 1) Fine-tuning / training loops
Reject for this phase.

Reason:
- out of scope relative to current `SELF_IMPROVEMENT_LOOP_V1.md`
- introduces cost, safety, and governance burden too early

### 2) Indefinite autonomous loops without hard stop-loss
Reject outright.

Reason:
- incompatible with current safety posture
- creates cost, churn, and governance risk

### 3) Broad mutation rights across repo governance/runtime surfaces
Reject outright.

Reason:
- violates the principle of bounded autonomous change
- increases blast radius before verification maturity exists

## Concrete follow-up actions
### Follow-up 1 — Define protected mutation policy
Create an A-005/OS policy that explicitly states:
- protected paths that autonomous improvement loops may not change
- allowed mutation paths for narrow experiments
- stop-loss conditions and human escalation points

### Follow-up 2 — Define a minimal experiment record
Add a lightweight experiment record format capturing:
- objective
- mutation surface
- metric/evaluation rule
- stop rule
- outcome
- promote/rollback decision
- evidence links

### Follow-up 3 — Pilot one bounded Ralph loop
Run one narrow loop only, ideally:
- validation-green or CI-green repair on a controlled repo surface
- no policy, credential, permission, or architecture changes
- hard iteration and time limits

### Follow-up 4 — Add scorecard metrics for loop quality
Track at minimum:
- convergence rate
- median iterations to completion
- revert rate
- safety/policy violation count
- recurrence of same failure class after “fix”

### Follow-up 5 — Use incident-driven eval growth
When a failure recurs, prefer turning it into a regression/eval artifact before expanding autonomy.

## Recommendation
Proceed with a **narrow, evidence-backed v1**:
- safe bounded loops
- protected mutation surface
- explicit evaluation gates
- no training loops
- no general autonomous optimization engine yet

That gives us the upside from the report without importing its risk profile wholesale.
