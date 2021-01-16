import pyautogui as p  
from time import sleep 

# Identified position of Google Chrome in Desktop
# sleep(2)
# print(p.position())

p.doubleClick(x=121, y=121)
sleep(4)
p.write('https://www.udemy.com/  ')
sleep(1)
window = p.getActiveWindow()
window.maximize()
sleep(3)
p.press('enter')
sleep(4)
window = p.getActiveWindow()
window.maximize()
sleep(5)
localSearch = p.locateOnScreen('Pesquisa.png', confidence=0.9)
# print(localSearch)
# valor das medidas pode mudar de acordo com a resolução do
#  monitor utilizado.

locateSearch = p.center(localSearch)
print(locateSearch)
p.click(locateSearch)
sleep(2)
p.write('RPA')
p.press('enter')
sleep(2)
for i in range(10):
    p.press('down')
sleep(1)
p.screenshot('Courses.png')
sleep(1)

localClose = p.locateOnScreen('Close.png', confidence=0.8)
locateClose = p.center(localClose)
print(locateClose)
p.click(locateClose)

'''
Opção de enviar a imagem para o email.  
'''