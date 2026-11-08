---
title: "CUSDEC Message"
linkTitle: "报关报文"
date: 2026-11-08
type: docs
subcategory: "报关流程"
---

> 📖 分类：**关务合规** / 报关流程　｜　CUSDEC Message = 报关报文

## 定义

CUSDEC Message（Customs Declaration Message，海关申报报文）是电子数据交换（EDI）标准中用于向海关提交进出口货物报关数据的电子文件格式。它允许货代、报关行或发货人以结构化数据直接向海关系统传输货物及运输工具的详细申报信息。

## 详细说明

- 使用场景：主要应用于海关电子申报环节，涵盖一般贸易、保税物流及跨境电商等多种进出口通关模式。
- 关键规则或数字：报文通常遵循 UN/EDIFACT（联合国管理、贸易和运输电子数据交换）标准，其结构代码和字段必须严格符合目的国海关的验核逻辑，任何数据格式错误都会导致海关系统自动退单。
- 实务注意事项：发送 CUSDEC 报文前，必须确保商品编码（HS Code）、货重、件数及毛净重等核心数据与提单（B/L）、商业发票（Commercial Invoice）完全一致，避免因数据差异引发海关稽查或延误放行。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 报关报文 | CUSDEC Message |
| 海关数据交互 | Customs Data Interchange |
| 电子数据交换 | Electronic Data Interchange (EDI) |
| 报关单 | Customs Declaration |
| 报文退单 | Message Rejection |

## 相关术语

- `CUSRES Message（海关响应报文）`
- `UN/EDIFACT（联合国贸易和运输电子数据交换标准）`
- `EDI（电子数据交换）`
- `HS Code（商品编码）`
- `Customs Clearance（清关/报关）`

## 常见误区

- 误区一：认为 CUSDEC 报文就是纸质报关单的扫描件。实际上它是严格结构化的纯数据文件，而非图像或普通文档。
- 误区二：只要成功发送了 CUSDEC 报文就代表货物已顺利通关。发送成功仅表示海关系统已接收，必须收到海关的放行响应报文（如 CUSRES）后才算完成通关。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
