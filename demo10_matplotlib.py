# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

# setting
account_start = 0 #起始資金
salary = 4.5 #月薪
bonus = 1.5 #年終
cost_living = 2 #生活費
cost_rent = 1 #房租
retired = 65 #退休年齡
life_year = range(26, 100) #預測區間
stock = 0.5 #拿多少比率的錢來投資
rate = 5/100 #年報酬率

# 每年淨收入
account_year = pd.Series(0, index=life_year) #建立空列表
account_year.iloc[0] = account_start #起始資金
account_year.loc[0:retired] += salary*(12+bonus) #退休前年收入
account_year -= (cost_living + cost_rent)*12 #扣除終身生活費及房租
'''
# 繪圖
plt.figure(0, figsize=(8,4))
plt.plot(account_year)
plt.title('Net Revenue')
plt.xlabel('age (years)')
plt.ylabel('revenue (millions)')
plt.show()
'''
# 累計資產
account_total = account_year.cumsum()
'''
# 繪圖
plt.figure(1, figsize=(8,4))
plt.plot(account_total)
plt.title('Total Assets')
plt.xlabel('age (years)')
plt.ylabel('assets (millions)')
plt.show()
'''
# 考慮投資
r0_list = [account_year.iloc[0]] #年收入(第一年)
ret_list = [account_year.iloc[0]] #累計(第一年)
for account in account_year[1:]: #第二年投資開始
    cost_stock = ret_list[-1]*stock #股票支出
    get_annual = ret_list[-1]*stock*(1+rate) #股票獲利
    
    #今年收入 = 去年資產 + 基本收入
    r0_account = account - cost_stock + get_annual
    r0_list.append(r0_account)
    #今年資產 = 去年資產 + 基本收入 - 股票支出 + 股票獲利
    ret_account = ret_list[-1] + r0_account  
    ret_list.append(ret_account) 
    
stock_account_year = pd.Series(r0_list, life_year)
stock_account_total = pd.Series(ret_list, life_year)
'''
# 有無投資的區別
plt.figure(2, figsize=(8,4))
plt.plot(account_total, label='no invest')
plt.plot(stock_account_total, label='invest', color='r',linestyle='--')
plt.title('Invest Stock')
plt.xlabel('age (years)')
plt.ylabel('assets (millions)')
plt.legend()
plt.show()
'''
# 圖片整合
plt.figure('Invest or not', figsize=(8,8))
plt.subplot(211)
plt.plot(account_year, label='no invest')
plt.plot(stock_account_year, label='invest', color='r',linestyle='--')
plt.title('Net Revenue')
plt.ylabel('assets (millions)')
plt.legend()
plt.subplot(212)
plt.plot(account_total, label='no invest')
plt.plot(stock_account_total, label='invest', color='r',linestyle='--')
plt.title('Total Assets')
plt.xlabel('age (years)')
plt.ylabel('assets (millions)')
plt.legend()
plt.savefig('test_matplotlib.png')
plt.show()