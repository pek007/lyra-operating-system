# PXS Consumption Interface

Status: Pilot-operational (bounded)
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
- when `pxs` needs Task Management/TDE intake behavior, it should rely on the product-owned intake contract rather than inventing workspace-local intake semantics

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
- live producer emission from inside `pxs` runtime flows is not yet proven
- automated provider-side processing is not yet implemented
- integrated nested-payload validation in one runtime processor is not yet in place

## Minimal executable slice v1

### Design choice
The first executable slice uses **artifact-mediated packet exchange**, not a dedicated live service boundary.

Reason:
- it matches the current Lyra OS -> `pxs` boundary posture
- it keeps transport explicit without introducing premature runtime coupling
- it can be validated and exercised immediately using current artifacts and tooling

### Transport
Initial transport choice:
- `pxs` produces a request packet as a governed artifact
- Task Management consumes that packet through the product-owned intake/acceptance contracts
- Task Management returns an explicit response artifact/result rather than relying on inferred success

This keeps the first executable contract compatible with:
- current workspace/package discipline
- explicit artifact review
- future evolution toward stronger schema/service packaging if justified

### Request envelope
Initial request envelope:
- envelope id
- envelope version
- consumer workspace (`pxs`)
- request type (`intake` | `assignment_acceptance`)
- referenced canonical contract
- payload schema/version
- payload artifact or inline payload reference
- submitted by
- submitted at
- source reference

Semantics:
- `request_type=intake` maps to `TDE_INTAKE_INTERFACE_CONTRACT_V1.md`
- `request_type=assignment_acceptance` maps to `TDE_ASSIGNMENT_ACCEPTANCE_CONTRACT_V1.md`
- the envelope does not replace the canonical product contracts; it makes `pxs` consumption explicit and versionable

### Response envelope
Initial response envelope:
- response id
- response version
- request id
- handled by
- handled at
- status (`accepted` | `accepted_no_runner` | `accepted_pending_binding` | `rejected_invalid_request` | `duplicate` | `recorded_no_action`)
- canonical target refs (task id, decision ref, evidence ref, or artifact ref as applicable)
- validation errors (if any)
- note

Semantics:
- when the request type is assignment-focused, the response should align to the assignment-acceptance result vocabulary wherever possible
- `recorded_no_action` is allowed for signal/intake cases where valid recording does not justify new executable work
- success must be explicit; no consumer should infer success from side effects alone

### Validation and error semantics
Validation rules for the first slice:
1. request envelope must be structurally valid
2. referenced canonical contract must be declared
3. payload version must be present
4. provenance/source fields must be complete
5. invalid requests must fail closed with explicit response output

Error/result stance:
- invalid envelope or incompatible payload -> `rejected_invalid_request`
- valid duplicate request -> `duplicate`
- valid intake recorded but no new executable action required -> `recorded_no_action`
- valid assignment packet accepted but no runner -> `accepted_no_runner`
- valid assignment packet accepted but binding incomplete -> `accepted_pending_binding`

### Compatibility and versioning
Versioning rules:
- request and response envelopes each carry their own version
- canonical payload contracts keep their own independent versioning
- breaking changes require explicit version bump
- `pxs` must declare which envelope version it emits
- Task Management must state which versions it accepts

### Worked examples
#### Example 1 — executable work intake
`pxs` emits:
- request type: `intake`
- canonical contract: `TDE_INTAKE_INTERFACE_CONTRACT_V1.md`
- payload class: `work`
- source reference: a concrete `pxs` artifact or issue

Expected response:
- status: explicit acceptance/recording result
- canonical target ref: created/updated task or linked artifact
- note: any next-step clarification

#### Example 2 — assignment acceptance request
`pxs` emits:
- request type: `assignment_acceptance`
- canonical contract: `TDE_ASSIGNMENT_ACCEPTANCE_CONTRACT_V1.md`
- payload schema: `tde_assignment_packet@1.0.0`

Expected response:
- status: one of `accepted`, `accepted_no_runner`, `accepted_pending_binding`, `rejected_invalid_request`, `duplicate`
- canonical target ref: created/updated task id when applicable
- validation output when rejected

#### Example 3 — signal intake with no new task
`pxs` emits:
- request type: `intake`
- canonical contract: `TDE_INTAKE_INTERFACE_CONTRACT_V1.md`
- payload class: `signal`
- source reference: review/status artifact

Expected response:
- status: `recorded_no_action` or explicit linked update result
- canonical target ref: updated artifact/evidence reference where applicable

## Current maturity
The `pxs` -> Task Management contract should now be treated as **pilot-operational for bounded use**.

Evidence supporting that status:
- executable contract slice defined in this interface artifact
- request/response envelope schemas added and registered
- worked examples validated against the schemas
- thin pilot completed
- semi-real pilot completed against a real `pxs` planning artifact
- first real bounded handling flow completed with a real Task Management state update
- response-state coverage now includes `accepted`, `accepted_no_runner`, `accepted_pending_binding`, `rejected_invalid_request`, `duplicate`, and `recorded_no_action`
- minimal deterministic processor now validates request envelope + nested payload and emits a response envelope for bounded cases
- processor now deterministically handles bounded cases for `accepted`, `duplicate`, `rejected_invalid_request`, `accepted_pending_binding`, `accepted_no_runner`, and `recorded_no_action`
- governed write-path now exists for deterministic response-envelope output under `control/runtime/pxs-tm-responses/`
- first bounded producer path now exists: `pxs/docs/now-next-later.md#next` -> governed request artifact -> processor -> governed response artifact

This is not yet full operational automation, but it is beyond descriptive design.

## Next likely interface evolution
Near-term expected shape:
- tighter compatibility notes for consumer/provider versions
- expanded bounded handling logic for `accepted_no_runner`, `accepted_pending_binding`, and `recorded_no_action`
- optional additional producer paths beyond `now-next-later.md#next` once the first path remains stable

Possible later shapes:
- clearer capability-pack style distribution
- fuller schema-backed task/decision contract
- a service boundary for consumer interaction if/when justified

For now, the correct interface is a documented operating contract with a first executable slice, which should next be backed by concrete schemas and pilot examples before downstream consumption claims are treated as proven.
