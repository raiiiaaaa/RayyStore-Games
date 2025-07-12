from libs.welcome import welcome_message
from fungsi_manajemen.fungsi_produk import *
from fungsi_manajemen.fungsi_transaksi import transaksi
from laporan import laporan_transaksi

''' MAIN PROGRAM '''
def menu():
    while True:  # REKURSI PERULANGAN WHILE
        welcome_message() # MENAMPILKAN OUTPUT SAMBUTAN
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
            transaksi()
        elif pilih == '7':
            laporan_transaksi()
        elif pilih == '0':
            print("Terima kasih!")
            break   # PROGRAM BERHENTI
        else:
            print("Pilihan tidak valid.")   # MENU PROGRAM BERULANG DARI AWAL

if __name__ == '__main__':
    menu()
