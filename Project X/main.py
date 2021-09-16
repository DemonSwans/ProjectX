from website import create_app
from flask_socketio import SocketIO, send
from flask_login import current_user
import string
import time

app = create_app()
socketio = SocketIO(app)

@socketio.on('message')
def handleBroadcastMessage(msg):
    username = current_user.login
    if msg != '':
	    send(username+': '+msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app,debug=True, host="192.168.1.10", port=80)