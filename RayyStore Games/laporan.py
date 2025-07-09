import datetime
from fungsi_manajemen.fungsi_util import load_transaksi

def laporan(tipe):
    transaksi = load_transaksi()
    print(f"\n=== Laporan {tipe.capitalize()} ===")
    hari_ini = datetime.datetime.now()
    for t in transaksi:
        tgl = datetime.datetime.strptime(t['tanggal'], '%Y-%m-%d')
        selisih = (hari_ini - tgl).days
        if tipe == 'harian' and selisih <= 1:
            print(t)
        elif tipe == 'mingguan' and selisih <= 7:
            print(t)
        elif tipe == 'bulanan' and selisih <= 30:
            print(t)
