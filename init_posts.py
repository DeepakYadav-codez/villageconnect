import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create posts table
cursor.execute('''
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL
)
''')

conn.commit()
conn.close()

print("✅ posts table created.")
