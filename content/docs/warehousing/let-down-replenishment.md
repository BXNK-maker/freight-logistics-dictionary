---
title: "Let-Down Replenishment"
linkTitle: "降位补货"
date: 2026-11-25
type: docs
subcategory: "补货作业"
---

> 📖 分类：**仓储** / 补货作业　｜　Let-Down Replenishment = 降位补货

## 定义

降位补货（Let-Down Replenishment，简称 Let-Down）是指在仓储管理中，将货物从仓库的高层货架（通常是后备存储区 Storage Area）移动到低层货架（通常是拣货区 Picking Area）的作业过程。这一操作旨在确保低层拣货位有充足的库存，以满足日常订单的高效拣选需求。


## 详细说明

- 使用场景：主要适用于采用垂直空间存储的高位货架仓库、电商物流中心以及SKU众多的现代配送中心，当拣货位库存降至安全库存以下时触发。
- 关键规则或数字：通常设定最小触发库存（Min Level）和补货上限（Max Level）。系统会根据历史出货频率和周转率，自动计算补货时机和最佳移动数量，避免拣货位爆仓或断货。
- 实务注意事项：作业时需避开出货高峰期，合理规划搬运路线，避免高空作业与地面拣货人员发生碰撞；同时必须严格核对货位条码与商品批次，防止货物放错位置导致账实不符。


## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 降位补货 | Let-Down Replenishment |
| 拣货区 | Pick Face / Picking Area |
| 后备存储区 | Reserve Storage Area |
| 补货触发点 | Replenishment Trigger Point |


## 相关术语

- `Pick and Pass（接力拣货）`
- `Slotting Optimization（货位优化）`
- `Safety Stock（安全库存）`
- `Warehouse Management System (WMS)（仓库管理系统）`


## 常见误区

- 误认为降位补货就是普通的仓库内部移位：实际上它有明确的目的性，专指“高位到低位”为了拣货而进行的补货，而普通移位可能包含同层调整或库间调拨。
- 忽视系统指令盲目人工补货：不依赖WMS系统的自动触发，仅凭经验随意降位，极易导致拣货位空间冲突或库存混乱。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
