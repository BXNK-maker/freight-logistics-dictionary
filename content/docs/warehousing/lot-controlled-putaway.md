---
title: "Lot-Controlled Putaway"
linkTitle: "批次控制上架"
date: 2026-11-24
type: docs
subcategory: "上架策略"
---

> 📖 分类：**仓储** / 上架策略　｜　Lot-Controlled Putaway = 批次控制上架

## 定义

批次控制上架（Lot-Controlled Putaway）是指在仓储管理系统中，根据货物的批次号（Lot Number）、生产日期或失效日期等关键属性，来指导和限制货物存放具体库位的作业流程。它确保了对特定批次货物的可追溯性和先进先出（FIFO）或先进后出（LIFO）等库存策略的严格执行。

## 详细说明

- 使用场景：广泛应用于医药、食品、化工及高科技电子等对产品质量、保质期和批次追溯有严格要求的行业。
- 关键规则：系统会根据货物的批次属性自动推荐或强制指定库位，禁止不同批次的高敏感货物混放，确保近效期货物优先出库。
- 实务注意事项：操作人员在手持终端（PDA）上架扫描时必须核对批次条码，严禁人为随意更改系统指定的库位，以免破坏库存追溯链条。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 批次控制上架 | Lot-Controlled Putaway |
| 批次管理 | Lot Management / Batch Management |
| 库位分配 | Bin Allocation / Location Assignment |
| 先进先出 | FIFO (First In, First Out) |

## 相关术语

- `Batch Number / Lot Number（批次号）`
- `Putaway Strategy（上架策略）`
- `FIFO - First In, First Out（先进先出）`
- `FEFO - First Expired, First Out（先到期先出）`
- `WMS - Warehouse Management System（仓储管理系统）`

## 常见误区

- 认为上架只是把货物放到空库位上，忽略了批次属性对库位选择的决定性影响。
- 混淆了批次管理与序列号管理的区别，批次管理针对同一批生产的批量货物，而序列号针对单件唯一商品。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
