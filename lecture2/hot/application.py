import requests
import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    query = requests.get("https://api.darksky.net/forecast/481d5ba64549cc9fb76fa705cb31c5cd/42.37,-71.11").json()
    temp = query["currently"]["temperature"]
    hot = True if temp > 85 else False
    return(render_template("index.html", hot=hot))
