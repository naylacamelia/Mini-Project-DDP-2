from prettytable import PrettyTable

data = {
    "2409116015": {"Nama": "Afrillia Putri", "Judul_Project": "Sistem Pemberian Nilai Rapor", "Tanggal": "10 Oktober 2024", "Waktu": "10:20", "Status": "disetujui"},
    "2409116009": {"Nama": "Nayla Camelia", "Judul_Project": "Sistem Penulisan Buku Harian", "Tanggal": "10 Oktober 2024", "Waktu": "13:00", "Status": "disetujui"},
}

tabel = PrettyTable()
tabel.field_names = ["Nama", "NIM", "Judul Project", "Tanggal", "Waktu", "Status"]

# Fungsi untuk memperbarui tabel setelah perubahan data
def perbarui_tabel():
    tabel.clear_rows()
    for Nim, detail in data.items():
        tabel.add_row([detail["Nama"], Nim, detail["Judul_Project"], detail["Tanggal"], detail["Waktu"], detail["Status"]])
perbarui_tabel()

# Fungsi untuk melihat jadwal
def lihat_jadwal():
    print(tabel)

# Fungsi untuk menambah jadwal
def tambah_jadwal():
    try:
        Nama = input("\nMasukkan nama siswa: ")
        Nim = input("Masukkan NIM anda: ")
        Judul_Project = input("Masukkan judul project: ")
        Tanggal = input("Masukkan jadwal Konsultasi (hh-bulan-tttt): ")
        Waktu = input("Masukkan waktu Konsultasi (jj:mm): ")
        Status = input("Masukkan Status Konsultasi (disetujui/tidak disetujui): ").lower()
        
        # Status jadwal harus  (disetujui/tidak disetujui)
        if Status not in ["disetujui", "tidak disetujui"]:
            print("Status yang dimasukkan tidak valid. Silakan coba lagi.")
            return tambah_jadwal()
        
        # Menggunakan NIM sebagai kunci pembeda
        data[Nim] = {"Nama": Nama, "Judul_Project": Judul_Project, "Tanggal": Tanggal, "Waktu": Waktu, "Status": Status}
        perbarui_tabel()
        print("\nBerikut adalah jadwal konsultasi data telah diperbarui: ")
        lihat_jadwal()
        print(f"Jadwal untuk siswa {Nama} dengan judul {Judul_Project} berhasil ditambahkan!")
    except ValueError:
        print("Input tidak valid. Silakan coba lagi.")
    
# Fungsi untuk memperbarui data pada jadwal
def update_jadwal():
    while True:
        Nim = input("\nMasukkan NIM dari mahasiswa yang ingin diubah statusnya: ")
        if Nim in data:
            break  # Keluar dari perulangan jika NIM ditemukan
        else:
            print("NIM tidak ditemukan. Silakan coba lagi.")
            
    # Meminta input status yang valid
    while True:
        Ubah_Status = input("Masukkan status konsultasi terbaru (disetujui/tidak disetujui): ").lower()
        if Ubah_Status in ["disetujui", "tidak disetujui"]:
            break  # Keluar dari perulangan jika status valid
        else:
            print("Status tidak valid. Silakan coba lagi.")
            
    # Memperbarui status pada data
    data[Nim]["Status"] = Ubah_Status
    print(f"Status untuk mahasiswa dengan NIM '{Nim}' berhasil diperbarui menjadi '{Ubah_Status}'.")
    perbarui_tabel()
    print("\nBerikut adalah jadwal Konsultasi setelah data diperbarui:")
    lihat_jadwal()

# Fungsi untuk menghapus data pada jadwal
def hapus_jadwal():
        lihat_jadwal()
        Nim = input("\nMasukan NIM mahasiswa yang jadwalnya ingin dihapus: ")
        if Nim in data:
            del data[Nim]
            perbarui_tabel()
            print("\nBerikut adalah jadwal konsultasi setelah data dihapus:")
            lihat_jadwal()
            print(f"\nJadwal untuk mahasiswa dengan NIM {Nim} telah dihapus.")
        else:
            print("NIM tidak ditemukan. Silakan coba lagi.")

# Fungsi untuk melakukan login
def login():
    while True:
        print("=" * 10 + " KONSULTASI PROJECT AKHIR " + "=" * 10)
        print("[1]. Mahasiswa")
        print("[2]. Dosen")
        pilihan = input("Pilih mode login sesuai dengan role anda: ")
        if pilihan == "1":
            mahasiswa()
        elif pilihan == "2":
            dosen()
            break
        else:
            print("Pilihan login tidak tersedia.")
            return login()
        
# Fungsi menu mahasiswa
def mahasiswa():
    print("")
    print("=" * 6 + " Halo, Selamat datang! " + "=" * 6)
    Nama = input("Masukkan nama anda: ")
    print(f"\nHalo {Nama}! Berikut adalah jadwal konsultasi saat ini: ")
    lihat_jadwal()
    
    # Meminta input untuk jadwal baru yang ingin diajukan
    Nama = input("\nMasukkan nama lengkap anda: ")
    Nim = input("Masukkan NIM anda: ")
    Judul_Project = input("Masukkan judul project yang ingin anda konsulkan: ")
    Tanggal = input("Tanggal konsultasi (contoh: 01 Januari 2024): ")
    Waktu = input("Waktu konsultasi (contoh: 12:30): ")
    Status = "Menunggu persetujuan"
    
    # Menambahkan jadwal 
    data[Nim] = {"Nama": Nama, "Judul_Project": Judul_Project, "Tanggal": Tanggal, "Waktu": Waktu, "Status": Status}
    perbarui_tabel()
    lihat_jadwal()
    print(f"\nJadwal konsultasi anda dengan judul {Judul_Project} berhasil diajukan!")
    
    # Pilihan apakah user ingin melakukan login kembali
    login_ulang = input("\nApakah anda ingin Keluar atau Kembali ke mode login? (Keluar/Kembali): ").lower()
    if login_ulang == "kembali":
        login()  # Kembali ke menu login
    elif login_ulang == "keluar":
        print("Terimakasih telah menggunakan program ini! ✰")
        exit()  # Keluar dari program
    else:
        print("Pilihan tidak tersedia.")

# Fungsi menu dosen
def dosen():
    while True:
        print("")
        print("=" * 6 + " Halo, Selamat datang! " + "=" * 6)
        print("Berikut adalah menu yang dapat anda jalankan: ")
        print("[1]. Lihat jadwal konsultasi")
        print("[2]. Tambah jadwal konsultasi")
        print("[3]. Update jadwal konsultasi")
        print("[4]. Hapus jadwal konsultasi")
        print("[5]. Kembali ke login")
        
        try:
            opsi = int(input("\nSilakan pilih menu yang anda inginkan: "))
            if opsi == 1:
                lihat_jadwal()
            elif opsi == 2:
                tambah_jadwal()
            elif opsi == 3:
                update_jadwal()
            elif opsi == 4:
                hapus_jadwal()
            elif opsi == 5:
                login_ulang = input("Apakah anda ingin Keluar atau Kembali ke mode login? (Keluar/Kembali): ").lower()
                if login_ulang == "keluar":
                    print("Terimakasih telah menggunakan program ini! ✰")
                    exit()
                elif login_ulang == "kembali":
                    login()
                else:
                    print("Pilihan tidak valid.")
            else:
                print("Pilihan tidak tersedia.")
        except ValueError:
            print("Masukkan angka yang valid.")

# Memanggil fungsi login 
login()