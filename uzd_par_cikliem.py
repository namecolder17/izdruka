"""#uzd1
x = int(input("Ievādi intervāla sākumpunktu: "))
y = int(input("Ievādi intervāla galapunktu: "))
for skaitlis in range(x, y+1):
    print(skaitlis, end=" ")

#uzd2
a = int(input("Ievādi veselu skaitli: "))
faktorials = 1
for i in range(1, a+1):
    faktorials = faktorials*i
print(f"Skaitļa {a} faktoriāls ir {faktorials}.")

#uzd3
x = int(input("Ievādi intervāla sākumpunktu: "))
y = int(input("Ievādi intervāla galapunktu: "))
z = int(input("Ievādi dalītāju: "))
for sk in range(x, y+1):
    if sk % z ==0:
        print(sk)"""

"""#uzd4
x1 = float(input("Ievādi pirmo skaitli: "))
x2 = float(input("Ievādi otro skaitli: "))
x3 = float(input("Ievādi trešo skaitli: "))
x4 = float(input("Ievādi ceturto skaitli: "))
x5 = float(input("Ievādi piekto skaitli: "))
x6 = float(input("Ievādi sesto skaitli: "))
x7 = float(input("Ievādi septito skaitli: "))
x8 = float(input("Ievādi astoto skaitli: "))
x9 = float(input("Ievādi devito skaitli: "))
x10 = float(input("Ievādi desmito skaitli: "))
myList = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
myList.sort()
print(myList)
#uzd3
x = int(input("Ievādi veselu skaitli: "))
for sk in range(x, 0-1, -1):
    if sk % 2 ==0:
         print(sk)

#uzd5
sk = 1
x = int(input("Ievādi veseo skaitli: "))
while sk**2 <= x:
    print(sk**2)
    sk+=1

#uzd6
x = 0
while x < 2:
    x = int(input("Ievadi veselu skaitli, kas ir vismaz 2: "))

dalitajs = 2
while True:
    if x % dalitajs == 0:
        print(f"Mazākais skaitlis ar ko {x} dalās bez atlikuma ir {dalitajs}.")
        break
    else:
        dalitajs += 1

#uzd7
sk = 1
a = ""
for sk in range(sk,5):
    a = a + str(sk)
    print(a)"""

n = int(input("Ievadi naturālu skaitli: "))
while True:
    if n < 1:
        n = int(input("Ievadi naturālu skaitli: "))
    else:
        break

faktorials = 1
summa = 0

for i in range(n):
    faktorials = faktorials*(i+1)
    summa = summa + faktorials
    print(faktorials,summa)
print (f"Pirmo {n} skaitļu faktoriālu summa ir {summa}.")

#Lietotājs ievada naturālu skaitli, kas ir lielāks par 1. Ja lietotājs ievada skaitli, kas ir mazāks par 1, prasa ievadīt to vēlreiz. Programma saskaita faktoriālu summu. Piemēram, ja lietotājs ievada 4, tad programma saskaita 1!+2!+3!+4!.
