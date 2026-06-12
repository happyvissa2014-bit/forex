# TUNGNS Trading OS

# Phase C.6 — Capability Migration

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

ưu tiên tiếp theo không phải Governance OS.

Ưu tiên cao nhất là:

```text
Phase C.5 — Capability Migration
```

Mục tiêu:

* loại bỏ duplicate capability;
* tạo One Skill Registry;
* tạo One Memory OS;
* tạo One Source of Truth;
* chuẩn bị cho Governance OS;
* chuẩn bị cho Evolution OS.

---

# Core Philosophy

Một capability chỉ được tồn tại một lần.

Không được có:

* hai folder giống nhau;
* hai implementation giống nhau;
* hai nguồn logic khác nhau.

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

# Current Problem

Hiện vẫn tồn tại:

```text
backend/app/market/
backend/app/guard/
backend/app/execution/
```

song song với:

```text
backend/app/skills/

market_analysis/
risk_engine/
execution_engine/
```

Điều này tạo ra:

* duplicate capability;
* duplicate imports;
* khó maintain;
* khó Evolution;
* Two Sources of Truth.

---

# New Architecture Decision

Chỉ giữ:

```text
backend/app/skills/
```

Không đặt business logic ở nơi khác.

---

# Remove Legacy Modules

Loại bỏ hoàn toàn:

```text
backend/app/market/
backend/app/guard/
backend/app/execution/
```

---

# New Capability Structure

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

| Legacy Module | New Skill        |
| ------------- | ---------------- |
| market        | market_analysis  |
| guard         | risk_engine      |
| execution     | execution_engine |

---

# Import Migration

## Market

### Old

```python
from backend.app.market.market_service import ...
```

### New

```python
from backend.app.skills.market_analysis import ...
```

---

## Guard

### Old

```python
from backend.app.guard.risk_manager import ...
```

### New

```python
from backend.app.skills.risk_engine import ...
```

---

## Execution

### Old

```python
from backend.app.execution.executor import ...
```

### New

```python
from backend.app.skills.execution_engine import ...
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
guard/
execution/
```

song song với:

```text
skills/
```

---

# One Memory OS

Chỉ giữ:

```text
backend/app/memory/
```

Không còn:

```text
memory/
```

ở root.

---

# One Source Of Truth

Kiến trúc cuối cùng:

```text
backend/app/

skills/
memory/
governance/
evolution/
agents/
hooks/
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

## Easier Maintenance

Một capability chỉ sửa ở một nơi.

---

## Easier Imports

Không còn import chéo giữa legacy và skills.

---

## Easier Governance

Governance OS chỉ quản lý một Skill Registry.

---

## Easier Evolution

Evolution OS chỉ học từ một nguồn duy nhất.

---

# Status

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

# Completion Criteria

Capability Migration chỉ được xem là hoàn tất khi:

```text
backend/app/market/      ✗
backend/app/guard/       ✗
backend/app/execution/   ✗
```

không còn tồn tại.

Và toàn bộ imports đã chuyển sang:

```python
backend.app.skills.market_analysis
backend.app.skills.risk_engine
backend.app.skills.execution_engine
```

---

# Next Phase

Chỉ sau khi đạt:

```text
One Skill Registry ✓
One Memory OS ✓
One Source Of Truth ✓
```

mới bắt đầu:

```text
Phase D — Governance OS
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
