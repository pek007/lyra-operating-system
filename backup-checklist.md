# backup-checklist.md — OpenClaw Recovery Assets

## Frequency
- Daily: critical backups
- Weekly: restore asset integrity check
- Monthly: drill restore on test host

---

## A) Critical backups (daily)
- [ ] `~/.openclaw/workspace/` complete snapshot
- [ ] OpenClaw config and gateway settings
- [ ] Scheduler/cron definitions
- [ ] Installed skills + versions + pinned state
- [ ] Dependency/tool list required by active skills

---

## B) Security-sensitive artifacts
- [ ] Secret inventory metadata (name, owner, rotation path)
- [ ] Vault export/backup strategy documented
- [ ] No plaintext secrets in policy/docs
- [ ] Credential rotation playbook available

---

## C) Governance artifacts
- [ ] `skills-governance.md`
- [ ] `skills-policy.yaml`
- [ ] `evidence-pack-template.md`
- [ ] `DR-PLAN.md`
- [ ] `restore.md`

---

## D) Verification checks (weekly)
- [ ] Backup can be read/mounted
- [ ] File counts/sizes look sane
- [ ] Latest snapshot timestamp verified
- [ ] Spot-check key files open correctly

---

## E) Monthly drill checklist
- [ ] Fresh test environment prepared
- [ ] Restore executed using `restore.md`
- [ ] `openclaw status` verified
- [ ] `openclaw security audit --deep` executed
- [ ] Critical smoke tests passed
- [ ] Measured total recovery time recorded
- [ ] Runbook updates captured after drill

---

## F) Contacts/ownership
- System owner: Peter
- DR runbook owner: Lyra + Peter
- Escalation path: define local support/vendor contacts

---

## G) Success criteria
- [ ] Core operations recovered within RTO (60 min)
- [ ] Data restored within RPO (24h)
- [ ] No unresolved critical security findings post-restore
