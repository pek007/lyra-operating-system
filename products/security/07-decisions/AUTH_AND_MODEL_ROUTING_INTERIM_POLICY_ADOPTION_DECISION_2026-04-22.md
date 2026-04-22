# Auth and Model Routing Interim Policy Adoption Decision — 2026-04-22

Status: Approved decision
Owner: Security
Date: 2026-04-22
Decision type: Interim operating policy adoption

## Decision statement
Approved on 2026-04-22: adopt `products/security/04-execution/RECOMMENDED_AUTH_AND_MODEL_ROUTING_POLICY_V1.md` as the interim operating policy for auth and model routing in Lyra OS until a more explicit control surface or superseding policy is approved.

## Why this decision now
The 2026-04-08 OpenClaw auth-loss / fallback / config-recovery incident showed that route health, fallback behavior, and restoration proof were too ambiguous to leave as implicit operator understanding.

By 2026-04-22, the following bounded artifacts exist:
- incident and follow-through chain
- auth/model-route recovery playbook
- current live posture note
- compact recommended routing policy

That is enough to adopt a bounded interim policy rather than continuing to operate on incident memory and chat reasoning alone.

## Policy adopted if approved
Adopt these interim rules:
1. keep `openai-codex/gpt-5.4` as the current primary route unless explicitly changed
2. require one explicit primary route per lane
3. treat fallback as degraded mode, not healthy operation
4. do not silently substitute fallback on higher-trust or higher-cost workflows
5. evaluate new models through bounded canary/testing before promotion
6. require explicit route-restoration verification before declaring auth/model-route recovery complete

## Scope
This interim decision applies to:
- current auth/model-route operating posture in Lyra OS
- operational handling of auth loss, route ambiguity, fallback activation, and model-upgrade evaluation

This decision does **not** claim that all control-surface implementation work is complete.
It sets the working policy baseline while fuller visibility/control treatment continues.

## Rationale
This is the smallest useful decision that:
- captures the current intended operating posture
- reduces silent degraded-mode ambiguity
- lowers the chance of accidental cost/trust exposure
- avoids over-rotating into a larger architecture rewrite before needed

## Approval options
### Option A. Approve now
Adopt the routing policy as the interim operating baseline immediately.

### Option B. Approve with amendments
Adopt now, but modify one or more of:
- fallback allowance boundaries
- canary/promotion rule
- restricted-workload definition
- restoration proof threshold

### Option C. Hold as proposed only
Keep the policy note as guidance, but do not yet treat it as adopted operating policy.

## Approved option
### Option A. Approve now
Reason:
The policy is bounded, conservative, and directly aligned with the actual failure pattern already experienced. Waiting did not appear to add value without a specific disagreement, so the interim policy was approved.

## Linked artifacts
- `OPENCLAW_OAUTH_FAILOVER_AND_CONFIG_VALIDATION_INCIDENT_2026-04-08.md`
- `products/security/03-operating-model/AUTH_AND_MODEL_ROUTE_FAILURE_RECOVERY_PLAYBOOK_V1.md`
- `products/security/04-execution/CURRENT_AUTH_AND_MODEL_ROUTING_POSTURE_2026-04-22.md`
- `products/security/04-execution/RECOMMENDED_AUTH_AND_MODEL_ROUTING_POLICY_V1.md`

## Short conclusion
The recommended routing policy was approved as the interim operating baseline on 2026-04-22 and should be used as the working auth/model-route policy until superseded.
