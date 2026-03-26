# Improvement P1 Canonical TDE Substrate — Approval Scope

Date: 2026-03-19
Prepared by: Control Tower overnight synthesis
Linked TDE task: `TDE-FORM-FORM-PRODUCTS-IMPROVEMENT-04-EXECUTION-TOP-PR-001`
Objective: `OBJ-FORM-FORM-PRODUCTS-IMPROVEMENT-04-EXECUTION-TOP-PR`

## Purpose
Define the bounded review/approval scope for Improvement Priority 1 so the next focused session can make one concrete decision and move directly into validation, rather than reopening broad substrate design.

## In-scope decision
Approve or reject this default path:

**Use the existing canonical TDE task model plus mandatory improvement metadata/linkage/closure-evidence rules** as the Phase 1 canonical improvement substrate.

## Inputs to review
- `products/improvement/04-execution/TOP_PRIORITIES.md`
- `products/improvement/04-execution/P1_CANONICAL_TDE_SUBSTRATE_SESSION_PREP_2026-03-18.md`
- `products/improvement/04-execution/P1_CANONICAL_TDE_SUBSTRATE_VALIDATION_MATRIX_2026-03-18.md`
- `products/improvement/04-execution/P1_CANONICAL_TDE_SUBSTRATE_ENFORCEMENT_SURFACES_2026-03-18.md`
- `products/improvement/04-execution/P1_CANONICAL_TDE_SUBSTRATE_DECISION_FRAME_2026-03-18.md`
- live TDE validation set: `OPS-2026-066` through `OPS-2026-069`
- current canonical TDE runtime projection: `os/runtime/TASKS_from_db.md`

## What this review must decide
1. Whether the approved substrate model is Option B from the decision frame.
2. The minimum mandatory metadata/linkage fields for canonical improvement work.
3. The minimum closure-evidence rule.
4. The named enforcement surfaces that must be updated in the same work cycle.
5. Whether the live validation set (`OPS-2026-066` through `OPS-2026-069`) is sufficient as the first validation batch.

## Proposed minimum approval package
### Routing rule
A signal becomes canonical improvement work when it is represented by a TDE task linked to a canonical intake artifact and carrying the approved improvement metadata contract.

### Minimum metadata contract
- `source_system`
- `source_reference`
- `product_scope`
- `improvement_type`
- `linked_source_artifact`
- `expected_closure_evidence`

### Minimum closure rule
No canonical improvement item closes without:
- an evidence link, and
- explicit source-to-closure trace.

### Minimum enforcement surfaces to update immediately after approval
- `products/improvement/04-execution/PLAN.md`
- `products/improvement/03-operating-model/OPERATING_MODEL.md`
- `products/improvement/07-decisions/DECISIONS.md`
- `governance/LYRA_CONTINUOUS_IMPROVEMENT_OPERATING_INSTRUCTION_V1.md`
- `products/improvement/04-execution/intake/` contract surface
- `products/improvement/04-execution/TOP_PRIORITIES.md`
- `os/tde/INDEX.md` if a new canonical substrate artifact is added there

## Explicitly out of scope
- redesigning the TDE kernel or DB schema
- inventing a separate improvement board
- broadening into A-005 deployment work
- reopening the already accepted Phase 1 Vega/PXS boundary posture
- forcing Delivery or Interfaces local priorities into overnight execution without stronger portfolio leverage

## Expected next step after this scope
Use this scope to run the approval/verification session, record the substrate decision, update the named enforcement surfaces, and validate the rule set against `OPS-2026-066` through `OPS-2026-069`.
