# CADENCE_GOVERNANCE_POLICY.md

## Purpose
Prevent human-team timeline assumptions from degrading execution pace or reducing operational cadence.

## Core Rule
Plan by **throughput and dependencies**, not by default calendar pacing (weeks/months), unless there is an external deadline.

## Planning Standard (default)
For every initiative, define:
1. Priority
2. Dependencies
3. Risk level
4. Required cadence class

Use cadence classes:
- **Continuous** (multiple times/day)
- **Daily**
- **3x/week**
- **Weekly**
- **Monthly**

## Recurring Activity Guardrails
Every recurring process must explicitly include:
- **Minimum safe cadence** (floor)
- **Target cadence**
- **Downgrade trigger** (what evidence permits lower frequency)
- **Upgrade trigger** (what evidence requires higher frequency)

### Hard rule
No cadence downgrade (e.g., daily → weekly) without explicit Peter approval.

## Language Rule
In plans and strategy docs:
- Prefer: "next iterations", "next execution cycle", "after dependency X"
- Avoid defaulting to: "next month/quarter" unless date-bound by external constraints.

## Scheduler Governance
Before creating/editing cron jobs, check:
1. Is this cadence tied to risk detection latency?
2. If yes, set minimum safe cadence and keep it explicit in prompt/docs.
3. Does faster delivery create unacceptable noise/churn?
4. If not, prefer higher cadence with tighter guardrails.

## Current Standard for Autonomous Sweeps
- `healthcheck:security-audit`
  - Minimum safe cadence: **Daily**
  - Target cadence: **Daily (02:10 Europe/Stockholm)**
- `continuous-improvement:sweep`
  - Minimum safe cadence: **3x/week**
  - Target cadence: **Daily (03:20 Europe/Stockholm)**

## Decision Logging
Cadence decisions must be logged in:
- `CRON_SPEC_AUTONOMOUS_GOVERNANCE_SWEEPS.md` (job-level)
- `TASKS.md` (if scope or cadence changes)
- `PROCESS_REGISTRY.md` (policy/register updates)

## Version
- v1.0
- Date: 2026-02-26
- Owner: Peter/Lyra
