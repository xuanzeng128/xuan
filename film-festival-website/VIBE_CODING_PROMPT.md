# Vibe Coding Prompt 紀錄｜《這一站，青春》

## 一、主要建置指令

> 請依據我提供的《這一站，青春》行銷影展期末企劃書，製作一個大二行銷影展專題介紹網站。主題聚焦臺中驛鐵道文化園區，以故事型短影音呈現兩位女孩從高中時期走訪文化場域，到多年後因相同吊飾再次重逢的青春故事。核心訊息是「古蹟留下歷史，我們留下足跡」。請忠實使用企劃書資料，不要自行編造調查結果、場域資訊或團隊成員。
>
> 網站需包含首頁、影展介紹、故事與場景、行銷企劃、製作團隊等分頁。每頁有一致的頂部導覽列、側邊資訊欄及頁尾。首頁呈現影展名稱、標語與主視覺；影展介紹頁呈現專案緣起、創作理念、廣告精神與目標；故事頁呈現劇情及臺中驛場域；行銷頁呈現18–24歲目標客群、AIO、消費者洞察、SWOT與市場定位；團隊頁呈現企劃書中的實際成員與分工。
>
> 使用 HTML5 語意化標籤、CSS Grid System 與 RWD，確保手機、平板及桌機皆能完整閱讀，不可產生水平溢出。CSS 必須拆分為多個檔案並放在 css 資料夾，圖片放在 images 資料夾，JavaScript 放在 js 資料夾。加入各頁獨立的 SEO title、description、keywords、author、robots 與 Open Graph。圖片需有描述性 alt，導覽列需支援鍵盤操作及手機收合。
>
> 視覺風格採復古鐵道與青春電影感，使用深墨綠、暖米白、復古金及低飽和色調，版面留白、清楚易讀。若沒有實際劇照，先使用清楚標示為示意的原創插畫，不可冒用網路圖片。未確認資訊請標示待補。

## 二、後續優化指令

- 請檢查手機寬度 390px 與平板寬度 768px 的排版，側邊欄在手機改為主內容下方。
- 請檢查所有分頁的導覽連結、圖片路徑、CSS 路徑與 SEO 描述。
- 請檢查文字對比、圖片 alt、按鈕 aria-label、aria-expanded 及鍵盤 focus 樣式。
- 請確認 CSS 沒有寫在 HTML 的 inline style，所有樣式皆由 css 資料夾載入。
- 請勿虛構企劃書沒有提供的數據；訪談僅以企劃書記載的四位受訪者作為初步洞察，不可宣稱代表整體青年。

## 三、檔案架構

```text
film-festival-website/
├── index.html
├── project.html
├── story.html
├── marketing.html
├── team.html
├── css/
│   ├── base.css
│   ├── layout.css
│   ├── components.css
│   └── rwd.css
├── images/
│   ├── hero.svg
│   ├── platform.svg
│   ├── oldstation.svg
│   ├── literature.svg
│   └── favicon.svg
├── js/nav.js
├── robots.txt
├── README.md
└── VIBE_CODING_PROMPT.md
```

## 四、部署需求

GitHub Repository：`xuanzeng128/xuan`。Vercel 匯入 Repository 時，Root Directory 設定為 `film-festival-website`，Framework Preset 選 Other。InfinityFree 則將本資料夾內的網站檔案上傳至網域的 `htdocs`，並確認首頁檔名為 `index.html`。

## 五、設計原則

內容以企劃書為依據；視覺以故事情感為主，不將網站做成單純報告文件；重要資訊清楚分頁，手機閱讀優先，圖片版權與實際拍攝資訊需於正式繳交前確認。
