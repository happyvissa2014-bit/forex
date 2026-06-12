from __future__ import annotations

from app.core.config import Settings
from app.core.models import Order
from .adapter import execute_order
from .order_router import ExecutionEngine


class ExecutionAdapterAgent:
    """Execution adapter agent that routes orders."""
    def __init__(self, settings: Settings):
        self.settings = settings
        self.engine = ExecutionEngine(settings=settings)

    def execute(self, order: Order) -> Order:
        return self.engine.execute(order)


__all__ = ["execute_order", "ExecutionAdapterAgent", "ExecutionEngine"]
