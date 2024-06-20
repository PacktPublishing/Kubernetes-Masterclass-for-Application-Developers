#!/usr/bin/env python
import os
from flask import Flask

app = Flask(__name__)

@app.route('/blue')
def hello():
    return "Hello back from: " + str(os.environ.get('HOSTNAME'))

@app.route('/health')
def health():
    return "The app is healthy!"

app.run(host='0.0.0.0', port='8080')
