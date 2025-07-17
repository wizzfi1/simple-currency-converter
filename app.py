from flask import flask,   
render_template, request, redirect
import requests
import sqlite3
from datetime import datetime

app = flask(_name_)

#DB setup

def init_db():
    conn = 
    sqlite3.connect('database_db')
    c = conn.cursor()
    c.execute(''' CREATE TABLE IF NOT EXISTS conversions (
    id INTEGER PRIMARY KEY
    AUTOINCREMENT,
    usd-amount REAL,
    target_currency TEXT,
    converted_amount REAL,
    timestamp TEXT 
    )''')
    conn.commit()
    conn.close()

    @app.route("/", methods= ["GET", "POST"])
    def index():
        result= None
        if request.method== "POST":
            usd_amount = 
            float (request.form ["usd_amount"])
            target target_currency= 
            request.form["target_currency"]

            res= 
            requests.get("https://open.er-api.com/v6/latest/USD").json()
            rate = 
            res["rates"].get (target_currency)

            if rate:
                converted = usd_amount * rate

                conn = 
                sqlite3.connect('database.db')
                c= conn.cursor ()
                c.execute("INSERT INTO conversions (usd_amount, target_currency, converted amount, timestamp) VALUES (?,?,?,?)",(usd_amount, target_currency, converted, datetime.now(), isoformat())))
                conn.commit()
                conn.close()

                conn= 
                sqlite3.connect('database.db')
                c= conn.cursor()
                c= execute(SELECT usd_amount, target_currency, converted_amount, timestamp FROM conversions ORDER BY id DESC)
                history = c.fetchall()
                conn.close()

                return
                render_template("index.html", history=history)

                if _name_ == "_main_":
                    init(db)
                    app.run(debug=True)

                    

             