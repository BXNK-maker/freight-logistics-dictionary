---
title: "Item Master"
linkTitle: "商品主数据"
date: 2026-11-25
type: docs
subcategory: "数据集成"
---

> 📖 分类：**仓储** / 数据集成　｜　Item Master = 商品主数据

## 定义
商品主数据（Item Master）是供应链与物流管理系统中的核心数据库档案，用于集中存储和管理所有库存商品的标准化基础信息。它为订单处理、仓储管理、运输规划及关务申报提供了唯一且权威的数据源。

## 详细说明
- 使用场景：广泛应用于仓库管理系统（WMS）、运输管理系统（TMS）以及企业资源规划系统（ERP）中，是货物入库、上架、拣选、打包及出库的全流程数据基础。
- 关键规则与数据：必须包含货物的唯一标识（如 SKU）、精准的物理属性（如长宽高、毛重、净重）、包装层级（如箱、托盘）、危险品属性及海关编码（HS Code）等。
- 实务注意事项：商品主数据的准确性直接影响物流费用核算和空间利用率。若尺寸或重量数据错误，极易导致仓库体积超载、运输运费错收或海关查验延误。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 商品主数据 / 物料主数据 | Item Master / Material Master |
| 库存单位 / 最小存货单位 | SKU (Stock Keeping Unit) |
| 商品描述 | Item Description / Product Description |
| 包装规格 | Packaging Specification |

## 相关术语
- SKU (Stock Keeping Unit)
- WMS (Warehouse Management System)
- HS Code (Harmonized System Code)
- Bill of Materials (BOM)

## 常见误区
- 误认为商品主数据只需在建档时录入一次即可，忽视了产品换代或包装变更后的实时更新。
- 混淆了 SKU（库存单位）与 Item Master 的概念，误将动态的库存数量等同于静态的商品属性。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
