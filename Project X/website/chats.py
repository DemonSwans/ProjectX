from flask import Blueprint, redirect,url_for,render_template
from flask_login import login_required,current_user
from flask_socketio import join_room, leave_room, emit
from flask_socketio import SocketIO

socketio = SocketIO()

chats = Blueprint('chats',__name__)

@chats.route('/chat')
@login_required
def chat_test():
    return render_template("chat_test.html")

