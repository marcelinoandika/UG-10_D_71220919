albert = int(input("Masukkan tahun: "))
if albert % 400 == 0:
    print("{} merupakan tahun kabisat".format(albert))
elif albert % 100 == 0:
    print("{} bukan tahun kabisat".format(albert))
elif albert % 4 == 0:
    print("{} merupakan tahun kabisat".format(albert))
else:
    print("{} bukan tahun kabisat".format(albert))
