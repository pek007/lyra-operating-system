# TDE Canary Runtime Wiring v1

Date: 2026-03-02
Status: Active

## Canary scope
- In-scope set: high-priority items tagged `tde_canary=true`
- Trigger sources: `heartbeat`, `cron`
- Cadence baseline:
  - heartbeat check: on heartbeat cycle
  - cron check: every 30 minutes (canary only)

## Runtime output artifact
Each cycle writes a status artifact to:
`knowledge/evidence/2026-03/tde-canary-status-latest.json`

Required fields:
- cycleTimestamp
- triggerSource
- triggerId
- evaluatedCount
- stalledCount
- routes[] with:
  - targetId
  - stallReasonCode
  - route
  - requiresApproval
  - status

## Guardrails
- `requiresApproval=true` routes must remain `blocked_pending_approval`
- Invalid trigger source -> reject cycle (fail-closed)
- If artifact write fails -> cycle status `degraded`, escalate in next cycle

## Rollout rule
- Keep canary-only until 3 consecutive clean cycles with no guardrail violations.
