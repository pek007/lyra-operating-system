# Agent & Runtime Catalog v1

Date: 2026-02-28
Owner: Peter/Lyra
Status: Active

## Purpose
Define runtime roles and boundaries without binding jobs 1:1 to persistent agents.

## Runtime entries

### Main agent (Lyra)
- Role: Control Tower orchestration + governance + high-context execution
- Non-role: unmanaged high-risk external actions
- Default surface: primary sessions
- Escalation: major risk, trust boundary, external impact

### Supplier sub-agents
- Role: bounded implementation/research tasks
- Non-role: policy decisions, broad scope changes
- Default surface: spawned sub-agents/sessions
- Escalation: ambiguity, scope drift, policy conflict

### Future persistent specialists (only if approved)
- Conditions: durable tool/sandbox/model/routing/trust boundary divergence
- Entry requirement: `AGENT_DEPLOYMENT_DECISION_TEMPLATE.md` + Peter approval

## Job binding reference
See `JOB_MARKET_MODEL_V1.md` for job-to-runtime assignment.
