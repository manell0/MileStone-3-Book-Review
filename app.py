import os

from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/get_books")
def get_books():
    books = list(mongo.db.books.find())
    vote = mongo.db.books.find_one('book_upvote')
    return render_template("books.html", books=books, vote=vote)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username exists
        existing_user =  mongo.db.users.find_one(
           {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists.")
            return redirect(url_for("register"))
        
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert(register)

        # Put new user into a cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exrists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # matching hashed password check
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # password not match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username dont exists
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab session username
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user session cookies
    session.clear()
    flash("You have logged out")
    return redirect(url_for("login"))


@app.route("/add_book")
def add_book():
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_book.html", categories=categories )


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)