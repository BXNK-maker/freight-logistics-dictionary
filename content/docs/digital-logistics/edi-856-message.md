---
title: "EDI 856 Message"
linkTitle: "EDI 856 发货通知报文"
date: 2026-10-24
type: docs
subcategory: "EDI 电子数据交换"
---

> 📖 分类：**物流数字化** / EDI 电子数据交换　｜　EDI 856 Message = EDI 856 发货通知报文

## 定义

EDI 856 报文（英文全称：Electronic Data Interchange 856 Message），在国际供应链中通常被称为 ASN（Advanced Shipping Notice，高级发货通知）。它是一种电子数据交换标准格式，供供应商在货物实际发运或到达前，向买方或物流承运人发送详细的装箱与货物配置信息。

## 详细说明

- 使用场景：广泛应用于零售商、大型电商及制造企业的供应链中。当供应商完成拣货、打包并装车后，系统自动生成该报文并传输给收货方，用于提前安排卸货、仓储及入库作业。
- 关键规则或数字：该报文采用严格的分级层级结构（Hierarchical Levels），通常包含四个核心层级：发货批次层（Shipment）、订单层（Order）、包装/箱层（Packaging）以及明细物品层（Item）。这种结构确保了条形码扫描和托盘识别的准确性。
- 实务注意事项：货代与外贸从业者必须确保 EDI 856 中的物理数据（如毛重、体积、箱号、SKU 数量）与实际装货单据完全一致。一旦数据出现误差，极易导致海外仓或零售商的自动化收货系统报错，从而产生高额的罚款（Chargeback）和延误。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 高级发货通知 | Advanced Shipping Notice (ASN) |
| 箱级明细 | Pack Level Detail |
| 托盘标签 | Pallet Label |
| 货物分级结构 | Hierarchical Level Structure |

## 相关术语

- EDI 850 (Purchase Order)
- EDI 810 (Invoice)
- ASN (Advanced Shipping Notice)
- UCC/EAN-128 (Shipping Container Code)

## 常见误区

- 认为 EDI 856 只是普通的电子邮件通知：实际上它是一种机器可读的结构化数据文件，旨在直接导入收货方的仓储管理系统（WMS），而非人工阅读。
- 认为发货后几天再发送也无妨：ASN 的核心价值在于“提前”，如果货物已经到达仓库而报文尚未送达，就会失去指导卸货和预验货的意义。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
