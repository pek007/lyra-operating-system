# Software Factory Real Delivery Dispatch Rep Friction Summary

Status: completed / no automation trigger
Date: 2026-05-06
Source run: `workspaces/software-factory/dry-runs/2026-05-06-real-delivery-dispatch-rep/`
Source evidence: `control/execution-evidence/software-factory-real-delivery-dispatch-rep-2026-05-06.md`

## Summary
This run intentionally held automatic git worktree/branch creation and used the existing lock-manifest + isolated-copy discipline. No blocker or major rework was observed from the manual isolated-copy approach during this bounded run.

## Observed friction
| Area | Observation | Automation relevance |
| --- | --- | --- |
| Intake setup | One schema enum was invalid (`human_approved_recommendation`) and was corrected to an allowed `chat_message` value before ingest. | Not worktree-related; schema discipline/process issue only. |
| Lock gate | Timestamped pre-dispatch lock gate ran cleanly and was easy to preserve. | No automation need. |
| Isolated-copy setup | Manual isolated-copy artifact paths were sufficient for two small Delivery artifacts. | No immediate automation trigger. |
| Integration | Exact-copy adoption and hash attribution remained straightforward. | No immediate automation trigger. |

## Decision signal
State: keep-manual
Reason: This additional real Delivery rep did not show enough worktree/setup friction to justify automatic git worktree creation yet.

## Next use
Use `products/delivery/06-architecture/SOFTWARE_FACTORY_PARALLEL_DISPATCH_FRICTION_LOG_V0.md` after the next real parallel dispatch to collect stronger evidence before revisiting automation.
