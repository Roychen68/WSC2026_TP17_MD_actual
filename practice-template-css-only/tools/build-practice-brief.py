from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "student" / "brief.pdf"

FONT_PATH = Path("/System/Library/Fonts/Supplemental/Arial Unicode.ttf")
if not FONT_PATH.exists():
    FONT_PATH = Path("/Library/Fonts/Arial Unicode.ttf")
pdfmetrics.registerFont(TTFont("ArialUnicode", str(FONT_PATH)))

PAGE_W, PAGE_H = A4
NAVY = colors.HexColor("#172033")
BLUE = colors.HexColor("#3157ff")
PALE = colors.HexColor("#f3f5fa")
LINE = colors.HexColor("#dfe3ec")
MUTED = colors.HexColor("#667085")


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.line(18 * mm, 15 * mm, PAGE_W - 18 * mm, 15 * mm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(18 * mm, 9 * mm, "CSS-only Atlas · Practice Brief")
    canvas.drawRightString(PAGE_W - 18 * mm, 9 * mm, str(doc.page))
    canvas.restoreState()


styles = getSampleStyleSheet()
title = ParagraphStyle(
    "TitleTW",
    parent=styles["Title"],
    fontName="ArialUnicode",
    fontSize=25,
    leading=34,
    textColor=NAVY,
    alignment=TA_LEFT,
    spaceAfter=8 * mm,
)
h1 = ParagraphStyle(
    "H1TW",
    parent=styles["Heading1"],
    fontName="ArialUnicode",
    fontSize=17,
    leading=23,
    textColor=NAVY,
    spaceBefore=4 * mm,
    spaceAfter=3 * mm,
)
h2 = ParagraphStyle(
    "H2TW",
    parent=styles["Heading2"],
    fontName="ArialUnicode",
    fontSize=12,
    leading=17,
    textColor=BLUE,
    spaceBefore=3 * mm,
    spaceAfter=2 * mm,
)
body = ParagraphStyle(
    "BodyTW",
    parent=styles["BodyText"],
    fontName="ArialUnicode",
    fontSize=10,
    leading=16,
    textColor=NAVY,
    spaceAfter=2.5 * mm,
)
small = ParagraphStyle(
    "SmallTW",
    parent=body,
    fontSize=8.7,
    leading=13,
    textColor=MUTED,
)
center = ParagraphStyle("CenterTW", parent=body, alignment=TA_CENTER)


def p(text, style=body):
    return Paragraph(text, style)


def bullets(items):
    return [p(f"• {item}") for item in items]


story = [
    Spacer(1, 14 * mm),
    p("WORLDSKILLS WEB TECHNOLOGIES · PRACTICE", small),
    p("CSS-only Template 練習任務", title),
    p("任務目標：使用同一份鎖定 HTML，只靠四份 CSS，完成四套可辨識的 layout、visual system 與 signature effect。"),
    Spacer(1, 4 * mm),
]

summary = [
    [p("Template", h2), p("架構", h2), p("招牌效果", h2)],
    [p("A · Simple"), p("頂部 sticky nav"), p("Button sweep-fill")],
    [p("B · Elegant"), p("左側 sticky sidebar"), p("Gallery filter reveal")],
    [p("C · Cyber"), p("底部 fixed dock"), p("Terminal typing + caret")],
    [p("D · Colorful"), p("全螢幕 snap + 右側 rail"), p("Recommended pulse ring")],
]
table = Table(summary, colWidths=[40 * mm, 57 * mm, 70 * mm], repeatRows=1)
table.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), PALE),
            ("GRID", (0, 0), (-1, -1), 0.5, LINE),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 7),
            ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]
    )
)
story += [table, Spacer(1, 7 * mm), p("規則", h1)]
story += bullets(
    [
        "不得修改 student 內的 HTML，唯一允許的差異是 stylesheet 路徑。",
        "每個 template 只允許一份本地 CSS；不得使用 JavaScript、外部 CSS 或 icon library。",
        "所有 tabs、slider、lightbox、dropdown、accordion 與 form state 都必須由 CSS 運作。",
        "student/images 必須原位使用，不可改名或搬移。",
        "規格列出的 CSS variables 名稱和值必須完全一致，且在樣式中實際引用。",
    ]
)
story += [PageBreak(), p("共用元件驗收", title)]
story += bullets(
    [
        "Tabs：只顯示 active panel；active label 狀態清楚；radio 仍可用鍵盤操作。",
        "Slider：三張 slide 以水平 translate 切換，並有 active control 與 transition。",
        "Gallery：1/2/3-4 欄響應式；剛好六張時才啟用 staggered mosaic。",
        "Lightbox：每張圖以 :target 開啟 full-screen overlay，close 回到 #gallery。",
        "Data hooks：card icon、statistics、timeline year 與 gallery caption 由 data-* 產生。",
        "Pricing：包含 .recommended 的整個 row 被強調。",
        "Dropdown：hover 與 focus-within 皆可開啟。",
        "Form：初次載入不顯示 error，使用者互動後 invalid 才出現。",
        "Email 與 .pdf links 的圖示由 CSS 加入；anchor navigation 使用 smooth scroll。",
    ]
)
story += [p("可及性與動態偏好", h1)]
story += bullets(
    [
        "所有互動元素需有清楚的 :focus-visible。",
        "用 visually-hidden 技巧隱藏 radio；不可使用 display:none。",
        "在 prefers-reduced-motion: reduce 下停用平滑捲動與非必要動畫。",
        "在 360、768、1280 px 測試水平溢位、fixed UI 遮擋與 touch target。",
    ]
)
story += [p("交付檔案", h1)]
story += bullets(
    [
        "css_only_simple.css",
        "css_only_elegant.css",
        "css_only_cyber.css",
        "css_only_colorful.css",
    ]
)
story += [PageBreak(), p("120 分鐘模擬流程", title)]

