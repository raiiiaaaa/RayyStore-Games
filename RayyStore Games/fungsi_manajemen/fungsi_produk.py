from fungsi_manajemen.fungsi_util import *

''' MENAMPILKAN SEMUA PRODUK CSV '''
def tampilkan_produk():
    produk = load_produk() # MENDEFINISI NILAI CSV DARI HASIL LOAD FUNCTION
    print("\n========== Daftar Produk Game ==========")

    # MENAMPILKAN ISI DATA CSV SECARA PERULANGAN BERUNTUNAN
    for p in produk:
        print(f"ID: {p['id']} | Nama: {p['nama']} | Stok: {p['stok']} | Harga: {p['harga']} | Deskripsi: {p['deskripsi']}")
    print('==========================================')



''' MENAMBAH PRODUK CSV SESUAI INPUT '''
def tambah_produk():
    while True:
        produk = load_produk() # MENDEFINISI NILAI CSV DARI HASIL LOAD FUNCTION

        # MENGINPUT KATEGORI PRODUK TAMBAHAN
        id_produk = input("ID Produk: ")
        nama = input("Nama Produk: ")

        # VALIDASI PENCEGAHAN INPUT ID & NAMA GAME YANG SAMA
        for p in produk:
            if p['id'] == id_produk.upper() and p['nama'] == nama.upper():
                print('Produk dengan ID dan Nama yang sama sudah ada. Tidak bisa ditambahkan!')
                return  # KEMBALI KE MENU

        stok = input("Stok Awal: ")
        harga = input("Harga: ")
        deskripsi = input("Deskripsi: ")

        # VALIDASI INPUT AGAR TIDAK TERJADI INPUT YANG KOSONG
        if not id_produk.strip() or not nama.strip() or not stok.strip() or not harga.strip() or not deskripsi.strip():
            print('Inputan tidak boleh kosong!')
            return
        else:
            break # KELUAR PERULANGAN PROSES TAMBAH PRODUK GAME

    # MENAMBAH HASIL INPUTAN KATEGORI SEMENTARA
    produk.append({'id': id_produk.upper(), 'nama': nama.upper(), 'stok': stok, 'harga': harga, 'deskripsi': deskripsi.upper()})
    
    simpan_produk(produk)   # MENYIMPAN HASIL INPUTAN KATEGORI CSV LEWAT FUNCTION
    print("Produk berhasil ditambahkan!")



''' UPDATE PRODUK CSV SESUAI INPUT '''
def update_produk():
    produk = load_produk() # MENDEFINISI NILAI CSV DARI HASIL LOAD FUNCTION

    id_cari = input("Masukkan ID Produk: ")
    
    # PERULANGAN BERUNTUN UNTUK VALIDASI URUTAN DATA PADA FILE CSV
    for p in produk:

        # VALIDASI INPUT AGAR TIDAK TERJADI INPUT YANG KOSONG
        if not id_cari.strip():
            print('Inputan tidak boleh kosong!')
            return  # KEMBALI KE MENU

        # VALIDASI INPUTAN DENGAN DATA YANG SESUAI
        if p['id'] == id_cari.upper():  
            id_baru = input('Masukkan ID baru: ')
            nama_baru = input('Masukkan Game baru: ')
            harga_baru = input('Masukkan Harga baru: ')
            deskripsi_baru = input('Masukkan Deskripsi baru: ')
            
            # MEMPERBARUI ITEM DATABASE DENGAN INPUTAN
            p['id'] = id_baru.upper()
            p['nama'] = nama_baru.upper()
            p['harga'] = harga_baru.upper()
            p['deskripsi'] = deskripsi_baru.upper()

            simpan_produk(produk) # MENYIMPAN HASIL INPUTAN KATEGORI CSV LEWAT FUNCTION
            print('Produk Game berhasil diperbarui!')
            return  # KEMBALI KE MENU PROGRAM
    print("Produk Game tidak ditemukan.")



''' MENGHAPUS PRODUK CSV SESUAI INPUT '''
def hapus_produk():
    produk = load_produk() # MENDEFINISI NILAI CSV DARI HASIL LOAD FUNCTION
    id_hapus = input("ID Produk yang akan dihapus: ")

    # VALIDASI INPUT AGAR TIDAK TERJADI INPUT YANG KOSONG
    if not id_hapus.strip():
        print('Inputan tidak boleh kosong!')
        return  # KEMBALI KE MENU

    produk_baru = [p for p in produk if p['id'] != id_hapus.upper()] # PERULANGAN AGAR TIDAK TERJADI KESALAHAN HAPUS PRODUK GAME
    simpan_produk(produk_baru) # MENYIMPAN HASIL INPUTAN KATEGORI CSV LEWAT FUNCTION
    
    print("Produk Game dihapus!")



''' MENCARI PRODUK CSV SESUAI INPUT '''
def cari_produk():
    produk = load_produk() # MENDEFINISI NILAI CSV DARI HASIL LOAD FUNCTION

    cari_produk = input('Masukkan game yang ingin dicari: ')

    # PERULANGAN BERUNTUN UNTUK VALIDASI URUTAN DATA PADA FILE CSV
    for p in produk:

        # VALIDASI INPUT AGAR TIDAK TERJADI INPUT YANG KOSONG
        if not cari_produk.strip():
            print('Inputan tidak boleh kosong!')
            return  # KEMBALI KE MENU

        # VALIDASI INPUTAN DENGAN DATA YANG DICARI
        if cari_produk.upper() == p['id']:    
            print('Produk Game ditemukan!')
            print('\nDetail Produk Game')
            print(f'Nama Game: {p['nama']}\nID Game: {p['id']}\nStok: {p['stok']}\nDeskripsi: {p['deskripsi']}')
            return
    print('Produk Game tidak ditemukan!')
