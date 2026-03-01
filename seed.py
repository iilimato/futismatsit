import random
import sqlite3

db = sqlite3.connect("database.db")

db.execute("DELETE FROM comments")
db.execute("DELETE FROM registrations")
db.execute("DELETE FROM game_levels")
db.execute("DELETE FROM games")
db.execute("DELETE FROM users")

USER_COUNT = 1000
GAME_COUNT = 10**5
COMMENT_COUNT = 10**6

locations = ["Lahden kisapuisto", "Töölön Pallokenttä 3", "Väinämöisen kenttä",
             "Tammelan stadion", "Kupittaan alakenttä",
             "Arabianrannan kenttä", "Laaksolahden jalkapallohalli", "Kuopion keskuskenttä",
             "Tikkurilan urheilupuisto", "Tapiolan urheilupuisto"]
levels = ["Aloittelijat", "Keskitaso", "Edistyneet"]

for i in range(1, USER_COUNT + 1):
    db.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
               ["user" + str(i), "hash" + str(i)])

for i in range(1, GAME_COUNT + 1):
    user_id = random.randint(1, USER_COUNT)
    location = random.choice(locations)
    player_count = random.choice([6, 8, 10, 12, 14, 22])
    db.execute("""INSERT INTO games (title, description, location, date, time,
                  player_count, user_id)
                  VALUES (?, ?, ?, ?, ?, ?, ?)""",
               ["peli" + str(i), "kuvaus" + str(i), location,
                "2026-03-" + str(random.randint(1, 28)).zfill(2),
                str(random.randint(10, 21)) + ":00",
                player_count, user_id])
    level = random.choice(levels)
    db.execute("""INSERT INTO game_levels (level, game_id)
                  VALUES (?, ?)""", [level, i])

for i in range(1, COMMENT_COUNT + 1):
    user_id = random.randint(1, USER_COUNT)
    game_id = random.randint(1, GAME_COUNT)
    db.execute("""INSERT INTO comments (content, sent_at, user_id, game_id)
                  VALUES (?, datetime('now'), ?, ?)""",
               ["kommentti" + str(i), user_id, game_id])

db.commit()
db.close()

print("Seed data created")
