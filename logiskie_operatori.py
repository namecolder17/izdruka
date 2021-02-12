#salidzināšana
print(2 == 2)
print(2 == "2")
print("asd" == "asd")
print(2 == 2.0)
print(2 == 4 / 2)
print(2 + 2 * 2 == 6)
print(2 * 2 != 5)
print(3**4 == 81)
a = 50
b = 4
c = 4
print(a > b, b != c, c == a, c + a == b + 50)

#loģiskie operatori - and/or/not
print(True and True)
a = 5
b = 10
c = 14
print(a > 5 and b > 20)
print(a >= 5 and b >= 7 and a < c and b >= c)  #izpildījas pirmie 3, bet pēdējais nē
print(a >= 5 and b >= 7 and a < c or b >= c)
print(not a > 7)
print(a < b and b < c)
print(a < b < c)
