# TDE Decision Loop Staging Pilot — Defer and Block Paths v1

Date: 2026-03-13
Status: Pilots executed successfully in isolated staging-style fixtures
Owner: Peter + Lyra
Scope: Staging validation of bounded `research_further -> research activation -> re-entry -> defer|block`

## Purpose
Complete the initial outcome-family validation set by testing the newly supported re-entry outcomes `defer` and `block` in deterministic isolated fixtures.

## Defer path result
### Intended flow
1. Origin task selects `research_further`
2. Research task activates
3. Research task executes
4. Origin decision re-enters with outcome `defer`

### Observed result
- tick 1 claimed the origin task and selected `research_further`
- tick 2 claimed the research task and executed it
- re-entry selected `defer`
- origin task remained claim-blocked and was marked with:
  - `decision_deferred = true`
- no follow-up task was activated

### Key artifacts
- `knowledge/evidence/staging/2026-03/tde-stage-defer-pilot-iso-tick-1.json`
- `knowledge/evidence/staging/2026-03/tde-stage-defer-pilot-iso-tick-2.json`
- `knowledge/evidence/staging/2026-03/tde-decision-advancement-tde-stage-defer-origin-iso-001-20260313-170248.json`
- `knowledge/evidence/staging/2026-03/tde-decision-advancement-tde-stage-defer-research-iso-001-20260313-170248.json`
- `knowledge/evidence/staging/2026-03/tde-stage-defer-research-note.md`

## Block path result
### Intended flow
1. Origin task selects `research_further`
2. Research task activates
3. Research task executes
4. Origin decision re-enters with outcome `block`

### Observed result
- tick 1 claimed the origin task and selected `research_further`
- tick 2 claimed the research task and executed it
- re-entry selected `block`
- origin task remained claim-blocked and was marked with:
  - `decision_blocked = true`
- no follow-up task was activated

### Key artifacts
- `knowledge/evidence/staging/2026-03/tde-stage-block-pilot-iso-tick-1.json`
- `knowledge/evidence/staging/2026-03/tde-stage-block-pilot-iso-tick-2.json`
- `knowledge/evidence/staging/2026-03/tde-decision-advancement-tde-stage-block-origin-iso-001-20260313-170248.json`
- `knowledge/evidence/staging/2026-03/tde-decision-advancement-tde-stage-block-research-iso-001-20260313-170248.json`
- `knowledge/evidence/staging/2026-03/tde-stage-block-research-note.md`

## Interpretation
These pilots confirm that the bounded re-entry outcome set is now functioning in isolated staging-style validation for:
- `continue`
- `retry`
- `defer`
- `block`
- and earlier `escalate` artifact generation / budget-forced escalation behavior

## Current runtime semantics clarified
- `continue` -> activates the specified next task and un-parks the origin
- `retry` -> activates the specified retry task and un-parks the origin
- `defer` -> keeps the origin claim-blocked and marks it deferred
- `block` -> keeps the origin claim-blocked and marks it blocked
- `escalate` -> emits escalation package and un-parks the origin

## Bottom line
The bounded re-entry outcome family is now validated across isolated staging-style pilots for all major intended outcomes except `branch` and `complete_stop`, which remain design-level rather than runtime-embodied in this slice.
