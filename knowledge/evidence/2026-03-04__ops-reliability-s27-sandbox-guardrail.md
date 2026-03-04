# S27 Reliability Guardrail — Sandbox Change Preflight

Date: 2026-03-04
Owner: Lyra

## Problem addressed
Prior incident pattern: enabling sandbox mode in main lane without dependency/runtime compatibility caused instability and blocked execution.

## Guardrail implemented
- Added preflight script: `tools/openclaw_sandbox_preflight.py`
- Enforced rule in ops docs/checklist: **main lane keeps `agents.defaults.sandbox.mode=off` unless explicit change window + canary/isolated validation + rollback plan**.

## Expected outcome
- Prevent repeat of sandbox-induced availability regressions.
- Keep sprint execution lane stable while still allowing isolated sandbox testing when explicitly planned.
