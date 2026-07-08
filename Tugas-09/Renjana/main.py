from tools import (
    daily_questionnaire,
    process_data,
    analyze_mood,
    show_result
)
from Manager.database import init_db, save_mood, get_history

def main():
    print("Welcome to Renjana")

    # Inisialisasi database
    init_db()

    # 1. Kuesioner (mini game otomatis muncul setelah pertanyaan ke-5)
    responses = daily_questionnaire()

    # 2. Pengolahan Data
    processed_data = process_data(responses)

    # 3. Analisis Mood
    mood_result = analyze_mood(processed_data)

    # 4. Simpan ke database
    save_mood(mood_result)

    # 5. Ambil riwayat mood
    history = get_history()

    # 6. Tampilkan hasil + riwayat
    show_result(mood_result, history)

if __name__ == "__main__":
    main()
