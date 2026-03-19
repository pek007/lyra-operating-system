# PXS consumption response coverage v1

Date: 2026-03-19
Owner: Lyra
Product: Task Management (`A-007`)
Outcome: `pass`

## Purpose
Harden the pilot-operational PXS -> Task Management contract slice by adding and validating representative response-envelope variants for non-happy-path and partial-acceptance states.

## Response variants added
- `products/task-management/07-decisions/examples/PXS_TM_RESPONSE_ENVELOPE_ACCEPTED_NO_RUNNER_V1.json`
- `products/task-management/07-decisions/examples/PXS_TM_RESPONSE_ENVELOPE_ACCEPTED_PENDING_BINDING_V1.json`
- `products/task-management/07-decisions/examples/PXS_TM_RESPONSE_ENVELOPE_REJECTED_INVALID_REQUEST_V1.json`

## Validation result
Each example validates against:
- `schemas/pxs_tm_response_envelope/v1.0.0.schema.json`

Coverage now explicitly includes:
- `accepted`
- `accepted_no_runner`
- `accepted_pending_binding`
- `rejected_invalid_request`
- `recorded_no_action`

## Why this matters
The contract slice is materially less fragile when the main operational response states are represented explicitly rather than only the happy path.

This improves:
- status coverage
- consumer expectation clarity
- readiness for a real bounded flow

## Remaining gaps
Still not yet covered with explicit example artifacts:
- `duplicate`
- one fully integrated runtime path that validates request envelope + nested payload + emitted response in one processor

## Recommended next action
Use the hardened contract set on one real bounded handling flow, then add `duplicate` coverage if the live flow exposes idempotency ambiguity.
