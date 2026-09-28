from synergy_adaptive_engine.synergy_contracts import CONTRACT_ID, market_regime_payload

def test_market_regime_payload_is_advisory():
    p=market_regime_payload(symbol="eurusd",returns=[.001,-.001,.002,-.002,.001],observation_id="obs-1")
    assert CONTRACT_ID=="synergy.trading.market-regime/v1"
    assert p["symbol"]=="EURUSD"
    assert p["regime"] in {"LOW_VOL","NORMAL","HIGH_VOL"}
    assert p["authorization"] is False
