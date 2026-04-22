# Recommended Auth and Model Routing Policy v1

Status: Draft recommendation
Owner: Security
Date: 2026-04-22

## Purpose
Provide a compact recommended policy for auth and model routing in Lyra OS after the 2026-04-08 auth-loss / fallback / config-recovery incident and the 2026-04-22 posture review.

This policy is intended to reduce ambiguity, silent degraded mode, and accidental cost exposure while preserving practical operational continuity.

## Baseline recommendation
### Primary steady-state route
Use:
- provider/auth route: `openai-codex`
- default model: `gpt-5.4`

This is the currently verified live route for both checked agents and should remain the default steady-state posture unless a deliberate model-change decision is made.

## Recommended routing model
### 1. Primary route
Define one explicit primary route per agent or lane.

Default current recommendation:
- `main` -> `openai-codex/gpt-5.4`
- `px-internal-dev` -> `openai-codex/gpt-5.4`

Rule:
The system should always be able to say what the intended primary route is for a given lane.

### 2. Fallback route
Fallback may exist, but it should be treated as:
- explicitly bounded
- visible to the operator
- not equivalent to healthy primary operation

Rule:
Fallback is a resilience tool, not the default truth surface.

### 3. Canary / evaluation route
New models should first enter the system through a bounded canary or evaluation path rather than instant global replacement.

Recommended use cases:
- test one new Codex model on one bounded agent/lane
- compare output quality, stability, and operator trust
- verify config/runtime support before broader rollout

### 4. Restricted / no-fallback workloads
Some workflows should not continue silently on fallback if the primary route fails.

Recommended categories for restricted fallback:
- higher-trust operator-control tasks
- high-cost unattended tasks
- tasks where route identity materially affects decision quality or control assumptions

Rule:
If route identity matters materially, fail visibly or pause rather than silently substituting another route.

## Health-state policy
### Healthy
Only classify as healthy when:
- the intended primary route is active
- the expected model mapping is in place
- no unacknowledged fallback is carrying the relevant load

### Degraded
Classify as degraded when:
- service is still functioning
- but fallback is active, route identity is uncertain, or auth instability is present

### Failed
Classify as failed when:
- the intended primary route is unavailable and no acceptable bounded continuation path exists

### Unknown
Classify as unknown when:
- the system appears responsive but the actual route cannot be established honestly

Rule:
Responsive service alone is not sufficient for `healthy`.

## Fallback policy
### Allowed fallback
Fallback may be allowed when all of the following are true:
- the affected workload is not in a restricted category
- the fallback route is visible and acknowledged
- cost exposure is bounded
- operator assumptions remain acceptable under the substitute route

### Not allowed silently
Fallback should not happen silently for:
- operator-control actions with meaningful trust implications
- tasks likely to consume meaningful credits/cost without visibility
- workflows whose correctness depends materially on model/provider identity

### Recommended default
If fallback is used, surface it explicitly as:
- degraded mode
- current route in use
- expected next recovery action

## Model upgrade policy
### 1. Do not auto-promote newly available models to primary
If OpenAI exposes a newer Codex model, do not immediately switch all live agents.

### 2. Use bounded evaluation first
For each candidate new model:
- verify OpenClaw supports the exact route/model string
- test on one bounded lane or agent
- compare quality, stability, and operational behavior
- decide whether to adopt, canary further, or reject

### 3. Promote only by explicit decision
Promotion from candidate to primary should be explicit and recorded in the appropriate decision / product / operating artifact.

## Recovery policy
When auth or route instability occurs:
1. treat the event as an operational-health issue
2. distinguish auth failure from route drift from post-change regression
3. contain hidden fallback/cost risk
4. restore the intended route
5. verify actual route restoration before declaring healthy

## Minimum operator visibility expectations
A workable routing posture should make these visible on demand:
- intended primary route
- actual current route if different or degraded
- whether fallback is active
- whether route identity is uncertain
- whether restoration has been verified on at least one bounded practical workload

## Recommended near-term operating stance
Until a more explicit control surface exists, use this practical stance:
- keep `openai-codex/gpt-5.4` as the primary route
- allow model evolution only through bounded evaluation first
- treat fallback as degraded, not healthy
- avoid silent fallback on high-trust or high-cost workflows
- require explicit route-restoration proof after auth incidents

## Short conclusion
Recommended policy:
- one explicit primary route per lane
- fallback only when bounded and visible
- canary new models before promotion
- no silent substitution where trust, control, or cost meaningfully matters
- route recovery is complete only after actual route verification
