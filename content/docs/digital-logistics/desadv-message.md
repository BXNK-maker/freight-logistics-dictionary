---
title: "DESADV Message"
linkTitle: "EDIFACT发运通知报文"
date: 2026-11-22
type: docs
subcategory: "数据标准"
---

> 📖 分类：**物流数字化** / 数据标准　｜　DESADV Message = EDIFACT发运通知报文

## 定义

DESADV Message（全称为 Despatch Advice Message，即 EDIFACT发运通知报文）是一种电子数据交换（EDI）标准报文。供应商通过该报文向买方或收货人发送详细的发货通知，告知即将运抵的货物清单、包装明细及运输相关信息。

## 详细说明

- 使用场景：广泛应用于汽车制造、零售商超和大型B2B供应链中。当供应商完成拣货并发车后，通常会立即向客户系统发送 DESADV，以便仓库提前做好收货准备。
- 关键规则或数字：该报文严格遵循联合国 EDIFACT（Electronic Data Interchange for Administration, Commerce and Transport）国际标准。它通常包含订单号、SKU、批次号、箱条码（SSCC）、数量以及物流承运商信息。
- 实务注意事项：DESADV 中的物理发货数据必须与实际到货的货盘标签及货物完全一致，否则会导致仓库收货扫描报错、入库效率下降甚至供应链索赔。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 发运通知报文 | Despatch Advice Message (DESADV) |
| 序列化物流容器代码 | Serial Shipping Container Code (SSCC) |
| 电子数据交换 | Electronic Data Interchange (EDI) |
| 预先发货通知 | Advance Shipping Notice (ASN) |

## 相关术语

- EDIFACT（联合国行政、商业和交通电子数据交换）
- ASN（预先发货通知）
- SSCC（系列化物流容器代码）
- WMS（仓库管理系统）

## 常见误区

- 误区一：认为 DESADV 就是传统的纸质装箱单。实际上它是结构化的电子数据，旨在实现收货环节的系统自动化匹配，无需人工录入。
- 误区二：认为 DESADV 只是一份简单的货物清单。它不仅包含商品信息，还深入到包装层级（如托盘、箱、件的嵌套关系），是供应链可视化和条码扫描的基础。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
