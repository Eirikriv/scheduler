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

class Comment(db.Model):
    
    __tablename__ = "comments"
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=comments)

    comments.append(request.form["contents"])
    return redirect(url_for('index'))
