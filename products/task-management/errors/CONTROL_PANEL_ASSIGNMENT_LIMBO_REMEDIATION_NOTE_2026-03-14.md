# Control Panel Assignment Silent-Limbo Remediation Note

Date: 2026-03-14
Owner: Task Management (`A-007`)
Related error: `products/task-management/errors/ERR-2026-03-14-control-panel-assignment-silent-limbo.md`

## Problem statement
The current Control Panel POC demonstrated that a task can be inserted into canonical TDE DB state without producing a trustworthy operational loop.

Observed characteristics:
- task row exists in `os/runtime/tde_state.sqlite`
- source marked `portfolio-poc`
- no visible intake record
- no visible execution pickup after insertion
- no explicit feedback to producer
- active runtime DB does not yet contain the newer intake/closure tables

## Immediate remediation goals
1. Remove ambiguity about whether an assignment was merely inserted or actually accepted for execution.
2. Ensure Control Panel uses a governed TDE interface rather than direct task-state mutation.
3. Make no-runner / no-binding / pathing problems visible to the producer.

## Proposed fix slices
### Slice 1 — Assignment adapter
Build a dedicated Control Panel → TDE assignment adapter that:
- emits canonical `tde_intake_packet`
- uses stable idempotency keys/source refs
- persists intake/triage outcome
- never treats raw DB insertion as success

### Slice 2 — Acceptance/result contract
Add a minimal result contract returned to Control Panel:
- `accepted`
- `accepted_no_runner`
- `accepted_pending_binding`
- `rejected_invalid_packet`
- `started`
- `blocked`
- `completed`

### Slice 3 — Runtime pathing hardening
Resolve active/staging runtime ambiguity for assignment-processing components.
At minimum:
- document authoritative DB path per environment
- prevent producer adapter/ingest/runtime from silently targeting different DBs

### Slice 4 — Silent-limbo detection
Add a guard that surfaces when:
- a new assignment reaches task state
- but no intake trace / no execution pickup / no feedback occurs within a bounded interval

## Recommended implementation order
1. Slice 2
2. Slice 1
3. Slice 3
4. Slice 4

Reason:
- feedback clarity should come first
- then canonical producer integration
- then pathing cleanup
- then automated limbo detection
