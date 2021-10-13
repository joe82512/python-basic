# -*- coding: utf-8 -*-
import os
import requests
from io import StringIO
import pandas as pd
import time

# 儲存檔案路徑
def file_path(folder,fname,fmat):
    # 新增資料夾
    if folder not in os.listdir():
        os.mkdir(folder)
    # 建立檔名(含路徑及格式)
    file = os.path.join(folder, fname+'.'+fmat)
    return file

# 儲存原始資料
def save_rowdata(file,content):
    f = open(file, 'w')
    f.write(content)
    f.close()

# 取得網址
def get_url(i,**kargs):
    if i==1: #每日收盤價
        '''
        >>> 格式
        date = 西元年份(4碼)月(2碼)日(2碼)
        type = ALL(全部) / ALLBUT0999(不含權證、牛熊證、可展延牛熊證)
        '''
        date = kargs['date']
        url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date='+str(date)+'&type=ALLBUT0999'
    elif i==2: #月報
        '''
        >>> 格式
        98年以前 = ~_民國年份_月(1~2碼).html
        99年以後 = ~_民國年份_月(1~2碼)_0.html
        '''
        year = kargs['year']
        month = kargs['month']
        if year-1911 < 99:
            url = 'https://mops.twse.com.tw/nas/t21/sii/t21sc03_'+str(year-1911)+'_'+str(month)+'.html'
        else:
            url = 'https://mops.twse.com.tw/nas/t21/sii/t21sc03_'+str(year-1911)+'_'+str(month)+'_0.html'
    else:
        url = ''
        
    return url

#################################################################



### 每日收盤價
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
url_1 = get_url(1,date=20201015)
res = requests.get(url_1, headers)
# 儲存原始檔
price = res.text.replace('\n','') #去除轉義符號\n
save_rowdata(file_path('demo12','price','csv'),price)
# 整理數據
content = res.text.replace('=', '') #部分ID前面有等號
row = content.split('\n') #以轉義符號為目標分割
rows = [] #去除指數之股價串列
for r in row:
    if len(r.split('",')) > 10: #去除雜項: 指數
        rows.append(r)
content = "\n".join(rows) #加入轉義符號為目標分割
df = pd.read_csv(StringIO(content)) #導入Pandas
df = df.astype(str) #全部字串化
df = df.apply(lambda s: s.str.replace(',','')) #把數字的逗號去掉
df = df.set_index(['證券代號', '證券名稱']) #更改row名稱
df = df.drop(columns=['Unnamed: 16']) #刪除多餘

time.sleep(5)

### 月報
url_2 = get_url(2,year=2019,month=3)
res = requests.get(url_2, headers)
# 儲存原始檔
report = res.content.decode('big5', 'ignore') #html內混用
save_rowdata(file_path('demo12','monthly','html'),report)
# 整理數據
res.encoding = res.apparent_encoding #轉碼
df2 = pd.read_html(StringIO(res.text))
df2 = [d for d in df2 if d.shape[1] > 3] #去除雜項: 標題
df2 = pd.concat(df2) #表格合併
df2.columns = df2.columns.get_level_values(1) #更改columns名稱
df2 = df2[df2['公司代號'] != '合計'] #去掉合計
df2 = df2.set_index(['公司代號', '公司名稱']) #更改row名稱
df2 = df2.drop(columns=['備註']) #刪除備註

#整理完的數據儲存成Excel
excel = pd.ExcelWriter(file_path('demo12','Data Cleansing','xlsx'))
df.to_excel(excel, sheet_name='price')
df2.to_excel(excel, sheet_name='monthly')
excel.save()