# TDE cutover readiness artifact path fix

Date: 2026-03-06

## Problem
Cutover readiness automation used a hard-coded dated path (`2026-03-04__...`) as the write/read source, causing archival confusion and duplicate-content artifacts across dates.

## Fix
Updated scripts to use deterministic current-date + latest alias model:
- `tools/tde_cutover_readiness_report.py`
  - writes `knowledge/evidence/metrics/YYYY-MM-DD__tde-db-cutover-readiness-report-v1.json`
  - writes `knowledge/evidence/metrics/tde-db-cutover-readiness-report-latest.json`
  - includes `evidence.previous_report` linkage
- `tools/tde_daily_readiness_check.sh`
  - now only calls the report generator (no fragile hard-coded copy path)
- `tools/tde_cutover_alert_check.py`
  - reads `...-latest.json` (fallback to most recent dated artifact)

## Verification
- `bash tools/tde_daily_readiness_check.sh` -> pass
- `python3 tools/tde_cutover_alert_check.py` -> pass
- latest report now references prior dated report correctly.

## Impact
Readiness evidence chain is now stable and time-correct, enabling clean observation-window tracking toward Trello retirement gate.
