# -*- coding: utf-8 -*-
import os
import pandas as pd
import time
import json

# json檔案輸出
if 'demo13' not in os.listdir(): #建立資料夾
    os.mkdir('demo13')
data = [{'ID':'0050','price':106.15},{'ID':'2330','price':450,'name':'台積電'}] #製作資料
json_data = json.dumps(data) #轉成json
with open('.\demo13\stock_test.json', 'w', encoding='utf-8') as f: #儲存json檔案
     f.write(json_data)

# 更新資料
with open('.\demo13\stock_test.json', 'r', encoding='utf-8') as f: #讀取json檔案
    log = json.load(f)
update = {'ID':'2884','price':24.85,'name':'玉山金'} #新增股票
log.append(update)
update2 = {'price':100,'name':'元大50'} #更新股票資訊
log[0] = {**log[0],**update2} #未更新的保留
with open('.\demo13\stock_test2.json', 'w', encoding='utf-8') as f: #儲存json檔案
    f.write(json.dumps(log))

#################################################################

# 股價爬蟲轉為 json 檔案
excel_df = pd.read_excel('.\demo12\Data Cleansing.xlsx', sheet_name = 'price') #讀取 Excel 資料
df_keys = excel_df.columns.tolist() #取columns作字典的鍵 (m,1)
df_values = excel_df.values.tolist() #取值作字典的值 (m,n)
df_json = [] #總體資料陣列
for df_v in df_values:
    d = {} #每一個股價的資訊包成字典
    for i in range(len(df_keys)):
        df_v[i] = None if df_v[i] != df_v[i] else df_v[i] #Nan 改成 None
        d.update({df_keys[i]:df_v[i]}) #股價的資訊更新
    df_json.append(d) #股票檔位更新
    
with open('.\demo13\stock_price.json', 'w', encoding='utf-8') as f:#儲存json檔案
    f.write(json.dumps(df_json))

#################################################################

# nan 與 None 區別
A = float('nan')
print('nan 是否與自身等價:', A==A)
B = None
print('None 是否與自身等價:', B==B)