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

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kutas'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import  views
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
    os.chdir(fr'{path}\website\Users_data')
    os.mkdir(f'{User.id}#{User.login}')
    os.chdir(fr'{User.id}#{User.login}')
    os.mkdir('user_photos')
    os.mkdir('user_video')
    os.chdir(path)

def password_recovery(mail):
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
    server.login("swansytest", "Testpass!2")
    try:
        msg = MIMEMultipart()
        msg['From'] = "swansytest@gmail.com"
        msg['To'] = mail
        msg['Subject'] = "Resetowanie hasła"
        body = f"http://83.31.190.89/forgot_password_change/{mail}"
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        server.sendmail("swansytest@gmail.com", mail , text)
    except Exception:
        pass

def password_change(passw, mail):
    from werkzeug.security import generate_password_hash
    from . models import User
    print(mail)
    user = User.query.filter_by(email= mail).first()
    print(user.login)
    user.password = generate_password_hash(passw, method='sha256')
    db.session.commit()




