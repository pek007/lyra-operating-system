# TOP_PRIORITIES

Product: Task Management
Last updated: 2026-03-17
Owner: Product Owner / Control Tower

## Priority 1
**Title:** Close the Vega/PXS boundary readiness gap and rerun it to PASS
**Why this matters now:** The strongest current blocker to downstream Task Management consumption is not TDE internals but the failing Vega/PXS boundary readiness conditions that make safe, repeatable consumption impossible.
**Current status:** Acceptance evidence currently shows blocking failures: `pxs` repo placement missing, pinned dependency not implemented, and cross-domain reads still allowed.
**Next concrete step:** treat the Vega/PXS acceptance failures as the top active gating dependency, close the failing conditions, and rerun the boundary acceptance sheet to PASS with evidence.
**Links:** `products/task-management/04-execution/PLAN.md`, `products/task-management/04-execution/RISKS.md`, `governance/VEGA_ACCEPTANCE_TEST_RUN_SHEET_V1.md`, `products/task-management/06-architecture/PXS_CONSUMPTION_INTERFACE.md`

## Priority 2
**Title:** Deliver a minimal executable `pxs` consumption contract with schemas and worked examples
**Why this matters now:** A taxonomy of intended interaction is useful, but downstream consumption will stay soft until the interface becomes an explicit executable contract.
**Current status:** First-pass consumption interface exists, but it still lacks minimal request/response schemas, compatibility/versioning clarity, and worked examples.
**Next concrete step:** upgrade the `pxs` consumption interface from descriptive contract to minimal executable contract with request/response expectations, validation/error semantics, explicit transport choice, and 2–3 worked examples.
**Links:** `products/task-management/04-execution/PLAN.md`, `products/task-management/06-architecture/PXS_CONSUMPTION_INTERFACE.md`, `products/task-management/02-strategy/DISTRIBUTION_MODEL.md`

## Priority 3
**Title:** Stabilize and prove the canonical substrate that `pxs` will consume
**Why this matters now:** Downstream consumers should not be built atop a canonical state transition that is still only described or provisionally evidenced.
**Current status:** Assignment acceptance thin-slice implementation completed 2026-03-16: `tools/tde_assignment_accept.py` fully tested (21/21 PASS) across all five canonical acceptance cases (accepted, accepted_pending_binding, accepted_no_runner, rejected_invalid_assignment, duplicate). Silent-limbo gap is closed at the acceptance boundary. Runtime pathing hardened, post-acceptance traces added, limbo detector implemented. Remaining open items: Control Panel adapter-layer wiring (slice 2), and the DB-cutover GO/NO-GO decision path.
**Next concrete step:** Wire the Control Panel assignment adapter more tightly to the canonical intake path (thin-slice 2); then close the DB-cutover decision path with explicit GO/NO-GO evidence.
**Links:** `products/task-management/04-execution/PLAN.md`, `products/task-management/04-execution/TDE_ASSIGNMENT_ACCEPTANCE_THIN_SLICE_PLAN_2026-03-15.md`, `products/task-management/04-execution/TDE_ASSIGNMENT_ACCEPTANCE_TEST_EVIDENCE_2026-03-16.md`, `products/task-management/05-performance/READINESS_SCORECARD.md`, `products/task-management/05-performance/METRICS.md`
