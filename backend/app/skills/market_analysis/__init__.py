from __future__ import annotations

from app.core.models import MarketTick
from .adapter import analyze_market_state
from .feature_pipeline import compute_features


class MockMarketDataAgent:
    """Mock market data agent for testing and development."""
    def __init__(self, start_price: float = 1.08000, spread: float = 0.00010):
        self.price = start_price
        self.spread = spread

    def fetch_tick(self, symbol: str) -> MarketTick:
        from backend.app.skills.shared.mock_market import generate_tick
        tick = generate_tick(symbol=symbol, start_price=self.price, spread=self.spread)
        self.price = tick.mid
        return tick

    def validate_independent_source(self, tick: MarketTick) -> bool:
        from backend.app.skills.shared.mock_market import validate_independent_source
        return validate_independent_source(tick)


__all__ = ["analyze_market_state", "MockMarketDataAgent", "compute_features"]
