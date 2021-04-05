import sys, os
from flask import Flask, render_template
from flask_socketio import SocketIO

# Below if block required for packaging all files into single file using pyinstaller
if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)

app.config['SECRET_KEY'] = 'you-will-never-guess'
app.debug = False
async_mode = None   

socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins="*")

@app.route('/')
def index():
   return render_template('index.html', name = 'SUNIL')

@socketio.on('connect', namespace='/index')
def connect(methods=['GET', 'POST']):
    print('<INFO> Received CONNECT event from INDEX')

@socketio.on('disconnect', namespace='/index')
def disconnect(methods=['GET', 'POST']):
    print('<INFO> Received DISCONNECT event from INDEX')

@socketio.on('testws', namespace='/index')
def testws(jsonmsg, methods=['GET', 'POST']):
    print('<INFO> received test WebSocket Message ==> ' + jsonmsg['data'])
    msg = 'This is SUCCESS response message from WebSocket'
    socketio.emit('test_response', msg, namespace='/index')

if __name__ == "__main__":
    socketio.run(app, use_reloader=True)
    
