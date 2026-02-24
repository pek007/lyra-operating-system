# CRON_SPEC_DAILY_HYGIENE.md

## Purpose
Daily automated hygiene check to detect configuration drift, channel failures, and security posture issues early.

## Scope
Run two checks and deliver a compact summary:
1. `openclaw doctor --non-interactive`
2. `openclaw security audit --json`

## Recommended Schedule
- Time: **08:30 Europe/Stockholm** (before main work block)
- Session mode: **isolated**
- Delivery: **announce to Telegram (Peter)**

## Output Format (compact)
1. Executive status: OK / Warning / Critical
2. Top issues (max 5)
3. Recommended actions (max 3)
4. Changes vs previous run (if known)

## Job Prompt (for isolated cron)
"Run daily hygiene checks for OpenClaw health and security. Use `openclaw doctor --non-interactive` and `openclaw security audit --json`. Summarize in 4 sections: (1) status, (2) top issues, (3) recommended actions, (4) what changed since last run if detectable. Keep concise and action-oriented."

## CLI Example (create job)
```bash
openclaw cron add \
  --name "Daily OpenClaw hygiene check" \
  --cron "30 8 * * *" \
  --tz "Europe/Stockholm" \
  --session isolated \
  --thinking low \
  --announce \
  --channel telegram \
  --to "8283124284" \
  --message "Run daily hygiene checks for OpenClaw health and security. Use openclaw doctor --non-interactive and openclaw security audit --json. Summarize: status, top issues, recommended actions, changes vs previous run."
```

## Guardrails
- Never auto-apply fixes without approval.
- For critical findings, escalate immediately.
- Keep output short; link details only if needed.

## Version
- v1.0
- Date: 2026-02-24
