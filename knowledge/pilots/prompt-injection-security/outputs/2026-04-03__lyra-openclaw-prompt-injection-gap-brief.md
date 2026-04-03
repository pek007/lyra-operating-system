# Lyra/OpenClaw Prompt Injection Gap Brief

Date: 2026-04-03
Status: reusable brief

## Bottom line
Lyra/OpenClaw is not starting from zero, but current posture is only partially aligned with the prompt-injection defense stance we want.

## Main strengths
- high-risk actions are conceptually approval-gated
- untrusted external content is increasingly treated as untrusted
- sandboxing/containment exists in the platform model

## Main gaps
- at least one runtime still has broad exec trust (`security=full`)
- shared/multi-user trust-boundary risk remains live
- no formal prompt-injection control checklist yet
- browser/tool/action-rich workflows create real indirect prompt-injection exposure

## Most important conclusion
The biggest practical risk is not just reading malicious content — it is reading malicious content in a runtime that also has broad authority and meaningful action channels.

## Recommended next move
Create a concrete Lyra OS prompt injection control checklist and review the highest-blast-radius tool/runtime paths against it.
