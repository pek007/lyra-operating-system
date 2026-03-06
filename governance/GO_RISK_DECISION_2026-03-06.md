# GO Risk Decision — 2026-03-06

## Context
OpenClaw runs in a trusted-operator setup and must listen to configured Telegram group topics without explicit @mention (`requireMention=false`) to support channel/topic-based operations.

## Decision
Proceed with operational GO under a **trusted-boundary model**, with compensating controls, rather than forcing full sandbox isolation (`sandbox.mode="all"`) that breaks required workflows.

## Accepted Risks
1. Security audit will continue to emit a trust-model warning in shared/group-access patterns when powerful tools are enabled.
2. Passive group listening increases exposure if ingress controls are too broad.

## Compensating Controls (required)
1. Telegram group access stays on allowlist mode.
2. Sender allowlists are explicit at channel/account/group levels.
3. `requireMention=false` remains enabled only for intended groups/topics.
4. `tools.fs.workspaceOnly=true` remains enabled.
5. Runtime tools (`exec`, `process`) remain restricted to trusted operator contexts.
6. Run `openclaw security audit --deep` periodically and after significant config changes.

## Implemented Today
- Added top-level Telegram sender allowlists to remove ambiguous allowlist scope:
  - `channels.telegram.groupAllowFrom = [8283124284]`
  - `channels.telegram.allowFrom = [8283124284]`

## Remaining Non-Blocking Warnings
1. Trust-model heuristic warning (expected under this architecture).
2. Telegram privacy-mode advisory for unmentioned messages (must be set in BotFather per bot).

## Verification Commands
- `openclaw status --all`
- `openclaw security audit --deep`

## Owner
Peter / Lyra
