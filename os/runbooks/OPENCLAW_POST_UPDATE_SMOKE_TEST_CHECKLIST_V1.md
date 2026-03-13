# OpenClaw Post-Update Smoke Test Checklist v1

Status: Active runbook
Owner: Lyra Operations
Date: 2026-03-13

## Purpose
Catch obvious regressions immediately after an OpenClaw update, with special attention to local memory search and Codex/ACP workflows.

## When to use
Run this checklist after:
- `gateway.update.run`
- `openclaw update`
- manual npm reinstall/upgrade of OpenClaw
- dependency repairs that may affect runtime behavior

## Short rule
Do not treat an OpenClaw update as complete until this checklist passes or known failures are explicitly logged in the error/improvement system.

## Checklist

### 1. Confirm runtime is back and on the expected version
Run:

```bash
openclaw status
```

Verify:
- gateway is reachable
- service is running
- reported version matches the intended updated version
- no obvious memory/channel/runtime failure is shown in status

### 2. Check memory search availability
Run a minimal memory search.

Expected result:
- `memory_search` returns results or an empty result set without being marked unavailable
- if local memory is configured, confirm it resolves with the expected local provider/model

If memory search is unavailable:
- treat it as a failed smoke test
- inspect memory provider config and embedding dependency state
- if using local embeddings, specifically check `node-llama-cpp`

### 3. Check Codex / ACP path
Run one lightweight Codex/ACP smoke test in the path we actually depend on.

Examples:
- confirm an ACP/Codex session starts successfully
- confirm a short prompt returns a final visible reply
- confirm the session survives/reconciles correctly after restart if that is the current risk area

Expected result:
- no immediate provider/runtime failure
- final assistant reply is delivered correctly

### 4. Check logs only if something failed or looks suspicious
Run only as needed:

```bash
openclaw logs --plain --limit 200
```

Look for:
- memory / embedding failures
- provider/auth failures
- session restore / ACP errors
- repeated retries or duplicated delivery behavior

### 5. If any step fails
Do all of the following:
- classify the issue
- create/update the proper error artifact
- record immediate mitigation
- assign corrective and preventive action
- do not stop at a daily memory note

## Local-memory note
If `agents.defaults.memorySearch.provider = "local"`, verify that the local embedding runtime is still available after the update.

Current known risk:
- `node-llama-cpp` may not be present after some update paths because it is optional rather than guaranteed by the main OpenClaw package install.

## Minimum completion standard
An update is considered operationally complete only when:
- `openclaw status` looks healthy
- memory search is available
- one Codex/ACP smoke test succeeds
- any failures are routed into the formal error/improvement loop
