# INTRA_LYRA_HANDOFF_PROTOCOL_V1.md

Status: Active v1 (standardized for same-runtime intra-Lyra handoffs)  
Owner: Lyra via Control Panel  
Date: 2026-03-10

## Purpose
Define a lightweight, practical protocol for coordination across Lyra sessions within the same runtime boundary.

This protocol is intentionally lighter than Vega's cross-domain handoff model. It is designed for:
- intra-Lyra coordination
- cross-session nudges and requests
- multi-step work that should not rely on copy-paste
- work that needs durable continuity without full cross-domain transfer controls

## When to use this protocol
Use it when:
- one Lyra session/product lane needs another to take action
- a request or blocker crosses session boundaries
- work will span more than one conversational turn or work cycle
- a human should not have to manually relay the request

Do not use it for:
- trivial one-message chat responses with no follow-up
- permanent cross-domain boundary transfers (use stricter domain handoff model where applicable)
- replacing durable job/product artifacts

## Core principle
Message for action. Write for continuity.

A session-to-session message can trigger work, but durable context must land in the right artifact when the handoff matters beyond the immediate turn.

## Minimal handoff packet
A valid intra-Lyra handoff should include at least:
- `handoff_id`
- `from_session_or_lane`
- `to_session_or_lane`
- `purpose`
- `requested_action`
- `due_or_timing` (or `none`)
- `context_refs`
- `expected_reply`
- `standardization_scope` (optional; use when evaluating or piloting protocol adoption)

## Suggested compact format
```yaml
handoff_id: HL-YYYYMMDD-###
from_session_or_lane: control-panel
to_session_or_lane: task-management
purpose: clarify-ownership | request-action | escalate-blocker | request-status | transfer-next-step
requested_action: "<clear action request>"
due_or_timing: "now | today | this week | <timestamp> | none"
context_refs:
  - "path-or-artifact"
  - "optional session/topic reference"
expected_reply: "status | result | decision-needed | blocked"
standardization_scope: "same-lane | same-runtime-multi-lane | broader | none"
durable_update_required: true | false
update_target: "jobs/<JOB-ID>/STATE.md | product artifact path | none"
```

## Transport rule
Default transport for intra-Lyra handoffs:
- `sessions_send`

Copy-paste should be fallback only.

## Write-back rule
If any of the following are true, update a durable artifact in the same work cycle:
- the handoff changes ownership or next actor
- the handoff affects more than one step
- the handoff includes a blocker, decision, or constraint
- the handoff will matter after session compaction or delay
- the receiver cannot safely continue without durable context

Preferred durable targets:
- job `STATE.md`
- job `HANDOVER.md`
- product `PLAN.md` / `DECISIONS.md` / relevant artifact
- evidence note for auditable or incident-like work

## Response contract
Receiver should respond in one of four forms:
- `status` — acknowledged, in progress
- `result` — completed, with artifact/evidence refs
- `decision-needed` — needs human or upstream decision
- `blocked` — cannot proceed, with specific blocker

If the sender is Control Panel, the sender should summarize only the high-signal outcome back into oversight artifacts.

## Control Panel role
Control Panel is the default coordinator for cross-session work.

Control Panel responsibilities:
- decide whether a handoff is needed
- send the initial concise packet
- ensure durable artifact update happens when required
- track unresolved handoffs if they affect oversight/priorities
- avoid becoming the place where all detailed execution context lives

## Session lane role
Product/session lanes should:
- act on handoffs relevant to their scope
- update the durable artifact when required
- respond with concise status/result/blocker
- avoid keeping important multi-step context only in chat replies

## Priority classes
Use these lightweight classes in the message body when helpful:
- `P1` — blocking / urgent
- `P2` — important / near-term
- `P3` — normal
- `P4` — informational / low urgency

## First operating rule set
1. Prefer `sessions_send` over copy-paste.
2. Keep the handoff message short and action-oriented.
3. Put durable state in files, not only in the message.
4. If the handoff changes ownership, update `HANDOVER.md` or `STATE.md`.
5. If the handoff is not durable, do not over-document it.
6. Control Panel coordinates; product lanes execute within scope.

## Example
```yaml
handoff_id: HL-20260310-001
from_session_or_lane: control-panel
to_session_or_lane: task-management
purpose: request-action
requested_action: "Validate whether the current Task Management lane should claim the first proof-case for real job-memory portability and propose the smallest viable test flow."
due_or_timing: "today"
context_refs:
  - "RUNTIME_ASSIGNMENT_MAP_V1.md"
  - "JOB_MEMORY_PORTABILITY_PROCESS_V1.md"
expected_reply: "result"
durable_update_required: true
update_target: "jobs/JOB-TEMPLATE/STATE.md"
```

## Non-goals
- Full approval workflow replacement
- Cross-domain trust-boundary enforcement
- Heavyweight ticketing/queue semantics
- Duplicating TDE as a chat-layer protocol

## Current standardization status
- Standardized for: same-runtime intra-Lyra handoffs across Lyra lanes
- Evidence basis: first live viability, same-lane repeatability, Governance transfer proof case, and Delivery transfer proof case
- Not standardized for: cross-runtime or cross-domain handoffs where stronger boundary controls may be needed

## Version
- v1.2
- Date: 2026-03-10
