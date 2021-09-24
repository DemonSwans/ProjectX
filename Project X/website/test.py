'''
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

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
someting = "kutas"
someen = f.encrypt(bytes(someting, encoding="utf8"))
print(str(f.decrypt(someen), encoding="utf8"))

import os
path = os.getcwd()
verification_key = open(f"{path}\\website\\Users_data\\1#Kutas\\verification_key.txt", "r")
print(verification_key.read())

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
DB_NAME = "database.db"
import os
from .models import User
path = os.getcwd()
user = User.query.filter_by(email=mail).first()
user_key = bytes(open(f"{path}\\website\\Users_data\\{user.id}#{user.login}\\verification_key.txt", "r"), encoding="utf8")
'''

email = "kutas@kutas."
check_mail = email.find("@")
if len(email) < 5:
    print("nope")
elif email.find(".", check_mail) == -1:
    print("nope")
elif len(email)-1 == email.find(".", check_mail):
    print("nope")
else:
    print("tak")