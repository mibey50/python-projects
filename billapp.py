from flask import Flask
from html import escape
import sqlite3

app = Flask(__name__)


def run_query(sql, values=()):
    connection = sqlite3.connect("water.db")
    cursor = connection.cursor()
    cursor.execute(sql, values)
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
    return rows

def work_out_bill(previous, current):
    units = current - previous
    if units <= 10:
        water_cost = units * 50
    else:
        water_cost = 10 * 50 + (units - 10) * 80
    service = 200
    total = water_cost + service
    return units, water_cost, service, total

@app.route("/")
def home():
    customers = run_query("SELECT id, meter_no, name, previous, current, status FROM customers")
    unpaid_total = 0

    text = "<h1>Water Billing System</h1>"
    text = text + "<table border='1' cellpadding='6'>"
    text = text + "<tr><th>Meter</th><th>Customer</th><th>Previous</th><th>Current</th><th>Units</th><th>Water</th><th>Service</th><th>Total</th><th>Status</th></tr>"

    for c in customers:
        units, water_cost, service, total = work_out_bill(c[3], c[4])
        if c[5] == "Unpaid":
            unpaid_total = unpaid_total + total
        text = text + "<tr>"
        text = text + "<td>" + escape(c[1]) + "</td>"
        text = text + "<td>" + escape(c[2]) + "</td>"
        text = text + "<td>" + str(c[3]) + "</td>"
        text = text + "<td>" + str(c[4]) + "</td>"
        text = text + "<td>" + str(units) + "</td>"
        text = text + "<td>" + str(water_cost) + "</td>"
        text = text + "<td>" + str(service) + "</td>"
        text = text + "<td>" + str(total) + "</td>"
        text = text + "<td>" + escape(c[5]) + "</td>"
        text = text + "</tr>"

    text = text + "</table>"
    text = text + "<h3>Total still unpaid: KES " + str(unpaid_total) + "</h3>"
    return text

app.run(debug=True)
