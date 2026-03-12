# TDE Assigned Work Wakeup Model v1

Status: Draft active
Owner: Peter / Lyra
Date: 2026-03-12
Related artifacts:
- `OBJECTIVE_TO_PRODUCTION_GAP_MAP_V1.md`
- `OBJECTIVE_START_GATE_V1.md`
- `ONE_ITERATION_TDE_UI_PILOT_V1.md`

## Purpose
Define a TDE-native mechanism for responsive handoff and collaboration.

The core idea is simple:
**when a new assigned work item enters canonical TDE state, the assignee should be notified or woken automatically.**

This is intended to replace mailbox-style coordination as the primary handoff mechanism.

## Why this exists
The inbox experiment showed that storage and visibility are not enough.
A request can exist and be visible without creating actual response, ownership, or collaboration.

The missing primitive is not “mailbox.”
It is:
- assignment,
- activation,
- response,
- canonical collaboration state.

## Design hypothesis
If TDE can natively support:
1. assigned work items,
2. assignee wake/notification,
3. explicit response semantics,
4. shared canonical work state,

then most cross-product handoff complexity collapses into one cleaner operating primitive.

## Core model
### Primary object
Use a generalized **Assigned Work Item** rather than only a simple task.

This object may represent:
- a task,
- a handoff,
- a decision request,
- a review request,
- a dependency/unblock request,
- a bounded delivery/support request.

## Minimum fields
An Assigned Work Item should contain at least:
- `work_item_id`
- `title`
- `work_type`
- `requester`
- `assignee`
- `linked_objective_id` or equivalent strategic linkage
- `requested_outcome`
- `status`
- `priority`
- `decision_needed` (bool or structured flag)
- `artifact_refs[]`
- `evidence_refs[]`
- `created_at`
- `assigned_at`
- `due_at` or review date where relevant
- `response_required`
- `wake_status`

## Recommended work types
Initial useful values:
- `task`
- `handoff`
- `decision-request`
- `review-request`
- `dependency-request`
- `delivery-support`
- `other`

## Lifecycle
Recommended minimum lifecycle:
- `proposed`
- `assigned`
- `acknowledged`
- `active`
- `blocked`
- `decision-needed`
- `response-ready`
- `delivered`
- `closed`
- `rejected`
- `retired`

## Status intent
- `proposed`: item exists but is not yet assigned
- `assigned`: assignee has been named; wake/notification should occur
- `acknowledged`: assignee has seen and acknowledged the item
- `active`: assignee is working it
- `blocked`: assignee cannot continue without dependency/decision
- `decision-needed`: explicit decision is required to proceed
- `response-ready`: bounded result exists and is ready for requester review
- `delivered`: result has been handed back
- `closed`: collaboration loop complete
- `rejected`: assignee declines item
- `retired`: item intentionally stopped/cancelled

## Wake-up semantics
### Core rule
Whenever an item enters `assigned` with a valid assignee, TDE must attempt an activation event.

### Activation event options
Depending on current runtime maturity, activation may mean one or more of:
- notify an existing product/session owner,
- wake the main session with a structured event,
- spawn a product-specific execution context,
- enqueue a product-specific run,
- mark the item on an explicit assignee queue that must be serviced.

### Wake status
Suggested values:
- `not-needed`
- `pending`
- `sent`
- `acknowledged`
- `failed`

### Fail-closed rule
An assigned item should not be assumed active merely because it has an assignee.
If no wake/acknowledgment occurs, the item remains assigned but unacknowledged.

## Response contract
The assignee must be able to return a bounded response of one of these forms:
- `acknowledged`
- `accepted`
- `rejected`
- `clarification-needed`
- `blocked`
- `completed`

Each response should write back to canonical state with:
- responder
- timestamp
- rationale
- next step
- linked artifacts/evidence where relevant

## Roles
### Requester
Creates the assigned item and defines the requested outcome.

### Assignee
Receives wake/notification, acknowledges the item, and returns progress or result.

### Approver
Decides when policy/risk requires explicit approval.

### TDE / Control layer
Maintains canonical state, triggers wake events, records acknowledgments/responses, and preserves the collaboration trail.

## Interaction model
Recommended flow:
1. requester creates Assigned Work Item
2. TDE records item canonically
3. TDE sets assignee and triggers wake event
4. assignee acknowledges or responds
5. work moves through active/blocked/decision-needed as needed
6. assignee returns bounded result
7. requester reviews/accepts
8. item closes with full audit trail

## Why this is cleaner than inboxes
Mailbox coordination separates request storage from assignee activation.
That creates silent failure modes.

Assigned-work wakeup combines:
- request,
- assignment,
- activation,
- response,
- collaboration state

into one canonical mechanism.

## Current implementation path
### Phase 1 — Minimal viable implementation
- add Assigned Work Item object to TDE state model
- support requester + assignee + status + refs + response contract
- add wake event generation when status becomes `assigned`
- require acknowledgment before treating the item as active

### Phase 2 — Operational hardening
- explicit assignee queues
- aging/timeout/escalation rules
- blocked/dependency handling
- decision-needed handling tied to decision records

### Phase 3 — Full collaboration layer
- integrate with objective packets and Delivery Units
- allow work-item chains and dependency graphs
- add richer metrics and SLA-style visibility

## Immediate design implications
This model suggests that inboxes should no longer be treated as the intended long-term path.
If retained at all, they should be treated only as:
- historical experiment artifacts,
- optional human-facing intake views,
- or compatibility surfaces over canonical assigned-work state.

## Current recommendation
Prioritize this as the next TDE-native coordination primitive.

Short rule:
**Assigned item enters canonical TDE state -> assignee wakes -> assignee acknowledges -> collaboration continues in TDE.**
