from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_session import Session
from flask_socketio import SocketIO
import os

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



