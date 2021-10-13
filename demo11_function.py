# -*- coding: utf-8 -*-
###############################
def test_print(): #無輸入及輸出
    print('print')

test_print()

print(test_print()) #沒回傳值則顯示 None
###############################
def test_return(): #無輸入但有輸出
    return 1

x = test_return()
print(x)
###############################
def test_pass(): #不執行任何事
    pass

test_pass()

print(test_pass()) #pass and None
print(None==False) #None與False不等價
###############################
def test_return2(i,j,k):
    return i,j,k

print(test_return2(1,3,5))
print(test_return2(k=1,j=3,i=5))
print(test_return2(1,j=3,k=5)) #位置引數必須擺前, 且引數不能重複
###############################
def test_return3(i,j=10,k=100): #預設參數必須擺後
    return i,j,k

print(test_return3(1,3))
###############################
def test_args(i,*args): #位置引數*tuple
    return i,args

print(test_args(1,3,5,7,9))
###############################
def test_kwargs(i,**kwargs): #關鍵字引數**dict
    return i,kwargs

print(test_kwargs(i=1,j=3,k=5,m=7,n=9))
###############################
def add(a,b):
    return a+b

def func_sum(func,i,j): #函數可做為引數
    print(func(i,j))

func_sum(add,10,20)
###############################
def func_sum2(i,j):
    def add2(a,b): #內部函數
        return a+b
    print(add2(i,j))

func_sum2(10,20)
###############################
add3 = lambda a,b: a+b #匿名函數
print(add3(10,20))
###############################
i = 10 #全域變數
def change():
    i = 100
    return i
print(change())
print(i)

def change2():
    global i #全域變數
    i = i**2
    return i
print(change2())
print(i)