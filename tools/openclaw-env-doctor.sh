#!/usr/bin/env bash
set -euo pipefail

# OpenClaw environment doctor
# Purpose: quickly detect context/mount drift before meaningful work.

STRICT=0
REPO_NAME="lyra-operating-system"
WORKSPACE_DIR="${OPENCLAW_WORKSPACE_DIR:-$HOME/.openclaw/workspace}"
REPO_DIR=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --strict) STRICT=1; shift ;;
    --repo) REPO_NAME="${2:-}"; shift 2 ;;
    --workspace) WORKSPACE_DIR="${2:-}"; shift 2 ;;
    *) echo "Unknown arg: $1"; exit 2 ;;
  esac
done

REPO_DIR="$WORKSPACE_DIR/repos/$REPO_NAME"
TMP_DIR="${TMPDIR:-/tmp}/openclaw-env-doctor"
mkdir -p "$TMP_DIR"
EXPLAIN_JSON="$TMP_DIR/sandbox-explain.json"
LIST_JSON="$TMP_DIR/sandbox-list.json"

pass() { echo "[PASS] $*"; }
warn() { echo "[WARN] $*"; }
fail() { echo "[FAIL] $*"; FAILURES=$((FAILURES+1)); }

FAILURES=0
WARNS=0

echo "== OpenClaw Env Doctor =="
echo "workspace: $WORKSPACE_DIR"
echo "repo:      $REPO_DIR"
echo

# 1) Core binaries
if command -v openclaw >/dev/null 2>&1; then
  pass "openclaw CLI found: $(command -v openclaw)"
else
  fail "openclaw CLI missing"
fi

if command -v git >/dev/null 2>&1; then
  pass "git found: $(git --version 2>/dev/null || echo present)"
else
  fail "git missing"
fi

# 2) Host path checks
[[ -d "$WORKSPACE_DIR" ]] && pass "workspace dir exists" || fail "workspace dir missing"
[[ -d "$WORKSPACE_DIR/repos" ]] && pass "workspace repos dir exists" || fail "workspace repos dir missing"
[[ -d "$REPO_DIR" ]] && pass "target repo dir exists" || fail "target repo dir missing"
[[ -d "$REPO_DIR/.git" ]] && pass "target repo .git exists" || fail "target repo .git missing"

# 3) OpenClaw sandbox state checks (best effort)
SANDBOX_MODE="unknown"
if command -v openclaw >/dev/null 2>&1; then
  if openclaw sandbox explain --json > "$EXPLAIN_JSON" 2>/dev/null; then
    pass "captured sandbox explain JSON"
    SANDBOX_MODE=$(python3 - <<'PY' "$EXPLAIN_JSON"
import json,sys
p=sys.argv[1]
try:
  d=json.load(open(p))
  mode=None
  if isinstance(d,dict):
    # current schema
    if isinstance(d.get('sandbox'),dict):
      mode=d['sandbox'].get('mode')
    # fallbacks for schema drift
    if mode is None:
      mode=d.get('mode')
    if mode is None and isinstance(d.get('effective'),dict):
      mode=d['effective'].get('mode')
  print(mode or 'unknown')
except Exception:
  print('unknown')
PY
)
  else
    warn "could not run 'openclaw sandbox explain --json'"
    WARNS=$((WARNS+1))
  fi

  if openclaw sandbox list --json > "$LIST_JSON" 2>/dev/null; then
    pass "captured sandbox list JSON"
  else
    warn "could not run 'openclaw sandbox list --json'"
    WARNS=$((WARNS+1))
  fi
fi

echo "sandbox mode (detected): $SANDBOX_MODE"

# 4) Docker dependency check when sandbox likely enabled
if [[ "$SANDBOX_MODE" != "off" && "$SANDBOX_MODE" != "unknown" ]]; then
  if command -v docker >/dev/null 2>&1; then
    if docker version >/dev/null 2>&1; then
      pass "docker available (required by sandbox mode=$SANDBOX_MODE)"
    else
      fail "docker CLI found but daemon unavailable"
    fi
  else
    fail "docker missing while sandbox mode=$SANDBOX_MODE"
  fi
fi

# 5) Runtime path hint
if [[ -d "/workspace" ]]; then
  if [[ -d "/workspace/repos/$REPO_NAME" ]]; then
    pass "runtime path /workspace/repos/$REPO_NAME visible"
  else
    warn "runtime /workspace exists but repo path missing (possible mount mismatch)"
    WARNS=$((WARNS+1))
  fi
else
  warn "runtime path /workspace not present in this shell (normal on host shell)"
  WARNS=$((WARNS+1))
fi

echo
if [[ $FAILURES -eq 0 ]]; then
  echo "RESULT: GREEN (no hard failures)"
  [[ $WARNS -gt 0 ]] && echo "NOTES: $WARNS warning(s)"
  exit 0
fi

echo "RESULT: RED ($FAILURES hard failure(s), $WARNS warning(s))"
if [[ $STRICT -eq 1 ]]; then
  exit 1
fi
exit 1
