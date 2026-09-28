from __future__ import annotations
from typing import Any

from .core import regime

CONTRACT_ID = "synergy.trading.market-regime/v1"
AUTHORITY = "adaptive_policy"


def market_regime_payload(
    *,
    symbol: str,
    returns: list[float],
    observation_id: str,
    low: float = .008,
    high: float = .02,
) -> dict[str, Any]:
    if not symbol.strip():
        raise ValueError("symbol required")
    if not observation_id.strip():
        raise ValueError("observation_id required")
    state = regime(returns, low=low, high=high)
    return {
        "observation_id": observation_id,
        "symbol": symbol.upper(),
        "regime": state,
        "sample_count": len(returns),
        "thresholds": {"low": float(low), "high": float(high)},
        "authorization": False,
    }
