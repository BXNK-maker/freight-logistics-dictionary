# 词源种子清单（通道 A/B）

本目录存放待导入主词表 `terms/terms.csv` 的种子词条，由 `scripts/merge_seeds.py`
统一去重后合并（status=pending），再由 GitHub Actions 自动生成正文。

## 文件清单与来源

| 文件 | 通道 | 内容 | 条数 | 来源/许可 |
|-----|------|-----|----:|---------|
| container-types.csv | B | ISO 集装箱类型与箱务术语 | 26 | ISO 6346 公开标准分类，通用行业知识 |
| dg-classes.csv | B | 危险品分类与单证术语 | 30 | IMDG/IATA DGR 公开的 9 类分类框架，通用行业知识 |
| ports.csv | B | 全球主要集装箱港口 | 125 | 公开港口名录，行业常识 |
| airports.csv | B | 全球主要货运机场 | 75 | IATA 公开机场名录，行业常识 |

> 注：以上均为"事实性名称与公开分类框架"（名称、编号、类别划分），
> 不含任何商业词库的表达性内容；正文释义由本仓库 AI 生成并经审核。

## 待编制（阶段 1 启动时补充）

- HS 编码 4 位品目标题（~1,240 条，需对照 WCO HS 2022 官方公开表核验）
- Incoterms 2020 变体与费用条款扩展
- 维基百科物流/贸易类目公开术语抽取

## 合并流程

```bash
# 1. 干跑查看报告
python scripts/merge_seeds.py --dry-run
# 2. 正式合并（自动备份 terms.csv.bak）
python scripts/merge_seeds.py
# 3. 校验
python scripts/validate_terms.py
```
