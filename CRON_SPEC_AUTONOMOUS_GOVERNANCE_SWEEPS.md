# CRON_SPEC_AUTONOMOUS_GOVERNANCE_SWEEPS.md

## Objective
Add two autonomous recurring jobs that improve security posture and operating quality **without making Peter a bottleneck**.

Design principle: auto-implement only low-risk, uncontroversial changes; route larger changes into backlog with clear IDs.

---

## Implemented Jobs

### 1) `healthcheck:security-audit`
- **Cron:** `10 2 * * *`
- **Timezone:** `Europe/Stockholm`
- **Session:** `isolated`
- **Delivery:** Telegram announce to Peter (`8283124284`)
- **Intent:** Nightly security/risk detection + safe hardening where deterministic.

**Runbook in prompt**
1. Run baseline checks:
   - `openclaw security audit --deep`
   - `openclaw update status`
   - `openclaw status --deep`
2. Run host read-only posture checks:
   - `lsof -nP -iTCP -sTCP:LISTEN`
   - `/usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate`
   - `pfctl -s info`
3. Auto-fix policy:
   - Allowed: `openclaw security audit --fix` (OpenClaw-local safe defaults only)
   - Forbidden (no auto-change): firewall rules, SSH config, network exposure, package install/remove
4. Reporting format:
   - Fixed now
   - Needs review
   - Backlog candidates (severity/rationale/owner)
5. Backlog behavior:
   - Append larger items to `TASKS.md` Inbox with ID format: `SEC-AUTO-YYYYMMDD-XX`
6. Escalation line:
   - Include: `For remediation workflow, run skill: healthcheck`

---

### 2) `continuous-improvement:sweep`
- **Cron:** `20 3 * * *` (daily)
- **Timezone:** `Europe/Stockholm`
- **Session:** `isolated`
- **Delivery:** Telegram announce to Lyra Operations (`-1003804530741`)
- **Intent:** Systematic marginal improvements in quality, robustness, scalability.

**Runbook in prompt**
1. Sweep for high-signal, low-controversy improvements across docs/code/structure:
   - consistency, clarity, naming, dead links, duplicate guidance, obvious hygiene/refactor items, missing guardrails
2. Perform OpenClaw release-delta check (see `OPENCLAW_RELEASE_DELTA_SOP.md`):
   - detect new versions (`openclaw update status`)
   - identify meaningful capability changes
   - convert into applied improvements or backlog tasks
3. Auto-implement only uncontroversial changes directly in workspace.
4. Never auto-change security boundaries, credentials, external integrations, or runtime permissions.
5. Output format:
   - Implemented now
   - Proposed for backlog
   - Risks/assumptions
   - Next best action
6. Backlog behavior:
   - Append non-trivial items to `TASKS.md` Inbox with ID format: `IMP-AUTO-YYYYMMDD-XX`

---

## Why this schedule
- Security job is nightly to reduce detection latency.
- Improvement job is daily for now to accelerate compounding quality gains; revisit cadence once noise/churn data is available.

---

## Change Log
- 2026-02-26: Repurposed previous hygiene/research jobs into autonomous governance sweeps with explicit guardrails and backlog integration.
