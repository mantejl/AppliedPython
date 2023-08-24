from flask import Flask, redirect, render_template, request, session, url_for
import os
import sqlite3 as sl

app = Flask(__name__)
db = "favouriteFoods.db"


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
        return render_template("login.html", message="Please login to continue")
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
        return render_template("admin.html", username=session["username"], message="Welcome back", result = db_get_user_list())
    else:
        return render_template("user.html", username=session["username"], fav_food = db_get_food(session["username"]))


# create user endpoint (admin only)
# adds new user to db, then re-renders admin template
@app.route("/action/createuser", methods=["POST", "GET"])
def create_user():
    """
    Callable from admin.html only
    Adds a new user to db by calling db_create_user, then re-renders admin template

    :return: redirects to home if user not logged in,
                re-renders admin.html otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    if not session.get("logged_in"):
        return redirect(url_for("home"))

    if request.method == "POST":
        db_create_user(request.form["username"], request.form["password"])

    return render_template("admin.html", username = request.form["username"], message = "Welcome back", result = db_get_user_list())



# remove user endpoint (admin only)
# removes user from db, then re-renders admin template
@app.route("/action/removeuser", methods=["POST", "GET"])
def remove_user():
    """
    Callable from admin.html only
    Removes user from the db by calling db_remove_user, then re-renders admin template.

    :return: redirects to home if user not logged in,
                re-renders admin.html otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    if not session.get("logged_in"):
        return redirect(url_for("home"))

    if request.method == "POST":
        db_remove_user(request.form["username"])

    return render_template("admin.html", username=request.form["username"], message="Welcome back",result= db_get_user_list())


# set food endpoint (user only)
# updates user food, then re-renders user template
@app.route("/action/setfood", methods=["POST", "GET"])
def set_food():
    """
    Callable from user.html only,
    Updates user food by calling db_set_food, then re-renders user template

    :return: redirects to home if user not logged in,
                re-renders user.html otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    if not session.get("logged_in"):
        return redirect(url_for("home"))

    if request.method == "POST":
        db_set_food(session["username"], request.form["set_fav_food"])

    return render_template("user.html", username=session["username"], fav_food = db_get_food(session["username"]))


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
        if db_check_creds(request.form["username"], request.form["password"]):
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


def db_get_user_list() -> dict:
    """
    Queries the DB's userfoods table to get a list
    of all the user and their corresponding favorite food for display on admin.html.
    Called to render admin.html template.

    :return: a dictionary with username as key and their favorite food as value
                this is what populates the 'result' variable in the admin.html template
    """
    # TODO: your code goes here and replaces 'pass' below
    conn = sl.connect('favouriteFoods.db')
    curs = conn.cursor()
    stmt = 'SELECT username, food from userfoods'
    curs.execute(stmt)
    users = curs.fetchall()
    conn.close()
    user_dict = {}
    for user in users:
        user_dict[user[0]] = user[1]
    return user_dict


def db_create_user(un: str, pw: str) -> None:
    """
    Add provided user and password to the credentials table
    Add provided user to the userfoods table
    and sets their favorite food to "not set yet".
    Called from create_user() view function.

    :param un: username to create
    :param pw: password to create
    :return: None
    """
    # TODO: your code goes here and replaces 'pass' below
    conn = sl.connect('favouriteFoods.db')
    curs = conn.cursor()
    stmt1 = "INSERT INTO credentials (username,password) VALUES (?, ?)"
    v = (un, pw)
    curs.execute(stmt1, v)
    stmt2 = "INSERT INTO userfoods (username, food) VALUES (?, ?)"
    v2 = (un, 'not set yet')
    curs.execute(stmt2,v2)
    conn.commit()
    conn.close()


def db_remove_user(un: str) -> None:
    """
    Removes provided user from all DB tables.
    Called from remove_user() view function.

    :param un: username to remove from DB
    :return: None
    """
    # TODO: your code goes here and replaces 'pass' below
    conn = sl.connect('favouriteFoods.db')
    curs = conn.cursor()
    stmt = 'DELETE FROM credentials WHERE username = ?'
    v = (un,)
    curs.execute(stmt, v)
    stmt2 = 'DELETE FROM userfoods WHERE username = ?'
    curs.execute(stmt2, v)
    conn.commit()
    conn.close()


def db_get_food(un: str) -> str:
    """
    Gets the provided user's favorite food from the DB.
    Called to render user.html fav_food template variable.

    :param un: username to get favorite food of
    :return: the favorite food of the provided user as a string
    """
    # TODO: your code goes here and replaces 'pass' below
    conn = sl.connect('favouriteFoods.db')
    curs = conn.cursor()
    v = (un,)
    stmt = "SELECT food FROM userfoods WHERE username = ?"
    curs.execute(stmt, v)
    food = curs.fetchone()
    conn.close()
    if food:
        return food[0]
    else:
        return None


def db_set_food(un: str, ff: str) -> None:
    """
    Sets the favorite food of user, un param, to new incoming ff (favorite food) param.
    Called from set_food() view function.

    :param un: username to update favorite food of
    :param ff: user's new favorite food
    :return: None
    """
    # TODO: your code goes here and replaces 'pass' below
    conn = sl.connect('favouriteFoods.db')
    curs = conn.cursor()
    v = (ff,un,)
    stmt= 'UPDATE userfoods SET food = ? WHERE username = ? '
    curs.execute(stmt,v)
    conn.commit()
    conn.close()

# database function
# connects to db and checks cred param (all clients)
def db_check_creds(un, pw):
    """
    Checks to see if supplied username and password are in the DB's credentials table.
    Called from login() view function.

    :param un: username to check
    :param pw: password to check
    :return: True if both username and password are correct, False otherwise.
    """
    conn = sl.connect(db)
    curs = conn.cursor()
    v = (un,)
    stmt = "SELECT password FROM credentials WHERE username=?"
    results = curs.execute(stmt, v)  # results is an iterable cursor of tuples (result set)
    correct_pw = ''
    for result in results:
        correct_pw = result[0]  # each result is a tuple of 1, so grab the first thing in it
    conn.close()
    if correct_pw == pw:
        return True
    return False


# main entrypoint
# runs app
if __name__ == "__main__":
    # DB function unit testing:
    assert db_check_creds('alice', 'alicesSecurePassWord') == True
    assert db_check_creds('wrongUser', 'alicesSecurePassWord') == False
    assert db_check_creds('alice', 'wrongPassword') == False

    # TODO: Unit test your other db_ functions here

    app.secret_key = os.urandom(12)
    app.run(debug=True)

