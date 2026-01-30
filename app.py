import sqlite3
from flask import Flask, abort
from flask import redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
import config
import db
import games

app = Flask(__name__)
app.secret_key = config.secret_key


def check_logged_in():
    if "user_id" not in session:
        abort(403)


@app.route("/")
def index():
    all_games = games.get_games()
    return render_template("index.html", games=all_games)


@app.route("/game/<int:game_id>")
def game(game_id):
    game = games.get_game(game_id)
    if not game:
        abort(404)
    return render_template("show_game.html", game=game)


@app.route("/new_game")
def new_game():
    check_logged_in()
    return render_template("new_game.html")


@app.route("/edit_game/<int:game_id>")
def edit_game(game_id):
    check_logged_in()
    game = games.get_game(game_id)
    if not game:
        abort(404)
    if game["user_id"] != session.get("user_id"):
        abort(403)
    return render_template("edit_game.html", game=game)


@app.route("/find_game")
def find_game():
    query = request.args.get("query")
    games_list = []
    if query:
        games_list = games.find_games_by_query(query)
    if not query:
        return render_template("find_game.html", games=games_list, query="")
    return render_template("find_game.html", games=games_list, query=query)


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
    description = request.form["description"]
    date = request.form["date"]
    time = request.form["time"]
    location = request.form["location"]
    player_count = request.form["player_count"]

    games.update_game(game_id, title, description, date, time,
                      location, player_count)
    return redirect(f"/game/{game_id}")


@app.route("/create_game", methods=["POST"])
def create_game():
    check_logged_in()
    title = request.form["title"]
    description = request.form["description"]
    date = request.form["date"]
    time = request.form["time"]
    location = request.form["location"]
    player_count = request.form["player_count"]
    user_id = session.get("user_id")

    games.add_game(title, description, date, time,
                   location, player_count, user_id)

    return redirect("/")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat"
    password_hash = generate_password_hash(password1)

    try:
        sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        db.execute(sql, [username, password_hash])
    except sqlite3.IntegrityError:
        return "VIRHE: tunnus on jo varattu"

    return "Tunnus luotu"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        sql = "SELECT id, password_hash FROM users WHERE username = ?"
        result = db.query(sql, [username])[0]
        user_id = result["id"]
        password_hash = result["password_hash"]

        if check_password_hash(password_hash, password):
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
