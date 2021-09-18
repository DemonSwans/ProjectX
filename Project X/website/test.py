import os
import numpy as np
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

path= os.getcwd()
context = ssl.create_default_context()
server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
server.login("swansytest","Testpass!2")

msg = MIMEMultipart()
msg['From'] = "swansytest@gmail.com"
msg['To'] = "swansytest@gmail.com"
msg['Subject'] = "Resetowanie hasła"
body = "hej"
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
server.sendmail("swansytest@gmail.com","swansytest@gmail.com", text)