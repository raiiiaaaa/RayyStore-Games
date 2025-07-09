import datetime
from collections import deque
from fungsi_manajemen.fungsi_util import *

queue_transaksi = deque()

def transaksi(tipe):
    global queue_transaksi

    produk = load_produk()
    transaksi = load_transaksi()
    id_produk = input("Masukkan ID Produk: ")
    jumlah = int(input("Jumlah: "))
    for p in produk:
        if p['id'] == id_produk:
            if tipe == 'penjualan' and int(p['stok']) < jumlah:
                print("Stok tidak mencukupi!")
                return
            # Update stok
            if tipe == 'penjualan':
                p['stok'] = str(int(p['stok']) - jumlah)
            elif tipe == 'pembelian':
                p['stok'] = str(int(p['stok']) + jumlah)

            total = int(p['harga']) * jumlah
            waktu = datetime.datetime.now().strftime('%Y-%m-%d')
            id_trans = f"T{len(transaksi) + 1:04d}"

            transaksi.append({'id_transaksi': id_trans, 'id_produk': id_produk,
                              'jumlah': jumlah, 'total': total,
                              'tanggal': waktu, 'tipe': tipe})

            queue_transaksi.append(transaksi[-1])
            simpan_produk(produk)
            simpan_transaksi(transaksi)
            print(f"Transaksi {tipe} berhasil!")
            return
    print("Produk tidak ditemukan.")
