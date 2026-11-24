---
title: "Location Capacity Check"
linkTitle: "储位容量校验"
date: 2026-11-24
type: docs
subcategory: "上架策略"
---

> 📖 分类：**仓储** / 上架策略　｜　Location Capacity Check = 储位容量校验

## 定义

储位容量校验（Location Capacity Check）是指在仓储管理系统（WMS）中，系统自动对指定货位（Location）的物理空间、重量承载极限及容积进行核算的控制机制。该机制旨在确保货物上架时不会超出货位的最大承载能力，是保障仓库作业安全与空间高效利用的核心校验环节。

## 详细说明

- 使用场景：主要应用于货物入库上架（Putaway）、库内移位（Bin-to-Bin Transfer）以及拼箱货（LCL）配载等仓储作业环节。
- 关键规则或数字：系统通常基于长宽高（Dimensions）、毛重（Gross Weight）及体积重比率进行三维立体校验。常见规则设定为货位实际占用体积或重量不得超过其设计最大容量的 100%，部分高货架仓库会预留 5%-10% 的安全余量。
- 实务注意事项：若基础数据（如货物包装尺寸或毛重）维护错误，极易导致校验失效或爆仓；同时需定期校准仓库各货位的物理属性，避免超重导致货架坍塌。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 储位容量校验 | Location Capacity Check |
| 最大承载重量 | Maximum Weight Capacity |
| 体积限制 | Cube Limit / Volume Limitation |
| 货位占用率 | Location Utilization Rate |

## 相关术语

- Putaway（上架）
- Warehouse Management System, WMS（仓库管理系统）
- Bin-to-Bin Transfer（库内移位）
- Cube Utilization（空间利用率）

## 常见误区

- 误以为只要货位有空隙就能存放货物，忽略了重量超载的风险。
- 将货物的外包装尺寸与实际毛重脱节，导致系统体积校验通过但物理空间无法容纳。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
