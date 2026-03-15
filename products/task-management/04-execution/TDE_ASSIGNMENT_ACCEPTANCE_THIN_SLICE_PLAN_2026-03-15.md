# TDE Assignment Acceptance Thin-Slice Plan — 2026-03-15

Owner: Lyra  
Linked task: `TASK-20260315-CP-TDE-ASSIGNMENT-ACCEPTANCE`  
Related error: `ERR-2026-03-14-CP-TDE-SILENT-LIMBO`

## Purpose
Define the first thin executable slice to close the Control Panel → TDE assignment acceptance / silent-limbo gap without trying to solve the entire ideal TDE interface model in one step.

## Problem recap
The current POC failure was not primarily a task-creation bug.
It was a trust/feedback bug.

What happened:
- Control Panel appears to have written directly into canonical TDE task state
- a task row existed
- no explicit intake trace existed
- no explicit acceptance result was returned
- no visible runner pickup occurred
- from the producer perspective the assignment entered silent limbo

## Thin-slice strategy
Follow the implementation order already implied by the remediation note and acceptance contract:
1. **acceptance/result contract first**
2. assignment adapter path second
3. runtime pathing cleanup third
4. limbo detection fourth

This plan covers only slice 1 in executable detail and frames the minimum immediate bridge into slice 2.

## Thin-slice objective
Make it impossible for Control Panel (or any equivalent producer) to mistake raw task insertion for operational acceptance.

## Scope of this slice
### In scope
- canonical assignment packet/result handling for one producer path
- explicit acceptance states returned and persisted
- canonical assignment packet persistence in `assignment_packets`
- linkage from assignment result to created/updated task id where applicable
- duplicate/idempotency handling at the assignment-result layer
- clear failure output for invalid assignment packets

### Out of scope for this slice
- full generalized multi-producer adapter ecosystem
- complete runtime path unification across active/staging
- automated limbo detection timers/alerts
- full execution lifecycle state machine (`started` / `blocked` / `completed`) beyond basic placeholders
- broad Control Panel UX work

## Desired behavior after this slice
When a producer submits an assignment packet, TDE must return exactly one explicit result:
- `accepted`
- `accepted_no_runner`
- `accepted_pending_binding`
- `rejected_invalid_assignment`
- `duplicate`

And TDE must persist:
- the raw assignment packet
- the acceptance state
- the result payload / reason
- the affected task id, if one was created or updated

## Why this slice first
Because this is the minimum meaningful trust repair.

Even if the underlying execution path remains thin, the producer must no longer be left guessing whether:
- the packet was valid
- TDE took responsibility
- a runner exists
- binding/policy context is missing
- the request was just a duplicate

## Proposed concrete deliverables
### 1. Assignment packet schema wiring
Use or confirm:
- `schemas/tde_assignment_packet/v1.0.0.schema.json`

Expected outcome:
- assignment packets can be validated deterministically before any state write is treated as success

### 2. Acceptance runtime entrypoint
Use or implement the first thin runtime handler around:
- `tools/tde_assignment_accept.py`

Expected outcome:
- one callable path that:
  1. validates packet
  2. checks duplicate/idempotency
  3. creates/updates canonical task state if appropriate
  4. determines acceptance state
  5. persists result to `assignment_packets`
  6. returns the explicit result payload

### 3. Canonical result payload shape
Minimum result payload should include:
- `assignment_id`
- `acceptance_state`
- `task_id` (nullable)
- `reason_code` or equivalent
- `message`
- `created_at` / `updated_at`

Illustrative shape:
```json
{
  "assignment_id": "string",
  "acceptance_state": "accepted|accepted_no_runner|accepted_pending_binding|rejected_invalid_assignment|duplicate",
  "task_id": "string|null",
  "reason_code": "string|null",
  "message": "string",
  "created_at": "ISO-8601",
  "updated_at": "ISO-8601"
}
```

### 4. Persistence rule for this slice
For every accepted or rejected assignment packet, write one row to:
- `assignment_packets`

And where possible, link the resulting task id in the packet/result payload.

### 5. Duplicate/idempotency rule
If the same stable assignment id with the same effective content is submitted again:
- return `duplicate`
- do not silently create a second ambiguous task path

## State determination logic for v1
### `rejected_invalid_assignment`
Use when:
- schema validation fails
- required semantics are missing
- packet is malformed

### `duplicate`
Use when:
- stable assignment id already exists with equivalent packet/content

### `accepted_pending_binding`
Use when:
- packet is valid
- canonical task state can be created/updated
- but required binding/policy/objective context is incomplete

### `accepted_no_runner`
Use when:
- packet is valid
- canonical task state can be created/updated
- binding context is sufficient
- but no known runner/execution path is available

### `accepted`
Use when:
- packet is valid
- canonical task state can be created/updated
- sufficient context exists for normal pickup by the runtime path

## Thin-slice success criteria
This slice is successful when all are true:
1. no assignment path relies on raw task-state insertion alone as the success signal
2. a producer receives one explicit acceptance result every time
3. assignment results are persisted canonically in `assignment_packets`
4. invalid packets fail explicitly
5. duplicates fail explicitly as duplicates
6. result payload makes silent limbo impossible at the acceptance boundary

## Test cases for the slice
### Case A — valid assignment, normal path
Expected:
- `accepted`
- task created/updated
- `assignment_packets` row persisted

### Case B — valid assignment, missing binding/objective context
Expected:
- `accepted_pending_binding`
- task may exist, but result makes incomplete context explicit

### Case C — valid assignment, no runner available
Expected:
- `accepted_no_runner`
- task may exist, but producer is told that execution pickup is not currently available

### Case D — invalid packet
Expected:
- `rejected_invalid_assignment`
- no ambiguous acceptance

### Case E — duplicate packet
Expected:
- `duplicate`
- no second ambiguous task path

## Recommended first implementation sequence
1. inspect current `tools/tde_assignment_accept.py`
2. confirm current assignment packet schema and DB writes
3. define/normalize returned payload shape
4. wire explicit acceptance-state determination
5. add/verify persistence into `assignment_packets`
6. add focused tests for the five cases above
7. only after that, wire the producer-side adapter more tightly

## Immediate next coding question
The first coding question is not architectural perfection.
It is:
**what minimal change makes `tools/tde_assignment_accept.py` return and persist explicit acceptance states today?**

That should be the next implementation move.

## Follow-on after this slice
Once slice 1 is working:
- build the dedicated Control Panel assignment adapter onto the canonical intake path
- unify active/staging runtime path expectations
- add explicit limbo detection if assignment exists without pickup/feedback after a bounded interval

## Bottom line
The first real TDE repair is not “make the task appear.”
It is “make assignment acceptance explicit, persisted, and impossible to misread.”
