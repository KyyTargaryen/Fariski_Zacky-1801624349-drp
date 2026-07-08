import sqlite3

DB_NAME = "moodtracker.db"

def mood_statistics():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT result FROM moods")
    rows = c.fetchall()
    conn.close()

    total = len(rows)
    if total == 0:
        print("❌ Tidak ada data mood di database.")
        return None

    positif = sum(1 for r in rows if "Positif" in r[0])
    netral = sum(1 for r in rows if "Cukup" in r[0])
    negatif = sum(1 for r in rows if "Negatif" in r[0])

    stats = {
        "total": total,
        "positif": positif,
        "netral": netral,
        "negatif": negatif
    }

    print(" Your Mood Statistics ")
    print(f"Total data: {total}")
    print(f"Mood Positif: {positif} ({(positif/total)*100:.1f}%)")
    print(f"Mood Cukup Positif: {netral} ({(netral/total)*100:.1f}%)")
    print(f"Mood Negatif: {negatif} ({(negatif/total)*100:.1f}%)")

    return stats