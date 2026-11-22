---
title: "IFTSTA Message"
linkTitle: "EDIFACT运输状态报文"
date: 2026-11-22
type: docs
subcategory: "数据标准"
---

> 📖 分类：**物流数字化** / 数据标准　｜　IFTSTA Message = EDIFACT运输状态报文

## 定义
IFTSTA Message（EDIFACT Transport Status Message，EDIFACT运输状态报文）是联合国贸易数据和行政、商业、运输标准（UN/EDIFACT）中的一种标准电子数据交换报文。它主要用于在货运代理、承运人、港口及收发货人之间，自动传输货物在运输过程中的状态和位置更新信息。

## 详细说明
- 使用场景：广泛应用于国际集装箱运输、多式联运和仓储物流中。当货物的运输状态发生关键节点变化时（如装船、卸船、出入闸、海关放行等），系统会自动生成并发送该报文。
- 关键规则或数字：作为国际标准报文，其结构严格遵循 UN/EDIFACT 语法规则（通常基于 D.96A 或更新的版本），确保不同国家和企业的 IT 系统能够无障碍地自动解析和处理物流状态数据。
- 实务注意事项：货代和外贸企业在对接系统时，必须确保自身 ERP 或物流管理系统能够准确映射 IFTSTA 报文中的状态代码，避免因代码解析错误导致客户查询不到最新的货物动态。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 运输状态报文 | Transport Status Message (IFTSTA) |
| 状态代码 | Status Code |
| 事件报告 | Event Reporting |
| 报文标准 | Message Standard |

## 相关术语
- `IFTMIN Message（EDIFACT 运输指令报文）`
- `CODECO Message（EDIFACT 港口/堆场箱进出闸报文）`
- `BAPLIE Message（EDIFACT 船舶配载图报文）`
- `EDIFACT（联合国行政、商业和运输电子数据交换）`

## 常见误区
- 误认为 IFTSTA 报文只适用于海运集装箱，实际上它同样适用于空运、公路和铁路等多式联运的货物状态追踪。
- 混淆 IFTSTA 与 IFTMIN，误将运输状态更新报文当成是向承运人下达的初始订舱或运输指令。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
