---
title: "Process Capability Index"
linkTitle: "过程能力指数"
date: 2026-11-23
type: docs
subcategory: "质量检验"
---

> 📖 分类：**贸易术语** / 质量检验　｜　Process Capability Index = 过程能力指数

## 定义

过程能力指数（Process Capability Index，简称 **Cp** 或 **Cpk**）是评估一个生产或服务流程满足客户及标准要求能力的统计指标。在货运与物流管理中，它用于衡量物流操作（如装箱效率、单证处理时效、仓库分拣准确率等）在规定公差范围内稳定运行的程度。

## 详细说明

- 使用场景：广泛应用于现代物流质量管理（如精益物流 Lean Logistics、六西格玛 Six Sigma 项目），常用于评估第三方物流（3PL）供应商的作业稳定性，或监控冷链运输中的温度波动等关键绩效指标。
- 关键规则与标准：
  - 当 $Cpk < 1.0$ 时，说明过程能力不足，极易产生质量缺陷或延误；
  - 当 $1.0 \le Cpk < 1.33$ 时，过程基本满足要求，但需加强监控；
  - 当 $Cpk \ge 1.33$ 时，过程能力充足，达到行业优良标准；
  - 若追求极高质量（如六西格玛水平），目标通常要求 $Cpk \ge 2.0$。
- 实务注意事项：计算该指数前，必须确保物流数据已处于统计受控状态（即消除所有特殊原因引起的波动），否则计算结果将失去参考价值。

## 中英对照

| 中文表达 | 英文表达 | 适用语境 |
| :--- | :--- | :--- |
| 过程能力指数 | Process Capability Index | 整体质量与能力评估 |
| 潜在过程能力指数 | Potential Process Capability Index (Cp) | 评估无偏移时的过程潜力 |
| 实绩过程能力指数 | Process Capability Index (Cpk) | 评估考虑中心偏移后的实际能力 |
| 规格上限 / 下限 | Upper / Lower Specification Limit (USL/LSL) | 客户或标准允许的误差范围 |

## 相关术语

- `Six Sigma（六西格玛）`
- `Lean Management（精益管理）`
- `Key Performance Indicator（关键绩效指标）`
- `Statistical Process Control（统计过程控制）`
- `Root Cause Analysis（根本原因分析）`

## 常见误区

- 误区一：认为 $Cpk$ 越高代表实际产量越大。实际上，$Cpk$ 衡量的是流程的稳定性和合规性，与处理货量的绝对大小无直接因果关系。
- 误区二：忽略了过程偏离。有些操作人员只看 $Cp$（不考虑均值偏移），导致高估了实际物流服务的合格率，应当结合 $Cpk$ 综合判定。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
