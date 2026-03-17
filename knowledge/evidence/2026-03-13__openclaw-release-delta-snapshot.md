# OpenClaw release-delta snapshot (2026-03-13)

Generated at: 2026-03-13T02:20:34.660557+00:00

## `openclaw --version`
```
OpenClaw 2026.3.8 (3caab92)
```

## `openclaw status`
```
OpenClaw status

Overview
┌─────────────────┬───────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Item            │ Value                                                                                             │
├─────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Dashboard       │ http://127.0.0.1:18789/                                                                           │
│ OS              │ macos 26.3.1 (arm64) · node 22.22.0                                                               │
│ Tailscale       │ off                                                                                               │
│ Channel         │ stable (default)                                                                                  │
│ Update          │ available · pnpm · npm update 2026.3.11                                                           │
│ Gateway         │ local · ws://127.0.0.1:18789 (local loopback) · reachable 13ms · auth token · Mac (192.168.1.67)  │
│                 │ app 2026.3.8 macos 26.3.1                                                                         │
│ Gateway service │ LaunchAgent installed · loaded · running (pid 19953, state active)                                │
│ Node service    │ LaunchAgent not installed                                                                         │
│ Agents          │ 2 · 2 bootstrap files present · sessions 80 · default main active 1m ago                          │
│ Memory          │ 25 files · 43 chunks · sources memory · plugin memory-core · vector ready · fts ready · cache on  │
│                 │ (57)                                                                                              │
│ Probes          │ skipped (use --deep)                                                                              │
│ Events          │ none                                                                                              │
│ Heartbeat       │ 30m (main), disabled (px-internal-dev)                                                            │
│ Sessions        │ 80 active · default gpt-5.4 (200k ctx) · 2 stores                                                 │
└─────────────────┴───────────────────────────────────────────────────────────────────────────────────────────────────┘

Security audit
Summary: 0 critical · 1 warn · 1 info
  WARN Potential multi-user setup detected (personal-assistant model warning)
    Heuristic signals indicate this gateway may be reachable by multiple users: - channels.telegram.groupPolicy="allowlist" with configured group targets - channel…
    Fix: If users may be mutually untrusted, split trust boundaries (separate gateways + credentials, ideally separate OS users/hosts). If you intentionally run shared-user access, set agents.defaults.sandbox.mode="all", keep tools.fs.workspaceOnly=true, deny runtime/fs/web tools unless required, and keep personal/private identities + credentials off that runtime.
Full report: openclaw security audit
Deep probe: openclaw security audit --deep

Channels
┌──────────┬─────────┬────────┬───────────────────────────────────────────────────────────────────────────────────────┐
│ Channel  │ Enabled │ State  │ Detail                                                                                │
├──────────┼─────────┼────────┼───────────────────────────────────────────────────────────────────────────────────────┤
│ Telegram │ ON      │ WARN   │ token config×2 (7680…i8dE · len 46) · accounts 2/2 · gateway: Config allows           │
│          │         │        │ unmentioned group messages (requireMention=false). Telegram Bot API p…                │
└──────────┴─────────┴────────┴───────────────────────────────────────────────────────────────────────────────────────┘

Sessions
┌─────────────────────────────────────────────────┬────────┬─────────┬──────────────┬─────────────────────────────────┐
│ Key                                             │ Kind   │ Age     │ Model        │ Tokens                          │
├─────────────────────────────────────────────────┼────────┼─────────┼──────────────┼─────────────────────────────────┤
│ agent:main:cron:00bd51dc-7eed-4…                │ direct │ 1m ago  │ gpt-5.4      │ 64k/272k (24%) · 🗄️ 280% cached │
│ agent:main:cron:00bd51dc-7eed-4…                │ direct │ 1m ago  │ gpt-5.4      │ 64k/272k (24%) · 🗄️ 280% cached │
│ agent:main:cron:5df2cb00-a984-4…                │ direct │ 21m ago │ gpt-5.4      │ 12k/272k (4%) · 🗄️ 185% cached  │
│ agent:main:cron:5df2cb00-a984-4…                │ direct │ 21m ago │ gpt-5.4      │ 12k/272k (4%) · 🗄️ 185% cached  │
│ agent:main:cron:5df2cb00-a984-4…                │ direct │ 51m ago │ gpt-5.4      │ 13k/272k (5%) · 🗄️ 277% cached  │
│ agent:main:cron:bc32d07c-8ff9-4…                │ direct │ 1h ago  │ gpt-5.4      │ 24k/272k (9%) · 🗄️ 436% cached  │
│ agent:main:cron:bc32d07c-8ff9-4…                │ direct │ 1h ago  │ gpt-5.4      │ 24k/272k (9%) · 🗄️ 436% cached  │
│ agent:main:cron:5df2cb00-a984-4…                │ direct │ 1h ago  │ gpt-5.4      │ 12k/272k (4%) · 🗄️ 185% cached  │
│ agent:main:cron:5df2cb00-a984-4…                │ direct │ 2h ago  │ gpt-5.4      │ 12k/272k (4%) · 🗄️ 185% cached  │
│ agent:main:cron:5df2cb00-a984-4…                │ direct │ 2h ago  │ gpt-5.4      │ 12k/272k (4%) · 🗄️ 185% cached  │
└─────────────────────────────────────────────────┴────────┴─────────┴──────────────┴─────────────────────────────────┘

FAQ: https://docs.openclaw.ai/faq
Troubleshooting: https://docs.openclaw.ai/troubleshooting

Update available (npm 2026.3.11). Run: openclaw update

Next steps:
  Need to share?      openclaw status --all
  Need to debug live? openclaw logs --follow
  Need to test channels? openclaw status --deep
```

## `openclaw update status`
```
OpenClaw update status

┌──────────┬──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Item     │ Value                                                                                                    │
├──────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Install  │ pnpm                                                                                                     │
│ Channel  │ stable (default)                                                                                         │
│ Update   │ available · pnpm · npm update 2026.3.11                                                                  │
└──────────┴──────────────────────────────────────────────────────────────────────────────────────────────────────────┘

Update available (npm 2026.3.11). Run: openclaw update
```
