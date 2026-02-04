import db


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
