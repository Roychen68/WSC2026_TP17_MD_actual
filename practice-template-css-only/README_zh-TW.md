# CSS-only Template 練習包

這是一套依據 WorldSkills 題目能力範圍重新設計的練習素材，不是原題解答。練習重點是：在**不修改 HTML 結構**的前提下，只用 CSS 完成四套真正不同的 template。

## 你會練到什麼

- 同一份 HTML，切換四種版面架構
- 以 radio input 保存 tabs 與 slider 狀態
- 以 `:target` 實作 lightbox
- 以 `data-*`、`attr()` 與結構選擇器產生內容與狀態
- 響應式 gallery、條件式 mosaic 與 navigation compact mode
- `details/summary` accordion、dropdown、原生表單驗證狀態
- `prefers-color-scheme`、`prefers-reduced-motion` 與鍵盤操作
- 四種 template 專屬動畫與導覽配置

## 練習規則

1. `student/*.html` 為鎖定檔案。只允許修改 `<link rel="stylesheet">` 的 CSS 路徑。
2. 每個 template 只能使用自己的單一 CSS 檔。
3. 不可加入 JavaScript、外部 CSS framework 或第三方 icon library。
4. `student/images/` 不可改名或移動。
5. 先閱讀 `analysis/template-analysis-zh-TW.md`，再依 `student/spec/` 逐套完成。

## 檔案結構

```text
practice-template-css-only/
├── analysis/                       題目 template 能力拆解
├── assessment/                     自評表與測試案例
├── reference/theme-overview.svg    四套版面視覺藍圖
├── source/shared.html.tpl           鎖定 HTML 的唯一來源
├── student/
│   ├── css_only_*.html              四份鎖定 HTML
│   ├── css_only_*.css               練習用空白 CSS
│   ├── images/                      六張原創 SVG 圖片
│   └── spec/                        四套 template 規格
└── tools/build-starter.mjs          重新產生鎖定 HTML
```

## 開始方式

在此資料夾執行：

```bash
python3 -m http.server 8000 -d student
```

接著開啟 `http://localhost:8000/css_only_simple.html`。

若不小心改到 HTML，可執行：

```bash
node tools/build-starter.mjs
```

## 建議練習順序

1. Template A：先完成共用元件與基本 RWD。
2. Template B：練習側欄版型、filter 與 overlay。
3. Template C：練習變數覆寫、深淺色與 typing animation。
4. Template D：最後處理 viewport、scroll snap 與 fixed rail。

完成後使用 `assessment/self-check-zh-TW.md` 逐項驗收。

