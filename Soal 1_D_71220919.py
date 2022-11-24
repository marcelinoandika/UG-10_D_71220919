print ("ketik 1 untuk menghitung penjumlahan")
print ("ketik 2 untuk menghitung pegurangan")
print ("ketik 3 untuk menghitung perkalian")
print ("ketik 4 untuk menghitung pembagian")
print ("ketik 5 untuk menghitung sisa hasil bagi")
print ("ketik 6 untuk menghitung pemangkatan")
x = int(input("masukan pilihan anda:"))
y = int(input("masukan bilangan pertama:"))
z = int(input("masukan bilangan kedua:"))
if x== 1 :
    jumlah = y+z
    print ("hasil dari",y,"dijumlahkan dengan",z,"adalah",jumlah)
elif x== 2 :
    jumlah = y-z
    print ("hasil dari",y,"dikurangi dengan",z,"adalah",jumlah)
elif x== 3 :
    jumlah = y*z
    print ("hasil dari",y,"dikali dengan",z,"adalah",jumlah)
elif x== 4 :
    jumlah = y/z
    print ("hasil dari",y,"dibagi dengan",z,"adalah",jumlah)
elif x== 5 :
    jumlah = y%z
    print ("hasil dari",y,"sisa bagi dengan",z,"adalah",jumlah)
elif x== 6 :
    jumlah = y**z
    print ("hasil dari",y,"dipangkatkan dengan",z,"adalah",jumlah)
else :
    print ("ramasokk")
