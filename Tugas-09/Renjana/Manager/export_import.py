import sqlite3
import json

DB_NAME = "moodtracker.db"
BACKUP_FILE = "backup.json"

def export_moods():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT date, result FROM moods ORDER BY id ASC")
    rows = c.fetchall()
    conn.close()

    data = [{"date": date, "result": result} for date, result in rows]

    with open(BACKUP_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"✅ Data berhasil diexport ke {BACKUP_FILE}")

def import_moods():
    try:
        with open(BACKUP_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("❌ File backup.json tidak ditemukan.")
        return

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    for record in data:
        c.execute("INSERT INTO moods (date, result) VALUES (?, ?)",
                  (record["date"], record["result"]))
    conn.commit()
    conn.close()

    print(f"✅ Data dari {BACKUP_FILE} berhasil diimport ke database")

if __name__ == "__main__":
    print("Menu Export/Import JSON")
    print("1. Export data mood ke backup.json")
    print("2. Import data mood dari backup.json")
    choice = input("Pilih menu (1/2): ").strip()

    if choice == "1":
        export_moods()
    elif choice == "2":
        import_moods()
    else:
        print("Pilihan tidak valid.")
