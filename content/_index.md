---
title: '首页'
date: 2026-10-15
type: landing

sections:
  - block: hero
    content:
      title: 货运物流字典
      text: 中英对照的货运物流术语词典 —— 涵盖国际贸易术语、运输、单证、清关、仓储与特种货运。
      primary_action:
        text: 浏览术语词典
        url: /docs/
        icon: book-open
    design:
      spacing:
        padding: [0, 0, 0, 0]
        margin: [0, 0, 0, 0]
      css_class: ""
      background:
        color: ""

  - block: collection
    id: docs
    content:
      title: 术语分类
      text: 按业务领域浏览词条
      filters:
        folders:
          - docs
    design:
      view: article-grid
      show_date: false
---
