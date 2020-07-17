from flask import Flask, render_template
from flask_socketio import SocketIO
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = 'you-will-never-guess'
app.debug = True
async_mode = None               #For Eventlet WebSockets
# async_mode = 'threading'        #For Multithreading

task_list = ['First Task', 'Second Task', 'Third Task']


socketio = SocketIO(app, async_mode=async_mode)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@socketio.on('connect', namespace='/tasks')
def connect(methods=['GET', 'POST']):
    print('Received Connect Event.')


@socketio.on('testws', namespace='/tasks')
def testws(jsonmsg, methods=['GET', 'POST']):
    print('received test WebSocket Message: ' + str(jsonmsg))
    socketio.emit('test_response', jsonmsg, namespace='/tasks')

@socketio.on('get_tasks', namespace='/tasks')
def get_tasks(jsonmsg, methods=['GET', 'POST']):
    print('received get task ' + str(jsonmsg))
    response = json.dumps(task_list)
    socketio.emit('task_list', response, namespace='/tasks')

@socketio.on('add_task', namespace='/tasks')
def add_task(jsonmsg, methods=['GET', 'POST']):
    print('received Add task ' + str(jsonmsg))
    print(jsonmsg['data'])
    task_list.append(jsonmsg['data'])
    response = json.dumps(task_list)
    socketio.emit('task_list', response, namespace='/tasks')

if __name__ == "__main__":
    print(f'<INFO> Debug Web server will run at http://127.0.0.1:5000')
    socketio.run(app, debug=True, use_reloader=True)

