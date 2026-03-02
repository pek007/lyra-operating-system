# TDE Canary Scheduling Contract v1

Date: 2026-03-02
Status: Active

## Purpose
Define deterministic local hook contracts for canary anti-stall cycles triggered by heartbeat or cron, including stable status artifact schema and fail-closed guardrail alerts.

## Trigger contract
Accepted trigger sources:
- `heartbeat` via `tools/tde_canary_heartbeat_hook.sh`
- `cron` via `tools/tde_canary_cron_hook.sh`

Both hooks execute:
- `python3 tools/tde_canary_runtime_cycle.py --trigger-source <heartbeat|cron> --stalled-alert-threshold ${TDE_STALLED_ALERT_THRESHOLD:-1}`

Fail-closed rule:
- Any trigger source other than `heartbeat|cron` is rejected.

## Local scheduling guidance
- Heartbeat: call `tools/tde_canary_heartbeat_hook.sh` once per heartbeat cycle.
- Cron canary baseline: every 30 minutes.
- Threshold tuning: set env var `TDE_STALLED_ALERT_THRESHOLD` in the scheduler context.

## Stable cycle artifact
Artifact path:
- `knowledge/evidence/2026-03/tde-canary-status-latest.json`

Required fields per cycle:
- `cycleTimestamp`
- `triggerSource`
- `triggerId`
- `evaluatedCount`
- `counts.active`
- `counts.atRisk`
- `counts.stalled`
- `stallReasonSummary` (map of reason code -> count)
- `routes[]`
- `guardrail.stalledAlertThreshold`
- `guardrail.thresholdBreached`
- `guardrail.violations[]`
- `guardrail.status` (`ok|alert`)
- `cleanCycle`
- `consecutiveCleanCycles`

State persistence:
- `knowledge/evidence/2026-03/tde-canary-cycle-state.json`

## Guardrail alert condition
Alert when stalled count breaches threshold:
- condition: `counts.stalled > guardrail.stalledAlertThreshold`
- effect: append `stalled_threshold_breached:<actual><threshold>` in `guardrail.violations[]`
- cycle `guardrail.status = alert`

## Clean-cycle rollout gate
Canary may be considered stable when 3 consecutive clean cycles are observed:
- clean cycle = no guardrail violations
- tracked by `consecutiveCleanCycles`
- simulation helper: `python3 tools/tde_canary_simulate_three_clean_cycles.py`
