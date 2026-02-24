#!/usr/bin/env bash
set -euo pipefail
source ~/.openclaw/.secrets/trello.env
cd /Users/lyra/.openclaw/workspace
python3 tools/trello_sync.py --from TASKS.md --ensure-labels --apply
