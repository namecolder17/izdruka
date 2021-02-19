#print("Sveiki")
#print("Sveiki")
#print("Sveiki "*5)

#while True:
   # print("Sveiki")

i = 0 #tipisks cikla mainīgais
while i <= 5:
    print("Sveiki")
    i += 1
print("i tagad ir", i)

j=0
while j < 5:
    print("Nr.",j)
    j += 1

while i > 0:
    print("Skaitām atpakaļ", i)
    i -= 1

i = 20
while True:
    if i > 26:
        break
    print("i ir", i)
    i += 2

#uzdevums
augstums = int(input("Ievādi eglītes augstumu metros: "))
i = 0
while i < augstums:
    print("*" * augstums)
    i += 1
