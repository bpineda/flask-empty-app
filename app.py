from flask import Flask
import os
import signal

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Welcome to this Flask Empty App!</p>"
