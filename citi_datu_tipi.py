#tuples - līdzīgi list, bet nav maināmi, izmanto (iekavas), sakārtots
my_tup = (1,2,3,4,5)
my_list = [1,2,3]
print(type(my_tup))
print(type(my_list))
print(len(my_tup))

#var saturēt dažādus datu tipus
my_tup = ("es", 6, 6, 2.58)
print(my_tup)

#var indeksēt
print(my_tup[0])
print(my_tup[-1])

#metodes
print(my_tup.count(6)) #saskaitā cik sešinieku sarakstā
print(my_tup.index(2.58))#parāda indeksu, kur pirmoreiz parādās objekts

#nav maināms
my_list[0] = "viens"
print(my_list)
"""my_tup[0] = "viens"
print(my_tup) - rāda kļūdu, jo tuple objektus nevar mainīt"""

#sets - nesākartota unikālu objektu kopa
my_set = set()
print(my_set)
my_set.add(1)
print(my_set)
my_set.add(2)
print(my_set)
my_set.add(1.26)
print(my_set)

my_list = [1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,3,3,3]
print(my_list)
print(set(my_list)) #izdrukā vienu unikālu skaitļu

#piemērs
s = "Salaspils"
my_set = set(s)
print(my_set)

#booleans - True vai False - izmanto bieži loģiskajos operatoros
print(True)
print(type(False))

#piemērs
print(3 > 2)
print(1 > 2)
print(1 == 1)