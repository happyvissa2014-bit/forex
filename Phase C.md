# TUNGNS Trading OS

# Phase C.5 — Capability Migration

### Inspired by MiMo Long Horizon

---

# Purpose

Sau khi hoàn thành:

```text
Skill Registry ✓
Journal Engine ✓
Portfolio Analysis ✓
Backtesting ✓
Memory OS ✓
```

bước quan trọng tiếp theo không phải Governance OS.

Ưu tiên cao nhất là:

```text
Phase C.5 — Capability Migration
```

Mục tiêu:

* loại bỏ duplicate capability;
* loại bỏ nhiều nguồn logic khác nhau;
* tạo One Skill Registry;
* tạo One Source of Truth;
* chuẩn bị cho Governance OS và Evolution OS.

---

# Core Philosophy

Robot không được có:

* hai skill giống nhau;
* hai folder giống nhau;
* hai nguồn logic khác nhau.

Một capability chỉ tồn tại một lần.

```text
Capability
↓
Evidence
↓
Memory
↓
Evolution
```

---

# Current Problems

Hiện tồn tại:

## Legacy Modules

```text
market/
strategy/
guard/
execution/
sweep/
```

---

## Kebab Case Skills

```text
journal-engine/
portfolio-analysis/
risk-engine/
optimization-engine/
```

---

## Snake Case Skills

```text
journal_engine/
portfolio_analysis/
risk_engine/
optimization_engine/
```

Điều này gây:

* duplicate logic;
* khó maintain;
* khó import;
* khó Evolution;
* hai nguồn sự thật.

---

# New Architecture Decision

Chỉ giữ:

```text
backend/app/skills/
```

Mọi capability phải nằm bên trong:

```text
backend/app/skills/
```

Không được tạo logic ở nơi khác.

---

# Naming Standard

Sai:

```text
journal-engine/
portfolio-analysis/
risk-engine/
optimization-engine/
```

Đúng:

```text
journal_engine/
portfolio_analysis/
risk_engine/
optimization_engine/
```

Lý do:

* tương thích Python import;
* thống nhất codebase;
* dễ maintain.

---

# Legacy Folder Migration

## Remove

```text
market/
strategy/
guard/
execution/
sweep/
```

---

## Replace By

```text
skills/

market_analysis/
setup_detection/
risk_engine/
execution_engine/
sweep_engine/
```

---

# Skill Registry Final Structure

```text
backend/app/skills/

market_analysis/
setup_detection/
risk_engine/
execution_engine/
hedge_engine/
optimization_engine/

journal_engine/
portfolio_analysis/
backtesting/
```

---

# Migration Mapping

| Legacy    | New              |
| --------- | ---------------- |
| market    | market_analysis  |
| strategy  | setup_detection  |
| guard     | risk_engine      |
| execution | execution_engine |
| sweep     | sweep_engine     |

---

| Kebab Case          | Snake Case          |
| ------------------- | ------------------- |
| journal-engine      | journal_engine      |
| portfolio-analysis  | portfolio_analysis  |
| risk-engine         | risk_engine         |
| optimization-engine | optimization_engine |

---

# Import Migration

## Old

```python
from market.market_service import ...
```

## New

```python
from backend.app.skills.market_analysis import ...
```

---

## Old

```python
from strategy.breakout import ...
```

## New

```python
from backend.app.skills.setup_detection import ...
```

---

## Old

```python
from guard.risk_manager import ...
```

## New

```python
from backend.app.skills.risk_engine import ...
```

---

## Old

```python
from execution.executor import ...
```

## New

```python
from backend.app.skills.execution_engine import ...
```

---

# One Skill Registry

Sau Migration:

```text
Agents
↓
Skills
↓
Memory
↓
Governance
↓
Evolution
```

Không còn:

```text
market/
strategy/
guard/
execution/
```

song song với:

```text
skills/
```

---

# One Source Of Truth

Sau Migration:

```text
backend/app/

skills/
memory/
governance/
evolution/
agents/
hooks/
```

là kiến trúc duy nhất của hệ thống.

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

Không còn:

```text
market/
strategy/
guard/
execution/
sweep/
```

Không còn:

```text
journal-engine/
portfolio-analysis/
```

---

# Long Horizon Flow

```text
Capability
↓
Evidence
↓
Memory
↓
Pattern Discovery
↓
Evolution
```

---

# Benefits

## One Skill Registry

Một capability chỉ tồn tại một lần.

---

## One Memory OS

Một bộ nhớ duy nhất.

---

## One Source Of Truth

Không còn duplicate.

---

## Easier Governance

Governance OS chỉ cần quản lý một nơi.

---

## Easier Evolution

Evolution OS chỉ cần học từ một nơi.

---

# Current Status

```text
Skill Registry        ✓
Journal Engine        ✓
Portfolio Analysis    ✓
Backtesting           ✓
Memory OS             ✓

Capability Migration  ⏳
Governance OS         0%
Evolution OS          20%
```

---

# Next Phase

Sau khi hoàn thành Capability Migration:

```text
Phase D — Governance OS
```

Kiến trúc sẽ trở thành:

```text
Skills
↓
Memory
↓
Governance
↓
Evolution
```

---

# Final Goal

Robot không phải Signal Bot.

Robot không phải EA.

Robot là:

```text
Adaptive Trading Operating System
```

theo triết lý MiMo Long Horizon:

```text
Evidence
↓
Memory
↓
Pattern Discovery
↓
Evolution
```
