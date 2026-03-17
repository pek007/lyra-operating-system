#!/usr/bin/env bash
set -euo pipefail

# Fail-closed preflight gate.
# Exits non-zero on any critical mismatch.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOCTOR="$SCRIPT_DIR/openclaw-env-doctor.sh"

if [[ ! -x "$DOCTOR" ]]; then
  echo "[FAIL] missing executable doctor script: $DOCTOR"
  exit 2
fi

"$DOCTOR" --strict "$@"

echo "[OK] preflight passed"
