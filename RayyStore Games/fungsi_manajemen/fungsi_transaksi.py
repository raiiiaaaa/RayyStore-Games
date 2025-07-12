import datetime
from collections import deque
from fungsi_manajemen.fungsi_util import *

queue_transaksi = deque()   # MENDEFINISI NILAI DARI FUNCTION deque() UNTUK

""" PROSES TRANSAKSI """
def transaksi():
    global queue_transaksi  # MENGGLOBALKAN VARIABEL DARI LUAR FUNCTION

    while True:
        print(f"\n========== Transaksi ===============")
        print('List Transaksi')
        print('1. Transaksi Penjualan')
        print('2. Transaksi Pembelian')
        print('========================================')

        pilih = input('Pilih Menu: ')

        # VALIDASI INPUTAN MENU
        if pilih == '1':
            tipe = 'penjualan'
            break
        elif pilih == '2':
            tipe = 'pembelian'
            break
        else:
            print('Input tidak valid. Coba lagi!')

    # SYNTAX INI BERFUNGSI MENGHINDARI KESALAHAN INPUT
    try: 

        # PERULANGAN PROGRAM TRANSAKSI
        while True:
            produk = load_produk()  # MENDEFINISI NILAI CSV DARI HASIL LOAD FUNCTION
            transaksi = load_transaksi() # MENDEFINISI NILAI CSV DARI HASIL LOAD FUNCTION
            id_produk = input("Masukkan ID Produk: ")
            jumlah = int(input("Jumlah: "))

            # VALIDASI JIKA INPUT JUMLAH KURANG DARI 0
            if jumlah <= 0:
                print("Jumlah tidak valid!")
                return
            
            # PERULANGAN BERUNTUN UNTUK VALIDASI TRANSAKSI
            for p in produk:

                # VALIDASI UNTUK MENAMBAHKAN NAMA GAME KE LAPORAN TRANSAKSI
                if p['id'] != p['nama']:
                    nama_game = p['nama']

                # VALIDASI KESESUAIAN INPUT DENGAN KATEGORI ID CSV
                if p['id'] == id_produk.upper():

                    # VALIDASI JIKA JUMLAH MELEBIHI STOK GAME
                    if tipe == 'penjualan' and int(p['stok']) < jumlah:
                        print("Stok tidak mencukupi!")
                        return
                    
                    # PROSES TRANSAKSI
                    if tipe == 'penjualan':
                        p['stok'] = str(int(p['stok']) - jumlah)
                    elif tipe == 'pembelian':
                        p['stok'] = str(int(p['stok']) + jumlah)
                        
                    total = int(p['harga']) * jumlah
                    waktu = datetime.datetime.now().strftime('%Y-%m-%d')
                    id_trans = f"T{len(transaksi) + 1:04d}"

                    # DATA PENYIMPANAN SEMENTARA UNTUK DIKIRIM KE CSV
                    transaksi.append({'tanggal':waktu, 'id_transaksi': id_trans.upper(), 'id_produk': id_produk.upper(),
                                    'jumlah':jumlah, 'game': nama_game.upper(),
                                    'total': total, 'tipe': tipe.upper()})

                    # MENAMBAH DATA SEMENTARA KE ANTRIAN PERTAMA
                    queue_transaksi.append(transaksi[-1])

                    # MENYIMPAN / MEMINDAHKAN DATA SEMENTARA KE CSV LEWAT FUNCTION
                    simpan_produk(produk) 
                    simpan_transaksi(transaksi)

                    print(f"Transaksi {tipe} berhasil!")
                    return
            print("Produk tidak ditemukan.")
    except ValueError:      # SYNTAX INI BERFUNGSI MENGHINDARI KESALAHAN INPUT
            print('Input tidak valid. Coba lagi!')
