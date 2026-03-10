# SKILL_CONCEPTS_FIRST_WAVE_V1.md

Status: Active draft v1  
Owner: Lyra via Control Panel  
Date: 2026-03-10

## Purpose
Define the first-wave skill concepts to implement from the product runtime embodiment plan.

This document stays at concept/spec level.
It is intended to make implementation clean, bounded, and low-drift before any actual skill-packaging work begins.

## First-wave skills
1. Control Panel coordination skill
2. Task Management / TDE operator skill
3. Governance VERIFY-cycle skill

---

## 1. Control Panel coordination skill

### Purpose
Help Control Panel coordinate cross-lane work consistently using the standardized same-runtime intra-Lyra handoff protocol.

### Primary use cases
- hand off work from Control Panel to a product lane
- clarify ownership or next actor
- escalate a blocker
- request bounded status/result without copy-paste
- summarize only high-signal outcome back into oversight artifacts

### Trigger
- direct invocation by Control Panel
- cross-lane issue detected
- ownership ambiguity
- need for durable handoff rather than ad hoc message

### Required inputs
- target lane/session
- requested action
- timing/urgency
- context refs
- whether durable update is required
- expected reply form

### Core procedure
1. Determine whether handoff is actually needed.
2. Build compact handoff packet.
3. Route via `sessions_send` where appropriate.
4. Ensure durable artifact target is explicit when required.
5. Capture only high-signal outcome in Control Panel artifacts.

### Outputs
- structured handoff message
- linked artifact refs
- optional oversight summary/update

### Evidence/output artifacts
- job `STATE.md` / `HANDOVER.md` where relevant
- evidence note only when the handoff itself is significant/auditable
- Control Panel improvement/decision/task artifacts when needed

### Escalation conditions
- multiple lanes appear to own the issue
- handoff would cross runtime/domain boundary
- authority/risk implications exceed normal lane scope
- no suitable durable target is available

### Boundaries / non-goals
- does not replace product execution
- does not replace canonical TDE contracts
- does not create broad project plans from small requests

### First implementation note
This should likely be the first implemented skill because the operating pattern is already validated.

---

## 2. Task Management / TDE operator skill

### Purpose
Provide a consistent operating procedure for bounded Task Management / TDE work that depends on explicit state, task/job continuity, and evidence-backed output.

### Primary use cases
- assess a bounded Task Management request
- set up or update a job bundle for active work
- perform a TDE-aligned operational review
- recommend the next smallest viable action in Task Management scope
- update durable state and evidence without relying on thread history

### Trigger
- direct request in Task Management lane
- Control Panel handoff
- future cron loop for anti-stall / queue hygiene / TDE alignment

### Required inputs
- task/job/product scope
- artifact refs
- expected result type
- state/evidence target
- constraints (e.g. no broad redesign)

### Core procedure
1. Read the referenced Task Management/TDE artifacts.
2. Identify the smallest bounded action or decision.
3. Update job/product state in the same work cycle.
4. Return concise result / status / blocker / decision-needed.
5. Link evidence where appropriate.

### Outputs
- bounded recommendation or action result
- same-cycle state update
- evidence reference when meaningful

### Evidence/output artifacts
- `jobs/<JOB-ID>/STATE.md`
- `jobs/<JOB-ID>/HANDOVER.md` if ownership changes
- product `PLAN.md` / `DECISIONS.md` / evidence note where needed

### Escalation conditions
- TDE kernel contract impact
- deployment/cutover judgment required
- cross-product interface conflict
- missing canonical state/evidence path

### Boundaries / non-goals
- does not silently alter TDE kernel contracts
- does not become a generic product-owner brain
- does not replace DB-canonical task state with chat-layer state

### First implementation note
This skill should be designed with explicit awareness that TDE is DB-canonical and artifact/evidence-heavy.

---

## 3. Governance VERIFY-cycle skill

### Purpose
Run one bounded Governance VERIFY cycle consistently, with clear evidence output and minimal interpretation drift.

### Primary use cases
- verify one governance artifact/process/claim
- complete one bounded VERIFY cycle
- package evidence and state outcome cleanly
- identify whether the result is pass / issue / decision-needed

### Trigger
- direct request in Governance lane
- Control Panel handoff
- future scheduled governance review loop

### Required inputs
- governance target/artifact
- verification objective
- evidence path
- output expectation
- boundary/risk notes

### Core procedure
1. Identify the exact verification target and scope.
2. Read only the necessary artifacts.
3. Execute one bounded VERIFY cycle.
4. Record evidence/result in a deterministic place.
5. Return concise pass/issue/blocker/decision-needed summary.

### Outputs
- VERIFY result summary
- evidence reference
- governance artifact update if required

### Evidence/output artifacts
- governance evidence note
- relevant `PLAN.md` / `DECISIONS.md` / `IMPROVEMENT_LOG.md` updates if triggered
- job state update if the work is job-shaped

### Escalation conditions
- authority/risk issue discovered
- policy ambiguity blocks verification
- result implies a material standards/boundary decision

### Boundaries / non-goals
- does not rewrite policy broadly during a bounded VERIFY cycle
- does not automate governance judgment where explicit human approval is required
- does not turn all governance work into a cron-only loop

### First implementation note
This is probably the safest skill to operationalize after Control Panel coordination because the cycle is bounded and evidence-oriented.

---

## Shared implementation rules for the first wave
- keep each skill narrow and bounded
- require explicit input refs where continuity matters
- prefer evidence/output artifacts over verbose narrative output
- make escalation conditions explicit
- do not let skills bypass product/system-of-record rules
- skill output should reduce ambiguity, not create more prose

## Recommended implementation order
1. Control Panel coordination skill
2. Governance VERIFY-cycle skill
3. Task Management / TDE operator skill

Reason:
- Control Panel coordination has the clearest validated pattern
- Governance VERIFY is bounded and low-risk
- Task Management / TDE has the highest leverage but touches the heaviest underlying substrate

## Version
- v1.0
- Date: 2026-03-10
