from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from .core import regime
app=FastAPI(title='SYNERGY Adaptive Engine',version='2.0.0')
class Req(BaseModel):returns:list[float]
@app.get('/health')
def health():return {'ok':True,'service':'adaptive-engine'}
@app.post('/v1/regime')
def reg(req:Req):return {'regime':regime(req.returns)}

# Enterprise v2 control/data plane
from .enterprise.service import EnterpriseRuntime, build_enterprise_router, install_observability
from .enterprise.product import build_product_router
enterprise_runtime=EnterpriseRuntime.from_env(service_name='synergy-adaptive-engine')
install_observability(app,enterprise_runtime)
app.include_router(build_enterprise_router(enterprise_runtime))
app.include_router(build_product_router(enterprise_runtime))

if __name__=='__main__':uvicorn.run(app,host='0.0.0.0',port=8000)
