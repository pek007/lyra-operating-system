# Product Inbox Coordination Model v1

Status: Draft active
Owner: Peter / Lyra
Date: 2026-03-12
Purpose: Interim coordination mechanism for cross-product requests while TDE-native coordination remains under development.

## Why this exists
The TDE UI pilot requires real collaboration between Task Management (`A-007`) and Delivery (`A-006`).

That exposes an immediate coordination problem:
- one product needs to request work, judgment, or delivery support from another,
- the request must be visible and auditable,
- but we do not yet want to block the pilot on designing the full long-term TDE coordination model.

This artifact defines a **temporary but structured** solution.

## Core principle
Use inboxes for **intake and handoff requests**.
Do **not** use inboxes as the long-term system of record for accepted cross-product execution state.

Inboxes are a bridge mechanism.
TDE remains the intended canonical home for accepted operational coordination state once the needed thin slice exists.

## Interim operating rule
Until TDE includes a fit-for-purpose coordination object:
- a product may issue a structured coordination request into another product's inbox,
- the receiving product must explicitly accept, reject, defer, or ask for clarification,
- material accepted work should be reflected into normal product execution state and decision artifacts,
- the inbox request should remain as the intake/audit entry, not the sole ongoing state tracker.

## Scope
This model is for:
- cross-product requests,
- handoffs,
- asks for bounded assessment or contribution,
- requests for delivery/review/readiness support,
- explicit decision-needed requests.

This model is not for:
- every internal note,
- broad strategy discussion,
- replacing the product plan,
- replacing TDE,
- replacing decision artifacts.

## Folder model
Each active product may have:
- `products/<product-slug>/08-inbox/`

Suggested initial use for current pilot:
- `products/task-management/08-inbox/`
- `products/delivery/08-inbox/`

## Inbox item naming
Use a sortable, explicit pattern:
- `REQ-YYYYMMDD-001__from-<product>__<short-slug>.md`

Example:
- `REQ-20260312-001__from-task-management__tde-ui-pilot-delivery-support.md`

## Minimum request structure
Each inbox request should contain:

### Header
- Request ID
- Date
- From product
- To product
- Requested by
- Status
- Urgency

### Body
- Purpose
- Requested outcome
- Why this request exists now
- What decision is needed, if any
- Expected response form
- Relevant refs
- Suggested next step

## Allowed statuses
Use only these interim statuses:
- `proposed`
- `accepted`
- `clarification-needed`
- `deferred`
- `rejected`
- `closed`

These are intake statuses, not the full delivery/task lifecycle.

## Required response behavior
The receiving product should respond in the same request artifact or a linked response note by stating one of:
- accepted
- rejected
- deferred
- clarification-needed

And include:
- owner,
- rationale,
- next action or expected next input,
- link to any product plan / decision / execution artifact where accepted work will continue.

## Canonical-state rule
A request becomes **real active work** only when it is reflected into at least one of:
- product execution plan,
- TDE state,
- decision artifact,
- delivery-unit / readiness / evidence flow,
- other explicitly named canonical execution surface.

A request left only in the inbox is still intake, not governed execution.

## Heartbeat usage rule
Heartbeats may be used to:
- check whether inboxes contain untriaged requests,
- surface important pending requests,
- remind the operator about aging requests.

Heartbeats must not be treated as the canonical decision mechanism.
Heartbeat is visibility support, not state authority.

## Review rule
Inbox requests should be reviewed during:
- weekly product review when relevant,
- milestone/gate review when the request materially affects release, readiness, or cross-product delivery.

Products should watch for inbox anti-patterns:
- accepted work never entering canonical execution state,
- old requests piling up without disposition,
- inboxes becoming shadow plans,
- decision requests being handled informally in chat without writing back.

## TDE end-state target
This inbox model is temporary.
The intended future state is a TDE-native coordination item with fields such as:
- requesting product,
- receiving product,
- linked objective,
- requested outcome,
- owner,
- decision-needed flag,
- current status,
- refs/evidence,
- acceptance/closure trail.

When that TDE thin slice exists, inboxes should remain optional intake surfaces only.

## Current recommendation for the TDE UI pilot
For the pilot:
1. Use product inboxes as the request-entry mechanism.
2. Require explicit accept/reject/defer/clarify responses.
3. Reflect accepted work into canonical product execution surfaces.
4. Capture material choices as decision artifacts rather than leaving them embedded in request prose.
5. Use the pilot to learn what the minimum TDE coordination object must contain.

## Short rule
**Inbox for intake. TDE for canonical coordination. Product plans/decisions/evidence for governed execution.**