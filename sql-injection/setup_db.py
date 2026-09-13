import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

cursor.execute("""
INSERT INTO users (username, password)
VALUES ('alice', 'password123')
""")

conn.commit()
conn.close()

print("Database created successfully.")
