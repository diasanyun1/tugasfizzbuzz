#input nya
X = int(input("Masukan Total Hari :"))

#proses nya
Tahun = X // 365
SisaHari = X % 365

Bulan = SisaHari // 30
Hari = SisaHari % 30

#output nya
print("Hasil Konversi", X, "Hari Adalah,", Tahun, "Tahun,", Bulan, "Bulan,", Hari, "Hari," )