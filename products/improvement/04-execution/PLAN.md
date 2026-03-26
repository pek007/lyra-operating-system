# Current Plan

## Current objectives
1. Converge improvement execution into one canonical TDE-first system of record.
2. Ship A-005 into PXS through a pinned lane with version truth, rollback, and verification semantics.
3. Roll out the minimum improvement interface across active products, starting with mandatory incident-to-improvement conversion.
4. Keep product-local status truth aligned with verified evidence.

## Priority 1 operating rule
Phase 1 canonical improvement execution uses the existing canonical TDE task model plus the mandatory intake contract defined in `products/improvement/04-execution/intake/CANONICAL_IMPROVEMENT_INTAKE_CONTRACT_V1.md`.

That means a signal becomes canonical improvement work only when:
1. it is represented by a TDE task in canonical runtime state, and
2. it is linked to an intake artifact that includes the required fields:
   - `source_system`
   - `source_reference`
   - `product_scope`
   - `evidence_links`
   - `improvement_type`
   - `expected_closure_evidence`

## Closure rule for canonical improvement work
No canonical improvement item closes unless linked closure evidence exists and the source-to-closure trace remains explicit.

## Current rollout status
- Approved substrate decision: `products/improvement/07-decisions/DECISIONS.md` (D-003)
- First validated exemplar batch: `OPS-2026-066` through `OPS-2026-069`
- Validation evidence: `products/improvement/04-execution/P1_CANONICAL_TDE_SUBSTRATE_EXEMPLAR_VALIDATION_2026-03-20.md`

## Next rollout step
The now-complete active-product rollout package has been published as the standard reference set for future product-side conversion, review visibility, and closure-evidence enforcement so future improvement work follows the contract by default rather than by exception.

In parallel, Improvement now also owns the minimum cross-system measurement-and-follow-up standard, beginning with the overnight loop. First live application is complete and repeated-use sufficiency has now been tested through three live cycles: the 2026-03-24 Control Tower overnight synthesis selected `CT-2026-03-24-IMPROVEMENT-OVERNIGHT-LEDGER` as the top overnight item, anchored it via `control/tde-intake/improvement-overnight-ledger-activation-2026-03-24.json`, and applied the canonical ledger path at `control/runtime/overnight-ledger/2026-03-24.json`, with execution evidence recorded in `products/improvement/04-execution/OVERNIGHT_LEDGER_ACTIVATION_STEP_2026-03-24.md`, `products/improvement/04-execution/OVERNIGHT_LEDGER_RUNTIME_LINKAGE_STEP_2026-03-24.md`, and `products/improvement/04-execution/OVERNIGHT_LEDGER_LIVE_APPLICATION_STATUS_2026-03-24.md`. The 2026-03-25 Control Tower overnight synthesis then selected follow-on priority `CT-2026-03-25-IMPROVEMENT-OVERNIGHT-LEDGER-REPEATED-CYCLE`, anchored it via `control/tde-intake/improvement-overnight-ledger-repeated-cycle-2026-03-25.json`, and recorded the second live-cycle control result in `control/runtime/overnight-ledger/2026-03-25.json` with bounded execution evidence in `products/improvement/04-execution/OVERNIGHT_LEDGER_REPEATED_CYCLE_SUFFICIENCY_STEP_2026-03-25.md` and `products/improvement/04-execution/OVERNIGHT_LEDGER_REPEATED_CYCLE_STUCKNESS_CHECK_2026-03-25.md`. The 2026-03-26 Control Tower overnight synthesis then selected third-cycle follow-on priority `CT-2026-03-26-IMPROVEMENT-OVERNIGHT-LEDGER-THIRD-CYCLE`, anchored it via `control/tde-intake/improvement-overnight-ledger-third-cycle-2026-03-26.json`, and recorded the third live-cycle control result in `control/runtime/overnight-ledger/2026-03-26.json` with explicit disposition evidence in `products/improvement/04-execution/OVERNIGHT_LEDGER_THIRD_CYCLE_DISPOSITION_CHECK_2026-03-26.md`. The immediate next step is now tighter: keep the compact control path only if the next selected reuse binds to a more concrete downstream proof/closure surface; otherwise escalate this work into stronger explicit task-layer representation rather than allowing a fourth representation-only cycle.

