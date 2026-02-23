# WAYS_OF_WORKING_V1.md

## Purpose
Build a practical Operating System (OS) for Lyra + Peter that is lightweight, secure, and scalable for PX Strategy.

## Design Goals
- Enterprise-grade clarity, startup-grade overhead
- Safe and stable by default
- Incremental improvement with measurable outcomes
- Documented decisions and repeatable execution

## Scope (v1)
This v1 focuses on foundations only:
1. Work management system
2. Knowledge/document system
3. Security and resilience baseline
4. Operating cadence and metrics
5. Core governance artifacts

---

## Target Operating Model (what “done” looks like)

### A) Single system of record for work
All requests, tasks, and improvement items are tracked in one place with status, owner, and due date.

### B) Single system of record for knowledge
Policies, runbooks, templates, and decisions are stored in one canonical location with versioning.

### C) Minimum security baseline
MFA, encryption, access hygiene, backups + tested restore, incident mini-runbook, retention baseline.

### D) Operating cadence
- Daily: triage and prioritization
- Weekly: planning + metrics review
- Monthly: retrospective + improvement backlog commit
- Quarterly: risk/control review

### E) Metrics baseline
Track a small KPI set:
- Throughput (tasks completed/week)
- Cycle time (start -> done)
- WIP (work in progress)
- Overdue tasks
- Incident count/time to recovery (even if zero)

---

## 2-Week Implementation Plan

## Week 1 — Foundations

### 1) Select systems of record (Day 1)
**Decision needed:**
- Work system: choose one tool
- Knowledge system: choose one tool

**Output:** ADR-001 (architecture decision record) with rationale and trade-offs.

### 2) Create workflow standard (Day 1–2)
Define canonical statuses:
- Inbox
- Triage
- Active
- Waiting
- Done
- Archived

Define priority classes:
- P1 critical
- P2 important
- P3 normal
- P4 nice-to-have

**Output:** SOP-001 Intake & Triage.

### 3) Definition of Done (Day 2)
A task is “Done” only if:
- Deliverable produced
- Key assumptions documented
- Next step identified or explicitly closed
- Stored in correct folder/system

**Output:** STD-001 Definition of Done.

### 4) Decision logging (Day 3)
Create decision log template and start using it.

**Output:** TEMPLATE-001 Decision Record + DECISIONS.md.

### 5) Security quick baseline (Day 3–4)
- Confirm MFA on critical accounts
- Confirm disk encryption status
- Confirm account/access hygiene

**Output:** SEC-001 Baseline Checklist (v1).

### 6) Backup + restore test (Day 4–5)
- Confirm backups are running
- Perform one restore test
- Record RTO and RPO targets

**Output:** OPS-001 Backup & Restore Runbook + test result note.

## Week 2 — Control and Cadence

### 7) Incident mini-runbook (Day 6–7)
Define what to do for:
- Tool outage
- Credential leak suspicion
- Data loss event

**Output:** IR-001 Incident Mini-Runbook.

### 8) Retention and access baseline (Day 7–8)
Define:
- What to retain
- Where to retain
- For how long
- Who can access

**Output:** GOV-001 Retention & Access Baseline.

### 9) Start cadence (Day 8–10)
Pilot:
- Daily 10-minute triage
- Weekly 45-minute planning + metrics

**Output:** recurring calendar/cadence entries + first weekly report.

### 10) Metrics dashboard-lite (Day 10)
Create a simple weekly dashboard file.

**Output:** METRICS_WEEKLY.md (template + first entry).

---

## Artifact Map (v1)
- `WAYS_OF_WORKING_V1.md` (this plan)
- `DECISIONS.md`
- `SOP-001_INTAKE_TRIAGE.md`
- `STD-001_DEFINITION_OF_DONE.md`
- `SEC-001_BASELINE_CHECKLIST.md`
- `OPS-001_BACKUP_RESTORE_RUNBOOK.md`
- `IR-001_INCIDENT_MINI_RUNBOOK.md`
- `GOV-001_RETENTION_ACCESS_BASELINE.md`
- `METRICS_WEEKLY.md`

---

## Risks and Mitigations
- **Risk:** Over-engineering too early
  - **Mitigation:** Keep v1 minimal and actionable; defer advanced controls.
- **Risk:** Process not adopted consistently
  - **Mitigation:** Daily/weekly cadence + definition of done + visible metrics.
- **Risk:** Security controls are assumed, not tested
  - **Mitigation:** Explicit checklist and restore test evidence.

---

## Decision Gates
At end of Week 2, decide:
1. Keep v1 as-is / refine / expand
2. Which controls to mature in v2 (e.g., vendor checklist, secure SDLC)
3. Whether to begin PX Strategy full operating framework build

---

## Ownership
- Accountable: Peter
- Responsible (drafting, tracking, maintenance): Lyra

## Version
- v1.0
- Date: 2026-02-23
