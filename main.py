from flask import Flask, render_template, request
import sqlite3

conn = sqlite3.connect('db.db', check_same_thread=False)


app = Flask(__name__)


@app.route("/",  methods=('GET', 'POST'))
def home():

    if request.method == "POST":
        email = request.form['email']
        print(email)
        conn.execute("INSERT INTO EMAILS VALUES (?)", (email,))
        conn.commit()
        print(email + " has been added to the database")
        return render_template("emaillist.html")
    elif request.method == "GET":


        return render_template("emaillist.html")