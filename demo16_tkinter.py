# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
from datetime import date as dt
from demo15_stockclass import Price, Monthly
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class StockLayout():
    def __init__(self):
        # GUI Layout
        self.window = tk.Tk()
        self.window.title('Crawler Stock Program')
        self.window.geometry('1000x550')

        # Menubar Layout
        self.menubar = tk.Menu(self.window)
        self.window.config(menu=self.menubar)
        self.crawlermenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Target', menu=self.crawlermenu)
        self.data_info = 0 #Target預設為Price
        self.crawlermenu.add_command(label='Price', command=lambda: self.data_mode(0))
        self.crawlermenu.add_command(label='Monthly', command=lambda: self.data_mode(1))
        self.exitmenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Exit', menu=self.exitmenu)
        self.exitmenu.add_command(label='Quit', command=self.window.quit)

        # Initial Date
        self.yy1,self.mm1,self.dd1 = self.date_layout(0) #0~3
        # Final Date
        self.yy2,self.mm2,self.dd2 = self.date_layout(4) #4~7

        # One or Range Mode
        self.cap_mode = tk.Label(self.window, text='Capture :')
        self.cap_mode.grid(row=8, column=0, sticky=tk.E)
        self.cap_mode.config(font=('Courier', 14))
        self.mode = tk.IntVar()
        self.mode.set(2) #無預設模式
        self.mode1 = tk.Radiobutton(self.window, text='only on \ninitial date')
        self.mode1['variable'] = self.mode #設置mode
        self.mode1['value'] = 0 #mode=0
        self.mode1['command'] = self.modebutton #顯示狀態功能
        self.mode1.grid(row=8, column=1, sticky=tk.E)
        self.mode2 = tk.Radiobutton(self.window, text= 'from initial date \nto final date')
        self.mode2['variable'] = self.mode #設置mode
        self.mode2['value'] = 1#mode=1
        self.mode2['command'] = self.modebutton #顯示狀態功能
        self.mode2.grid(row=8, column=2)

        # ID
        self.cap_id = tk.Label(self.window, text='ID :')
        self.cap_id.grid(row=9, column=0, sticky=tk.E)
        self.cap_id.config(font=('Courier', 14))
        self.id = tk.StringVar()
        self.id.set('2330')
        self.entry_id = tk.Entry(self.window, justify=tk.LEFT)
        self.entry_id.config(font=('Courier', 14))
        self.entry_id['textvariable'] = self.id
        self.entry_id['width'] = 8
        self.entry_id.grid(row=9, column=1, sticky=tk.W)

        # Crawler
        self.crawler_b = tk.Button(self.window, text='Crawler', activeforeground='red')
        self.crawler_b.grid(row=10, column=0, columnspan=3)
        self.crawler_b['width'] = 14
        self.crawler_b['height'] = 1
        self.crawler_b.config(font=('Courier', 14), foreground='blue')
        self.crawler_b['command'] = self.crawlerbutton

        # Show Status
        self.text = tk.Text(self.window)
        self.text.grid(row=11, column=0, columnspan=3)
        self.text['width'] = 40
        self.text['height'] = 14
        self.text.tag_config('title1', font=('Courier', 12) )
        self.text.tag_config('tag1', backgroun='yellow', foreground='red')
        self.text.insert(tk.END,'    <<< User Guide >>>', 'title1')
        self.text.insert(tk.END,'\n若要取得')
        self.text.insert(tk.END,'當日資訊', 'tag1')
        self.text.insert(tk.END,'，\n 請在 Initial Date 處選擇日期；')
        self.text.insert(tk.END,'\n若要取得')
        self.text.insert(tk.END,'時間範圍內的所有資訊', 'tag1')
        self.text.insert(tk.END,'，\n 請在 Initial Date 選擇開始日期')
        self.text.insert(tk.END,'\n 以及 Final Date 處選擇結束日期。')
        self.text.insert(tk.END,'\n================================')
        self.text.insert(tk.END,'\n')
        self.text.insert(tk.END,'\nStatus :')

        # Plot Price
        self.fig = plt.figure(figsize=(3.2,2.2), dpi=100) #window size
        self.canvas = FigureCanvasTkAgg(self.fig, self.window)
        self.canvas.get_tk_widget().grid(row=2, column=3, rowspan=12, columnspan=2)

        self.frame = tk.Frame(self.window) #toolbar無法直接使用grid
        self.frame.grid(row=1, column=3)
        self.toobar = NavigationToolbar2Tk(self.canvas, self.frame)
        
        self.export_b = tk.Button(self.window, text='Export', activeforeground='red', command=self.csv_export)
        self.export_b.grid(row=1, column=4)
        self.export_b['width'] = 14
        self.export_b['height'] = 1
        self.export_b.config(font=('Courier', 14), foreground='green')

        # loop
        self.window.mainloop()

    def date_layout(self,n): #介面排版
        if n < 3:
            p = tk.Label(self.window, text='Initial Date (the day)')
        else:
            p = tk.Label(self.window, text='Final Date')
        p.grid(row=n, column=0, columnspan=3)
        p.config(font=('Courier', 18))
        # Entr yyyy
        year_list = tk.Label(self.window, text='Year :')
        year_list.grid(row=n+1, column=0, sticky= tk.E)
        yy = tk.StringVar() #取得文字用
        yy.set('2021') #預設2021年
        entry_yy = tk.Entry(self.window, justify=tk.LEFT) #輸入框
        entry_yy['textvariable'] = yy
        entry_yy['width'] = 12
        entry_yy.grid(row=n+1, column=1)
        # Combobox mm
        month_list = tk.Label(self.window, text='Month :')
        month_list.grid(row=n+2, column=0, sticky=tk.E)
        mm = ttk.Combobox(self.window, values=[m+1 for m in range(12)]) #12個月
        mm.current(0)
        mm['width'] = 10
        mm.grid(row=n+2, column=1)
        # Combobox dd
        day_list = tk.Label(self.window, text='Day :')
        day_list.grid(row=n+3, column=0, sticky= tk.E)
        dd = ttk.Combobox(self.window, values=[d+1 for d in range(31)]) #31號
        dd.current(0)
        dd['width'] = 10
        dd.grid(row=n+3, column=1)
        return yy,mm,dd

