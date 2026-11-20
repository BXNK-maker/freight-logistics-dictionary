---
title: "Croston's Method"
linkTitle: "克罗斯顿法"
date: 2026-11-20
type: docs
subcategory: "计划体系"
---

> 📖 分类：**供应链管理** / 计划体系　｜　Croston's Method = 克罗斯顿法

## 定义

克罗斯顿法（Croston's Method）是一种专门用于预测具有间歇性需求（Intermittent Demand）特征的库存和物流数据的方法。该方法将需求拆分为“需求发生的概率”和“每次发生的平均需求量”两个维度进行独立预测，从而有效解决传统预测模型在面对大量零需求数据时产生的严重偏差问题。

## 详细说明

- 使用场景：广泛应用于航空航天、汽车备件、高价值机械配件以及长尾商品等“慢转库存”的备货管理中，这些货物的特点是长期没有需求，偶尔产生一次或几次。
- 关键规则或数字：Croston法将时间序列拆分为两个独立成分：一是需求间隔时间（Interval），二是需求量的大小（Size）。它采用指数平滑法（Exponential Smoothing）分别对这两个成分进行更新，通常平滑系数 $\alpha$ 设在 0.1 到 0.2 之间。
- 实务注意事项：在供应链管理中，不能直接将该方法算出的理论值四舍五入作为安全库存或订货点，必须结合订货提前期（Lead Time）和目标服务水平进行综合评估。

## 中英对照

| 英文表达 | 中文翻译 |
| :--- | :--- |
| Croston's Method | 克罗斯顿法 |
| Intermittent Demand | 间歇性需求 |
| Slow-moving Inventory | 慢转库存 / 呆滞库存 |
| Exponential Smoothing | 指数平滑法 |

## 相关术语

- Intermittent Demand（间歇性需求）
- Slow-moving Inventory（慢转库存）
- Safety Stock（安全库存）
- Reorder Point（再订货点）
- Exponential Smoothing（指数平滑法）

## 常见误区

- 误区一：认为Croston's Method适用于所有类型的货物预测。实际上，对于需求连续且平稳的快消品或标准件，传统的移动平均法或指数平滑法效果更好，使用克罗斯顿法反而会降低准确性。
- 误区二：将预测出的数值直接等同于最终发货量。该方法输出的是统计学上的期望值，在实际国际物流订舱和备货时，必须叠加季节性波动和供应商交货延迟等现实变量。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
