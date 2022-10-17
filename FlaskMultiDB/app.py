# NOT WORKING WITH FLASK-SQLALCHEMY 3.0

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///D:\DevProjects\TICSTest\FlaskMultiDB\TICSDB\config.db"
app.config["SQLALCHEMY_BINDS"] = {"oper": "sqlite:///D:\DevProjects\TICSTest\FlaskMultiDB\TICSDB\operations.db"}


db = SQLAlchemy()
db.init_app(app)
with app.app_context():
    db.reflect()
    # db.reflect("oper")

# with app.app_context():
#     db.Model.metadata.reflect(bind=db.engine, views=True)
#     db.Model.metadata.reflect(bind=db.engine, views=True)

print(db.Model.metadata.tables)
class pacArea(db.Model):
    with app.app_context():
        __bind_key__ = "oper"
    # oper_engine = db.engines["oper"]
        # oper_engine = db.get_engine(app,"oper")
        # db.Model.metadata.reflect(bind=oper_engine)
        __table__ = db.Model.metadata.tables["r_cstPacArea"]

    def __repr__(self):
        return "<pacArea %r>" % self.i_AreaNo

class Role(db.Model):
    __table__ = db.Model.metadata.tables["Roles"]

    def __repr__(self):
        return "<Roles %r>" % self.id

@app.get("/")
def index():
    all_roles = Role.query.all()
    # with app.app_context():
    all_pac = pacArea.query.all()
    return render_template("index.html", roles=all_roles, pacareas = all_pac)


if __name__ == "__main__":
    print(app.template_folder)
    app.run(debug=True)