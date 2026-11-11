# Vibe Coding 指令紀錄｜行銷影展專題網站

## 主要 Prompt

> 請使用 HTML5、CSS Grid、RWD 與少量原生 JavaScript，製作繁體中文多頁式大二行銷影展專題網站。作品名稱為《那年青春，我們走進的古蹟》，故事以兩位女孩的高中暑假回憶為主軸，走訪臺中文學館與臺中驛鐵道文化園區。網站需有首頁、作品介紹、故事與場景、製作團隊等分頁；每頁共用導覽列、側邊欄與頁尾。請加入每頁不同的 SEO title、description、keywords、author、robots、Open Graph meta。CSS 拆分至 css 資料夾，圖片放 images，JavaScript 放 js。視覺採溫暖復古的深綠、米白與金色。請使用語意化 HTML、圖片 alt、鍵盤焦點樣式與可收合的手機導覽列。未確認的組員姓名、正式劇照、影片網址與拍攝資訊請標示待填或示意素材，不可捏造。

## 後續迭代 Prompt
- 請檢查 390px 手機畫面，避免水平捲動，側欄改排在主內容下方。
- 請逐頁檢查 SEO 標題、摘要與 Open Graph 是否符合該頁。
- 請檢查圖片 alt、導覽列 aria-label、按鈕 aria-expanded 與鍵盤 focus。
- 請保留 HTML、css、images、js 分資料夾，不要將 CSS 寫回行內 style。

## 檔案結構
```text
film-festival-website/
├── index.html / project.html / story.html / team.html
├── css/ (base.css, layout.css, components.css, rwd.css)
├── images/ (cover.svg, literature.svg, railway.svg, favicon.svg)
├── js/nav.js
└── VIBE_CODING_PROMPT.md
```

## 部署設定
- GitHub：將整個資料夾推送至 Repository。
- Vercel：匯入 Repository，Framework Preset 選 Other，Output Directory 設定為 `film-festival-website`。
- InfinityFree：把資料夾內的首頁、其他 HTML、css、images、js 一起上傳到 `htdocs`。

> 本專案 SVG 為示意插畫，正式發表請替換成團隊實際拍攝且取得授權的照片。
