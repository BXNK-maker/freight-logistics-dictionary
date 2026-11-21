---
title: "Perpetual Inventory"
linkTitle: "永续盘存"
date: 2026-11-21
type: docs
subcategory: "库存策略"
---

> 📖 分类：**供应链管理** / 库存策略　｜　Perpetual Inventory = 永续盘存

## 定义

永续盘存（Perpetual Inventory）是指企业通过现代仓库管理系统（WMS）或企业资源计划（ERP）系统，对库存商品的入库、出库、移位及盘点等全流程进行实时动态记录与更新的库存管理方法。该方法确保账面库存数据与物理实际库存保持高度同步，无需依赖定期的全面盘点即可随时获取准确的库存余额。

## 详细说明

- 使用场景：广泛应用于高吞吐量的第三方物流（3PL）仓库、跨境电商海外仓以及SKU繁多的现代化配送中心，特别适合处理订单频繁、出入库流转极快的货品。
- 关键规则或数字：系统核心在于“动账即实时更新”，即每发生一笔收货、发货或退货，系统库存数量会自动加减；同时配合ABC分类法，通常对A类高价值货物实施高频次的循环盘点（Cycle Counting），如每月或每季度盘点一次，确保盘点准确率达到99%以上。
- 实务注意事项：货代与仓储操作人员必须严格执行条形码（Barcode）或RFID扫描作业，严禁“先操作后补录”或“白条出库”，否则会导致系统账面库存与实体货物产生误差，引发错发、漏发或库存短缺。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 永续盘存 / 实时库存 | Perpetual Inventory |
| 循环盘点 | Cycle Counting |
| 仓库管理系统 | Warehouse Management System (WMS) |
| 库存准确率 | Inventory Accuracy |
| 实体库存 | Physical Inventory |

## 相关术语

- `Physical Inventory（实地盘点）`
- `Cycle Counting（循环盘点）`
- `Stock Keeping Unit（库存单位/SKU）`
- `Warehouse Management System（仓库管理系统）`
- `Safety Stock（安全库存）`

## 常见误区

- 认为永续盘存上线后就完全不需要进行人工实地盘点了。实际上，由于系统录入失误、货物损耗或盗窃等原因，仍需通过循环盘点来纠正账实差异。
- 混淆永续盘存与定期盘存（Periodic Inventory）。永续盘存是实时动态更新的，而定期盘存是仅在特定会计期末才进行一次性全盘统计。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
