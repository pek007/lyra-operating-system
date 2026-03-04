# Tool & External Service Hardening Plan v1

Status: Active  
Owner: Peter (A), Lyra (R)

## Implemented now
1. Research report ingested and indexed.
2. Tool governance baseline doc created.

## Next high-leverage steps
1. Add CI checks: secret scanning + dependency review + policy checks for tool risk gates.
2. Add shared HTTP wrapper for external scripts (timeouts, retries, backoff, 429 handling).
3. Add structured audit logging format for external calls.
4. Enforce approval obligations for high-risk action families.

## Success criteria
- No external integration without evidence pack + risk class + rollback path.
- External calls are rate-limit safe and auditable.
- High-risk actions cannot execute without approval artifact.
