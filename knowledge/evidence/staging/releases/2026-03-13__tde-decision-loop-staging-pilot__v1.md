# TDE Decision Loop Staging Pilot v1

Date: 2026-03-13
Status: Pilot executed
Owner: Peter + Lyra
Scope: Staging validation of bounded `research_further` -> research activation -> recursive decision loop behavior

## Purpose
Run the new decision loop in a realistic staging path and observe end-to-end behavior.

## Seeded pilot tasks
- `TDE-STAGE-ORIGIN-001`
- `TDE-STAGE-RESEARCH-001`
- `TDE-STAGE-CONTINUE-001`

Workflow intent:
1. Origin task selects `research_further`
2. Research task becomes active
3. Research task should later complete and re-enter the origin decision
4. Post-research continuation should activate the continue task

## Commands executed
- export staging projection
- run staging tick 1
- run staging tick 2

Artifacts:
- `knowledge/evidence/staging/2026-03/tde-stage-pilot-tick-1.json`
- `knowledge/evidence/staging/2026-03/tde-stage-pilot-tick-2.json`
- `knowledge/evidence/staging/2026-03/tde-decision-advancement-tde-stage-origin-001-20260313-160108.json`
- `knowledge/evidence/staging/2026-03/tde-decision-escalation-tde-stage-origin-001-job-tick-20260313-160108.json`

## What worked
### Tick 1
Observed:
- origin task claimed
- `research_further` selected
- decision advancement record emitted
- research task activated in staging DB

This proves the first half of the loop works in staging.

## What did not work as intended
### Tick 2
Observed:
- origin task was claimed again
- origin task escalated because research budget was now exhausted
- research task was still `Active`
- continue task remained `Waiting`

### Root cause
The origin task remained `Active` after the `research_further` decision.
That means the runtime still considered it claimable on the next tick.

As a result, the second tick did not naturally progress through:
- research task execution,
- re-entry,
- and post-research continuation.

Instead, it reprocessed the origin task and hit the budget bound.

## Interpretation
This pilot is useful because it validates the architecture and exposes the next missing runtime rule:

When a task selects `research_further`, the origin task should no longer remain normally claimable in the same way.

We need a bounded park/defer state for the origin decision while the research child is active.

## Conclusion
### Proven
- `research_further` artifacting works
- bounded research successor activation works
- research budget enforcement works
- forced escalation on budget exhaustion works

### Not yet proven end-to-end in staging
- research task completion -> re-entry -> continue-task activation in a realistic multi-tick staging run

## Required next fix
Add an origin-task parking rule for `research_further`, so the origin task is not re-claimed while the bounded research task is active.

Possible implementation directions:
1. move origin task out of `Active` after `research_further`
2. mark origin task with a non-claimable runtime status/flag while research is in progress
3. teach claimant selection to skip origin tasks with an active research child

## Recommendation
Implement the parking/non-claimable rule next, then rerun the same staging pilot.
