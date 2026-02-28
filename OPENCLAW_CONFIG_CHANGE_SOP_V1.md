# SOP: OpenClaw Config Change Control & Rollback v1

Date: 2026-02-28
Owner: Peter/Lyra
Status: Active

## Purpose
Prevent service disruption from live OpenClaw configuration changes by enforcing preview, approval, validation, and rollback steps.

## Scope
Any change to:
- `~/.openclaw/openclaw.json`
- included config fragments
- gateway/channel/tool/sandbox/routing/auth settings

## Change Classes
- **Low risk:** comments/formatting/non-runtime metadata
- **Medium risk:** non-critical defaults (timeouts, cosmetic behavior)
- **High risk:** channel policy, auth, tool policy, sandbox, routing, gateway bind/network exposure

Default: if unsure, classify as **High risk**.

## Mandatory Workflow (no exceptions)

### 1) Propose only (no live change)
Provide:
- exact diff (before -> after)
- risk class
- expected behavior impact
- validation plan
- rollback plan

### 2) Explicit approval
Required for all High-risk changes.
Approval must include a clear "apply now" from Peter.

### 3) Pre-change backup
Create timestamped backup:
- `~/.openclaw/openclaw.json.bak-YYYYMMDD-HHMMSS`

### 4) Apply minimal diff
- only approved lines
- no opportunistic edits

### 5) Validate immediately
Run:
1. `openclaw gateway status`
2. `openclaw status --deep`
3. channel health checks relevant to affected channels
4. confirm expected behavior in target workflow

### 6) Report result
- applied changes summary
- validation results
- any warnings/errors
- next actions (if any)

## Failure / Rollback Procedure
Trigger rollback if any of these occur:
- gateway fails to start/restart cleanly
- channel connectivity regresses
- unexpected policy lockout or behavior regression
- any uncertainty about current live state

Rollback steps:
1. Restore last known-good backup file
2. Restart gateway
3. Re-run validation checks
4. Log incident + root cause + prevention action

## Safe Execution Rules
- Never combine unrelated config changes in one operation
- Never change config and code simultaneously in same recovery window
- Never proceed without a tested rollback path
- Prefer staged changes over large one-shot edits

## Required Artifacts
- Change request record (can be in task/WO)
- diff snapshot
- validation output summary
- rollback confirmation (if rollback used)
- incident entry (if degraded behavior occurred)

## Version
- v1.0
- Date: 2026-02-28
