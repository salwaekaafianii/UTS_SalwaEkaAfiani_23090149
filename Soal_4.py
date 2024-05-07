def hitung_bmi(berat_badan, tinggi_badan):
    bmi = berat_badan / (tinggi_badan ** 2)
    return bmi

def rekomendasi_bmi(bmi):
    if bmi < 18.5:
        return 'Berat badan kurang'
    elif 18.5 <= bmi < 24.9:
        return 'Berat badan normal'
    elif 25 <= bmi < 29.9:
        return 'Kelebihan berat badan'
    else:
        return 'Obesitas'

def main():
    print('Program Kalkulator BMI')
    berat_badan = float(input('Masukkan berat badan (kg): '))
    tinggi_badan = float(input('Masukkan tinggi badan (m): '))

    bmi = hitung_bmi(berat_badan, tinggi_badan)
    rekomendasi = rekomendasi_bmi(bmi)

    print('\nHasil Perhitungan BMI:')
    print('Nilai BMI Anda:', round(bmi, 2))
    print('Kategori BMI:', rekomendasi)

if __name__ == "__main__":
    main()
