# TOP_PRIORITIES

Product: Interfaces
Last updated: 2026-03-14
Owner: Product Owner / Control Tower

## Priority 1
**Title:** Resolve Interfaces identity, scope, and ownership boundaries
**Why this matters now:** Interfaces cannot function as a stable product if it collides with provider-owned interface artifacts or remains ambiguous about what it actually owns.
**Current status:** Core structural issue and the main prerequisite for coherent productization.
**Next concrete step:** make explicit that Interfaces owns cross-cutting interface standards, packaging, and change-governance discipline — not every concrete provider interface — and eliminate naming/scope confusion where it still exists.
**Links:** `products/interfaces/04-execution/PLAN.md`, `products/interfaces/06-architecture/INTERFACES.md`, `products/interfaces/07-decisions/DECISIONS.md`

## Priority 2
**Title:** Make the Interfaces assembly real, self-consistent, and consumable
**Why this matters now:** Verification and pinned-lane migration are not meaningful if the assembly package itself is path-broken or under-specified.
**Current status:** Strong contract ideas exist, but assembly packaging and installability have been weaker than the product intent.
**Next concrete step:** keep the assembly paths/links/artifact set self-consistent, define the export manifest implicitly through real packaged artifacts, and strengthen install/activation/verify so the pack can be consumed honestly.
**Links:** `products/interfaces/04-execution/PLAN.md`, `assemblies/prompting-and-3pp/v0.1/assembly.yaml`, `assemblies/prompting-and-3pp/v0.1/ACTIVATION.md`, `assemblies/prompting-and-3pp/v0.1/VERIFY.md`

## Priority 3
**Title:** Run one downstream consumption pilot with evidence and one preventive drift guard
**Why this matters now:** Interfaces only becomes valuable when one real workflow proves the contracts improve execution quality and one preventive control reduces silent drift.
**Current status:** Evaluation concepts exist, but the closed-loop promotion path is still light.
**Next concrete step:** require one real workflow evidence link in VERIFY and add a drift guard that expects changelog + verification evidence for meaningful interface-contract changes.
**Links:** `products/interfaces/04-execution/PLAN.md`, `products/interfaces/05-performance/METRICS.md`, `assemblies/prompting-and-3pp/v0.1/VERIFY.md`
