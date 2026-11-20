---
title: "Weighted Absolute Percentage Error (WAPE)"
linkTitle: "加权绝对百分比误差"
date: 2026-11-20
type: docs
subcategory: "计划体系"
---

> 📖 分类：**供应链管理** / 计划体系　｜　Weighted Absolute Percentage Error (WAPE) = 加权绝对百分比误差

## 定义
加权绝对百分比误差（Weighted Absolute Percentage Error，简称 WAPE）是一种用于衡量货运物流中预测准确度的统计指标。它通过计算预测值与实际值绝对偏差的总和占实际值总和的比例，帮助供应链管理者评估需求预测或运量预测的整体偏差水平。

## 详细说明
- 使用场景：广泛应用于国际货代和供应链管理中的月度/季度集装箱吞吐量预测、干线运输需求量预测以及仓储安全库存规划的准确性评估。
- 关键规则或数字：计算公式为绝对误差之和除以实际值之和。相比常规的 MAPE，WAPE 能有效避免因实际需求为零时产生的数学崩塌，且赋予大批量货量更高的权重，更符合物流降本增效的业务关注点。
- 实务注意事项：在多SKU或多航线汇总时，WAPE 可能会掩盖个别航线的严重预测失误（正负误差相互抵消），因此建议结合偏态分析或分层评估共同使用。

## 中英对照
| 英文表达 | 中文翻译 |
| :--- | :--- |
| Weighted Absolute Percentage Error (WAPE) | 加权绝对百分比误差 |
| Demand Forecasting Accuracy | 需求预测准确度 |
| Absolute Deviation | 绝对偏差 |
| Actual vs. Forecast | 实际值与预测值对比 |

## 相关术语
- Mean Absolute Percentage Error (MAPE)（平均绝对百分比误差）
- Forecast Bias (FB)（预测偏差）
- Mean Squared Error (MSE)（均方误差）
- Safety Stock (SS)（安全库存）

## 常见误区
- 认为 WAPE 和 MAPE 是完全一样的指标：实际上 WAPE 是先求和再求比率（即总误差除以总需求），而 MAPE 是先计算每个数据点的百分比误差再求平均，两者的权重分配逻辑有本质区别。
- 盲目追求 0% 的误差：在长周期海运物流中，市场波动剧烈，过分追求极低的 WAPE 可能会导致预测模型过度拟合，反而降低应对突发供应链中断的韧性。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
