import csv
produk_file = 'produk.csv'
transaksi_file = 'transaksi.csv'

''' LOAD SYSTEM '''
def load_produk():
    try:
        with open(produk_file, mode='r', newline='') as file:   # MEMBUKA FILE PRODUK.CSV LALU MEMBERI INISIAL 'file'
            reader = csv.DictReader(file)   # MENDEFINISI NILAI READER DARI DATA FILE PRODUK.CSV
            return list(reader)     # MENGEMBALIKAN NILAI LIST BERUPA ISIAN DARI FILE PRODUK.CSV
    except FileNotFoundError:   # SYNTAX UNTUK MENGATASI JIKA DATA DALAM FILE PRODUK.CSV TIDAK DITEMUKAN
        return []   # MENGEMBALIKAN NILAI BERUPA LIST KOSONG
    
def load_transaksi():
    try:
        with open(transaksi_file, mode='r', newline='') as file: # MEMBUKA FILE TRANSAKSI.CSV LALU MEMBERI INISIAL 'file'
            reader = csv.DictReader(file) # MENDEFINISI NILAI READER DARI DATA FILE TRANSAKSI.CSV
            return list(reader) # MENGEMBALIKAN NILAI LIST BERUPA ISIAN DARI FILE TRANSAKSI.CSV
    except FileNotFoundError: # SYNTAX UNTUK MENGATASI JIKA DATA DALAM FILE TRANSAKSI.CSV TIDAK DITEMUKAN
        return [] # MENGEMBALIKAN NILAI BERUPA LIST KOSONG



''' SAVE SYSTEM '''
def simpan_produk(data):
    with open(produk_file, mode='w', newline='') as file: # MEMBUKA FILE PRODUK.CSV LALU MEMBERI INISIAL 'file'
        fieldnames = ['id', 'nama', 'stok', 'harga', 'deskripsi']   # MENDEFINISI KATEGORI YG DITAMBAHKAN PADA FILE CSV
        writer = csv.DictWriter(file, fieldnames=fieldnames)    # MEMBUAT OBJEK WRITER UNTUK MENULIS PADA FILE PRODUK.CSV
        writer.writeheader() # MENULIS BARIS PERTAMA HEADER PADA PRODUK.CSV
        
        # PERULANGAN UNTUK MELAKUKAN ITERASI SETIAP ITEM SEBAGAI BARIS BARU 
        for row in data:
            writer.writerow(row) # MENULIS TERASI SEBAGAI SATU BARIS DATA


def simpan_transaksi(data):
    with open(transaksi_file, mode='w', newline='') as file: # MEMBUKA FILE TRANSAKSI.CSV LALU MEMBERI INISIAL 'file'
        fieldnames = ['tanggal','id_transaksi', 'id_produk', 'jumlah', 'game', 'total', 'tipe'] # MENDEFINISI KATEGORI YG DITAMBAHKAN PADA FILE CSV
        writer = csv.DictWriter(file, fieldnames=fieldnames)    # MEMBUAT OBJEK WRITER UNTUK MENULIS PADA FILE TRANSAKSI.CSV
        writer.writeheader()    # MENULIS BARIS PERTAMA HEADER PADA PRODUK.CSV
        
        # PERULANGAN UNTUK MELAKUKAN ITERASI SETIAP ITEM SEBAGAI BARIS BARU 
        for row in data:
            writer.writerow(row) # MENULIS TERASI SEBAGAI SATU BARIS DATA
