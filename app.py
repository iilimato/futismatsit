import re
import secrets
import sqlite3
import time
from flask import Flask, abort, flash, g
from flask import redirect, render_template, request, session
import markupsafe
import config
import games
import users

app = Flask(__name__)
app.secret_key = config.secret_key

@app.before_request
def before_request():
    g.start_time = time.time()

@app.after_request
def after_request(response):
    elapsed_time = round(time.time() - g.start_time, 2)
    print("elapsed time:", elapsed_time, "s")
    return response


@app.template_filter()
def show_lines(content):
    content = str(markupsafe.escape(content))
    content = content.replace("\n", "<br />")
    return markupsafe.Markup(content)


# helper: abort if user is not logged in
def check_logged_in():
    if "user_id" not in session:
        abort(403)


def check_csrf():
    if "csrf_token" not in request.form:
        abort(403)
    if "csrf_token" not in session:
        abort(403)
    if request.form["csrf_token"] != session["csrf_token"]:
        abort(403)


# pages: viewing games

@app.route("/")
def index():
    all_games = games.get_games()
    return render_template("index.html", games=all_games)


@app.route("/game/<int:game_id>")
def game(game_id):
    game = games.get_game(game_id)
    if not game:
        abort(404)
    level = games.get_level(game_id)
    comments = games.get_comments(game_id)
    registrations = games.get_registrations(game_id)
    is_registered = False
    if "user_id" in session:
        is_registered = games.is_registered(game_id, session["user_id"])
    spots_left = game["player_count"] - len(registrations)
    return render_template("show_game.html", game=game, level=level,
                           comments=comments, registrations=registrations,
                           is_registered=is_registered, spots_left=spots_left)


@app.route("/find_game")
def find_game():
    query = request.args.get("query")
    games_list = []
    if query:
        games_list = games.find_games_by_query(query)
    if not query:
        return render_template("find_game.html", games=games_list, query="")
    return render_template("find_game.html", games=games_list, query=query)


@app.route("/user/<int:user_id>")
def show_user(user_id):
    user = users.get_user(user_id)
    if not user:
        abort(404)
    user_games = users.get_games_by_user(user_id)
    user_registrations = users.get_registrations_by_user(user_id)
    return render_template("show_user.html", user=user, games=user_games,
                           registrations=user_registrations)


# pages: creating, editing, and deleting games

@app.route("/new_game")
def new_game():
    check_logged_in()
    classes = games.get_all_classes()
    return render_template("new_game.html", classes=classes)


@app.route("/edit_game/<int:game_id>")
def edit_game(game_id):
    check_logged_in()
    game = games.get_game(game_id)
    if not game:
        abort(404)
    if game["user_id"] != session.get("user_id"):
        abort(403)
    level = games.get_level(game_id)
    classes = games.get_all_classes()
    return render_template("edit_game.html", game=game, level=level, classes=classes)


@app.route("/delete_game/<int:game_id>", methods=["GET", "POST"])
def delete_game(game_id):
    check_logged_in()
    game = games.get_game(game_id)
    if not game:
        abort(404)
    if game["user_id"] != session.get("user_id"):
        abort(403)
    if request.method == "POST":
        check_csrf()
        if "confirm" in request.form:
            games.delete_game(game_id)
            return redirect("/")
        else:
            return redirect(f"/game/{game_id}")
    if request.method == "GET":
        game = games.get_game(game_id)
        return render_template("delete_game.html", game=game)


# form handlers: creating and updating games

