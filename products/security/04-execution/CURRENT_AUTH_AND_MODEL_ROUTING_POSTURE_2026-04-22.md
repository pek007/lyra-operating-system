# Current Auth and Model Routing Posture — 2026-04-22

Status: Working posture note
Owner: Security
Date: 2026-04-22

## Purpose
Record the current live auth and model-routing posture after the 2026-04-08 OpenClaw auth-loss / fallback / config-recovery incident and the subsequent 2026-04-22 recovery and posture discussion.

This note is intentionally compact. It is not a full architecture spec. It states the currently verified route, the current posture judgment, and the next control questions that still remain open.

## Live evidence checked
- `node /Users/lyra/.nvm/versions/node/v22.22.0/lib/node_modules/openclaw/openclaw.mjs config get agents.list`
- `node /Users/lyra/.nvm/versions/node/v22.22.0/lib/node_modules/openclaw/openclaw.mjs status --all`
- gateway status output showing `agent model: openai-codex/gpt-5.4`

## Current verified primary route
### Primary auth/provider route
- `openai-codex`

### Primary model
- `gpt-5.4`

### Current effective agent mapping verified directly
- `main` -> `openai-codex/gpt-5.4`
- `px-internal-dev` -> `openai-codex/gpt-5.4`

## Current posture judgment
### 1. Primary route appears live again
As of 2026-04-22, the live status and agent configuration indicate that the intended primary route is active again on the currently checked agents.

### 2. Recovery confidence is improved but not fully mature as a control system
The route is currently working, but the broader resilience posture is still not fully closed because the system still needs clearer bounded rules for degraded mode, fallback visibility, and explicit restoration proof.

### 3. Silent fallback remains the core design risk
The most important unresolved posture issue is not whether the current primary route is live. It is whether future auth loss or provider disruption can produce hidden fallback behavior, ambiguous health state, or cost exposure without sufficiently explicit operator visibility.

## Current intended operating posture
### A. Preferred steady state
The preferred steady state is:
- primary auth/provider route: `openai-codex`
- primary model: `gpt-5.4`
- primary agent operation on the intended route rather than on hidden fallback

### B. Degraded mode should not count as healthy
If the intended primary route is unavailable but another route is carrying load, that should be treated as degraded mode rather than healthy operation.

### C. Route restoration should require proof
Recovery should not be treated as complete only because the gateway starts or sessions respond.

Minimum meaningful restoration proof should include:
- the intended primary route is active again
- the intended model mapping is restored for the affected agent(s)
- fallback is no longer silently carrying the relevant load, or is explicitly bounded and visible
- at least one bounded practical workload or lane confirms the restored route in use

## Current known limitations / open questions
### 1. Fallback policy is not yet fully codified on one compact surface
We know fallback behavior mattered in the incident, but the current bounded allowed/forbidden fallback policy is not yet expressed on one compact operator-facing note.

### 2. Auth-loss visibility still needs stronger explicit control treatment
The general direction is already recorded in the auth resilience disposition and recovery playbook, but the exact compact operator-facing visibility/control surface is still not fully closed.

### 3. Model-option evolution remains external to this note
OpenAI may add additional Codex models over time, but availability from OpenAI is not identical to immediate operational adoption in OpenClaw. New models should be treated as candidate routes pending support verification and bounded evaluation.

## Operational rule for now
Until a narrower and more explicit routing-control surface exists, the practical posture is:
- use `openai-codex/gpt-5.4` as the verified primary route
- treat auth loss or route ambiguity as a resilience issue, not just a provider hiccup
- do not assume fallback behavior is acceptable merely because service remains responsive
- require explicit bounded verification before calling route recovery complete

## Linked artifacts
- `OPENCLAW_OAUTH_FAILOVER_AND_CONFIG_VALIDATION_INCIDENT_2026-04-08.md`
- `IR-001_INCIDENT_MINI_RUNBOOK.md`
- `products/improvement/04-execution/OPENCLAW_AUTH_RESILIENCE_CONTROL_VISIBILITY_DISPOSITION_2026-04-09.md`
- `products/improvement/04-execution/OPENCLAW_ACPX_CONFIG_COMPATIBILITY_DISPOSITION_2026-04-09.md`
- `products/security/03-operating-model/AUTH_AND_MODEL_ROUTE_FAILURE_RECOVERY_PLAYBOOK_V1.md`

## Short conclusion
Current verified posture on 2026-04-22:
- both checked agents are configured for `openai-codex/gpt-5.4`
- the primary route appears live again
- the remaining problem is not basic route availability, but operational maturity around degraded mode, fallback visibility, and explicit restoration proof
