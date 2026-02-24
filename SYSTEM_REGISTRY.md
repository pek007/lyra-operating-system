# SYSTEM_REGISTRY.md

## Purpose
Inventory of key tools/services with ownership, criticality, cost posture, and fallback.

| System/Service | Purpose | Criticality | Owner | Cost Posture | Fallback | Status |
|---|---|---|---|---|---|---|
| OpenClaw Gateway | Core orchestration/runtime | High | Peter/Lyra | Existing | Restart + logs + doctor | Active |
| Telegram Bot Channel | Primary messaging interface | High | Peter/Lyra | Existing | Local dashboard/manual ops | Active |
| OpenAI API path | Primary model execution | High | Peter | Paid (existing API path) | Alternate model/provider; local fallback (future) | Active |
| Brave Search API | External web discovery | Medium | Peter | Optional paid | Manual deep research | Not enabled |
| Deep Research (manual) | High-depth external synthesis | Medium | Peter | Subscription-based/manual | Internal analysis | Available |
| Local model runtime | Resilience + low-cost utility | Medium | Lyra | Free/low | Cloud models | Planned |

## Notes
- Add vendor, renewal date, and monthly spend once finance tracking is set.
