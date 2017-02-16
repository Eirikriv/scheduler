from flask import Flask, redirect, render_template, request, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="eirikriv",
    password="hubrohubro",
    hostname="eirikriv.mysql.pythonanywhere-services.com",
    databasename="eirikriv$Courses",
)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
comments = []

class Courses(db.Model):
    __tablename__ = "Courses"
    studentid = db.Column('studentid',db.Unicode, primary_key=True)
    courseid = db.Column('courseid', db.Unicode)
    coursename = db.Column('coursename',db.Unicode)
    def __init__(self, studentid, courseid, coursename):
        self.studentid = studentid
        self.courseid = courseid
        self.coursename = coursename
 
