import os, sys, json
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
app.debug = True
async_mode = None   

socketio = SocketIO(app, async_mode=async_mode)

@app.route('/')
def index():
   return render_template('index.html', name = 'SUNIL')

@app.route('/p5')
def p5():
   return render_template('p5.html', name = 'SUNIL')

@app.route('/vue')
def vue():
   return render_template('vue.html')

@app.template_filter()
def vue_filter(item):
    return '{{ ' + item + ' }}'

@app.route('/svg')
def svg():
   return render_template('svg.html')

@app.route('/cpl')
def cpl():
   return render_template('CPL.html')


@socketio.on('connect')
def rootconnect(methods=['GET', 'POST']):
    print('<INFO> Received CONNECT event from ROOT')

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
    while True:
        socketio.emit('test_response', msg, namespace='/index')
        socketio.sleep(2)


if __name__ == '__main__':
    print(f'<INFO> Debug Web server will run at http://127.0.0.1:5000')
    socketio.run(app, debug=True, use_reloader=True)