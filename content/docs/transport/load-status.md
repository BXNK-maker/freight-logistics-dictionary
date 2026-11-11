---
title: "Load Status"
linkTitle: "重空箱状态"
date: 2026-11-11
type: docs
subcategory: "码头信息化"
---

> 📖 分类：**运输** / 码头信息化　｜　Load Status = 重空箱状态

## 定义

Load Status（重空箱状态）是指集装箱在国际货运和堆场管理中，处于装载货物（重箱）还是空置（空箱）的状态标识。准确的箱状态记录是船公司、码头和货代进行箱量调度、堆场规划以及费用结算的核心依据。

## 详细说明

- 使用场景：广泛应用于船公司官网查询、码头闸口进出港登记、堆场（CY）库存盘点以及设备交接单（EIR）的填制。
- 关键规则或数字：常见的状态代码通常简写为 F/L（Full/Loaded，重箱）与 M/MT（Mty/Empty，空箱）。在EDI报文中，重空状态直接决定了箱子是否需要计算堆存费（Storage）及是否涉及危险品特殊申报。
- 实务注意事项：拖车提空箱或还重箱时，必须核对EIR上的 Load Status 是否与实际一致。若空箱误报为重箱进港，可能导致码头拒收或产生重空状态更改费。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 重箱状态 | Full Status / Loaded Status |
| 空箱状态 | Empty Status |
| 重空状态代码 | F/M Code (Full/Empty Code) |
| 更改重空状态 | Amend Load Status |

## 相关术语

- `CY (Container Yard，集装箱堆场)`
- `EIR (Equipment Interchange Receipt，设备交接单)`
- `SOC (Shipper's Owned Container，货主自有箱)`
- `COC (Carrier's Owned Container，船公司自有箱)`

## 常见误区

- 认为集装箱的 Load Status 可以由拖车司机在闸口随意口头更改，忽略了必须通过系统或书面申请进行正式修改的流程。
- 将箱子里面装有货物但未关门的临时状态误认为已经是 Full Status，实际上只有完成装箱并办结相关场站手续后，系统状态才会正式变更为重箱。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
