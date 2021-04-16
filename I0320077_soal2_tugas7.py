# Soal 2
# Fungsi abs
bil1 = float(input("Masukan bilangan negatif = "))
while bil1 >= 0:
    bil1 = float(input("Masukan lagi bilangan negatif = "))
print("|bil1| = ", abs(bil1))
print("-"*40)

# Fungsi ceil
import math
bil2 = float(input("Masukan bilangan riil = "))
print("Hasil pembulatan ke atas bil2 = ", math.ceil(bil2))

# Fungsi floor
print("Hasil pembulatan ke bawah bil2 = ", math.floor(bil2))
print("-"*40)

# Fungsi min dan max
bil3 = int(input("Masukan bilangan 1 = "))
bil4 = int(input("Masukan bilangan 2 = "))
bil5 = int(input("Masukan bilangan 3 = "))
print("Nilai max dari ketiga bilangan tersebut = ", max(bil3, bil4, bil5))
print("-"*40)

# Funsgi choice
import random
angka = [5, 10, 2001, 9, 16, 8]
print("Angka yang dipilih acak adalah = ", random.choice(angka))
