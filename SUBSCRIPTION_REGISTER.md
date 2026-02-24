# SUBSCRIPTION_REGISTER.md

## Purpose
Single source of truth for all paid tools/services: cost, owner, usage, renewal, and termination readiness.

## Operating Rule
No paid service without an entry here.

## Fields
- Service
- Category
- Owner
- Plan
- Monthly cost (SEK)
- Billing cycle
- Renewal date
- Payment method
- Purpose / expected value
- Usage metric
- Last 30d usage
- ROI status (Keep / Review / Cancel)
- Cancel path tested? (Y/N)
- Cancellation URL/steps
- Notes

## Active Subscriptions

| Service | Category | Owner | Plan | Monthly cost (SEK) | Billing cycle | Renewal date | Purpose | Usage metric | Last 30d usage | ROI status | Cancel path tested? | Cancellation URL/steps |
|---|---|---|---|---:|---|---|---|---|---|---|---|---|
| Brave Search API | Research API | Peter | Search API | TBD | Monthly | TBD | Enable live web research in OpenClaw | `web_search` calls/day | Baseline starts now | Review in 30 days | No | Brave dashboard > API billing/subscription |

## Review Cadence
- Weekly: update Last 30d usage for paid services.
- Monthly: decide Keep / Review / Cancel for each service.
- Quarterly: zero-based review (justify every paid tool again).

## Termination Standard
A service is "termination-ready" only when:
1. Cancellation path is documented.
2. Data export path is known.
3. Operational fallback is defined.
4. A replacement or shutdown plan exists.

## Version
- v1.0
- Date: 2026-02-24