A first enforcement-tightening pass is now also complete: the Improvement-side canonical interface no longer describes active-product coverage as future intent and instead states the five required elements as a current requirement for active products with canonical `TOP_PRIORITIES.md` surfaces.

The Improvement operating model is now aligned with that same expectation, so future product reviews and product-surface changes reuse the standard reference set and correct drift at the point of change rather than treating conformance as a separate future rollout.

Standard reference artifact:
- `products/improvement/04-execution/MINIMUM_IMPROVEMENT_INTERFACE_STANDARD_REFERENCE_SET_2026-03-22.md`

Conformance tightening evidence:
- `products/improvement/04-execution/MINIMUM_IMPROVEMENT_INTERFACE_CONFORMANCE_TIGHTENING_STEP_2026-03-22.md`

Operating-model alignment evidence:
- `products/improvement/04-execution/MINIMUM_IMPROVEMENT_INTERFACE_OPERATING_MODEL_ALIGNMENT_STEP_2026-03-22.md`

Current rollout seed:
- `products/improvement/04-execution/MINIMUM_IMPROVEMENT_INTERFACE_ROLLOUT_SEED_2026-03-21.md`

Current deployment evidence:
- `products/improvement/04-execution/MINIMUM_IMPROVEMENT_INTERFACE_SECURITY_DEPLOYMENT_STEP_2026-03-21.md`
- `products/improvement/04-execution/MINIMUM_IMPROVEMENT_INTERFACE_TASK_MANAGEMENT_DEPLOYMENT_STEP_2026-03-21.md`
- `products/improvement/04-execution/MINIMUM_IMPROVEMENT_INTERFACE_GOVERNANCE_DEPLOYMENT_STEP_2026-03-21.md`
- `products/improvement/04-execution/MINIMUM_IMPROVEMENT_INTERFACE_INTERFACES_DEPLOYMENT_STEP_2026-03-21.md`
- `products/improvement/04-execution/MINIMUM_IMPROVEMENT_INTERFACE_DELIVERY_DEPLOYMENT_STEP_2026-03-22.md`

Current alignment status:
- `products/improvement/06-architecture/INTERFACES.md` now states that Phase 1 canonical Improvement work requires a canonical TDE task plus the six-field linked intake artifact.
- `os/tde/INDEX.md` now links the canonical Improvement intake contract directly from the TDE entrypoint surface.
- Security now carries the first explicit product-side deployment of the minimum improvement interface in `products/security/06-architecture/INTERFACES.md` and `products/security/03-operating-model/OPERATING_MODEL.md`.
- Task Management now carries the second explicit product-side deployment of the minimum improvement interface in `products/task-management/06-architecture/INTERFACES.md` and `products/task-management/03-operating-model/OPERATING_MODEL.md`, using compact-surface drift and stale steering/control surfaces as the first bounded signal class.
- Governance now carries the third explicit product-side deployment of the minimum improvement interface in `products/governance/06-architecture/INTERFACES.md` and `products/governance/03-operating-model/OPERATING_MODEL.md`, using completed proof-case retirement and durable protocol formalization as the bounded signal class via `OPS-2026-068`.
- Interfaces now carries the fourth explicit product-side deployment of the minimum improvement interface in `products/interfaces/06-architecture/INTERFACES.md` and `products/interfaces/03-operating-model/OPERATING_MODEL.md`, using interface-packaging drift and recurring verification/ownership-boundary misses as the bounded signal class.
- Delivery now carries the fifth explicit product-side deployment of the minimum improvement interface in `products/delivery/06-architecture/INTERFACES.md` and `products/delivery/03-operating-model/OPERATING_MODEL.md`, using repo-integrity control misses, placeholder/weak quality-gate findings, and recurring verification/rollback-readiness gaps as the bounded signal class.
- Product-local reports, notes, and discussion surfaces remain valid signal sources, but are explicitly non-canonical until the TDE-linked intake contract is met.
