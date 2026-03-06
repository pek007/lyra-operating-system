---
id: OPP-2026-001
title: "Drift Aftercare Standard (7-day post-change checkpoint)"
status: ready
created: 2026-03-03
owner_job: JOB-CI-001
owner_actor: "agent=main"
risk_class: low
related_signals:
  - IMP-AUTO-20260303-03
related_tasks:
  - OPS-2026-046
related_evidence:
  - "knowledge/reports/WEEKLY_SYNTHESIS__2026-03-03.md"
---

# Opportunity Packet: Drift Aftercare Standard

## Hypothesis
If we enforce a 7-day post-change drift checkpoint for structural/governance changes, then residual schema/process drift will drop because unresolved edge cases are surfaced and converted to execution before they age.

## Mechanism
- Friction origin: major harmonization efforts close, but residual legacy rows/edge cases remain.
- Recurrence driver: no mandatory aftercare checkpoint, so residuals compete with new work.
- Feedback loops / delays: delay in detection increases context loss and repair cost.
- Second-order effects: lower trust in governance artifacts if residual mismatch persists.

## Pilot design (1 week, reversible)
### Change to test
- Add a temporary “aftercare required” rule for one active drift item (`IMP-AUTO-20260303-03`).
- Require one checkpoint artifact within 7 days documenting residuals, decisions, and actions.

### Safety and reversibility
- Rollback plan: remove the temporary rule and close pilot with reject rationale.
- Blast radius: documentation + task handling only.
- Guardrails: no security boundary, credential, integration, or runtime permission changes.

### Instrumentation
- Baseline window: current open drift debt as of 2026-03-03.
- Data sources: `TASKS.md`, checkpoint artifact, and linked evidence files.
- Metric calculation: did residual drift item get decomposed/executed with explicit next steps within 7 days (Y/N).

## Success and failure signals
### Leading indicators (1–7 days)
- Checkpoint artifact created on time.
- Residual drift converted into explicit executable tasks.

### Lagging indicators (2–6 weeks)
- Fewer recurring schema/process drift items after major changes.

### Stop conditions (abort)
- Pilot creates process overhead without converting any residual to executable action.

## Risks and assumptions
- Assumption: residual drift is primarily caused by missing aftercare, not capability limits.
- Risk -> mitigation: excess admin overhead -> keep checkpoint to one page with strict template.

## Decision request
- Approver(s): Peter (lightweight go/no-go)
- Decision needed by: 2026-03-04
- Default action if no response: run pilot for one week, low-risk documentation scope only.

## Conversion to execution
### Work orders
- WO-CI-2026-001 | Drift Aftercare pilot execution (1 week)

### Next actions
- [x] OPS-2026-047 | Executed Drift Aftercare pilot for `IMP-AUTO-20260303-03` and published checkpoint evidence (`knowledge/evidence/2026-03-06__ops-2026-047-drift-aftercare-pilot-closeout.md`).
