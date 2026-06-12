from __future__ import annotations

from .adapter import optimize_parameters
from .gene_search import BacktestOptimizer


class BacktestOptimizationAgent:
    """Optimization agent for parameter search."""
    def __init__(self):
        self.optimizer = BacktestOptimizer()

    def run(self, symbol: str, timeframe: str, step_range: list[float], x_range: list[int], risk_range: list[float]):
        return self.optimizer.run(symbol=symbol, timeframe=timeframe, step_range=step_range, x_range=x_range, risk_range=risk_range)


__all__ = ["optimize_parameters", "BacktestOptimizationAgent", "BacktestOptimizer"]
