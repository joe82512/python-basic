# -*- coding: utf-8 -*-
import os
import requests
from io import StringIO
import pandas as pd
import json
import time
from datetime import date as dt

class Price():
    def __init__(self, folder): #初始建立資料夾及偽瀏覽器
        self.f = folder
        if self.f not in os.listdir():
            os.mkdir(self.f)
            print(self.f,'資料夾建立成功')
        else:
            print(self.f,'資料夾已存在')
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

    def file_path(self, fname, fmat): #取得完整資料名稱(含格式)
        return os.path.join(self.f, fname+'.'+fmat)
    
    def get_url(self, **kargs): #取得爬蟲網址
        date = kargs['date']
        url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date='+str(date)+'&type=ALLBUT0999'
        return url
    
    def save_rowdata(self, file, content): #儲存原始檔
        f = open(file, 'w')
        f.write(content)
        f.close()

    def cleansing(self, res): #資料整理
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
        #df = df.set_index(['證券代號', '證券名稱']) #更改row名稱
        df = df.drop(columns=['Unnamed: 16']) #刪除多餘
        return df

    def save_excel(self, df, fname): #儲存成Excel檔
        excel = pd.ExcelWriter(self.file_path(fname,'xlsx'))
        df = df.set_index(['證券代號', '證券名稱']) #更改row名稱
        df.to_excel(excel, sheet_name='price')
        excel.save()

    def save_json(self, excel_df, fname): #儲存成json檔
        df_keys = excel_df.columns.tolist() #取columns作字典的鍵 (m,1)
        df_values = excel_df.values.tolist() #取值作字典的值 (m,n)
        df_json = [] #總體資料陣列
        for df_v in df_values:
            d = {} #每一個股價的資訊包成字典
            for i in range(len(df_keys)):
                df_v[i] = None if df_v[i] != df_v[i] else df_v[i] #Nan 改成 None
                d.update({df_keys[i]:df_v[i]}) #股價的資訊更新
            df_json.append(d) #股票檔位更新
        with open(self.file_path(fname,'json'), 'w', encoding='utf-8') as f:#儲存json檔
            f.write(json.dumps(df_json))

    def crawler(self, date, fmat='csv'): #獲取每日收盤價
        fname = 'price_'+str(date)
        if os.path.isfile(self.file_path(fname,fmat)): #檔案重複
            print(fname+' file exist')
        else:
            time.sleep(5) #防止爬蟲被擋
            url = self.get_url(date=date)        
            res = requests.get(url, self.headers)
            price = res.text.replace('\n','') #去除轉義符號\n
            if len(price) > 10: #排除空資料
                if fmat=='csv':
                    self.save_rowdata(self.file_path(fname,'csv'),price)
                elif fmat=='xlsx':
                    self.df = self.cleansing(res=res)
                    self.save_excel(self.df, fname=fname)
                elif fmat=='json':
                    self.df = self.cleansing(res=res)
                    self.save_json(self.df, fname=fname)
                else:
                    print('儲存失敗')
            else:
                print('此資料為空')



class Monthly(Price):    
    def get_url(self, **kargs): #取得爬蟲網址
        year = kargs['year']
        month = kargs['month']
        if year-1911 < 99:
            url = 'https://mops.twse.com.tw/nas/t21/sii/t21sc03_'+str(year-1911)+'_'+str(month)+'.html'
        else:
            url = 'https://mops.twse.com.tw/nas/t21/sii/t21sc03_'+str(year-1911)+'_'+str(month)+'_0.html'
        return url

    def cleansing(self, res): #資料整理
        res.encoding = res.apparent_encoding #轉碼
        df = pd.read_html(StringIO(res.text))
        df = [d for d in df if d.shape[1] > 3] #去除雜項: 標題
        df = pd.concat(df) #表格合併
        df.columns = df.columns.get_level_values(1) #更改columns名稱
        df = df[df['公司代號'] != '合計'] #去掉合計
        #df = df.set_index(['公司代號', '公司名稱']) #更改row名稱
        df = df.drop(columns=['備註']) #刪除備註
        return df
            
    def save_excel(self, df, fname): #儲存成Excel檔
        excel = pd.ExcelWriter(self.file_path(fname,'xlsx'))
        df = df.set_index(['公司代號', '公司名稱']) #更改row名稱
        df.to_excel(excel, sheet_name='monthly')
        excel.save()

    def date2month(self, date): #計算年月份
        year = int(date//10000)
        month = int((date%10000)//100)
        return (year,month)
    
    def crawler(self, date, fmat='html'): #獲取月報
        year, month = self.date2month(date)
        fname = 'monthly_'+str(year)+'_'+str(month)
        if os.path.isfile(self.file_path(fname,fmat)): #檔案重複
            print(fname+' file exist')
        else:
            time.sleep(5) #防止爬蟲被擋
            url = self.get_url(year=year, month=month)
            res = requests.get(url, self.headers)
            report = res.content.decode('big5', 'ignore') #html內混用
            if len(report) > 2000: #排除空資料
                if fmat=='html':
                    self.save_rowdata(self.file_path(fname,'html'),report)
                elif fmat=='xlsx':
                    self.df = self.cleansing(res=res)
                    self.save_excel(self.df, fname=fname)
                elif fmat=='json':
                    self.df = self.cleansing(res=res)
                    self.save_json(self.df, fname=fname)
                else:
                    print('儲存失敗')
            else:
                print('此資料為空')

if __name__ == '__main__':
    d = 20210304
    try: #測試日期是否正確
        dt(int(d//10000),int((d%10000)//100),int(d%100))
    except:
        print('date not exist')
    else:
        a = Price('demo15')
        a.crawler(date=d,fmat='xlsx')
        b = Monthly('demo15')
        b.crawler(date=d,fmat='xlsx')