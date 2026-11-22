---
title: "INVOIC Message"
linkTitle: "EDIFACT发票报文"
date: 2026-11-22
type: docs
subcategory: "数据标准"
---

> 📖 分类：**物流数字化** / 数据标准　｜　INVOIC Message = EDIFACT发票报文

## 定义

INVOIC Message（全称为 Electronic Data Interchange for Administration, Commerce and Transport Invoice Message，即 EDIFACT发票报文）是联合国贸易数据交换标准（UN/EDIFACT）中用于传输商业发票及相关财务数据的标准电子报文格式。它允许买卖双方或物流供应链各方在无纸化环境下，以结构化数据自动交换费用账单和付款要求。

## 详细说明

- 使用场景：广泛应用于国际货运代理、船公司、航空公司与客户之间的电子计费，常见于运费账单（Freight Invoice）、仓储费结算以及海关税费代垫清算。
- 关键规则或数字：作为国际通用的 EDI 标准，INVOIC 报文严格遵循 UN/EDIFACT 语法规则（通常基于 ISO 9735），能够与 DESADV（发货通知）和 ORDERS（订单）报文无缝衔接，实现供应链的闭环数据流。
- 实务注意事项：在发送 INVOIC 报文前，需确保报文中的税号、币种代码（ISO 4217）和银行账户信息与贸易合同完全一致；同时要关注接收方的系统版本，避免因映射错误导致账单解析失败或财务对账延迟。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 发票报文 | INVOIC Message |
| 电子数据交换 | Electronic Data Interchange (EDI) |
| 商业发票 | Commercial Invoice |
| 运费账单 | Freight Invoice |
| 账单对账 | Invoice Reconciliation |

## 相关术语

- `EDIFACT（联合国行政、商业和交通电子数据交换）`
- `DESADV Message（发货通知报文）`
- `IFTMIN Message（货运指令报文）`
- `BAPLIE Message（舱位配载报文）`

## 常见误区

- 误区一：认为 INVOIC 报文就是一张普通的 PDF 或图片发票。实际上，它是一串符合特定语法规则的纯文本结构化数据，需要通过 EDI 翻译软件解析后才能转化为可视化账单。
- 误区二：认为发票报文只能在买卖双方之间流转。在现代物流中，货代和船公司也频繁使用它向货主发送运杂费账单，用于自动化财务入账。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
