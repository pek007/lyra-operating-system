#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

TDE_ENV="${TDE_ENV:-}"
if [[ -z "$TDE_ENV" ]]; then
  echo "ERROR: TDE_ENV must be explicitly set to dev|staging|prod" >&2
  exit 1
fi
if [[ "$TDE_ENV" != "dev" && "$TDE_ENV" != "staging" && "$TDE_ENV" != "prod" ]]; then
  echo "ERROR: Invalid TDE_ENV='$TDE_ENV' (expected dev|staging|prod)" >&2
  exit 1
fi

RUNTIME_ROOT="$ROOT_DIR/os/runtime/$TDE_ENV"
EVIDENCE_ROOT="$ROOT_DIR/knowledge/evidence/$TDE_ENV"
mkdir -p "$RUNTIME_ROOT" "$EVIDENCE_ROOT"
CURRENT_YYYY_MM="$(date +%Y-%m)"
EVIDENCE_PERIOD_DIR="$EVIDENCE_ROOT/$CURRENT_YYYY_MM"
mkdir -p "$EVIDENCE_PERIOD_DIR"

SHADOW_ENABLED="${TDE_SHADOW_STATE_ENABLED:-1}"
SHADOW_DB_PATH="${TDE_SHADOW_STATE_DB_PATH:-$RUNTIME_ROOT/tde_state.sqlite}"
SHADOW_ALERT_PATH="${TDE_SHADOW_STATE_ALERT_PATH:-$EVIDENCE_ROOT/metrics/tde-shadow-state-alerts.jsonl}"
SHADOW_MISMATCH_THRESHOLD="${TDE_SHADOW_STATE_MISMATCH_THRESHOLD:-3}"
CANONICAL_STORE="${TDE_CANONICAL_STATE_STORE:-db}"
CANONICAL_DB_PATH="${TDE_CANONICAL_DB_PATH:-$RUNTIME_ROOT/tde_state.sqlite}"
WRITEBACK_TASKS_PATH="${TDE_TASKS_PROJECTION_PATH:-$RUNTIME_ROOT/TASKS_from_db.md}"
OBJECTIVE_REGISTRY_PATH="${TDE_OBJECTIVE_REGISTRY_PATH:-$RUNTIME_ROOT/tde_objectives.json}"
BINDING_REGISTRY_PATH="${TDE_BINDING_REGISTRY_PATH:-$RUNTIME_ROOT/tde_active_bindings.json}"
ARTIFACT_PATH="${TDE_JOB_TICK_ARTIFACT_PATH:-$EVIDENCE_PERIOD_DIR/tde-job-tick-latest.json}"

CMD=(
  python3 "$ROOT_DIR/tools/tde_job_tick_runner.py"
  --trigger-source cron
  --session-key "${TDE_JOB_TICK_SESSION_KEY:-cron:tde-job-runner-v1}"
  --job-id "${TDE_JOB_ID:-JOB-PROD-001}"
  --binding-id "${TDE_JOB_BINDING_ID:-BIND-JOB-PROD-001-ACTIVE}"
  --actor-id "${TDE_ACTOR_ID:-lyra}"
  --max-claim "${TDE_JOB_MAX_CLAIM:-1}"
  --tasks-path "$ROOT_DIR/TASKS.md"
  --writeback-tasks-path "$WRITEBACK_TASKS_PATH"
  --artifact-path "$ARTIFACT_PATH"
  --binding-registry-path "$BINDING_REGISTRY_PATH"
  --objective-registry-path "$OBJECTIVE_REGISTRY_PATH"
  --canonical-store "$CANONICAL_STORE"
  --canonical-db-path "$CANONICAL_DB_PATH"
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
