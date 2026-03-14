# Product Owner Daily Priority Refresh Protocol v1

Status: Draft protocol
Owner: Lyra OS / Product Owners
Date: 2026-03-14

## Purpose
Define how each Product Owner refreshes the current top priorities from the full product stack before nightly reporting and overnight execution depend on them.

This protocol exists to prevent `TOP_PRIORITIES.md` from becoming a stale executive snapshot disconnected from current product reality.

## Core principle
Nightly reporting should consume current priorities from code.
That only works if Product Owners review the full product stack regularly and deliberately update `TOP_PRIORITIES.md` when needed.

## Scope
This protocol applies to active products that participate in recurring executive reporting, overnight coordination, or TDE-driven execution planning.

## Product stack to review
At minimum, the Product Owner should review:
- `PRODUCT.md`
- `MODEL.yaml`
- `01-identity/VISION.md`
- `02-strategy/STRATEGY.md`
- `03-operating-model/*` relevant operating and governance artifacts
- `04-execution/PLAN.md`
- `04-execution/RISKS.md` and/or `ROADMAP.md` when present
- `05-performance/METRICS.md` and readiness/health artifacts when present
- `07-decisions/DECISIONS.md`
- current TDE / execution reality / blockers / evidence
- current `04-execution/TOP_PRIORITIES.md`

## Daily refresh questions
The Product Owner should answer:
1. Is the product still pointed at the right outcome?
2. Does current execution still align with strategy?
3. What is the strongest current bottleneck?
4. Are the current top three priorities still correct?
5. Has any priority completed, become stale, or been overtaken by risk or dependency?
6. What is the next concrete step for each active priority?

## Refresh rule
If the answer to any of the above suggests the current priorities are stale, incomplete, or misordered, the Product Owner should update:
- `products/<slug>/04-execution/TOP_PRIORITIES.md`

before the nightly product-owner report is generated.

## Output of a refresh pass
A successful daily refresh produces one of two outcomes:

### Outcome A — No priority change
- `TOP_PRIORITIES.md` remains valid
- nightly report may state that priorities remain current

### Outcome B — Priority update required
- `TOP_PRIORITIES.md` is updated in code
- nightly report should reflect the refreshed priorities
- if the change is material, the report should note that the top priorities changed and why

## Trigger timing
Recommended timing:
- shortly before nightly product-owner reporting
- additionally whenever a product review, milestone, or major execution shift makes the current priorities stale

## Relationship to nightly reporting
Nightly reporting must not silently recreate priorities from scratch if a codified `TOP_PRIORITIES.md` exists.
Instead:
1. run the daily refresh logic
2. update `TOP_PRIORITIES.md` if needed
3. generate the nightly report from the refreshed code-based source

## Relationship to Control Tower
Product Owners own product-local priority refresh.
Control Tower owns cross-product overnight coordination.

If Control Tower needs portfolio rebalancing that materially affects product focus, that should result in a visible update to `TOP_PRIORITIES.md` rather than remaining only an implicit runtime preference.

## Anti-patterns
Avoid:
- treating nightly reporting as the hidden source of truth for priorities
- leaving `TOP_PRIORITIES.md` stale because the report can “figure it out” from broader context
- changing priorities casually without updating the canonical artifact
- using daily refresh to churn priorities without material cause

## Minimal implementation expectation
A product-owner nightly runtime should:
1. read the full product stack
2. compare it to current `TOP_PRIORITIES.md`
3. update `TOP_PRIORITIES.md` if stale or wrong
4. only then emit the nightly report

## Version
- v1.0
- Date: 2026-03-14
- Owner: Lyra OS / Product Owners
