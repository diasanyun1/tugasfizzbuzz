#input nya
TotalDetik = int (input("masukan total detik :"))

#proses nya
hari = TotalDetik // 86400
sisahari = TotalDetik % 86400

jam = sisahari // 3600
sisajam = sisahari % 3600

menit = sisajam // 60
detik = sisahari % 60 

#output nya
print ("Hasil Konversi", TotalDetik, "Detik Adalah,", hari, "hari,", jam,"jam,", menit, "menit,", detik, "detik")