# TOOL_EXTERNAL_SERVICE_GOVERNANCE_V1.md

Status: Active (v1)
Owner: Peter (A), Lyra (R)

## Purpose
Turn tool/external-service governance from policy intent into enforceable controls.

## Minimum control requirements
1. Default deny for high-impact external actions unless approval obligation satisfied.
2. Credential handling via managed secrets (no plaintext repo secrets; no long-lived static keys when avoidable).
3. Request controls: schema validation, timeout, bounded retry with backoff, rate limits.
4. Response controls: sanitize outputs before reinjection into model context.
5. Audit controls: every external call must emit structured audit record.

## Scope
All external integrations (messaging, task systems, model APIs, web tools, code hosting APIs).

## Change gate
No new external integration is promoted beyond evaluation unless:
- evidence pack is complete,
- risk class and approval gate are set,
- rollback/kill-switch is documented.
