# TDE Mutation Authority Matrix v2 (Job-Bound)

Status: Draft-for-approval  
Date: 2026-03-02

## Why v2
v1 mixed execution principals and role concepts (for example, `Worker Agents` and `Control Tower`) and did not cleanly separate **agent identity** from **job authority**.

v2 defines authority as a **job-bound policy** inherited by whichever agent currently holds the job binding.

## Glossary
- **Agent**: execution principal (session/runtime/sub-agent) that performs actions.
- **Job**: role contract defining decision rights, obligations, and escalation rules.
- **Job binding**: active assignment of a job to an agent for a bounded period.
- **Effective authority**: permission result after combining all guards.

## Effective authority rule
`effective_authority = base_agent_envelope ∩ active_job_policy ∩ process_gate_conditions`

Interpretation:
- A job can allow an action, but tool sandbox/policy can still deny it.
- Process gates (approvals, evidence freshness, DoR/DoD, risk class) are mandatory checks.

## Decision classes
- **Low**: reversible, internal, bounded side effects.
- **Medium**: constrained external/operational side effects.
- **High/Critical**: boundary-changing, irreversible, or high-impact side effects.

## Authority matrix (v2)

### Decision owner (human)
- **Peter** is the final authority for high/critical decisions and boundary changes unless explicit delegation is documented.

### Job policies

#### JOB-CTL-001 — Head of Control Tower
- Read/query/summarize: **allow**
- Create/triage tasks: **allow**
- Low-risk task transitions: **allow (policy-checked)**
- Medium-risk operational transitions: **allow-with-obligations**
- Approve low-risk internal decision packets: **allow**
- External send/publish: **allow-with-obligations**
- OpenClaw config/routing/tool-policy changes: **propose-only**
- Credential/access boundary changes: **deny**
- Merge/release/deploy prod-affecting changes: **propose-only**
- Emergency actions: **allow-with-obligations** (only via break-glass protocol)

#### JOB-ARC-001 — Chief Architect
- Read/query/summarize: **allow**
- Create/triage architecture tasks: **allow**
- Low-risk task transitions: **allow (policy-checked)**
- Approve architecture decision packets/ADRs: **allow**
- OpenClaw config/routing/tool-policy changes: **allow-with-obligations**
- Credential/access boundary changes: **propose-only**
- Merge/release/deploy prod-affecting changes: **propose-only**
- External send/publish: **propose-only**
- Emergency actions: **propose-only**

#### JOB-ENG-001 — Software Developer
- Read/query/summarize: **allow**
- Create/triage implementation tasks: **allow**
- Low-risk task transitions: **allow (policy-checked)**
- Code/test/build in approved repos: **allow**
- Merge/release/deploy prod-affecting changes: **allow-with-obligations** (pre-approved runbook + checks)
- OpenClaw config/routing/tool-policy changes: **propose-only**
- Credential/access boundary changes: **deny**
- External send/publish: **deny unless explicit approval obligation is satisfied**
- Emergency actions: **deny**

#### JOB-SEC-001 — Head of Security
- Read/query/summarize: **allow**
- Create/triage security tasks/incidents: **allow**
- Security policy/control updates (non-boundary): **allow-with-obligations**
- OpenClaw config hardening changes: **allow-with-obligations**
- Credential/access boundary changes: **allow-with-obligations**
- External send/publish: **propose-only**
- Merge/release/deploy prod-affecting changes: **propose-only**
- Emergency actions (security incidents): **allow-with-obligations**

#### JOB-AUD-001 — Auditor
- Read/query/summarize: **allow**
- Create audit findings/tasks: **allow**
- Any state mutation outside audit records: **propose-only**
- OpenClaw config/routing/tool-policy changes: **propose-only**
- Credential/access boundary changes: **deny**
- External send/publish: **deny**
- Merge/release/deploy prod-affecting changes: **deny**
- Emergency actions: **deny**

## Enforcement obligations
- Every mutate/execute action must include:
  1. policy decision record id,
  2. idempotency key,
  3. actor (agent id) + active job id,
  4. expected version / concurrency guard where relevant.
- `allow-with-obligations` blocks execution until obligations are satisfied.
- High/Critical actions require explicit approval artifact linked to audit trail.

## Supersession
Supersedes:
- `knowledge/distilled/2026-03-01__matrix__tde-mutation-authority-v1.md`
