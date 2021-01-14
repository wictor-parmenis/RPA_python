import rpa as r 
from time import sleep
import pyautogui as p

r.init()
sleep(2)
r.url('http://www.google.com')
window = p.getActiveWindow()
window.maximize()
sleep(2)
# r.type('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input', 'Imune Kids[enter]')
r.type('//*[@name="q"]', 'Imune Kids[enter]')

sleep(2)
r.snap('page', 'img.png')
sleep(2)
r.close()