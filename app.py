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

# Start page
@app.route("/")
@app.route("/get_books")
def get_books():
    books = list(mongo.db.books.find())
    vote = mongo.db.books.find_one('book_upvote')
    return render_template("books.html", books=books, vote=vote)


# Search section on start page
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    books = list(mongo.db.books.find({"$text": {"$search": query}}))
    return render_template("books.html", books=books)


# Register
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


# LogIn Page
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


# Profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab session username
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# Log out
@app.route("/logout")
def logout():
    # remove user session cookies
    session.clear()
    flash("You have logged out")
    return redirect(url_for("login"))


# User Add book page
@app.route("/add_book", methods=["GET","POST"])
def add_book():
    if request.method == "POST":
        book = {
            #"some_data": request.form.getlist("if U want to take a hole list with same name attribute")
            "category_name": request.form.get("category_name"),
            "book_name": request.form.get("book_name"),
            "book_author": request.form.get("book_author"),
            "book_release": request.form.get("book_release"),
            "book_description": request.form.get("book_description"),
            "book_upvote": request.form.get("book_upvote"),
            "created_by": session["user"]

        }
        mongo.db.books.insert_one(book)
        flash("Book Successfully Added")
        return redirect(url_for("get_books"))
        #mongo.db.books.insert_one(request.form.to_dict())
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_book.html", categories=categories )


# Edit Book 
@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":
        submit = {
            #"some_data": request.form.getlist("if U want to take a hole list with same name attribute")
            "category_name": request.form.get("category_name"),
            "book_name": request.form.get("book_name"),
            "book_author": request.form.get("book_author"),
            "book_release": request.form.get("book_release"),
            "book_description": request.form.get("book_description"),
            "book_upvote": request.form.get("book_upvote"),
            "created_by": session["user"]

        }
        mongo.db.books.update({"_id": ObjectId(book_id)}, submit)
        flash("Book Successfully Updated")

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_book.html", book=book, categories=categories )


# Delete user owner book
@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    mongo.db.books.remove({"_id": ObjectId(book_id)})
    flash("Book Successfully Deleted")
    return redirect(url_for("get_books"))

# Categories CRUD for admin only (login = admin, password = admin)
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect("get_categories")

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)