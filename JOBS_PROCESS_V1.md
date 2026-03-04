# JOBS_PROCESS_V1.md

Status: Active (v1)  
Owner: Lyra (R), Peter (A)

## Purpose
Govern the lifecycle of jobs as first-class operating objects, including safe authority evolution.

## Scope
- Job creation, refinement, reassignment, retirement
- Job-to-agent bindings
- Authority-impacting changes to job policies

## Flow
Propose -> Classify change -> Authority diff check -> Approval gate -> Activate -> Audit log -> Review

## Change classes
1. **Class A (Descriptive):** naming/scope text, no authority delta
2. **Class B (Authority-impacting):** permissions, obligations, escalation paths, risk classes
3. **Class C (Boundary/Ceiling):** authority ceiling changes, credential/boundary rights, break-glass semantics

## Mandatory controls
- No actor may approve a change that increases its own effective authority.
- Any Class B/C change must include a machine-readable authority diff.
- Activation blocked until required approvals are linked.
- All activations must emit audit records with before/after snapshots.

## Approval gates
- Class A: job owner + reviewer
- Class B: job owner + **JOB-OWN-001** approval
- Class C: **JOB-OWN-001** + independent second approver (dual control), plus rollback plan

## Product/acceptance governance rule
- Detailed acceptance-test approvals are delegated to domain jobs, not defaulted to **JOB-OWN-001**.
- For TDE thin-slice acceptance tests:
  - **JOB-PROD-001 (Product Owner)** approves product fitness/completeness.
  - **JOB-ARC-001 (Chief Architect)** approves technical/safety integrity.
  - **JOB-OWN-001** is escalation/final arbiter only for unresolved conflicts or high/critical risk exceptions.
- Phase-level delegation to JOB-PROD-001 must be documented in a charter artifact with explicit reserved authorities.

## Binding and transfer integration
Authority follows jobs, not fixed agents.
- Use `knowledge/distilled/2026-03-02__spec__job-binding-and-authority-transfer-v1.md` for transfer protocol.
- Re-evaluate pending obligations after every binding change.

## Artifacts required per change
- Updated job record (`JOB_MARKET_MODEL_V1.md` or successor registry)
- Authority diff record
- Approval artifact(s)
- Activation event + audit link

## Cadence
- Weekly: open job changes + pending authority diffs
- Monthly: authority hygiene review (unused rights, excessive obligations, stale delegations)
