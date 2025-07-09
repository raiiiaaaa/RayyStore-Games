import csv
produk_file = 'produk.csv'
transaksi_file = 'transaksi.csv'

# __all__ = ['load_produk', 'simpan_produk', 'load_transaksi', 'simpan_transaksi']

def load_produk():
    try:
        with open(produk_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def simpan_produk(data):
    with open(produk_file, mode='w', newline='') as file:
        fieldnames = ['id', 'nama', 'stok', 'harga', 'deskripsi']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def load_transaksi():
    try:
        with open(transaksi_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def simpan_transaksi(data):
    with open(transaksi_file, mode='w', newline='') as file:
        fieldnames = ['id_transaksi', 'id_produk', 'jumlah', 'total', 'tanggal', 'tipe']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
