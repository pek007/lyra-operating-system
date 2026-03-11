# TASKS Reference Misuse Error Report — 2026-03-11

## Header
- Error ID: `ERR-SYS-2026-03-11-TASKS-REFERENCE-01`
- Date: `2026-03-11`
- Title: `New corrective actions were added to legacy TASKS.md despite its non-canonical status`
- Type: `process_failure`
- Scope: `system_level`
- Owning product or owner: `Lyra / shared system coordination`
- Affected products/contexts: `shared system coordination`, `Task Management / TDE context`, `governance/error-reporting workflow`
- Status: `mitigated`
- Review / closure date: `2026-03-18`

## Summary
- While trying to close the loop on the Git topology incident, new corrective actions were added to `TASKS.md`. That placement was conceptually inconsistent because `TASKS.md` is explicitly marked as a legacy/reference board rather than the canonical runtime system of record.

## Impact
- Actual impact:
  - corrective actions were placed in a location whose current authority is ambiguous or intentionally reduced
  - this risked reinforcing outdated operating habits and architectural confusion
- Potential impact:
  - future users/agents may keep treating `TASKS.md` as a live canonical inbox
  - corrective action placement may remain inconsistent across incidents
  - ambiguity between legacy reference boards and canonical action systems may persist

## Detection
- How was it detected?
  - Peter explicitly challenged why new items were being added to `TASKS.md`
- Detection gap, if any:
  - the closed-loop follow-up step did not first verify the correct canonical action system for shared/system corrective actions
  - the workspace still contains visible references and habits that make `TASKS.md` feel live enough to attract new actions

## Root cause
- Primary root cause:
  - corrective-action placement was optimized for immediacy rather than canonical action-system clarity
- Contributing factors:
  - `TASKS.md` still contains many open items and remains highly visible in the workspace
  - the canonical action system for shared/system corrective actions is not yet explicit enough
  - the new closed-loop model was applied faster than the action-placement architecture was clarified

## Immediate mitigation
- The newly added corrective items were removed from `TASKS.md`.
- The Git topology incident report was updated to mark the actions as still needing canonical placement.
- This error report was created to retain the lesson explicitly.

## Corrective actions
- [ ] Define or point to the canonical action system for shared/system corrective actions.
- [ ] Review whether `TASKS.md` still contains signals or references that make it look authoritative despite its legacy disclaimer.
- [ ] Tighten the closed-loop improvement guidance so action assignment explicitly checks canonical action placement before creating tasks.

## Preventive changes
- Before creating new corrective tasks, first confirm the canonical action register for that scope.
- Treat legacy/reference artifacts as read-mostly unless an explicit exception exists.
- Reduce architectural ambiguity where legacy artifacts still look operationally live.

## Linked artifacts
- Related tasks:
  - none yet assigned into the canonical action system
- Related decisions:
  - none yet
- Related evidence:
  - chat exchange identifying the issue
  - prior Git topology incident follow-up edits
- Related product/shared artifacts:
  - `TASKS.md`
  - `GIT_TOPOLOGY_AND_SYNC_ERROR_REPORT_2026-03-11.md`
  - `ERROR_REPORTING_STANDARD_V1.md`
  - `CLOSED_LOOP_IMPROVEMENT_MODEL_V1.md`

## Closure criteria
- canonical action placement for shared/system corrective actions is explicit
- no new corrective actions are added to `TASKS.md` unless its authority is deliberately changed
- legacy/reference status of `TASKS.md` is no longer easy to misread in practice

## Closure note
- Initial misuse corrected by removing the new items. Full closure depends on clarifying the canonical action system and reducing the residual ambiguity around `TASKS.md`.
