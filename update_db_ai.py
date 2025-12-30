import sqlite3

conn = sqlite3.connect("smart_home.db")
cursor = conn.cursor()

try:
    cursor.execute("ALTER TABLE service_requests ADD COLUMN category TEXT")
except:
    pass

try:
    cursor.execute("ALTER TABLE service_requests ADD COLUMN priority TEXT")
except:
    pass

conn.commit()
conn.close()

print("Database updated with AI fields.")
