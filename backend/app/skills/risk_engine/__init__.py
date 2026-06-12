from __future__ import annotations

from app.core.config import Settings
from app.core.models import MarketTick, RiskDecision, RobotState
from .adapter import risk_analysis
from .risk_guard import evaluate_risk


class RiskGuardAgent:
    """Risk guard agent that evaluates market risk."""
    def __init__(self, settings: Settings):
        self.settings = settings

    def evaluate(self, state: RobotState, tick: MarketTick | None = None, api_latency_ms: int = 0) -> RiskDecision:
        return evaluate_risk(state=state, settings=self.settings, tick=tick, api_latency_ms=api_latency_ms)


__all__ = ["risk_analysis", "RiskGuardAgent", "evaluate_risk"]
