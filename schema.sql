CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);


CREATE TABLE games (
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT,
    location TEXT,
    date TEXT,
    time TEXT,
    player_count INTEGER,
    user_id INTEGER REFERENCES users
);

CREATE TABLE classes (
    id INTEGER PRIMARY KEY,
    title TEXT,
    value TEXT
);


CREATE TABLE game_levels (
    id INTEGER PRIMARY KEY,
    level TEXT,
    game_id INTEGER REFERENCES games(id)
);

CREATE TABLE comments (
    id INTEGER PRIMARY KEY,
    game_id INTEGER REFERENCES games,
    user_id INTEGER REFERENCES users,
    content TEXT,
    sent_at TEXT
);

CREATE TABLE registrations (
    id INTEGER PRIMARY KEY,
    game_id INTEGER REFERENCES games,
    user_id INTEGER REFERENCES users
);