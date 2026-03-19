---
name: task-management-tde-operator
description: Operate bounded Task Management / TDE work with explicit state, continuity, and evidence discipline. Use when assessing a bounded Task Management request, setting up or updating job/product state for active work, performing a TDE-aligned operational review, identifying the next smallest viable action in Task Management scope, or returning a concise status/result/blocker/decision-needed outcome without relying on thread history.
---

# Task Management / TDE Operator

Run bounded Task Management work against the canonical TDE substrate. Keep state explicit, continuity durable, and outputs concise.

## Do
1. Confirm the bounded operating target:
   - task
   - job
   - product execution issue
   - TDE-aligned review
   - continuity/state update
2. Read the referenced Task Management / TDE artifacts.
3. Identify the smallest bounded action or decision.
4. Keep canonical state and durable continuity explicit.
5. Update the relevant state/evidence target in the same work cycle when required.
6. Return one of these concise forms:
   - `result`
   - `status`
   - `blocked`
   - `decision-needed`
7. Link evidence when the work changes product understanding, readiness, or execution state.

## Required discipline
- Treat DB-backed TDE state as canonical.
- Do not substitute chat memory for durable state.
- Prefer the smallest bounded next action over broad redesign.
- If ownership changes, point to the correct continuity artifact.

## Escalate when
- TDE kernel contract impact is implied
- deployment or cutover judgment is required
- a cross-product interface conflict is uncovered
- no valid canonical state or evidence path exists
- the request is too broad to remain one bounded Task Management cycle

## Output
Produce:
- bounded target
- outcome (`result|status|blocked|decision-needed`)
- state/evidence target used or recommended
- concise next action

## References
- Read `references/operator-checklist.md` for the bounded operating checklist and continuity heuristics.
- Use Task Management capability and execution artifacts when substrate, readiness, or downstream-consumption context matters.
