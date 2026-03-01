# TDE Mutation Authority Matrix v1

Status: Draft-for-approval  
Date: 2026-03-01

## Decision classes
- Low risk / Type 2 reversible
- Medium risk / constrained side effects
- High/Critical risk / Type 1 or boundary-changing

## Authority table (v1)

| Action family | Worker Agents | Control Tower | Peter |
|---|---|---|---|
| Read/query/summarize | Allow | Allow | Allow |
| Create task in inbox/triage | Allow | Allow | Allow |
| Transition task within low-risk lifecycle | Allow (policy-checked) | Allow | Allow |
| Approve/reject low-risk internal decision draft | Propose only | Allow | Allow |
| External send/publish | Deny unless approval obligation satisfied | Allow-with-approval | Allow |
| OpenClaw config/routing/tool-policy changes | Deny | Allow-with-approval | Allow |
| Credential/access boundary changes | Deny | Allow-with-approval | Allow |
| Merge/release/deploy production-affecting changes | Deny unless pre-approved runbook path | Allow-with-approval | Allow |
| Emergency break-glass actions | Deny (unless emergency token + obligations) | Allow-with-obligations | Allow |

## Enforcement notes
- All mutate/execute operations require policy decision record.
- `allow-with-obligations` blocks execution until obligations are satisfied.
- High-risk actions require explicit approval artifact and audit linkage.
