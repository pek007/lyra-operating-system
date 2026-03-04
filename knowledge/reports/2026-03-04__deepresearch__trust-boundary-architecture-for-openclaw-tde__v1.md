# Trust Boundary Architecture for OpenClaw/TDE

Source: deep research report shared by Peter (2026-03-04)

## Executive recommendation (captured)
Use **Option A (hardened single-trust boundary)** as the default production posture now, and keep **Option B (split boundary)** pre-planned with explicit trigger thresholds.

## Why this recommendation fits current state
- Matches OpenClaw’s documented default security model (single trusted operator boundary per gateway).
- Matches current stable operating posture after sandbox incidents:
  - `agents.defaults.sandbox.mode=off`
  - `tools.fs.workspaceOnly=true`
  - residual `security.trust_model.multi_user_heuristic` accepted under explicit policy/reopen triggers.

## Core architectural principle from report
Separate:
1. **Policy decision layer** (declares trust boundary, allowed channels, escalation/split triggers)
2. **Runtime enforcement layer** (OpenClaw config toggles, allowlists, tool denies, sandbox posture, trusted proxies)

## Option A controls (recommended default)
- Loopback bind + explicit trusted proxy posture
- Telegram group allowlist + sender allowlist + mention gating
- Group-level tool denies for high-risk tools
- Main lane stability rule: sandbox mode remains `off` unless approved change window + canary + preflight
- Residual warning acceptance remains valid only while reopen triggers are false

## Option B trigger model (A -> B split)
Trigger split boundary when any of these become true:
- Group expands beyond mutually trusted operators
- More than one distinct human can steer high-impact tool paths on same gateway
- Need to expose gateway beyond loopback for shared access
- Security audit criticals or unacceptable trust-boundary drift appears

## Sprint interpretation from report
- **Sprint 1:** Formalize Option A policy + enforceable channel/tool controls + mandatory post-change validation bundle.
- **Sprint 2:** Prepare low-drama Option B template (separate shared gateway profile, handoff protocol, incident playbook addendum).

## Practical takeaway
No immediate architecture flip is required. We should codify Option A as policy/enforcement baseline now and implement explicit A→B trigger-based migration readiness.
