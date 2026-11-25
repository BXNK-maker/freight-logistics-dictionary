---
title: "Wave Cutoff"
linkTitle: "波次截单"
date: 2026-11-25
type: docs
subcategory: "波次计划"
---

> 📖 分类：**仓储** / 波次计划　｜　Wave Cutoff = 波次截单

## 定义

波次截单（Wave Cutoff）是指在仓库自动化订单履行（Fulfillment）或电商大促发货场景中，运营系统将订单按批次（波次）进行归集处理的最终截止时间点。在该时间点之后生成的订单或对订单的修改，将无法被纳入当前的拣货、打包和装车波次中，只能顺延至下一个波次处理。

## 详细说明

- 使用场景：广泛应用于跨境电商仓储、第三方物流（3PL）以及大型B2C配送中心，特别是在大促期间需要高频次、分批次处理海量订单时尤为关键。
- 关键规则与时间节点：系统通常会根据货车到站时间（Dock Time）、海关截单时间或航班/船期（SI/SO Cutoff）倒推，设定多个固定的波次截单时间点。一旦到达Wave Cutoff，系统会瞬间锁定该波次的数据，停止接收新订单，并生成相应的拣货任务单（Pick List）。
- 实务注意事项：仓库操作人员和客服团队必须密切协同，确保买家在Wave Cutoff前完成付款或信息修改，否则极易导致订单错失当日发运窗口，进而引发延迟交付。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 波次截单 | Wave Cutoff |
| 波次管理 | Wave Management / Wave Planning |
| 拣货截单 | Pick Cutoff |
| 订单截单时间 | Order Cutoff Time |
| 发运截单 | Shipping Cutoff |

## 相关术语

- Order Cutoff Time（订单截单时间）
- Dock Cutoff（码头截单时间）
- Pick List（拣货单）
- Fulfillment Center（履约中心）
- Shipping Window（发货窗口期）

## 常见误区

- 误以为Wave Cutoff就是整票货物的最终海关截关时间（Customs Cutoff），实际上它属于仓库内部作业的时间节点，早于物理运输的截单。
- 认为波次截单后仍可随时加单或修改收货地址，实际上系统锁定后，任何变更都无法实时反映在当前的拣货作业中。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
