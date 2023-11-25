from flask import Flask, render_template , request
from flask_socketio import SocketIO, send
import time

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')


@socketio.on('message_from_client')
def handle_message(message):
    times = time.strftime('%H:%M')
    chat = {'message' : message,
            'times' : times
            }
    socketio.emit('message_from_server', chat)

@app.route('/')
def index():
    return render_template('index.html')
    



if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0',debug=True, port=5000)
