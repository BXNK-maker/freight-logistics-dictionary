---
title: "FHL"
linkTitle: "分运单舱单报文"
date: 2026-11-07
type: docs
subcategory: "电子货运"
---

> 📖 分类：**运输** / 电子货运　｜　FHL = 分运单舱单报文

## 定义

FHL 是航空货运电子数据交换中的核心报文之一，英文全称为 **House Waybill Manifest Message**（分运单舱单报文）。它是集中托运人（Consolidator）或货运代理人向航空公司传输的电子数据，用于向航空公司提供同一主运单（Master Air Waybill）下所有分运单（House Air Waybill）的详细货物信息。

## 详细说明

- 使用场景：主要用于国际航空货运拼货（Consolidation）业务。当货代将多票不同发货人的货物合并为一票交给航空公司时，需发送此报文。
- 关键规则：FHL 必须在航班起飞前或在航空公司规定的截止时间前成功发送并被海关/航司系统接收。它的传输通常依赖于主运单舱单报文（FFM）的配合，两者数据必须严格一致。
- 实务注意事项：FHL 中的分运单重量、件数和货描必须与实际报关单及纸质分运单相符，否则极易导致目的港清关延误或航司罚款。随着各国的“预先航空货物信息”（PRE/ICS2）合规要求收紧，FHL 数据的准确性对避免安检扣货至关重要。

## 中英对照

| 中文表达 | 英文原称 |
| :--- | :--- |
| 分运单舱单报文 | House Waybill Manifest Message (FHL) |
| 主运单舱单报文 | Flight Manifest Message (FFM) |
| 航空分运单 | House Air Waybill (HAWB) |
| 航空主运单 | Master Air Waybill (MAWB) |
| 集中托运人 | Consolidator |

## 相关术语

- `FFM（航班舱单报文）`
- `MAWB（航空主运单）`
- `HAWB（航空分运单）`
- `Consolidation（集中托运/拼货）`
- `ACI（预先货物信息）`

## 常见误区

- 误区一：认为发送了 FFM 就不需要发送 FHL。实际上，FFM 只包含主运单级别的大货信息，涉及具体收发货人的明细必须通过 FHL 传输。
- 误区二：FHL 可以随意修改。在海关或航司锁定舱单数据后，修改 FHL 需要走繁琐的更改程序，甚至产生改单费。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
