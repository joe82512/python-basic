# -*- coding: utf-8 -*-
class Car():
    def __init__(self, brand):
        self.brand = brand

    def c_model(self, model):
        self.model = model
        print(self.brand, self.model)
        
##################################################
# 繼承
print('=== 繼承 ===')
class Suv(Car):
    #pass
    def __init__(self, brand, l=5, w=2, h=1.75): #覆寫
        self.brand = brand
        self.l = l
        self.w = w
        self.h = h

    def c_model(self, model, hp=400): #super()新增功能
        super().c_model(model)
        self.hp = hp
        print(str(self.hp) + ' hp!!!')

    def c_space(self): #添加
        return self.l * self.w * self.h

mycar = Suv('BMW')
mycar.c_model('X5')
print(mycar.c_space())

print('= 多層繼承 =')
class BMWsuv(Suv): #多層繼承
    pass

X5 = BMWsuv('BMW')
X5.c_model('X5')
print(X5.c_space())

##################################################
# 封裝
print('=== 封裝 ===')

print('= 屬性修改 =')
print('l =',mycar.l)
mycar.l = 4.6 #修改屬性
mycar.h = 1.4
mycar.c_model('320i')
print(mycar.c_space())

print('= 私有變數 =')
class Private_car(Car):
    def __init__(self, brand): #覆寫
        self.__brand = brand

    def c_model(self, model, hp=400): #覆寫
        self.__model = model        
        self.__hp = hp
        print(self.__brand, self.__model, ':', self.__hp, ' hp!!!')
       
    def get_hp(self): #添加
        return self.__hp
    
    def set_hp(self, hp): #添加
        self.__hp = hp

    def del_hp(self): #添加
        del self.__hp
        print('No information about hp.')

    hp = property(get_hp, set_hp, del_hp)

    @property
    def hp2(self): #添加
        return self.__hp

    @hp2.setter
    def hp2(self, hp): #添加
        self.__hp = hp

    @hp2.deleter
    def hp2(self): #添加
        del self.__hp
        print('No information about hp.')

mycar2 = Private_car('BMW')
try:
    print('hp =',mycar2.__hp) #嘗試輸出__hp
except:
    print('Error')

mycar2.c_model('320i') #預設400
print(mycar2.get_hp()) #400
mycar2.c_model('320i', 184) #修改屬性184
print(mycar2.get_hp()) #184
mycar2.__hp = 300 #修改屬性
print(mycar2.get_hp()) #184
mycar2.c_model('320i') #預設400
print(mycar2.get_hp()) #400

print('= property =')
mycar2.hp = 184
print(mycar2.hp)
del mycar2.hp

mycar2.hp2 = 184
print(mycar2.hp2)

##################################################
# 多型
print('=== 多型 ===')
class Benz(Car):
    def __init__(self): #覆寫
        self.brand = 'Benz'

class Tesla(Car):
    def __init__(self): #覆寫
        self.brand = 'Tesla'

Benz().c_model('GLE')
Tesla().c_model('Model X')