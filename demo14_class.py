# -*- coding: utf-8 -*-
class Person():
    def __init__(self, name):
        #pass
        self.n = name #self.n 共用

    def p_print(self):
        self.status = 'Kono ' + self.n + ' da!!!!!!!!!!!!'
        return self.status

    def p_gender(self, name):
        if name == 1: #name與先前不共用
            return 'boy'
        elif name == 0:
            return 'girl'
        else:
            return "We don't know."

    def p_name(self):
        print('=======================================')
        print(self.n)
        print(__name__)
        print('=======================================')

if __name__ == '__main__':
    a = Person('DIO') #實體化
    print(a.p_print())
    print(a.p_gender(1))
    a.p_name()