schedule = [
    [p("時間", h2), p("工作", h2), p("完成定義", h2)],
    [p("0-15"), p("Tokens / base"), p("變數、reset、typography、focus-visible")],
    [p("15-45"), p("核心互動"), p("tabs、slider、gallery、lightbox")],
    [p("45-65"), p("內容元件"), p("data hooks、pricing、FAQ、form")],
    [p("65-100"), p("Template 特徵"), p("layout architecture + signature effect")],
    [p("100-120"), p("回歸測試"), p("RWD、keyboard、reduced motion")],
]
schedule_table = Table(schedule, colWidths=[25 * mm, 48 * mm, 94 * mm], repeatRows=1)
schedule_table.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), PALE),
            ("GRID", (0, 0), (-1, -1), 0.5, LINE),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 7),
            ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ]
    )
)
story += [schedule_table, Spacer(1, 7 * mm), p("最後檢查", h1)]
story += bullets(
    [
        "先用鍵盤走完整頁，再用滑鼠檢查 hover 狀態。",
        "暫時移除一個 gallery item，確認 mosaic 跨欄取消。",
        "暫時移除一個 nav link，確認 compact sizing 取消。",
        "切換系統 color scheme，確認只有 Cyber 改變配色。",
        "啟用 reduce motion，確認 typing、pulse、slider transition 與 smooth scroll 停用。",
    ]
)
story += [Spacer(1, 8 * mm), p("完整規格請閱讀 student/spec；評分細項請閱讀 assessment/self-check-zh-TW.md。", center)]

doc = SimpleDocTemplate(
    str(OUTPUT),
    pagesize=A4,
    rightMargin=18 * mm,
    leftMargin=18 * mm,
    topMargin=18 * mm,
    bottomMargin=22 * mm,
    title="CSS-only Template 練習任務",
    author="OpenAI Codex",
)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUTPUT)
