from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect('web.db')
    cursor = conn.cursor()
    data = cursor.execute("SELECT status FROM status").fetchall()
    con = sqlite3.connect("web.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT starttime, endtime, status, rid FROM log")
    tabel = cur.fetchall()
    return render_template("status.html", data=data, tabel=tabel)

if __name__ == '__main__':
    app.run()
