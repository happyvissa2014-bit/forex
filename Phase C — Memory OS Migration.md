# TUNGNS Trading OS

# Phase C — Memory OS Migration

### Inspired by MiMo Long Horizon

---

# Purpose

Memory OS phải có một nguồn sự thật duy nhất.

Không được tồn tại hai bộ nhớ song song.

Mục tiêu của Migration này là:

* loại bỏ duplicate memory;
* chuẩn hóa cấu trúc;
* tạo One Source of Truth;
* chuẩn bị cho Evolution OS.

---

# New Architecture Decision

Chỉ giữ:

```text
backend/app/memory/
```

Toàn bộ:

```text
memory/
```

ở root sẽ bị loại bỏ.

---

# Old Architecture

```text
memory/

memory_manager.py
schemas.py

winners/
losers/
patterns/
strategies/
failed_trades/
```

Nhược điểm:

* duplicate memory;
* hai nguồn dữ liệu khác nhau;
* khó indexing;
* khó evolution;
* khó backup.

---

# New Architecture

```text
backend/app/memory/

__init__.py

memory_manager.py
memory_models.py
memory_index.py

winners/
failures/
patterns/
strategies/
regimes/
sessions/
statistics/
evidence/

examples/
metrics/
tests/
```

---

# Folder Responsibilities

## winners/

Lưu:

* trade winners;
* evidence;
* statistics.

---

## failures/

Lưu:

* failed trades;
* lessons;
* evidence.

---

## patterns/

Lưu:

* breakout;
* pullback;
* reversal;
* continuation.

---

## strategies/

Lưu:

* strategy history;
* performance history;
* weakness history.

---

## regimes/

```text
Trending
Ranging
Volatile
News
Low Liquidity
```

---

## sessions/

```text
Asian
London
New York
Overlap
```

---

## statistics/

Theo dõi:

* win rate;
* profit factor;
* expectancy;
* drawdown.

---

## evidence/

Chỉ lưu:

* indicators;
* screenshots;
* metadata;
* confidence.

Không lưu:

```text
opinions
emotions
guesses
```

---

# Migration Mapping

| Root Memory   | Memory OS        |
| ------------- | ---------------- |
| winners       | winners          |
| losers        | failures         |
| failed_trades | failures         |
| patterns      | patterns         |
| strategies    | strategies       |
| schemas.py    | memory_models.py |

---

# Naming Standard

Sai:

```text
losers/
failed_trades/
```

Đúng:

```text
failures/
```

Vì:

```text
Failure
↓
Evidence
↓
Learning
↓
Evolution
```

Robot không trừng phạt thất bại.

Robot học từ thất bại.

---

# One Source Of Truth

Sau Migration:

```text
Journal Engine
        ↓
Memory Manager
        ↓
backend/app/memory/
        ↓
Portfolio Analysis
        ↓
Backtesting
        ↓
Evolution OS
```

Không còn:

```text
memory/
backend/app/memory/
```

song song nữa.

---

# Import Migration

## Old

```python
from memory.memory_manager import ...
```

## New

```python
from backend.app.memory.memory_manager import ...
```

---

## Old

```python
from memory.schemas import ...
```

## New

```python
from backend.app.memory.memory_models import ...
```

---

# memory_manager.py

Responsibilities:

* save;
* load;
* update;
* delete;
* query.

Không:

* execution;
* signal;
* risk.

---

# memory_models.py

Models:

* TradeMemory;
* EvidenceMemory;
* PatternMemory;
* StrategyMemory;
* SessionMemory;
* RegimeMemory;
* StatisticsMemory.

---

# memory_index.py

Purpose:

Biến Memory thành hệ thống có thể truy vấn.

Index:

```text
symbol
strategy
setup
regime
session
result
```

Ví dụ:

```text
XAUUSD
↓
Breakout
↓
Trending
↓
London
↓
Winner
```

Đây là nền tảng của:

```text
Pattern Discovery
↓
Evolution
```

---

# Memory Flow

```text
Trade
↓
Journal Engine
↓
Evidence
↓
Memory OS
↓
Portfolio Analysis
↓
Backtesting
↓
Evolution OS
```

---

# Learning Flow

```text
Evidence
↓
Memory
↓
Pattern Discovery
↓
Evolution
```

---

# Final Backend Architecture

```text
backend/app/

skills/
memory/
governance/
evolution/
agents/
hooks/
```

Trong đó:

```text
backend/app/memory/
```

là Memory OS duy nhất của toàn bộ hệ thống.

---

# Long Horizon Thinking

Robot không suy nghĩ:

```text
1 Trade
```

Robot suy nghĩ:

```text
Portfolio
↓
Month
↓
Week
↓
Day
↓
Session
↓
Trade
```

---

# Final Goal

Robot không phải Signal Bot.

Robot không phải EA.

Robot là:

```text
Adaptive Trading Operating System
```

phù hợp với triết lý MiMo Long Horizon:

```text
Evidence
↓
Memory
↓
Pattern Discovery
↓
Evolution
```

Memory OS là nền tảng của Evolution OS.
