---
title: "Min-Max Replenishment"
linkTitle: "上下限补货"
date: 2026-11-25
type: docs
subcategory: "补货作业"
---

> 📖 分类：**仓储** / 补货作业　｜　Min-Max Replenishment = 上下限补货

## 定义
上下限补货（Min-Max Replenishment）是一种经典的库存控制策略，英文全称为 Minimum-Maximum Replenishment。该策略设定了库存的最低警戒线（Min）与最高容量线（Max），当库存降至最低线或以下时，系统会自动触发补货订单，将库存补充至最高线。

## 详细说明
- 使用场景：广泛应用于仓库管理（WMS）、供应商管理库存（VMI）以及跨境电商海外仓的日常补货，特别适合需求相对平稳、SKU数量庞大的标准品。
- 关键规则或数字：
  - Min（最小库存）：基于安全库存和平均补货提前期（Lead Time）设定，用于防止缺货。
  - Max（最大库存）：基于仓储成本、资金占用和库容限制设定，用于防止库存积压。
  - 订货量计算公式：每次补货量 = 最高库存（Max） - 当前可用库存。
- 实务注意事项：在国际物流中，必须将较长的海运或空运运输时间（Lead Time）纳入Min值的计算中，否则极易在头程运输期间发生断货。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 上下限补货 | Min-Max Replenishment |
| 最小库存 / 安全库存 | Minimum Stock / Safety Stock |
| 最大库存 | Maximum Stock |
| 补货提前期 | Replenishment Lead Time |

## 相关术语
- `Safety Stock（安全库存）`
- `Lead Time（提前期）`
- `Reorder Point (ROP)（再订货点）`
- `Economic Order Quantity (EOQ)（经济订货量）`
- `Vendor-Managed Inventory (VMI)（供应商管理库存）`

## 常见误区
- 误区一：认为 Min 值就是绝对的零库存警戒线。实际上，Min 值应当包含在途库存和满足提前期消耗的余量，若见底才开始订货，往往会导致断货。
- 误区二：将 Min-Max 策略一成不变。市场需求和国际物流的准时性会发生变化，如果长期不评估和调整 Min 与 Max 的数值，会导致库存周转率恶化或频繁缺货。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
