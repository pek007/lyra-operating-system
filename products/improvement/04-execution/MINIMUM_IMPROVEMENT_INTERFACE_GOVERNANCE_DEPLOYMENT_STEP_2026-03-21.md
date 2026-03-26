# Minimum Improvement Interface — Governance Deployment Step

Date: 2026-03-21
Prepared by: Overnight execution loop
Linked overnight priority: `products/improvement/04-execution/TOP_PRIORITIES.md` Priority 3
Linked rollout seed: `products/improvement/04-execution/MINIMUM_IMPROVEMENT_INTERFACE_ROLLOUT_SEED_2026-03-21.md`
Linked TDE intake: `control/runtime/2026-03-21/improvement-minimum-interface-rollout-intake.json` (`OPS-2026-070`)
Linked prior deployment step: `products/improvement/04-execution/MINIMUM_IMPROVEMENT_INTERFACE_TASK_MANAGEMENT_DEPLOYMENT_STEP_2026-03-21.md`

## Purpose
Record the third concrete deployment step for the broader minimum product-side improvement interface by extending the rollout into Governance / operating-model hygiene.

## Selected priority -> current work -> execution evidence chain
- Control Tower overnight synthesis selected the post-substrate rollout gap as the highest-value overnight follow-through item and promoted it through `OPS-2026-070`.
- The rollout seed named Governance / operating-model hygiene as the next bounded deployment scope after Security and Task Management, specifically for proof-case retirement and durable protocol formalization.
- This step applies the same minimum interface rule to canonical Governance product surfaces so the rollout now spans a third live product rather than remaining concentrated in only Security and Task Management.

## Why Governance was chosen next
Governance already had a live, explicitly named seed reference that maps cleanly to the minimum interface rule:
- `OPS-2026-068`

That signal is about completed proof-case retirement and durable handoff/protocol formalization, which is exactly the kind of governance hygiene gap that should become canonical TDE-linked improvement work instead of lingering in prose-only notes.

## Surfaces updated in this step
1. `products/governance/06-architecture/INTERFACES.md`
   - Added the explicit Governance -> Improvement interface.
   - Stated that governance operating-model drift, completed proof-case retirement misses, and recurring protocol/authority ambiguity must route into canonical TDE-linked improvement work.
   - Added the six-field intake contract, closure-evidence rule, and first bounded deployment scope for Governance.

2. `products/governance/03-operating-model/OPERATING_MODEL.md`
   - Added the minimum improvement interface expectation to Governance's recurring operating model.
   - Made review visibility explicit for open Governance-origin improvement items until disposition or closure.

## Result
The broader minimum improvement interface now has a third explicit product-side deployment case.
In Governance it now covers:
- named signal class,
- canonical routing rule,
- required intake fields,
- closure-evidence expectation, and
- recurring review expectation.

## Remaining gap after this step
The interface still needs equivalent deployment into the remaining active product surfaces, but the rollout now spans Security, Task Management, and Governance with explicit product-side evidence.

## Completion evidence for this step
- `products/governance/06-architecture/INTERFACES.md`
- `products/governance/03-operating-model/OPERATING_MODEL.md`
- `products/improvement/04-execution/MINIMUM_IMPROVEMENT_INTERFACE_ROLLOUT_SEED_2026-03-21.md`
- `control/runtime/2026-03-21/improvement-minimum-interface-rollout-intake.json`
