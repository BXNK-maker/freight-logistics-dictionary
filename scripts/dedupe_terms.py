#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""词条去重扫描（三级去重）：精确匹配 -> 归一化匹配 -> 相似度匹配。

仅用 Python 标准库。只读扫描 terms/terms.csv（可含 terms/seed/*.csv），
输出重复报告，不修改任何文件。

用法:
  python scripts/dedupe_terms.py            # 扫描主词表
  python scripts/dedupe_terms.py --seed     # 主词表 + 种子词表
  python scripts/dedupe_terms.py --threshold 0.90
"""

import csv
import difflib
import json
import re
import string
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TERMS_FILE = ROOT / "terms" / "terms.csv"
SEED_DIR = ROOT / "terms" / "seed"

_PUNCT = set(string.punctuation + "－—－·．。、，；：（）()【】[]「」『』")


def normalize(text: str) -> str:
    """归一化：小写、去标点、去空格、统一连字符。"""
    t = text.strip().lower()
    t = t.replace("–", "-").replace("—", "-")
    t = "".join(ch for ch in t if ch not in _PUNCT and not ch.isspace())
    return t


def load_rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return [r for r in csv.DictReader(f) if (r.get("term_en") or "").strip()]


def main() -> int:
    args = sys.argv[1:]
    scan_seed = "--seed" in args
    threshold = 0.92
    if "--threshold" in args:
        threshold = float(args[args.index("--threshold") + 1])

    rows = load_rows(TERMS_FILE)
    sources = {i: "main" for i in range(len(rows))}
    if scan_seed:
        for seed_file in sorted(SEED_DIR.glob("*.csv")):
            seed_rows = load_rows(seed_file)
            for r in seed_rows:
                sources[len(rows)] = f"seed:{seed_file.name}"
                rows.append(r)

    print(f"扫描词条总数: {len(rows)}（含种子: {scan_seed}）")

    # 1) 精确 + 归一化匹配
    seen: dict[str, int] = {}
    exact_dupes = []
    zh_seen: dict[str, int] = {}
    zh_dupes = []
    for i, r in enumerate(rows):
        en = normalize(r.get("term_en", ""))
        zh = (r.get("term_zh") or "").strip()
        if en and en in seen:
            exact_dupes.append((seen[en], i, "EN-normalized"))
        elif en:
            seen[en] = i
        if zh and zh in zh_seen:
            zh_dupes.append((zh_seen[zh], i, "ZH-exact"))
        elif zh:
            zh_seen[zh] = i

    # 2) 相似度匹配（英文归一化后两两比较，n 大时分桶加速：按首字母分桶）
    sim_dupes = []
    buckets: dict[str, list[int]] = {}
    for i, r in enumerate(rows):
        en = normalize(r.get("term_en", ""))
        if not en:
            continue
        for key in {en[:1], en[:2], en[:3]}:
            buckets.setdefault(key, []).append(i)
    checked: set[tuple[int, int]] = set()
    for key, idxs in buckets.items():
        for a in range(len(idxs)):
            for b in range(a + 1, len(idxs)):
                i, j = idxs[a], idxs[b]
                if (i, j) in checked or (j, i) in checked:
                    continue
                checked.add((i, j))
                en_i = normalize(rows[i].get("term_en", ""))
                en_j = normalize(rows[j].get("term_en", ""))
                if abs(len(en_i) - len(en_j)) > 6:
                    continue
                ratio = difflib.SequenceMatcher(None, en_i, en_j).ratio()
                if ratio >= threshold:
                    sim_dupes.append((i, j, f"sim={ratio:.2f}"))

    def report(pairs, label):
        print(f"\n== {label}: {len(pairs)} 组 ==")
        for i, j, why in pairs[:60]:
            si, sj = sources.get(i, "?"), sources.get(j, "?")
            print(f"  [{why}] #{i}({si}) {rows[i].get('term_en','')} / {rows[i].get('term_zh','')}"
                  f"  <->  #{j}({sj}) {rows[j].get('term_en','')} / {rows[j].get('term_zh','')}")

    report(exact_dupes, "英文重复（精确/归一化）")
    report(zh_dupes, "中文重复（精确）")
    report(sim_dupes, f"英文高相似（>={threshold}）")

    total = len(exact_dupes) + len(zh_dupes) + len(sim_dupes)
    print(f"\n总计问题组数: {total}")
    print("结论: " + ("存在重复，需在合并种子前处理" if total else "词表干净 ✓"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
