---
title: "Bill of Lading Number Format"
linkTitle: "提单号格式"
date: 2026-11-23
type: docs
subcategory: "运输单证"
---

> 📖 分类：**单证** / 运输单证　｜　Bill of Lading Number Format = 提单号格式

## 定义

提单号格式（Bill of Lading Number Format）是指船公司、无船承运人或货运代理人在签发提单时，所采用的由特定字母和数字组合而成的编号编排规则。该格式通常包含前缀代码和流水号，用于唯一标识每一份运输契约及相关货物。

## 详细说明

- 使用场景：广泛应用于海运进出口订舱、货物追踪、舱单传输（如AMS/EN24）、报关查验以及目的港换单提货的全业务流程中。
- 关键规则或数字：通常由3位前缀（如船公司SCAC代码）加上6至9位不等的流水数字组成，部分提单号末尾还会包含校验位（Check Digit）。
- 实务注意事项：在录入舱单或报关资料时，提单号的格式必须与船公司系统完全一致，多输、漏输连字符或空格都可能导致海关退单或目的港无法正常提货。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 提单号格式 | Bill of Lading Number Format |
| 前缀代码 | Prefix Code / SCAC Code |
| 校验位 | Check Digit |
| 提单号录入 | Bill of Lading Number Entry |

## 相关术语

- `SCAC (Standard Carrier Alpha Code)`
- `Master Bill of Lading (船东单 / 主单)`
- `House Bill of Lading (货代单 / 分单)`
- `Cargo Tracking (货物追踪)`

## 常见误区

- 误认为所有船公司的提单号长度和结构都完全一致，导致在集成多个船公司系统时出现数据校验报错。
- 忽略了提单号中的空格或特殊符号（如连字符），在系统录入时随意删减，从而引发电子舱单传输失败。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
