from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    message = "<h1>Training 22</h1><p>Hi, my name is Angelie</p>"
    return message