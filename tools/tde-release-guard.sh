#!/usr/bin/env bash
set -euo pipefail

# TDE release guard: fail-closed readiness gate
# Runs environment + contract checks and basic canary freshness checks.

REPO_NAME="lyra-operating-system"
WORKSPACE_DIR="${OPENCLAW_WORKSPACE_DIR:-$HOME/.openclaw/workspace}"
ROOT="$WORKSPACE_DIR/repos/$REPO_NAME"
CANARY_FILE="$ROOT/knowledge/evidence/2026-03/tde-canary-status-latest.json"
MAX_CANARY_AGE_MIN=90

FAIL=0
WARN=0
pass(){ echo "[PASS] $*"; }
warn(){ echo "[WARN] $*"; WARN=$((WARN+1)); }
fail(){ echo "[FAIL] $*"; FAIL=$((FAIL+1)); }

echo "== TDE Release Guard =="
echo "root: $ROOT"

if [[ ! -d "$ROOT" ]]; then
  echo "[FAIL] repo root not found: $ROOT"
  exit 2
fi

# 1) Environment preflight (hard gate)
if "$ROOT/tools/openclaw-preflight.sh" --repo "$REPO_NAME"; then
  pass "environment preflight passed"
else
  fail "environment preflight failed"
fi

# 2) Kernel thin-slice tests (hard gate)
if python3 "$ROOT/tools/tde_kernel_slice_tests.py"; then
  pass "TDE kernel thin-slice tests passed"
else
  fail "TDE kernel thin-slice tests failed"
fi

# 3) Runtime authority/objective registries present (hard gate)
[[ -f "$ROOT/os/runtime/tde_active_bindings.json" ]] && pass "binding registry present" || fail "missing tde_active_bindings.json"
[[ -f "$ROOT/os/runtime/tde_objectives.json" ]] && pass "objective registry present" || fail "missing tde_objectives.json"

# 4) Canary freshness + stalled count (warn gate)
if [[ -f "$CANARY_FILE" ]]; then
  pass "canary artifact found"
  python3 - "$CANARY_FILE" "$MAX_CANARY_AGE_MIN" <<'PY'
import json,sys,time,datetime
p=sys.argv[1]
max_age_min=int(sys.argv[2])
with open(p) as f:
    d=json.load(f)
ts=d.get('cycleTimestamp')
stalled=d.get('stalledCount')
# tolerate ISO with/without Z
if ts:
    t=ts.replace('Z','+00:00')
    dt=datetime.datetime.fromisoformat(t)
    age=(datetime.datetime.now(datetime.timezone.utc)-dt.astimezone(datetime.timezone.utc)).total_seconds()/60
    print(f"CANARY_AGE_MIN={age:.1f}")
    if age>max_age_min:
        print("CANARY_STALE=1")
if stalled is not None:
    print(f"CANARY_STALLED={stalled}")
PY
  AGE_LINE=$(python3 - "$CANARY_FILE" <<'PY'
import json,sys,datetime
p=sys.argv[1]
with open(p) as f:
    d=json.load(f)
ts=d.get('cycleTimestamp')
if not ts:
    print("UNKNOWN")
    raise SystemExit
try:
    dt=datetime.datetime.fromisoformat(ts.replace('Z','+00:00'))
    age=(datetime.datetime.now(datetime.timezone.utc)-dt.astimezone(datetime.timezone.utc)).total_seconds()/60
    print(f"{age:.1f}")
except Exception:
    print("UNKNOWN")
PY
)
  if [[ "$AGE_LINE" != "UNKNOWN" ]]; then
    if python3 - "$AGE_LINE" "$MAX_CANARY_AGE_MIN" <<'PY'
import sys
age=float(sys.argv[1]); max_age=float(sys.argv[2])
raise SystemExit(0 if age>max_age else 1)
PY
    then
      warn "canary artifact stale (${AGE_LINE} min > ${MAX_CANARY_AGE_MIN} min)"
    else
      pass "canary artifact freshness OK (${AGE_LINE} min)"
    fi
  else
    warn "unable to parse canary timestamp"
  fi
else
  warn "canary artifact missing: $CANARY_FILE"
fi

echo
if [[ $FAIL -gt 0 ]]; then
  echo "RESULT: RED ($FAIL hard failure(s), $WARN warning(s))"
  exit 1
fi

echo "RESULT: GREEN (0 hard failures, $WARN warning(s))"
exit 0
