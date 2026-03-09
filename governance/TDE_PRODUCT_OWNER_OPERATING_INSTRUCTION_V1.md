# TDE Product Owner Operating Instruction v1

Status: Active
Owner: Peter Eklind
Applies to: All Lyra OS product owners and product-like workstreams
Date: 2026-03-09

## Purpose
Define how Product Owners should use the Task & Decision Engine (TDE) now that it is the canonical operating substrate for task execution state.

The intent is not just to keep work organized. The intent is to make the system operate from high-level goals downward, while continuously improving execution quality, decision quality, and product leverage over time.

## Policy statement
Product Owners must use TDE as the canonical operational layer for active work, decision visibility, execution evidence, and improvement capture.

TDE is not a replacement for product judgment. It is the mechanism that turns product judgment into visible, auditable, improvable execution.

## What Product Owners are responsible for
Each Product Owner is responsible for making sure their product:
1. Operates from explicit goals and outcomes, not just loose tasks.
2. Keeps active work visible in the canonical TDE runtime, not in side lists or chat memory.
3. Surfaces decisions, blockers, dependencies, and approvals explicitly.
4. Accumulates evidence of progress and problems.
5. Uses that evidence to improve the product, the workflow, and the surrounding operating system.

## Core operating rule
Start from goals. Use TDE to drive execution downward from those goals.

That means:
- Goals define what matters.
- Plans define what should move next.
- TDE tracks what is active, blocked, waiting, or done.
- Decisions and evidence explain why progress happened or stalled.
- Improvement work is captured as first-class work, not treated as optional cleanup.

## Required behaviors
### 1) Link work to objectives
Do not allow meaningful work to float without outcome context.

For active or decision-relevant work, Product Owners should ensure there is a clear link to:
- product goal
- initiative or intended outcome
- rationale for why the work matters now

If a task cannot be explained in outcome terms, it should usually be:
- clarified,
- decomposed,
- moved back to triage, or
- dropped.

### 2) Keep TDE as the operational system of record
Do not run the product from:
- chat threads,
- private scratch lists,
- untracked ad hoc notes,
- parallel task boards that drift from TDE.

Discussion can happen anywhere. Operational state should not.

### 3) Make decisions visible
When progress depends on a real choice, capture it as a decision need, not as vague delay.

Examples:
- scope trade-off
- sequencing choice
- quality vs speed judgment
- dependency escalation
- approval request
- rollback vs proceed call

A blocked task without a visible decision path is usually governance debt.

### 4) Require evidence, not just movement
Completion is not just “someone says it’s done.”

Product Owners should expect visible evidence where appropriate, such as:
- verification artifact
- test result
- deployment/cutover note
- updated contract/SOP
- documented decision rationale
- customer/product-facing proof of usability

If there is no useful evidence, the system is likely optimizing for motion rather than progress.

### 5) Treat improvement as part of delivery
Every product should continuously capture:
- repeated friction
- recurring failure modes
- handoff confusion
- missing interfaces
- weak visibility
- poor quality loops
- work that should become standard, automated, or policy-backed

Improvement items should be recorded and prioritized through the same operating discipline as feature or delivery work.

## Anti-patterns to avoid
Product Owners should actively avoid:
- managing by chat alone
- equating activity with progress
- allowing “important but ownerless” work to accumulate
- keeping work active without a clear next decision or next action
- using TDE only for low-level tasks while strategy remains disconnected
- treating continuous improvement as side work for “later"
- keeping shadow systems because they feel faster in the moment

## Practical weekly posture for Product Owners
At least weekly, each Product Owner should be able to answer:
1. What are this product’s current goals?
2. What active work in TDE is directly advancing those goals?
3. What is blocked, and is the blocker operational or decisional?
4. What evidence shows actual progress this week?
5. What recurring friction should become an improvement item?
6. What should be stopped, simplified, automated, or clarified?

If these answers are hard to produce, the product is not yet operating cleanly enough.

## Expected use of TDE for maximum leverage
TDE should be used to create leverage in five ways:

### A. Goal-to-execution alignment
So work can be traced back to why it exists.

### B. Decision quality
So important choices are explicit, reviewable, and not buried in conversation.

### C. Reliable follow-through
So active work has visible state, bounded WIP, and fail-closed behavior where needed.

### D. Learning loop
So evidence from execution improves future planning, interfaces, and standards.

### E. System compounding
So each product improves not only its outputs, but the quality of the operating system around it.

## Minimum standard for a healthy Product Owner operating in TDE
A healthy Product Owner should be able to show that:
- product goals are explicit
- active work is visible in TDE
- decisions are surfaced when required
- evidence exists for meaningful progress
- improvement items are being captured and acted on
- the product is becoming easier to operate over time

## Leadership expectation
Product Owners are not just backlog managers.

They are responsible for turning strategic intent into a controlled execution system that gets smarter over time.

TDE is the mechanism for doing that.

## Immediate implementation guidance
All Product Owners should now:
1. Review their active product goals and make sure current work maps to them.
2. Eliminate any shadow operational list that conflicts with TDE state.
3. Identify one current blocked item that should be reframed as an explicit decision.
4. Identify one recurring friction that should become an improvement item.
5. Use TDE as the default place to inspect active operational state going forward.
