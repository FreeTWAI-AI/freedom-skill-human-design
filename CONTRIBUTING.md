# 一起改善技能書

先看 [BACKLOG.md](BACKLOG.md)、[Issues](https://github.com/FreeTWAI-AI/freedom-skill-human-design/issues) 和 [PR](https://github.com/FreeTWAI-AI/freedom-skill-human-design/pulls)。選一個小範圍，寫清預期成果、準備改哪些檔案、驗收方式；維護者已直接派工時沿用授權。

1. Fork 本倉，從 main 開自己的分支。
2. 手冊與模板使用繁體中文；程式和結構化欄位可用英文。公開範例只用合成資料。
3. 保留來源與授權，避免整段搬運教材；新內容以本倉 MIT 授權提交。
4. 執行 `python3 scripts/validate.py examples/research-notes.json` 與 `python3 -m unittest discover -s tests -v`。
5. PR 送到 FreeTWAI-AI/freedom-skill-human-design:main，附 task id、前後差異、實測結果與仍需真人核對的事項。

審查與合併由 repo 維護者負責，平台公會身分不取代審查權。Agent 先讀 [AGENTS.md](AGENTS.md)。尚未驗證的實地成果保持未驗證；不代發邀請、訂場、付款或操作設備。
