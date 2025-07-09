from fungsi_manajemen.fungsi_util import *

''' MENAMPILKAN SEMUA PRODUK CSV '''
def tampilkan_produk():
    produk = load_produk() # MENDEFINISI NILAI PRODUK DARI HASIL LOAD FUNCTION
    print("\n========== Daftar Produk ==========")
    # MENAMPILKAN ISI DATA SECARA PERULANGAN BERUNTUNAN

    for p in produk:
        print(f"ID: {p['id']} | Nama: {p['nama']} | Stok: {p['stok']} | Harga: {p['harga']} | Deskripsi: {p['deskripsi']}")
    print('==============================')

''' MENAMBAH PRODUK CSV SESUAI INPUT '''
def tambah_produk():
    while True:
        produk = load_produk() # MENDEFINISI NILAI PRODUK DARI HASIL LOAD FUNCTION

        # MENGINPUT KATEGORI PRODUK TAMBAHAN
        id_produk = input("ID Produk: ")
        nama = input("Nama Produk: ")
        stok = input("Stok Awal: ")
        harga = input("Harga: ")
        deskripsi = input("Deskripsi: ")
        if id_produk == ' ' or nama == ' ' or stok == ' ' or harga == ' ' or deskripsi == ' ':
            print('Inputan tidak boleh kosong!')
        else:
            break

        # MENAMBAH HASIL INPUTAN KATEGORI 
    produk.append({'id': id_produk, 'nama': nama, 'stok': stok, 'harga': harga, 'deskripsi': deskripsi})
    simpan_produk(produk)   # MENYIMPAN HASIL INPUTAN KATEGORI LEWAT FUNCTION
    print("Produk berhasil ditambahkan!")

''' UPDATE PRODUK CSV SESUAI INPUT '''
def update_produk():
    produk = load_produk() # MENDEFINISI NILAI PRODUK DARI HASIL LOAD FUNCTION

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

''' MENGHAPUS PRODUK CSV SESUAI INPUT '''
def hapus_produk():
    produk = load_produk()
    id_hapus = input("ID Produk yang akan dihapus: ")
    produk_baru = [p for p in produk if p['id'] != id_hapus]
    simpan_produk(produk_baru)
    print("Produk dihapus!")
