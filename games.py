import db


def get_all_classes():
    sql = "SELECT title, value FROM classes ORDER BY id"
    result = db.query(sql)

    classes = {}
    for title, value in result:
        classes[title].append(
            value) if title in classes else classes.setdefault(title, [value])

    return classes


def add_game(title, description, date, time, location, player_count, user_id, level):
    sql = """INSERT INTO games
             (title, description, date, time, location, player_count, user_id)
             VALUES (?, ?, ?, ?, ?, ?, ?)"""
    db.execute(sql, [title, description, date, time,
               location, player_count, user_id])

    game_id = db.last_insert_id()

    sql_level = """INSERT INTO game_levels (game_id, level)
                   VALUES (?, ?)"""
    db.execute(sql_level, [game_id, level])


def get_games():
    sql = """SELECT games.id, games.title, games.description,
             games.date, games.time, games.location,
             games.player_count, users.username
             FROM games LEFT JOIN users
             ON games.user_id = users.id
             ORDER BY games.id DESC"""
    return db.query(sql)


def get_game(game_id):
    sql = """SELECT games.id, games.title, games.description,
             games.date, games.time, games.location,
             games.player_count, users.id user_id, users.username
             FROM games LEFT JOIN users
             ON games.user_id = users.id
             WHERE games.id = ?"""
    result = db.query(sql, [game_id])
    if len(result) == 0:
        return None
    return result[0]


def update_game(game_id, title, description, date, time, location, player_count, level):
    sql = """UPDATE games SET title = ?, description = ?, date = ?,
             time = ?, location = ?, player_count = ?
             WHERE id = ?"""
    db.execute(sql, [title, description, date, time,
               location, player_count, game_id])
    sql_level = """UPDATE game_levels SET level = ?
                   WHERE game_id = ?"""
    db.execute(sql_level, [level, game_id])


def delete_game(game_id):
    sql_registrations = "DELETE FROM registrations WHERE game_id = ?"
    db.execute(sql_registrations, [game_id])
    sql_comments = "DELETE FROM comments WHERE game_id = ?"
    db.execute(sql_comments, [game_id])
    sql_levels = "DELETE FROM game_levels WHERE game_id = ?"
    db.execute(sql_levels, [game_id])
    sql = "DELETE FROM games WHERE id = ?"
    db.execute(sql, [game_id])


def find_games_by_query(query):
    sql = """SELECT games.id, games.title, games.description,
             games.date, games.time, games.location,
             games.player_count, users.username
             FROM games LEFT JOIN users
             ON games.user_id = users.id
             WHERE games.title LIKE ? OR games.description LIKE ? OR games.location LIKE ?
             ORDER BY games.id DESC"""
    like_query = f"%{query}%"
    return db.query(sql, [like_query, like_query, like_query])


def get_level(game_id):
    sql = "SELECT level FROM game_levels WHERE game_id = ?"
    result = db.query(sql, [game_id])
    if len(result) == 0:
        return None
    return result[0]["level"]


def add_comment(game_id, user_id, content):
    sql = """INSERT INTO comments (game_id, user_id, content, sent_at)
             VALUES (?, ?, ?, datetime('now'))"""
    db.execute(sql, [game_id, user_id, content])


def get_comments(game_id):
    sql = """SELECT comments.id, comments.content, comments.sent_at,
                    users.id user_id, users.username
             FROM comments, users
             WHERE comments.game_id = ? AND comments.user_id = users.id
             ORDER BY comments.id DESC"""
    return db.query(sql, [game_id])


def add_registration(game_id, user_id):
    sql = "INSERT INTO registrations (game_id, user_id) VALUES (?, ?)"
    db.execute(sql, [game_id, user_id])


def remove_registration(game_id, user_id):
    sql = "DELETE FROM registrations WHERE game_id = ? AND user_id = ?"
    db.execute(sql, [game_id, user_id])


def get_registrations(game_id):
    sql = """SELECT users.id user_id, users.username
             FROM registrations, users
             WHERE registrations.game_id = ? AND registrations.user_id = users.id
             ORDER BY registrations.id"""
    return db.query(sql, [game_id])


def is_registered(game_id, user_id):
    sql = "SELECT id FROM registrations WHERE game_id = ? AND user_id = ?"
    result = db.query(sql, [game_id, user_id])
    return len(result) > 0


def count_registrations(game_id):
    sql = "SELECT COUNT(*) count FROM registrations WHERE game_id = ?"
    result = db.query(sql, [game_id])
    return result[0]["count"]
