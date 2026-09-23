---
name: freedom-human-design
description: 整理人類圖共讀筆記、來源與反思提問，保留不同解讀及本人選擇。
---

# 人類圖共讀與研究手冊

## 適用範圍

人類圖是供討論與自我反思的詮釋框架；本包不提供科學診斷、醫療建議、能力認證或職業配對。

## 輸入

- 一本已合法取得的讀物、公開文章或自己寫的摘要
- 這次想討論的概念與可查來源連結
- 參與者願意公開的匿名反思；不需要出生時間、出生地或真實姓名

## 執行步驟

1. 複製 templates/reading-notes.md，先寫來源與自己的轉述，不整段搬運書籍或課程。
2. 把「原作者主張」「自己的解讀」「生活觀察」分欄，留一欄不同觀點。
3. 用 templates/discussion-plan.md 排出共讀與自由回應；參與者可跳過任何個人分享。
4. 填 templates/research-notes.json 並驗證來源、主張標籤及匿名資料狀態。
5. 以去識別範例提交 PR；讓讀者看見限制與待釐清問題，不替他人貼上固定標籤。

## 輸出與驗收

一份附來源、不同觀點與匿名反思提問的共讀紀錄。

```sh
python3 scripts/validate.py examples/research-notes.json
python3 -m unittest discover -s tests -v
```

驗證結果只描述結構檢查；實地確認、內容授權、參與者同意及實際成效必須另由當事人提供，未知保持未知。不要把模板範例當成已發生事實。

## 協作交接

1. 查 [BACKLOG.md](BACKLOG.md)、[Issues](https://github.com/FreeTWAI-AI/freedom-skill-human-design/issues) 與 [PR](https://github.com/FreeTWAI-AI/freedom-skill-human-design/pulls) 的最新狀態，避免重複工作。
2. 在已授權範圍內選一個待辦，用自己的 Fork／分支製作最小可審查變更。尚未派工時先在 Issue 協調；當前使用者已明確派工則直接沿用。
3. PR 目標 `https://github.com/FreeTWAI-AI/freedom-skill-human-design:main`。列 task id、變更用途、實跑命令、結果、未驗證項目及相依 PR。
4. 保留作者、來源與審查結果。Agent 可讀此技能，不因此取得帳號、發送訊息、付款、現場設備或平台資料的操作權。

## 邊界

- 不收集出生日期、精確出生時間、出生地或完整人類圖；這份入門包不需要這些資料。
- 不把人類圖類型用來篩选聘雇、健康診斷、信用、會員權限或強制定位。
- 來源授權要逐份確認；不得公開複製付費課程、圖表或書籍長篇內容。
