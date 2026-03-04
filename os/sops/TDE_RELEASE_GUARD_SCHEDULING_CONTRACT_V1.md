# TDE Release Guard Scheduling Contract v1

Date: 2026-03-04
Status: Active

## Purpose
Define deterministic scheduling and output semantics for `tde-release-guard` so release progression can be blocked automatically on hard failures.

## Trigger contract
Accepted trigger source:
- `cron` via `tools/tde_release_guard_cron_hook.sh`

Hook executes:
- `tools/tde-release-guard.sh`

Fail-closed rule:
- Any hard failure in release guard exits non-zero and should block release progression.

## Local scheduling guidance
- During active release windows: every 15 minutes.
- Outside release windows: every 60 minutes (optional).
- Run immediately before any manual broaden-scope release action.

## Stable artifact
Artifact path:
- `knowledge/evidence/2026-03/tde-release-guard-latest.txt`

Artifact contains:
- UTC start/end timestamps
- preflight result
- kernel slice test result
- runtime registry checks
- canary freshness/stall warning state
- final GREEN/RED result

## Escalation semantics
Escalate and freeze release progression when guard is RED due to:
- environment preflight failure
- TDE kernel slice test failure
- missing runtime binding/objective registries

Warnings (e.g., stale canary) do not hard-block by default but require explicit operator acknowledgment before scope broadening.
