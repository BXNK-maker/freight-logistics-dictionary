---
title: "Intermittent Demand Forecasting"
linkTitle: "间歇性需求预测"
date: 2026-11-20
type: docs
subcategory: "计划体系"
---

> 📖 分类：**供应链管理** / 计划体系　｜　Intermittent Demand Forecasting = 间歇性需求预测

## 定义

间歇性需求预测（Intermittent Demand Forecasting）是指对那些需求发生频率低、且每次需求数量不规则的货物进行未来需求量的预测方法。该方法广泛应用于长尾备件、航空航天航海维修件以及低频高值的供应链管理中。

## 详细说明

- 使用场景：主要适用于备件物流（Spare Parts Logistics）、MRO（维护、修理和运营）物资仓储以及偶发性大宗货物的国际运输规划。
- 关键规则与特征：此类需求在大多数时间段内的需求量为零，一旦产生需求则数量随机。传统的时间序列预测模型（如移动平均法）在此场景下会失效，通常需采用克鲁斯特法（Croston's Method）等专用算法，将需求发生的间隔与需求量分开进行预测。
- 实务注意事项：货代与物流从业者应避免根据历史平均出货量盲目备货或预留运力，而应与客户建立安全库存（Safety Stock）联动机制，密切关注供应链终端的突发性订单，以防出现空载率高或关键时刻无舱位可用的困境。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 间歇性需求预测 | Intermittent Demand Forecasting |
| 备件物流 | Spare Parts Logistics |
| 克鲁斯特法 | Croston's Method |
| 安全库存 | Safety Stock |
| 需求间隔期 | Demand Interval |

## 相关术语

- Spare Parts Logistics（备件物流）
- Inventory Optimization（库存优化）
- Safety Stock（安全库存）
- Lead Time（提前期）

## 常见误区

- 认为可以用传统的移动平均法或指数平滑法直接预测零星出货，导致预测偏差极大。
- 误将“间歇性需求”等同于“季节性需求”，忽略了其发生的随机性和突发性。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
