# TDE Intake Interface Contract v1

Status: Draft active
Owner: Peter + Lyra
Product: Task Management (`A-007`)
Date: 2026-03-14
Related:
- `products/task-management/03-operating-model/OPERATING_MODEL.md`
- `products/task-management/06-architecture/INTERFACES.md`
- `products/task-management/06-architecture/PXS_CONSUMPTION_INTERFACE.md`
- `products/task-management/07-decisions/TDE_INTENT_INTAKE_AND_FORMATION_POLICY_V1.md`
- `products/task-management/07-decisions/TDE_REQUEST_ENTRY_WORKFLOW_V1.md`

## Purpose
Define the canonical intake contract by which upstream systems, operators, and downstream consumer workspaces submit operational input into TDE.

This contract exists to make "use TDE" machine-usable rather than merely advisory.

## Design rule
There should be one canonical TDE intake surface, but it must accept multiple intake classes.

The important distinction is not separate ad hoc entry paths for every producer.
The important distinction is:
- one governed intake contract
- multiple typed intake classes
- explicit downstream routing rules

## Ownership and discovery rule
This is a product-owned interface artifact.

That means:
- AGENTS-level guidance should state only the principle that actionable work belongs in TDE
- workspace process discovery artifacts should route users to the applicable local front door and then to this product-owned contract when Task Management/TDE behavior is needed
- detailed intake behavior must not be copied into shared front-door docs or AGENTS files

## Canonical intake classes
Every intake packet must declare exactly one `intake_class`.

### 1. `direction`
Use for:
- vision
- strategic outcomes
- opportunity framing
- high-level goals
- initiative candidates

Meaning:
The input is meaningful but not necessarily execution-ready.

Expected handling:
- route to intent formation / planning
- propose bounded objective(s)
- avoid pretending a strategic aspiration is already a task

### 2. `decision`
Use for:
- judgment calls
- trade-offs
- approvals
- escalation candidates
- unresolved choices that block or shape work

Expected handling:
- route to decision framing / escalation / approval logic
- link to affected objective/work/task when present

### 3. `work`
Use for:
- directly actionable tasks
- implementation requests
- bounded follow-ups
- review/fix items ready for execution tracking

Expected handling:
- create or update executable work in canonical TDE state
- preserve explicit constraints and links

### 4. `signal`
Use for:
- status reports
- blockers
- risks
- confidence changes
- telemetry or review inputs
- prioritization inputs

Expected handling:
- triage first
- update existing work where possible
- create new work or decisions only when justified
- allow a valid outcome of "recorded, no further action"

### 5. `incident`
Use for:
- failures
- control breaks
- urgent exceptions
- operating conditions requiring fast routing or escalation

Expected handling:
- route to the incident/error path
- create or link urgent work and escalation artifacts as needed

## Canonical fields
Every intake packet must include at minimum:
- `contract_version`
- `intake_id`
- `intake_class`
- `source_system`
- `source_type`
- `source_reference`
- `submitted_at`
- `submitted_by`
- `title`
- `summary`
- `body`
- `priority_hint`
- `workspace_scope`
- `product_scope`
- `related_entities`
- `evidence_links`
- `proposed_action`

## Field intent
### Identity and idempotency
- `intake_id` must be stable enough for dedupe/idempotency handling
- `source_system` + `source_reference` must allow tracing back to origin

### Scope
- `workspace_scope` identifies the consumer/operating scope
- `product_scope` identifies the owning or affected product/domain when known

### Provenance
- `submitted_by` should identify the operator, agent, service, or workflow that produced the packet
- systems must not create anonymous canonical intake packets

### Content
- `title` and `summary` should be human-reviewable
- `body` may contain structured or semi-structured source detail
- `evidence_links` should point to supporting artifacts where relevant

### Routing hints
- `priority_hint` is advisory, not authoritative
- `proposed_action` may suggest routing but does not override policy

## Class-specific required content
### `direction`
Must include enough context to identify:
- desired outcome or change
- affected scope
- major constraint if already known

### `decision`
Must include:
- decision question
- options or tension when known
- why a decision is needed now

