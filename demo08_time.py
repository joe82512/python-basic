# -*- coding: utf-8 -*-
import time
# 顯示現在時間
now = time.time()
local_now = time.localtime(now) #本機時間
UTC_now = time.gmtime(now) #UTC時間
print(time.asctime(now))
print('local:', time.asctime(local_now)) #asctime()用於轉換資料結構
print('UTC:', time.asctime(UTC_now))

# 格式化時間的資料結構
'''
### 轉換表 ###
%Y >>> 年 
%m >>> 月(數字)
%B >>> 月(英文)
%b >>> 月(英文縮寫)
%d >>> 月-日
%A >>> 星期(英文)
%a >>> 星期(英文縮寫)
%H >>> 時(24)
%I >>> 時(12)
%p >>> AM/PM
%M >>> 分
%S >>> 秒
'''
print(time.strftime("%Y-%m-%d (%p)%I:%M:%S", local_now)) #strftime()用於格式化資料結構

# 計時功能
t0 = time.time()
for i in range(5):
    print(i)
    time.sleep(1)
t1 = time.time()
print('計時結果:', t1-t0)