# Control Panel Coordination Skill — Handoff Examples

## Canonical packet shape
```yaml
handoff_id: HL-YYYYMMDD-###
from_session_or_lane: control-panel
to_session_or_lane: <target>
purpose: request-action | request-status | escalate-blocker | clarify-ownership | transfer-next-step
requested_action: "<bounded action>"
due_or_timing: "now | today | this week | <timestamp> | none"
context_refs:
  - "<artifact path>"
expected_reply: "status | result | decision-needed | blocked"
standardization_scope: "same-runtime-multi-lane | none"
durable_update_required: true | false
update_target: "jobs/<JOB-ID>/STATE.md | jobs/<JOB-ID>/HANDOVER.md | product artifact path | none"
```

## When durable write-back is required
Use durable write-back when:
- ownership changes
- the request spans more than one step
- a blocker, decision, or constraint is involved
- the context would otherwise be lost after delay or compaction

## Preferred continuity target order
1. `jobs/<JOB-ID>/STATE.md`
2. `jobs/<JOB-ID>/HANDOVER.md`
3. relevant product artifact (`PLAN.md`, `DECISIONS.md`, etc.)
4. evidence note if the coordination itself is material/auditable

## Good example — bounded action request
```yaml
handoff_id: HL-20260310-010
from_session_or_lane: control-panel
to_session_or_lane: governance
purpose: request-action
requested_action: "Run one bounded VERIFY pass on A-002-I1 and return pass/fail/issues with one next action."
due_or_timing: "today"
context_refs:
  - "products/A-002/management/PLAN.md"
  - "jobs/JOB-GOV-001/STATE.md"
expected_reply: "result"
standardization_scope: "same-runtime-multi-lane"
durable_update_required: true
update_target: "jobs/JOB-GOV-001/STATE.md"
```

## Good example — status ask
```yaml
handoff_id: HL-20260310-011
from_session_or_lane: control-panel
to_session_or_lane: task-management
purpose: request-status
requested_action: "Confirm whether JOB-TM-002 has any open blocker or is ready for closeout."
due_or_timing: "now"
context_refs:
  - "jobs/JOB-TM-002/STATE.md"
expected_reply: "status"
durable_update_required: false
update_target: "none"
```

## Escalate instead of hand off when
- ownership is materially ambiguous
- the request crosses runtime/domain boundaries
- the request implies policy/architecture/authority change
- the target lane still would not have enough context even with refs
- no adequate continuity target exists
