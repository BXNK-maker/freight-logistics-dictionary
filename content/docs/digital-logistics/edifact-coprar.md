---
title: "EDIFACT COPRAR"
linkTitle: "EDIFACT 装载指令报文"
date: 2026-10-24
type: docs
subcategory: "EDI 电子数据交换"
---

> 📖 分类：**物流数字化** / EDI 电子数据交换　｜　EDIFACT COPRAR = EDIFACT 装载指令报文

## 定义
EDIFACT COPRAR（全称为 Container Discharge and Loading Report / Order）是联合国贸易数据和行政、商业、运输标准（EDIFACT）中的一种标准电子数据交换报文。它主要用于船舶营运人、港口码头营运商以及货运代理之间，传输集装箱的装卸船指令与作业报告，实现港口物流的高效数字化协同。

## 详细说明
- 使用场景：广泛应用于班轮公司与码头（Terminal）之间。当船舶靠港前，船公司通过该报文向码头发送装卸货计划；作业完成后，码头也常利用此格式向船公司反馈实际装卸情况。
- 关键规则或数字：作为结构化电子数据，报文严格遵循 EDIFACT 国际标准语法（如 UNH、BGM、EQD 等标准段），确保不同IT系统间的数据自动解析无误，减少人工录入错误。
- 实务注意事项：报文中的箱号（Container Number）、封铅号（Seal Number）、贝位信息（Bay Position）及危险品等级等数据必须与实际货物完全一致，否则码头系统会拒收或产生现场纠错费用。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 装载指令报文 | COPRAR (Container Discharge and Loading Order) |
| 集装箱卸货报告 | Container Discharge Report |
| 电子数据交换 | EDI (Electronic Data Interchange) |
| 贝位代码 | Bay Position Code |
| 码头营运商 | Terminal Operator |

## 相关术语
- COPARN（集装箱预告报文）
- BAPLIE（船舶配载图报文）
- EDIFACT（联合国行政、商业和运输电子数据交换规则）
- CODECO（集装箱进出闸/门吉报文）
- VGM（集装箱重量验证）

## 常见误区
- 误区一：认为 COPRAR 只是普通的电子邮件或 PDF 附件。实际上它是一种结构化的纯文本数据流，需通过专门的 EDI 系统进行解析和对接。
- 误区二：将 COPRAR 与 BAPLIE 混淆。BAPLIE 侧重于展示整船集装箱的三维立体配载图，而 COPRAR 侧重于向码头发出的具体装卸作业指令与确认。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
