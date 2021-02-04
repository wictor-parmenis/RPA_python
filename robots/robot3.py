import rpa as r 
import pyautogui as auto  
from time import sleep
from datetime import datetime

# Email modules
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

r.init()
r.url('https://www.melhorcambio.com/dolar-hoje')
sleep(4)
window = auto.getActiveWindow()
window.maximize()
dolar = r.read('//*[@id="comercial"]')
sleep(2)
r.snap('page', 'img3.png')
sleep(2)
# window.close() fecha todas as janelas do
# navegador. Já o r.close() fecha apenas a 
# janela do bot.
r.close()
print(dolar)

# Session of email
text_email = f'Dolar hoje: {dolar}\nDay: {str(datetime.today())}'

# email sender, password and destiny
fromadr = 'wictorsong@gmail.com'
pwd = '###########'
toadr = 'wictorsong@gmail.com'

# Setup of MIME
message = MIMEMultipart()
message['From'] = fromadr
message['To'] = toadr
# message['To'] = toadr2

# Title of email
message['Subject'] = 'Cotação do dolar' 

# Body of email with attach
message.attach(MIMEText(text_email, 'plain'))

# Anexo
filename = 'img3.png'
attach = open('img3.png', 'rb')
p = MIMEBase('application', 'octet-stream')
p.set_payload((attach).read())

# encode em base 64
encoders.encode_base64(p)
p.add_header('Content-Disposition', 'attachment; filename= %s'% filename)
message.attach(p)

# Create SMTP session for sending mail
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls() # Security
session.login(fromadr, pwd) #Login and password of user
text = message.as_string()
session.sendmail(fromadr, toadr, text)
session.quit()

arq = open('relatory.txt', 'w')
arq.write(f'Email sended in {datetime.today()} for {toadr}')



# auto.hotkey('win', 'r')
# sleep(1)
# auto.typewrite('notepad')
# sleep(2)
# auto.press('enter')
# sleep(2)
# auto.typewrite(f'{text_email} send for {toadr}')
# sleep(2)
# value = auto.getActiveWindow()
# sleep(1)
# value.close()
# sleep(1)
# auto.press('right')
# sleep(1)
# auto.press('enter')


'''
OBS: importante adicionar um try na hora de enviar o email.  
Pois as vezes, a conexão com o SMTP falha e se é preciso reiniciar 
o script manualmente..

Próximo passo: adicionar um try and except.
'''
