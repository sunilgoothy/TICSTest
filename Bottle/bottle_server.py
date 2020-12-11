from bottle import route, run, template

@route('/hello/<name>')
def greet(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/')
def index():
    name = "SunilG"
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080, debug=True, reloader=True)