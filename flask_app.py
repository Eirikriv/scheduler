
# A very simple Flask Hello World app for you to get started with...
import 
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return 'Hello fellow hubroers'
