# A-007 — Interfaces

Status: Draft v0.1
Product: Task Management
Primary capability: TDE

## Purpose
Define the first product-facing interface expectations for consuming Task Management/TDE, with `pxs` as the first downstream customer.

## Consumer model (v0.1)
Task Management exposes a controlled execution capability rather than open-ended direct state mutation. Consumers submit task/decision work through explicit request artifacts or versioned capability interfaces, and receive structured status/outcome evidence.

## Inbound interface categories
1. **Task request**
   - Consumer asks TDE to execute a defined unit of work
   - Required contract (to be finalized): request id, objective/context link, task type, priority, authority context, requested output

2. **Decision/escalation request**
   - Consumer requests a decision path or asks TDE to surface a blocked item for human review
   - Required contract (to be finalized): decision context, options or blocker, risk level, required approver if known

3. **Recurring/cadence-managed work**
   - Consumer registers or consumes recurring operational work via approved job/binding primitives
   - Required contract (to be finalized): cadence, owner, authority scope, evidence expectations, rollback/disable path

## Outbound interface categories
1. **Acknowledgement/status**
   - Accepted / rejected / blocked / in-progress / complete
2. **Outcome payload**
   - Result, generated artifacts, or no-op explanation
3. **Escalation payload**
   - Reason for human intervention, required decision, risk/impact note
4. **Audit/evidence reference**
   - Evidence path(s), event/action ids, or related decision artifact references

## Delivery principles
- Prefer explicit, versioned, reusable interfaces over hidden workspace coupling
- Preserve workspace and authority boundaries in line with `LYRA_OS_PXS_INTEGRATION_PLAN_V1`
- High-risk mutation paths should move toward deterministic service/plugin interfaces over time
- Consumer experience should minimize bespoke interpretation by operators

## Current gaps
- No finalized request schema published yet
- No consumer-facing compatibility/versioning note yet
- No completed `pxs` pilot evidence yet

## Immediate next interface work
- Define a minimal request/output schema for first `pxs` pilot use cases
- Select transport path for v1 consumption (likely document/artifact mediated first, capability-pack or service path later)
- Add validation and error semantics before wider rollout
