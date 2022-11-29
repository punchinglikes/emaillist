from flask import Flask, render_template, request
import sqlite3

conn = sqlite3.connect('db.db', check_same_thread=False)


app = Flask(__name__)


@app.route("/",  methods=('GET', 'POST'))
def home():

    if request.method == "POST":
        email = request.form['email']
        #print(email)
        #check if email already exists
        cur = conn.execute("SELECT email FROM EMAILS")
        email_exists = cur.fetchall()

        email_found = False
        for row in email_exists:
            print(row[0])
            if email == row[0]:
                print("email has already been added to the list")
                email_found = True
                return render_template("emaillist.html")
                break
        
        if email_found == False:

            conn.execute("INSERT INTO EMAILS VALUES (?)", (email,))
            conn.commit()
            print(email + " has been added to the database")
            return render_template("emaillist.html")
    elif request.method == "GET":
        return render_template("emaillist.html")

@app.route("/send", methods = ["GET", "POST"])
def sendEmail():
    if request.method == "POST":
        message = request.form['message']
        
        cur = conn.execute("SELECT email FROM EMAILS")
        email_list = cur.fetchall()
        for row in email_list:
            email = row[0]
            title = "test"
            #Could not get to actually sending an email
            print("----------------------\nemail: " + email + "\n\n Title: " + title + "\n\n Message: " + message + "\n----------------------")

        return render_template("masssend.html")

    if request.method == "GET":
        return render_template("masssend.html") 







