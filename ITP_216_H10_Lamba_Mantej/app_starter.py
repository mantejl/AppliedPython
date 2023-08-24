# Name: Mantej Lamba
# USC email: mlamba@usc.edu
# ITP 216, Fall 2022
# Section: 31883R
# Assignment 10
# Description: assignment where we work with flask and a web application and make calls to json files that ask as a database

from flask import Flask, redirect, render_template, request, session, url_for
import os

from util import FileDBHelper as fdb

app = Flask(__name__)

# root end point
# routes to login unless client has already logged in
@app.route("/")
def home():
    """
    Checks whether the user is logged in and returns appropriately.
    :return: renders login.html if not logged in,
                redirects to client otherwise.
    """
    # TODO: your code goes here and replaces 'pass' below
    if not session.get("logged_in"):
        return render_template("login.html", message = "Please login to continue")
    else:
        return redirect(url_for("client"))


# client endpoint
# renders appropriate template (admin or user)
@app.route("/client")
def client():
    """
    Renders appropriate template (admin or user)
    NOTE: Should only come to /client if /login'ed successfully, i.e. (db_check_creds() returned True)

    :return: redirects home if not logged in,
                renders admin.html if logged in as admin,
                user.html otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    if not session.get("logged_in"):
        return redirect(url_for("home"))
    if session.get("username") == "admin":
        return render_template("admin.html", username = session["username"], message = "Welcome back", result = fdb.db_get_user_list(foods_db_file))
    else:
        return render_template("user.html", username = session["username"], fav_food = fdb.db_get_food(session["username"], foods_db_file))


# create user endpoint (admin only)
# adds new user to db, then re-renders admin template
@app.route("/action/createuser", methods=["POST", "GET"])
def create_user():
    """
    Gets called from admin.html form submit
    Adds a new user to db by calling db_create_user, then re-renders admin template

    :return: redirects to home if user not logged in,
                re-renders admin.html otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    if not session.get("logged_in"):
        return redirect(url_for("home"))

    if request.method == "POST":
        fdb.db_create_user(request.form["username"], request.form["password"], creds_db_file, foods_db_file)

    return render_template("admin.html", username = request.form["username"], message = "Welcome back", result = fdb.db_get_user_list(foods_db_file))

# remove user endpoint (admin only)
# removes user from db, then re-renders admin template
@app.route("/action/removeuser", methods=["POST", "GET"])
def remove_user():
    """
    Gets called from admin.html form submit
    Removes user from the db by calling db_remove_user, then re-renders admin template.

    :return: redirects to home if user not logged in,
                re-renders admin.html otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    if not session.get("logged_in"):
        return redirect(url_for("home"))

    if request.method == "POST":
        fdb.db_remove_user(request.form["username"], creds_db_file, foods_db_file)
        return render_template("admin.html", username = request.form["username"], message = "Welcome back", result = fdb.db_get_user_list(foods_db_file))

# set food endpoint (user only)
# updates user food, then re-renders user template
@app.route("/action/setfood", methods=["POST", "GET"])
def set_food():
    """
    Gets called from user.html form submit
    Updates user food by calling db_set_food, then re-renders user template

    :return: redirects to home if user not logged in,
                re-renders user.html otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    if not session.get("logged_in"):
        return redirect(url_for("home"))

    if request.method  == "POST":
        fdb.db_set_food(session["username"], request.form["set_fav_food"], foods_db_file)
        fav_food = fdb.db_get_food(session["username"], foods_db_file)


    return render_template("user.html", username = session["username"], fav_food = fdb.db_get_food(session["username"], foods_db_file))


