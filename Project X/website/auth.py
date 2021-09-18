from flask import Blueprint, render_template, request, flash, redirect, url_for
import string
from .models import User
from . import db,create_users_directory,password_recovery
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user,login_required,logout_user,current_user
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

auth = Blueprint('auth',__name__)


@auth.route('/',methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        login = request.form.get('login')
        haslo = request.form.get('haslo')
        user = User.query.filter_by(login=login).first()
        if user:
            if check_password_hash(user.password, haslo):
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))

    return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/register',methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        login = request.form.get('login')
        email = request.form.get('email')
        haslo = request.form.get('haslo')
        haslo_powt = request.form.get('haslo_powt')
        day = request.form.get('dzien')
        month = request.form.get('miesiac')
        year = request.form.get('rok')
        ymd = f'{year}-{month}-{day}'
        birth_date = datetime.datetime.strptime(ymd, '%Y-%m-%d')
        join_date = date.today()
        special_characters = string.punctuation
        tfhaslo = list(map(lambda char: char in special_characters, haslo))
        user_login = User.query.filter_by(login=login).first()
        user_email = User.query.filter_by(email=email).first()
        if user_email or user_login:
            flash('Dany login/email jest zajęty', category='error')
        elif relativedelta(date.today(),birth_date).years >70:
            flash('Zbyt odległa data urodzenia', category='error')
        elif len(email) < 5:
            flash('To nie email', category='error')
        elif len(haslo) < 7 or not (haslo.islower() == False and haslo.isupper() == False) or not any(tfhaslo) or not (any(map(str.isdigit, haslo))):
            flash('Hasło nie spełnia wymagań', category='error')
        elif haslo != haslo_powt:
            flash('Hasła nie są identyczne', category='error')
        else:
            new_user = User(login=login,email=email,birth_date=birth_date,join_date=join_date,password=generate_password_hash(haslo, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            create_users_directory(current_user)
            return redirect(url_for('views.home'))

    if current_user.is_authenticated:
        return redirect(url_for('views.home'))



    return render_template("register.html")

@auth.route('/forgot_password_change', methods=['GET','POST'])
def forgot_password_change():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    if request.method == "POST":
        pass1 = request.form.get('pass1')
        pass2 = request.form.get('pass2')
        code = request.form.get('code')
        print(pass1 + " " + pass2 + " " + code)
    return  render_template("forgot_pass.html")

@auth.route('/forgot_password', methods=['GET','POST'])
def forgot_password():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    if request.method == "POST":
        mail = request.form.get('mail')
        password_recovery(mail)
    return  render_template("forgot_pass.html")