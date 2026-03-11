# Error Reporting Standard v1

Status: Draft active standard
Owner: Peter / Lyra
Date: 2026-03-11

## Purpose
Define a lightweight standard for reporting incidents, near misses, and control/process failures in PX Strategy / Lyra OS.

This standard exists to make error reporting:
- structured enough to support learning and prevention
- linked to ownership and corrective action
- compatible with Product-as-Code and the process-ownership rule
- light enough to use without creating documentation theater

## Core principle
An error report is not just a retrospective note.
It is a structured learning/control artifact that should help the system:
- understand what happened
- understand why it happened
- reduce recurrence risk
- make ownership and closure explicit

## Ownership rule
Error reporting follows the same ownership rule as processes.

### Product-local errors
If the issue primarily occurred inside one product boundary, the owning product should own the error report.

Examples:
- Task Management readiness failure
- Delivery verification failure
- Security posture/control miss
- Control Panel runtime incident

These reports should normally live inside the owning product domain.

### Shared/system errors
If the issue is cross-product, system-level, or reveals a coordination/control failure across boundaries, a shared/system error report is justified.

Examples:
- wrong Git root used for sync decisions
- cross-product handoff confusion
- canonical repo ambiguity
- portfolio-level coordination/control failure
- cross-runtime context failure

These reports may live centrally.

## Report types
Use one of these simple types:
- **incident** — an actual failure or harmful event occurred
- **near_miss** — failure was narrowly avoided
- **control_failure** — an intended safeguard/check did not work as expected
- **process_failure** — a process broke down or was followed incorrectly
- **decision_failure** — a decision path was materially wrong, unclear, or made on the wrong basis

## Scope levels
Use one of these scope labels:
- **product_local**
- **cross_product**
- **system_level**

## When a report is required
A report should usually be created when one or more are true:
1. real impact or material risk occurred
2. a control failed or nearly failed
3. the same class of mistake could plausibly recur
4. multiple products/contexts were affected
5. human intervention was needed to prevent worse outcome
6. the event exposed an architectural ambiguity
7. the event changed trust, correctness, delivery, or governance assumptions

Do **not** require heavy reports for every tiny mistake.
The standard is for meaningful errors and near misses, not routine noise.

## Minimum report fields
Each error report should include:
- error ID
- date
- title
- type
- scope
- owning product or owner
- affected products/contexts
- summary
- impact
- detection method
- root cause
- contributing factors
- immediate mitigation
- corrective actions
- preventive changes
- owner
- status
- review / closure date
- links to related artifacts (tasks, decisions, evidence, product docs)

## Effective use rule
Every error report should produce at least one of:
- a corrective task
- a product-model update
- a control/process change
- a decision record
- a closure/verification check

If it produces none of these, it is probably not yet an effective operational error report.

## Relationship to Product-as-Code
Error reports do not replace product models.
They should feed product models by causing updates where needed.

Examples:
- product-local error -> update product `RISKS.md`, `GOVERNANCE.md`, `PLAN.md`, or `DECISIONS.md`
- shared/system error -> update shared rules, portfolio artifacts, or coordination mechanisms

## Relationship to process ownership rule
This standard should not create a parallel central error-reporting layer.

Instead:
- product-owned issues stay with products
- shared/system issues stay central only when genuinely cross-boundary

## Suggested storage pattern
### Product-local
Store inside the product domain, e.g.:
- `products/<slug>/errors/ERR-...md`
- or another clearly named product-local incident/error folder if needed

### Shared/system
Store centrally only for cross-product/system issues, e.g.:
- workspace root
- `governance/`
- another shared/system location if standardized later

## Review/closure rule
An error report should remain open until:
- immediate mitigation is complete
- corrective actions are assigned
- preventive action is defined or consciously declined
- closure criteria are met and recorded

## Short rule
**Error reports are structured learning/control artifacts. Products own product-local errors; shared artifacts own only cross-product/system errors.**
