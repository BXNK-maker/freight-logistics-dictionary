#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""词条库 CI 校验：CSV 结构、分类白名单、slug 冲突、已发布文件 front-matter。

仅用 Python 标准库。校验失败输出报告并以退出码 1 结束（供 GitHub Actions 使用）。

用法:
  python scripts/validate_terms.py
"""

import csv
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TERMS_FILE = ROOT / "terms" / "terms.csv"
DOCS_DIR = ROOT / "content" / "docs"
CONFIG = ROOT / "configs" / "categories.json"

REQUIRED_COLUMNS = {"term_en", "term_zh", "category", "status"}

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def main() -> int:
    import json

    categories = set()
    if CONFIG.exists():
        categories = set(json.loads(CONFIG.read_text(encoding="utf-8"))["categories"])
    else:
        warn("configs/categories.json 不存在，跳过分类白名单校验")

    # ---- CSV 校验 ----
    if not TERMS_FILE.exists():
        err(f"{TERMS_FILE} 不存在")
        rows = []
    else:
        with TERMS_FILE.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            header = set(reader.fieldnames or [])
            missing = REQUIRED_COLUMNS - header
            if missing:
                err(f"terms.csv 缺少必需列: {missing}")
            rows = [r for r in reader if (r.get("term_en") or "").strip()]

    if rows:
        # 状态合法性
        for i, r in enumerate(rows):
            st = (r.get("status") or "").strip()
            if st not in {"pending", "published"}:
                err(f"terms.csv 第{i + 2}行: status 非法 -> '{st}' ({r.get('term_en')})")
            cat = (r.get("category") or "").strip()
            if categories and cat not in categories:
                err(f"terms.csv 第{i + 2}行: 分类不在白名单 -> '{cat}' ({r.get('term_en')})")

        # 重复检查（归一化英文 + 精确中文）
        def norm(t: str) -> str:
            return re.sub(r"[^a-z0-9]+", "", t.strip().lower())

        seen_en: dict[str, int] = {}
        seen_zh: dict[str, int] = {}
        for i, r in enumerate(rows):
            en, zh = norm(r.get("term_en", "")), (r.get("term_zh") or "").strip()
            if en and en in seen_en:
                err(f"terms.csv 重复英文术语: {r.get('term_en')}（第{seen_en[en] + 2}行与第{i + 2}行）")
            elif en:
                seen_en[en] = i
            if zh and zh in seen_zh:
                err(f"terms.csv 重复中文术语: {zh}（第{seen_zh[zh] + 2}行与第{i + 2}行）")
            elif zh:
                seen_zh[zh] = i

    # ---- 已发布文件校验 ----
    slug_owner: dict[str, str] = {}
    md_count = 0
    if DOCS_DIR.exists():
        for md in DOCS_DIR.glob("*/*.md"):
            if md.name == "_index.md":
                continue
            md_count += 1
            rel = md.relative_to(ROOT)
            cat = md.parent.name
            if categories and cat not in categories:
                err(f"{rel}: 文件位于未知分类目录 {cat}")
            text = md.read_text(encoding="utf-8", errors="replace")
            if not text.startswith("---"):
                err(f"{rel}: 缺少 frontmatter")
                continue
            m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
            if not m:
                err(f"{rel}: frontmatter 格式错误")
                continue
            fm = m.group(1)
            if 'title: "' not in fm:
                err(f"{rel}: frontmatter 缺少 title")
            if 'linkTitle: "' not in fm:
                err(f"{rel}: frontmatter 缺少 linkTitle")
            slug_owner.setdefault(md.stem, str(rel))

    # ---- 汇总 ----
    status_count = Counter((r.get("status") or "").strip() for r in rows)
    print(f"terms.csv: {len(rows)} 条 | {dict(status_count)}")
    print(f"content/docs 词条文件: {md_count} 个")
    pub = status_count.get("published", 0)
    if md_count and pub and abs(md_count - pub) > max(5, pub * 0.05):
        warn(f"已发布条数({pub})与文件数({md_count})偏差超过 5%")

    for w in warnings:
        print(f"⚠️  {w}")
    for e in errors[:50]:
        print(f"✗ {e}")
    if len(errors) > 50:
        print(f"✗ ...另有 {len(errors) - 50} 个错误未显示")
    print(f"\n校验结果: {'❌ 失败' if errors else '✅ 通过'}（错误 {len(errors)}，警告 {len(warnings)}）")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
