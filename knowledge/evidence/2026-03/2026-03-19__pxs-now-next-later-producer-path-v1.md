# PXS now-next-later producer path v1

Date: 2026-03-19
Owner: Lyra
Product: Task Management (`A-007`)
Outcome: `pass`

## Purpose
Connect the first real bounded producer path from `pxs` into the pilot-operational Task Management contract processor.

## Producer path
Source:
- `pxs/docs/now-next-later.md#next`

Current selection rule:
- first bullet under `## Next`

Current emitted item on this run:
- `Build first vertical slice`

## Artifacts added
- producer: `tools/pxs_emit_now_next_later_request.py`
- producer test: `tools/test_pxs_emit_now_next_later_request.py`
- governed request directory: `control/runtime/pxs-tm-requests/`

## End-to-end result
Producer wrote request artifact:
- `control/runtime/pxs-tm-requests/pxs-nnl-next-d59e26956e.json`

Processor wrote governed response artifact:
- `control/runtime/pxs-tm-responses/pxs-nnl-next-d59e26956e__response.json`

## Validation result
- `[PASS] PXS now-next-later producer tests passed`
- `[PASS] PXS Task Management contract processor tests passed`
- live producer execution completed successfully end-to-end

## Why this matters
The bridge is no longer only processor-capable; it now has one real producer path that emits a governed request artifact from a live `pxs` source and receives a governed response artifact back.

## Remaining gaps
- producer coverage still limited to one source and one selection rule
- no automatic evidence-note emission tied to each producer run
- bounded handling logic still limited mainly to `accepted`, `duplicate`, and `rejected_invalid_request` in the processor

## Recommended next action
Keep this first producer path stable, then either:
1. expand processor-side bounded handling logic, or
2. add one second producer path only after this one remains clean and low-drift.
