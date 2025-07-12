import csv
import random


gunung_list = []           
history_stack = []         

def load_data():
    global gunung_list
    try:
        with open('gunung.csv', mode='r', newline='', encoding='utf-8') as file:
            gunung_list = list(csv.DictReader(file))
    except FileNotFoundError:
        gunung_list = []

def save_data():
    with open('gunung.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['NamaGunung', 'Tinggi', 'Daerah'])
        writer.writeheader()
        writer.writerows(gunung_list)

def lihat_data():
    if not gunung_list:
        print("\n Tidak ada data gunung.")
        return
    print("\n Daftar Gunung:")
    for idx, g in enumerate(gunung_list, start=1):
        print(f"{idx}. {g['NamaGunung']} - {g['Tinggi']} m - {g['Daerah']}")

def tambah_data():
    nama = input("Nama Gunung: ")
    tinggi = input("Tinggi (meter): ")
    daerah = input("Daerah: ")

    if nama and tinggi and daerah:
        gunung_list.append({'NamaGunung': nama, 'Tinggi': tinggi, 'Daerah': daerah})
        save_data()
        print(" Data berhasil ditambahkan.")
    else:
        print(" Data tidak lengkap.")

def edit_data():
    lihat_data()
    try:
        idx = int(input("Pilih nomor yang ingin diedit: ")) - 1
        if 0 <= idx < len(gunung_list):
            gunung_list[idx]['NamaGunung'] = input("Nama baru: ")
            gunung_list[idx]['Tinggi'] = input("Tinggi baru (meter): ")
            gunung_list[idx]['Daerah'] = input("Daerah baru: ")
            save_data()
            print(" Data berhasil diperbarui.")
        else:
            print(" Nomor tidak valid.")
    except ValueError:
        print(" Input harus angka.")

def hapus_data():
    lihat_data()
    try:
        idx = int(input("Pilih nomor yang ingin dihapus: ")) - 1
        if 0 <= idx < len(gunung_list):
            del gunung_list[idx]
            save_data()
            print(" Data berhasil dihapus.")
        else:
            print(" Nomor tidak valid.")
    except ValueError:
        print(" Input harus angka.")

def main_game():
    if not gunung_list:
        print("\n Data kosong. Tambahkan dulu.")
        return

    soal = random.choice(gunung_list)
    nama = soal['NamaGunung']
    tinggi = int(soal['Tinggi'])
    daerah = soal['Daerah']

    print(f"\n Tebak Tinggi Gunung: {nama} di {daerah}")
    try:
        tebakan = int(input("Masukkan tebakan tinggi (meter): "))
        history_stack.append(soal)

        selisih = abs(tebakan - tinggi)
        if selisih == 0:
            print(f" Tepat! Tinggi {nama} adalah {tinggi} m.")
        elif selisih <= 100:
            print(f" Hampir benar! Tinggi {nama} adalah {tinggi} m.")
        else:
            print(f" Salah. Tinggi {nama} adalah {tinggi} m.")

        print(f" Lokasi: {daerah}\n")

    except ValueError:
        print(" Masukkan angka yang valid.")

def lihat_history():
    if not history_stack:
        print("\n Belum ada riwayat soal.")
        return
    print("\n Riwayat Soal (Terbaru ke Lama):")
    for soal in reversed(history_stack):
        print(f"- {soal['NamaGunung']} ({soal['Daerah']})")

def main_menu():
    load_data()
    while True:
        print("\n=== Mini Game Tebak Tinggi Gunung ===")
        print("1. Main Game")
        print("2. Lihat Data Gunung")
        print("3. Tambah Data Gunung")
        print("4. Edit Data Gunung")
        print("5. Hapus Data Gunung")
        print("6. Lihat Riwayat Soal")
        print("7. Keluar")

        pilihan = input("Pilih menu (1-7): ")

        if pilihan == '1':
            main_game()
        elif pilihan == '2':
            lihat_data()
        elif pilihan == '3':
            tambah_data()
        elif pilihan == '4':
            edit_data()
        elif pilihan == '5':
            hapus_data()
        elif pilihan == '6':
            lihat_history()
        elif pilihan == '7':
            print(" Terima kasih! Sampai jumpa.")
            break
        else:
            print(" Pilihan tidak valid.")


main_menu()
