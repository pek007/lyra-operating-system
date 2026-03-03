# INC-2026-003 Investigation — OpenClaw availability regression (sandbox/Docker)

Date: 2026-03-03
Owner: Lyra
Status: Initial investigation complete

## 1) Executive summary

OpenClaw instability today was **real** and primarily caused by a configuration/runtime mismatch:

- `agents.defaults.sandbox.mode` was switched into sandbox-requiring modes (`all` and later `non-main`) while Docker was not installed/available in PATH.
- The gateway then produced repeated embedded-agent failures:
  - `Sandbox mode requires Docker, but the "docker" command was not found in PATH...`
- In parallel, autonomous cron jobs (notably the 10-minute continuous sprint loop and Trello sync) repeatedly executed under incompatible runtime assumptions, producing persistent failures, retries, and backoffs.
- Multiple config overwrites and gateway restarts occurred during mitigation, extending the disturbance window.

Bottom line: this was **not a single bug in TDE code**. It was a **change-control + environment preflight failure** amplified by autonomous jobs.

## 2) Evidence and timeline (from `openclaw logs`)

### Key failure signals

- 14:10:34 CET: first hard failure observed:
  - `lane task error ... Sandbox mode requires Docker... command was not found in PATH`
- 14:54:51, 15:00:00, 15:54:51, 16:00:00 CET: recurring cron lane failures with same Docker/sandbox error.
- 17:00 onward: sandboxed/isolated execution path issues:
  - missing files in sandbox (`Sandbox FS error (ENOENT)` for memory and workspace targets)
  - write failures due to read-only paths (`Sandbox path is read-only`)
  - missing runtime tools inside execution environment (`git: not found`, `python3: not found`, `openclaw: not found`, script not found)

### Config churn observed

Repeated config writes changed sandbox mode multiple times during active operations:

- 14:13:16 — updated `agents.defaults.sandbox.mode`
- 14:50:21 — updated `agents.defaults.sandbox.mode`
- 16:52:43 — updated `agents.defaults.sandbox.mode`
- 16:55:27 — updated `agents.defaults.sandbox`
- 19:31:54 — updated `agents.defaults.sandbox.mode`

Gateway restarts followed several changes (e.g., 14:13, 14:50, 16:52, 17:05, 19:32), causing additional service interruption.

### Current snapshot of relevant config backups

From `/Users/lyra/.openclaw/openclaw.json*` inspection:

- current: `sandbox.mode = off`
- `.bak` (latest prior): `sandbox.mode = non-main`
- `.bak.2` and `.bak.4`: `sandbox.mode = all`
- `.bak.1` and `.bak.3`: `sandbox.mode = off`

This confirms oscillation between modes during incident handling.

## 3) Was TDE development the root cause?

**Partially, but not exclusively.**

What we can say with confidence:

- TDE-related/automation activity increased pressure (continuous sprint loop attempted operations not compatible with the sandboxed environment and path model).
- However, the trigger condition for broad failures was the **platform-level sandbox mode change without Docker preflight validation**.

So the true root cause is at the **runtime governance layer**, not just one development stream.

## 4) Root cause analysis (5-Whys)

1. Why did tasks fail repeatedly?
   - Because sandbox-required execution paths were activated on a host without Docker.
2. Why was sandbox mode activated anyway?
   - Config was changed without a hard dependency gate (Docker presence check).
3. Why did impact spread across operations?
   - Autonomous cron jobs continued running and retried under incompatible assumptions.
4. Why did mitigation take longer?
   - Multiple config toggles/restarts happened while active jobs were in flight; mode was not stabilized quickly with a runbooked rollback.
5. Why was this possible?
   - Missing change-control guardrails for high-risk runtime switches (sandbox mode), and no preflight/canary process bound to that switch.

## 5) Lessons learned (non-negotiable)

1. **No sandbox mode change without dependency preflight.**
   - If Docker is absent, sandbox mode must be blocked automatically.
2. **Runtime mode flips are production changes.**
   - Treat like a release: pre-checks, maintenance window, rollback command prepared.
3. **Autonomous cron jobs amplify incidents.**
   - Pause high-autonomy jobs before risky runtime config changes.
4. **One authority for critical config.**
   - Prevent mode thrash by requiring a single change flow and explicit confirmation.
5. **Canary before global.**
   - Verify one isolated test lane first; only then propagate to defaults.

## 6) Preventive controls to implement now

## P0 (today/tomorrow)

- Add a preflight script/gate for sandbox mode changes:
  - checks `docker` availability when mode != `off`
  - fails closed with explicit remediation text
- Add emergency stabilization runbook:
  - stop/pause selected cron jobs
  - restore known-good mode
  - restart gateway
  - verify channel + cron health
- Add incident flag in operations checklist: no repeated toggles without post-change verification.

## P1 (this week)

- Add "runtime compatibility matrix" for autonomous jobs:
  - which jobs are valid in `off`, `non-main`, `all`
  - filesystem assumptions and required binaries
- Add canary job for new sandbox mode (single low-risk check job).
- Add alerting rule:
  - if same lane emits sandbox/dependency errors > N times in 15 minutes => auto-pause affected cron jobs and page operator.

## P2 (next sprint)

- Add policy-as-code enforcement for high-risk config fields (`agents.defaults.sandbox.*`).
- Add regression tests for cron jobs in each allowed sandbox mode.
- Add “safe mode” command profile for recovery that disables high-risk autonomous loops quickly.

## 7) What to keep vs change

Keep:
- Ambition to use stronger sandboxing in shared contexts.

Change:
- Never enable sandboxing as default without host dependency readiness.
- Never roll runtime mode changes while autonomous loops are fully active.

## 8) Final verdict

This incident was preventable.

Primary cause: **control-plane gap** (configuration change allowed without environment preflight).
Secondary amplifiers: **autonomous cron loops + repeated mode toggles/restarts**.

If we implement the P0 controls above, this exact class of failure should not recur.
