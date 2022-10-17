import os, sys
from flask import Flask, render_template, jsonify
# from pprint import pprint

# stdout unbuffering
sys.stdout = os.fdopen(sys.stdout.fileno(), "w", buffering=1)

# Below if block required for packaging all files into single file using pyinstaller
# if getattr(sys, 'frozen', False):
#     template_folder = os.path.join(sys._MEIPASS, 'templates')
#     static_folder = os.path.join(sys._MEIPASS, 'static')
#     app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
# else:
#     app = Flask(__name__)

# Below if block required for having static and template folders alongside exe file
if getattr(sys, "frozen", False):
    print(f"Application temporary path: {sys._MEIPASS}")
    cwd = os.path.dirname(os.path.realpath(sys.executable))  # inside executable directory
    template_folder = os.path.join(cwd, "templates")
    static_folder = os.path.join(cwd, "static")
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)
    cwd = os.path.dirname(os.path.realpath(__file__))  # inside .\<folder>\wAPP
    cwd = os.path.dirname(cwd)  # inside .\<folder>


#app = Flask(__name__)


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


if __name__ == '__main__':
   # app.run(debug = True)
   app.run(host="0.0.0.0")