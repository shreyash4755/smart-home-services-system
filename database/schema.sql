CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact TEXT NOT NULL
);

CREATE TABLE technicians (
    tech_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    specialization TEXT NOT NULL
);

CREATE TABLE service_requests (
    request_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    issue TEXT NOT NULL,
    status TEXT NOT NULL,
    assigned_tech INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(assigned_tech) REFERENCES technicians(tech_id)
);

ALTER TABLE service_requests ADD COLUMN category TEXT;
ALTER TABLE service_requests ADD COLUMN priority TEXT;
