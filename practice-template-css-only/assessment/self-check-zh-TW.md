# 自評與測試清單（100 分）

## A. 鎖定結構與 CSS 架構（10 分）

- [ ] 四份 HTML 除 CSS 路徑外完全一致（4）
- [ ] 每套只載入一份本地 CSS，沒有 JavaScript（2）
- [ ] 規格中的 CSS variables 名稱與值正確，並有實際使用（4）

## B. CSS-only 互動元件（35 分）

- [ ] Tabs：僅 active panel 顯示；label 有 active 狀態（5）
- [ ] Slider：三張水平 translate；控制點 active；有 transition（5）
- [ ] Lightbox：六張都可開啟與關閉；overlay 可完整覆蓋 viewport（5）
- [ ] FAQ：`details/summary` 展開狀態清楚（3）
- [ ] Dropdown：hover 與 keyboard focus 都可使用（4）
- [ ] Form：初次載入不顯示錯誤；互動後 invalid 才顯示（5）
- [ ] Email 與 PDF link icon 由 CSS 產生（3）
- [ ] 頁內連結 smooth scroll；reduced motion 時停用（5）

## C. 資料 hooks 與條件式版面（20 分）

- [ ] feature icon 來自 `data-icon`（3）
- [ ] statistic number 來自 `data-value`（3）
- [ ] timeline badge 來自 `data-year`，highlight 有差異（3）
- [ ] pricing 整列因 `.recommended` 而被強調（3）
- [ ] gallery 在 6 張時為 mosaic；改成 5 或 7 張時回到 regular grid（5）
- [ ] nav 在 5 項時 compact；改成 4 項時恢復 default（3）

## D. Template 專屬特徵（25 分）

- [ ] A：sticky top nav + sweep-fill（5）
- [ ] B：sticky left sidebar + filter reveal/caption（5）
- [ ] C：fixed bottom dock + typing/caret + system light mode（7）
- [ ] D：full viewport sections + right rail + mandatory snap + pulse ring（8）

## E. 響應式與可及性（10 分）

- [ ] 360、768、1280 px 均無水平溢位（3）
- [ ] radio 以 visually-hidden 技術處理，仍可 keyboard focus（2）
- [ ] 每個互動元件都有清楚的 `:focus-visible`（2）
- [ ] 色彩對比、touch target、reduced motion 合理（3）

## 快速回歸案例

1. 只用鍵盤依序操作 nav、tabs、slider、gallery、FAQ、dropdown 與 form。
2. 將 gallery item 暫時刪成五張，確認 large item 不再跨欄。
3. 將 nav 暫時刪成四項，確認 compact 尺寸取消。
4. 在系統 dark/light preference 間切換，只有 Cyber 會改 scheme。
5. 開啟 reduce motion，確認 typing、pulse、slider transition 與 smooth scroll 被停用。

