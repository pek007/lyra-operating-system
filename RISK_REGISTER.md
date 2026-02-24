# RISK_REGISTER.md

## Purpose
Maintain a live register of operational, security, and execution risks.

| Risk | Impact | Likelihood | Owner | Mitigation | Status |
|---|---|---|---|---|---|
| Channel outage (Telegram/API token issues) | High | Medium | Lyra | Token hygiene, pair verification, status checks | Monitoring |
| Missing external web search API | Medium | High | Peter | Use manual deep research until business case approved | Open |
| Process drift (docs not followed) | Medium | Medium | Lyra | Weekly metrics + review cadence + DoD enforcement | Open |
| Single-provider model dependency | Medium | Medium | Peter/Lyra | Model routing policy + add secondary/provider fallback | Open |
| Backup/restore not yet fully runbooked | High | Medium | Lyra | Create OPS-001 + restoration test evidence | Planned |

## Review Rule
- Update weekly in metrics cycle.
- Escalate any risk that becomes High impact + High likelihood.
