import datetime
from collections import deque
from fungsi_manajemen.fungsi_util import *

queue_transaksi = deque()   # MENDEFINISI NILAI DARI FUNCTION deque() UNTUK

def transaksi(tipe):
    global queue_transaksi

    try:
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

                # VALIDASI KESESUAIAN INPUT DENGAN KATEGORI ID CSV
                if p['id'] == id_produk:

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
                    transaksi.append({'id_transaksi': id_trans, 'id_produk': id_produk,
                                    'jumlah': jumlah, 'total': total,
                                    'tanggal': waktu, 'tipe': tipe})

                    queue_transaksi.append(transaksi[-1])   # MENAMBAH DATA SEMENTARA KE ANTRIAN PERTAMA

                    # MENYIMPAN / MEMINDAHKAN DATA SEMENTARA KE CSV LEWAT FUNCTION
                    simpan_produk(produk) 
                    simpan_transaksi(transaksi)

                    print(f"Transaksi {tipe} berhasil!")
                    return
            print("Produk tidak ditemukan.")
    except ValueError:
            print('Input tidak valid. Coba lagi!')
