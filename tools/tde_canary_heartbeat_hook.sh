#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
python3 tools/tde_canary_runtime_cycle.py \
  --trigger-source heartbeat \
  --stalled-alert-threshold "${TDE_STALLED_ALERT_THRESHOLD:-1}"
