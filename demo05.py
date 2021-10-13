# -*- coding: utf-8 -*-
'''
變數指派
'''
x = 87 #87指派給x
print('x=',x)
print('========')

x = 'change' #更改x的內容
print('x=',x)
print('========')

y = x #把x的內容指派給y
print('x=',x)
print('y=',y)
print('========')

x = 87 #更改x的內容
print('x=',x)
print('y=',y)
print('========')



'''
資料型態: 數字
'''
print('type of x:',type(x)) #顯示資料型態
print('type of y:',type(y))
print('========')

print('type of 7:',type(7)) #整數
print('type of 7:',type(7.0)) #浮點數
print('========')

a = (1+2)*3 #基本運算
print('a: (1+2)*3 =',a)
b = a/5 #與py2有區別
print('b: 9/5 =',b)
a **= 2 #等同於 a = a**2
print('a = a**2 >>>',a)
print('========')



'''
資料型態: 字串
'''
A = '字串內"在放一組引號"的功能示範'
print(A)
B = '''這是多行字串的
功能範例'''
print(B)
print('========')

C = '萬聖'
C += '節' #字串合併
C *= 5 #字串複製
print(C)
print('========')

D = 'abcdefghijk'
print(D[2]) #第2個字元, 從0起算
print(D[:]) #擷取全部
print(D[2:-2]) #擷取第2個字元到倒數第2再前1個字元, 即倒數第3
print(D[::-3]) #從後往前間隔3取字元
print('========')

E = '''I am the bone of my sword.
Steel is my body and fire is my blood.
I have created over a thousand blades.
Unknown to death,
Nor known to life.
Have withstood pain to create many weapons.
Yet these hands will never hold anything.
So as I pray, ”Unlimited Blade Works”'''
print(E.upper())
print(E.swapcase())
print('========')

F = '轉義換行\n不轉義並輸出 \\n, ' #\代表轉譯, \\則可跳離轉譯變成字元\
G = r'若要兩個以上的反斜線可以添加 r 如 \\\n'
print(F+G)
print('========')



'''
資料型態: 布林
'''
print('True與 1 等價?', True==1)
print('False與 0 等價?', False==0)
print('True與 10 等價?', True==10)
print(type(1.0),type(1),type(True), 1.0==1, 1.0==True)
print('========')



'''
資料型態轉換
'''
print('1'==True)
print(bool('1')==True)
print(float('1')==True)
print(int('1')==True)