@app.route("/create_game", methods=["POST"])
def create_game():
    check_logged_in()
    check_csrf()
    title = request.form["title"]
    if len(title) < 1 or len(title) > 50:
        abort(403)
    description = request.form["description"]
    if len(description) < 1 or len(description) > 1000:
        abort(403)
    all_classes = games.get_all_classes()
    level = request.form["Taitotaso"]
    if not level:
        abort(403)
    if "Taitotaso" not in all_classes:
        abort(403)
    if level not in all_classes["Taitotaso"]:
        abort(403)
    date = request.form["date"]
    if not re.search(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$", date):
        abort(403)
    time = request.form["time"]
    if not re.search(r"^([01][0-9]|2[0-3]):[0-5][0-9]$", time):
        abort(403)
    location = request.form["location"]
    if len(location) < 1 or len(location) > 50:
        abort(403)
    player_count = request.form["player_count"]
    if not re.search(r"^[1-9][0-9]{0,1}$", player_count):
        abort(403)
    user_id = session.get("user_id")

    games.add_game(title, description, date, time,
                   location, player_count, user_id, level)

    return redirect("/")


@app.route("/update_game", methods=["POST"])
def update_game():
    check_logged_in()
    check_csrf()
    game_id = request.form["game_id"]
    game = games.get_game(game_id)
    if not game:
        abort(404)
    if game["user_id"] != session.get("user_id"):
        abort(403)
    title = request.form["title"]
    if len(title) < 1 or len(title) > 50:
        abort(403)
    description = request.form["description"]
    if len(description) < 1 or len(description) > 1000:
        abort(403)
    date = request.form["date"]
    if not re.search(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$", date):
        abort(403)
    time = request.form["time"]
    if not re.search(r"^([01][0-9]|2[0-3]):[0-5][0-9]$", time):
        abort(403)
    location = request.form["location"]
    if len(location) < 1 or len(location) > 50:
        abort(403)
    player_count = request.form["player_count"]
    if not re.search(r"^[1-9][0-9]{0,1}$", player_count):
        abort(403)
    all_classes = games.get_all_classes()
    level = request.form["Taitotaso"]
    if not level:
        abort(403)
    if "Taitotaso" not in all_classes:
        abort(403)
    if level not in all_classes["Taitotaso"]:
        abort(403)

    games.update_game(game_id, title, description, date, time,
                      location, player_count, level)
    return redirect(f"/game/{game_id}")


# user authentication: register, login, logout

@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]

    if not username or not password1 or not password2:
        abort(403)
    if len(username) < 1 or len(username) > 20:
        abort(403)
    if len(password1) < 6:
        flash("VIRHE: salasanan tulee olla vähintään 6 merkkiä")
        return redirect("/register")
    if len(password1) > 100:
        abort(403)
    if password1 != password2:
        flash("VIRHE: salasanat eivät ole samat")
        return redirect("/register")

    try:
        users.create_user(username, password1)
    except sqlite3.IntegrityError:
        return "VIRHE: tunnus on jo varattu"

    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_id = users.check_login(username, password)
        if user_id:
            session["user_id"] = user_id
            session["username"] = username
            session["csrf_token"] = secrets.token_hex(16)
            return redirect("/")
        else:
            return "VIRHE: väärä tunnus tai salasana"


@app.route("/logout")
def logout():
    del session["user_id"]
    del session["username"]
    return redirect("/")


# form handler for creating comments

@app.route("/create_comment", methods=["POST"])
def create_comment():
    check_logged_in()
    check_csrf()

    game_id = request.form["game_id"]
    content = request.form["content"]

    if len(content) < 1 or len(content) > 1000:
        abort(403)

    game = games.get_game(game_id)
    if not game:
        abort(404)

    user_id = session["user_id"]
    games.add_comment(game_id, user_id, content)

    return redirect("/game/" + str(game_id))


# form handlers for game registration

@app.route("/register_game", methods=["POST"])
def register_game():
    check_logged_in()
    check_csrf()
    game_id = request.form["game_id"]

    game = games.get_game(game_id)
    if not game:
        abort(404)

    if games.is_registered(game_id, session["user_id"]):
        abort(403)

    count = games.count_registrations(game_id)
    if count >= game["player_count"]:
        abort(403)

    games.add_registration(game_id, session["user_id"])
    return redirect("/game/" + str(game_id))


@app.route("/unregister_game", methods=["POST"])
def unregister_game():
    check_logged_in()
    check_csrf()
    game_id = request.form["game_id"]

    game = games.get_game(game_id)
    if not game:
        abort(404)

    if not games.is_registered(game_id, session["user_id"]):
        abort(403)

    games.remove_registration(game_id, session["user_id"])
    return redirect("/game/" + str(game_id))
