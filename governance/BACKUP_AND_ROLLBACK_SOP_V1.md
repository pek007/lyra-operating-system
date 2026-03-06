# Backup and Rollback SOP (OpenClaw) — V1

Date: 2026-03-06  
Owner: Peter / Lyra  
Scope: Local OpenClaw runtime on Mac mini

## 1) Objective
Ensure we can recover quickly from bad config changes, failed updates, or runtime regressions without losing operational continuity.

## 2) What must be backed up
1. OpenClaw config: `~/.openclaw/openclaw.json`
2. Workspace and governance: `~/.openclaw/workspace`
3. Agent sessions/state: `~/.openclaw/agents/**/sessions`
4. Optional logs for forensics: `~/.openclaw/logs`

## 3) Backup policy (minimum)
- **Pre-change snapshot:** before every config or upgrade change
- **Daily snapshot:** once/day
- **Retention:**
  - Daily: 14 days
  - Weekly: 8 weeks
  - Monthly: 6 months
- **Storage:** local + GitHub (workspace), optionally encrypted external/archive

## 4) Pre-change checklist (GO gate)
Run before any state change:
```bash
openclaw status
openclaw security audit --deep
```
If output includes new critical findings, stop and assess before proceeding.

## 5) Create a snapshot (manual commands)
Use timestamped folder:
```bash
TS=$(date +"%Y%m%d-%H%M%S")
BASE="$HOME/.openclaw/backups/$TS"
mkdir -p "$BASE"

cp "$HOME/.openclaw/openclaw.json" "$BASE/openclaw.json"
cp -R "$HOME/.openclaw/workspace" "$BASE/workspace"
mkdir -p "$BASE/agents"
cp -R "$HOME/.openclaw/agents" "$BASE/agents/all"

# optional
cp -R "$HOME/.openclaw/logs" "$BASE/logs"

echo "Snapshot saved: $BASE"
```

## 6) Fast rollback (known-good config)
When only config is broken:
```bash
# 1) restore known-good config
cp "$HOME/.openclaw/backups/<TIMESTAMP>/openclaw.json" "$HOME/.openclaw/openclaw.json"

# 2) restart gateway
openclaw gateway restart

# 3) verify
openclaw status
openclaw security audit --deep
```

## 7) Full rollback (config + workspace + sessions)
Use when behavior changed materially and config rollback is insufficient:
```bash
SRC="$HOME/.openclaw/backups/<TIMESTAMP>"

cp "$SRC/openclaw.json" "$HOME/.openclaw/openclaw.json"
rm -rf "$HOME/.openclaw/workspace"
cp -R "$SRC/workspace" "$HOME/.openclaw/workspace"
rm -rf "$HOME/.openclaw/agents"
cp -R "$SRC/agents/all" "$HOME/.openclaw/agents"

openclaw gateway restart
openclaw status
openclaw security audit --deep
```

## 8) Telegram-specific safety notes
- `requireMention=false` is intentional for passive topic listening.
- Keep `groupPolicy="allowlist"` and explicit sender allowlists.
- Bot privacy mode is configured in **BotFather** (Telegram), not OpenClaw config.

## 9) GitHub sync procedure
From workspace:
```bash
git add -A
git commit -m "<change summary>"
git push origin main
```
If push fails due to auth, use local commit as rollback anchor and resolve credentials first.

## 10) Post-change verification standard
Always run:
```bash
openclaw status
openclaw security audit --deep
```
Pass condition for operational GO:
- 0 critical findings
- any remaining warnings are documented and accepted by owner

## 11) Incident trigger for immediate rollback
Rollback immediately if any of these occur:
1. Agent cannot respond in primary operations group/topic
2. Unauthorized ingress observed
3. Repeated gateway crash/restart loop
4. Critical security finding after change
5. Major workflow break with no quick forward fix (<15 min)

## 12) Change log discipline
For each change, record:
- timestamp
- reason
- exact command(s)
- files changed
- verification output (status + audit)
- rollback point (backup timestamp + git commit)
