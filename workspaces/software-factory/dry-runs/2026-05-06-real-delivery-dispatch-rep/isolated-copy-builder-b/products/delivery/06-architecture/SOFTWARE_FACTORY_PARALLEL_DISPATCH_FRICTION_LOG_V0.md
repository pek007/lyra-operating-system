# Software Factory Parallel Dispatch Friction Log v0

Status: template / Builder B draft
Factory run ID: `SF-ORCH-2026-05-06-REAL-DELIVERY-DISPATCH-REP`
Owner/reviewer: Peter Eklind / Lyra Operations
Scope: capture friction during bounded parallel Software Factory dispatch and decide whether automatic worktree creation is justified.

## Purpose

Use this log after each parallel dispatch run to record real operator friction, separate tooling gaps from authority decisions, and make a bounded recommendation on whether future runs should automate worktree creation.

## Friction Entry

| Field | Notes |
| --- | --- |
| Run ID | `<factory-run-id>` |
| Timestamp | `<local timestamp + timezone>` |
| Reporter / Role | `<orchestrator, builder, verifier, integrator, other>` |
| Dispatch Step | `<pre-dispatch gate, packet handoff, isolated-copy setup, validation, integration, other>` |
| Friction Type | `<delay, ambiguity, path conflict, manual setup, validation gap, authority boundary, tooling error>` |
| What happened | `<1-3 sentence factual description>` |
| Impact | `<none, minor delay, major delay, rework, blocked dispatch, unsafe-to-continue>` |
| Evidence | `<file path, command output, result file, or short excerpt>` |
| Immediate workaround | `<manual step used, or none>` |
| Follow-up owner | `<role/person/lane>` |

## Automatic Worktree Creation Decision Check

Answer after reviewing all friction entries for the run.

| Question | Yes / No / Unknown | Evidence |
| --- | --- | --- |
| Did manual isolated-copy or worktree setup cause repeated delay or rework? |  |  |
| Did builders need stronger filesystem isolation than assigned write scopes provided? |  |  |
| Did any friction come from ambiguous paths that automation could derive safely from the manifest? |  |  |
| Did the pre-dispatch lock check pass before builder work began? |  |  |
| Can automation be limited to declared worker IDs, branches, worktree paths, and write scopes? |  |  |
| Would automation avoid credentials/access changes, deploy/release/push/merge, persistent agents, and prohibited product mutation? |  |  |
| Is there a rollback path if automatic setup fails before worker dispatch? |  |  |
| Is human/integrator authority still required before root artifact integration? |  |  |

## Recommendation

State: `keep-manual | pilot-automation | automate-by-default | decision-needed | reject-automation`

Reason: `<one sentence tied to observed friction and authority boundary>`

Required guardrails if piloting or automating:
- Use only a passed pre-dispatch lock manifest as input.
- Create only declared worker paths; do not infer extra scopes.
- Fail closed on duplicate IDs, overlapping write scopes, unsafe paths, or missing result paths.
- Do not push, merge, deploy, release, change access, mutate customer/product systems, or edit root final artifacts.
- Preserve worker result files and validation evidence for integrator review.

## Run Summary

- Total friction entries: `<n>`
- Blocking friction entries: `<n>`
- Automation-relevant entries: `<n>`
- Non-automation process fixes: `<short list or none>`
- Final recommended next action: `<short action>`