### `work`
Must include:
- bounded requested action
- enough context to execute or form execution-ready work
- success signal or completion condition when known

### `signal`
Must include at least one of:
- status
- blocker
- risk
- confidence change
- prioritization proposal

### `incident`
Must include:
- incident/failure summary
- immediate impact
- urgency/severity signal when known

## Routing policy
### `direction`
Default route:
- intent formation
- objective/initiative shaping
- clarification only when material

### `decision`
Default route:
- decision workflow
- escalation/approval handling
- optional linkage to work creation/update

### `work`
Default route:
- canonical work creation/update
- assignment/prioritization/state placement

### `signal`
Default route:
- triage
- merge into existing state when possible
- create work/decision only when warranted

### `incident`
Default route:
- incident/error path
- urgent work and escalation linkage as appropriate

## Producer adapter rule
Upstream systems must not rely on free-text assumptions alone.

Each meaningful producer should expose an explicit adapter from its native output into this contract.

Examples:
- product-owner nightly report adapter
- control-panel prioritization adapter
- manual operator entry adapter
- future email/chat/import adapters where justified

The producer adapter is responsible for:
- classifying the intake class
- populating required fields
- preserving provenance
- supplying stable source references
- avoiding silent loss of important constraints

## Validation gate
Before TDE accepts a packet into canonical handling, it should validate:
1. schema validity
2. required fields by intake class
3. provenance/source completeness
4. authorization of the producer where relevant
5. idempotency / duplicate handling
6. policy compatibility for the targeted route

Invalid packets should not be silently accepted.
They should be rejected, quarantined, or returned for correction with explicit validation output.

## Persistence rule
TDE should persist:
- the raw intake packet
- the normalized packet if transformation occurs
- the resulting canonical object link(s)
- the routing/decision outcome

This is required for:
- traceability
- replayability
- debugging
- auditability

## Decision and execution layering
This contract supports three distinct layers:
- intent layer
- decision layer
- execution layer

Interpretation guidance:
- `direction` usually enters at intent layer
- `decision` usually enters at decision layer
- `work` usually enters at execution layer
- `signal` may stay in intent/decision unless promoted
- `incident` may cut across decision and execution with urgency

## Example interpretation: nightly product-owner report
A nightly product-owner report should normally enter as `signal`, not `work`.

Recommended flow:
1. product owner emits a structured report packet
2. control panel enriches/prioritizes it through its adapter
3. TDE triages it as signal input
4. TDE decides whether to:
   - update existing work
   - create new work
   - create a decision item
   - record with no further action

This avoids converting every status observation into task spam.

## Workspace consumption rule
Consumer workspaces should not be told only "use TDE" with no local routing support.

Instead they should:
1. define their local task/decision/process front-door artifacts
2. point process discovery to those local front doors
3. consume this product contract when Task Management/TDE intake behavior is needed
4. avoid duplicating this contract in local AGENTS or discovery indexes

## Minimal machine-contract shape
Illustrative canonical packet shape:

```json
{
  "contract_version": "v1",
  "intake_id": "string",
  "intake_class": "direction|decision|work|signal|incident",
  "source_system": "string",
  "source_type": "string",
  "source_reference": "string",
  "submitted_at": "ISO-8601",
  "submitted_by": "string",
  "title": "string",
  "summary": "string",
  "body": "string or object",
  "priority_hint": "low|medium|high|critical|unspecified",
  "workspace_scope": "string",
  "product_scope": "string or null",
  "related_entities": [],
  "evidence_links": [],
  "proposed_action": "string or null"
}
```

## Machine-readable contract added
The first v1 schema for the intake packet is now defined in:
- `schemas/tde_intake_packet/v1.0.0.schema.json`

## Implementation expectation
The next as-code step should be to create:
1. producer adapter implementations for known sources
2. validation gates in request-entry/runtime tooling
3. test cases covering each intake class and invalid packet handling
4. canonical persistence and routing records for accepted packets

## Bottom line
"Use TDE" is not enough.

The durable operating answer is:
- one canonical intake contract
- typed intake classes
- producer adapters
- validation gates
- product-owned interface artifacts discoverable through local process front doors
