---
title: "REST API"
linkTitle: "REST接口"
date: 2026-11-22
type: docs
subcategory: "数据标准"
---

> 📖 分类：**物流数字化** / 数据标准　｜　REST API = REST接口

## 定义
REST API（Representational State Transfer Application Programming Interface）是一种基于 HTTP 协议的软件架构风格接口。在货运物流领域，它允许不同的货代系统、船公司官网和跨境电商平台之间进行安全、高效的数据实时交互。

## 详细说明
- 使用场景：广泛应用于船期查询、舱位预定、货物追踪（轨迹查询）、电子舱单提交及海关申报等环节。
- 关键规则或数字：通常基于标准 HTTP 方法（如 GET 用于查询、POST 用于提交），数据格式多采用轻量级的 JSON，响应时间通常要求在毫秒级别以支持高并发。
- 实务注意事项：调用外部 API 时必须妥善保管 API Key 或 Token 以防数据泄露；同时需注意服务商的调用频率限制（Rate Limit），避免因超限导致查询失败或IP被封。

## 中英对照

| 中文表达 | 英文表达 |
| :--- | :--- |
| REST接口 | REST API |
| 应用程序接口 | Application Programming Interface |
| 数据传输 | Data Transfer / Data Transmission |
| 调用限制 | Rate Limit / Call Limitation |
| 实时追踪 | Real-time Tracking |

## 相关术语
- `API Key（接口密钥）`
- `JSON（JavaScript对象表示法）`
- `Webhook（网络钩子）`
- `EDI（电子数据交换）`
- `Payload（有效负载）`

## 常见误区
- 认为 REST API 是一种具体的软件或数据库：实际上它只是一种规范和通信协议，本身不存储数据。
- 混淆 REST API 与传统 EDI：传统 EDI 多采用固定格式和专线传输，而 REST API 基于互联网和标准 HTTP 协议，更加灵活且开发成本低。

---

*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*
