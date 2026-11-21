---
title: "Capacitated VRP"
linkTitle: "带容量约束车辆路径"
date: 2026-11-21
type: docs
subcategory: "人工智能应用"
---

> 📖 分类：**物流数字化** / 人工智能应用　｜　Capacitated VRP = 带容量约束车辆路径

## 定义

带容量约束车辆路径（Capacitated Vehicle Routing Problem，简称 CVRP）是运筹学和物流管理中的经典问题。它指的是在满足每个客户需求的前提下，如何为一组有载重量限制的运输车辆规划最优的配送路线，以实现总体运输成本或行驶距离最小化。

## 详细说明

- 使用场景：广泛应用于同城快递配送、冷链物流、超市多点补货以及B2B企业的定期末端派送等场景。
- 关键规则或数字：车辆的总载货量必须严格小于或等于其最大额定载重（Capacity）；每条配送路线的起点和终点通常设定为同一个中央仓库（Depot），且每位客户只能由一辆车服务一次。
- 实务注意事项：在实际操作中，除了车辆容量限制，还需综合考量道路限高限重、客户指定的签收时间窗口（Time Windows）以及驾驶员的工时限制，以确保排线方案具备可落地性。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 带容量约束车辆路径 | Capacitated Vehicle Routing Problem (CVRP) |
| 车辆路径问题 | Vehicle Routing Problem (VRP) |
| 中心仓库 | Depot |
| 车辆载重容量 | Vehicle Capacity |

## 相关术语

- VRP (Vehicle Routing Problem，车辆路径问题)
- VRPTW (Vehicle Routing Problem with Time Windows，带时间窗车辆路径问题)
- TSP (Traveling Salesperson Problem，旅行商问题)
- 3PL (Third-Party Logistics，第三方物流)

## 常见误区

- 认为 CVRP 只需要考虑最短距离：实际上，车辆的物理载重上限是核心硬约束，不满足容量限制的“最短路线”在实操中是无效的。
- 混淆 CVRP 与 TSP：TSP 仅处理单车拜访多个地点的闭环路线，而 CVRP 涉及多台车辆、车队总容量分配以及更复杂的组合优化。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
