# -*- coding: utf-8 -*-
import psutil
# 所有執行程式
pids = psutil.pids() #所有執行程式
p_info = {}
for pid in pids:
    p = psutil.Process(pid)
    p_info.update({p.name():pid}) #{程式名稱:程式編號}

# 讀取固定程式資訊
pid_python = p_info['python.exe'] #python.exe編號
print(pid_python)
p_python = psutil.Process(pid_python) #python的線程
print(p_python.exe()) #bin路徑
print(p_python.cwd()) #工作路徑
print(p_python.status()) #狀態
print(p_python.num_threads()) #使用執行緒數

# 計算CPU
print('CPU已使用: ' + str(psutil.cpu_percent()) + '%') #已使用%數
print('Python占用CPU: ' + str(p_python.cpu_percent()/psutil.cpu_count()) + '%') #Python使用%數

# 計算RAM
EXPAND = 1024 * 1024
print('RAM總共: ' + str(psutil.virtual_memory().total/EXPAND) + ' MB') #總額
print('RAM已使用: ' + str(psutil.virtual_memory().used/EXPAND) + ' MB') #已使用
print('RAM已使用:' + str(psutil.virtual_memory().percent) + ' %') #已使用%數
print('Python占用RAM: ' + str(p_python.memory_percent()) + ' %') #Python使用%數