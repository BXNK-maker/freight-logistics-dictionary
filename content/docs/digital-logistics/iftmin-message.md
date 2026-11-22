---
title: "IFTMIN Message"
linkTitle: "EDIFACT运输指令报文"
date: 2026-11-22
type: docs
subcategory: "数据标准"
---

> 📖 分类：**物流数字化** / 数据标准　｜　IFTMIN Message = EDIFACT运输指令报文

## 定义

IFTMIN Message 是指联合国贸易数据和行政、商业、运输电子数据交换（EDIFACT）中的运输指令报文（Instruction Message），英文全称为 EDIFACT Instruction Message。它是货主、发货人或货运代理向承运人发送的标准化电子指令，用于传输出口或进口货物的具体装运要求和订舱细节。

## 详细说明

- 使用场景：主要用于国际供应链中，发货人或货代在完成货物准备后，向船公司、航空公司或拼箱公司正式下达发运指令，替代传统的纸质托运书或电子邮件。
- 关键规则或数字：该报文严格遵循联合国 EDIFACT 标准格式，通常包含报文头（UNH）、报文尾（UNT）以及涵盖货物品名、毛重、体积、起运港、目的港和集装箱信息的多个标准段（Segments）。
- 实务注意事项：发送 IFTMIN 之前，必须确保所有基础数据（如提单号、件毛体）与实际货物完全一致，因为承运人系统通常会自动抓取该报文生成舱单或提单草稿，数据错误将直接导致后续海关申报延误或高昂的改单费。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 运输指令报文 | IFTMIN Message / Instruction Message |
| 电子数据交换 | EDI (Electronic Data Interchange) |
| 联合国贸易简化与电子商务中心 | UN/CEFACT |
| 托运书 / 订舱委托书 | Shipping Instruction / Booking Note |

## 相关术语

- `IFTSTA Message（EDIFACT 运输状态报文）`
- `INVOIC Message（EDIFACT 发票报文）`
- `IFTMBC Message（EDIFACT 船公司预报/确认报文）`
- `EDIFACT（电子数据交换标准）`

## 常见误区

- 误区一：认为 IFTMIN 报文就是最终的提单。实际上它只是发货人发出的“指令”，承运人确认并签发后才会产生提单。
- 误区二：认为所有船公司都可以直接接收任意版本的 IFTMIN。虽然遵循统一标准，但不同船公司在具体字段的映射和截单时间（SI Cut-off）上有各自的特殊要求。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
