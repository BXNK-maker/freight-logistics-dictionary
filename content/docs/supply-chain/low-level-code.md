---
title: "Low-Level Code"
linkTitle: "低位码"
date: 2026-11-20
type: docs
subcategory: "计划体系"
---

> 📖 分类：**供应链管理** / 计划体系　｜　Low-Level Code = 低位码

## 定义

Low-Level Code（低位码，简称LLC）是物料需求计划（MRP）系统中用于标识物料在所有产品BOM（物料清单）中所处最低层级的数字代码。通过确定低位码，系统能够确保在计算物料需求时，对同一物料的所有需求进行汇总后才进行净需求计算。

## 详细说明

- 使用场景：广泛应用于ERP及供应链物流系统的MRP运算、库存规划和采购计划生成阶段。
- 关键规则：当同一物料在多个产品结构中出现并处于不同层级时，该物料的低位码会被赋予这些层级中的最低值（即数字最大的一层）。系统在进行运算时，必须按低位码由小到大的顺序（从第0层最高层开始逐层向下）依次计算。
- 实务注意事项：在维护BOM时，若出现循环引用或层级错误，会导致低位码计算混乱，进而引发采购计划数量失真或库存积压。物流与供应链计划员需定期检查并优化系统中的物料层级数据。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 低位码 | Low-Level Code (LLC) |
| 物料清单 | Bill of Materials (BOM) |
| 物料需求计划 | Material Requirements Planning (MRP) |
| 独立需求 | Independent Demand |
| 相关需求 | Dependent Demand |

## 相关术语

- Bill of Materials（物料清单）
- Material Requirements Planning（物料需求计划）
- Master Production Schedule（主生产计划）
- Enterprise Resource Planning（企业资源计划）

## 常见误区

- 误区一：认为低位码数值越小代表物料层级越深。实际上，数字越小代表层级越高（终产品为

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
