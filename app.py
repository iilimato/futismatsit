import re
import sqlite3
from flask import Flask, abort
from flask import redirect, render_template, request, session
import config
import games
import users

app = Flask(__name__)
app.secret_key = config.secret_key


# helper: abort if user is not logged in
def check_logged_in():
    if "user_id" not in session:
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
    # game["level"] = level
    return render_template("show_game.html", game=game, level=level)


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
    return render_template("show_user.html", user=user, games=user_games)


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
    title = request.form["title"]
    if len(title) < 1 or len(title) > 50:
        abort(403)
    description = request.form["description"]
    if len(description) < 1 or len(description) > 1000:
        abort(403)
    all_classes = games.get_all_classes()
    level = request.form["Taitotaso"]
    if level:
        if "Taitotaso" not in all_classes:
            abort(403)
        if level not in all_classes["Taitotaso"]:
            abort(403)
    date = request.form["date"]
    if not re.search(r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.\d{4}$", date):
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
    if not re.search(r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.\d{4}$", date):
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
    if level:
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
    if len(password1) < 4 or len(password1) > 100:
        abort(403)
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat"

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
            return redirect("/")
        else:
            return "VIRHE: väärä tunnus tai salasana"


@app.route("/logout")
def logout():
    del session["user_id"]
    del session["username"]
    return redirect("/")
