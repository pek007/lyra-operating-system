# A-005 — Incident-to-Improvement Loop

Status: Active v1
Owner: Lyra
Last updated: 2026-03-10

## Purpose
Turn errors, incidents, and meaningful near-misses into a mandatory closed-loop process:
1. stabilize the situation,
2. write the record,
3. decide the prevention action,
4. route the work,
5. verify the prevention,
6. learn at portfolio level.

This sits under A-005 as the canonical product-owned process for converting failure into operational learning.

## Trigger conditions
Run this process when any of the following happens:
- operational incident or outage
- repeated error pattern
- failed release / failed deployment / failed automation run
- security-relevant incident or near-miss
- material manual recovery caused by process or system weakness
- same class of issue occurs more than once

## Mandatory outputs
For every triggered case, create or update all of the following:
- Incident record in `INCIDENT_LOG.md` if the event is an actual incident
- A-005 improvement log entry in `products/A-005/management/IMPROVEMENT_LOG.md`
- Linked execution artifact for the prevention action:
  - task / backlog item
  - decision record if the fix changes policy, architecture, or guardrails
  - evidence note if verification is completed

## Required minimum fields
Every error/improvement record must capture:
- date
- trigger type
- summary of what happened
- impact
- root cause or best current cause hypothesis
- immediate corrective action
- preventive action
- owner
- due / review date
- linked artifacts
- status: open / in-progress / verified / accepted / rejected

## Operating flow
### 1) Stabilize
- Stop the bleed first.
- Recover minimum safe operation before optimization.
- If needed, pause or constrain automations that are amplifying the issue.

### 2) Record
- Write the incident/error report while context is fresh.
- Use `INCIDENT_LOG.md` for incident chronology.
- Add an A-005 improvement log entry for the learning/action thread.

### 3) Classify
Classify the failure source as one or more of:
- process gap
- missing control
- documentation gap
- tooling gap
- automation logic gap
- monitoring / alerting gap
- decision / governance gap
- environment / dependency mismatch
- human execution miss

### 4) Decide the prevention action
Every material incident must produce one explicit outcome:
- prevent via control
- reduce likelihood via process/documentation/tooling change
- reduce blast radius via containment/guardrail
- improve detection via monitoring/alerting
- consciously accept with rationale

"Fix now, prevent later" is not sufficient. The prevention action must be named and owned.

### 5) Route the work
Route the preventive action into the right execution lane:
- small local process/doc/tool fix -> implement directly with evidence
- non-trivial work -> create backlog/task item
- policy/architecture/authority change -> decision record + approval path as needed
- cross-product pattern -> include in weekly A-005 synthesis

## Trigger rules
The following actions are mandatory when conditions are met:
- Repeated issue twice or more -> create a prevention task even if workaround exists
- Security-relevant event -> also follow the relevant security incident/learning path
- Automation-amplified failure -> add containment/guardrail action, not just root-cause fix
- Material customer/user impact -> add verification evidence before closing
- Policy or system-boundary change -> add/update decision record

## Closure criteria
Do not close the loop until all are true:
- incident is stabilized
- written record exists
- preventive action is explicitly defined
- owner and review date exist
- linked execution artifact exists
- verification evidence exists or a time-boxed follow-up review is scheduled

## Portfolio learning
A-005 weekly synthesis must review:
- top recurring failure classes
- repeat incidents with same root-cause family
- overdue prevention actions
- controls added vs verified effectiveness
- candidates for automation of the loop itself

## Autonomous target state
The intended end state is an autonomous self-improvement loop with human-governed guardrails:
- detect failures automatically
- draft structured incident/improvement records automatically
- propose preventive actions automatically
- route work automatically into the correct lane
- verify outcomes automatically where safe
- escalate to Peter only for material, risky, or one-way-door changes

Until that state is proven safe, autonomy remains constrained by the existing guardrails in A-005 and the wider operating system.
