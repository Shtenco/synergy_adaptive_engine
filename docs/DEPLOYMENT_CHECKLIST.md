# Deployment checklist — SYNERGY Adaptive Engine

- [ ] Pin accepted commit and image digest; rerun `pytest -q`.
- [ ] Put API behind customer TLS ingress/service mesh.
- [ ] Integrate customer OIDC/mTLS/JWKS and least-privilege role mapping.
- [ ] Store JWT/DB/venue secrets in KMS/secret manager.
- [ ] Restrict PostgreSQL/ClickHouse and venue egress at network level.
- [ ] Apply audit schemas; configure encryption, backup, retention and restore test.
- [ ] Exercise `/enterprise/v1/adaptive/update` with representative customer payload.
- [ ] Prove allowed roles **researcher, risk** and `viewer` denial.
- [ ] Validate `X-Request-ID` linkage into audit evidence.
- [ ] Scrape `/enterprise/metrics`; alert on 5xx, latency, circuit-open and audit failures.
- [ ] Run timeout, 429/5xx, DB outage and restart drills.
- [ ] Keep `SYNERGY_ALLOW_LIVE_EXECUTION=false` through evaluation.
- [ ] Obtain Trading + Risk + Ops + Security/Compliance approval before any live canary.
- [ ] Archive benchmark, security and acceptance evidence before production review.
