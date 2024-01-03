from flask import Flask, request, render_template, redirect, session, make_response
from tools import errors, filters
import datetime

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("mainpage.html")

@app.route("/singup", methods=["POST", "GET"])
def auth():
    
    if request.method=="POST":
        username = request.form["username"]
        email = request.form['email']
        password = request.form["password"]
        
        
        if len(username) == 0 or len(email) == 0 or len(password) == 0:
            return render_template("singup.html", error=errors.emptyFieldErrorMessage)
        
        elif len(username) > 32 or len(email) > 32 or len(password) > 32:
            return render_template("singup.html", error=errors.charOverloadMessage)
        
        elif filters.chek_password(password):
            print(username, email, password)
        else: 
            return render_template("singup.html", error=errors.easyPasswordMessage)
        
    return render_template("singup.html")


app.run()

