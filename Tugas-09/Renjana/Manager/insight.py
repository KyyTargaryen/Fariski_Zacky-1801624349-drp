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

def mood_insight(stats):
    if not stats:
        return

    total = stats["total"]
    positif = stats["positif"]
    netral = stats["netral"]
    negatif = stats["negatif"]

    print("\n Insight")
    if positif > negatif and positif > netral:
        print("Mayoritas mood kamu cenderung positif 😊")
    elif negatif > positif and negatif > netral:
        print("Mayoritas mood kamu cenderung negatif 😞")
    else:
        print("Mayoritas mood kamu berada di kategori cukup positif 🙂")

    # contoh tambahan: tren sederhana
    if positif/total >= 0.7:
        print("Kesimpulan: Mood kamu sangat sehat dan optimis.")
    elif negatif/total >= 0.5:
        print("Kesimpulan: Perlu perhatian, banyak mood kamu yang negatif.")
    else:
        print("Kesimpulan: Mood cukup seimbang, tidak terlalu ekstrem.")

if __name__ == "__main__":
    stats = mood_statistics()
    mood_insight(stats)