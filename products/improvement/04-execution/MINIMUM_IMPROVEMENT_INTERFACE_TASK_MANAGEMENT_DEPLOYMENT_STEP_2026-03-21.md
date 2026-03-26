# Minimum Improvement Interface — Task Management Deployment Step

Date: 2026-03-21
Prepared by: Overnight execution loop
Linked overnight priority: `products/improvement/04-execution/TOP_PRIORITIES.md` Priority 3
Linked rollout seed: `products/improvement/04-execution/MINIMUM_IMPROVEMENT_INTERFACE_ROLLOUT_SEED_2026-03-21.md`
Linked TDE intake: `control/runtime/2026-03-21/improvement-minimum-interface-rollout-intake.json` (`OPS-2026-070`)
Linked prior deployment step: `products/improvement/04-execution/MINIMUM_IMPROVEMENT_INTERFACE_SECURITY_DEPLOYMENT_STEP_2026-03-21.md`

## Purpose
Record the second concrete deployment step for the broader minimum product-side improvement interface after the first product-side deployment in Security.

## Selected priority -> current work -> execution evidence chain
- Control Tower overnight synthesis selected the post-substrate rollout gap as the highest-value overnight follow-through item and promoted it through `OPS-2026-070`.
- The rollout seed named Task Management as the next active product surface after Security, specifically for compact-surface drift and product-control gaps.
- The 2026-03-21 Task Management nightly report confirmed that stale compact steering surfaces remain the main current reporting issue.
- This step applies the same minimum interface rule to a canonical Task Management product surface so the rollout now covers a second live product, not just Security.

## Why Task Management was chosen next
Task Management already had an explicit live signal that maps cleanly to the minimum interface rule:
- `products/task-management/04-execution/nightly-reports/2026-03-21-po-nightly-report.json`
- current Priority 1 in `products/task-management/04-execution/TOP_PRIORITIES.md`
- the identified problem is not lack of evidence but compact-surface drift between accepted reality and steering artifacts

That made Task Management the next low-risk, high-leverage rollout target after Security.

## Surfaces updated in this step
1. `products/task-management/06-architecture/INTERFACES.md`
   - Added the explicit Task Management -> Improvement interface.
   - Stated that compact-surface drift, stale steering surfaces, and recurring product-control gaps must route into canonical TDE-linked improvement work.
   - Added the six-field intake contract, closure-evidence rule, and first bounded deployment scope for this product.

2. `products/task-management/03-operating-model/OPERATING_MODEL.md`
   - Added the minimum improvement interface expectation to Task Management's recurring operating model.
   - Made review visibility explicit for open Task-Management-origin improvement items until disposition or closure.

## Result
The broader minimum improvement interface now has a second explicit product-side deployment case.
In Task Management it now covers:
- named signal class,
- canonical routing rule,
- required intake fields,
- closure-evidence expectation, and
- recurring review expectation.

## Remaining gap after this step
The interface still needs equivalent deployment into the remaining active product surfaces, but the rollout now spans both Security and Task Management with explicit product-side evidence.

## Completion evidence for this step
- `products/task-management/06-architecture/INTERFACES.md`
- `products/task-management/03-operating-model/OPERATING_MODEL.md`
- `products/task-management/04-execution/nightly-reports/2026-03-21-po-nightly-report.json`
- `products/improvement/04-execution/MINIMUM_IMPROVEMENT_INTERFACE_ROLLOUT_SEED_2026-03-21.md`
- `control/runtime/2026-03-21/improvement-minimum-interface-rollout-intake.json`
