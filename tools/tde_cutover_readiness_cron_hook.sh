#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

bash "$ROOT_DIR/tools/tde_daily_readiness_check.sh"
python3 "$ROOT_DIR/tools/tde_cutover_alert_check.py"

echo "[PASS] tde cutover readiness cron hook completed"
