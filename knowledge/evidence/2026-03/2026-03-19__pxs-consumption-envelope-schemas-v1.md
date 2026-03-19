# PXS consumption envelope schemas v1

Date: 2026-03-19
Owner: Lyra
Product: Task Management (`A-007`)

## Purpose
Record the first machine-checkable schema layer for the PXS -> Task Management consumption contract slice.

## Artifacts added
- `schemas/pxs_tm_request_envelope/v1.0.0.schema.json`
- `schemas/pxs_tm_response_envelope/v1.0.0.schema.json`
- `products/task-management/07-decisions/examples/PXS_TM_REQUEST_ENVELOPE_INTAKE_WORK_V1.json`
- `products/task-management/07-decisions/examples/PXS_TM_REQUEST_ENVELOPE_ASSIGNMENT_ACCEPTANCE_V1.json`
- `products/task-management/07-decisions/examples/PXS_TM_RESPONSE_ENVELOPE_RECORDED_NO_ACTION_V1.json`
- `schemas/_registry.json` updated with both new schema entries

## Validation result
Validated with local Draft 2020-12 JSON Schema checks.

Result:
- PASS `PXS_TM_REQUEST_ENVELOPE_INTAKE_WORK_V1.json`
- PASS `PXS_TM_REQUEST_ENVELOPE_ASSIGNMENT_ACCEPTANCE_V1.json`
- PASS `PXS_TM_RESPONSE_ENVELOPE_RECORDED_NO_ACTION_V1.json`

## Outcome
The PXS consumption contract now has:
- explicit envelope schemas
- registered machine-checkable schema refs
- representative worked examples that validate successfully

## Next action
Use these schemas in one real or simulated end-to-end pilot flow, then decide whether to:
1. add stricter payload cross-validation,
2. generate example response variants for `accepted_no_runner` / `accepted_pending_binding` / `rejected_invalid_request`, and
3. promote the contract slice from descriptive to pilot-operational.
