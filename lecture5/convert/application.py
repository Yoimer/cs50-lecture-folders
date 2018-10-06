import requests, os

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

apikey = os.getenv("API_KEY")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():

    # Query for currency exchange rate
    symbol = request.form.get("currency")
    res = requests.get("http://data.fixer.io/api/latest", params={
        "access_key": apikey, "base": "EUR", "symbols": symbol})

    # Make sure request succeeded
    if res.status_code != 200:
        return jsonify({"success": False})

    # Make sure currency is in response
    data = res.json()

    if data['success'] == False:
        return jsonify({"success": False})

    if symbol not in data['rates']:
        return jsonify({"success": False})

    return jsonify({"success": True, "rate": data["rates"][symbol]})
