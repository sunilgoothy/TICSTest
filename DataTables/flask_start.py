from flask import Flask, render_template, jsonify, request
from pprint import pprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, or_
from sqlalchemy.inspection import inspect
from sqlalchemy import create_engine
import datetime 

app = Flask(__name__)

SQLITE_DB = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLITE_DB
print(f"<INFO> Database URI {app.config['SQLALCHEMY_DATABASE_URI']}")

app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.reflect()

class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

class employees(db.Model, Serializer):
    __table__ = db.Model.metadata.tables['employees']

    def serialize(self):
        d = Serializer.serialize(self)
        d['Join_Date'] = d['Join_Date'].strftime("%Y-%m-%d") # Format a datetime column
        # del d['password']   #to remove columns that should not be returned
        return d

    def __repr__(self):
        return '<employee %r>' % self.eid

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/server-side')
def serverside_table():
    return render_template('serverside_table.html')

@app.route('/client-side')
def clientside_table():
    return render_template('clientside_table.html')

@app.route("/employees_data", methods=['GET'])
def employees_data():
#    pprint(request.args)
    draw = request.args.get('sEcho')

    sort_col_id = 'mDataProp_' + request.args.get('iSortCol_0')
    sort_col = request.args.get(sort_col_id)
    sort_dir = request.args.get('sSortDir_0')
    sort_order = f"employees.{sort_col} {sort_dir}"
    print(f"Sorting on column: {sort_col}, sort direction: {sort_dir}")

    search_key = request.args.get('sSearch')
    columns = employees.__table__.columns 
    print(f"columns: {columns}")
    search_args = [col.ilike('%%%s%%' % search_key) for col in columns]

    iDisplayStart = request.args.get('iDisplayStart')
    iDisplayLength = request.args.get('iDisplayLength')

    recordsTotal = employees.query.count()
    print(f"Total Records in table: {recordsTotal}")

    filtered_data = employees.query.order_by(text(sort_order)).filter(or_(*search_args))
    EmployeesData = filtered_data.offset(iDisplayStart).limit(iDisplayLength).all()
    recordsTotal = employees.query.count()
    recordsFiltered = filtered_data.count()
    print(f"Filtered rows count: {recordsFiltered}")
    print(EmployeesData)
    serialized_data = employees.serialize_list(EmployeesData)
    # print(f"Serialized Data:")
    # pprint(serialized_data)
    json_response = {"draw": draw, "recordsTotal": recordsTotal, "recordsFiltered": recordsFiltered, "data":serialized_data}
    # print(f"JSON Response:")
    # pprint(json_response)
    return jsonify(json_response)

@app.route("/employees_client_data", methods=['GET'])
def employees_client_data():
    EmployeesData = employees.query.all()
    serialized_data = employees.serialize_list(EmployeesData)
    json_response = {"data":serialized_data}
    print(f"Client Side request processed")
    return jsonify(json_response)

@app.route("/insert_data", methods=['GET'])
def insert_data():
    engine = create_engine(SQLITE_DB)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind = engine)
    session = Session()

    join_date = datetime.datetime.strptime('2020-04-01 09:15:00.001', '%Y-%m-%d %H:%M:%S.%f')
    new_employee = employees(Name='Sunil15', Phone=8888, Join_Date=join_date, Address='Bangalore')

    session.add(new_employee)
    session.commit()
    
    return ('', 204)  

if __name__ == '__main__':
    app.run(debug = True)