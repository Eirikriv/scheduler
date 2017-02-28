from flask import Flask, redirect, render_template, request, url_for
from flask.ext.sqlalchemy import SQLAlchemy
import sys
sys.path.insert(0, '/home/eirikriv/mysite/selenium')

from readFromDatabase import createAndReturnJson


app = Flask(__name__)
json = createAndReturnJson()
@app.route('/')
def hello_world():
    return json

