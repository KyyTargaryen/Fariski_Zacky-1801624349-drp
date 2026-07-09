import json
import random
from datetime import datetime, timedelta

# Daftar kemungkinan hasil mood
moods = [
    "Mood Positif",
    "Mood Negatif",
    "Mood Netral"
]

data = []

# Waktu awal
start_date = datetime(2026, 1, 1, 8, 0, 0)

# Jumlah data awal
jumlah_data = 60000

for i in range(1, jumlah_data + 1):
    random_time = start_date + timedelta(minutes=random.randint(0, 500000))

    record = {
        "id": i,
        "date": random_time.strftime("%Y-%m-%d %H:%M:%S"),
        "result": random.choice(moods)
    }

    data.append(record)

with open("mood_dummy.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print("===================================")
print("Berhasil membuat mood_dummy.json")
print(f"Jumlah data : {jumlah_data}")
print("===================================")
