# 货运物流字典（Freight & Logistics Dictionary）

中英对照的货运物流术语词典网站。**零代码运营**：GitHub 生态全自动 —— AI 生成词条 → Pull Request 人工审核 → 自动构建 → GitHub Pages 发布。

## 工作原理

```text
terms/terms.csv（术语表）
      ↓  GitHub Actions 每天 10:00（北京时间）自动运行
Gemini API 生成词条 Markdown（scripts/generate_entries.py）
      ↓
自动创建 Pull Request
      ↓  人工审核后点 Merge
HugoBlox 自动构建（.github/workflows/build.yml）
      ↓
GitHub Pages 免费托管上线
```

- 站点框架：[HugoBlox](https://hugoblox.com) Documentation 模板（MIT）
- 词条生成：Gemini API（脚本只用 Python 标准库，无需装依赖）
- 人工审核门槛：AI 初稿必须经 PR 审核合并才会发布

## 首次部署步骤（10 分钟）

### 1. 创建 GitHub 仓库

在本目录执行：

```bash
git init
git add -A
git commit -m "init: 货运物流字典站点"
gh repo create freight-logistics-dictionary --public --source=. --push
```

（若未登录 GitHub CLI，先执行 `gh auth login` 按提示操作）

### 2. 配置 Gemini API Key

1. 到 [Google AI Studio](https://aistudio.google.com/apikey) 免费领取 API Key
2. 仓库页面 → `Settings` → `Secrets and variables` → `Actions` → `New repository secret`
3. Name 填 `GEMINI_API_KEY`，Secret 填你的 Key

⚠️ Key 只放 Secrets，**绝不能写进代码文件**（本仓库是 public，代码所有人可见）。

### 3. 启用 GitHub Pages

仓库 `Settings` → `Pages` → `Build and deployment` → Source 选 **GitHub Actions**。

### 4. 跑一次验证

仓库 `Actions` 页 → 左侧选 **Generate dictionary entries** → **Run workflow** → 运行完成后会出现一个 PR（标题：📚 新词条初稿）→ 检查内容后点 **Merge pull request** → 网站自动构建发布 → 访问：

```text
https://bxnk-maker.github.io/freight-logistics-dictionary/
```

## 日常运营

| 你想做什么 | 怎么做 |
|---|---|
| 添加新术语 | 编辑 `terms/terms.csv` 加一行（status 填 `pending`），push 后次日自动生成，或手动 Run workflow |
| 审核词条 | Actions 跑完会在 PR 里给出新词条，检查后 Merge 即上线 |
| 改词条内容 | 直接编辑 `content/docs/<分类>/<词条>.md`，push 后自动重新部署 |
| 加新分类 | `scripts/generate_entries.py` 里的 `CATEGORY_NAMES` 加一行映射 |

## 目录结构

```text
├── terms/terms.csv            # 术语表（唯一需要日常维护的清单）
├── scripts/generate_entries.py # Gemini 词条生成脚本
├── content/docs/              # 词条内容（AI 生成 + 人工修订）
├── config/_default/           # 站点配置（标题、菜单、品牌）
└── .github/workflows/
    ├── generate-terms.yml     # 每天：生成词条 → 自动开 PR
    ├── build.yml              # 构建（HugoBlox 官方可复用工作流）
    └── deploy.yml             # 部署到 GitHub Pages
```

## 许可与免责

- 代码：MIT（见 LICENSE.md）
- 词条内容：AI 生成初稿、人工审核，仅供学习参考，不构成法律或商务建议
