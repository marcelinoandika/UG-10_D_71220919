print ("ketik 1 untuk menghitung penjumlahan")
print ("ketik 2 untuk menghitung pegurangan")
print ("ketik 3 untuk menghitung perkalian")
print ("ketik 4 untuk menghitung pembagian")
print ("ketik 5 untuk menghitung sisa hasil bagi")
print ("ketik 6 untuk menghitung pemangkatan")
x = int(input("masukan pilihan anda"))
y = int(input("masukan bilangan pertama"))
z = int(input("masukan bilangan kedua"))
if x== '1' :
    jumlah = y+z
    print (f"hasil operasi bilangan {y} + {z}= {} ")
