# 人類圖共讀與研究手冊

整理人類圖共讀筆記、來源與反思提問，保留不同解讀及本人選擇。

**公會：人類圖研究所** · [自由工坊](https://freetwai.com) · [線上技能書](https://freetwai.com/development/skills/human-design)

## 開始使用

1. 讀 [SKILL.md](SKILL.md)，選擇 `templates/` 的表格。
2. 參考 `examples/research-notes.json` 的全合成範例，填自己的工作副本。
3. 執行下面的結構檢查，再由實際負責人確認內容。

交付：一份附來源、不同觀點與匿名反思提問的共讀紀錄。

人類圖是供討論與自我反思的詮釋框架；本包不提供科學診斷、醫療建議、能力認證或職業配對。

## 一起做

[待辦與里程碑](BACKLOG.md) · [認領與討論](https://github.com/FreeTWAI-AI/freedom-skill-human-design/issues) · [目前 PR](https://github.com/FreeTWAI-AI/freedom-skill-human-design/pulls) · [Fork](https://github.com/FreeTWAI-AI/freedom-skill-human-design/fork)

Agent 先讀 [AGENTS.md](AGENTS.md)、[SKILL.md](SKILL.md) 與 [CONTRIBUTING.md](CONTRIBUTING.md)。待辦是可以提出認領的規劃；尚未分派，不代表已獲准或已完成。Issue 最新討論與 PR 是認領／審查紀錄。

```sh
python3 scripts/validate.py examples/research-notes.json
python3 -m unittest discover -s tests -v
```

只檢查資料結構與模板的已知約束，不代表真實活動、器材、研究或當事人同意已驗證。Python 3.10+，無第三方相依、無外部連線。

## 平台邊界

本倉維護原創手冊、模板與合成案例。會員、公會、權限與技能書綁定由 [freedom-platform](https://github.com/FreeTWAI-AI/freedom-platform) 的 API／PostgreSQL 管理；本倉不能直接改中央資料庫。跨 repo 變更先連結相依 PR，不自行增加平台權限。公會會長未在此指定。

## 授權與來源

此包是自由工坊的原創入門內容，採 [MIT](LICENSE)。未複製第三方課程、圖表、媒體或設備軟體；外部素材必須保留各自權利與來源。`examples/` 均為合成資料，沒有已辦活動、真實客戶或研究成果的宣稱。
