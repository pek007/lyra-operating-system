# OVERNIGHT_LOOP_LEDGER_CONTRACT_V1.md

Status: Active
Owner: Improvement
Date: 2026-03-23

## Purpose
Define the minimum canonical ledger record for one overnight loop run.

This ledger exists only to answer:
1. Did the loop run?
2. Did it help?
3. Can we verify what happened?

It is intentionally small.

## Ledger scope
One ledger record per night should cover the full loop:
- product learn-and-replan passes
- portfolio input consolidation
- portfolio decide-and-kickoff
- overnight execution loop
- morning executive brief

## Canonical location
Default location:
- `control/runtime/overnight-ledger/YYYY-MM-DD.json`

If the implementation later changes, keep one stable canonical pointer from the overnight loop standard.

## Minimum schema

```json
{
  "date": "YYYY-MM-DD",
  "loop": "overnight",
  "status": "success|partial|failed",
  "stages": [
    {
      "stage": "overnight:governance-learn-and-replan",
      "status": "success|failed|partial|skipped",
      "output": "path-or-object-reference",
      "contribution": "advanced_priority|reduced_blocker|improved_understanding|prepared_next_step|no_meaningful_movement",
      "blocker": "optional short note"
    }
  ],
  "portfolio_summary": {
    "selected_priority": "short identifier or note",
    "contribution": "advanced_priority|reduced_blocker|improved_understanding|prepared_next_step|no_meaningful_movement",
    "blocker": "optional short note"
  },
  "executive_brief": "path-or-message-reference"
}
```

## Field rules
- `date`: overnight date in local operating timezone.
- `loop`: fixed value `overnight`.
- `status`: overall loop result.
  - `success` = loop ran end-to-end without material control break
  - `partial` = some meaningful part ran but there was an interruption/failure/gap
  - `failed` = the loop did not complete in a usable way
- `stages`: one compact entry per major stage only.
- `output`: reference to the canonical artifact/object/message for that stage.
- `contribution`: choose one primary contribution classification only.
- `blocker`: only when useful; keep short.
- `portfolio_summary.selected_priority`: the main overnight-selected priority or the clearest equivalent summary.
- `executive_brief`: reference to the final 06:00 summary artifact/message.

## Contribution meanings
- `advanced_priority` — moved a current priority forward materially
- `reduced_blocker` — lowered or clarified a blocker/risk in a meaningful way
- `improved_understanding` — produced useful learning that changed understanding, planning, or options
- `prepared_next_step` — made the next action clearer/readier even if no major advancement occurred
- `no_meaningful_movement` — activity happened but did not materially help

## Control intent
The ledger is not a narrative report.
It is a compact control record for:
- weekly review,
- failure inspection,
- stuckness detection,
- and audit/debug follow-up.

## Implementation guidance
- Prefer one write per night after the 06:00 brief when possible.
- If written incrementally, keep updates additive and stable.
- Do not duplicate large report contents inside the ledger; link instead.
- If a stage does not run, record `skipped` or `failed` rather than omitting it silently.
