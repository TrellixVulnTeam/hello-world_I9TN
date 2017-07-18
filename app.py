from flask import Flask
app = Flask(__name__)

@app.route('/')
def render_homepage():
   return 'Hello! This is Maggie\'s Homepage'

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

if __name__ == '__main__':
   app.run(debug = True)
