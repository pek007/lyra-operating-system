# SEC-AUTO-20260305-01 — Residual risk revalidation (multi-user heuristic)

Date: 2026-03-06

## Revalidation result
Command run: `openclaw security audit --deep`

Current summary:
- 0 critical
- 1 warn
- 1 info

Persisting warning:
- `security.trust_model.multi_user_heuristic`
- Triggered by group-capable Telegram setup with runtime/process tools and sandbox-off posture for main agent.

## Acceptance decision
Residual warning is **accepted** under the documented trusted-operator model.

Acceptance criteria (must remain true):
1. Telegram group access remains strict allowlist with explicit sender allowlists.
2. `tools.fs.workspaceOnly=true` remains enabled.
3. Runtime/tooling access remains intentionally scoped to trusted operator contexts.
4. No new untrusted-user surface is added without explicit boundary decision.

## Expiry / review trigger
- Acceptance expiry: **2026-04-06** (30 days)
- Reopen immediately if any of:
  - group/user trust boundary changes
  - new external/public ingress path is added
  - requirement emerges for non-trusted multi-user access

## Migration path if boundary changes
If trust model changes from single trusted-operator to mixed/untrusted users:
- split to separate gateway + identity boundary (preferred), or
- isolate with sandbox-first constraints and reduced high-impact tool exposure.

## Linked records
- `governance/GO_RISK_DECISION_2026-03-06.md`
- `governance/TRUST_BOUNDARY_POLICY_RECORD_2026-03-04.md`
