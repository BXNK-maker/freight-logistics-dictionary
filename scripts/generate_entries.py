#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
货运物流字典 - 词条生成脚本
读取 terms/terms.csv，对 status=pending 的术语调用 Gemini API 生成
中英对照词条 Markdown，写入 content/docs/<分类>/，并将 CSV 状态更新为 published。

仅使用 Python 标准库，无需安装任何依赖。

用法（在 GitHub Actions 中）:
  env GEMINI_API_KEY=xxx python scripts/generate_entries.py

可选环境变量:
  GEMINI_MODEL   默认 gemini-flash-lite-latest
  MAX_ENTRIES    单次运行最多生成多少条，默认 20（控制 API 用量）
"""

import csv
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TERMS_FILE = ROOT / "terms" / "terms.csv"
DOCS_DIR = ROOT / "content" / "docs"

GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-flash-lite-latest")
# 支持逗号分隔的模型链：404 或配额问题时自动切换下一个
MODEL_CHAIN = [m.strip() for m in GEMINI_MODEL.split(",") if m.strip()]
model_idx = 0
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
MAX_ENTRIES = int(os.environ.get("MAX_ENTRIES", "20"))

# 分类文件夹 -> 页面展示名（新增分类时在这里补一行即可）
CATEGORY_NAMES = {
    "trade-terms": "贸易术语",
    "transport": "运输",
    "documents": "单证",
    "customs": "清关",
    "warehousing": "仓储与配送",
    "special-cargo": "特种货运",
}

PROMPT_TEMPLATE = """你是一名资深的国际货运与物流专家，正在为一本中英对照的货运物流术语词典撰写词条。

请为术语「{term_en}」（中文：{term_zh}）撰写词条，严格遵循以下要求：

1. 内容准确、面向货代/外贸从业者，语言平实易懂。
2. 全部使用简体中文撰写（专有名词和缩写保留英文）。
3. 输出为纯 Markdown 正文（不要 YAML frontmatter，不要代码块包裹）。
4. 使用以下小节结构（用 ## 二级标题）：
   - ## 定义（2-3 句话，说清这个术语是什么）
   - ## 详细说明（要点用 - 列表，覆盖：使用场景、关键规则或数字、实务注意事项）
   - ## 中英对照（一个 Markdown 表格，3-5 行，列出与本术语相关的常用中英对照表达）
   - ## 常见误区（1-3 条，用 - 列表）
5. 总长度控制在 400-700 字之间，不要输出开场白和结束语。"""


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower()).strip("-")
    return slug or "entry"


def call_gemini(prompt: str, retries: int = 6) -> str:
    """调用 Gemini generateContent API，返回文本（支持模型降级链）。"""
    global model_idx
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{GEMINI_MODEL}:generateContent"
    )
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.3},
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": GEMINI_API_KEY,
        },
        method="POST",
    )
    last_err = None
    attempt = 0
    while attempt < retries:
        model = MODEL_CHAIN[model_idx]
        url = (
            "https://generativelanguage.googleapis.com/v1beta/models/"
            f"{model}:generateContent"
        )
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": 0.3},
        }
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "x-goog-api-key": GEMINI_API_KEY,
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            text = data["candidates"][0]["content"]["parts"][0]["text"]
            return text.strip()
        except urllib.error.HTTPError as err:
            last_err = err
            # 404/429 且还有下一个模型时，立即切换（各模型配额独立）
            if err.code in (404, 429) and model_idx < len(MODEL_CHAIN) - 1:
                model_idx += 1
                print(f"  [模型切换] {model} -> {MODEL_CHAIN[model_idx]}", flush=True)
                continue
            attempt += 1
            wait = min(attempt * 15, 45)
            print(f"  [重试 {attempt}/{retries}] {err}，{wait}s 后再试", flush=True)
            time.sleep(wait)
        except Exception as err:  # noqa: BLE001
            last_err = err
            attempt += 1
            wait = min(attempt * 15, 45)
            print(f"  [重试 {attempt}/{retries}] {err}，{wait}s 后再试", flush=True)
            time.sleep(wait)
    raise RuntimeError(f"Gemini API 调用失败: {last_err}")


def build_markdown(term_en: str, term_zh: str, category_key: str, body: str) -> str:
    category_name = CATEGORY_NAMES.get(category_key, category_key)
    # 去掉模型可能额外包的 ```markdown 围栏
    body = re.sub(r"^```(?:markdown)?\s*\n?", "", body)
    body = re.sub(r"\n?```\s*$", "", body).strip()
    frontmatter = (
        "---\n"
        f'title: "{term_en}"\n'
        f'linkTitle: "{term_zh}"\n'
        f"date: {date.today().isoformat()}\n"
        f'type: docs\n'
        "---\n\n"
        f"> 📖 分类：**{category_name}**　｜　{term_en} = {term_zh}\n\n"
        f"{body}\n\n"
        "---\n\n"
        "*本词条由 AI 生成初稿、经人工审核后发布，仅供学习参考，不构成法律或商务建议。*\n"
    )
    return frontmatter


def ensure_category_index(category_key: str) -> None:
    category_dir = DOCS_DIR / category_key
    category_dir.mkdir(parents=True, exist_ok=True)
    index_file = category_dir / "_index.md"
    if not index_file.exists():
        name = CATEGORY_NAMES.get(category_key, category_key)
        index_file.write_text(
            f"---\ntitle: \"{name}\"\nlinkTitle: \"{name}\"\n---\n\n"
            f"本分类收录「{name}」相关的货运物流术语。\n",
            encoding="utf-8",
        )


def main() -> int:
    if not GEMINI_API_KEY:
        print("错误：未设置 GEMINI_API_KEY 环境变量", file=sys.stderr)
        return 1

    with TERMS_FILE.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    pending = [r for r in rows if r.get("status", "").strip() == "pending"]
    if not pending:
        print("没有待生成的词条（status=pending），本次运行结束。")
        return 0

    todo = pending[:MAX_ENTRIES]
    print(f"共 {len(pending)} 条待生成，本次处理 {len(todo)} 条（模型链: {' -> '.join(MODEL_CHAIN)}）\n")

    generated = 0
    consecutive_fail = 0
    for row in todo:
        term_en = row["term_en"].strip()
        term_zh = row["term_zh"].strip()
        category = row["category"].strip()
        print(f"→ 生成 {term_en} ({term_zh}) ...", flush=True)

        try:
            body = call_gemini(PROMPT_TEMPLATE.format(term_en=term_en, term_zh=term_zh))
            consecutive_fail = 0
        except RuntimeError as err:
            consecutive_fail += 1
            print(f"  ✗ 跳过：{err}", flush=True)
            if consecutive_fail >= 5:
                print("\n⚠️ 连续 5 条失败，疑似 API 配额耗尽，提前熔断退出。", flush=True)
                (ROOT / ".quota_exhausted").write_text("1", encoding="utf-8")
                break
            continue

        ensure_category_index(category)
        out_file = DOCS_DIR / category / f"{slugify(term_en)}.md"
        out_file.write_text(
            build_markdown(term_en, term_zh, category, body), encoding="utf-8"
        )
        row["status"] = "published"
        generated += 1
        print(f"  ✓ 已写入 {out_file.relative_to(ROOT)}", flush=True)
        time.sleep(2)  # 简单限速，避免触发 API 配额

    # 回写 CSV 状态
    if generated:
        fieldnames = ["term_en", "term_zh", "category", "status"]
        with TERMS_FILE.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    print(f"\n完成：本次生成 {generated} 条词条。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
