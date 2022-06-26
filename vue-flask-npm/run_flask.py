from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder="./webpack/static", template_folder="./webpack")


@app.route("/home")
def hello():
    return "Hello World from Flask"


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
