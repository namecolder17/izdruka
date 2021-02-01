# lists jeb saraksti
['Sveika,', 100, 'tu', 3.59, 'skaista!', [1, 26]]
myList = [1, 2, 3, 100, 'tu', 3.59, 'skaista!']
print(len(myList))  #saraksta garums

my_list = ["viens", "divi", "trīs", 'četri']
print(my_list[0])  #izdrukā elementu ar norādītu indeksu
print(my_list[1:])  #izdrukā no norādītā indeksa līdz beigām

#sarakstu apvienošana jeb konkatinācija
cits_list = ["pieci", "seši"]
print(my_list + cits_list)  #izdrukā sakarstu ar abu mainīgo elementiem
jauns_list = my_list + cits_list
print(jauns_list)

#sarakstu mainīšana
jauns_list[0] = 1
print(jauns_list)

jauns_list.append("septiņi")  #pievieno pēdējo elementu
print(jauns_list)
jauns_list.append("8")
print(jauns_list)

jauns_list.pop()
print(jauns_list)  #noņem pēdējo elementu
jauns_list.pop(3)  #noņem elementu ar indeksu 3
print(jauns_list)
pop_elem = jauns_list.pop(2)  #noņem elementu ar indeksu 2
print(jauns_list)
print(pop_elem)  #izdrukā elementu ar indeksu 2

#elementu kārtošana
new_list = ['b', 'a', 'z', 'e']
print(new_list)
num_list = [4, 1, 8, 3]
print(num_list)
new_list.sort() #sakārtoja pēc alfabēta
print(new_list)
num_list.sort() #sakārtoja no mazāka skaitļa uz lielāko
print(num_list)
num_list.reverse() #sakārtoja no lielāka skaitļa uz mazāko
print(num_list)

myList = [1, 2, 3, 100, 3.59]
myList.sort()
print(myList)

#saraksts sarakstā (nested)
nested_list = [1,5,[7,2]]
print(nested_list[2][1]) #izdrukājam simbolu ar indeksu 1 otrajā sarakstā

augli = ["ābols", "banāns", "gurķis"]
print(augli[2])

augli[2]="apelsīns"
print(augli) #aizstājam elementu gurķis -> apelsīns

augli.append("bumbieris")
print(augli) #pievienojam beigās "bumbieris"

augli.insert(2, "citrons")
print(augli) #ievietojam elementu tur, kur gribam

augli.pop(1)
print(augli) #noņemam elementu ar indeksu 1

"""augli.remove("banāns")
print(augli) #otrais variant, kā noņemt elementu"""

print(f"Sarakstā ir {len(augli)} dažādi augļi.")
augli.sort()
print(augli)