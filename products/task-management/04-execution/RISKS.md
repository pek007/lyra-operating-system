# Risks

## Purpose
Track the current risks that could prevent Task Management from becoming a reliable and reusable product.

## Current risks

### R-001 — Compact steering surfaces lag the accepted and evidenced product state
- Description: The main current control risk is no longer failure to establish a viable Phase 1 boundary. The boundary is accepted, the bounded `pxs` interface exists, and assignment acceptance is strongly evidenced, but compact steering artifacts can still imply an older blocker picture.
- Consequence: management judgment, prioritization, and readiness communication can lag reality even when the underlying product has improved.
- Mitigation: keep `PLAN.md`, `RISKS.md`, and `READINESS_SCORECARD.md` synchronized to accepted scope, interface state, and current evidence.

### R-002 — Readiness description can outrun readiness evidence
- Description: Even with stronger evidence now available, downstream confidence weakens if readiness claims get ahead of explicit proof or if compact summaries fail to point to the current evidence base.
- Consequence: consumers may either over-trust or under-trust the substrate because the current-state surface is ambiguous.
- Mitigation: keep readiness tied to explicit evidence, decision records, and compact review surfaces.

### R-003 — Downstream consumption remains softer than the internal product model suggests
- Description: The `pxs` consumption contract is now pilot-operational for bounded use, but broader compatibility clarity, operational examples, and low-friction inspection evidence are still limited.
- Consequence: consumer adoption remains bounded, bespoke, or more fragile than the internal model implies.
- Mitigation: tighten compatibility semantics, extend bounded proofs, and keep the consumer/provider contract explicit.

### R-004 — Boundary blur between product and coordination layers
- Description: While refreshing compact surfaces and hardening execution, Task Management can still unintentionally absorb responsibilities that belong to governance, delivery, or workspace-local operating structures.
- Consequence: hidden coupling, unclear ownership, and weaker product discipline.
- Mitigation: keep provider/consumer boundaries explicit while the downstream consumption path hardens.

### R-005 — Producer/adapter runtime path remains less closed than the acceptance substrate
- Description: The assignment-acceptance substrate is behaviorally verified, and the self-UI proving slice is now implemented and live, but producer/adapter wiring, canonical runtime-task formation for the experiment slice, and the DB-cutover decision path are not yet closed as one operational chain.
- Consequence: runtime confidence can stall between a proven substrate, a live inspectable UI slice, and a still-incompletely integrated execution path.
- Mitigation: form the experiment tasks into canonical DB-backed runtime state, wire the producer/adapter path more tightly to canonical intake, and make DB-cutover readiness an explicit evidence-backed GO/NO-GO decision.

### R-006 — Shadow operating state
- Description: Important active work may still leak into chat or side lists instead of the canonical operating substrate.
- Consequence: lost visibility, weak traceability, and degraded control.
- Mitigation: continue reinforcing TDE as the system of record for active product work.

## Current evidence anchors
- accepted Phase 1 boundary posture: `governance/VEGA_ACCEPTANCE_TEST_RUN_SHEET_V1.md` (**PASS (Phase 1)**)
- bounded-operational downstream interface: `products/task-management/06-architecture/PXS_CONSUMPTION_INTERFACE.md`
- assignment-acceptance substrate proof: `products/task-management/04-execution/TDE_ASSIGNMENT_ACCEPTANCE_TEST_EVIDENCE_2026-03-16.md` (**21/21 PASS**)
- canonical runtime projection / active TDE state: `os/runtime/TASKS_from_db.md`

## Risk posture
Current risk posture is manageable. The strongest immediate blocker is compact current-state drift and runtime-path closure, not re-establishing the Phase 1 boundary from scratch.
