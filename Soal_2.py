def tes_tahun_kabisat(tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        kabisat = 'merupakan TAHUN KABISAT'
    else:
        kabisat = 'bukan TAHUN KABISAT'
    return kabisat

tahun = int(input('Masukkan Tahun: '))

print('Tahun', tahun, tes_tahun_kabisat(tahun) + '.')
