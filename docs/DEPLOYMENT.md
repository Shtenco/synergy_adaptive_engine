# Deployment

## Local
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e '.[dev]'
pytest -q
python -m synergy_adaptive_engine.api
```

## Docker
```bash
docker build -t synergy-adaptive-engine:2.0.0 .
docker run --rm -p 8000:8000 synergy-adaptive-engine:2.0.0
```

The default deployment is simulation/read-only. Add venue credentials only in a customer-controlled production secret store.
