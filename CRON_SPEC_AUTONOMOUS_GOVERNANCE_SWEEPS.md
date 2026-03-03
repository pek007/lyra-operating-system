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
   - perform a **library relevance pass** across key knowledge surfaces (`governance/`, top-level process docs, `knowledge/`, `tools/`) to identify older artifacts that became newly relevant due to recent decisions/releases
   - run `python3 tools/docs_hygiene_bundle.py` to execute docs-hygiene checks (local markdown link integrity + TASKS.md ID hygiene) with a single fail-fast gate before proposing doc edits
   - run `python3 -m unittest tools/test_parser_smoke.py` to keep parser helper smoke coverage green before modifying automation scripts
2. Perform OpenClaw release-delta check (see `OPENCLAW_RELEASE_DELTA_SOP.md`):
   - capture auditable command snapshot via `python3 tools/openclaw_release_delta_snapshot.py` (writes `knowledge/evidence/YYYY-MM-DD__openclaw-release-delta-snapshot.md`)
   - detect new versions (`openclaw update status`)
   - identify meaningful capability changes
   - convert into applied improvements or backlog tasks
3. Review `TASKS.md` improvement execution status:
   - check open `IMP-AUTO-*` items for stale aging/blockers
   - propose reprioritization or decomposition when execution stalls
   - ensure at least one concrete next-step recommendation is included when open improvement work exists
4. Auto-implement only uncontroversial changes directly in workspace.
5. Never auto-change security boundaries, credentials, external integrations, or runtime permissions.
6. Output format:
   - Implemented now
   - Proposed for backlog
   - Risks/assumptions
   - Next best action
7. Backlog behavior:
   - Append non-trivial items to `TASKS.md` Inbox with ID format: `IMP-AUTO-YYYYMMDD-XX`

---

## Why this schedule
- Security job is nightly to reduce detection latency.
- Improvement job is daily for now to accelerate compounding quality gains; revisit cadence once noise/churn data is available.

---

## Change Log
- 2026-03-03: Expanded `continuous-improvement:sweep` runbook with explicit library relevance pass (`governance/`, process docs, `knowledge/`, `tools/`) and mandatory `TASKS.md` improvement-execution review (stale `IMP-AUTO-*` detection + next-step recommendation).
- 2026-03-03: Added `tools/docs_hygiene_bundle.py` and wired continuous-improvement sweep to run docs-hygiene checks (markdown links + task ID hygiene) through a single fail-fast command.
- 2026-03-03: Added `tools/openclaw_release_delta_snapshot.py` evidence-capture step to the continuous-improvement sweep runbook for auditable release-delta snapshots.
- 2026-03-03: Added `python3 -m unittest tools/test_parser_smoke.py` to the continuous-improvement sweep runbook to keep parser helper smoke coverage green before automation edits.
- 2026-03-03: Added `tools/task_hygiene_check.py` to the continuous-improvement sweep runbook to fail fast on duplicate open task IDs or malformed `IMP-AUTO` IDs.
- 2026-02-26: Repurposed previous hygiene/research jobs into autonomous governance sweeps with explicit guardrails and backlog integration.
