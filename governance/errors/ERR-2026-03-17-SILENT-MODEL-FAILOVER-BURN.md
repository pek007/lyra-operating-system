# Error Report

## Header
- Error ID: ERR-2026-03-17-SILENT-MODEL-FAILOVER-BURN
- Date: 2026-03-17
- Title: Silent fallback from Codex to Claude Sonnet continued for ~2 days without alert, causing material credit burn
- Type: incident
- Scope: system_level
- Owning product or owner: Lyra OS / runtime controls
- Affected products/contexts: main runtime, cron sessions, Telegram operations, model-cost controls
- Status: mitigated
- Review / closure date: 2026-03-17

## Summary
- The primary model path (`openai-codex/gpt-5.4`) went down about two days ago.
- The runtime continued operating on the backup model (`anthropic/claude-sonnet-4.6`) without surfacing a warning.
- The backup-model usage consumed roughly $100 in credits before the issue became obvious.
- The issue only became fully visible after credits were depleted and service stopped working.
- Peter manually reconnected Codex and removed the fallback option before this report was filed.

## Impact
- Actual impact: material cost burn (~$100), silent degradation of control visibility, temporary service interruption when credits ran out.
- Potential impact: continued hidden spend, incorrect assumptions about active provider/model, reduced trust in unattended runtime behavior.

## Detection
- How was it detected? Peter noticed the service failure after credits were depleted and identified the silent fallback path.
- Detection gap, if any: No alert was raised when the provider/model switched away from Codex. No fail-closed behavior stopped execution after primary-model loss. No cost/spend guard surfaced the abnormal backup usage.

## Root cause
- Primary root cause: The runtime had a live fallback path to Claude Sonnet and allowed continued operation after Codex failure without explicit user-facing alerting.
- Contributing factors:
  - No provider-switch alert.
  - No fail-closed rule for production use when the primary model became unavailable.
  - No lightweight recurring monitor for backup-model activation in recent sessions.
  - No cost guard tied to backup-model usage.

## Immediate mitigation
- Peter manually reconnected Codex.
- Peter removed the fallback option.
- Current config now shows both `main` and `px-internal-dev` set to `openai-codex/gpt-5.4` with no configured model fallback under `agents.defaults.model`.

## Corrective actions
- [x] File incident report.
- [x] Verify current config is back on Codex-only primary path.
- [x] Add runtime monitor that alerts if backup-model usage appears in recent sessions (`tools/model_fallback_monitor.sh` + cron job `model-fallback-monitor`, every 30 min).
- [x] Add explicit model-provider health / switch visibility to the operating cadence via the recurring monitor alert.
- [ ] Decide whether backup models should be forbidden entirely in production, or only allowed with explicit time-bounded approval.

## Preventive changes
- Backup-model activation should be treated as an alert condition, not a silent continuity feature.
- For production use, primary-model failure should default to fail-closed unless Peter has explicitly approved temporary fallback.
- Daily/recurring health checks should include recent active model/provider verification.

## Linked artifacts
- Related evidence:
  - `openclaw status` on 2026-03-17 showing recent cron sessions on `anthropic/claude-sonnet-4.6`
  - `/Users/lyra/.openclaw/openclaw.json` current config showing Codex restored as primary and no fallback in `agents.defaults.model`
- Related product/shared artifacts:
  - `/Users/lyra/.openclaw/openclaw.json`
  - `governance/errors/ERR-2026-03-17-SILENT-MODEL-FAILOVER-BURN.md`

## Closure criteria
- Backup-model activation monitor is live.
- A clear production rule exists for fallback behavior (forbidden by default, or explicit approval required).
- The control is verified in a future check.

## Closure note
- Incident mitigated by reconnecting Codex and removing fallback.
- Preventive controls are being added now; report remains mitigated until monitor + policy are in place.
