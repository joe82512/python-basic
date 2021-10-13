# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# 月報網址
url = 'https://mops.twse.com.tw/nas/t21/sii/t21sc03_109_1_0.html'
# 偽瀏覽器
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# 送出請求
res = requests.get(url, headers=headers)
# 編碼轉換
print('網頁返回編碼:',res.encoding)
print('Requests推測的網頁編碼:',res.apparent_encoding)
res.encoding = res.apparent_encoding
# 解析網頁
soup = BeautifulSoup(res.text, 'lxml') #parser
#print(soup.prettify()) #輸出解析結果
# 擷取表格內資訊
tr = soup.find_all('tr', align = 'right')
#print(tr[0])
# 擷取固定行
td = tr[0].find_all('td')
#print(td)
# 取得公司名稱及營收
print(td[1].string+'當月營收:'+ td[2].string)
# 當參數含有 class
title = soup.find('th', class_ = 'tt') #class為類別宣告
#print(title)