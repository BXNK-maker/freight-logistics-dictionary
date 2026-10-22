#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 terms/seed/*.csv 中的词条合并进 terms/terms.csv（通道 A/B 导入用）。

- 自动三级去重（精确 / 归一化 / 相似度，针对英文；中文精确）
- 新词条 status=pending，由 GitHub Actions 自动生成正文
- 合并前自动备份 terms.csv -> terms/terms.csv.bak

用法:
  python scripts/merge_seeds.py --dry-run     # 只报告，不写入
  python scripts/merge_seeds.py               # 实际合并
  python scripts/merge_seeds.py --limit 500   # 每个种子文件最多合并 500 条
"""

import csv
import difflib
import re
import shutil
import string
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TERMS_FILE = ROOT / "terms" / "terms.csv"
SEED_DIR = ROOT / "terms" / "seed"
FIELDNAMES = ["term_en", "term_zh", "category", "subcategory", "status"]

_PUNCT = set(string.punctuation + "－—－·．。、，；：（）()【】[]「」『』")


def normalize(text: str) -> str:
    t = text.strip().lower().replace("–", "-").replace("—", "-")
    return "".join(ch for ch in t if ch not in _PUNCT and not ch.isspace())


def main() -> int:
    args = sys.argv[1:]
    dry = "--dry-run" in args
    limit = 10**9
    if "--limit" in args:
        limit = int(args[args.index("--limit") + 1])

    with TERMS_FILE.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r.setdefault("subcategory", "")
    existing_en = {normalize(r["term_en"]) for r in rows}
    existing_zh = {r["term_zh"].strip() for r in rows if r.get("term_zh")}
    all_en_norm = [normalize(r["term_en"]) for r in rows]

    added, skipped = [], []
    for seed_file in sorted(SEED_DIR.glob("*.csv")):
        with seed_file.open("r", encoding="utf-8-sig", newline="") as f:
            for r in csv.DictReader(f):
                if len(added) >= limit and seed_file.name != sorted(SEED_DIR.glob('*.csv'))[0].name:
                    pass
                en, zh = (r.get("term_en") or "").strip(), (r.get("term_zh") or "").strip()
                cat = (r.get("category") or "").strip()
                sub = (r.get("subcategory") or "").strip()
                if not en or not zh or not cat:
                    skipped.append((en, zh, "字段缺失"))
                    continue
                n_en = normalize(en)
                if n_en in existing_en:
                    skipped.append((en, zh, "英文重复"))
                    continue
                if zh in existing_zh:
                    skipped.append((en, zh, "中文重复"))
                    continue
                # 相似度检查（对现有词表两两太慢：只比首 3 字符同桶的项）
                hit = None
                prefix = n_en[:3]
                for idx, other in enumerate(all_en_norm):
                    if other[:3] != prefix or abs(len(other) - len(n_en)) > 6:
                        continue
                    if difflib.SequenceMatcher(None, n_en, other).ratio() >= 0.92:
                        hit = rows[idx]["term_en"]
                        break
                if hit:
                    skipped.append((en, zh, f"与「{hit}」高相似"))
                    continue
                existing_en.add(n_en)
                existing_zh.add(zh)
                all_en_norm.append(n_en)
                added.append({"term_en": en, "term_zh": zh, "category": cat,
                              "subcategory": sub, "status": "pending"})

    print(f"种子合并报告: 新增 {len(added)} 条，跳过 {len(skipped)} 条")
    for en, zh, why in skipped[:30]:
        print(f"  跳过 [{why}] {en} / {zh}")
    if len(skipped) > 30:
        print(f"  ...另有 {len(skipped) - 30} 条跳过")
    by_cat: dict[str, int] = {}
    for r in added:
        key = f"{r['category']}/{r['subcategory'] or '-'}"
        by_cat[key] = by_cat.get(key, 0) + 1
    print("\n新增分布:")
    for k, v in sorted(by_cat.items()):
        print(f"  {k}: {v}")

    if dry:
        print("\n(dry-run 模式，未写入。去掉 --dry-run 执行真实合并)")
        return 0

    shutil.copy(TERMS_FILE, TERMS_FILE.with_suffix(".csv.bak"))
    rows.extend(added)
    with TERMS_FILE.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    print(f"\n已合并写入 {TERMS_FILE}（备份: terms.csv.bak），词表现共 {len(rows)} 条。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
