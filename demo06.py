# -*- coding: utf-8 -*-
'''
串列 list
'''
x = [1,7,3,7,5,7, 'string', 7]
print(x)
print('第1值:', x[1]) #從0開始算
print('第1到3值:', x[1:4])

x[2] = True #第2值改為 True
print('更改第2值', x)
print('========')

y = [2,4,6]
print(x + y)
z = 8
y.append(z)
print(x + y)
print('========')

x.remove(7) #刪掉元素 7
print('remove_x:', x)
pop_x = x.pop()
print('pop_x:', pop_x, '/ x:', x)
print('========')

equal_x = x #指派
copy_x = x.copy() #複製
x.append(y)
x.append(z)
print('串列 x 內新增串列 y 及串列 z:', x)
print('指派等於x:', equal_x)
print('複製x:', copy_x)
print('========')



'''
Tuple
'''
t_y = 1, 3, 5, 7
print('type:', type(t_y))
a, b, c, d = t_y
print(a,b,c,d)

a, b, c, d = y
print('type:', type(y))
y[0] = 10
print(a,b,c,d) #a並不等於10

print('type:', type(tuple(y)))
print('========')



'''
字典dict / 集合
'''
d1 = {0:123, '1':True, 2.3:'abc', (1, 3, 5, 7):'abc'}
print("d1['1']:", d1['1']) #雙引號內的單引號
d1['1'] = False
d1[10] = 'New'
print('更新d1:', d1)

d2 = {11:'11', 22:'22', 33:'33'}
d1.update(d2)
print('d1 d2 合併:', d1)
print('========')

print('{}是空:',type({}))
print('========')

s1 = {1,2,3,4,1,2,3,9} #重複1,2,3
print('s1:', s1)
s2 = {1,2,3,4,5,6,7,8}
print('s2:', s2)
print('交集:', s1&s2)
print('聯集:', s1|s2)
print('差集:', s1-s2)
print('========')

d_x = {'1':1, '2':2, '3':3}
d_y = {'3':3, '1':1, '2':2}
print('字典與排列無關? :', d_x==d_y)
