from flask import Flask, redirect, render_template, request, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask import request
import sys
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def getRequest():
    if request.method == "GET":
        return "Hubro"
    else:
        content = request.get_json(force=True)
    return content
	
