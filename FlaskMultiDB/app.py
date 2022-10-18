# NOT WORKING WITH FLASK-SQLALCHEMY 3.0
# UPDATE: FLASK-SQLALCHEMY 3.0 Now working with below code. Had to use sessionmaker and session while querying.

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'DB\config.db')
app.config["SQLALCHEMY_BINDS"] = {"oper": 'sqlite:///' + os.path.join(basedir, 'DB\operations.db')}


db = SQLAlchemy(app)
with app.app_context():
    db.reflect()
    db.Model.metadata.reflect(bind=db.engines["oper"], views=True)
    db_oper_session = sessionmaker(bind=db.engines["oper"], expire_on_commit=False)

# print(db.Model.metadata.tables)

class Role(db.Model):
    __table__ = db.Model.metadata.tables["Roles"]

    def __repr__(self):
        return "<Roles %r>" % self.id

class pacArea(db.Model):
    __table__ = db.Model.metadata.tables["r_cstPacArea"]

    def __repr__(self):
        return "<pacArea %r>" % self.i_AreaNo


@app.get("/")
def index():
    all_roles = Role.query.all()
    with db_oper_session.begin() as session:
        all_pac = session.query(pacArea).all()

    for area in all_pac:
        print(area.c_Description)
    return render_template("index.html", roles=all_roles, pacareas = all_pac)


if __name__ == "__main__":
    app.run(debug=True)