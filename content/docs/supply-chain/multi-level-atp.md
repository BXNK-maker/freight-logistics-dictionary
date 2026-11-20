---
title: "Multi-Level ATP"
linkTitle: "多层可承诺量"
date: 2026-11-20
type: docs
subcategory: "计划体系"
---

> 📖 分类：**供应链管理** / 计划体系　｜　Multi-Level ATP = 多层可承诺量

## 定义

Multi-Level ATP（多层可承诺量，Multi-Level Available-to-Promise）是供应链与高级物流规划中的一项核心库存分配机制。它不仅检查最终成品的库存，还能逐层向下穿透，实时检查半成品、原材料及各级供应商的产能与物料可用性，从而为客户订单提供准确的交货承诺。

## 详细说明

- 使用场景：广泛应用于复杂制造、全球供应链分销以及跨境JIT（准时制）物流项目中。当客户订购定制化货物或大宗商品时，系统用它来评估现有库存和各生产层级的物料是否充足。
- 关键规则或数字：系统会按照BOM（物料清单）和分销网络的多级结构进行并行计算。它能够将订单拆解到组件级别，通常在毫秒级内给出是否可承诺以及具体交货日期的答复。
- 实务注意事项：货代和物流专员应注意，ATP数据依赖于准确的实时库存和运输状态更新。如果国际运输段出现延误，多层ATP系统未能及时同步在途库存（In-Transit Inventory），就会导致承诺的交货期失效。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 多层可承诺量 | Multi-Level Available-to-Promise (Multi-Level ATP) |
| 物料清单 | Bill of Materials (BOM) |
| 可承诺量 | Available-to-Promise (ATP) |
| 生产计划 | Master Production Schedule (MPS) |

## 相关术语

- BOM（物料清单）
- MPS（主生产计划）
- ERP（企业资源计划）
- CTB（可装配量）

## 常见误区

- 误区一：认为Multi-Level ATP只是销售部门的事，与物流无关。实际上，国际运输中的在途库存和港口滞留数据直接影响ATP的准确性。
- 误区二：将ATP与物理库存（Physical Inventory）混淆。ATP不仅包含现有库存，还涵盖了未来计划生产量和采购到货量。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
