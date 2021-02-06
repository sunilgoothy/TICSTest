import os, sys
from flask import Flask, render_template, jsonify
from pprint import pprint
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)


SQLITE_DB = 'sqlite://database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLITE_DB
print(f"<INFO> Database URI {app.config['SQLALCHEMY_DATABASE_URI']}")

app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Alarm(db.Model):
    __table__ = db.Model.metadata.tables['AlarmHistory']

    def __repr__(self):
        return '<Alarm %r>' % self.i_AlarmId

@app.route('/Alarm-Report')
def CreateAlarmReport():
    AlarmData =Alarm.query.order_by(Alarm.dt_StartTime.desc()).limit(5000).all()
    return render_template('AlarmReport.html', AlarmData=AlarmData , pagetitle="Alarm Reports")   

@app.route('/')
def serverside_table():
   return render_template('serverside_table.html')

@app.route("/serverside_get_data", methods=['GET'])
def serverside_get_data():
   AlarmData =Alarm.query.order_by(Alarm.dt_StartTime.desc()).limit(5000).all()
   #  return render_template('AlarmReport.html', AlarmData=AlarmData , pagetitle="Alarm Reports")  
   print(AlarmData)
   return 200

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