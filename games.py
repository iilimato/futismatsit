import db


def add_game(title, description, date, time, location, player_count, user_id):
    sql = """INSERT INTO games
             (title, description, date, time, location, player_count, user_id)
             VALUES (?, ?, ?, ?, ?, ?, ?)"""
    db.execute(sql, [title, description, date, time,
               location, player_count, user_id])
