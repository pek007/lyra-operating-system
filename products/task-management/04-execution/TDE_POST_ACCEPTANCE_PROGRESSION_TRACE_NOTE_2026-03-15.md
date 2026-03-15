# TDE Post-Acceptance Progression Trace Note — 2026-03-15

Owner: Lyra  
Linked task: `TASK-20260315-CP-TDE-ASSIGNMENT-ACCEPTANCE`

## Purpose
Define and implement the first canonical post-acceptance progression trace so accepted assignments stop looking silent once they actually enter a visible downstream path.

## Change
Added runtime event emission for the first meaningful post-acceptance traces:
- `task_activated` when a task is explicitly activated in canonical DB flow
- `task_progressed` when a claimed task is written back by the job tick
- one-time `assignment_progressed` backfill support for already-existing accepted assignments that predate this trace

## Why this matters
The limbo detector correctly showed that accepted assignments still looked silent because the system had:
- acceptance events
- task rows
- but no follow-on runtime trace

This change gives the system a minimal canonical answer to:
- “what happened after acceptance?”

## Current interpretation
A valid non-silent path now includes one or more of:
- `task_activated`
- `task_progressed`
- `task_closed`
- `assignment_progressed` (backfill compatibility for already-existing assignments)

## Boundary of this slice
This is still a thin slice.
It does not model the entire execution lifecycle.
It does provide the first reliable observable step after assignment acceptance.

## Bottom line
Accepted assignments now have a canonical path to visible downstream trace instead of relying only on the initial `assignment_accepted` event.
