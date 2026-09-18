# API examples — SYNERGY Adaptive Engine

Base URL: `http://127.0.0.1:8000`.

Control endpoints:
- `GET /enterprise/health`
- `GET /enterprise/metrics`
- `GET /enterprise/whoami`
- `GET /enterprise/audit` (admin)

Primary action: `POST /enterprise/v1/adaptive/update` — roles **researcher, risk**.

Create a short-lived **evaluation-only** token:

```bash
export SYNERGY_AUTH_SECRET='replace-with-a-long-random-evaluation-secret'
export TOKEN=$(python - <<'PY'
import os
from synergy_adaptive_engine.enterprise.auth import sign_token
from synergy_adaptive_engine.enterprise.models import Role
print(sign_token(os.environ['SYNERGY_AUTH_SECRET'],subject='cto-evaluation',
    roles=[Role('researcher')],tenant_id='pilot-fund',ttl_seconds=900))
PY
)
```

Example request payload:
```json
{"portfolio_id":"demo","names":["a","b","c"],"rewards":[0.2,-0.1,0.05],"returns":[0.001,-0.001,0.002,0.0005,-0.0002,0.001]}
```

```bash
curl -sS -X POST 'http://127.0.0.1:8000/enterprise/v1/adaptive/update' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -H 'X-Request-ID: pilot-001' \
  -d @request.json
```

Expected response includes **weights, regime, portfolio_id, request_id**. Use `/docs` or `/openapi.json` as the canonical interface for the pinned revision.
