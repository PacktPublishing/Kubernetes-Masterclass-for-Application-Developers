#!/usr/bin/env python
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello back!"

app.run(host='0.0.0.0', port='8080')
