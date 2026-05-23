from datetime import datetime


aktivitas = input("Masukkan aktivitas (sarapan/berangkat kerja): ").lower()

if aktivitas == "sarapan":
    print("Menu Sarapan yang Tersedia:")
    print("1. Telur")
    print("2. Ikan")
    print("3. Nugget")
    print("4. Lainnya")

    pilihan = input ("Pilih Menu 1-4: ")

    if pilihan == "1":
        menu = "telur"
        print(f"menu {menu} tersedia, akan dimasak terlebih dahulu")

    elif pilihan == "2":
        menu = "ikan"
        print(f"menu {menu} tersedia, akan dimasak terlebih dahulu")

    elif pilihan == "3":
        menu = "nugget"
        print(f"menu {menu} tersedia, akan dimasak terlebih dahulu")

    elif pilihan == "4":
        menu = input("Masukkan menu lain: "). lower()
        print(f"bahan untuk menu {menu} tidak ada, harus membeli dahulu")

    

elif aktivitas == "berangkat kerja":
    jam_sekarang = datetime.now()
    jam_masuk = datetime(jam_sekarang.year, jam_sekarang.month, jam_sekarang.day, 8, 0)

    if jam_sekarang >= jam_masuk:
        print(f"Sudah {jam_sekarang.strftime('%H:%M')}, Anda terlambat masuk kerja")
    else:
        print(f"Masih {jam_sekarang.strftime('%H:%M')}, Anda datang tepat waktu")

else:
    print("Aktivitas tidak dikenali.")
