from flask import Flask, render_template
import sqlite3 as sql

DATABASE = "stocks.db"

app=Flask(__name__)

@app.route("/")
def index():
    with sql.connect(DATABASE) as con:
        cur = con.cursor()
    res = cur.execute("select * from stocks")
    return render_template("index.html",users=res)

if __name__ == "__main__":
    app.run()