import db


def add_game(title, description, date, time, location, player_count, user_id):
    sql = """INSERT INTO games
             (title, description, date, time, location, player_count, user_id)
             VALUES (?, ?, ?, ?, ?, ?, ?)"""
    db.execute(sql, [title, description, date, time,
               location, player_count, user_id])


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


def update_game(game_id, title, description, date, time, location, player_count):
    sql = """UPDATE games SET title = ?, description = ?, date = ?,
             time = ?, location = ?, player_count = ?
             WHERE id = ?"""
    db.execute(sql, [title, description, date, time,
               location, player_count, game_id])
