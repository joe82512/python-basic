# -*- coding: utf-8 -*-
'''
if / elif / else
'''
x = 1
if x == 1:
    print('Y')
else:
    print('N')


y = 3
if y == 1: #第一層判斷式
    print('1')
elif y == 2:
    print('2')
elif str(y) == '3':
    print('String')
    if x == 1: #第二層判斷式
        print('Y')
    else:
        print('N')
elif y == 3: #雖然為 True, 但先前條件已成立
    print('3')
else:
    print('Failed')


if y == 1:
    print('1')
elif (str(y) == '3') and (x == 1): #條件組合
    print('Y')
else:
    print('Failed')


z = []
if z: #視為 False
    print('Filling')
else:
    print('Empty')



'''
try / except
'''
tuple_a = (1,2,3,4,5)
try:
    tuple_a[1] = 10
    print(tuple_a)
except NameError:
    print("NameError")
except ValueError:
    print("ValueError")
except TypeError as te:
    print("TypeError", te)

'''
while / for
'''
i = 0
while i < 10:
    i = i + 1
    if i == 8: # 8以後停止
        break
    elif i == 5: # 5不輸出,下一循環
        continue
    print(i)

j_dict = {'1st':0, '2nd':1, '3rd':2, '4th':3}
for j in j_dict: #輸出鍵
    print(j)

for j in j_dict.values(): #輸出值
    print(j)

for j,k in j_dict.items(): #輸出(值, 鍵)
    print(j,k)



'''
生成式
'''
list_x = [2**x for x in range(10) if x%3 == 1] # x = 1,4,7
print(list_x)
dict_y = {str(y):int(y/2) for y in list_x}
print(dict_y)