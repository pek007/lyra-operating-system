#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

SHADOW_ENABLED="${TDE_SHADOW_STATE_ENABLED:-1}"
SHADOW_DB_PATH="${TDE_SHADOW_STATE_DB_PATH:-$ROOT_DIR/os/runtime/tde_state.sqlite}"
SHADOW_ALERT_PATH="${TDE_SHADOW_STATE_ALERT_PATH:-$ROOT_DIR/knowledge/evidence/metrics/tde-shadow-state-alerts.jsonl}"
SHADOW_MISMATCH_THRESHOLD="${TDE_SHADOW_STATE_MISMATCH_THRESHOLD:-3}"

CMD=(
  python3 "$ROOT_DIR/tools/tde_job_tick_runner.py"
  --trigger-source cron
  --session-key "${TDE_JOB_TICK_SESSION_KEY:-cron:tde-job-runner-v1}"
  --job-id "${TDE_JOB_ID:-JOB-PROD-001}"
  --binding-id "${TDE_JOB_BINDING_ID:-BIND-JOB-PROD-001-ACTIVE}"
  --actor-id "${TDE_ACTOR_ID:-lyra}"
  --max-claim "${TDE_JOB_MAX_CLAIM:-1}"
  --tasks-path "$ROOT_DIR/TASKS.md"
  --artifact-path "$ROOT_DIR/knowledge/evidence/2026-03/tde-job-tick-latest.json"
)

if [[ "$SHADOW_ENABLED" == "1" ]]; then
  CMD+=(
    --shadow-state-enabled
    --shadow-state-db-path "$SHADOW_DB_PATH"
    --shadow-state-alert-path "$SHADOW_ALERT_PATH"
    --shadow-state-mismatch-threshold "$SHADOW_MISMATCH_THRESHOLD"
  )
fi

"${CMD[@]}"
