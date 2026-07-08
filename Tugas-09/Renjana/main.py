from tools import (
    daily_questionnaire,
    play_game,
    process_data,
    analyze_mood,
    show_result
)
from Manager.database import (
    init_db,
    save_mood,
    get_history,
    update_mood,
    delete_mood
)

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

    print("\n=== Menu CRUD ===")
    print("1. Update Mood")
    print("2. Hapus Mood")
    print("3. Selesai")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
    id_mood = int(input("Masukkan ID mood yang ingin diupdate: "))
    hasil_baru = input("Masukkan hasil mood baru: ")
    update_mood(id_mood, hasil_baru)
    print("✅ Data mood berhasil diperbarui.")

    history = get_history()
    show_result("Data berhasil diperbarui", history)
    
    elif pilihan == "2":
    id_mood = int(input("Masukkan ID mood yang ingin dihapus: "))
    delete_mood(id_mood)
    print("✅ Data mood berhasil dihapus.")

    history = get_history()
    show_result("Data berhasil dihapus", history)

    else:
        print("Terima kasih telah menggunakan Renjana.")

if __name__ == "__main__":
    main()
