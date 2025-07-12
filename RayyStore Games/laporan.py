import datetime
from fungsi_manajemen.fungsi_util import load_transaksi

''' LAPORAN TRANSAKSI '''
def laporan_transaksi():
    transaksi = load_transaksi() # MENDEFINISI NILAI CSV DARI HASIL LOAD FUNCTION

    # PERULANGAN PROGRAM LAPORAN
    while True:
        print(f"\n========== Laporan Transaksi ========")
        hari_ini = datetime.datetime.now() # MENDEFINISI DATA WAKTU HARI INI

        print('List Laporan Transaksi')
        print('1. Transaksi Harian')
        print('2. Transaksi Mingguan')
        print('3. Transaksi Bulanan')
        print('========================================')

        pilih = input('Pilih Transaksi: ')

        # VALIDASI INPUTAN MENU
        if pilih == '1':
            tipe = 'harian'
            break           
        elif pilih == '2':
            tipe = 'mingguan'
            break
        elif pilih == '3':
            tipe = 'bulanan'
            break
        else:
            print('Input tidak valid. Coba lagi!')
    print(f'\nLAPORAN TRANSAKSI {tipe.upper()}')

    # PERULANGAN BERUNTUN UNTUK PROSES LAPORAN
    for t in transaksi:

        # MENDEFINISI TANGGAL DENGAN DATA WAKTU SAAT INI (TAHUN, BULAN, HARI)
        tgl = datetime.datetime.strptime(t['tanggal'], '%Y-%m-%d')
        selisih = (hari_ini - tgl).days # MENDEFINISI SELISIH HARI
        
        # VALIDASI TIPE TRANSAKSI DENGAN PERBANDINGAN SELISIH HARI
        if tipe == 'harian' and selisih <= 1:
            print(
                f'Tanggal: {t['tanggal']} | '
                f'ID Transaksi: {t['id_transaksi']} | '
                f'ID Produk: {t['id_produk']} | '
                f'Jumlah {tipe.capitalize()}: {t['jumlah']} | '
                f'Game:{t['game']} |'
                f'Total: {t['total']} | '
                f'Tipe: {t['tipe']}'
            )

        elif tipe == 'mingguan' and selisih <= 7:
            print(
                f'Tanggal: {t['tanggal']} | '
                f'ID Transaksi: {t['id_transaksi']} | '
                f'ID Produk: {t['id_produk']} | '
                f'Jumlah {tipe.capitalize()}: {t['jumlah']} | '
                f'Game:{t['game']} |'
                f'Total: {t['total']} | '
                f'Tipe: {t['tipe']}'
            )

        elif tipe == 'bulanan' and selisih <= 30:
            print(
                f'Tanggal: {t['tanggal']} | '
                f'ID Transaksi: {t['id_transaksi']} | '
                f'ID Produk: {t['id_produk']} | '
                f'Jumlah {tipe.capitalize()}: {t['jumlah']} | '
                f'Game:{t['game']} |'
                f'Total: {t['total']} | '
                f'Tipe: {t['tipe']}'
            )
