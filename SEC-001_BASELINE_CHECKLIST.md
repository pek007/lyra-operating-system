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
- [ ] API keys/tokens stored in approved config/auth stores
- [ ] No long-term plain-text secret storage in docs
- [ ] Secret rotation procedure defined
- [ ] Exposure response tested (rotate + verify)

## Operations & Resilience
- [ ] Backup path enabled
- [ ] Restore test completed (last 30 days)
- [ ] Incident mini-runbook available and known

## Runtime Safety (Agent)
- [ ] External-send actions require explicit intent/approval
- [ ] Sensitive data handling rules documented
- [ ] Prompt-injection caution applied to external content
- [ ] High-risk actions are logged and reviewable

## Evidence Tracking
- Last reviewed:
- Reviewed by:
- Gaps found:
- Remediation tasks created:

## Version
- v1.0
- Date: 2026-02-24
