import datetime
from fungsi_manajemen.fungsi_util import load_transaksi

''' LAPORAN TRANSAKSI '''
def laporan(tipe):
    transaksi = load_transaksi() # MENDEFINISI NILAI CSV DARI HASIL LOAD FUNCTION
    print(f"\n========== Laporan {tipe.capitalize()} ========")
    hari_ini = datetime.datetime.now() # MENDEFINISI WAKTU HARI INI

    # PERULANGAN BERUNTUN UNTUK PROSES LAPORAN
    for t in transaksi:
        tgl = datetime.datetime.strptime(t['tanggal'], '%Y-%m-%d')
        selisih = (hari_ini - tgl).days
        if tipe == 'harian' and selisih <= 1:
            print(t)
        elif tipe == 'mingguan' and selisih <= 7:
            print(t)
        elif tipe == 'bulanan' and selisih <= 30:
            print(t)
