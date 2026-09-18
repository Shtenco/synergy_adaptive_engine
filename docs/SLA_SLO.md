# Reference SLA / SLO framework — SYNERGY Adaptive Engine

This is a **contract starting point**, not an executed SLA or warranty.

| SLI | Reference target |
|---|---:|
| Enterprise API availability | 99.9% monthly |
| `/enterprise/health` p95 | <250 ms on accepted customer environment |
| Server-side 5xx rate | <0.1% |
| Audit correlation coverage | 100% accepted privileged product actions |
| Reference RTO | 30 min |
| Reference audit RPO | 5 min |

No universal latency promise is made for `/enterprise/v1/adaptive/update`; payload size and infrastructure materially change runtime. Customer pilot must define representative workload and accepted p50/p95/p99.

Venue latency, fills, spread, market impact and venue availability are external dependencies. A service SLO is not an execution-quality or profitability SLA.
