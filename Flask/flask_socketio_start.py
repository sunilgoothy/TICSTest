import os, sys, json, time
from flask import Flask, render_template
from flask_socketio import SocketIO
import pandas as pd
import numpy as np
import datetime as dt

df_nf5 = pd.DataFrame([],columns=['Date Time', 'Price'])
tempdf_nf5 = pd.DataFrame([],columns=['Date Time', 'Price'])

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

socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins="*")

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

@app.route('/material')
def material():
   return render_template('material.html')
   
# @socketio.on('connect')
# def rootconnect(methods=['GET', 'POST']):
#     print('<INFO> Received CONNECT event from ROOT')
nifty_intraday_run = False
def Nifty_Intraday():
    global nifty_intraday_run
    loop_count = 0
    while(nifty_intraday_run):
        loop_count = loop_count + 1
        print(f"Loop in progress... {loop_count}")
        socketio.sleep(3)

@socketio.on('connect', namespace='/index')
def connect(methods=['GET', 'POST']):
    print('<INFO> Received CONNECT event from INDEX')
    print(f"Starting Strategy Loop...")
    global nifty_intraday_run
    nifty_intraday_run = True

@socketio.on('disconnect', namespace='/index')
def disconnect(methods=['GET', 'POST']):
    global nifty_intraday_run
    nifty_intraday_run = False
    print('<INFO> Received DISCONNECT event from INDEX')

@socketio.on('testws', namespace='/index')
def testws(jsonmsg, methods=['GET', 'POST']):
    print('<INFO> received test WebSocket Message ==> ' + jsonmsg['data'])
    msg = 'This is SUCCESS response message from WebSocket'
    # while True:
    socketio.emit('test_response', msg, namespace='/index')
        # socketio.sleep(2)

@socketio.on('start_nifty_strategy', namespace='/index')
def start_nifty_strategy(jsonmsg, methods=['GET', 'POST']):
    print(jsonmsg['data'])
    # Nifty_Intraday()


@socketio.on('ltp_tick', namespace='/index')
def ltp_tick(jsonmsg, methods=['GET', 'POST']):
    ltp = jsonmsg
    global df_nf5
    global tempdf_nf5
    # df_nf5 = pd.DataFrame(ltp.items())
    # print(type(ltp))
    print(ltp)
    # current_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # tempdf_nf5.loc[0] = pd.DataFrame([current_time, ltp['GOLDM SEP FUT']])
    # print(tempdf_nf5)
    # print(df_nf5)




if __name__ == '__main__':
    port = 5001
    print(f'<INFO> Debug Web server will run at http://127.0.0.1:{port}')
    socketio.run(app, port=port, debug=True, use_reloader=True)