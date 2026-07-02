from tools import (
    daily_questionnaire,
    play_game,
    process_data,
    analyze_mood,
    show_result
)
from Manager.database import init_db, save_mood, get_history

def main():
    print("Welcome to Renjana")

    # Inisialisasi database
    init_db()

    # 1. Kuesioner
    responses = daily_questionnaire()

    # 2. Mini Game (setelah kuesioner selesai)
    responses = play_game(responses)

    # 3. Pengolahan Data
    processed_data = process_data(responses)

    # 4. Analisis Mood
    mood_result = analyze_mood(processed_data)

    # 5. Simpan ke database
    save_mood(mood_result)

    # 6. Ambil riwayat mood
    history = get_history()

    # 7. Tampilkan hasil + riwayat
    show_result(mood_result, history)

if __name__ == "__main__":
    main()
