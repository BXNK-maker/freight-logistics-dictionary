---
title: "Interleaved Replenishment"
linkTitle: "交叉补货"
date: 2026-11-25
type: docs
subcategory: "补货作业"
---

> 📖 分类：**仓储** / 补货作业　｜　Interleaved Replenishment = 交叉补货

## 定义

交叉补货（Interleaved Replenishment）是一种仓库管理优化策略，指将库存补货任务与订单拣货（Picking）任务交替或穿插安排给作业人员。该策略旨在打破传统的“先补货后拣货”或各司其职的独立作业模式，实现人员与动线的深度融合。

## 详细说明

- 使用场景：适用于SKU众多、订单碎片化严重的高频电商仓库，以及仓库通道狭窄、空间资源紧张导致动线冲突频发的作业环境。
- 关键规则与逻辑：系统会实时监控货位库存。当某货位因拣货出现低库存时，系统会生成补货指令，并将其与附近的拣货任务进行路径优化合并，指派同一作业员在同一行程中顺路完成。
- 实务注意事项：需要强有力的WMS（仓库管理系统）支持，以实现实时算法调度；同时对作业人员的综合操作能力要求较高，需配备手持终端（PDA）进行无纸化指引。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 交叉补货 | Interleaved Replenishment |
| 动态补货 | Dynamic Replenishment |
| 任务交织 / 任务交替 | Task Interleaving |
| 货位管理 | Slotting Management |
| 拣货路径优化 | Pick Path Optimization |

## 相关术语

- `Task Interleaving（任务交织）`
- `WMS (Warehouse Management System)（仓储管理系统）`
- `Dynamic Slotting（动态货位分配）`
- `Pick-to-Light（电子标签拣货）`
- `Wave Picking（波次拣货）`

## 常见误区

- 误区一：认为交叉补货就是盲目地边拣货边补货。实际上，它高度依赖WMS系统的算法，必须基于精确的动线规划和实时库存触发，否则容易造成通道拥堵。
- 误区二：认为该模式会降低拣货员的工作效率。事实上，通过合理合并行程，它显著减少了空载行走时间，提升了仓库整体人效。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
