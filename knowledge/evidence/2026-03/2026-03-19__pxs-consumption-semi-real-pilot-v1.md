# PXS consumption semi-real pilot v1

Date: 2026-03-19
Owner: Lyra
Product: Task Management (`A-007`)
Pilot type: semi-real request/response check grounded in an actual `pxs` planning artifact
Outcome: `pass` with operational next step

## Pilot target
Verify that the first executable PXS -> Task Management contract slice works not only for a fabricated example, but for a request grounded in a real current `pxs` artifact.

## Grounding artifact
- `pxs/docs/now-next-later.md#next`
- Actual `Next` entry used: `Build first vertical slice`

## Pilot artifacts
Request:
- `products/task-management/07-decisions/examples/PXS_TM_REQUEST_ENVELOPE_SEMI_REAL_VERTICAL_SLICE_V1.json`

Response:
- `products/task-management/07-decisions/examples/PXS_TM_RESPONSE_ENVELOPE_SEMI_REAL_VERTICAL_SLICE_ACCEPTED_V1.json`

Schemas:
- `schemas/pxs_tm_request_envelope/v1.0.0.schema.json`
- `schemas/pxs_tm_response_envelope/v1.0.0.schema.json`

## Validation result
PASS:
- request envelope schema
- response envelope schema
- grounded source reference to a real `pxs` artifact
- request/response linkage via request id

## Judgment
PASS for the semi-real pilot.

What this proves:
- the contract can carry a request grounded in a real `pxs` planning surface
- the request can be interpreted without hidden thread-memory dependence
- Task Management can return an explicit accepted result with concrete references
- the contract is credible enough for bounded pilot-operational use

## Limits still not proven
This still does not prove:
- live emission from inside `pxs` runtime flows
- automated runtime consumption by Task Management tooling
- integrated nested-payload validation in a single runtime processor
- harder operational states like `accepted_no_runner`, `accepted_pending_binding`, `duplicate`, or `rejected_invalid_request` under real conditions

## Operational next step
Use the same contract shape on one real bounded Task Management handling path, not just an example pair.

Best next move:
1. choose one real `pxs` planning or backlog artifact
2. emit one contract-shaped request packet
3. process it through a bounded Task Management operating cycle
4. emit the response envelope and update the target state/evidence artifact in the same cycle

## Recommended interpretation
The contract slice should now be treated as **pilot-operational for bounded use**, not merely descriptive.
