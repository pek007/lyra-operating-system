# TDE Assignment Limbo Detection Note — 2026-03-15

Owner: Lyra  
Linked task: `TASK-20260315-CP-TDE-ASSIGNMENT-ACCEPTANCE`

## Purpose
Add a first explicit detector for the silent-limbo condition so assignment failures become visible without depending on manual forensic inspection.

## Detection rule (v1)
Flag an assignment when all are true:
- assignment exists in `assignment_packets`
- acceptance state is one of the normal accepted states that imply expected downstream movement (`accepted`)
- the assignment is older than a bounded stale interval
- no intake trace is found linked to the assignment
- no follow-on non-assignment event is found for the assignment/task

## What is intentionally not flagged
- `duplicate`
- `rejected_invalid_assignment`
- `accepted_no_runner`
- `accepted_pending_binding`

Those are already explicit outcomes rather than silent limbo.

## Runtime artifact
Detector script:
- `tools/tde_assignment_limbo_check.py`

Test:
- `tools/tde_assignment_limbo_check_tests.py`

## Current value
This does not solve execution pickup by itself.
It solves observability: accepted assignments that go quiet can now be surfaced as visible findings.

## Recommended next operational use
- run after assignment-related changes
- add to a bounded TDE health check / cron path later if useful
- use findings to tighten producer adapter linkage, intake linkage, and runner pickup semantics

## Bottom line
Silent limbo is now detectable as a first-class condition instead of only discoverable through manual investigation.
