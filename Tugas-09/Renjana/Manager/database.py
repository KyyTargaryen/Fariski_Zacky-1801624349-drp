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
    c.execute("SELECT id, date, result FROM moods ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return rows

def update_mood(id, new_result):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    c.execute("""
        UPDATE moods
        SET date = ?, result = ?
        WHERE id = ?
    """, (today, new_result, id))

    conn.commit()
    conn.close()

def delete_mood(id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("DELETE FROM moods WHERE id = ?", (id,))

    conn.commit()
    conn.close()
