import sqlite3

conn = sqlite3.connect("smart_home.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO users (name, contact) VALUES (?, ?)", ("Amit", "9999999999"))
cursor.execute("INSERT INTO technicians (name, specialization) VALUES (?, ?)", ("Rahul", "Electrical"))

conn.commit()
conn.close()

print("Sample data inserted.")
