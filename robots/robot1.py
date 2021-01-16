import pyautogui as p  
from time import sleep

# Any basic commands. 
# p.moveTo(119, 328, 1)
# p.click(119, 328, 1)
# p.sleep(2)
# print(p.position())

def notes():
    p.hotkey('win', 'r')
    p.sleep(1)
    p.typewrite('notepad')
    p.sleep(2)
    p.press('enter')
    p.sleep(2)
    p.typewrite('Hoje é sábado, como poso ajudá-lo?')
    p.sleep(4)
    value = p.getActiveWindow()
    value.close()
    p.press('right')
    p.sleep(1)
    p.press('enter')
notes()