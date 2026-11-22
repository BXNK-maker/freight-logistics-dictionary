---
title: "ORDRSP Message"
linkTitle: "EDIFACT订单响应报文"
date: 2026-11-22
type: docs
subcategory: "数据标准"
---

> 📖 分类：**物流数字化** / 数据标准　｜　ORDRSP Message = EDIFACT订单响应报文

## 定义

ORDRSP Message（全称为 Purchase Order Response Message，即联合国标准 EDI 订单响应报文）是一种电子数据交换格式，用于买卖双方在确认采购订单时的自动化信息交互。在国际货运与供应链管理中，它通常由供应商向买方或物流服务商发送，用来反馈订单的接受、拒绝、修改状态或备货情况。

## 详细说明

- 使用场景：买方通过 EDI 发送订单（ORDERS）后，供应商系统自动或手动生成 ORDRSP 报文，用于回复订单是否可执行、预计交货时间及具体的商品明细。
- 关键规则或数字：该报文严格遵循联合国 EDIFACT（电子数据交换、行政、商业和运输）标准协议，通过结构化的代码（如状态代码：接受、拒绝、部分接受）实现系统间无缝对接，无需人工干预。
- 实务注意事项：在国际物流和VMI（供应商管理库存）项目中，务必确保 ORDRSP 中的交货时间与后续的货运预约（IFTMIN）及发货通知（DESADV）数据保持一致，否则容易引发系统报错或仓库收货延迟。

## 中英对照

| 英文表达 | 中文翻译 |
| :--- | :--- |
| Purchase Order Response Message | 采购订单响应报文 |
| Acceptance of Order | 订单接受 |
| Line Item Status | 明细行状态 |
| EDIFACT Standard | EDIFACT 标准 |

## 相关术语

- ORDERS Message（订单报文）
- DESADV Message（发货通知报文）
- INVOIC Message（发票报文）
- ASN - Advance Shipping Notice（预先发货通知）

## 常见误区

- 误以为 ORDRSP 报文是货运代理发送给船公司的舱单数据，实际上它是供应链上下游之间关于商务订单确认的报文，与具体运输环节无直接对应关系。
- 认为收到 ORDRSP 就代表货物已经发出，其实该报文仅表示订单已被确认或调整，真正的发货状态需要查看 DESADV 发货通知报文。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
