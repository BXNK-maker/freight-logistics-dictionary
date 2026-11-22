---
title: "EDIFACT"
linkTitle: "联合国EDIFACT标准"
date: 2026-11-22
type: docs
subcategory: "数据标准"
---

> 📖 分类：**物流数字化** / 数据标准　｜　EDIFACT = 联合国EDIFACT标准

## 定义
EDIFACT（Electronic Data Interchange for Administration, Commerce and Transport）是联合国开发并推荐的国际电子数据交换标准。它定义了一套全球通用的语法和报文标准，使不同企业、不同系统之间的商业与物流数据能够实现无纸化自动传输。

## 详细说明
- 使用场景：广泛应用于国际货运、海关申报、港口调度及供应链管理中，常用于船公司、货代、码头和收发货人之间的大规模数据交互。
- 关键规则与数字：其核心标准为ISO 9735，报文结构由服务字符串、报文头、数据段、数据元和组合数据元组成，通过结构化文本实现跨平台解析。
- 实务注意事项：各系统对接时必须严格校验报文格式（如EDIFACT D.96A等版本），任何标点或字段错位都会导致整条报文解析失败，需配合AS2或VAN网络确保传输安全性。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 联合国电子数据交换标准 | UN/EDIFACT |
| 电子数据交换 | Electronic Data Interchange (EDI) |
| 报文类型 | Message Type |
| 贸易数据交换 | Trade Data Interchange (TDI) |

## 相关术语
- `EDI (Electronic Data Interchange)`
- `API (Application Programming Interface)`
- `AS2 (Applicability Statement 2)`
- `XML (Extensible Markup Language)`
- `BAPLIE (Bayplan/Stinted Detailed Message)`

## 常见误区
- 误认为EDIFACT是一种软件：它只是一套数据格式标准，而非可以直接点击安装的应用程序。
- 混淆版本号：不同版本的EDIFACT报文（如D.03B与D.96A）语法细节有差异，直接混用会导致系统报错。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
