from synergy_adaptive_engine.core import *

def test_weights_sum():
    e=AdaptiveEnsemble(['a','b']);e.update([1,-1]);assert abs(e.weights.sum()-1)<1e-12 and e.weights[0]>e.weights[1]

def test_regime():assert regime([.1,-.1,.1,-.1,.1])=='HIGH_VOL'
