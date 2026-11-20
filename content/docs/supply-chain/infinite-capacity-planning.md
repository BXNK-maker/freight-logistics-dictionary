---
title: "Infinite Capacity Planning"
linkTitle: "无限产能计划"
date: 2026-11-20
type: docs
subcategory: "计划体系"
---

> 📖 分类：**供应链管理** / 计划体系　｜　Infinite Capacity Planning = 无限产能计划

## 定义

无限产能计划（Infinite Capacity Planning）是一种生产或物流排程方法，它在制定计划时假设可用资源、劳动力或设备产能是无限的，完全不考虑实际的产能瓶颈与约束。该方法的核心目的是先计算出满足客户需求或交货期所需的理想资源和时间，然后再对结果进行评估和调整。

## 详细说明

- 使用场景：通常适用于供应链规划的初期阶段、需求预测分析，或是企业产能相对富余、不需要担心资源短缺的特定业务场景。
- 关键规则或数字：排程计算过程中不设置任何上限阈值（即 Capacity = Infinity），所有订单均按最早需求日期进行正向或逆向排程，最终生成的计划往往会出现工作中心超载（Overload）的情况。
- 实务注意事项：由于未考虑现实约束，该计划不能直接用于车间生产或仓库发运。从业者必须通过“产能调整”将其转化为有限产能计划（Finite Capacity Planning），否则会导致交期延误、成本上升和客户满意度下降。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 无限产能计划 | Infinite Capacity Planning |
| 有限产能计划 | Finite Capacity Planning |
| 工作中心 | Work Center |
| 产能需求计划 | Capacity Requirements Planning (CRP) |

## 相关术语

- Finite Capacity Planning（有限产能计划）
- Capacity Requirements Planning（产能需求计划）
- Master Production Schedule（主生产计划）
- Rough-Cut Capacity Planning（粗能力计划）

## 常见误区

- 认为无限产能计划可以直接下达给仓库或承运商执行，忽略了实际运力和人力的物理限制。
- 将其与物料需求计划（MRP）混淆，误以为它计算的是原材料库存，而实际上它关注的是设备和劳动力等生产资源。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
