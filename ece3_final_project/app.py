from flask import Flask, render_template, request, redirect
from pymongo import MongoClient


app = Flask(__name__)
my_connection = MongoClient("localhost", 27017)
my_db = my_connection["ece3_final"]
callme = my_db["callme"]

@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

@app.route("/callme", methods=["POST"])
def callme_details():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["number"]
    course = request.form["course"]
    callme.insert_one({
        "name":name, "email":email, "number": phone, "course":course
    })
    return redirect("/")

@app.route("/campus-tour", methods=["GET"])
def campus_tour():
    return render_template("campus_tour.html")


app.run(debug=True)