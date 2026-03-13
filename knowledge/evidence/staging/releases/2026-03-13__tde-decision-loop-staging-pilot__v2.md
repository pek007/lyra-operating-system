# TDE Decision Loop Staging Pilot v2

Date: 2026-03-13
Status: Pilot executed successfully after parking-rule fix
Owner: Peter + Lyra
Scope: Staging validation of bounded `research_further` -> research activation -> re-entry -> continuation

## Purpose
Rerun the same staging pilot after implementing the origin-task parking / non-claimable rule.

## Seeded pilot tasks
- `TDE-STAGE-ORIGIN-001`
- `TDE-STAGE-RESEARCH-001`
- `TDE-STAGE-CONTINUE-001`

## Commands executed
- export staging projection
- run staging tick 1b
- run staging tick 2b

Artifacts
- `knowledge/evidence/staging/2026-03/tde-stage-pilot-tick-1b.json`
- `knowledge/evidence/staging/2026-03/tde-stage-pilot-tick-2b.json`
- `knowledge/evidence/staging/2026-03/tde-decision-advancement-tde-stage-origin-001-20260313-161038.json`
- `knowledge/evidence/staging/2026-03/tde-decision-advancement-tde-stage-research-001-20260313-161038.json`

## Result summary
### Tick 1b
- origin task claimed
- `research_further` selected
- origin task became non-claimable (`decision_claim_blocked = true`)
- research task activated

### Tick 2b
- research task, not origin task, was claimed
- research task executed and wrote back to `Waiting`
- origin decision re-entered with outcome `continue`
- continue task activated
- origin task was unparked (`decision_claim_blocked = false`)

## What is now proven end to end
In staging, the bounded loop now works across two ticks:
1. origin task selects `research_further`
2. bounded research task activates
3. origin task is parked and skipped by claimant selection
4. research task executes
5. origin decision re-enters
6. continue successor activates

## Important runtime state observation
After successful re-entry:
- origin task remains logically active in the broader workflow sense
- but is no longer claim-blocked
- research task returns to `Waiting` after execution under current writeback semantics
- continue task becomes `Active`

## Interpretation
The missing runtime rule exposed by v1 has now been implemented successfully.

The system now has a practical, governed recursive decision loop in staging.

## Remaining considerations
Potential future refinement areas:
- whether origin task should remain `Active` or move to a more explicit parked/awaiting-reentry state
- whether research tasks should return to `Waiting` or transition to a more explicit completed evidence state
- richer evidence/confidence propagation into the re-entry decision record

## Bottom line
The staged decision loop now works end to end for the bounded `research_further -> re-entry -> continue` path.
