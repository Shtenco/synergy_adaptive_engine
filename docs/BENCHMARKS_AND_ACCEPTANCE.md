# Benchmarks and acceptance — SYNERGY Adaptive Engine

Fresh verification:
- **20 automated tests passed**.
- Product endpoint: `/enterprise/v1/adaptive/update`.
- RBAC acceptance covers permitted-role success and `viewer` denial.
- Product actions are tested for request-ID/audit linkage.

Local smoke against `GET /enterprise/health`: **80/80 HTTP 200**, p50 **15.7 ms**, p95 **91.1 ms**, p99 **133.1 ms**, ~**454 req/s** at 80 requests / concurrency 16.

These are reproducible **health-endpoint smoke figures only**. They do not measure customer ingress, OIDC, PostgreSQL/ClickHouse, `/enterprise/v1/adaptive/update` workload, CEX/broker latency, fills, impact or profitability.

Customer acceptance gates:
1. Reproduce tests from a pinned revision.
2. Map customer IdP roles and prove denial paths.
3. Trace one request ID from API through the configured audit store.
4. Run target-hardware p50/p95/p99 with customer auth and databases.
5. Freeze customer-specific domain acceptance data/criteria before results.
6. Sandbox/paper before any venue canary.
7. Exercise timeout, 429/5xx, DB outage, restart, circuit open and rollback.
