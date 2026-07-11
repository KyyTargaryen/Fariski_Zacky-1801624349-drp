from tools import (
    daily_questionnaire,
    process_data,
    analyze_mood,
    show_result
)
from Manager.database import add_priority, get_priorities, init_db, init_priorities, save_mood, get_history

def main():
    print("Welcome to Renjana")
    print ("Menu:")
    print("1. Isi kuesioner")
    print("2. Export data mood ke JSON")
    print("3. Import data mood dari JSON")
    print("4. Tambah Prioritas Aktivitas")
    print("5. Lihat Prioritas Aktivitas")

    choice = input("Pilih menu (1/2/3/4/5): ").strip()

    if choice == "4":
        kategori = input("Masukkan kategori aktivitas: ")
        add_priority(kategori)

    elif choice == "5":
        priorities = get_priorities()
        for p in priorities:
            print(p)

    # Inisialisasi database + tabel prioritas
    init_db()
    init_priorities()

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

