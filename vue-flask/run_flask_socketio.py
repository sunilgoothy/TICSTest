from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")

app.config['SECRET_KEY'] = 'you-will-never-guess'
app.debug = True
async_mode = None   

socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins="*")

@app.route("/home")
def hello():
    return "Hello World from Flask"

@app.route('/')
def home():
    return render_template("index.html")   

if __name__ == "__main__":
	socketio.run(app, port=5000, debug=True, use_reloader=True)