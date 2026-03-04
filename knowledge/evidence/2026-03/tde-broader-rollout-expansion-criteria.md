# TDE Canary→Broader Rollout Bounded Expansion Criteria

Generated: 2026-03-02T18:36:16.807795+00:00

- Expansion bound: max scope from 3 to 8 high-priority local tasks per cycle.
- Scope restriction: local-only task set (no 3PP, no new repo, fail-closed policy preserved).
- Preconditions: at least 3 consecutive clean canary cycles; guardrail status must be `ok`; no approval-gate bypass violations.
- Health thresholds during broadened cycle: stalled count <= 1 and stalled ratio <= 25%.
- Rollback triggers: any guardrail alert, any approval-gate bypass, or stalled count threshold breach.

```json
{
  "expansionWindow": {
    "fromMaxItems": 3,
    "toMaxItems": 8
  },
  "scopeRule": "expand high-priority local tasks only; no 3PP integrations",
  "requiredPreconditions": {
    "consecutiveCleanCyclesMin": 3,
    "guardrailStatus": "ok",
    "approvalGateBypass": "forbidden"
  },
  "cycleHealthThresholds": {
    "maxStalledCount": 1,
    "maxStalledRatio": 0.25
  },
  "rollbackTriggers": [
    "guardrail.status == alert",
    "approval_gate_bypass detected",
    "stalled_count > 1 in broadened cycle"
  ]
}
```
