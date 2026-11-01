from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    data = requests.get("https://open.er-api.com/v6/latest/USD").json()
    rates = data["rates"]

    page = "<h1>Exchange rates for 1 USD</h1>"
    for code in ["KES", "EUR", "GBP", "UGX", "TZS"]:
        page = page + "<p>" + code + ": " + str(rates[code]) + "</p>"
    return page


app.run(debug=True)
