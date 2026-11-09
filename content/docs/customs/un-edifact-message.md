---
title: "UN/EDIFACT Message"
linkTitle: "联合国电子报文"
date: 2026-11-09
type: docs
subcategory: "报关流程"
---

> 📖 分类：**关务合规** / 报关流程　｜　UN/EDIFACT Message = 联合国电子报文

## 定义

UN/EDIFACT Message（联合国行政、商业和运输电子数据交换报文）是由联合国欧洲经济委员会制定的一套国际标准电子报文格式。它将国际贸易和货运中的各种单证（如发票、提单、订舱单等）转化为结构化的标准数据，供计算机系统之间自动传输与处理。

## 详细说明

- 使用场景：广泛应用于国际供应链、海关申报、港口调度以及货代与船公司、航空公司之间的系统对接。例如，船公司发送的舱单数据、货代发送的订舱请求（IFTMIN）多采用此格式。
- 关键规则或数字：该标准遵循 ISO 9735 语法规范，采用严格的分隔符（如加号 `+` 和撇号 `'`）来界定数据段和数据元素，确保全球不同系统能无歧义地解析数据。
- 实务注意事项：由于报文结构极为严苛，任何标点符号的遗漏或字段超长都会导致传输失败（即 EDI 报错）。货代和外贸企业在系统对接时，必须严格校验报文版本的兼容性。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 联合国电子报文 | UN/EDIFACT Message |
| 电子数据交换 | Electronic Data Interchange (EDI) |
| 报文类型 | Message Type |
| 数据段 | Data Segment |

## 相关术语

- EDI (Electronic Data Interchange)
- INVOIC (Commercial Invoice Message)
- IFTMIN (Instruction Message)
- CUSCAR (Customs Cargo Report Message)

## 常见误区

- 误以为 UN/EDIFACT 是一种可以随意编辑的电子表格文件，实际上它是高度结构化的纯文本数据流，必须由专门的 EDI 翻译软件进行解析。
- 认为发送了 EDI 报文就等于完成了法律上的交付，忽略了报文传输后的功能性回执（如 CONTRL 报文）确认。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
