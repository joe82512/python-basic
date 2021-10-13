# -*- coding: utf-8 -*-
import numpy as np

# 建立數列
x = range(10)
y = [2**x/5 for x in range(10)]

# 矩陣化
x = np.array(x)
y = np.array(y)
print('x:', x.shape)
'''
x = np.arange(10)
x = np.empty((10,1))
x = np.zeros((10,1))
x = np.ones((10,1))
x = np.full((10,1), np.pi)
'''

# 矩陣重塑
x.resize(1,10)
#x = x.reshape(1,10)
print('x:', x.shape)
y.resize(1,10)

# 矩陣合併
xy = np.concatenate((x,y), axis=0)

# 儲存檔案
filename = 'test_numpy.txt' #檔案名稱
np.savetxt(filename, xy.T, delimiter='\t', fmt='%.2f')
'''
%s >>> 字串表示
%d >>> 整數表示
%f >>> 浮點數表示
%e >>> 浮點數表示(科學記號)
'''

# 讀取檔案
result = np.loadtxt(filename)
x = result[:,0]
y = result[:,1]*5

# 矩陣運算
plus_xy = x+y
print(plus_xy.max())
#print(np.max(plus_xy))
multiply_xy = x*y
print(multiply_xy.mean())