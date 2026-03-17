#!/usr/bin/env bash
set -euo pipefail
source ~/.openclaw/.secrets/trello.env
cd /Users/lyra/.openclaw/workspace
python3 tools/trello_sync.py --from os/runtime/TASKS_from_db.md --ensure-labels --apply
