---
title: "(s; S) Policy"
linkTitle: "(s; S)补货策略"
date: 2026-11-20
type: docs
subcategory: "库存策略"
---

> 📖 分类：**供应链管理** / 库存策略　｜　(s; S) Policy = (s; S)补货策略

## 定义

(s; S)补货策略（英文全称：(s; S) Inventory Replenishment Policy）是一种广泛应用于供应链与库存管理中的经典周期性审查库存控制策略。其中，小写字母 $s$ 代表订货警戒点（Reorder Point），大写字母 $S$ 代表库存上限或目标库存水平（Order-up-to Level）。当系统审查发现当前库存降至或低于 $s$ 时，便会触发补货，将库存补充至 $S$。

## 详细说明

- 使用场景：适用于需求波动较大、需要定期盘点库存，且批量采购能带来规模经济效益的国际贸易与仓储管理。
- 关键规则或数字：当库存量 $I \le s$ 时，下单量为 $Q = S - I$；当库存量 $I > s$ 时，不采取行动。这种机制有效避免了频繁小批量订货带来的高额订购成本与运输成本。
- 实务注意事项：在国际物流操作中，必须将供应商的提前期（Lead Time）以及海运/空运途中的在途库存（Pipeline Inventory）纳入计算，否则极易因盲目设定 $s$ 和 $S$ 导致供应链断层或港口滞箱费增加。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| (s; S)补货策略 | (s; S) Inventory Policy |
| 订货警戒点 | Reorder Point (s) |
| 目标库存水平 | Order-up-to Level (S) |
| 提前期 | Lead Time |
| 在途库存 | Pipeline Inventory |

## 相关术语

- Economic Order Quantity, EOQ（经济订货批量）
- Safety Stock（安全库存）
- Reorder Point System（再订货点系统）
- Inventory Turnover（库存周转率）

## 常见误区

- 误认为 $s$ 和 $S$ 的数值是一成不变的：在国际物流中，航线延误、季节性需求变动都会影响参数，必须动态调整。
- 混淆了固定订货量模型与 (s; S) 策略：(s; S) 的每次订货量是变动的，取决于当前库存与目标 $S$ 的差额，而不是固定的批次。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
