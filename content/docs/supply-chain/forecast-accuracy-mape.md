---
title: "Forecast Accuracy (MAPE)"
linkTitle: "预测准确率 MAPE"
date: 2026-10-26
type: docs
subcategory: "需求管理"
---

> 📖 分类：**供应链管理** / 需求管理　｜　Forecast Accuracy (MAPE) = 预测准确率 MAPE

## 定义

Forecast Accuracy (MAPE) 即平均绝对百分比误差（Mean Absolute Percentage Error），是衡量供应链需求预测或货量预测准确程度的核心指标。它通过计算预测值与实际值之间绝对误差百分比的平均值，直观反映出预测结果偏离实际货量的程度。


## 详细说明

- 使用场景：广泛应用于海运、空运及合同物流中的月度/周度货量预测、舱位预定规划以及仓库安全库存设定，帮助货代评估客户或分公司预测的可靠性。
- 关键规则或数字：MAPE 的计算公式为实际绝对误差占实际值的百分比平均值。通常来说，MAPE 值越低代表预测越准；在成熟的物流网络中，稳定的航线或长期大客户的 MAPE 通常要求控制在 15% 到 20% 以内。
- 实务注意事项：当实际货量为零或接近零时，MAPE 计算结果会出现失真或趋于无穷大，因此在处理零星出货或季节性波动极大的航线时需谨慎使用，建议结合绝对偏差（MAD）综合评估。


## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 预测准确率 (MAPE) | Forecast Accuracy (MAPE) |
| 货量预测 | Cargo Volume Forecast |
| 实际出货量 | Actual Shipment Volume |
| 预测误差 | Forecast Error |


## 相关术语

- Demand Forecasting（需求预测）
- Safety Stock（安全库存）
- Lead Time（提前期）
- S&OP (Sales and Operations Planning)（销售与运营规划）


## 常见误区

- 误认为 MAPE 越接近 0% 就一定对业务最有利：盲目追求极低的 MAPE 可能会导致企业持有过高的备用舱位或库存成本，需在预测准确性与备货灵活性之间寻找平衡。
- 混淆 MAPE 与偏差总和（Bias）：MAPE 计算的是绝对值的百分比，无法看出预测是持续偏高还是偏低，因此必须配合正负偏差分析才能找出预测系统的根本问题。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
