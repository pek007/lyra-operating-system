# CROSS_RUNTIME_INBOX_CHECK_CRON_DESIGN_V0_1.md

Status: Active draft v0.1  
Owner: Lyra via Control Panel  
Date: 2026-03-10

## Purpose
Define the first minimal cron-backed inbox check design for cross-runtime handoffs.

This design is intentionally narrow:
- one side first
- review/respond discipline only
- no automatic execution of payloads
- no plugin work

## Recommended first side
**Lyra OS side first**

Reason:
- safer to iterate here
- easier visibility into current handoff artifacts/register
- lower disruption risk than changing both sides at once
- enough to validate pickup, validation, status handling, and noise behavior

## Loop name
**OS cross-runtime inbox review loop**

## Scope of v0.1
The loop should:
1. scan OS `handoffs/incoming/`
2. identify new/unhandled handoffs
3. validate minimum required fields and payload presence
4. decide only one of:
   - valid and ready for manual review/respond
   - invalid / correction needed
   - expired
5. update register/status
6. optionally emit one concise summary only when something actionable exists

The loop should **not**:
- execute the payload automatically
- fabricate missing context
- reply conversationally without durable artifact output
- reprocess handled artifacts

## Recommended cadence
- every **30 minutes** initially

Reason:
- low enough to avoid noise
- frequent enough to remove routine courier dependency
- can be tightened later only if traffic proves the need

## Inputs
- `handoffs/incoming/`
- local handoff register
- local clock/time for expiry checks

## Validation checklist
A handoff is valid only if it has:
- `handoff_id`
- `from_domain`
- `to_domain`
- `owner`
- `purpose`
- `checksum`
- `approved_by`
- visible payload when payload is required

If missing any of the above:
- mark as `Rejected` or `Correction needed`
- do not process further

## Suggested status handling
### Open
- newly seen and valid but not yet processed

### Consumed
- reviewed and explicitly handled by local runtime with response artifact created

### Rejected
- invalid or missing required material

### Expired
- expiry date passed before handling

### Archived
- closed and retained only for audit

## Minimal handled-state rule
The loop must have a deterministic way to avoid duplicate processing.

Recommended v0.1 approach:
- maintain status in the handoff register
- treat any non-`Open` status as not eligible for reprocessing

Optional later improvement:
- sidecar marker file or move-to-subfolder convention

## Output behavior
The loop should normally stay silent.

Only emit output when:
- a new valid handoff requires attention
- a handoff is invalid/rejected
- a handoff expired

Allowed output shape:
- one concise summary with:
  - handoff ID
  - status
  - reason/action needed
  - artifact refs

## Durable artifacts produced
At v0.1, the cron loop itself may update:
- handoff register status
- optional evidence/log note if repeated invalid or expired artifacts become a pattern

It should **not** create full response artifacts unless the actual runtime review/handling step occurs.

## Escalation rules
Escalate rather than guess when:
- payload is missing but envelope is otherwise valid
- approval or ownership is ambiguous
- the handoff appears to cross the wrong boundary
- the same artifact repeatedly fails validation

## Success criteria
The first loop is successful if:
1. new handoffs are detected reliably
2. invalid/expired handoffs are surfaced clearly
3. no duplicate reprocessing occurs
4. output remains low-noise
5. humans no longer need to act as routine inbox checkers on that side

## Failure signals
- repeated duplicate handling
- noisy summaries with little value
- hidden dependency on manual inspection to know what changed
- unclear status ownership in the register
- pressure to automate payload execution too early

## Recommended next step after v0.1 design
If approved:
1. decide exact register status format and ownership
2. define whether `Correction needed` is a separate status or maps to `Rejected`
3. implement the first cron loop on Lyra OS side only
4. observe behavior before mirroring to PX

## Bottom line
The first cron-backed cross-runtime inbox check should be:
- **Lyra OS side only**
- **30-minute cadence**
- **review/respond discipline only**
- **register-status based duplicate prevention**
- **no automatic payload execution yet**

## Version
- v0.1
- Date: 2026-03-10
