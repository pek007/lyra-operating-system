# SEC-001: Security Baseline Checklist

## Purpose
Minimum security controls for safe day-to-day operation.

## Identity & Access
- [ ] MFA enabled on critical accounts (email, Telegram bot owner, model providers, repo)
- [ ] No shared passwords without explicit control
- [ ] Access list reviewed monthly

## Device Security
- [ ] Full-disk encryption enabled (FileVault)
- [ ] Screen lock enabled with reasonable timeout
- [ ] OS and critical software update cadence defined

## Secrets Hygiene
- [x] API keys/tokens stored in approved config/auth stores
- [x] No long-term plain-text secret storage in docs
- [x] Secret rotation procedure defined
- [x] Exposure response tested (rotate + verify)

## Operations & Resilience
- [ ] Backup path enabled
- [x] Restore test completed (last 30 days)
- [x] Incident mini-runbook available and known

## Runtime Safety (Agent)
- [x] External-send actions require explicit intent/approval
- [x] Sensitive data handling rules documented
- [x] Prompt-injection caution applied to external content
- [x] High-risk actions are logged and reviewable

## Evidence Tracking
- Last reviewed: 2026-02-24
- Reviewed by: Lyra
- Gaps found: MFA verification pending, monthly access review not yet established, backup path evidence still partial, state-dir permissions warning (mode 755).
- Remediation tasks created: OPS-2026-004, OPS-2026-005, OPS-2026-006

## Version
- v1.0
- Date: 2026-02-24
