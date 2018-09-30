from flask import Flask

app = Flask(__name__)

#root page
@app.route('/')
def hello():
    return 'this is a Flask'

app.run('0.0.0.0', debug=True)