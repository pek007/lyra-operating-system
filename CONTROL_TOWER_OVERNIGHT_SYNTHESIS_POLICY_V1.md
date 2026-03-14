# Control Tower Overnight Synthesis Policy v1

Status: Draft policy
Owner: Control Tower / Lyra OS
Date: 2026-03-14

## Purpose
Define how overnight product-owner signals should be synthesized into a coordinated portfolio view and converted into selected overnight execution priorities.

This policy exists to prevent every product from independently promoting its own local top priority into execution without portfolio coordination.

## Core principle
Product Owners report product-local truth.
Control Tower decides cross-product overnight execution priorities.

## Inputs
Control Tower overnight synthesis should use:
- the current nightly product-owner reports
- current `TOP_PRIORITIES.md` artifacts for active products
- current TDE execution state
- current known blockers, risks, and readiness signals
- current strategic phase and portfolio bottleneck

## Main questions
Control Tower should answer:
1. What is the strongest current portfolio bottleneck?
2. Which product-local priorities matter most now at the portfolio level?
3. Which proposed actions should become overnight TDE execution priorities?
4. Which signals should be recorded but not promoted into action?
5. What, if anything, may require Peter in the morning?

## Promotion rule
A nightly product-owner report should not automatically become work.
It should first be treated as signal.

Control Tower may decide to:
- update existing active work
- create new work
- create a decision item
- record with no further action

## Default overnight selection rule
Control Tower should normally select only **1-3 overnight execution priorities** across the portfolio.

Selection should favor:
- the strongest current bottleneck
- the highest leverage path toward current strategic objectives
- work that is executable overnight without requiring fresh human judgment
- low-risk movement with clear next steps

Selection should avoid:
- local optimization that ignores portfolio reality
- spreading effort too thinly across products
- activating work that is blocked by missing decisions or dependencies

## Product-owner vs Control-Tower roles
### Product Owner
- maintains product-local priorities
- reports product-local truth
- recommends next actions

### Control Tower
- judges cross-product leverage
- resolves local-priority collisions
- selects overnight execution priorities
- decides what should enter or change in TDE now

## Required synthesis output
A valid overnight synthesis note should contain:
- portfolio bottleneck
- selected overnight priorities (1-3)
- what was activated/updated in TDE
- what was done immediately
- what remains blocked
- what may require Peter before 07:00

## Relationship to TDE
Control Tower synthesis should ideally produce canonical TDE outcomes via the Task Management intake/triage path rather than relying only on chat-level interpretation.

The synthesis note is the executive projection.
The TDE update is the operational commitment.

## Relationship to morning summary
The morning summary should be derived from:
- overnight selected priorities
- overnight TDE movement
- blockers and decisions surfaced during the execution loop

## Anti-patterns
Avoid:
- selecting one top item from every product just for symmetry
- treating every reported priority as execution-worthy now
- making overnight execution a hidden portfolio strategy reset
- leaving important portfolio trade-offs implicit

## Review/update rule
This policy should be updated when:
- the overnight cadence changes materially
- TDE-native intake/signal handling becomes the primary runtime path
- strategic phase changes alter the portfolio bottleneck logic

## Minimal implementation expectation
The overnight runtime should:
1. gather product-owner report signals
2. compare them against current portfolio bottleneck and TDE state
3. select 1-3 overnight priorities
4. update TDE accordingly
5. emit a concise executive synthesis summary

## Version
- v1.0
- Date: 2026-03-14
- Owner: Control Tower / Lyra OS
