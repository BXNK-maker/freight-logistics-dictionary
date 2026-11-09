---
title: "CUSDEC Message"
linkTitle: "报关报文"
date: 2026-11-09
type: docs
subcategory: "报关流程"
---

> 📖 分类：**关务合规** / 报关流程　｜　CUSDEC Message = 报关报文

## 定义

CUSDEC Message（Customs Declaration Message，海关申报报文）是一种符合电子数据交换（EDI）标准的电子文件，用于进出口商或其代理人向海关传输货物申报数据。它是国际贸易和海关无纸化通关的核心工具，能够实现报关单据的标准化和自动化流转。

## 详细说明

- 使用场景：主要应用于海关进出口申报、转关申报以及保税货物的进出境备案，替代了传统纸质报关单的逐项录入与人工递交。
- 关键规则与标准：CUSDEC 通常遵循联合国贸易简化与电子商务促进会（UN/CEFACT）制定的 EDIFACT 标准，或符合各地海关（如中国海关单一窗口）制定的特定 XML/EDI 报文规范，对字段长度、数据格式和必填项有严格的校验逻辑。
- 实务注意事项：报文中的商品编码（HS Code）、货名、重量、价值等核心数据必须与商业发票、装箱单及提单保持高度一致，任何格式错误或逻辑冲突都会导致海关系统自动退单（Rejection）。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 海关申报报文 | Customs Declaration Message (CUSDEC) |
| 电子数据交换 | Electronic Data Interchange (EDI) |
| 海关单一窗口 | Single Window |
| 报关单退单 | Customs Declaration Rejection |

## 相关术语

- `CUSRES Message（海关响应报文）`
- `EDIFACT（联合国行政、商业和运输电子数据交换规则）`
- `Single Window（单一窗口）`
- `HS Code（商品编码）`

## 常见误区

- 误区一：认为 CUSDEC 就是报关单本身。实际上它只是报关单数据的“电子载体”，其本质是一串符合特定语法规则的计算机可读代码。
- 误区二：只要发送了 CUSDEC 报文就等于货物已经顺利通关。报文发送成功仅代表海关系统已接收，后续必须收到海关的 CUSRES（响应报文）确认放行，才算真正完成通关手续。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
