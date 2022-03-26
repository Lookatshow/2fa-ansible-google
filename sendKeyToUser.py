#!/usr/bin/python
import requests
import sys
import smtplib

#Указать адрес и порт SMTP Relay
SMTPRelayAddres = "127.0.0.1:2222"

sender = 'linux-admin@ourdomain.com'
receivers = [f'{sys.argv[0]}@ourdomain.com']

message = f"""From: From Person <linux-admin@ourdomain.com>
To: To Person {sys.argv[0]}@ourdomain.com
Subject: SMTP e-mail privatekey + QRcode Link

 Данное сообщение отправляется пользователю чтобы доставить приватный ключ и ссылку на QRCode (опять же опционально)
"""

#Логин и пароль от доменной уз если SMTP Relay требует аутентификации
smtp.login(username, password)

try:
   
   smtpObj = smtplib.SMTP(SMTPRelayAddres)
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except SMTPException as e:
   print("Error: unable to send email: {e}")



# Отправить информацию 
# python3 sendKeyToUser UserName /path/Private.key
#(учетная запись: логин должен совпадать linux username = username@domain.com) 

