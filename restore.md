# restore.md — Step-by-Step OpenClaw Restore

Use this runbook when recovering from hardware failure, OS reinstall, or severe corruption.

## Pre-flight
1. Confirm you have access to:
   - latest backup snapshot
   - account credentials for required services
   - secret manager / key vault
2. Decide restore mode:
   - Fast Restore (backup-based)
   - Clean Rebuild (from scratch + backup workspace)

---

## Phase 1 — Base system and OpenClaw
1. Install system updates and required runtimes.
2. Install OpenClaw.
3. Start gateway/service.
4. Verify baseline:
   - `openclaw gateway status`
   - `openclaw status`

If OpenClaw does not start, stop here and fix platform/runtime before continuing.

---

## Phase 2 — Restore workspace
1. Restore backup of `~/.openclaw/workspace/`.
2. Verify key files exist:
   - `skills-governance.md`
   - `skills-policy.yaml`
   - `evidence-pack-template.md`
   - `DR-PLAN.md`
   - `backup-checklist.md`
3. Check git state (if repository-backed):
   - `git -C ~/.openclaw/workspace status`

---

## Phase 3 — Rebuild skills and tooling
1. Reinstall required CLIs/tool dependencies.
2. Reinstall skills from pinned list.
3. Apply skill states per policy:
   - enabled
   - sandbox-evaluate
   - restricted
4. Validate skill availability with a read-only check.

---

## Phase 4 — Restore secrets safely
1. Reconnect secrets from vault/keyring.
2. Reissue/rotate keys that were exposed during incident.
3. Validate no plaintext secrets in workspace docs.
4. Confirm each S2/S3 skill auth path works with least privilege.

---

## Phase 5 — Security and integrity validation
Run:
- `openclaw security audit --deep`
- `openclaw update status`

Review and fix critical findings before moving on.

---

## Phase 6 — Smoke tests (critical workflows)
Run one test per critical area:
1. Research workflow (e.g., summarize read-only)
2. Git workflow (non-destructive API/list action)
3. Notes/transcription workflow (local processing)
4. Cost/usage reporting workflow

Mark pass/fail and record issue owner.

---

## Phase 7 — Bring automations back
1. Restore scheduled jobs/cron tasks.
2. Verify each task has:
   - name
   - cadence
   - output destination
3. Trigger one manual run for each critical scheduled job.

---

## Completion criteria
- OpenClaw healthy
- Policies/templates restored
- Required skills operational in correct risk state
- Security audit run and reviewed
- Smoke tests passing
- Automation baseline restored

---

## Incident notes template
- Incident date/time:
- Trigger/root cause:
- Recovery mode used:
- Start time / End time:
- Total recovery duration:
- Data loss window (RPO):
- Credentials rotated:
- Follow-ups:
