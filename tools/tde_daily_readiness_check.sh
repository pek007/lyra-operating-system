#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DATE_TAG="$(date -u +%Y-%m-%d)"

python3 "$ROOT_DIR/tools/tde_cutover_readiness_report.py"

SRC="$ROOT_DIR/knowledge/evidence/metrics/2026-03-04__tde-db-cutover-readiness-report-v1.json"
DST="$ROOT_DIR/knowledge/evidence/metrics/${DATE_TAG}__tde-db-cutover-readiness-report-v1.json"

if [[ "$SRC" != "$DST" ]]; then
  cp "$SRC" "$DST"
  echo "[PASS] archived readiness report -> $DST"
else
  echo "[PASS] readiness report already date-stamped for $DATE_TAG"
fi
