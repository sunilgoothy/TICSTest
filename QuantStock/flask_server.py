from flask import Flask, render_template
from flask_socketio import SocketIO
import datetime as dt
import sqlite3

template_folder = 'templates'
static_folder = 'static'

app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
app.config['SECRET_KEY'] = 'you-will-never-guess'
async_mode = None  

socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins="*")

@app.route('/')
def index():
   print('<INFO> Request received at root route')

@socketio.on('connect', namespace='/index')
def connect(methods=['GET', 'POST']):
    print('<INFO> Received CONNECT event')

@socketio.on('disconnect', namespace='/index')
def disconnect(methods=['GET', 'POST']):
    print('<INFO> Received DISCONNECT event')

@socketio.on('ltp_tick', namespace='/index')
def ltp_tick(jsonmsg, methods=['GET', 'POST']):
    current_time = dt.datetime.now()
    seconds = current_time.strftime("%S ")
    print(seconds, end='', flush=True)
    if current_time.minute % 1 == 0 and current_time.second % 60 == 0:
        current_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        print(current_time)
        connection = sqlite3.connect("data\\stocks.db3")
        cursor = connection.cursor()   
        for (scrip, value) in jsonmsg.items():
            print(scrip, value)  
            cursor.execute("Insert into Intraday values (?, ?, ?)", (current_time, scrip, value))
            connection.commit()
        
        connection.close()

if __name__ == '__main__':
    port = 5001
    print(f'<INFO> Debug Web server will run at http://127.0.0.1:{port}')
    socketio.run(app, port=port, debug=True, use_reloader=True)