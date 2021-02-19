#1. uzdevums
a = 15
b = 2.5
c = 4.78
if b > a > c:
  print("Skaitlis 'b' ir vislielākais, bet skaitlis 'c' - vismazākais, skaitlis 'a' ir lielāks nekā 'c', bet mazāks nekā 'b'")  
elif b > c > a:
    print("Skaitlis 'b' ir vislielākais, bet skaitlis 'a' - vismazākais, skaitlis 'c' ir lielāks nekā 'a', bet mazāks nekā 'b'")

if a > b > c:
    print("Skaitlis 'a' ir vislielākais, bet skaitlis 'c' - vismazākais, skaitlis 'b' ir lielāks nekā 'c', bet mazāks nekā 'a'")
elif a > c > b:
    print("Skaitlis 'a' ir vislielākais, bet skaitlis 'b' - vismazākais, skaitlis 'c' ir lielāks nekā 'b', bet mazāks nekā 'a'")

if c > a > b:
    print("Skaitlis 'c' ir vislielākais, bet skaitlis 'b' - vismazākais, skaitlis 'a' ir lielāks nekā 'b', bet mazāks nekā 'c'")
elif c > b > a:
    print ("Skaitlis 'c' ir vislielākais, bet skaitlis 'a' - vismazākais, skaitlis 'b' ir lielāks nekā 'a', bet mazāks nekā 'b'")

#2. uzdevums
x = float(input("Ievadi sava kermeņa temperatūru skaitļos: "))
if x < 35.0:
    print("Vai nav par aukstu?")
elif 35.0 <= x <= 37.0:
    print("Viss kārtībā.")
elif x > 37.0:
    print("Iespējams drudzis.")

atr = "banka"
atr = "veikals"
atr = "aptieka"
x = str(input("Ievādi savu atrašanas vietu: "))
if atr == "banka":
    print("Te ir daudz naudas")
elif atr == "shop":
    print("Jānopērk āboli")
elif atr == "med":
    print("Man ir iesnas")
else:
    print("Ābolu nav")