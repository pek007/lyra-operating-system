# PXS Consumption Interface

Status: Draft active
Product: Task Management (`A-007`)
Consumer: `pxs`
Date: 2026-03-11
Owner: Lyra

## Purpose
Define the formal first-pass interface by which `pxs` consumes Task Management capability.

This artifact exists to make the downstream consumption path explicit enough that `pxs` does not depend on tribal knowledge, chat history, or hidden workspace assumptions.

## Interface goal
`pxs` should be able to consume Task Management as a capability that helps it:
- make work visible
- keep task state explicit
- capture decisions with enough structure to act on them later
- reduce dropped work and coordination ambiguity
- operate through a clearer execution system rather than thread memory alone

## What `pxs` consumes
### 1. Operating pattern
`pxs` consumes the Task Management operating pattern:
- meaningful work should map to explicit goals or outcomes
- active work should have visible state
- blockers should be explicit
- real decisions should be captured as decisions rather than buried in chat
- meaningful completion should have some evidence where appropriate

### 2. Artifact-level interface
`pxs` consumes these artifact expectations:
- task/decision state should live in the designated operational system of record
- decision-relevant work should link to rationale or decision records
- active work should not depend on transcript reconstruction alone
- important follow-through should be inspectable by another operator or agent
- the consumer workspace should provide a usable local operating package front door so these expectations are discoverable in local context

Current first-pass local workspace operating package examples in `pxs` now include:
- `WORKSPACE_PROFILE.md`
- `SOURCE_OF_TRUTH.md`
- `PROCESS_DISCOVERY_INDEX.md`
- `TASK_SYSTEM_OF_RECORD.md`
- `DECISION_AND_ESCALATION.md`
- `ERROR_AND_INCIDENT_HANDLING.md`

### 3. Management-layer interface
`pxs` consumes these management expectations:
- there is a visible owner or operating role for meaningful work
- active work can be reviewed through a compact product/task lens
- recurring friction should become improvement work rather than remaining implicit

## What remains internal to Task Management
The following remain internal product design choices unless separately exposed:
- exact internal implementation details of TDE
- product-internal architecture and refactoring choices
- broader product-model experimentation not required for consumer use
- internal-only readiness debates that do not affect the consumer-facing operating contract

## Consumer obligations for `pxs`
For the interface to work, `pxs` must:
1. use the designated task/decision operating substrate rather than relying only on chat memory
2. keep meaningful work linked to explicit outcomes where possible
3. surface blockers and decisions explicitly enough to be reviewable
4. avoid creating shadow operational systems that conflict with the consumed Task Management layer
5. maintain enough local workspace operating package structure that task, decision, process, and error routes are explicit in the consumer scope

## Provider obligations for Task Management
Task Management must:
1. keep the operating expectations explicit and stable enough to use
2. provide enough guidance that `pxs` can adopt the capability without bespoke rescue work
3. avoid hidden dependencies on Lyra-internal context where those dependencies affect consumption
4. keep readiness, boundary, and evidence expectations visible

## Current interface shape
Current shape is **artifact-and-operating-model based**, not yet a dedicated service or packaged capability.

That means the interface currently depends on:
- documented operating rules
- product/task artifacts
- TDE-related contracts and readiness rules
- visible review and decision discipline

## Evidence of usable consumption
This interface should be considered operationally usable when:
- `pxs` can use the task/decision operating pattern with minimal custom explanation
- another operator/agent can inspect active work and understand what matters, what is blocked, and what was decided
- important work is not disappearing into thread memory alone
- recurring friction in `pxs` can be converted into explicit improvement work

## Current known gaps
- the exact system-of-record mechanics for `pxs` still need clearer operational examples
- readiness is still easier to describe than measure compactly
- the boundary between product-internal model sophistication and consumer-required simplicity still needs discipline

## Next likely interface evolution
Possible future shapes:
- clearer capability-pack style distribution
- a more explicit schema-backed task/decision contract
- a service boundary for consumer interaction if/when justified

For now, the correct interface is a documented operating contract with explicit reviewability and evidence expectations.
