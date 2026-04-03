# Lyra OS Prompt Injection Posture — Brief

Date: 2026-04-03
Status: reusable brief

## Bottom line
Lyra OS should treat prompt injection as an ongoing, unsolved risk in any workflow that ingests untrusted content and can take meaningful actions.

## Recommended posture
- assume external content can contain hidden instructions
- treat consequence reduction as equally important as detection
- use layered defenses, not single mitigations
- keep agent authority narrow by default
- require approval for high-risk actions
- prefer bounded workflows over broad autonomy where practical

## Most relevant risk areas
- browser and web-fetch flows
- external documents and files
- RAG/retrieved content
- tool-using agents with messaging, file writing, or execution powers

## Practical implication
The safest default is not “trust the model more.” It is:
- stronger boundaries
- lower privilege
- tighter approval gates
- better trust labeling for external content
- ongoing testing and monitoring
