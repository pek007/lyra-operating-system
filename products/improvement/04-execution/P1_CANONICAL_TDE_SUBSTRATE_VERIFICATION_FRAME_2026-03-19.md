# Improvement P1 Canonical TDE Substrate — Verification Frame

Date: 2026-03-19
Prepared by: Overnight execution loop
Linked TDE task: `TDE-FORM-FORM-PRODUCTS-IMPROVEMENT-04-EXECUTION-TOP-PR-002`
Objective: `OBJ-FORM-FORM-PRODUCTS-IMPROVEMENT-04-EXECUTION-TOP-PR`

## Why this exists
Control Tower selected Improvement P1 as the highest-leverage overnight priority on 2026-03-19 because the portfolio still lacks one approved canonical TDE-first substrate for improvement work.

The prior overnight step bounded the approval scope. This note performs the next concrete step for the live verification path: test whether the first validation batch (`OPS-2026-066` through `OPS-2026-069`) is already compatible with the proposed minimum substrate contract.

## Authoritative chain
- Overnight selection: `memory/2026-03-19.md` (Control Tower overnight synthesis entry, 01:35 CET)
- Product priority: `products/improvement/04-execution/TOP_PRIORITIES.md` (Priority 1)
- Approval scope: `products/improvement/04-execution/P1_CANONICAL_TDE_SUBSTRATE_APPROVAL_SCOPE_2026-03-19.md`
- Canonical runtime projection: `os/runtime/TASKS_from_db.md`
- Validation batch intake packets:
  - `products/improvement/04-execution/intake/intake-ops-2026-066-final.json`
  - `products/improvement/04-execution/intake/intake-ops-2026-067-final.json`
  - `products/improvement/04-execution/intake/intake-ops-2026-068-final.json`
  - `products/improvement/04-execution/intake/intake-ops-2026-069-final.json`

## Verification question
Is the default substrate path from the approval scope already viable for the first live validation batch?

Default path under test:
**Keep the existing canonical TDE task model and enforce mandatory improvement metadata/linkage/closure-evidence rules rather than creating a separate improvement task type or board.**

## Proposed minimum contract being tested
From the approval scope:
- `source_system`
- `source_reference`
- `product_scope`
- `improvement_type`
- `linked_source_artifact`
- `expected_closure_evidence`

Minimum closure rule under test:
- no canonical improvement item closes without an evidence link, and
- no canonical improvement item closes without explicit source-to-closure trace

## Batch verification result
### Summary verdict
**Partially ready; approval can proceed, but the first validation batch needs a small contract backfill before it can serve as the clean canonical exemplar.**

### What is already true in all four live packets
All four final intake packets already contain enough structure to support the proposed substrate direction without changing the TDE kernel or inventing a new object class:
- `source_system` present in all 4
- `source_reference` present in all 4
- `product_scope` present in all 4
- linked source evidence already present in practice via `evidence_links` in all 4
- each packet is already routed through canonical TDE intake and represented in `os/runtime/TASKS_from_db.md` as live work (`OPS-2026-066` through `OPS-2026-069`)

### What is still missing from the clean contract
The live packets do **not** yet carry two of the proposed explicit fields:
- `improvement_type` — missing in all 4
- `expected_closure_evidence` — missing in all 4

Additionally, the proposed field name `linked_source_artifact` is not present literally; current packets use `evidence_links`, which is directionally sufficient but should either be:
1. accepted as the canonical implementation field, or
2. mapped/backfilled to the explicit contract field during approval rollout

## Per-packet spot-check
### OPS-2026-066
- packet: `intake-ops-2026-066-final.json`
- current compatibility: source + product + source-linkage present
- gap: no explicit `improvement_type`; no explicit `expected_closure_evidence`

### OPS-2026-067
- packet: `intake-ops-2026-067-final.json`
- current compatibility: source + product + source-linkage present
- gap: no explicit `improvement_type`; no explicit `expected_closure_evidence`

### OPS-2026-068
- packet: `intake-ops-2026-068-final.json`
- current compatibility: source + product + source-linkage present
- gap: no explicit `improvement_type`; no explicit `expected_closure_evidence`

### OPS-2026-069
- packet: `intake-ops-2026-069-final.json`
- current compatibility: source + product + source-linkage present
- gap: no explicit `improvement_type`; no explicit `expected_closure_evidence`

## Interpretation
This result supports the low-risk Option B path from the decision frame.

Why:
1. The live validation set already proves the existing TDE task model can carry improvement work.
2. The missing pieces are contract-enforcement details, not kernel-schema blockers.
3. The required cleanup is bounded and can be rolled into the same work cycle as substrate approval and enforcement-surface updates.

## Recommended verification outcome
### Recommend: PASS with bounded follow-through
Approve the substrate if the approval session also commits to the following immediate follow-through:
1. finalize the canonical field choice for source linkage (`evidence_links` vs `linked_source_artifact`)
2. add/require `improvement_type` on canonical improvement intake packets
3. add/require `expected_closure_evidence` on canonical improvement intake packets
4. update the named enforcement surfaces so future intake follows the rule by default
5. backfill the four validation packets or their corresponding canonical item records before treating them as the reference exemplar batch

## Explicit next execution step
After approval, update the named enforcement surfaces from the approval scope and then backfill/validate `OPS-2026-066` through `OPS-2026-069` against the finalized field contract so the first batch becomes a fully compliant exemplar.

## What this does not require
- no TDE DB schema redesign
- no separate improvement board
- no expansion into A-005 deployment work
- no new overnight activation outside the selected Improvement P1 path
