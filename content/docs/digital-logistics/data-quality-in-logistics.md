---
title: "Data Quality in Logistics"
linkTitle: "物流数据质量"
date: 2026-10-24
type: docs
subcategory: "数据治理"
---

> 📖 分类：**物流数字化** / 数据治理　｜　Data Quality in Logistics = 物流数据质量

## 定义
物流数据质量（Data Quality in Logistics）是指在货运、仓储及供应链管理过程中，所采集、传输和处理的数据在准确性、完整性、及时性和一致性方面的表现。高质量的物流数据是确保货物高效流转、减少运营风险和实现供应链可视化的基础。

## 详细说明
- 使用场景：广泛应用于EDI数据交换、TMS运输管理系统、WMS仓库管理系统以及海关申报环节，特别是跨境电商物流和多式联运中。
- 关键规则或数字：国际物流行业普遍追求“垃圾进，垃圾出（Garbage In, Garbage Out）”的反向标准，核心指标包括：关键字段（如舱单信息、HS Code、重量体积）的准确率通常需达到99%以上，节点状态更新延迟应控制在15分钟以内。
- 实务注意事项：在单证录入和API对接时，必须严格校验收发货人信息、货物描述及件毛体数据，任何微小误差都可能导致海关查验、滞箱费（Demurrage & Detention）或舱单不符罚款。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 物流数据质量 | Data Quality in Logistics |
| 数据准确性 | Data Accuracy |
| 数据完整性 | Data Completeness |
| 电子数据交换 | Electronic Data Interchange (EDI) |
| 数据治理 | Data Governance |

## 相关术语
- EDI (Electronic Data Interchange)
- Master Data Management (主数据管理)
- Visibility (供应链可视化)
- Customs Manifest (海关舱单)

## 常见误区
- 认为数据质量只是IT部门的责任：实际上，一线操作人员录入的运单、尺码等基础数据才是源头，业务人员同样对数据质量负有直接责任。
- 只要系统不报错就代表数据没问题：系统校验通过仅代表格式合规，并不等于业务逻辑和实际货物的物理状态相符。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
