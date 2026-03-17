#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ARTIFACT_DIR="$ROOT_DIR/knowledge/evidence/2026-03"
ARTIFACT_PATH="$ARTIFACT_DIR/tde-release-guard-latest.txt"
mkdir -p "$ARTIFACT_DIR"

{
  echo "[tde-release-guard] started: $(date -u +%FT%TZ)"
  "$ROOT_DIR/tools/tde-release-guard.sh"
  echo "[tde-release-guard] completed: $(date -u +%FT%TZ)"
} | tee "$ARTIFACT_PATH"
