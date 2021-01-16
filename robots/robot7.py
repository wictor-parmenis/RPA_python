import rpa as r  
import pyautogui as p  
import pandas as pd  
import xlrd 
import openpyxl
from time import sleep
import os  

try:
    os.remove('challenge.xlsx')
except:
    pass

r.init()
r.url('http://rpachallenge.com/')
sleep(10)

r.download('http://rpachallenge.com/assets/downloadFiles/challenge.xlsx', 'challenge.xlsx')
window = p.getActiveWindow()
window.maximize()

sleep(4)

df = pd.read_excel('challenge.xlsx', sheet_name='Sheet1')
datas = pd.DataFrame(df, columns=["First Name", "Last Name ", "Company", "Name",	"Role in Company",
                        "Address Email"	"Phone Number"])
r.click('/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button')
for collumn in df.itertuples():
    print(collumn)
    r.type('//*[@ng-reflect-name="labelFirstName"]', str(collumn[1]))
    r.type('//*[@ng-reflect-name="labelLastName"]', str(collumn[2]))
    r.type('//*[@ng-reflect-name="labelCompanyName"]', str(collumn[3]))
    r.type('//*[@ng-reflect-name="labelRole"]', str(collumn[4]))
    r.type('//*[@ng-reflect-name="labelAddress"]', str(collumn[5]))
    r.type('//*[@ng-reflect-name="labelEmail"]', str(collumn[6]))
    r.type('//*[@ng-reflect-name="labelPhone"]', str(collumn[7]))
    r.click('/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input')

sleep(3)
p.screenshot('score.png')
r.close()
exit()

'''
<input _ngcontent-c2="" ng-reflect-name="labelFirstName" id="Z84Lc" name="Z84Lc" class="ng-pristine ng-invalid ng-touched">
'''


