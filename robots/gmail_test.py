import rpa as r
import pyautogui as p
from time import sleep

sleep(5)
print(p.position())
p.click(x=580, y=763, duration=2)
sleep(5)
p.typewrite('https://accounts.google.com/')
sleep(2)
p.press('enter')
sleep(5)
p.click(x=639, y=370, duration=2)
sleep(4)
p.typewrite('#Deadpoll29')
sleep(1)
p.press('enter')
sleep(10)
print(p.position())
p.click(x=1275, y=134, duration=2)
sleep(7)
print(p.position())
p.click(x=1049, y=418, duration=2)
