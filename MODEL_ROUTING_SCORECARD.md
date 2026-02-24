# MODEL_ROUTING_SCORECARD.md

## Purpose
Champion-challenger evaluation for model routing with anti-thrash governance.

## Lanes
- Operations lane
- Research lane
- Build lane
- Premium Type-1 lane

## Monthly Anti-Thrash Rule
- Default route changes occur only in monthly review unless:
  - outage,
  - severe quality regression,
  - major cost anomaly.
- Emergency changes require rollback note + review date.

## Scorecard Metrics (per lane)
- Quality (1-5)
- Speed (1-5)
- Cost efficiency (1-5)
- Reliability/tool success (1-5)
- Rework required (inverse, 1-5)

## Weekly Sample Log Template
| Date | Lane | Champion Model | Challenger Model | Winner | Notes |
|---|---|---|---|---|---|
| YYYY-MM-DD | ops/research/build/premium | ... | ... | ... | ... |

## Current Defaults (initial)
- Keep current main default stable.
- Use challenger tests on subagent tasks before switching any lane default.

## Decision Rule
- Promote challenger only if it wins 2 consecutive weekly samples and has no risk red flags.

## Version
- v1.0
- Date: 2026-02-24
