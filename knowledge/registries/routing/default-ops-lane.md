---
id: ROUTE-default-ops
enabled: true
priority: 100
match:
  taskType: [ops]
  riskLevel: [low, medium]
  decisionType: [type2]
  dataClass: [internal, confidential]
route:
  championModel: openai-codex/gpt-5.3-codex
  challengerModel: openrouter/anthropic/claude-sonnet-4-5
  fallbackModels: [openai-codex/gpt-5.3-codex]
  maxCostTier: medium
  maxLatencyMs: 120000
governance:
  antiThrashWindowDays: 30
  changeGate: normal
review:
  lastReviewed: 2026-02-25
  nextReview: 2026-03-25
---

# Routing Rule
Default operations-lane routing rule.
