# PXS consumption minimal processor v1

Date: 2026-03-19
Owner: Lyra
Product: Task Management (`A-007`)
Outcome: `pass`

## Purpose
Add the smallest deterministic processor for the pilot-operational PXS -> Task Management contract.

## Artifact added
- `tools/pxs_tm_contract_processor.py`
- `tools/test_pxs_tm_contract_processor.py`

## Current processor behavior
The processor currently:
- validates the request envelope against `pxs_tm_request_envelope@1.0.0`
- validates the nested inline payload against the schema registry
- detects duplicates by request id against known response-envelope artifacts in a search root
- emits deterministic response envelopes for bounded cases:
  - `accepted`
  - `duplicate`
  - `rejected_invalid_request`

## Validation result
- `[PASS] PXS Task Management contract processor tests passed`
- direct processor invocation on the intake-work example emitted a valid `accepted` response envelope

## Why this matters
The contract is no longer only manually exercised.
There is now a minimal executable processor that can perform the core bounded validation/response loop.

## Remaining gaps
- no deterministic write-path yet from processor output into governed response-artifact locations
- no live producer emission from inside `pxs`
- no full handling logic for `accepted_no_runner`, `accepted_pending_binding`, or `recorded_no_action`

## Recommended next action
Add a deterministic output/write mode for governed response artifacts, then connect one real bounded producer path to the processor.
