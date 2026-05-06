# Software Factory Worker Result Contract v0

Status: active v0 / Phase 3 MVP integrated
Factory run ID: `SF-ORCH-2026-05-06-EPHEMERAL-DISPATCH-MVP`
Owner/reviewer: Peter Eklind / Lyra Operations
Scope: ephemeral Software Factory workers returning integration-ready results
Source run: `workspaces/software-factory/dry-runs/2026-05-06-ephemeral-dispatch-mvp/`
Integrated from ephemeral Architect, Builder, and Gatekeeper worker results on 2026-05-06.


## Purpose

This contract defines the minimum result shape every ephemeral Software Factory worker must return so an Integrator can safely combine role outputs without replaying the worker's full context.

It applies to Architect, Builder, Verifier, Gatekeeper, Integrator-support, and comparable bounded worker roles.

## Worker Result File

Each worker must write one Markdown result file at the path assigned in its role packet. The file must be self-contained and concise.

Required top-level fields:

```markdown
# <Role> Result

Status: pass | issue | blocked | decision-needed | not-run
Factory run ID: `<run-id>`
Role: <Architect | Builder | Verifier | Gatekeeper | Integrator | other>
Assigned packet: `<relative-path-to-role-packet>`
Result timestamp: <ISO-8601 or local timestamp with timezone>

## Summary
- <1-5 bullets describing what changed, found, or verified>

## Changed Files
- `<relative-path>` — <created | modified | deleted | none>; <brief purpose>

## Evidence
- <command, file inspection, diff, test, review, or other concrete evidence>

## Validation
- Command: `<exact command run>`
- Result: pass | fail | not-run
- Notes: <short output summary, failure reason, or why not run>

## Blockers / Risks
- <none, or explicit blocker/risk with owner/needed decision if known>

## Authority Boundary
- <confirmation that no prohibited action was taken, or explicit exception/blocker>

## Recommended Integration State
State: integrate | needs-review | needs-fix | blocked | reject
Reason: <one sentence>

## Handoff Notes
- <optional concise notes for the next actor>
```

## Field Semantics

### Status

- `pass`: assignment completed and validation/evidence supports integration.
- `issue`: assignment completed but non-blocking defects, gaps, or risks remain.
- `blocked`: assignment could not proceed without missing input, access, authority, or prohibited action.
- `decision-needed`: worker reached a bounded decision point requiring human or owning-lane judgment.
- `not-run`: worker performed no substantive work; explain why.

### Changed Files

- List every file created, modified, or deleted by the worker.
- Use relative paths from `/Users/lyra/.openclaw/workspace` unless the role packet says otherwise.
- If no files changed, write `- none — no file changes made`.
- Do not list files only read as changed files.

### Evidence

Evidence must be concrete enough for another worker to verify the claim quickly. Prefer:

- exact validation commands and summarized results;
- relevant file paths and sections inspected;
- generated artifacts and their locations;
- explicit comparison against acceptance criteria;
- concise failure excerpts when validation fails.

Avoid vague evidence such as "looks good" without a command, file, or inspection basis.

### Validation

- Run only validation commands allowed by the role packet or owning lane.
- Preserve the exact command string.
- If validation is not run, state `Result: not-run` and explain the constraint.
- A failing validation does not automatically mean the result is unusable, but it must set `Status: issue` or `blocked` unless clearly unrelated.

### Blockers / Risks

Use `Blockers / Risks` to distinguish:

- **Blocker:** prevents completion or safe integration now.
- **Risk:** does not prevent integration but needs follow-up, review, or monitoring.
- **Decision needed:** a human or owning product lane must choose between acceptable options.

Each blocker should name the missing input, authority, or next actor when known.

### Authority Boundary

Workers must not exceed their role packet. The result must explicitly state whether the worker avoided:

- credentials or access changes;
- external sends or client communications;
- deploy, release, push, merge, or persistent agent creation;
- destructive cleanup;
- mutation of prohibited products, customer data, or operational systems.

If useful work would require a prohibited action, stop and return `Status: blocked` or `decision-needed`.

### Recommended Integration State

The worker recommends, but does not authorize, the next state:

- `integrate`: safe for Integrator to include as-is.
- `needs-review`: human/reviewer or another role should inspect before integration.
- `needs-fix`: another worker should revise before integration.
- `blocked`: integration cannot proceed until blocker is resolved.
- `reject`: output should not be used; explain why.

Final authority remains with the human owner/reviewer and designated integration gate. Worker recommendations are advisory only.

## Integration Requirements

An Integrator may consume a worker result when:

1. the result file exists at the assigned path;
2. all required sections are present;
3. changed files are inside the worker's allowed scope;
4. evidence and validation are specific enough to inspect;
5. blockers, risks, and authority boundaries are explicit;
6. the recommended integration state is stated with a reason.

If any requirement is missing, the Integrator should mark the worker result `needs-fix`, `needs-review`, or `blocked` rather than inferring unstated facts.
