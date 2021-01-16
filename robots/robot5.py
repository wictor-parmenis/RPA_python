import pyautogui as p  
from time import sleep 


# Técnica de comentar e executar.
p.hotkey('win', 'r')
sleep(1)
p.write('C:\RPA.pbix')
p.press('enter')
sleep(50)
print(p.position())
p.click(x=697, y=114, duration=3)
sleep(10)
p.click(x=687, y=406, duration=2)
sleep(5)
print(p.position())
p.click(x=1337, y=8, duration=2)
sleep(5)
print(p.position())
# p.click(x=708, y=401, duration=2)
sleep(5)
p.click(x=772, y=401, duration=2)
