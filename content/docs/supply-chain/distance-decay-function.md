---
title: "Distance Decay Function"
linkTitle: "距离衰减函数"
date: 2026-11-21
type: docs
subcategory: "网络设计"
---

> 📖 分类：**供应链管理** / 网络设计　｜　Distance Decay Function = 距离衰减函数

## 定义
Distance Decay Function（距离衰减函数）是物流网络规划和地理信息系统（GIS）中的一个数学模型，用于描述两点之间的空间交互强度随距离增加而递减的规律。在国际货运与供应链管理中，它常被用来模拟运输成本、时间和客户需求对配送密度的影响。

## 详细说明
- 使用场景：广泛应用于海外仓选址、配送中心（DC）布局、末端配送网络优化以及客户需求预测。
- 关键规则或数字：该函数通常呈非线性下降趋势（如负指数或幂律分布）。这意味着当运输距离从10公里增至50公里时，服务频次或客户下单概率的跌幅远大于从100公里增至140公里。
- 实务注意事项：在跨国物流规划中，“距离”不仅指直线物理距离，更应换算为实际运输成本（Freight Cost）和时效（Transit Time），因关卡、拥堵和多式联运换装会扭曲纯地理距离。

## 中英对照

| 中文表达 | 英文原称 |
| :--- | :--- |
| 距离衰减函数 | Distance Decay Function |
| 空间交互 | Spatial Interaction |
| 运输成本 | Transportation Cost |
| 网络优化 | Network Optimization |

## 相关术语
- Gravity Model（引力模型）
- Hub-and-Spoke Network（轴辐式网络）
- Last-Mile Delivery（末端配送）
- Facility Location Problem（设施选址问题）

## 常见误区
- 误认为距离衰减是恒定的直线下降：实际业务中，衰减率往往受服务可达性和规模效应影响，呈现出阶段性陡降或平缓的非线性特征。
- 仅用直线距离（欧氏距离）代替实际物流距离：忽视了路网结构、海关口岸及地形限制，导致物流成本测算出现重大偏差。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
