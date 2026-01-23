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
    game_time TEXT,
    players_needed INTEGER,
    user_id INTEGER REFERENCES users,
    created_at TEXT
);