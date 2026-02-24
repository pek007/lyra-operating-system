# RISK_REGISTER.md

## Purpose
Maintain a live register of operational, security, and execution risks.

| Risk | Impact | Likelihood | Owner | Mitigation | Status |
|---|---|---|---|---|---|
| Channel outage (Telegram/API token issues) | High | Medium | Lyra | Token hygiene, pair verification, status checks | Monitoring |
| External web search cost/ROI uncertainty | Medium | Medium | Peter | Brave API enabled; run 30-day usage baseline and monthly subscription review | Monitoring |
| Process drift (docs not followed) | Medium | Medium | Lyra | Weekly metrics + review cadence + DoD enforcement | Open |
| Single-provider model dependency | Medium | Medium | Peter/Lyra | Model routing policy + add secondary/provider fallback | Open |
| Backup/restore execution evidence incomplete | Medium | Low | Lyra | RST-2026-001 completed; repeat monthly and add offsite simulation | Monitoring |

## Review Rule
- Update weekly in metrics cycle.
- Escalate any risk that becomes High impact + High likelihood.
