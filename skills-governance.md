# Skills Governance Policy (OpenClaw)

## Purpose
Enable skills safely while minimizing security, privacy, and operational risk.

## Scope
Applies to all installed skills (bundled, managed, workspace) and any included scripts/resources.

## Risk Classes
- **S0**: Documentation-only (no scripts, no credentials, no network)
- **S1**: Local tooling (no credentials; bounded filesystem)
- **S2**: Credentialed API/tool access (read/write)
- **S3**: Meta-tools/toolchains that can expand capability surface

## Default Rules
1. New skills default to **sandbox + disabled**.
2. No production enablement without a completed **Evidence Pack**.
3. No auto-update in production agents.
4. Every enabled skill must be version-pinned.
5. Secrets must not be stored in plaintext when avoidable.
6. Secrets must never be placed in prompts/logs.

## Mandatory Controls by Class

### S0
- Inspect
- Pin version
- Log installation

### S1
- Sandbox preferred
- Workspace/path allowlist
- Basic usage/error telemetry

### S2
- Sandbox required
- Least-privilege credentials/scopes
- Ephemeral secret injection
- Approval for write/destructive actions
- Outbound domain allowlist
- Cost/spend guardrails if external model/API usage

### S3
- Dedicated sandbox-only agent
- Strict tool/network allowlists
- Explicit approval for external calls and integrations
- No extension auto-installs
- Named owner sign-off before any promotion

## Action Gates (Always Approval-Required)
- Send email
- Create/update calendar events
- Merge PR / create release
- Bulk write or delete operations
- Add MCP server or new external integration
- Enable any skill in production agent profile

## Lifecycle Workflow
Discovery → Inspect → Risk classify (S0-S3) → Pin version → Sandbox tests → Evidence pack review → Approve/reject → Runtime monitoring → Periodic re-review → Decommission

## Monitoring Requirements
Track per skill:
- usage volume
- errors/failures
- denied risky actions
- cost (if external API/model usage)
- anomaly events

## Incident Handling
On suspected compromise:
1. Quarantine skill
2. Disable in policy/config
3. Stop related sessions/workflows
4. Revoke/rotate credentials
5. Capture evidence (logs, version, hashes, commands)
6. Assess impact (data, files, outbound calls)
7. Remediate and update guardrails

## Current Recommended Classification (Top 15)

| Skill | Class | State |
|---|---:|---|
| weather | S1 | enabled |
| model-usage | S1 | enabled |
| openai-whisper | S1 | enabled |
| summarize | S2 | enabled (guarded) |
| github | S2 | enabled (guarded) |
| gog | S2 | sandbox-evaluate |
| notion | S2 | sandbox-evaluate |
| obsidian | S1/S2* | sandbox-evaluate |
| nano-pdf | S1/S2* | sandbox-evaluate |
| self-improving-agent | S2 | sandbox-evaluate |
| sonoscli | S1 | restricted |
| nano-banana-pro | S2 | restricted |
| gemini | S3 | restricted |
| mcporter | S3 | restricted |
| skill-creator | S3 | restricted |

\* Final class depends on validated network/data behavior.
