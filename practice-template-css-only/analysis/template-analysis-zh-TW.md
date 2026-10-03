# Template 部分分析

## 題目真正評量的內容

四個 template 並不是同一套版面換 palette。每套都要同時呈現三層差異：

1. **Layout architecture**：導覽列位置、內容流向與 viewport 行為不同。
2. **Visual system**：字體、間距、邊框、陰影與色彩變數不同。
3. **Signature effect**：每套有一個可單獨辨識、可評分的 CSS 動畫或互動效果。

因此最好的實作策略，是先完成可共用的元件行為，再為每個 template 建立自己的 layout 與 visual rules。不要先複製整份 CSS 再只換顏色。

## 四套 template 的能力矩陣

| Template | 版面架構 | 招牌效果 | 額外難點 |
|---|---|---|---|
| A / Simple | sticky top horizontal nav | button sweep-fill | 乾淨層級、focus 樣式 |
| B / Elegant | sticky left sidebar | gallery filter reveal + caption | 側欄與內容 offset、低彩度質感 |
| C / Cyber | fixed bottom dock | terminal typing + caret | dark default、system light variant |
| D / Colorful | full-viewport sections + fixed right rail | recommended plan pulse ring | mandatory scroll snap、固定導覽避讓 |

## 共用 HTML hooks 的目的

- `input[type="radio"] + label`：tabs 與 slider 的 CSS state machine。
- `.lightbox:target`：不使用 JavaScript 的 overlay 開關。
- `[data-size="large"]`：mosaic 中的跨欄項目。
- `[data-category]::after`：gallery caption。
- `[data-icon]::before`、`[data-value]::before`、`[data-year]::before`：從資料屬性產生顯示內容。
- `tr:has(.recommended)`：強調整個 pricing row，而非只標示單一 cell。
- `details[open]`：accordion 展開狀態。
- `:focus-within`：鍵盤可操作的 theme dropdown。
- `:user-invalid`：避免頁面初次載入就出現錯誤狀態。

## 容易失分的地方

- 用 `display: none` 隱藏 radio，導致鍵盤無法聚焦。
- tabs 只改 label 樣式，沒有真正隱藏非選取 panel。
- slider 用淡入淡出，沒有水平 translate 的滑動。
- gallery 永遠套 mosaic，沒有「剛好六張」才跨欄的條件。
- dropdown 只有 hover，鍵盤 focus 無法開啟。
- pricing 只強調 `.recommended` cell，沒有強調整列。
- Cyber 把 light mode 做成手動 toggle，而不是跟隨系統偏好。
- Colorful 只有 `scroll-snap-type`，但 section 沒有對應的 `scroll-snap-align` 或 viewport 高度。
- 動畫沒有 `prefers-reduced-motion` fallback。

## 建議時間配置（120 分鐘練習版）

- 0-15 分：變數、reset、共用 typography 與 focus-visible。
- 15-45 分：tabs、slider、gallery、lightbox。
- 45-65 分：cards、stats、timeline、pricing、FAQ、form。
- 65-100 分：套用指定 template layout 與 signature effect。
- 100-120 分：RWD、鍵盤、reduced motion、回歸測試。

