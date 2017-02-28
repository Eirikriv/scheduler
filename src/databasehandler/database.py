from flask import Flask, redirect, render_template, request, url_for
from flask.ext.sqlalchemy import SQLAlchemy

#Connecting to Database on pythonanywheresite
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

#Creating an importable db object of the "Courses database"
class Courses(db.Model):
    __tablename__ = "Courses"
    studentID = db.Column('studentID',db.Unicode, primary_key=True)
    courseName = db.Column('courseName', db.Unicode)
    startTime = db.Column('startTime', db.Unicode)
    endTime = db.Column('endTime', db.Unicode)
    stardate = db.Column('stardate', db.Unicode)
    enddate = db.Column('enddate', db.Unicode)
    description = db.Column('description', db.Unicode)
    location = db.Column('location', db.Unicode)
    attachments = db.Column('attachments', db.Unicode)
    def __init__(self, studentID, courseName, startTime, endTime, stardate, enddate, description, location, attachments):
        self.studentID = studentID
        self.courseName = courseName
        self.startTime = startTime
        self.endTime = endTime
        self.stardate = stardate
        self.enddate = enddate
        self.description = description
        self.location = location
        self.attachments = attachments 
