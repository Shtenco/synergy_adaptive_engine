# Customer pilot — SYNERGY Adaptive Engine

## Objective
Demonstrate that the product can **update bounded strategy weights from reward evidence and classify the current return regime** inside the customer's environment under agreed identity, audit, risk and operational controls.

## Phases
**0 — Scope:** choose one desk/use case; freeze representative data, workload and pass/fail criteria.  
**1 — Isolated deployment:** pinned revision in dev/UAT; integrate identity, PostgreSQL audit and monitoring; live execution off.  
**2 — Functional evidence:** run `/enterprise/v1/adaptive/update`; verify roles, request ID, deterministic behavior where applicable and response fields **weights, regime, portfolio_id, request_id**.  
**3 — Resilience/performance:** target-hardware load tests plus timeout/429/5xx/DB outage/restart/rollback drills.  
**4 — Domain gate:** customer OOS/paper process with realistic fees/spread/slippage/latency/capacity where relevant.

Final report must record commit/image digest, configuration, tested identities/roles, functional pass/fail, benchmark evidence, unresolved risks and the customer decision: reject / extend research / paper / bounded canary / production review.

Passing a technology pilot does not imply alpha or future profitability.
