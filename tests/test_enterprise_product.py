import json
from fastapi.testclient import TestClient
from synergy_adaptive_engine.api import app
from synergy_adaptive_engine.enterprise.auth import sign_token
from synergy_adaptive_engine.enterprise.models import Role

SECRET="dev-only-change-me-not-for-production"

def token(role):
    return sign_token(SECRET,subject="fund-user",roles=[Role(role)],tenant_id="fund-a",ttl_seconds=3600)

def test_product_enterprise_endpoint_and_audit_linkage():
    c=TestClient(app)
    request_id="acceptance-123"
    res=c.post('/enterprise/v1/adaptive/update',json={'portfolio_id': 'demo', 'names': ['a', 'b', 'c'], 'rewards': [0.2, -0.1, 0.05], 'returns': [0.001, -0.001, 0.002, 0.0005, -0.0002, 0.001]},headers={"Authorization":"Bearer "+token('researcher'),"X-Request-ID":request_id})
    assert res.status_code==200, res.text
    body=res.json()
    for key in ['weights', 'regime', 'request_id']: assert key in body
    assert body["request_id"]==request_id
    admin=token("admin")
    audit=c.get('/enterprise/audit',headers={"Authorization":"Bearer "+admin})
    assert audit.status_code==200
    assert any(e["request_id"]==request_id for e in audit.json())

def test_product_endpoint_requires_authorized_role():
    c=TestClient(app)
    res=c.post('/enterprise/v1/adaptive/update',json={'portfolio_id': 'demo', 'names': ['a', 'b', 'c'], 'rewards': [0.2, -0.1, 0.05], 'returns': [0.001, -0.001, 0.002, 0.0005, -0.0002, 0.001]},headers={"Authorization":"Bearer "+token("viewer")})
    assert res.status_code==403

def test_api_exposes_enterprise_control_routes():
    paths={r.path for r in app.routes}
    assert '/enterprise/health' in paths
    assert '/enterprise/v1/adaptive/update' in paths
