# Improvement P1 Canonical TDE Substrate — Entry Surface Alignment Step

Date: 2026-03-20
Prepared by: Overnight execution loop
Linked overnight priority: `products/improvement/04-execution/TOP_PRIORITIES.md` Priority 1
Linked prior rollout step: `products/improvement/04-execution/P1_CANONICAL_TDE_SUBSTRATE_ENFORCEMENT_ROLLOUT_2026-03-20.md`

## Purpose
Record the next concrete overnight execution step after the first enforcement rollout: review remaining improvement intake/runtime entry surfaces and align them so future improvement work does not drift back into ambiguous entry paths.

## Selected priority -> current work -> execution evidence chain
- Control Tower overnight synthesis selected Improvement Priority 1 as the highest-value overnight follow-through item (`control/CT-OVERNIGHT-SYNTHESIS-2026-03-20.md`, `memory/2026-03-20.md`).
- Product priority surface named the next concrete step as checking remaining intake/runtime entry surfaces for direct alignment needs or explicit non-canonical marking (`products/improvement/04-execution/TOP_PRIORITIES.md`).
- The substrate decision and first rollout were already completed in D-003 plus the enforcement rollout artifact (`products/improvement/07-decisions/DECISIONS.md`, `products/improvement/04-execution/P1_CANONICAL_TDE_SUBSTRATE_ENFORCEMENT_ROLLOUT_2026-03-20.md`).
- This step aligned the remaining boundary/entry surfaces below so the contract is visible both from the Improvement interface side and the TDE entrypoint side.

## Surfaces reviewed and updated
1. `products/improvement/06-architecture/INTERFACES.md`
   - Added the Phase 1 canonical rule that product-side Improvement intake must route through a canonical TDE task plus the linked six-field intake artifact.
   - Explicitly marked lighter notes, nightly reports, and discussion surfaces as valid signal sources but non-canonical until the TDE-linked intake contract is met.

2. `os/tde/INDEX.md`
   - Added the canonical Improvement intake contract as a named contract in the TDE canonical entrypoint index.
   - This makes the Improvement contract discoverable from the runtime/TDE authority surface rather than only from product-local docs.

3. `products/improvement/04-execution/PLAN.md`
   - Refreshed rollout status so the current alignment state is visible from the live execution surface.

## Result
The remaining obvious entry-surface gap is now reduced:
- the Improvement product interface explicitly says what qualifies as canonical work,
- the TDE entrypoint index links the authoritative Improvement intake contract, and
- non-canonical signal surfaces are explicitly bounded as signal-only until they become TDE-linked canonical work.

## Remaining gap after this step
Broader cross-product deployment of the minimum improvement interface still belongs to Improvement Priority 3. This step only tightened the Phase 1 canonical entry surfaces for Priority 1.

## Completion evidence for this step
- `products/improvement/06-architecture/INTERFACES.md`
- `os/tde/INDEX.md`
- `products/improvement/04-execution/PLAN.md`
