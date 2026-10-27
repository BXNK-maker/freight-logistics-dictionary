---
title: "FWB Message"
linkTitle: "FWB 主运单电子报文"
date: 2026-10-27
type: docs
subcategory: "空运报文"
---

> 📖 分类：**运输** / 空运报文　｜　FWB Message = FWB 主运单电子报文

## 定义

FWB 报文（英文全称：Freight Waybill Message）是航空货运电子化过程中的一种标准 EDI 报文，主要用于向航空公司传输空运主运单（Master Air Waybill, MAWB）的纸面货运数据。它是无纸化航空货运（e-Freight）的核心组成部分，替代了传统的人工录入和纸质单据传递。

## 详细说明

- 使用场景：货代在完成舱位订舱并理清货物数据后，通过货代系统（FMS）生成 FWB 报文，并以电子方式发送给承运人（航空公司）或地面代理。
- 关键规则或数字：FWB 必须遵循国际航空运输协会（IATA）制定的 Cargo-IMP 或 XML 标准格式。报文中包含的数据（如计费重量、件数、品名、运费条款等）必须与实际交货及物理纸质主运单完全一致，否则系统校验会报错。
- 实务注意事项：若 FWB 传输错误或缺失，可能导致航空公司无法正常出单、航班起飞前无法完成舱单申报，甚至产生海关滞留或航司的数据纠正费。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 主运单电子报文 | FWB Message (Freight Waybill Message) |
| 货运数据传输 | Cargo Data Transmission |
| 电子货运 | e-Freight |
| 报文校验 | Message Validation |

## 相关术语

- FHL Message（分运单电子报文）
- CIMP（货运信息交换标准）
- MAWB（主运单）
- EDI（电子数据交换）
- e-AWB（电子运单）

## 常见误区

- 误区一：认为发送了 FWB 报文就不需要再制作纸质主运单。实际上，虽然推广 e-Freight，但在许多航线和目的港，仍需纸质文件配合或作为应急备用。
- 误区二：将 FWB 和 FHL 混淆。FWB 仅传输主运单（MAWB）信息，而 FHL 用于传输拼货（Consolidation）情况下的分运单（HAWB）数据。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
