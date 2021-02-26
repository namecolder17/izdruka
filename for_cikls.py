#iterācija - kādas darbības atkārtota izpīldīšana
mainigais = [1, 2, 3]
for elements in mainigais:
    print(elements)  #darbības, kas jāveic

#drukā list elementus
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for skaitlis in mylist:
    print(skaitlis)

for _ in mylist:
    print("Sveiki!")  #var nerakstīt cikla mainīgā nosaukumu

#izdrukā tikai pāra skaitļus
for sk in mylist:
    if sk % 2 == 0:
        print(sk)
    else:
        print(f"{sk} ir nepāra skaitlis")

#summas apreķināšana
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
summa = 0

for sk in mylist:
    summa = summa + sk
    print(f"Pēc {sk} skaitļu saskaitīšanas summa ir {summa}")
print(summa)

#drukā tekstu
mystring = "Sveika, pasaule!"
for burts in mystring:
    print(burts)

for burts in "programma":
    print(burts, end=" ")

#drukā tuple
tup = (1, 2, 3, 4)
for elements in tup:
    print(elements)

mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(len(mylist))

for elements in mylist:  #atpako listu
    print(elements)

for viens, otrs in mylist:  #var nelikt iekavas
    print(viens)
    print(otrs)

mylist = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in mylist:
    print(b)

#vārdnīcas
d = {"k1": 11, "k2": 12, "k3": 13}
for elements in d:
    print(elements) #izdrukā tikai atslēgas

for elements in d.items():
    print(elements) #drukā pārus

for atslega,vertiba in d.items():
    print(vertiba)


#ar skaitļiem izmanto funkciju range()
for skaitlis in range(15): #izdrukā visus skaitļus no 0-15
    print(skaitlis)

for skaitlis in range(5, 15): #izdrukā visus skaitļus no 5-15
    print(skaitlis)

for skaitlis in range(5, 15, 2): #izdrukā visus skaitļus no 5-15 ar soli 2
    print(skaitlis)