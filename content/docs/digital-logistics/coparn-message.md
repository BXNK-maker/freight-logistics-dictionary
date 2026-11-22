---
title: "COPARN Message"
linkTitle: "集装箱通报报文"
date: 2026-11-22
type: docs
subcategory: "数据标准"
---

> 📖 分类：**物流数字化** / 数据标准　｜　COPARN Message = 集装箱通报报文

## 定义

COPARN Message（Container Pre-arrival Notice Message，集装箱通报报文）是国际货运和电子数据交换（EDI）中，发货人、货代或车队向码头运营商（Terminal Operator）预先发送的集装箱进场通报电子报文。该报文用于提前告知码头即将有特定集装箱运达，以便码头做好接收和堆存准备。

## 详细说明

- 使用场景：通常在出口集装箱装货前，由货代或车队在安排集卡提重、装货并送往码头（或堆场）之前，通过 EDI 系统传输给码头。
- 关键规则或数字：COPARN 报文基于联合国贸易和运输数据电子交换（UN/EDIFACT）标准。它必须在集装箱实际抵达码头闸口之前发送，否则码头系统可能拒绝集装箱入闸，直接影响进港效率。
- 实务注意事项：报文中的关键数据（如箱号、铅封号、箱型尺寸、VGM重量、目的港等）必须与实际进港货物及后续的装船清单完全一致。任何信息错误都可能导致集装箱无法顺利入闸或延误装船。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 集装箱通报报文 | COPARN Message (Container Pre-arrival Notice Message) |
| 电子数据交换 | Electronic Data Interchange (EDI) |
| 联合国标准报文 | UN/EDIFACT |
| 码头运营商 | Terminal Operator |

## 相关术语

- COPRIN Message（集装箱进场确认报文）
- CODECO Message（集装箱进出场报告报文）
- BAPLIE Message（舱位配载及积载计划报文）
- EDIFACT（联合国贸易和运输数据电子交换标准）

## 常见误区

- 误以为 COPARN 是船公司发给货代的：实际上它通常是由货代或场站发给码头的预报报文，方向正好相反。
- 认为发送了 COPARN 报文就等于完成了报关：它仅用于码头物流作业的货物预报，不能替代海关的报关和放行手续。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
