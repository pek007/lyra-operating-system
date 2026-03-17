# TOP_PRIORITIES

Product: Interfaces
Last updated: 2026-03-16
Owner: Product Owner / Control Tower

## Priority 1
**Title:** Resolve Interfaces identity, scope, and ownership boundaries
**Why this matters now:** Interfaces cannot function as a stable product if it collides with provider-owned interface artifacts or remains ambiguous about what it actually owns. This is the strategic guardrail for all downstream work.
**Current status:** Core structural issue and the main prerequisite for coherent productization. Charter narrowed and documented; requires ongoing enforcement as cross-cutting boundary issues arise.
**Next concrete step:** Keep the ownership stance explicit anywhere Interfaces is referenced, especially when boundary issues arise in downstream workspaces or other products.
**Links:** `products/interfaces/04-execution/PLAN.md`, `products/interfaces/06-architecture/INTERFACES.md`, `products/interfaces/07-decisions/DECISIONS.md`

## Priority 2
**Title:** Make the Interfaces assembly real, self-consistent, and consumable — including as-code contract pack
**Why this matters now:** Verification and pinned-lane migration are not meaningful if the assembly package itself is path-broken or under-specified. The 2026-03-15 plan update added explicit as-code rollout scope: shared schemas/schema fragments for cross-repo exchange, shared enums/taxonomy to prevent drift, and PXS execution object mapping to Lyra OS artifact types.
**Current status:** Assembly packaging has known broken documentation links (assembly.yaml points to wrong paths). As-code contract pack definition is newly added to the plan but not yet started. Both sub-problems must be resolved before Priority 3 can close.
**Next concrete step:** (a) Correct assembly.yaml metadata/documentation references; (b) begin scoping the shared As-Code Contract Pack between Lyra OS and PXS — identify the minimal shared schema surface as a starting point.
**Links:** `products/interfaces/04-execution/PLAN.md`, `assemblies/prompting-and-3pp/v0.1/assembly.yaml`, `assemblies/prompting-and-3pp/v0.1/ACTIVATION.md`, `assemblies/prompting-and-3pp/v0.1/VERIFY.md`

## Priority 3
**Title:** Run one downstream consumption pilot with evidence and one preventive drift guard
**Why this matters now:** Interfaces only becomes valuable when one real workflow proves the contracts improve execution quality and one preventive control reduces silent drift.
**Current status:** Verify/activation expectations defined, but evidence path not yet closed. VERIFY contains unchecked criteria; no linked workflow evidence surfaced in the product stack. As-code rollout adds new surface that will also need verification discipline.
**Next concrete step:** Require one real workflow evidence link in VERIFY and enforce the changelog-plus-verification drift guard for meaningful interface-contract changes.
**Links:** `products/interfaces/04-execution/PLAN.md`, `products/interfaces/05-performance/METRICS.md`, `assemblies/prompting-and-3pp/v0.1/VERIFY.md`
