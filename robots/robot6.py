import os as o
import rpa as r  
import pyautogui as p 
from time import sleep
import xlrd 
import openpyxl
import pandas as pd
# pip install numpy==1.19.3      for work pandas

'''
Aparentemente o RPA é mais lento em webscrapping do que o selenium.
'''
r.init()
r.url('https://rpachallengeocr.azurewebsites.net/')
window = p.getActiveWindow()
window.maximize()
sleep(6)

# Apagando arquivo anterior.
try:
    o.remove('WebTable.csv')
except:
    pass

countPage = 1
while countPage <= 3:
    if countPage == 1:
        # Put datas in a temporary arquive.
        r.table('//*[@id="tableSandbox"]', 'temp.csv')
        sleep(1)
        # Save datas in a variable.
        datas = pd.read_csv('temp.csv')
        # Write datas in a permanent arquive.
        datas.to_csv(r'WebTable.csv', mode='a', index=None, header=True)
        sleep(1)
        r.click('//*[@id="tableSandbox_next"]')
        countPage += 1
    else:
        # Put datas in a temporary arquive.
        r.table('//*[@id="tableSandbox"]', 'temp.csv')
        sleep(1)
        # Save datas in a variable.
        datas = pd.read_csv('temp.csv')
        # Write datas in a permanent arquive.
        datas.to_csv(r'WebTable.csv', mode='a', index=None, header=False)
        sleep(1)
        r.click('//*[@id="tableSandbox_next"]')
        countPage += 1
r.close()
o.remove('temp.csv')
csv_xls = pd.read_csv(r'WebTable.csv')
csv_xls.to_excel(r'WebTable02.xlsx')