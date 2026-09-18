from __future__ import annotations
from dataclasses import dataclass
import numpy as np

@dataclass
class AdaptiveEnsemble:
    names:list[str]
    eta:float=.25
    max_step:float=.15
    def __post_init__(self):
        if not self.names:raise ValueError('at least one strategy required')
        self.weights=np.ones(len(self.names),dtype=float)/len(self.names)
    def score(self,signals:list[float])->float:
        s=np.asarray(signals,float)
        if len(s)!=len(self.weights):raise ValueError('signal length mismatch')
        return float(self.weights@s)
    def update(self,rewards:list[float]):
        r=np.asarray(rewards,float)
        if len(r)!=len(self.weights):raise ValueError('reward length mismatch')
        target=self.weights*np.exp(self.eta*np.clip(r,-1,1)); target/=target.sum()
        delta=np.clip(target-self.weights,-self.max_step,self.max_step)
        self.weights=np.maximum(0,self.weights+delta);self.weights/=self.weights.sum()
        return dict(zip(self.names,self.weights.tolist()))

def regime(returns:list[float],low=.008,high=.02)->str:
    if len(returns)<5:return 'UNKNOWN'
    vol=float(np.std(np.asarray(returns,float),ddof=1))
    return 'LOW_VOL' if vol<low else 'HIGH_VOL' if vol>high else 'NORMAL'
