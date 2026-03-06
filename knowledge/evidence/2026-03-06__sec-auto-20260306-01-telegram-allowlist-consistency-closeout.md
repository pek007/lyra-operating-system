# SEC-AUTO-20260306-01 closeout — Telegram allowlist consistency

Date: 2026-03-06

## Objective
Resolve Telegram allowlist inconsistency (`groupPolicy=allowlist` with empty `groupAllowFrom/allowFrom`) to prevent silent group-message drops and align trust intent.

## Verification snapshot
Config (`~/.openclaw/openclaw.json`) now shows explicit sender allowlists:
- `channels.telegram.groupPolicy = "allowlist"`
- `channels.telegram.groupAllowFrom = [8283124284]`
- `channels.telegram.allowFrom = [8283124284]`
- `channels.telegram.accounts.default.groupAllowFrom = [8283124284]`
- `channels.telegram.accounts.vega.groupAllowFrom = [8283124284]`

Operational checks:
- `openclaw status --all` shows Telegram account notes with `allow:8283124284` for both accounts.
- `openclaw security audit --deep` no longer reports empty allowlist inconsistency; remaining warning is trust-model heuristic (expected and separately governed).

## Outcome
Allowlist inconsistency is resolved and documented. Residual security warning scope is unchanged (sandbox/trust-boundary heuristic) and already tracked under separate SEC task(s).
