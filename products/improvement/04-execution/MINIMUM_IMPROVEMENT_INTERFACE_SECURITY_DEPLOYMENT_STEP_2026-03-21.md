# Minimum Improvement Interface — Security First Deployment Step

Date: 2026-03-21
Prepared by: Overnight execution loop
Linked overnight priority: `products/improvement/04-execution/TOP_PRIORITIES.md` Priority 3
Linked rollout seed: `products/improvement/04-execution/MINIMUM_IMPROVEMENT_INTERFACE_ROLLOUT_SEED_2026-03-21.md`
Linked TDE intake: `control/runtime/2026-03-21/improvement-minimum-interface-rollout-intake.json` (`OPS-2026-070`)

## Purpose
Record the first concrete deployment step for the broader minimum product-side improvement interface after the Phase 1 canonical TDE-first substrate was selected and aligned.

## Selected priority -> current work -> execution evidence chain
- Control Tower overnight synthesis selected the post-substrate rollout gap as the highest-value overnight follow-through item and promoted it through `OPS-2026-070`.
- The rollout seed narrowed the first deployment scope to Security, specifically stale findings / explicit disposition gaps.
- This step applies that rollout seed to a canonical product-side Security surface so the interface now exists in one live product rather than only in Improvement-side planning.

## Why Security was chosen first
Security already had the clearest live backlog pressure and the strongest reference set for a bounded deployment:
- `OPS-2026-067`
- `OPS-2026-069`
- `SEC-AUTO-20260307-01`
- `SEC-AUTO-20260309-02`

These items already make the stale-finding/disposition problem concrete, and they map cleanly to the minimum interface rule without needing a new tracker.

## Surfaces updated in this step
1. `products/security/06-architecture/INTERFACES.md`
   - Added the explicit Security -> Improvement interface.
   - Stated that material incidents, repeated misses, and stale finding/disposition gaps must route into canonical TDE-linked improvement work.
   - Added the six-field intake contract, closure-evidence rule, and first bounded deployment scope for stale findings / disposition gaps.

2. `products/security/03-operating-model/OPERATING_MODEL.md`
   - Added the minimum improvement interface expectation to Security's recurring operating model.
   - Made review visibility explicit for open Security-origin improvement items until disposition or closure.

## Result
The broader minimum improvement interface is no longer only an Improvement-side intent.
It now has a first explicit deployment case in Security, with:
- named signal class,
- canonical routing rule,
- required intake fields,
- closure-evidence expectation, and
- recurring review expectation.

## Remaining gap after this step
The interface still needs equivalent deployment into the next active product surfaces, but the first product-side rollout step is now complete and inspectable.

## Completion evidence for this step
- `products/security/06-architecture/INTERFACES.md`
- `products/security/03-operating-model/OPERATING_MODEL.md`
- `products/improvement/04-execution/MINIMUM_IMPROVEMENT_INTERFACE_ROLLOUT_SEED_2026-03-21.md`
- `control/runtime/2026-03-21/improvement-minimum-interface-rollout-intake.json`
