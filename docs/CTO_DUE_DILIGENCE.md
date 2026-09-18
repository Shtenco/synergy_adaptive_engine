# CTO due-diligence brief — SYNERGY Adaptive Engine v2.0.0

**Use case:** Bounded online strategy weighting and regime-aware adaptation for systematic portfolios.  
**Buyer:** Quant funds, prop firms, systematic portfolio teams and adaptive research desks.  
**Enterprise action:** `POST /enterprise/v1/adaptive/update` with roles **researcher, risk**.  
**Status:** enterprise technology / paid-pilot candidate; not customer-certified production infrastructure.

Implemented:
- installable Python 3.11+ package and FastAPI/OpenAPI;
- deterministic product core plus automated tests;
- JWT principal, tenant ID and RBAC;
- request-ID correlation and audit event path;
- PostgreSQL/ClickHouse audit layer;
- health/metrics, retry/circuit-breaker and deployment assets;
- Bybit V5 / CCXT / MetaTrader 5 integration contracts; live disabled by default.

Evidence: **20 tests passed**; local health smoke **80/80 HTTP 200**, p95 **91.1 ms** in this container.

Known boundaries: no independent security/regulatory certification; no universal production latency claim; no guarantee of venue fills, alpha, market impact or profitability; customer OIDC/JWKS, schemas, adapters and operations may require integration work.
