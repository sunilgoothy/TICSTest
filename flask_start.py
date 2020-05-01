from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html', name = 'ISHA')

@app.route('/p5')
def p5():
   return render_template('p5.html', name = 'ISHA')

@app.route('/vue')
def vue():
   return render_template('vue.html')

@app.template_filter()
def vue_filter(item):
    return '{{ ' + item + ' }}'

if __name__ == '__main__':
   app.run(debug = True)