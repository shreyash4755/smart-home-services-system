import sqlite3

conn = sqlite3.connect("smart_home.db")
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS technicians (
    tech_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    specialization TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS service_requests (
    request_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    issue TEXT NOT NULL,
    status TEXT NOT NULL,
    assigned_tech INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(assigned_tech) REFERENCES technicians(tech_id)
);
""")

conn.commit()
conn.close()

print("Database initialized successfully.")
