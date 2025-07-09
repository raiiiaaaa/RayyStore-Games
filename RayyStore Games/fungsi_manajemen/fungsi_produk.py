from fungsi_manajemen.fungsi_util import *

def tampilkan_produk():
    produk = load_produk()
    print("\n========== Daftar Produk ==========")
    for p in produk:
        print(f"ID: {p['id']} | Nama: {p['nama']} | Stok: {p['stok']} | Harga: {p['harga']} | Deskripsi: {p['deskripsi']}")
    print('==============================')

def tambah_produk():
    produk = load_produk()
    id_produk = input("ID Produk: ")
    nama = input("Nama Produk: ")
    stok = input("Stok Awal: ")
    harga = input("Harga: ")
    deskripsi = input("Deskripsi: ")
    produk.append({'id': id_produk, 'nama': nama, 'stok': stok, 'harga': harga, 'deskripsi': deskripsi})
    simpan_produk(produk)
    print("Produk berhasil ditambahkan!")

def update_produk():
    produk = load_produk()
    id_cari = input("Masukkan ID Produk: ")
    for p in produk:
        if p['id'] == id_cari:
            print('Masukkan id baru!')
            p['id'] = input('Id baru: ')
            print('Id berhasil diperbarui!\n')

            print('Masukkan nama game baru!')
            p['nama'] = input('Game baru: ')
            print('Nama game berhasil diperbarui!\n')

            print('Masukkan stok baru!')
            p['stok'] = input("Stok baru: ")
            simpan_produk(produk)
            print("Stok berhasil diperbarui!\n")

            print('Masukkan harga baru!')
            p['harga'] = input('Harga baru: ')
            print('Harga berhasil diperbarui!\n')

            print('Masukkan deskripsi terbaru!')
            p['deskripsi'] = input('Deskripsi baru: ')
            print('Deskripsi berhasil diperbarui!')
            return
    print("Produk tidak ditemukan.")

# def update_harga():
#     produk = load_produk()
#     id_cari = input("Masukkan ID Produk: ")
#     for p in produk:
#         if p['id'] == id_cari:
#             p['harga'] = input("Harga baru: ")
#             simpan_produk(produk)
#             print("Harga berhasil diperbarui!")
#             return
#     print("Produk tidak ditemukan.")

def hapus_produk():
    produk = load_produk()
    id_hapus = input("ID Produk yang akan dihapus: ")
    produk_baru = [p for p in produk if p['id'] != id_hapus]
    simpan_produk(produk_baru)
    print("Produk dihapus!")
