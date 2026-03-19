# PXS consumption governed write-path v1

Date: 2026-03-19
Owner: Lyra
Product: Task Management (`A-007`)
Outcome: `pass`

## Purpose
Extend the minimal PXS -> Task Management contract processor so it can write deterministic governed response-envelope artifacts to disk, not only print JSON to stdout.

## Changes
- `tools/pxs_tm_contract_processor.py`
  - added governed output directory support
  - added deterministic output naming: `<request_id>__response.json`
  - added `--write-governed`
- `tools/test_pxs_tm_contract_processor.py`
  - added write-path test coverage

## Governed output path
- `control/runtime/pxs-tm-responses/`

## Validation result
- `[PASS] PXS Task Management contract processor tests passed`
- direct invocation with `--write-governed` wrote:
  - `control/runtime/pxs-tm-responses/pxs-tm-req-2026-03-19-001__response.json`

## Why this matters
The contract processor now has a deterministic governed write-path, which makes it materially easier to use in repeatable bounded flows without hand-copying processor output.

## Remaining gaps
- no live producer emission from inside `pxs` yet
- no automatic evidence-note creation tied to each processed request
- bounded handling logic still defaults mainly to `accepted`, `duplicate`, and `rejected_invalid_request`

## Recommended next action
Connect one bounded producer path from `pxs` into this processor, then expand processor-side handling to cover more response states deterministically.
