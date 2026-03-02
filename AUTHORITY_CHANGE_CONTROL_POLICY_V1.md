# AUTHORITY_CHANGE_CONTROL_POLICY_V1.md

Status: Active (v1)  
Owner: Peter (A), Lyra (R)

## Purpose
Prevent privilege escalation and unsafe drift when job authorities are created or changed.

## Principles
1. Authority is job-bound, inherited via active binding.
2. Effective authority is constrained by agent envelope and process gates.
3. No self-escalation approvals.
4. High-impact authority changes require dual control and rollback readiness.

## Authority ceiling
A change is **ceiling-impacting** if it adds or relaxes any of the following rights:
- Credential/access boundary mutation
- OpenClaw routing/tool-policy override rights
- External side-effect execution without prior obligations
- Production deploy/release bypass rights
- Break-glass expansion (scope/duration/triggers)

Ceiling-impacting changes are Class C and cannot be auto-approved.

## Anti-self-escalation rule
A principal (agent/job holder) cannot approve an authority change that would increase its own effective authority directly or indirectly.

## Required evidence per authority change
- Before/after authority matrix snapshot
- Risk class and rationale
- Affected jobs and bindings
- Approval chain
- Rollback plan (mandatory for Class C)

## Enforcement mapping
- Process owner: `JOBS_PROCESS_V1.md`
- Runtime enforcement: policy decision check + obligation gate + audit linkage
- Transfer semantics: `knowledge/distilled/2026-03-02__spec__job-binding-and-authority-transfer-v1.md`

## Exceptions
Emergency temporary grants allowed only under break-glass protocol with explicit expiry and post-incident review.
