def tambah_data(nama, tugas, uts, uas, data_mahasiswa):
    nilai_akhir = 0.3 * tugas + 0.35 * uts + 0.35 * uas
    data_mahasiswa[nama] = {'Tugas': tugas, 'UTS': uts, 'UAS': uas, 'Nilai Akhir': nilai_akhir}
    print("Data mahasiswa berhasil ditambahkan!")

def ubah_data(nama, tugas, uts, uas, data_mahasiswa):
    if nama in data_mahasiswa:
        nilai_akhir = 0.3 * tugas + 0.35 * uts + 0.35 * uas
        data_mahasiswa[nama] = {'Tugas': tugas, 'UTS': uts, 'UAS': uas, 'Nilai Akhir': nilai_akhir}
        print("Data mahasiswa berhasil diubah!")
    else:
        print("Data mahasiswa tidak ditemukan!")

def hapus_data(nama, data_mahasiswa):
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print("Data mahasiswa berhasil dihapus!")
    else:
        print("Data mahasiswa tidak ditemukan!")

def tampilkan_data(data_mahasiswa):
    print("\nDaftar Nilai Mahasiswa:")
    print("{:<15} {:<10} {:<10} {:<10} {:<15}".format("Nama", "Tugas", "UTS", "UAS", "Nilai Akhir"))
    for nama, nilai in data_mahasiswa.items():
        print("{:<15} {:<10} {:<10} {:<10} {:<15}".format(nama, nilai['Tugas'], nilai['UTS'], nilai['UAS'], nilai['Nilai Akhir']))

def cari_data(nama, data_mahasiswa):
    if nama in data_mahasiswa:
        nilai = data_mahasiswa[nama]
        print("\nData Mahasiswa:")
        print("{:<15} {:<10} {:<10} {:<10} {:<15}".format("Nama", "Tugas", "UTS", "UAS", "Nilai Akhir"))
        print("{:<15} {:<10} {:<10} {:<10} {:<15}".format(nama, nilai['Tugas'], nilai['UTS'], nilai['UAS'], nilai['Nilai Akhir']))
    else:
        print("Data mahasiswa tidak ditemukan!")

# Dictionary untuk menyimpan data mahasiswa
data_mahasiswa = {}

while True:
    print("\n=== Menu Pilihan ===")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("6. Keluar")

    pilihan = input("Masukkan pilihan (1-6): ")

    if pilihan == '1':
        nama = input("Masukkan Nama Mahasiswa: ")
        tugas = float(input("Masukkan Nilai Tugas: "))
        uts = float(input("Masukkan Nilai UTS: "))
        uas = float(input("Masukkan Nilai UAS: "))
        tambah_data(nama, tugas, uts, uas, data_mahasiswa)

    elif pilihan == '2':
        nama = input("Masukkan Nama Mahasiswa yang Ingin Diubah: ")
        tugas = float(input("Masukkan Nilai Tugas Baru: "))
        uts = float(input("Masukkan Nilai UTS Baru: "))
        uas = float(input("Masukkan Nilai UAS Baru: "))
        ubah_data(nama, tugas, uts, uas, data_mahasiswa)

    elif pilihan == '3':
        nama = input("Masukkan Nama Mahasiswa yang Ingin Dihapus: ")
        hapus_data(nama, data_mahasiswa)

    elif pilihan == '4':
        tampilkan_data(data_mahasiswa)

    elif pilihan == '5':
        nama = input("Masukkan Nama Mahasiswa yang Ingin Dicari: ")
        cari_data(nama, data_mahasiswa)

    elif pilihan == '6':
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan masukkan angka 1-6.")
