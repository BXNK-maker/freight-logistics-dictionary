---
title: "GS1-128 Barcode"
linkTitle: "GS1-128条码"
date: 2026-11-22
type: docs
subcategory: "数据标准"
---

> 📖 分类：**物流数字化** / 数据标准　｜　GS1-128 Barcode = GS1-128条码

## 定义

GS1-128条码（原称UCC/EAN-128）是一种高密度的一维条码，广泛应用于全球供应链的物流、仓储和零售配送环节。它能够在一个条码中承载丰富的数据信息，包括产品代码、批次号、生产日期、序列号以及物流货运单元序列号等。

## 详细说明

- 使用场景：主要用于外包装、托盘标签和物流运输标签（如SSCC托盘标签），在仓库收货、分拣、盘点以及零售商供应链交接时进行高效扫描。
- 关键规则或数字：该条码基于Code 128编码字符集，最大特点是使用“应用标识符”（Application Identifiers，简称AI）来界定后面数据的含义。常用的AI如(00)代表SSCC（物流序列号），(02)代表商品代码，(10)代表批次号，每个AI都有严格的格式和长度规范。
- 实务注意事项：货代和外贸人员在制作发往大型零售商（如Walmart、Target等）的托盘标签时，必须严格遵守客户及GS1组织的标准，确保AI括号的使用、条码尺寸、打印对比度及粘贴位置准确无误，否则会导致仓库扫描失败并产生高额罚款。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| GS1-128条码 | GS1-128 Barcode |
| 应用标识符 | Application Identifier (AI) |
| 物流序列号 | Serial Shipping Container Code (SSCC) |
| 托盘标签 | Pallet Label / Shipping Label |

## 相关术语

- SSCC (Serial Shipping Container Code，系列货运包装代码)
- UCC/EAN-128 (Uniform Code Council / European Article Numbering-128，统一代码委员会/欧洲物品编码128，GS1-128的前身)
- EDI (Electronic Data Interchange，电子数据交换)
- RFID (Radio Frequency Identification，无线射频识别)

## 常见误区

- 误区一：认为GS1-128条码只能编码数字。实际上，它是一种字母数字条码（Alphanumeric），可以同时编码大小写字母、数字和特殊字符。
- 误区二：混淆条码与应用标识符（AI）。AI本身是数据的一部分，打印在条码下方时通常用括号括起（仅供人类识读），但在条码符号中会通过特殊的FNC1字符进行编码转换，扫描设备会自动识别。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
