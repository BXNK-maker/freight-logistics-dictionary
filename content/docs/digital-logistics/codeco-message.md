---
title: "CODECO Message"
linkTitle: "集装箱进出闸报文"
date: 2026-11-22
type: docs
subcategory: "数据标准"
---

> 📖 分类：**物流数字化** / 数据标准　｜　CODECO Message = 集装箱进出闸报文

## 定义

CODECO Message（Container Discharge/Load Confirmation Message，简称集装箱进出闸报文）是国际航运和电子数据交换（EDI）中使用的一种标准电子消息。它由码头经营人、堆场或仓库向船公司、货代等相关方发送，用于通报集装箱在港口或场站的实际进出闸、装卸船及状态变更情况。

## 详细说明

- 使用场景：广泛应用于集装箱码头（CT）、内陆堆场（ICD）与船公司或无船承运人（NVOCC）之间的实时数据同步，常用于进出口货物的门到门或港到港追踪。
- 关键规则或数字：该报文基于联合国标准EDIFACT（Electronic Data Interchange for Administration, Commerce and Transport）格式编写，通常要求在集装箱实际发生进闸（Gate-in）、出闸（Gate-out）、装船（Load）或卸船（Discharge）操作后的规定时间内（通常为2至4小时内）自动生成并发送。
- 实务注意事项：货代与外贸企业应确保系统能够自动解析CODECO报文，以便实时掌握货物动态；若报文中的铅封号、箱体状态（空/重）或进出闸时间与实际不符，可能导致码头滞箱费（Demurrage）争议或海关放行延误，需及时与堆场核对。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 集装箱进出闸报文 | CODECO Message |
| 进闸 / 门入 | Gate-in |
| 出闸 / 门出 | Gate-out |
| 电子数据交换 | Electronic Data Interchange (EDI) |

## 相关术语

- BAPLIE Message（贝位图报文）
- EDIFACT（行政、商业和运输电子数据交换）
- CY/CY（场到场）
- Demurrage and Detention（滞箱费与滞期费）

## 常见误区

- 认为CODECO就是提单或装箱单：实际上它不是单证本身，而是一种底层的操作状态确认电文，主要向系统报告“箱子动了”。
- 混淆CODECO与COPARN：CODECO是确认集装箱“已经完成”的进出闸或装卸动作，而COPARN（集装箱预告/装卸指令报文）是操作前的计划指令。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
