---
title: "SWIFT MT707"
linkTitle: "SWIFT 信用证修改报文"
date: 2026-11-22
type: docs
subcategory: "信用证实务"
---

> 📖 分类：**物流金融** / 信用证实务　｜　SWIFT MT707 = SWIFT 信用证修改报文

## 定义

SWIFT MT707 是国际结算中用于修改信用证（Letter of Credit）条款的标准电文格式，英文全称为 SWIFT Message Type 707: Amendment to Documentary Credit。当买卖双方在合同执行过程中需要对原信用证的金额、效期、装运期、单据要求等内容做出变更时，开证行会通过 SWIFT 系统向通知行发送此报文。

## 详细说明

- 使用场景：当贸易合同发生变更（如延期交货、增减货量、修改单据条款等），申请人（买方）通过开证行发出 MT707，以修改已生效的 MT700 原证。
- 关键规则：MT707 必须明确标注原信用证编号、修改序号（Amendment Number），并且每一项修改都必须指明是“修改”（Amend）还是“取消”（Cancel）。
- 实务注意事项：在收到 MT707 之前，受益人（卖方）切勿盲目按照口头或买方邮件变更单据，必须等待通知行正式转交 MT707 修改通知书。受益人审核修改内容后，需决定接受（Accept）或拒绝（Reject），若部分接受可能导致信用证失效。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| 信用证修改报文 | SWIFT MT707 / Amendment to Documentary Credit |
| 修改序号 | Amendment Number |
| 接受/拒绝修改 | Accept / Reject Amendment |
| 原信用证 | Original Documentary Credit (MT700) |

## 相关术语

- MT700（信用证开证报文）
- MT799（信用证自由格式报文）
- Amendment of LC（信用证修改）
- Beneficiary（受益人）
- Advising Bank（通知行）

## 常见误区

- 误区一：认为收到买方的修改确认邮件就可以安全发货。实际上，只有通过银行系统正式接收到 MT707 报文，信用证条款才算法律意义上的变更。
- 误区二：认为修改信用证只需要改动金额或日期。任何文字描述、单据要求的微调都必须通过 MT707 规范体现，否则极易导致交单时产生不符点（Discrepancy）。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
