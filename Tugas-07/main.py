

# Soal 1: Membuat layout papan catur
def papan_catur(size=8):
    print("Papan Catur")
    for i in range(size):
        row = ""
        for j in range(size):
            if (i + j) % 2 == 0:
                row += "⬜ "   # putih
            else:
                row += "⬛ "   # hitam
        print(row)
    print("\n")  # spasi antar bagian


# Soal 2: Input aktivitas
def input_aktivitas():
    aktivitas_list = []
    print("Input Aktivitas")
    while True:
        aktivitas = input("Masukkan aktivitas atau ketik 'selesai' untuk berhenti: ")
        if aktivitas.lower() == "selesai":
            break
        
        # Tambahkan aktivitas ke list
        aktivitas_list.append({"aktivitas": aktivitas})
        
        # Tambahan detail terkait aktivitas
        detail = input(f"Detail untuk aktivitas '{aktivitas}': ")
        aktivitas_list[-1]["detail"] = detail

    # Cetak semua aktivitas
    print("\nDaftar Aktivitas:")
    for idx, data in enumerate(aktivitas_list, start=1):
        print(f"{idx}. {data['aktivitas']} - {data['detail']}")



# Main Program
if __name__ == "__main__":
    papan_catur()       # tampilkan papan catur
    input_aktivitas()   # jalankan input aktivitas
