import sqlite3

# Connect to database (or create if doesn't exist)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create services table
cursor.execute("""
CREATE TABLE IF NOT EXISTS services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
)
""")

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    role TEXT NOT NULL  -- 'villager', 'official'
)
""")

conn.commit()
conn.close()

print("✅ Tables created successfully in database.db")
