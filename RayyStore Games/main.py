from libs.welcome import welcome_message
from fungsi_manajemen.fungsi_produk import *
from fungsi_manajemen.fungsi_transaksi import transaksi
from laporan import laporan

''' MAIN PROGRAM '''
def menu():
    while True:  # REKURSI PERULANGAN WHILE
        welcome_message()
        pilih = input("Pilih menu: ")

        # VALIDASI INPUT PILIHAN MENU
        if pilih == '1':
            tampilkan_produk()
        elif pilih == '2':
            tambah_produk()
        elif pilih == '3':
            update_produk()
        elif pilih == '4':
            hapus_produk()
        elif pilih == '5':
            cari_produk()
        elif pilih == '6':
            transaksi('penjualan')
        elif pilih == '7':
            transaksi('pembelian')
        elif pilih == '8':
            laporan('harian')
        elif pilih == '9':
            laporan('mingguan')
        elif pilih == '10':
            laporan('bulanan')
        elif pilih == '0':
            print("Terima kasih!")
            break   # JIKA INPUT EXIT, PERULANGAN BERHENTI
        else:
            print("Pilihan tidak valid.")   # JIKA INPUT TIDAK VALID, MENU PROGRAM BERULANG DARI AWAL

if __name__ == '__main__':
    menu()
