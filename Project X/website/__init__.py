from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_session import Session
from flask_socketio import SocketIO
import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
db = SQLAlchemy()

DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kutas'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .chats import chats

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(chats, url_prefix='/')
    from .models import User

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    create_database(app)

    return app



def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("Created database")

def create_users_directory(User):
    path = os.getcwd()
    user_login = User.login.replace(" ", "_")
    os.chdir(fr'{path}\website\Users_data')
    os.mkdir(f'{User.id}#{user_login}')
    os.chdir(fr'{User.id}#{user_login}')
    os.mkdir('user_photos')
    os.mkdir('user_video')
    verification_file = open("verification_key.txt", "x")
    verification_file.write(str(f.generate_key(), encoding="utf8"))
    os.chdir(path)

def password_recovery(mail):
    from .models import User
    path = os.getcwd()
    user = User.query.filter_by(email=mail).first()
    user_login = user.login.replace(" ", "_")
    user_key = bytes(open(f"{path}\\website\\Users_data\\{user.id}#{user_login}\\verification_key.txt", "r").read(), encoding="utf8")
    f_user = Fernet(user_key)
    encmail = str(f_user.encrypt(mail.encode()), encoding="utf8")
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
    server.login("swansytest", "Testpass!2")
    try:
        msg = MIMEMultipart()
        msg['From'] = "swansytest@gmail.com"
        msg['To'] = mail
        msg['Subject'] = "Resetowanie hasła"
        body = f"http://83.31.191.236/forgot_password_change/{user.id}/{encmail}/{user_login}"
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        server.sendmail("swansytest@gmail.com", mail , text)
    except Exception:
        pass

def password_change(passw, encmail, id, login):
    from werkzeug.security import generate_password_hash
    from . models import User
    path = os.getcwd()
    user_key = bytes(open(f"{path}\\website\\Users_data\\{id}#{login}\\verification_key.txt", "r").read(), encoding="utf8")
    f_user = Fernet(user_key)
    mail = str(f_user.decrypt(encmail.encode()), encoding="utf8")
    user = User.query.filter_by(email= mail).first()
    user.password = generate_password_hash(passw, method='sha256')
    db.session.commit()

def verification_func(email):
    from .models import User
    mail = email
    f_user = Fernet(key)
    encmail = str(f_user.encrypt(mail.encode()), encoding="utf8")
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
    server.login("swansytest", "Testpass!2")
    try:
        msg = MIMEMultipart()
        msg['From'] = "swansytest@gmail.com"
        msg['To'] = mail
        msg['Subject'] = "Verification"
        body = f"http://83.31.191.236/verification/{encmail}"
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        server.sendmail("swansytest@gmail.com", mail , text)

    except Exception:
        pass

