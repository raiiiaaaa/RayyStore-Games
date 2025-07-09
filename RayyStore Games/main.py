from libs.welcome import welcome_message
from fungsi_manajemen.fungsi_produk import *
from fungsi_manajemen.fungsi_transaksi import transaksi
from laporan import laporan
from collections import deque

# ==== GLOBAL VARIABLES ====
# produk_file = 'produk.csv'
# transaksi_file = 'transaksi.csv'
# queue_transaksi = deque()

# ==== MENU UTAMA ====

''' MAIN PROGRAM '''
def menu():
    while True:  # rekursi perulangan while
        welcome_message()
        pilih = input("Pilih menu: ")

        # validasi input pilihan menu
        if pilih == '1':
            tampilkan_produk()
        elif pilih == '2':
            tambah_produk()
        elif pilih == '3':
            update_produk()
        elif pilih == '4':
            hapus_produk()
        elif pilih == '5':
            transaksi('penjualan')
        elif pilih == '6':
            transaksi('pembelian')
        elif pilih == '7':
            laporan('harian')
        elif pilih == '8':
            laporan('mingguan')
        elif pilih == '9':
            laporan('bulanan')
        elif pilih == '0':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == '__main__':
    menu()
