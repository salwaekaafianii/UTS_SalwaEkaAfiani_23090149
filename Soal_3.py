def hitung_total_harga(harga_barang):
    total = sum(harga_barang)
    return total

jumlah_barang = int(input('Masukkan Jumlah Barang: '))

harga_barang = []
for i in range(jumlah_barang):
    if i < 2:  
        harga = float(input(f'Masukkan harga barang ke-{i+1}: '))
        harga_barang.append(harga)

harga_barang.append(10000)

total_harga = hitung_total_harga(harga_barang)

print('Total belanjaan : Rp ', total_harga)

