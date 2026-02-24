# GOV-001: Retention & Access Baseline

## Purpose
Set minimum rules for what we keep, who can access it, and for how long.

## Data Handling Principles
1. Keep only what is needed (minimization)
2. Retain only as long as necessary
3. Restrict access to least privilege
4. Document sensitive decisions and exceptions

## Data Categories (v1)
- **Operational docs:** policies, SOPs, runbooks, registries
- **Work artifacts:** drafts, deliverables, notes
- **Sensitive client data:** confidential business/personal info
- **Credentials/secrets:** API keys, tokens, auth data

## Retention Baseline
- Operational docs: retain while active + archive historical versions
- Work artifacts: retain per business need; review quarterly
- Sensitive client data: retain only when necessary for active engagement/obligations
- Credentials/secrets: never store in plain-text docs; rotate when exposed/suspected exposed

## Access Baseline
- Primary access: Peter + Lyra environment only
- Share externally only when explicitly approved
- In group/shared channels: never disclose private context by default

## Secret Handling Rules
- Do not paste secrets into long-term docs
- If secret is shared in chat, treat as exposed and rotate
- Prefer managed auth/config storage over manual plaintext handling

## Review Cadence
- Monthly review of retention/access practices
- Immediate review after any incident involving data or credentials

## Evidence
- Record exceptions and major changes in `DECISIONS.md`
- Reflect active risks in `RISK_REGISTER.md`

## Version
- v1.0
- Date: 2026-02-24
