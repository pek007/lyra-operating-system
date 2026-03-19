# PXS consumption duplicate coverage v1

Date: 2026-03-19
Owner: Lyra
Product: Task Management (`A-007`)
Outcome: `pass`

## Purpose
Close the last major response-state example gap in the pilot-operational PXS -> Task Management contract by adding and validating explicit `duplicate` handling coverage.

## Artifact added
- `products/task-management/07-decisions/examples/PXS_TM_RESPONSE_ENVELOPE_DUPLICATE_V1.json`

## Validation result
PASS against:
- `schemas/pxs_tm_response_envelope/v1.0.0.schema.json`

## Interpretation
The response-state coverage set is now materially complete for bounded pilot use:
- `accepted`
- `accepted_no_runner`
- `accepted_pending_binding`
- `rejected_invalid_request`
- `duplicate`
- `recorded_no_action`

## Related maturity update
`products/task-management/06-architecture/PXS_CONSUMPTION_INTERFACE.md` should now reflect that the contract is no longer merely descriptive; it is pilot-operational for bounded use.

## Recommended next action
Build one minimal processor that validates request envelope + nested payload and emits the matching response envelope deterministically.
