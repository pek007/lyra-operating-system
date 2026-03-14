# Product Top Priorities Standard v1

Status: Draft standard
Owner: Lyra OS
Date: 2026-03-14

## Purpose
Define a canonical, explicit, code-based artifact for the current top three priorities of each product.

This standard exists so product-owner reporting, portfolio coordination, and overnight execution do not need to infer current product priorities from broad product context alone.

## Core rule
Each mature product should maintain a canonical current-priority artifact at:

- `products/<slug>/04-execution/TOP_PRIORITIES.md`

This file is the executive-priority surface for the product.
It is not a backlog, not a roadmap, and not a substitute for `PLAN.md`.

## Why this artifact exists
`TOP_PRIORITIES.md` should make it easy to answer:
- What are the top three priorities for this product right now?
- Why do they matter for the product vision?
- What is the next concrete move on each?
- What supporting execution artifacts or tasks are linked?

## Relationship to other product artifacts
- `VISION.md` defines the intended future state.
- `STRATEGY.md` defines the chosen route.
- `PLAN.md` defines broader execution structure.
- `ROADMAP.md` may define sequence over time.
- `TOP_PRIORITIES.md` defines the current executive focus.

## Required location
Recommended canonical location:
- `04-execution/TOP_PRIORITIES.md`

Rationale:
- priorities are an execution concern
- they should remain close to current execution logic
- but separate from broader plan content

## Required structure
A valid `TOP_PRIORITIES.md` should contain:
- product name
- last updated date
- update authority / owner
- optional short framing note
- exactly three current priorities unless a deliberate exception is stated

For each priority include:
- title
- why this matters now
- current status
- next concrete step
- links to supporting artifacts/tasks/decisions where relevant

## Minimal template
```md
# TOP_PRIORITIES

Product: <name>
Last updated: <YYYY-MM-DD>
Owner: <role/person>

## Priority 1
**Title:** ...
**Why this matters now:** ...
**Current status:** ...
**Next concrete step:** ...
**Links:** ...

## Priority 2
**Title:** ...
**Why this matters now:** ...
**Current status:** ...
**Next concrete step:** ...
**Links:** ...

## Priority 3
**Title:** ...
**Why this matters now:** ...
**Current status:** ...
**Next concrete step:** ...
**Links:** ...
```

## Update rule
`TOP_PRIORITIES.md` must be updated when one or more of the following occurs:
- a priority is completed
- a priority is deprioritized or replaced
- product context changes enough that the top three are no longer accurate
- product review identifies mismatch between stated priorities and actual execution
- control-tower/portfolio coordination causes a material change in product focus

## Quality rule
A valid priority should be:
- meaningful enough to matter to the vision
- current enough to guide near-term action
- specific enough to support execution
- stable enough to avoid daily churn without cause

## Anti-patterns
Avoid using `TOP_PRIORITIES.md` as:
- a dumping ground for many tasks
- a narrative progress memo
- a duplicate of roadmap bullets
- a hidden backlog in executive language

## Consumption rule
When producing a product-owner executive report, read `TOP_PRIORITIES.md` first.
Use the rest of the product model as supporting context, not as the primary place to rediscover current priorities.

## Exceptions
If a product is too immature to define explicit top priorities yet, record that explicitly rather than pretending they are codified.

## Version
- v1.0
- Date: 2026-03-14
- Owner: Lyra OS
