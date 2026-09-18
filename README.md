# SYNERGY Adaptive Engine

**Online champion/challenger strategy weighting with regime-aware adaptation and bounded updates**

Version: `2.0.0` · Python 3.11+ · REST API · Docker · CI · automated tests

## Why this exists
Static ensembles decay across regimes; uncontrolled online learning creates a different risk.

## Commercial buyer
Quant funds and prop teams using multiple strategies/models.

## Core guarantee
The software guarantees deterministic interface behavior covered by tests. **It does not guarantee trading profit.** Live-market deployment requires customer-specific OOS validation, fees/spread/slippage/latency/capacity modelling, security review and legal/compliance approval.

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest -q
python -m synergy_adaptive_engine.api
```

Then open `http://localhost:8000/docs`.

## Commercial package
- standalone installable Python package;
- versioned FastAPI boundary;
- deterministic reference core;
- Dockerfile and GitHub Actions CI;
- sales one-pager, security boundary, deployment notes and provenance;
- proprietary evaluation licence ready for a paid pilot.

## Research lineage
MQL5 RL / Cellular10K / adaptive graph research + MIDAS RL policy lineage

See `docs/PRODUCT_STATUS.md`, `docs/SALES_ONE_PAGER.md`, `docs/SECURITY.md` and `docs/PROVENANCE.md`.

## Enterprise v2.0.0

The repository now includes a separate enterprise boundary around the product core:

- JWT/RBAC roles (`viewer`, `researcher`, `trader`, `risk`, `operator`, `admin`);
- request-id propagation and auditable product actions;
- PostgreSQL and ClickHouse audit stores;
- Bybit V5, CCXT multi-CEX and MetaTrader 5 adapters with live execution disabled by default;
- retry/circuit breaker controls;
- health and Prometheus-compatible metrics;
- Docker Compose deployment reference;
- deterministic synthetic customer dataset and HTTP/k6 load harnesses.

See `docs/ENTERPRISE_ARCHITECTURE.md`, `docs/ENTERPRISE_DEPLOYMENT.md` and `docs/CUSTOMER_ACCEPTANCE.md` before any customer deployment.
