sayang = int(input("Masukkan tahun: "))
if sayang % 400 == 0:
    print("{} merupakan tahun kabisat".format(sayang))
elif sayang % 100 == 0:
    print("{} bukan tahun kabisat".format(sayang))
elif sayang % 4 == 0:
    print("{} merupakan tahun kabisat".format(sayang))
else:
    print("{} bukan tahun kabisat".format(sayang))
