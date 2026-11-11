# Vibe Coding 指令紀錄｜《這一站，青春》

## 專題依據
本網站依據《甲四_這一站，青春_期末企劃書》製作。企劃以臺中驛鐵道文化園區為核心，主要目標客群為18至24歲青年與大學生。企劃指出，部分青年對鐵道歷史古蹟有距離感，常將園區視為轉乘動線，尚未深入體會其文化與情感價值。專案透過現況分析、SWOT、STP及故事型短影音，將歷史古蹟轉化為紀錄青春足跡與同行回憶的情感載體。

## 主要 Vibe Coding Prompt
>
> 網站名稱為「這一站，青春」，核心場域為臺中驛鐵道文化園區。網站需包含首頁、影展介紹、故事與場景、行銷企劃、製作團隊五個分頁。首頁呈現主視覺、核心標語與專題摘要；影展介紹頁呈現專案執行摘要、個案概述、企劃緣起、廣告精神與目標；故事與場景頁介紹成年女主角在火車上翻閱相簿、高中時期女1帶女2走訪臺中文學館及臺中驛、兩人購買吊飾作為紀念，以及多年後因相同吊飾重逢的故事；行銷企劃頁呈現產業現況、未來趨勢、消費市場與需求、競爭者分析、SWOT、市場區隔、目標客群、AIO、功能與情感需求、競爭者比較、差異化優勢及市場定位；團隊頁呈現企劃書實際組員姓名與分工。
>
> 使用 HTML5 語意化標籤、CSS Grid System 與 RWD，確保桌機、平板及手機都能完整閱讀。每頁使用一致的頂部導覽列、側邊欄與頁尾。CSS 拆分為多個檔案並放入 css 資料夾，圖片放入 images 資料夾，JavaScript 放入 js 資料夾。每頁加入獨立 SEO title、description、keywords、author、robots 及 Open Graph。圖片需有描述性 alt，手機導覽列需可收合，並提供鍵盤焦點樣式。
>
> 視覺採復古車站與青春電影感，使用深墨綠、暖米白、復古金色，版面保留留白並確保閱讀性。沒有實際劇照時使用原創示意插畫並清楚標示為示意，不可假裝是真實拍攝照片。手機版不得出現水平捲動。

## 迭代與檢查 Prompt
1. 請檢查 390px 手機、768px 平板與桌機版面，確認導覽列、側欄及內容不會互相擠壓。
2. 請檢查每頁 SEO 標題、摘要、關鍵字及 Open Graph 是否符合該頁內容。
3. 請確認 CSS 全部放在 css 資料夾，不使用 inline style；圖片全部放在 images 資料夾。
4. 請檢查圖片 alt、連結、按鈕 aria-label、aria-expanded 及鍵盤 focus。
5. 請核對企劃書，不可將企劃內容推測成已證實的調查結論。

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

## 部署設定
- GitHub Repository：`xuanzeng128/xuan`
- Vercel：匯入 Repository，Root Directory 設為 `film-festival-2026`，Framework Preset 選 Other。
- InfinityFree：將本資料夾中的網站檔案上傳到網域的 `htdocs`，確保首頁檔名為 `index.html`。