# login endpoint
# allows client to log in (checks creds)
@app.route("/login", methods=["POST", "GET"])
def login():
    """
    Allows client to log in
    Calls db_check_creds to see if supplied username and password are correct

    :return: redirects to client if login correct,
                redirects back to home otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    if request.method == "POST":
        if fdb.db_check_creds(request.form["username"], request.form["password"],creds_db_file):
            session["username"] = request.form["username"]
            session["logged_in"] = True
            return redirect(url_for("client"))

    return redirect(url_for("home"))


# logout endpoint
@app.route("/logout", methods=["POST", "GET"])
def logout():
    """
    Logs client out, then routes to login
    Remove the user from the session
    :return: redirects back to home
    """
    # TODO: your code goes here and replaces 'pass' below
    if request.method == 'POST':
        session['logged_in'] = False
        session.pop('username', None)
    return redirect(url_for('home'))


# main entrypoint
# runs app
if __name__ == "__main__":

    creds_db_file = "./util/creds_db_file.json"
    foods_db_file = "./util/foods_db_file.json"

    # Initialize python dicts
    cred_db_dict = {"admin": "password", "user1": "pass1", "user2": "pass2", "user3": "pass3"}
    food_db_dict = {"user1": "cake", "user2": "popcorn", "user3": "pie"}

    # Save python dicts to their respective json db files
    fdb.save_dict_to_json_file(cred_db_dict, creds_db_file)
    fdb.save_dict_to_json_file(food_db_dict, foods_db_file)

    # Load json db files back to python dicts
    cred_db_dict = fdb.load_json_file_to_dict(creds_db_file)
    food_db_dict = fdb.load_json_file_to_dict(foods_db_file)
    assert cred_db_dict == {"admin": "password", 'user1': 'pass1', 'user2': 'pass2', 'user3': 'pass3'}
    assert food_db_dict == {'user1': 'cake', 'user2': 'popcorn', 'user3': 'pie'}

    # Make sure a new user is created successfully in both tables w/ the proper initial values everywhere
    fdb.db_create_user('newUser', 'newPassword', creds_db_file, foods_db_file)
    creds_db_dict = fdb.load_json_file_to_dict(creds_db_file)
    foods_db_dict = fdb.load_json_file_to_dict(foods_db_file)
    assert creds_db_dict == {"admin": "password", 'user1': 'pass1', 'user2': 'pass2', 'user3': 'pass3', 'newUser': 'newPassword'}
    assert foods_db_dict == {'user1': 'cake', 'user2': 'popcorn', 'user3': 'pie', 'newUser': 'not set yet'}

    # Make sure a user is actually removed from the DB
    fdb.db_remove_user('user3', creds_db_file, foods_db_file)
    db_dict = fdb.load_json_file_to_dict(creds_db_file)
    foods_db_dict = fdb.load_json_file_to_dict(foods_db_file)
    assert db_dict == {"admin": "password", 'user1': 'pass1', 'user2': 'pass2', 'newUser': 'newPassword'}
    assert food_db_dict == {'user1': 'cake', 'user2': 'popcorn', 'user3': 'pie'}

    # Make sure removing a user that doesn't exist behaves properly (no effect on DB)
    fdb.db_remove_user('user doesnt exist', creds_db_file, foods_db_file)
    db_dict = fdb.load_json_file_to_dict(creds_db_file)
    assert db_dict == {"admin": "password", 'user1': 'pass1', 'user2': 'pass2', 'newUser': 'newPassword'}
    assert food_db_dict == {'user1': 'cake', 'user2': 'popcorn', 'user3': 'pie'}

    # Make sure get user list function works
    assert fdb.db_get_user_list(foods_db_file) == {'user1': 'cake', 'user2': 'popcorn', 'newUser': 'not set yet'}

    # Correct username and password (green case)
    assert fdb.db_check_creds('user1', 'pass1', creds_db_file) is True
    # Wrong username but right password
    assert fdb.db_check_creds('wrong user', 'pass1', creds_db_file) is False
    # Right username but wrong password
    assert fdb.db_check_creds('user1', 'wrong password', creds_db_file) is False
    # Wrong everything
    assert fdb.db_check_creds('wrong user', 'wrong password', creds_db_file) is False

    # Spot check values
    assert fdb.db_get_food('user1', foods_db_file) == 'cake'
    assert fdb.db_get_food('newUser', foods_db_file) == 'not set yet'
    assert fdb.db_get_food('user doesnt exist', foods_db_file) == 'Not Found!'

    # Update existing user
    fdb.db_set_food('user1', 'oreos', foods_db_file)
    assert fdb.db_get_user_list(foods_db_file) == {'user1': 'oreos', 'user2': 'popcorn', 'newUser': 'not set yet'}

    app.secret_key = os.urandom(12)
    app.run(debug=True)

