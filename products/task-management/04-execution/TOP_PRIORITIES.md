# TOP_PRIORITIES

Product: Task Management
Last updated: 2026-03-14
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
**Current status:** Readiness mechanisms are strong, and cutover evidence is promising, but the canonical-state proof path still needs explicit closed-loop decision completion.
**Next concrete step:** complete the DB-cutover observation/decision path with explicit GO/NO-GO evidence and keep readiness claims tied to current proof rather than only to description.
**Links:** `products/task-management/04-execution/PLAN.md`, `products/task-management/05-performance/READINESS_SCORECARD.md`, `products/task-management/05-performance/METRICS.md`
