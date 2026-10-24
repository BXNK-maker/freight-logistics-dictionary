---
title: "EDIFACT VERMAS"
linkTitle: "EDIFACT VGM 申报报文"
date: 2026-10-24
type: docs
subcategory: "EDI 电子数据交换"
---

> 📖 分类：**物流数字化** / EDI 电子数据交换　｜　EDIFACT VERMAS = EDIFACT VGM 申报报文

## 定义

EDIFACT VERMAS（全称：Electronic Data Interchange for Administration, Commerce and Transport - Verified Gross Mass Message）是国际航运界用于电子传输集装箱验证毛重（VGM）的标准报文。它基于联合国 EDIFACT 标准，允许托运人或其授权代表直接向船公司和码头以结构化数据格式发送集装箱的重量信息。

## 详细说明

- 使用场景：主要应用于海运集装箱出口环节，在截重日（VGM Closing Time）之前，由托运人向承运人及港口码头提交合规的重量数据，以确保船舶配载安全。
- 关键规则：报文中必须包含唯一的集装箱号、准确的重量数值（精确到公斤）、称重方法（Method 1 或 Method 2）、授权签名人姓名以及提交时间戳，符合国际海事组织（IMO）SOLAS 公约的要求。
- 实务注意事项：报文发送后应密切关注船公司或码头的回执（如 CONTRL 报文），若回执提示格式错误或数据缺失需及时修正并重新发送，避免因数据未更新而导致箱子无法进港。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 验证毛重申报报文 | EDIFACT VERMAS / VGM Message |
| 电子数据交换 | EDI (Electronic Data Interchange) |
| 称重方法一（衡器称重） | Method 1 (Weighing) |
| 称重方法二（计算称重） | Method 2 (Calculation) |
| 截重日/VGM截止时间 | VGM Closing Time |

## 相关术语

- SOLAS Convention（国际海上人命安全公约）
- VGM (Verified Gross Mass)
- Container Terminal (集装箱码头)
- Port Cut-off Time (截关时间)

## 常见误区

- 误以为 VERMAS 报文可以随舱单信息一起随意更改，实际上 VGM 一旦被码头锁定，修改需要经过复杂的审批流程并可能产生改单费。
- 认为发送了普通装箱单（IFTMIN）就等于完成了 VGM 申报，VERMAS 是独立的专用重量申报报文，不可混淆。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
