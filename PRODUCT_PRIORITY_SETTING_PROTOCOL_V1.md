# Product Priority Setting Protocol v1

Status: Draft protocol
Owner: Lyra OS
Date: 2026-03-14

## Purpose
Define the mechanism for creating and updating `TOP_PRIORITIES.md` in the first place.

This protocol exists because a canonical priority artifact is only useful if there is a disciplined way to produce and revise it.

## Core principle
Top priorities should not be invented ad hoc by whatever report happens to run next.
They should be deliberately set through a product-aware process and then recorded in code.

## Priority-setting authority
### Product Owner owns proposal
The Product Owner for a product is responsible for proposing the current top three priorities for that product.

### Control Tower owns cross-product coordination
Control Tower may challenge, sequence, or rebalance product priorities when portfolio constraints or bottlenecks require it.

### Peter retains strategic override
Peter can override product priorities directly when needed.

## Inputs for priority setting
Priority setting should consider, at minimum:
- `VISION.md`
- `STRATEGY.md`
- `PLAN.md`
- `ROADMAP.md` and/or `RISKS.md` where present
- current bottlenecks
- current readiness/performance evidence
- major open decisions
- current TDE execution reality

## Standard priority-setting flow
### Step 1. Read current product state
Review the current product model and any current execution evidence.

### Step 2. Propose top three priorities
The Product Owner proposes the three priorities that would most improve progress toward the product vision now.

### Step 3. Test against portfolio reality
Check whether the proposed priorities:
- conflict with current portfolio bottlenecks
- duplicate another product's leading responsibility
- depend on blocked prerequisites
- are too broad or too weakly actionable

### Step 4. Refine to execution-grade priorities
Refine until each priority has:
- strategic relevance
- clear present-tense importance
- an actionable next step

### Step 5. Record in code
Write/update:
- `products/<slug>/04-execution/TOP_PRIORITIES.md`

### Step 6. Link to execution
Ensure each priority points to or implies:
- relevant plan/roadmap/task/decision artifacts
- the next concrete step that could be activated in TDE

## Trigger points
This protocol should run when:
- a product is first brought to Standard maturity
- a new `TOP_PRIORITIES.md` is being created
- a top priority completes or materially changes
- a product review identifies stale priorities
- Control Tower rebalances the portfolio
- Peter requests a priority refresh

## First creation rule
When a product has no `TOP_PRIORITIES.md` yet:
1. Product Owner proposes draft top three priorities from the canonical product artifacts.
2. Control Tower reviews for portfolio fit if the product is active in cross-product execution.
3. Record the first version in `04-execution/TOP_PRIORITIES.md`.
4. Mark it with the first creation date.

## Update cadence guidance
Suggested minimum cadence:
- update whenever materially stale
- review during product reviews
- review before recurring executive reporting systems depend on it heavily

## Relationship to nightly reporting
Nightly product-owner reports should normally consume `TOP_PRIORITIES.md`, not recreate it.
If the report detects that `TOP_PRIORITIES.md` is stale or missing, it should say so explicitly.
It may recommend an update, but should not silently invent a replacement unless explicitly acting in a priority-setting run.

## Relationship to TDE
`TOP_PRIORITIES.md` is not itself the task system of record.
It should, however, point toward the highest-value execution candidates that should be considered for TDE activation.

## Anti-patterns
Avoid:
- changing top priorities every day without material reason
- setting priorities with no next-step implications
- using reporting runs as the hidden source of truth for priorities
- letting portfolio coordination overwrite product ownership without explicit reason

## Recommended creation modes
### Mode A — Product initialization
Used when a product first receives a Standard-level execution layer.

### Mode B — Product-owner refresh
Used when current priorities are stale or completed.

### Mode C — Control-Tower rebalance
Used when portfolio coordination requires explicit reprioritization.

## Output
A successful run of this protocol produces:
- a created or updated `TOP_PRIORITIES.md`
- explicit linkage to the current product model and execution reality
- enough clarity for executive reporting to fetch from code rather than infer from scratch

## Version
- v1.0
- Date: 2026-03-14
- Owner: Lyra OS
