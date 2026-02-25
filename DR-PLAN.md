# DR-PLAN.md — OpenClaw Rapid Recovery Plan

## Objective
Restore core Lyra/OpenClaw operations quickly after host failure, reinstall, or major corruption.

**Target RTO (Recovery Time Objective):** 60 minutes for core operations  
**Target RPO (Recovery Point Objective):** 24 hours (daily backups)

---

## 1) Recovery Priorities (in order)
1. OpenClaw service online
2. Workspace restored (`~/.openclaw/workspace`)
3. Skills and policies restored (pinned versions)
4. Secrets reconnected/rotated
5. Core workflows validated
6. Optional automations (cron/secondary agents) restored

---

## 2) What must be backed up

### Critical (must-have)
- `~/.openclaw/workspace/`
  - governance docs
  - policies/templates
  - memory files
  - custom workflows/assets
- OpenClaw configuration and scheduler definitions
- Installed skills list + pinned versions
- Tool/runtime dependency list (CLI requirements)
- Secret inventory metadata (where each secret lives, owner, rotation method)

### Sensitive handling
- Do **not** store plaintext secrets in docs.
- Keep encrypted backup for any secret material if you choose to back it up.
- Prefer re-issuance/rotation during restore.

---

## 3) Recovery Modes

### Mode A — Fast Restore (preferred)
Use latest known-good backup snapshot and follow `restore.md`.

### Mode B — Clean Rebuild
Reinstall OpenClaw and dependencies from scratch, then restore workspace and reapply governance controls.

---

## 4) Validation Gates (must pass)
- `openclaw status` returns healthy
- `openclaw security audit --deep` completes without critical blockers
- Required skills are installed and in expected state
- One smoke test per critical workflow passes
- Cost/usage telemetry available

---

## 5) Roles and decisions
- **System owner:** Peter
- **Decision rule during incident:** restore minimal safe baseline first, then optimize
- **Change control:** no risky expansion during incident; only recovery-required changes

---

## 6) Drill policy
- Run one recovery drill monthly (sandbox/test host)
- Track:
  - actual restore time
  - failed steps
  - missing artifacts
- Update `restore.md` immediately after each drill

---

## 7) Post-incident checklist
- Rotate exposed/reused credentials
- Review logs and identify root cause
- Patch backup gaps
- Update DR docs and governance controls
- Record lessons learned in memory/workspace docs

---

## 8) “Done” definition
Recovery is complete when:
1. Core service healthy
2. Workspace + policies restored
3. Critical workflows pass smoke tests
4. Security audit and credential posture verified
5. Incident notes captured
