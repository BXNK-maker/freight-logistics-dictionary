---
title: "Empty Ledger"
linkTitle: "台账空转"
date: 2026-11-10
type: docs
subcategory: "加工贸易"
---

> 📖 分类：**关务合规** / 加工贸易　｜　Empty Ledger = 台账空转

## 定义

台账空转（Empty Ledger）是指在集装箱运输和场站管理中，系统中记录的空箱进出台账与堆场实际物理库存不符，导致数据流与物流脱节的异常状态。该现象通常由于数据录入滞后、系统漏打或单证流转错误引起。


## 详细说明

- 使用场景：主要出现在港口堆场（CY）、内陆集装箱货运站（CFS）以及船公司（Carrier）的空箱管理与对账环节。
- 关键规则或数字：在标准EDI（电子数据交换）传输中，集装箱门到门或提还箱信息应在24小时内同步更新；若系统台账与实物盘点差异率超过1%，即触发出库对账预警。
- 实务注意事项：操作人员必须确保每一次提空（Gate-out Empty）或还空（Gate-in Equipment Return）都有对应的设备交接单（EIR）支撑，避免因台账空转导致后续提单无法背箱或产生巨额滞箱费（Demurrage）。


## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 台账空转 | Empty Ledger |
| 设备交接单 | Equipment Interchange Receipt (EIR) |
| 空箱盘点 | Empty Container Inventory Check |
| 电子数据交换 | Electronic Data Interchange (EDI) |


## 相关术语

- `EIR (Equipment Interchange Receipt)`
- `Demurrage & Detention (滞箱费与滞期费)`
- `CY/CY (场站到场站)`
- `Container Tracking (集装箱追踪)`


## 常见误区

- 误区一：认为台账空转只是简单的电脑数据错误，不会产生实际经济损失。事实上，它常掩盖空箱盗抢、错还或漏计费等严重问题。
- 误区二：盲目信任系统自动生成的库存报表，不定期进行现场实物盘点，导致财务对账时出现坏账。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
