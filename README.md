# 本人為嘉義大學學生，僅作為方便填寫工作日誌維護使用
安裝好環境後，直接下載run.py就可以使用。
## 環境需求
* tkinter
* selenium
* pytesseract
* PIL
* io
* cv2

# 執行展示
![執行展示](https://github.com/sandwich9487/AutoNewSite/blob/28ffb102f6d291018b2972f373263eddd85d3e5e/display.png "display")
## 圖片說明
* 開始驗證的按鈕會自行便是驗證碼，諾沒有便是成功則在按一次
* 開始的日期為，投保的第一天
* 總共幾天為，總時數/8 ，且須要連續(會自動跳過第六天，且一天會填八小時)
* 第一、二開始的時段為，一天無課程衝突的兩個時段開始時段(都會自動四個小時)
* 輸入w為，自動填寫的工作內容
