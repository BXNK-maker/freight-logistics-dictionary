---
title: "Inventory Snapshot"
linkTitle: "库存快照"
date: 2026-11-25
type: docs
subcategory: "WMS功能"
---

> 📖 分类：**仓储** / WMS功能　｜　Inventory Snapshot = 库存快照

## 定义

Inventory Snapshot（库存快照）是指在特定时间点对仓库中所有存货状态及数量的静态记录。它相当于给动态变化的库存拍下一张“照片”，用于准确反映某一精准时刻的库存资产状况。

## 详细说明

- 使用场景：广泛应用于月末/年末财务盘点、仓库系统结算（EOD/EOM）、以及对接跨境电商ERP或WMS（仓储管理系统）以同步实时库存数据。
- 关键规则或数字：快照必须精确到秒，通常设定在业务低峰期（如午夜 00:00）生成，以确保此时没有货物入库或出库，从而避免数据偏差。
- 实务注意事项：在海外仓和FBA（Fulfillment by Amazon）业务中，生成库存快照时要区分可用库存（Available）、在途库存（In-transit）和预留库存（Reserved），防止因未结算订单导致账实不符。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 库存快照 | Inventory Snapshot |
| 期末库存 | Ending Inventory |
| 实时库存 | Real-time Inventory |
| 库存盘点 | Inventory Count / Stocktaking |

## 相关术语

- WMS (Warehouse Management System)（仓储管理系统）
- Safety Stock（安全库存）
- Stock Keeping Unit (SKU)（库存单位）
- Cycle Counting（循环盘点）

## 常见误区

- 误区一：认为库存快照就是实时库存。实际上，快照是“过去某个时间点”的静态数据，而实时库存会随着每单出入库随时变动。
- 误区二：在有大量未完成出库作业时生成快照。这会导致快照数据与实际物理库存产生差异，影响后续的账务核对。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
