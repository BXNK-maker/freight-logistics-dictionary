---
title: "Auto-Replenishment"
linkTitle: "自动补货"
date: 2026-11-21
type: docs
subcategory: "库存策略"
---

> 📖 分类：**供应链管理** / 库存策略　｜　Auto-Replenishment = 自动补货

## 定义
Auto-Replenishment（自动补货）是指供应链系统根据预设的库存水平、销售数据和需求预测，自动向供应商或仓库发出补货指令的机制。该技术能够减少人工干预，确保货物在短时间内得到补充，从而维持高效的库存周转。

## 详细说明
- 使用场景：广泛应用于跨境电商海外仓、VMI（供应商管理库存）项目以及高频次补货的快消品物流管理中。
- 关键规则或数字：通常设定安全库存（Safety Stock）和再订货点（ROP，Reorder Point）。当库存降至ROP时，系统自动触发补货，补货量一般以达到最大库存容量（Max Stock Level）为限。
- 实务注意事项：货代与物流服务商需要与客户的ERP或WMS系统进行API对接，确保数据实时同步；同时，应考虑国际海运或空运的运输途牛（Lead Time），避免因航程延误导致断货。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 自动补货 | Auto-Replenishment / Automatic Replenishment |
| 安全库存 | Safety Stock |
| 再订货点 | Reorder Point (ROP) |
| 供应商管理库存 | Vendor Managed Inventory (VMI) |

## 相关术语
- `Vendor Managed Inventory（供应商管理库存）`
- `Safety Stock（安全库存）`
- `Reorder Point（再订货点）`
- `Lead Time（交货期 / 提前期）`
- `Warehouse Management System（仓库管理系统）`

## 常见误区
- 认为自动补货不需要人工监控：实际上，市场需求具有波动性，系统参数（如提前期和安全库存）需要根据淡旺季定期人工调整，否则易导致呆滞库存或缺货。
- 混淆自动补货与传统定期采购：自动补货基于“实时库存触发（事件驱动）”，而传统采购多为“定期盘点下单”，两者的响应速度和库存成本有显著差异。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
