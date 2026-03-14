# TDE Task Closure Runtime Path v1

Status: Draft active
Owner: Peter + Lyra
Product: Task Management (`A-007`)
Date: 2026-03-14
Related:
- `products/task-management/07-decisions/TDE_TASK_CLOSURE_AND_FEEDBACK_POLICY_V1.md`
- `schemas/tde_task_closure_record/v1.0.0.schema.json`
- `tools/tde_task_close.py`

## Purpose
Embodied runtime path for closing a TDE task with a structured closure record.

This path gives the closure/feedback policy a first executable implementation so meaningful task endings do not depend only on prose or chat interpretation.

## What the runtime path does
The v1 path:
1. builds or accepts a `tde_task_closure_record`
2. validates it against the registered schema
3. persists the closure record in canonical sqlite state
4. updates task metadata with closure information
5. updates task runtime status according to closure state
6. emits a task-closed event record
7. applies bounded automatic follow-up for selected feedback outcomes

Current bounded automatic follow-up support:
- `close_and_chain` -> activate explicit follow-up refs and apply ready-promotion checks
- `close_and_escalate` -> create escalation package artifact
- `close_and_improve` -> create a lightweight improvement follow-up artifact in the owning product/runtime path
- `close_as_error` -> create a lightweight error report artifact aligned to the error-reporting standard

## Current status mapping
Current v1 runtime mapping is:
- `Done` -> task status `Done`
- `Blocked` -> task status `Waiting`
- `Deferred` -> task status `Waiting`
- `Escalated` -> task status `Waiting`

Interpretation:
- the richer closure meaning lives in the closure record and task metadata
- the current runtime status model remains intentionally thin
- future runtime versions may introduce richer native status/state handling

## Why this is acceptable for v1
The goal of v1 is not to perfect the final state model.
The goal is to ensure that closure meaning becomes durable, validated, and queryable in the canonical store.

## Current implementation note
The first implementation exists at:
- `tools/tde_task_close.py`

The first tests exist at:
- `tools/tde_task_close_tests.py`

## Next likely follow-on work
- add explicit decision/escalation/improvement follow-up creation from closure outcomes
- integrate closure records into task projections and control-panel views
- decide whether richer native terminal/handoff statuses should exist directly in runtime state
