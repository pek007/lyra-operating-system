# Job Binding and Authority Transfer Spec v1

Status: Draft-for-approval  
Date: 2026-03-02

## Purpose
Define how authority follows **jobs**, not fixed agent identities, including safe transfer between agents/runtimes.

## Core model
1. Authority is attached to job policy.
2. Agent receives authority only through an active job binding.
3. Removing binding removes inherited job authority immediately.
4. Human decision owner authority remains outside job-binding mechanics.

## Binding object (minimum fields)
- `binding_id`
- `job_id`
- `agent_id`
- `session_or_runtime_id`
- `granted_by`
- `granted_at`
- `expires_at` (required for temporary bindings)
- `scope` (repo/domain/process constraints)
- `status` (`active|revoked|expired`)
- `reason`

## Effective permission check
For each attempted action:
1. Resolve active binding(s) for calling agent.
2. Evaluate job policy for requested action/risk class.
3. Intersect with base agent envelope/tool sandbox constraints.
4. Evaluate process gates/obligations.
5. Return `allow|allow-with-obligations|propose-only|deny` with explanation code.

## Transfer protocol (A -> B)
1. **Prepare**
   - Validate B satisfies required execution profile for job.
   - Snapshot open obligations/approvals for active tasks.
2. **Revoke old binding**
   - Set A binding status to `revoked` with timestamp/reason.
3. **Issue new binding**
   - Create active binding for B with explicit scope and expiry.
4. **Re-evaluate in-flight work**
   - Re-check pending approvals/obligations under new binding.
5. **Audit log**
   - Emit transfer event linking revoke+grant and affected task/decision ids.

## Safety rules
- No dual-active binding for the same exclusive job unless explicitly marked `shared=true`.
- Any high/critical action started before transfer but executed after transfer must be re-authorized against new binding.
- Break-glass grants must be time-bounded and auto-expire.

## Failure handling
- If grant succeeds but revoke fails: mark transfer `incomplete`, block high-risk actions, escalate.
- If revoke succeeds but grant fails: job becomes `unassigned`; route to human decision owner.
- If audit write fails: execute no further privileged actions until audit channel recovers.

## Acceptance checks
- Transfer removes A authority immediately (no sticky permissions).
- B can execute only actions permitted by job policy + envelope + process gates.
- Pending obligations are visible and re-validated post-transfer.
- All transfer events are queryable and linked to action audit records.
