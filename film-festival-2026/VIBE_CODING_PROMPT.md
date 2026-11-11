# Vibe Coding 指令紀錄｜《這一站，青春》

## 專題背景
本網站依據行銷影展企劃《這一站，青春》製作。核心場域為臺中驛鐵道文化園區，企劃以綜藝節目訪談形式介紹臺中約會景點，透過來賓推薦與景點比較，呈現臺中驛的鐵道歷史、交通便利性、展覽、市集、藝文表演及休閒體驗。競爭景點包含宮原眼科與審計新村，主要目標客群為18至24歲大學生。企劃定位為「結合歷史文化與青春體驗的特色約會景點」，核心標語為「古蹟留下歷史，我們留下足跡」。

## 主要 Vibe Coding Prompt
> 請依據我提供的《這一站，青春》行銷影展企劃書，製作一個大二影展專題介紹網站。請以企劃書為唯一內容依據，不要自行虛構研究數據、訪談結果、成員姓名或場域資訊。
>
> 網站名稱為「這一站，青春」，核心場域為臺中驛鐵道文化園區。網站需有首頁、影展介紹、故事與場景、行銷企劃、製作團隊等分頁。首頁呈現主視覺、標語與專題摘要；影展介紹頁說明企劃緣起、創作理念、廣告精神與目標；故事與場景頁介紹綜藝訪談腳本、臺中驛及比較景點宮原眼科、審計新村；行銷企劃頁呈現產業現況、消費市場與需求、功能性及情感價值、競爭者分析、SWOT、STP、目標市場與市場定位、十字定位圖；團隊頁呈現企劃書所列組員與分工。
>
> 請使用 HTML5 語意化標籤、CSS Grid System 與 RWD，建立桌機、平板及手機都能完整閱讀的版面。每頁需有一致的導覽列、側邊欄與頁尾。CSS 拆分成多個檔案並放入 css 資料夾，圖片放入 images 資料夾，JavaScript 放入 js 資料夾。每頁加入獨立 SEO title、description、keywords、author、robots、Open Graph。圖片必須有 alt，導覽列須有手機收合功能與鍵盤焦點樣式。
>
> 視覺採復古車站與青春電影感，使用深墨綠、暖米白、復古金色，排版清楚並保留留白。沒有實際劇照時使用原創示意插畫並標示為示意，不可假裝是真實拍攝照片。手機版不得出現水平捲動。

## 迭代與檢查 Prompt
1. 請檢查 390px 手機、768px 平板與桌機版面，確保導覽列、側欄及內容不會互相擠壓。
2. 請檢查每頁 SEO 標題、摘要、關鍵字及 Open Graph 是否符合頁面內容。
3. 請確認 CSS 全部放在 css 資料夾，不使用 inline style；圖片全部放在 images 資料夾。
4. 請檢查圖片 alt、連結、按鈕 aria-label、aria-expanded、鍵盤 focus。
5. 請核對企劃書資料，不可將企劃內容推測成已證實的調查結論。

## 專案結構
```text
film-festival-2026/
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
└── VIBE_CODING_PROMPT.md
```

## 部署方式
- GitHub Repository：`xuanzeng128/xuan`
- Vercel：匯入 Repository，Root Directory 設為 `film-festival-2026`，Framework Preset 選 Other。
- InfinityFree：將本資料夾中的網站檔案上傳到網域的 `htdocs`，確保首頁檔名為 `index.html`。