######################################################################
    def data_mode(self,i):
        if i == 0:
            self.data_info = 0 #Price
        else:
            self.data_info = 1 #Monthly

    def modebutton(self): #顯示狀態用
        self.d1 = int(self.yy1.get())*10000+int(self.mm1.get())*100+int(self.dd1.get())
        self.d2 = int(self.yy2.get())*10000+int(self.mm2.get())*100+int(self.dd2.get())
        status0 = '  Get '+self.crawlermenu.entrycget(self.data_info,'label') #取得Target
        if self.mode.get() == 0: #當日當月
            status = status0 +' in '+str(self.d1)
        else: #一段時間
            status = status0 +' from '+ str(self.d1)+' to '+str(self.d2)
        self.text.delete(10.0, tk.END)
        self.text.insert(tk.END,'\n'+status)

    def crawlerbutton(self):
        self.crawler_b['state'] = tk.DISABLED #鎖住按鈕,防呆用
        self.modebutton() #取得現在模式
        self.crawlermenu.entrycget(self.data_info,'label') #取得現在目標
        if self.mode.get()==0: #當日當月資訊
            self.date_crawler(self.d1)
        elif self.mode.get()==1: #一段時間資訊
            self.i_list = []
            self.date_list = []
            self.price_list = []
            for i in range(self.d1,self.d2):
                self.date_crawler(i) #爬蟲並儲存檔案
                file_path = os.path.join(self.folder, 'price_'+str(i)+'.xlsx')
                try:                    
                    db = pd.read_excel(file_path) #讀取已儲存的收盤價
                except:
                    pass
                else:
                    db = db.set_index(['證券代號'])
                    db_p = db.loc[self.id.get(),'收盤價']
                    self.name_id = db.loc[self.id.get(),'證券名稱']
                    self.i_list.append(i)
                    self.date_list.append(str(int((i%10000)//100))+'-'+str(int(i%100)))
                    self.price_list.append(float(db_p))
            self.plot_axes(self.date_list,self.price_list) #繪圖
                
        else: #沒選擇模式
            self.text.delete(10.0, tk.END)
            self.text.insert(tk.END,'\n  Must choose capture mode !')        
        self.crawler_b['state'] = tk.NORMAL #按鈕解鎖

    def date_crawler(self,d): #爬蟲
        try: #確定日期是否存在
            dt(int(d//10000),int((d%10000)//100),int(d%100))
        except:
            print('date not exist')
        else:
            self.folder = 'demo16'
            if self.data_info == 0: #股價
                a = Price(self.folder)
                a.crawler(date=d,fmat='xlsx')
                status0 = str(int(d//10000))+'-'+str(int((d%10000)//100))+'-'+str(int(d%100))
            else: #月報
                b = Monthly(self.folder)
                b.crawler(date=d,fmat='xlsx')
                status0 = str(int(d//10000))+'-'+str(int((d%10000)//100))   
            self.text.delete(11.0, tk.END)
            self.text.insert(tk.END,'\n   ===> '+status0)

    def plot_axes(self,x,y): #繪圖
        plt.clf() # clear current
        plt.plot(x,y)
        plt.tick_params(labelsize=5)
        plt.gcf().canvas.draw()

    def csv_export(self): #輸出收盤價
        today = time.strftime("%Y%m%d", time.localtime())
        file_path = os.path.join(self.folder, self.name_id+'_'+today+'.csv')
        file_data = np.array([self.i_list,self.price_list]).T
        np.savetxt(file_path, file_data, fmt='%.2f', delimiter=',')
        messagebox.showinfo('program', '匯出完成 !') #對話框

######################################################################        
if __name__ == '__main__':
    StockLayout()