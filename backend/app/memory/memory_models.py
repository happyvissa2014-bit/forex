from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any, Dict


class MemoryType(Enum):
    SHORT_TERM = "short_term"
    LONG_TERM = "long_term"
    EPHEMERAL = "ephemeral"


@dataclass
class MemoryRecord:
    memory_id: str
    created_at: str
    memory_type: MemoryType
    content: dict[str, Any]
    tags: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "memory_id": self.memory_id,
            "created_at": self.created_at,
            "memory_type": self.memory_type.value,
            "content": self.content,
            "tags": self.tags,
        }

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "MemoryRecord":
        return MemoryRecord(
            memory_id=data["memory_id"],
            created_at=data["created_at"],
            memory_type=MemoryType(data["memory_type"]),
            content=data["content"],
            tags=data.get("tags", []),
        )


@dataclass
class MemoryQuery:
    query: str
    tags: list[str] = field(default_factory=list)
    memory_type: MemoryType | None = None


@dataclass
class TradeMemory:
    trade_id: str
    symbol: str
    direction: str
    result: float
    session: str | None = None
    regime: str | None = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class EvidenceMemory:
    id: str
    screenshots: list[str] = field(default_factory=list)
    indicators: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)
    confidence: float = 0.0

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class PatternMemory:
    pattern_type: str
    details: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class StrategyMemory:
    strategy_id: str
    performance: Dict[str, Any] = field(default_factory=dict)
    drawdown: float = 0.0
    expectancy: float = 0.0

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class SessionMemory:
    name: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class RegimeMemory:
    regime: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class StatisticsMemory:
    win_rate: float = 0.0
    profit_factor: float = 0.0
    expectancy: float = 0.0
    sharpe_ratio: float = 0.0
    drawdown: float = 0.0

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
