---
title: "FHL Message"
linkTitle: "FHL 分运单电子报文"
date: 2026-10-27
type: docs
subcategory: "空运报文"
---

> 📖 分类：**运输** / 空运报文　｜　FHL Message = FHL 分运单电子报文

## 定义

FHL Message（全称为 Freight House Lower-level Message，即分运单电子报文）是航空货运中用于传输集中托运货物下属分运单（House Waybill）详细数据的标准电子报文。该报文由货代（Freight Forwarder）发送给航空公司，以便航司在舱单和安检申报时获取每个收发货人的具体货物明细。

## 详细说明

- 使用场景：主要用于国际航空货运拼货（Consolidation）业务。当货代将多票不同客户的货物合并为一票主运单（Master Air Waybill, MAWB）托运给航空公司时，必须同时传输对应的主运单报文（FWB）和分运单报文（FHL）。
- 关键规则或数字：FHL 报文必须与同批次的 FWB 报文严格匹配。如果主运单下包含 N 个分运单，FHL 报文中必须完整且准确地包含这 N 个分运单的计费重量、件数、品名、收发货人信息等。
- 实务注意事项：FHL 数据传输不准确或延迟会导致海关预申报失败、航空公司无法正常出具舱单，进而引发货物滞留机场海关或产生罚款。货代操作员在录入时，必须确保分运单上的毛重、体积和件数之和与主运单完全一致。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 分运单电子报文 | FHL Message / Freight House Lower-level Message |
| 主运单电子报文 | FWB Message / Freight Waybill Message |
| 航空分运单 | HAWB / House Air Waybill |
| 航空主运单 | MAWB / Master Air Waybill |
| 集中托运 | Consolidation |

## 相关术语

- FWB Message（主运单电子报文）
- HAWB（航空分运单）
- MAWB（航空主运单）
- EDI（电子数据交换）
- CASS（货运结算系统）

## 常见误区

- 认为发送了主运单报文（FWB）就足够了：实际操作中，拼货必须同时发送 FWB 和 FHL，缺一不可，否则航司无法识别具体的货主信息。
- FHL 数据可以晚于货物到达目的地后再补发：FHL 必须在航班起飞前或按海关及航司规定的时限内成功传输，否则会严重影响目的港的清关效率。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
