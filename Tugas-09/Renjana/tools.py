questions = [
    "1. Apakah suasana hati kamu secara umum terasa positif hari ini?",
    "2. Apakah kamu merasa berenergi untuk menjalani aktivitas hari ini?",
    "3. Apakah tidur kamu semalam cukup dan nyenyak?",
    "4. Apakah kamu merasa cemas, gelisah, atau khawatir yang berlebihan hari ini?",
    "5. Apakah ada kejadian spesifik hari ini yang merusak mood kamu?",
    "6. Apakah kamu berhasil meluangkan waktu untuk melakukan hal yang kamu sukai hari ini?",
    "7. Apakah kamu merasa mudah marah atau tersinggung hari ini?",
    "8. Apakah kamu merasa didukung atau dihargai oleh orang-orang di sekitar kamu hari ini?",
    "9. Apakah kamu bisa berkonsentrasi dengan baik dalam menyelesaikan tugas atau pekerjaan hari ini?",
    "10. Apakah kamu merasa optimis bahwa hari esok akan berjalan dengan baik?"
]

emoji_game = {
    "👍🌍": "Sukabumi",
    "💡🆖": "Lampung",
    "🦁👑": "Singaraja"
}

def mini_game():
    print("\n Stop! Tebak-tebakan dulu yuk")
    print("Tebak-tebakan emoji! (ketik 'lewati' untuk skip)")
    score = 0
    for emoji, word in emoji_game.items():
        print(f"Tebak kata dari emoji {emoji}")
        guess = input("Jawaban: ").strip().lower()
        if guess == "lewati":
            print("⏩ Kamu melewati game ini.")
        elif guess == word.lower():
            print("Benar! +1 poin 😊")
            score += 1
        else:
            print(f"Salah, kata yang benar adalah '{word}'.")
    print(f"Skor mini game kamu: {score}")
    return score

def daily_questionnaire():
    responses = []
    print("Jawab dengan 'yes' atau 'no'.")
    for idx, q in enumerate(questions):
        ans = input(f"{q} (yes/no): ").strip().lower()
        if ans == "yes":
            responses.append("😊")
        else:
            responses.append("😞")

        # Sisipkan game setelah pertanyaan ke-5
        if idx == 4:
            mini_game()   # game dipanggil sekali di sini

    return responses

def process_data(responses):
    numeric = []
    for r in responses:
        if r == "😊":
            numeric.append(1)
        elif r == "😞":
            numeric.append(0)
    return numeric

def analyze_mood(data):
    total = sum(data)
    if total >= 6:
        return "Mood Positif 😊"
    elif total >= 4:
        return "Mood Cukup Positif 🙂"
    else:
        return "Mood Negatif 😞"

def show_result(mood_result, history):
    print("\n Yeay This is your mood today!")
    print(f"Hasil mood hari ini: {mood_result}")
    print("\nRiwayat mood sebelumnya:")
    for date, result in history:
        print(f"{date} → {result}")
