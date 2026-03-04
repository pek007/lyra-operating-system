# TDE Build Gate Approval RACI v1

Status: Draft-for-approval  
Date: 2026-03-02

## Purpose
Define explicit approval accountability for TDE build-gate decisions so governance is clear and escalation is controlled.

## Roles
- **JOB-OWN-001** — System Owner & Final Decision Authority (Peter)
- **JOB-PROD-001** — Product Owner
- **JOB-ARC-001** — Chief Architect
- **JOB-SEC-001** — Head of Security
- **JOB-ENG-001** — Software Developer
- **JOB-AUD-001** — Auditor

## RACI legend
- **R** = Responsible (does the work)
- **A** = Accountable (final sign-off)
- **C** = Consulted
- **I** = Informed

## Build-gate RACI

### 1) Scope and non-goal conformity
- R: JOB-PROD-001
- A: JOB-OWN-001
- C: JOB-ARC-001
- I: JOB-ENG-001, JOB-AUD-001

### 2) Thin-slice acceptance test quality/completeness
- R: JOB-PROD-001
- A: JOB-PROD-001
- C: JOB-ARC-001, JOB-ENG-001
- I: JOB-OWN-001, JOB-AUD-001

### 3) Technical/safety integrity of thin slice
- R: JOB-ARC-001
- A: JOB-ARC-001
- C: JOB-SEC-001, JOB-ENG-001
- I: JOB-OWN-001, JOB-AUD-001

### 4) Mutation authority model coherence (job-bound)
- R: JOB-ARC-001
- A: JOB-OWN-001
- C: JOB-SEC-001, JOB-AUD-001
- I: JOB-PROD-001, JOB-ENG-001

### 5) Job binding/transfer control adequacy
- R: JOB-SEC-001
- A: JOB-OWN-001
- C: JOB-ARC-001, JOB-AUD-001
- I: JOB-PROD-001, JOB-ENG-001

### 6) Security posture and boundary controls for build start
- R: JOB-SEC-001
- A: JOB-OWN-001
- C: JOB-ARC-001
- I: JOB-PROD-001, JOB-ENG-001, JOB-AUD-001

### 7) Build-phase backlog sequencing (WIP-limited)
- R: JOB-PROD-001
- A: JOB-PROD-001
- C: JOB-ARC-001, JOB-ENG-001
- I: JOB-OWN-001, JOB-AUD-001, JOB-SEC-001

### 8) Final go/no-go to start kernel-slice build
- R: JOB-PROD-001 + JOB-ARC-001 (joint recommendation)
- A: JOB-OWN-001
- C: JOB-SEC-001, JOB-AUD-001
- I: JOB-ENG-001

## Escalation rule
If Product Owner and Chief Architect disagree on readiness, the decision escalates to **JOB-OWN-001** with written dissent notes from both roles.

## Control rule
No role may approve a change that increases its own effective authority (per `AUTHORITY_CHANGE_CONTROL_POLICY_V1.md`).
