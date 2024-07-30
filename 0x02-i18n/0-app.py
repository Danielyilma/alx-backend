#!/usr/bin/env python3
'''setting simple flask app'''
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    '''index page'''
    return render_template("templates/0-index.html")
