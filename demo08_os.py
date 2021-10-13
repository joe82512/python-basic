# -*- coding: utf-8 -*-
import os
origin_path = os.getcwd() #目前路徑
new_path = origin_path + r'\data' #內有轉義符號

if os.path.isdir(new_path): #判斷資料夾是否存在
    print('資料夾已存在')    
else:
    print('建立新資料夾')
    os.mkdir(new_path) #建立資料夾

os.chdir(new_path) #改變路徑
file_list = os.listdir() #路徑內檔案列表
file_format = '.pdf' #副檔名
pdf_list = [] #更新pdf檔名稱列表

for f in file_list:
    if not f.find(file_format)==-1: #篩選副檔名.pdf
        new_filename = f[2:] #扣除前兩個字元
        #new_filename = '1_' + f #加回兩個字元
        os.rename(f, new_filename) #更改檔名
        f = f[:len(f)-len(file_format)] #扣除副檔名
        pdf_list.append(f) #更新pdf檔名稱列表

print(pdf_list) #輸出pdf檔案