import sqlite3

DB_NAME = "smart_home.db"

def get_connection():
    return sqlite3.connect(DB_NAME)
