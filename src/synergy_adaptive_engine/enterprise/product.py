from __future__ import annotations
from threading import RLock
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from ..core import AdaptiveEnsemble, regime
from .models import Principal, Role
from .service import EnterpriseRuntime, principal_dependency, request_id_header

class UpdateRequest(BaseModel): portfolio_id:str; names:list[str]; rewards:list[float]; returns:list[float]
_states:dict[tuple[str,str],AdaptiveEnsemble]={};_lock=RLock()

def build_product_router(runtime:EnterpriseRuntime)->APIRouter:
    router=APIRouter(prefix="/enterprise/v1/adaptive",tags=["enterprise-adaptive"])
    @router.post("/update")
    async def update(req:UpdateRequest, principal:Principal=Depends(principal_dependency(runtime,{Role.RESEARCHER,Role.RISK})), request_id:str=Depends(request_id_header)):
        key=(principal.tenant_id,req.portfolio_id)
        with _lock:
            engine=_states.get(key)
            if engine is None or engine.names!=req.names:
                engine=AdaptiveEnsemble(req.names);_states[key]=engine
            weights=engine.update(req.rewards)
        state=regime(req.returns)
        runtime.record(principal,action="adaptive.update",request_id=request_id,payload={"portfolio_id":req.portfolio_id,"weights":weights,"regime":state})
        return {"request_id":request_id,"portfolio_id":req.portfolio_id,"weights":weights,"regime":state}
    return router
