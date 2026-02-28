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

CREATE INDEX idx_games_user_id ON games(user_id);
CREATE INDEX idx_game_levels_game_id ON game_levels(game_id);
CREATE INDEX idx_comments_game_id ON comments(game_id);
CREATE INDEX idx_registrations_game_id ON registrations(game_id);
CREATE INDEX idx_registrations_user_id ON registrations(user_id);