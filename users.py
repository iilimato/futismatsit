from werkzeug.security import check_password_hash, generate_password_hash

import db


def create_user(username, password):
    password_hash = generate_password_hash(password)
    sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
    db.execute(sql, [username, password_hash])


def check_login(username, password):
    sql = "SELECT id, password_hash FROM users WHERE username = ?"
    result = db.query(sql, [username])
    if not result:
        return None

    user_id = result[0]["id"]
    password_hash = result[0]["password_hash"]
    if check_password_hash(password_hash, password):
        return user_id
    else:
        return None


def get_user(user_id):
    sql = "SELECT id, username FROM users WHERE id = ?"
    result = db.query(sql, [user_id])
    if len(result) == 0:
        return None
    return result[0]


def get_games_by_user(user_id):
    sql = """SELECT games.id, games.title, games.description,
             games.date, games.time, games.location,
             games.player_count
             FROM games
             WHERE games.user_id = ?
             ORDER BY games.id DESC"""
    return db.query(sql, [user_id])
