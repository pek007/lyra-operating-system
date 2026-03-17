#!/usr/bin/env bash
set -euo pipefail

STATUS_OUTPUT="$(openclaw status 2>/dev/null || true)"

if [[ -z "$STATUS_OUTPUT" ]]; then
  echo "ALERT: openclaw status returned no output. Check runtime/model health manually."
  exit 0
fi

# Check only the newest visible main + cron sessions. Older rows may remain in the status table
# after an incident and should not keep re-triggering alerts once the system is back on Codex.
MAIN_LINE="$(echo "$STATUS_OUTPUT" | grep "agent:main:telegram:group" | head -1 || true)"
CRON_LINES="$(echo "$STATUS_OUTPUT" | grep "agent:main:cron" | head -3 || true)"
CHECK_BLOCK="$MAIN_LINE
$CRON_LINES"

if echo "$CHECK_BLOCK" | grep -E "anthropic/claude-sonnet|openrouter/anthropic|claude-sonnet-4\.6" >/dev/null; then
  echo "ALERT: Non-Codex model detected in newest main/cron OpenClaw sessions. Expected primary: openai-codex/gpt-5.4. Investigate provider switch/fallback immediately."
  echo
  echo "$CHECK_BLOCK"
  exit 0
fi

# Also alert if newest main session is not on gpt-5.4.
if [[ -n "$MAIN_LINE" ]] && ! echo "$MAIN_LINE" | grep -E "gpt-5\.4|openai-codex" >/dev/null; then
  echo "ALERT: Main session is not on Codex/gpt-5.4. Investigate model routing immediately."
  echo "$MAIN_LINE"
  exit 0
fi

# Silent success.
exit 0
