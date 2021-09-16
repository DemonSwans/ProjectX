from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key= True)
    login = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    birth_date = db.Column(db.Date())
    join_date = db.Column(db.Date())
    password = db.Column(db.String(150))
