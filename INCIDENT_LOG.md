# INCIDENT_LOG.md

## Purpose
Chronological record of incidents, response, and learnings.

## Template
- Incident ID:
- Date/Time:
- Severity:
- Incident Tags: (choose one or more: `trust_boundary`, `security_access`, `data_integrity`, `availability`, `channel_integration`, `automation_regression`, `other`)
- Summary:
- Impact:
- Detected by:
- Containment actions:
- Recovery actions:
- Root cause:
- Preventive actions:
- Owner:
- Status:

---

## Entries

### INC-2026-001
- Incident ID: INC-2026-001
- Date/Time: 2026-02-23
- Severity: SEV-2
- Incident Tags: channel_integration
- Summary: Telegram channel integration failures (404 errors)
- Impact: Messaging instability / inability to interact reliably
- Detected by: Status/doctor checks and channel logs
- Containment actions: Token rotation, channel reconfiguration, pairing approval
- Recovery actions: Gateway restart, channel health verification
- Root cause: Invalid/incorrect token state and pending pairing state
- Preventive actions: Token hygiene protocol and incident runbook formalization
- Owner: Lyra
- Status: Resolved

### INC-2026-002
- Incident ID: INC-2026-002
- Date/Time: 2026-03-03 05:34 CET
- Severity: SEV-4
- Incident Tags: data_integrity, automation_regression
- Summary: Unintended overwrite of `memory/2026-03-03.md` while attempting to append a new autonomous sprint checkpoint.
- Impact: Partial loss of same-day continuity notes in the daily memory file.
- Detected by: Immediate post-write verification during sprint loop.
- Containment actions: Stopped further writes and reconstructed visible checkpoints from session artifacts.
- Recovery actions: Rebuilt `memory/2026-03-03.md` with recovered checkpoints and explicit loss note.
- Root cause: Used overwrite write-path instead of append/edit operation for memory update.
- Preventive actions: Use `read` + `edit` append pattern for existing memory files; avoid raw `write` unless creating a new file.
- Owner: Lyra
- Status: Mitigated

### INC-2026-003
- Incident ID: INC-2026-003
- Date/Time: 2026-03-03 14:10-19:32 CET
- Severity: SEV-2
- Incident Tags: availability, automation_regression
- Summary: OpenClaw availability degraded by repeated sandbox-mode changes requiring Docker on a host without Docker, combined with autonomous cron workloads that were incompatible with isolated/sandboxed runtime assumptions.
- Impact: Repeated embedded-agent failures, cron task failures/backoff, multiple gateway restarts, and unstable operations during the incident window.
- Detected by: Gateway logs (`openclaw logs`) and failed task telemetry in cron state.
- Containment actions: Toggled sandbox mode multiple times (`off` <-> `all` <-> `non-main`) and restarted gateway as immediate mitigation.
- Recovery actions: Returned runtime to stable mode (`agents.defaults.sandbox.mode=off` as of 19:31/19:32 restart), restored service continuity.
- Root cause: Configuration drift + missing dependency gate. Sandbox was enabled on a machine lacking Docker; isolated cron workloads and path assumptions then failed repeatedly. No preflight dependency check blocked the change.
- Preventive actions: Add preflight config/dependency guardrails, staged rollout for sandbox mode, canary job before global toggle, and per-workload runtime compatibility matrix.
- Owner: Lyra
- Status: Monitoring
