import sqlite3
from datetime import datetime

DB_NAME = "moodtracker.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS moods (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    result TEXT
                )''')
    conn.commit()
    conn.close()

def save_mood(result):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO moods (date, result) VALUES (?, ?)", (today, result))
    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT date, result FROM moods ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return rows

def init_priorities():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS priorities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category TEXT
                )''')
    conn.commit()
    conn.close()

def add_priority(category):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO priorities (category) VALUES (?)", (category,))
    conn.commit()
    conn.close()
    print("✅ Prioritas berhasil ditambahkan.")

def get_priorities():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT id, category FROM priorities")
    rows = c.fetchall()
    conn.close()
    return rows

def update_priority(id, new_category):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE priorities SET category=? WHERE id=?", (new_category, id))
    conn.commit()
    conn.close()
    print("✅ Prioritas berhasil diperbarui.")

def delete_priority(id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM priorities WHERE id=?", (id,))
    conn.commit()
    conn.close()
    print("✅ Prioritas berhasil dihapus.")
