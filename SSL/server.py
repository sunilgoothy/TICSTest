# https://realpython.com/python-https/

# server.py
from flask import Flask

SECRET_MESSAGE = "<h1>fluffy tail</h1>"
app = Flask(__name__)

@app.route("/")
def get_secret_message():
    return SECRET_MESSAGE


app.run(debug=True, ssl_context=('./SSL/cert.pem', './SSL/key.pem'))