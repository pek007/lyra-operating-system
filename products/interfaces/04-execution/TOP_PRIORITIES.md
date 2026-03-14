# TOP_PRIORITIES

Product: Interfaces
Last updated: 2026-03-14
Owner: Product Owner / Control Tower

## Priority 1
**Title:** Clarify the OS → PXS capability export boundary
**Why this matters now:** Without a clear export boundary, Interfaces risks becoming vague and downstream consumption stays dependent on explanation rather than contract.
**Current status:** Core active objective.
**Next concrete step:** Make the export boundary explicit in the interface and packaging artifacts that govern what downstream workspaces actually consume.
**Links:** `products/interfaces/04-execution/PLAN.md`, `products/interfaces/06-architecture/INTERFACES.md`, `products/interfaces/01-identity/VISION.md`

## Priority 2
**Title:** Make interface contracts and packaging rules more explicit
**Why this matters now:** Contract clarity is the main way Interfaces prevents hidden coupling and fuzzy handoffs across product and workspace boundaries.
**Current status:** Direction is explicit, but more codified contract surfaces are still needed.
**Next concrete step:** Tighten the canonical contract/packaging artifacts so they can be consumed with less narrative interpretation.
**Links:** `products/interfaces/04-execution/PLAN.md`, `products/interfaces/06-architecture/INTERFACES.md`, `products/interfaces/07-decisions/DECISIONS.md`

## Priority 3
**Title:** Reduce the risk that Interfaces becomes a residual product with unclear ownership
**Why this matters now:** If Interfaces becomes the place where uncategorized boundary issues go, the product loses strategic coherence.
**Current status:** Risk recognized; ownership discipline needs to remain active.
**Next concrete step:** Continue separating true interface/contract responsibilities from problems that belong inside product-local operating models.
**Links:** `products/interfaces/04-execution/PLAN.md`, `products/interfaces/02-strategy/STRATEGY.md`, `products/interfaces/03-operating-model/OPERATING_MODEL.md`
