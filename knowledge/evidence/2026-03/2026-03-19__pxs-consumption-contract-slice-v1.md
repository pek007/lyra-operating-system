# PXS consumption contract — minimal executable slice v1

Date: 2026-03-19
Owner: Lyra
Related product: Task Management (`A-007`)
Target artifact: `products/task-management/06-architecture/PXS_CONSUMPTION_INTERFACE.md`

## Purpose
Capture the first minimal executable slice for `pxs` consumption of Task Management so the interface stops depending only on descriptive operating guidance.

## Slice chosen
The first executable slice is a **provider-owned request/response contract** for `pxs` -> Task Management interaction, using artifact-mediated transport compatible with current workspace and boundary conditions.

## Why this slice first
It is the smallest step that adds executable semantics without prematurely committing to a service boundary.

It clarifies:
- transport
- request envelope
- response envelope
- validation/error semantics
- worked examples

while staying aligned to existing product-owned intake and assignment-acceptance contracts.

## Contract posture
- Transport: artifact-mediated packet exchange
- Request model: consumer emits a typed intake request referencing the canonical Task Management intake/assignment contracts
- Response model: provider returns explicit acceptance/result envelope rather than relying on inferred success
- Versioning: request and response envelopes each carry explicit version identifiers
- Validation: fail closed with explicit error/result output

## Next likely evolution
If this slice works in practice, the next increment should be:
1. JSON schema files for the `pxs` request/response envelopes
2. 2–3 pilot examples exercised end-to-end
3. transport hardening and compatibility notes
