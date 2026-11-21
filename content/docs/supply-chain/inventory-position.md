---
title: "Inventory Position"
linkTitle: "库存头寸"
date: 2026-11-21
type: docs
subcategory: "库存策略"
---

> 📖 分类：**供应链管理** / 库存策略　｜　Inventory Position = 库存头寸

## 定义

Inventory Position（库存头寸，简称 IP）是供应链管理与库存控制中的一个核心指标，用于衡量当前实际可支配的库存水平。它综合计算了企业手头的现有库存、在途采购量以及已承诺但尚未发货的订单量，是制定补货计划和生产排程的重要依据。

## 详细说明

- 使用场景：广泛应用于国际贸易、仓储物流、库存规划以及供应链管理中，帮助货主和物流经理实时掌握真实的货物供应能力，避免缺货或库存积压。
- 关键规则或数字：Inventory Position 的标准计算公式为：**库存头寸 = 现有库存 (On-hand Inventory) + 在途库存 (On-order/Pipeline Inventory) - 预定出货量 (Backorders/Allocated Inventory)**。只有当计算结果大于安全库存线时，供应链才处于健康状态。
- 实务注意事项：在国际货运中，计算在途库存时必须充分考虑海运航程、海关查验等不确定因素带来的时间延误（Lead Time），否则容易导致头寸计算失真。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 库存头寸 | Inventory Position (IP) |
| 现有库存 | On-hand Inventory |
| 在途库存 | In-transit / On-order Inventory |
| 预定出货量 | Allocated Inventory / Backorders |
| 安全库存 | Safety Stock |

## 相关术语

- Safety Stock（安全库存）
- Lead Time（提前期）
- Reorder Point（再订货点）
- Economic Order Quantity（经济订货量）
- Stockkeeping Unit（库存单位）

## 常见误区

- 误区一：认为 Inventory Position 等同于仓库里的实际库存数。实际上，它不仅加上了在途的货物，还减去了已经分配但未发走的订单，是一个动态的未来可用库存概念。
- 误区二：忽略国际物流中的运输时间变动。在计算在途库存时，如果按固定的理想航程计算，往往会导致库存头寸偏高，从而在旺季引发缺货危机。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
