from datetime import datetime


aktivitas = input("Masukkan aktivitas (sarapan/berangkat kerja): ").lower()

if aktivitas == "sarapan":
    menu = input("Menu sarapan yang diinginkan: ").lower()
    bahan_tersedia = ["telur", "ikan", "nugget"]

    if menu in bahan_tersedia:
        print(f"Menu {menu} tersedia, perlu dimasak terlebih dahulu.")
    else:
        print(f"Bahan untuk menu {menu} tidak ada, harus membeli dulu.")

elif aktivitas == "berangkat kerja":
    jam_sekarang = datetime.now()
    jam_masuk = datetime(jam_sekarang.year, jam_sekarang.month, jam_sekarang.day, 8, 0)

    if jam_sekarang >= jam_masuk:
        print(f"Sudah {jam_sekarang.strftime('%H:%M')}, Anda terlambat masuk kerja")
    else:
        print(f"Masih {jam_sekarang.strftime('%H:%M')}, Anda datang tepat waktu")

else:
    print("Aktivitas tidak dikenali.")
