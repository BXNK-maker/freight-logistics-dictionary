---
title: "VERMAS Message"
linkTitle: "VGM申报报文"
date: 2026-11-22
type: docs
subcategory: "数据标准"
---

> 📖 分类：**物流数字化** / 数据标准　｜　VERMAS Message = VGM申报报文

## 定义

VERMAS Message（Verified Gross Mass Message，VGM申报报文）是国际海运电子数据交换（EDI）标准报文中专门用于传输集装箱验证毛重的数据文件。它由托运人或其授权代表发送给承运人或码头运营商，以确保船舶配载安全并符合国际公约要求。

## 详细说明

- 使用场景：在集装箱进港前或截重日期（Closing Date）前，托运人通过EDI系统向船公司或码头提交VGM数据时使用。
- 关键规则或数字：报文必须包含集装箱号、验证总重（精确到千克）、称重方法（方法一或方法二）、授权签名以及负责人的身份信息。根据SOLAS公约，无VGM数据的集装箱严禁装船。
- 实务注意事项：报文中的VGM数据必须与实际过磅单或计算清单完全一致。若数据有误，需及时发送修改报文（Correction），否则可能产生码头改单费或导致箱子被甩。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| VGM申报报文 | VERMAS Message |
| 验证毛重 | Verified Gross Mass (VGM) |
| 电子数据交换 | Electronic Data Interchange (EDI) |
| 称重方法 | Weighing Method |

## 相关术语

- SOLAS Convention（国际海上人命安全公约）
- EDIFACT（联合国贸易和运输电子数据交换规则）
- Closing Date（截关日）
- Terminal Operator（码头运营商）

## 常见误区

- 认为VERMAS报文可以代替海运提单（B/L）或装箱单（Packing List），实际上它属于独立的配载安全数据。
- 以为只有船公司系统需要VERMAS，事实上码头（CY）系统也必须实时接收该报文才能放行集装箱进重箱场。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
