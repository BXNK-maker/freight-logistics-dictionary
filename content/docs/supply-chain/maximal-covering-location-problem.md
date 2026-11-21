---
title: "Maximal Covering Location Problem"
linkTitle: "最大覆盖选址问题"
date: 2026-11-21
type: docs
subcategory: "网络设计"
---

> 📖 分类：**供应链管理** / 网络设计　｜　Maximal Covering Location Problem = 最大覆盖选址问题

## 定义

最大覆盖选址问题（Maximal Covering Location Problem，简称 MCLP）是运筹学和物流网络设计中的经典数学模型。其核心目标是在资源有限的情况下，选择最优的设施建设地址，使得在预设的服务距离或时间范围内，能够覆盖最大数量的客户需求点或货量。

## 详细说明

- 使用场景：广泛应用于物流网络规划、区域配送中心（DC）选址、跨境电商海外仓布局、快递末端网点及自提柜规划。
- 关键规则或数字：通常设定固定的设施数量上限（如 $p$ 个仓库）或预算限制，并以“时间窗”（如城区 2 小时达）或“服务半径”（如 50 公里内）作为覆盖阈值，最大化吞吐量或服务人口。
- 实务注意事项：在实际操作中，不能仅考虑几何距离，还需结合交通路况、海关监管区分布、干线运输成本及未来业务增长潜力进行综合动态评估。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 最大覆盖选址问题 | Maximal Covering Location Problem (MCLP) |
| 设施选址 | Facility Location |
| 服务半径 | Service Radius / Coverage Distance |
| 需求点 | Demand Point |
| 配送中心 | Distribution Center (DC) |

## 相关术语

- $p$-Median Problem（$p$-中值问题）
- Facility Location Problem（设施选址问题）
- Warehouse Management System（仓库管理系统）
- Supply Chain Network Design（供应链网络设计）

## 常见误区

- 误区一：认为 MCLP 追求的是总运输成本最低。实际上，MCLP 的首要目标是最大化服务覆盖面，若追求成本最低应选择 $p$-中值或运输问题模型。
- 误区二：忽略了服务半径的刚性限制。实际建仓时，若超出设定的时间或距离阈值，即使能送到也不计入有效覆盖。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
