# CONTROL_PANEL_COORDINATION_SKILL_SPEC_V1.md

Status: Active draft v1  
Owner: Lyra via Control Panel  
Date: 2026-03-10

## Purpose
Define the first implementation-ready specification for the **Control Panel coordination skill**.

This skill is intended to package the now-validated same-runtime intra-Lyra coordination pattern into a repeatable, bounded operating capability for Control Panel.

## Why this skill is first
This is the strongest first build candidate because:
- the coordination pattern has already been validated live
- the protocol is standardized for same-runtime intra-Lyra handoffs
- repeated manual orchestration is already visible in daily work
- the skill can reduce friction immediately without changing deeper product/runtime boundaries

## Scope
The skill helps Control Panel:
- decide whether a handoff is needed
- package a bounded handoff cleanly
- route it to the correct lane/session
- ensure durable write-back expectations are explicit
- summarize only the high-signal outcome back into oversight artifacts

## Non-goals
This skill does **not**:
- replace product-lane execution
- decide portfolio strategy on its own
- bypass canonical task/job/system-of-record contracts
- handle cross-runtime or cross-domain transfers using the lighter same-runtime protocol
- become a generic planner for all cross-product work

## Primary use cases
1. **Request action**
- Control Panel needs another lane to take a bounded next action.

2. **Request status**
- Control Panel needs a concise status/result without dragging the whole thread context across.

3. **Escalate blocker**
- A lane cannot proceed and Control Panel needs to route or summarize the blocker.

4. **Clarify ownership**
- Work needs a next owner or session lane assignment.

5. **Transfer next step**
- Control Panel wants to move execution out to a lane after framing the issue.

## Trigger conditions
Use this skill when all of the following are true:
- Control Panel is the coordinating context
- another same-runtime Lyra lane/session should act
- the work is bounded enough to describe clearly
- a lightweight handoff is better than keeping the whole workflow central

Do **not** use when:
- the work is purely local to Control Panel
- the target boundary is cross-runtime or cross-domain and needs stronger controls
- the issue is still too ambiguous to hand off cleanly

## Inputs
Required:
- `target_lane_or_session`
- `purpose`
- `requested_action`
- `context_refs`
- `expected_reply`

Optional but recommended:
- `due_or_timing`
- `priority_class`
- `durable_update_required`
- `update_target`
- `standardization_scope` (mainly during protocol/pattern evaluation)

## Output contract
The skill should produce:
1. a compact handoff packet
2. a recommendation about whether durable write-back is required
3. a recommended artifact target for write-back when applicable
4. a concise Control Panel follow-up summary template for use after the result returns

## Handoff packet format
Default packet should follow `INTRA_LYRA_HANDOFF_PROTOCOL_V1.md`.

Canonical shape:
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

## Decision logic
The skill should apply the following logic:

### Step 1 — Decide whether a handoff is needed
Questions:
- is another lane actually the right execution owner?
- is the issue bounded enough to hand off?
- is the request better handled directly by Control Panel instead?

If no clean handoff is possible, the skill should say so.

### Step 2 — Decide whether durable write-back is required
Write-back is required when:
- ownership changes
- the request spans more than one step
- a blocker/decision/constraint is involved
- the context would otherwise be lost after delay or compaction

### Step 3 — Choose the best write-back target
Preference order:
1. `jobs/<JOB-ID>/STATE.md`
2. `jobs/<JOB-ID>/HANDOVER.md`
3. product `PLAN.md` / `DECISIONS.md` / relevant artifact
4. evidence note (when the coordination itself is significant/auditable)

### Step 4 — Keep the request bounded
The skill should resist creating broad work from vague prompts.
It should push toward:
- one next action
- one decision needed
- one blocker to resolve
- one bounded status ask

## Recommended user-facing behavior
If invoked in a live workflow, the skill should help Control Panel produce messaging that is:
- short
- action-oriented
- artifact-linked
- low-theater
- explicit about expected reply form

## Escalation conditions
The skill should recommend escalation rather than handoff when:
- ownership is materially ambiguous
- the issue crosses runtime/domain boundaries
- the request implies policy/architecture/authority change
- no adequate artifact target exists for continuity
- the target lane lacks enough context to proceed safely even with refs

## Evidence/output expectations
A coordination event should produce at least one of:
- durable job state update
- product artifact update
- evidence note
- concise Control Panel summary of high-signal outcome

The skill should not encourage storing full execution detail in Control Panel artifacts unless oversight genuinely needs it.

## Human-vs-skill boundary
The skill should do:
- packet shaping
- continuity target recommendation
- bounded handoff framing
- escalation detection

Control Panel human/judgment layer should still do:
- priority judgment
- portfolio trade-off judgment
- major cross-product decisions
- ambiguous strategic framing

## First implementation form
Recommended first implementation form:
- **Skill**, not plugin
- small and narrow
- centered on packet generation + continuity guidance + output shaping

Not recommended yet:
- plugin-based orchestration engine
- heavy automation around lane selection
- broad stateful coordination substrate

## Acceptance criteria for implementation
The first implemented version is good enough if:
1. it reliably produces a clean bounded handoff packet
2. it consistently recommends the right continuity target in common cases
3. it reduces ad hoc/manual coordination friction
4. it does not overstep into strategic decision-making
5. it remains small enough to be used often without heavy context cost

## Suggested next implementation step
Use this spec as the basis for the first actual skill package draft.
The implementation should likely include:
- a concise SKILL.md
- possibly a small reference file with packet examples and target-selection heuristics
- no script unless repeated formatting logic proves worth automating

## Version
- v1.0
- Date: 2026-03-10
