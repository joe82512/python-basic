# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# 讀取檔案
filename = 'test_numpy.txt'
result = np.loadtxt(filename)

# 建立Series
idx = ['no.'+str(x+1) for x in range(10)]
s = pd.Series(result[:,1], index=idx)
print(s.index, s.values)

# 建立DataFrame
df = pd.DataFrame(result, index=idx, columns=['x', '2^x/5'])
'''
r = {'x': result[:,0], '2^x/5': result[:,1]}
df = pd.DataFrame(r, index=idx)
'''
df.index.name = 'Number' #index 命名為 Number

# 擷取
x = df.loc['no.3':'no.9','x']
print(x)
y = df.iloc[2,:]
print(y)

# csv儲存與讀取
df.to_csv('test_pandas.csv')
csv_df = pd.read_csv('test_pandas.csv')

# Excel儲存與讀取
excel = pd.ExcelWriter('test_pandas.xlsx')
df.to_excel(excel, sheet_name='sheet')
df.to_excel(excel, sheet_name='pandas')
excel.save()

excel_df = pd.read_excel('test_pandas.xlsx', sheet_name = None) #sheet_name預設只讀第一個工作表
sheet_list = [sheet for sheet in excel_df.keys()] #工作表名稱
print(sheet_list)
sheet_data = excel_df.get(sheet_list[1]) #第二個工作表數據
print(sheet_data)