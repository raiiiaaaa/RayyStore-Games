from fungsi_manajemen.fungsi_util import *

''' MENAMPILKAN SEMUA PRODUK CSV '''
def tampilkan_produk():
    produk = load_produk() # MENDEFINISI NILAI CSV DARI HASIL LOAD FUNCTION
    print("\n========== Daftar Produk ==========")

    # MENAMPILKAN ISI DATA CSV SECARA PERULANGAN BERUNTUNAN
    for p in produk:
        print(f"ID: {p['id']} | Nama: {p['nama']} | Stok: {p['stok']} | Harga: {p['harga']} | Deskripsi: {p['deskripsi']}")
    print('==============================')

''' MENAMBAH PRODUK CSV SESUAI INPUT '''
def tambah_produk():
    while True:
        produk = load_produk() # MENDEFINISI NILAI CSV DARI HASIL LOAD FUNCTION

        # MENGINPUT KATEGORI PRODUK TAMBAHAN
        id_produk = input("ID Produk: ")
        nama = input("Nama Produk: ")
        stok = input("Stok Awal: ")
        harga = input("Harga: ")
        deskripsi = input("Deskripsi: ")

        # VALIDASI INPUT AGAR TIDAK TERJADI KATEGORI YANG KOSONG
        if not id_produk.strip() or not nama.strip() or not stok.strip() or not harga.strip() or not deskripsi.strip():
            print('Inputan tidak boleh kosong!')
        else:
            break # KELUAR PERULANGAN PROSES TAMBAH PRODUK GAME

        # MENAMBAH HASIL INPUTAN KATEGORI SEMENTARA
    produk.append({'id': id_produk, 'nama': nama, 'stok': stok, 'harga': harga, 'deskripsi': deskripsi})
    simpan_produk(produk)   # MENYIMPAN HASIL INPUTAN KATEGORI CSV LEWAT FUNCTION
    print("Produk berhasil ditambahkan!")

''' UPDATE PRODUK CSV SESUAI INPUT '''
def update_produk():
    produk = load_produk() # MENDEFINISI NILAI CSV DARI HASIL LOAD FUNCTION

    id_cari = input("Masukkan ID Produk: ")
    
    # PERULANGAN BERUNTUN UNTUK VALIDASI URUTAN DATA PADA FILE CSV
    for p in produk:
        # VALIDASI INPUTAN DENGAN DATA YANG SESUAI
        if p['id'] == id_cari:  
            print('\nMasukkan id baru!')
            p['id'] = input('Id baru: ')

            print('\nMasukkan nama game baru!')
            p['nama'] = input('Game baru: ')

            print('\nMasukkan stok baru!')
            p['stok'] = input("Stok baru: ")

            print('\nMasukkan harga baru!')
            p['harga'] = input('Harga baru: ')

            print('\nMasukkan deskripsi terbaru!')
            p['deskripsi'] = input('Deskripsi baru: ')
            print('Produk Game berhasil diperbarui!')
            simpan_produk(produk) # MENYIMPAN HASIL INPUTAN KATEGORI CSV LEWAT FUNCTION
            return  # KEMBALI KE MENU PROGRAM
    print("Produk Game tidak ditemukan.")

''' MENGHAPUS PRODUK CSV SESUAI INPUT '''
def hapus_produk():
    produk = load_produk() # MENDEFINISI NILAI CSV DARI HASIL LOAD FUNCTION
    id_hapus = input("ID Produk yang akan dihapus: ")
    produk_baru = [p for p in produk if p['id'] != id_hapus] 
    simpan_produk(produk_baru) # MENYIMPAN HASIL INPUTAN KATEGORI CSV LEWAT FUNCTION
    print("Produk Gane dihapus!")

def cari_produk():
    produk = load_produk() # MENDEFINISI NILAI CSV DARI HASIL LOAD FUNCTION

    cari_produk = input('Masukkan game yang ingin dicari: ')

    # PERULANGAN BERUNTUN UNTUK VALIDASI URUTAN DATA PADA FILE CSV
    for p in produk:
        # VALIDASI INPUTAN DENGAN DATA YANG DICARI
        if cari_produk == p['nama']:    
            print('Produk Game ditemukan!')
            print('Detail Produk Game')
            print(f'Nama Game: {p['nama']}\nID Game: {p['id']}\nStok: {p['stok']}')
