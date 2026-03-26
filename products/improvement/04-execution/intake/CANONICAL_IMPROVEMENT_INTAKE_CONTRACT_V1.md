# Canonical Improvement Intake Contract v1

Status: Draft
Date: 2026-03-19
Prepared by: Overnight execution loop
Linked TDE task: `TDE-FORM-FORM-PRODUCTS-IMPROVEMENT-04-EXECUTION-TOP-PR-002`
Objective: `OBJ-FORM-FORM-PRODUCTS-IMPROVEMENT-04-EXECUTION-TOP-PR`

## Purpose
Define the minimum Phase 1 intake contract for canonical improvement work so Improvement Priority 1 can move from approval framing into enforceable, TDE-first operating behavior without redesigning the TDE kernel.

This contract is the concrete intake-side surface implied by the 2026-03-19 overnight Control Tower selection and the subsequent approval/verification artifacts.

## Authoritative chain
- Overnight selection: `memory/2026-03-19.md` (01:35 CET Control Tower synthesis)
- Product priority: `products/improvement/04-execution/TOP_PRIORITIES.md` (Priority 1)
- Approval scope: `products/improvement/04-execution/P1_CANONICAL_TDE_SUBSTRATE_APPROVAL_SCOPE_2026-03-19.md`
- Verification result: `products/improvement/04-execution/P1_CANONICAL_TDE_SUBSTRATE_VERIFICATION_FRAME_2026-03-19.md`
- Exemplar backfill spec: `products/improvement/04-execution/P1_CANONICAL_TDE_SUBSTRATE_EXEMPLAR_BACKFILL_SPEC_2026-03-19.md`
- First live validation batch:
  - `products/improvement/04-execution/intake/intake-ops-2026-066-final.json`
  - `products/improvement/04-execution/intake/intake-ops-2026-067-final.json`
  - `products/improvement/04-execution/intake/intake-ops-2026-068-final.json`
  - `products/improvement/04-execution/intake/intake-ops-2026-069-final.json`

## Core rule
A signal becomes canonical improvement work when it is represented by a TDE task linked to a canonical intake artifact that satisfies this contract.

Phase 1 uses the existing canonical TDE task model.
This contract adds required improvement metadata, source linkage, and closure-evidence expectations.

## Required intake fields
Every canonical improvement intake packet must include:
- `source_system`
- `source_reference`
- `product_scope`
- `evidence_links`
- `improvement_type`
- `expected_closure_evidence`

## Field definitions
### `source_system`
The originating system or operating surface that produced the signal.

Examples:
- `jobs-review`
- `nightly-audit`
- `product-review`
- `incident-review`

### `source_reference`
The specific report, review, decision, or source cycle that produced the signal.

Examples:
- `weekly-jobs-review-2026-03-16`
- `security-nightly-2026-03-09`

### `product_scope`
The primary product or operating domain responsible for the work.

Examples:
- `improvement`
- `security`
- `governance`

### `evidence_links`
The canonical Phase 1 source-linkage field.

This field carries explicit traceability to the artifacts that justify the work and later help prove closure.
Phase 1 chooses `evidence_links` instead of introducing a duplicate `linked_source_artifact` field.

Minimum expectation:
- at least one link to the originating evidence, review, or canonical artifact
- enough specificity that a later reviewer can reconstruct why the item exists

### `improvement_type`
A bounded categorization of the improvement intent.

Purpose:
- make improvement work comparable across products
- support later reporting and review
- clarify expected treatment without adding a new TDE object type

Current approved working examples from the exemplar batch:
- `runtime-compatibility-hardening`
- `control-gap-remediation`
- `operating-model-hygiene`
- `risk-disposition-hardening`

### `expected_closure_evidence`
The minimum proof bundle expected before the canonical item can close.

This should be specific enough to support real validation, not generic enough to permit paper closure.
Use a list when multiple evidence elements are required.

## Closure rule
No canonical improvement item closes unless:
1. closure evidence exists,
2. the evidence is linked, and
3. the source-to-closure trace is explicit.

In practice this means:
- the item retains source linkage through `evidence_links`, and
- the completion state references the artifact(s) that prove the intended improvement outcome was actually achieved.

## Exemplar-batch application
The first validation batch (`OPS-2026-066` through `OPS-2026-069`) is the reference set for Phase 1 contract rollout.

Compatibility result from verification work:
- already present in all four packets: `source_system`, `source_reference`, `product_scope`, `evidence_links`
- still required as bounded backfill: `improvement_type`, `expected_closure_evidence`

## Phase 1 non-goals
This contract does not require:
- TDE DB schema redesign
- a separate improvement board
- a dedicated improvement task class
- broader task-management kernel changes

## Immediate enforcement implication
When the approval path is finalized, the following surfaces should align to this contract in the same work cycle:
- `products/improvement/04-execution/PLAN.md`
- `products/improvement/03-operating-model/OPERATING_MODEL.md`
- `products/improvement/07-decisions/DECISIONS.md`
- `governance/LYRA_CONTINUOUS_IMPROVEMENT_OPERATING_INSTRUCTION_V1.md`
- this intake surface

## Status note
This artifact is intentionally narrow.
It is not the final approval decision record; it is the explicit intake-side contract surface needed to keep the selected overnight Improvement P1 path execution-ready and to support exemplar-batch backfill/validation.
