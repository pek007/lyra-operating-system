# Improvement P1 Canonical TDE Substrate — Exemplar Backfill Spec

Date: 2026-03-19
Prepared by: Overnight execution loop
Linked TDE task: `TDE-FORM-FORM-PRODUCTS-IMPROVEMENT-04-EXECUTION-TOP-PR-002`
Objective: `OBJ-FORM-FORM-PRODUCTS-IMPROVEMENT-04-EXECUTION-TOP-PR`

## Why this exists
The 2026-03-19 verification frame established that the current validation batch (`OPS-2026-066` through `OPS-2026-069`) already supports the low-risk canonical substrate direction, but cannot yet serve as the clean exemplar batch because two explicit contract fields are missing from all four packets.

This note turns that verification result into a bounded execution-ready backfill spec so the first batch can become the reference exemplar immediately after substrate approval.

## Authoritative chain
- Overnight selection: `memory/2026-03-19.md` (01:35 CET Control Tower synthesis)
- Product priority: `products/improvement/04-execution/TOP_PRIORITIES.md` (Priority 1)
- Approval scope: `products/improvement/04-execution/P1_CANONICAL_TDE_SUBSTRATE_APPROVAL_SCOPE_2026-03-19.md`
- Verification result: `products/improvement/04-execution/P1_CANONICAL_TDE_SUBSTRATE_VERIFICATION_FRAME_2026-03-19.md`
- Validation batch intake packets:
  - `products/improvement/04-execution/intake/intake-ops-2026-066-final.json`
  - `products/improvement/04-execution/intake/intake-ops-2026-067-final.json`
  - `products/improvement/04-execution/intake/intake-ops-2026-068-final.json`
  - `products/improvement/04-execution/intake/intake-ops-2026-069-final.json`

## Canonical field choice for source linkage
Recommendation: **use existing `evidence_links` as the canonical implementation field for source linkage** rather than introducing a duplicate `linked_source_artifact` field in Phase 1.

Rationale:
1. all four validation packets already carry `evidence_links`
2. `evidence_links` is more general than a singular source-artifact field and already supports explicit traceability
3. choosing the existing field keeps the approval rollout inside bounded contract enforcement rather than schema churn

## Required backfill fields for the exemplar batch
Add these explicit fields to each exemplar packet (or to the canonical item record if the approval session chooses record-level enforcement first):
- `improvement_type`
- `expected_closure_evidence`

## Batch-level rule
A packet counts as a canonical exemplar only if it has:
- `source_system`
- `source_reference`
- `product_scope`
- `evidence_links`
- `improvement_type`
- `expected_closure_evidence`

## Per-packet backfill specification

### OPS-2026-066
- Current task title: `Validate JOB-CI-001 cron delivery model against OpenClaw 2026.3.11 breaking change`
- Proposed `improvement_type`: `runtime-compatibility-hardening`
- Proposed `expected_closure_evidence`:
  - updated cron/job configuration or runbook showing compliant delivery model
  - smoke-test evidence proving JOB-CI-001 still delivers correctly after the OpenClaw 2026.3.11 change
  - checklist/update artifact showing cron delivery validation is now part of the post-update smoke path

### OPS-2026-067
- Current task title: `Add stale-finding SLA to JOB-SEC-001 to prevent findings ageing without disposition`
- Proposed `improvement_type`: `control-gap-remediation`
- Proposed `expected_closure_evidence`:
  - JOB-SEC-001 definition updated with explicit stale-finding SLA and enforcement rule
  - evidence or decision records showing retroactive disposition of `SEC-AUTO-20260307-01` and `SEC-AUTO-20260309-02`
  - validation artifact confirming the stale-finding rule is now part of the recurring security review loop

### OPS-2026-068
- Current task title: `Retire completed proof-case job bundles and standardize intra-Lyra handoff protocol`
- Proposed `improvement_type`: `operating-model-hygiene`
- Proposed `expected_closure_evidence`:
  - archival/index artifact proving the four completed proof-case bundles were retired or marked archived canonically
  - published governance artifact for the intra-Lyra handoff protocol
  - index or registry update showing where completed bundles are now tracked

### OPS-2026-069
- Current task title: `Force explicit disposition of SEC-AUTO-20260307-01 and SEC-AUTO-20260309-02`
- Proposed `improvement_type`: `risk-disposition-hardening`
- Proposed `expected_closure_evidence`:
  - formal disposition record for `SEC-AUTO-20260307-01` (risk acceptance or fix plan, with expiry/reopen logic if accepted)
  - formal disposition or approved fallback proof path for `SEC-AUTO-20260309-02`
  - traceable linkage from both stale findings to their disposition artifacts

## Interpretation
This is intentionally narrow.

It does not reopen substrate design. It makes the first live batch execution-ready under the approval-scope contract by specifying the minimum missing fields and their expected values.

## Immediate next use
After substrate approval:
1. keep `evidence_links` as the canonical source-linkage field
2. backfill `improvement_type` and `expected_closure_evidence` for `OPS-2026-066` through `OPS-2026-069`
3. validate the batch against the approved contract
4. use the completed batch as the first canonical exemplar set for Improvement P1 enforcement
