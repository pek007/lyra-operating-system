# Decisions

### D-001 — Improvement is treated as a product
- Decision: Continuous improvement is managed as an explicit product capability.
- Why it matters: This creates continuity, ownership, and repeatable cross-product learning.

### D-002 — Improvement is the learning-and-prevention loop, not the canonical task-state engine
- Decision: Improvement remains distinct from Task Management by owning the closed-loop learning/prevention mechanism rather than the canonical task/decision state itself.
- Why it matters: This preserves a real boundary while acknowledging close coupling between the two products.

### D-003 — Phase 1 canonical improvement substrate uses the existing TDE task model plus a mandatory intake contract
- Decision: Phase 1 canonical improvement work will use the existing canonical TDE task model rather than a separate improvement board or task class. Canonical improvement intake must carry the required fields `source_system`, `source_reference`, `product_scope`, `evidence_links`, `improvement_type`, and `expected_closure_evidence`.
- Closure rule: No canonical improvement item closes without linked closure evidence and explicit source-to-closure trace.
- Why it matters: This selects the low-risk substrate path identified in Improvement Priority 1, keeps execution in one inspectable TDE-first system of record, and avoids reopening kernel redesign.
- Evidence: `products/improvement/04-execution/P1_CANONICAL_TDE_SUBSTRATE_APPROVAL_SCOPE_2026-03-19.md`, `products/improvement/04-execution/intake/CANONICAL_IMPROVEMENT_INTAKE_CONTRACT_V1.md`, `products/improvement/04-execution/P1_CANONICAL_TDE_SUBSTRATE_EXEMPLAR_VALIDATION_2026-03-20.md`
- Review trigger: Revisit only if the intake contract proves insufficient in live use or if a later Task Management kernel change makes a dedicated improvement object materially better.

### D-004 — The completed active-product rollout package is the standard reference set for future product-side minimum improvement interface work
- Decision: Reuse the bounded rollout package (`IMP-ERR-20260315`, `OPS-2026-066` through `OPS-2026-070`, and the five 2026-03-21/22 deployment-step artifacts) as the standard reference set for future product-side minimum improvement interface deployment, review, and closure-evidence enforcement.
- Why it matters: The remaining gap after first deployment coverage is no longer definition. It is consistent reuse. Naming the package as the standard reference set prevents product-local reinvention and keeps future improvement routing anchored to the same source-to-closure rule.
- Evidence: `products/improvement/04-execution/MINIMUM_IMPROVEMENT_INTERFACE_STANDARD_REFERENCE_SET_2026-03-22.md`, `products/improvement/04-execution/MINIMUM_IMPROVEMENT_INTERFACE_CONFORMANCE_TIGHTENING_STEP_2026-03-22.md`
- Review trigger: Revisit only if a later rollout reveals a missing reference pattern or if the active-product scope changes enough that the package no longer covers the dominant signal classes.

### D-005 — Improvement owns the minimum cross-system measurement-and-follow-up standard
- Decision: Improvement owns the cross-system minimum standard for lightweight measurement and follow-up on recurring operational loops, beginning with the overnight loop. Its purpose is to answer only three questions: did the loop run, did it help, and can we verify what happened.
- Scope: define the minimum useful control measures, detect stuckness/drift/repeated low-value activity, maintain a usable follow-up discipline, and keep the audit trail inspectable without creating a heavyweight reporting bureaucracy.
- Non-scope: Improvement does not own all product metrics, all delivery reporting, or a broad dashboard program by default.
- Why it matters: Performance management is currently too implicit and scattered. Making this responsibility explicit gives the system a home for simple measurement, follow-up, and closed-loop learning without creating a separate management layer.
- Evidence: `OVERNIGHT_LOOP_MINIMUM_PERFORMANCE_STANDARD_V1.md`
- Review trigger: Revisit if the measurement layer becomes too heavy, fails to detect drift/stuckness, or later justifies a separate explicit product/capability.
