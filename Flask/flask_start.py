import os, sys
from flask import Flask, render_template, jsonify
from pprint import pprint
# Below if block required for packaging all files into single file using pyinstaller
if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)


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

@app.route('/serverside-table')
def serverside_table():
   return render_template('serverside_table.html')

@app.route("/serverside_table_content", methods=['GET'])
def serverside_table_content():
   data_dict=dict()
   data_dict["Column A"] = 1
   data_dict["Column B"] = 2
   data_dict["Column C"] = 3
   data_dict["Column D"] = 4
   data_dict2=dict()
   data_dict2["Column A"] = 5
   data_dict2["Column B"] = 5
   data_dict2["Column C"] = 5
   data_dict2["Column D"] = 5
   final_dict = {'data':[data_dict,data_dict2]}
   pprint(final_dict)
   json_data = jsonify(final_dict)
   print(json_data)
   return json_data


if __name__ == '__main__':
   app.run(debug = True)
   # app.run()