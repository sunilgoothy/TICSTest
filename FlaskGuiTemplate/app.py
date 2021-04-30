import sys, os
from flask import Flask, render_template
from flask_socketio import SocketIO


#below imports for pyinstaller hidden imports
from engineio.async_drivers import eventlet
from eventlet.hubs import epolls, kqueue, selects
from dns import dnssec,e164,edns,entropy,exception,flags,grange,hash,inet,ipv4,ipv6,message,name,namedict
from dns import node,opcode,query,rcode,rdata,rdataclass,rdataset,rdatatype,renderer,resolver,reversename,rrset,set
from dns import tokenizer,tsig,tsigkeyring,ttl,update,version,wiredata,zone
from sqlalchemy.orm import state, strategies, strategy_options

# Below if block required for packaging all files into single file using pyinstaller
if getattr(sys, 'frozen', False):
    print(f'Application temporary path: {sys._MEIPASS}')
    cwd = os.path.dirname(os.path.realpath(sys.executable)) 
    template_folder = os.path.join(cwd, 'templates')
    static_folder = os.path.join(cwd, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)
    cwd = os.path.dirname(os.path.realpath(__file__))
    cwd = os.path.dirname(cwd)     


print(f'<INFO> Working Directory {cwd}')
print(f'<INFO> Static Directory {app.static_folder}')
print(f'<INFO> Application Name {app}')

app.config['SECRET_KEY'] = 'you-will-never-guess'
app.debug = False
async_mode = None   
app.config['TEMPLATES_AUTO_RELOAD'] = True

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
    socketio.run(app, host='0.0.0.0', use_reloader=True)
    
