import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    fourth = now.month == 7 and now.day == 4
    return render_template("index.html", fourth=fourth)
