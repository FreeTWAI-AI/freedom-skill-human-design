# 共創待辦與里程碑

以下是原創起始規劃，**全部待認領／未開始**。沒有指定負責人、完成百分比或承諾日期。開始前查 [Issues](https://github.com/FreeTWAI-AI/freedom-skill-human-design/issues)／[PR](https://github.com/FreeTWAI-AI/freedom-skill-human-design/pulls)；把認領範圍與相依工作連回來，最新討論优先。

## M1：可複用的入門流程（planned）

完成條件：新增合成案例、模板欄位及其結構檢查；由維護者審查後才標完成。

### HUMAN-01 · 整理常見術語的多來源索引

- 狀態：proposed／未認領
- 範圍：新增原創術語表，每項列來源、原作者用法與仍有爭議的解讀。
- 驗收：以自己的話摘要；每項至少一個來源 ref；不將詮釋列為實證結論。
- 驗證：`python3 scripts/validate.py examples/research-notes.json`；`python3 -m unittest discover -s tests -v`；人工核對模板文字。
- PR 附：task id、改動檔案、範例、執行結果與未驗證事項。

### HUMAN-02 · 完善共讀主持與不分享選項

- 狀態：proposed／未認領
- 範圍：擴充討論模板，讓參與者自行決定分享程度。
- 驗收：可完全不提供出生資訊；有跳過提問與撤回公開筆記的方法；提供一份全合成討論案例。
- 驗證：`python3 scripts/validate.py examples/research-notes.json`；`python3 -m unittest discover -s tests -v`；人工核對模板文字。
- PR 附：task id、改動檔案、範例、執行結果與未驗證事項。

### HUMAN-03 · 建立主張與證據對照模板

- 狀態：proposed／未認領
- 範圍：分開記錄引用來源、反例、限制與待查問題。
- 驗收：個人觀察不變成因果主張；明確分開框架用語與可驗證事實；不產生診斷或職業決定。
- 驗證：`python3 scripts/validate.py examples/research-notes.json`；`python3 -m unittest discover -s tests -v`；人工核對模板文字。
- PR 附：task id、改動檔案、範例、執行結果與未驗證事項。

## M2：由真實使用回饋改善（planned）

M1 後，由自願使用者提供可公開、已去識別的回饋。僅把實際收到的回饋列入 Issue；不預填活動成果、人數、成效或測試成功。跨公會協作可連結原 Issue，不重複複製責任。
