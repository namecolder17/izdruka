x = input("Ievadi teikumu: ")
print(len(x)) # 1.uzd

x = input("Ievadi vārdu: ")
print(x[0]) # 2.uzd

print("Sveika, Pasaule"[10:15]) # 3.uzd

x = input("Ievadi teikumu: ")
print(x.upper()) # 4.uzd

x = input("Ievadi teikumu: ")
print(x.lower()) # 5.uzd

x = "samērcēt"
y = x.replace("samērcēt" , "pamērcēt")
print(y) # 6.uzd

x = " Sveika, Pasaule! "
y = x.strip()
print(y) # 7.uzd

# Tagad es jums parādīšu triku. Izdomājiet skaitli (x), saskaitiet ar to (x+x=y), reiziniet ar 4 (y*4=z), daliet ar izdomāto skaitli (z/x=a). Atbilde (a) ir 8?
x = int(input("Izdomā skaitli: "))
y = x + x
z = y*4
atbilde = z / x
print(atbilde)  # 8.uzd

x = input("Ievadi savu vārdu: ")
print(x[::-1] + ". Pamatīgs juceklis, vai ne, " + x[0] + "?") # 9.uzd