# TDE Use Case — Progress Transparency Monitoring v1

Date: 2026-03-02
Source: Peter meta-note in Lyra Operations

## Problem
Delegation and autonomous execution improve throughput, but owner visibility can lag. This creates ambiguity between:
- true stall (no meaningful progress), and
- active background execution (progress happening but not visible).

## Use-case objective
Provide owner-facing progress transparency that makes execution state legible at a glance.

## Expected capability (later-stage TDE)
- Progress indicators per active workstream (e.g., checklist completion, milestone phase, evidence count)
- Confidence signal: `On track / At risk / Stalled`
- Last meaningful activity timestamp and next expected checkpoint
- Stall detector reason codes (waiting-on-approval, blocked-by-dependency, retrying, etc.)

## OpenClaw-native implementation direction
- Heartbeat summaries for periodic progress snapshots
- Cron-driven status snapshots for deterministic intervals
- Session/tool event-derived progress counters, not manual reporting only

## Acceptance criteria candidates
1. Every active high-priority workstream has a machine-readable progress state.
2. Owner can distinguish `active-background` vs `stalled` without asking in chat.
3. Any item classified `stalled` auto-triggers anti-stall pathway (resume/escalate/redefine/retire).

## Product impact
Add this as a first-class TDE observability use-case and tie it to milestone dashboard/reporting artifacts.
