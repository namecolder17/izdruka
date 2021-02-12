#if, else, elif
"""
if nosacījums:
    izpildāmās darbības
elif cits nosacījums:
    izpildāmās darbības
else:
    izpildāmās darbības visos citos gadījumos
"""
#ja skaitlis ir lielāks par 5, izdrukā, ka lielāks par 5, citādi, ja skaitlis lielāks par 0, izdrukā, ka lielāks par 0. Citādi izdrukā, ka tas nav pozitīvs skaitlis
a = 6
if a > 5:
    print("skaitlis ir lielāks par 5")
elif a > 0:
    print("skaitlis ir lielāks par 0")
else:
    print("skaitlis nav pozitīvs")

x = input("Ievadi pirmo skaitļu: ")
y = input("Ievadi otro skaitļu: ")
z = input("Ievadi trešo skaitļu: ")
saraksts = [x, y, z]
saraksts.sort()
print(saraksts)

suns_grib_est = True
if suns_grib_est:
    print("Pabaro suni")
else:
    print("Suns ir paedis")