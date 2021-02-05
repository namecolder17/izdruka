#vārdnīcas jeb dictionaries
tel = {
    "direktors": "67947253",
    "vietnieks": "65674720",
    "sekretāre": "65826974"
}
print(tel["direktors"])

cenas = {
    "piens": 1.12,
    'āboli': 0.95,
    'apelsīni': 1.89
}
print(cenas['piens'])

d = {
    "k1": 123,
    "k2": [10,11,12], 
    "k3": {"atsl1":100, "atsl2":200}
}
print(d["k3"])
print(d["k3"]["atsl2"]) #izdrukā iekšējās vārdnīcas vērtību
print(d["k2"][1]) #izdrukā iekšējā saraksta elementu ar norādītu indeksu

my_dict = {'key1': ['a', 'b', 'c']}
print(my_dict)
my_list = my_dict['key1']
print(my_list)
burts = my_list[2]
print(burts.upper()) #izdrukā lielo burtu C, kas atrodas vārdnīcas vērtībā

print(my_dict['key1'][2].upper()) #vienā rindā atlasa elementu un pārveido

#pievieno jaunus objektus
new_dict = {"k1":100, "k2":200}
print(new_dict)
new_dict["k3"] = 300
print(new_dict)

#var piešķirt esošai atslēgai jaunu vērtību
new_dict["k1"] = "simts"
print(new_dict)

#vārdnīcu metodes
print(new_dict.keys()) #izdrukā visas atslēgas
print(new_dict.values()) #izdrukā vērtības
print(new_dict.items()) #izdrukā pārus
vertibu_list = list(new_dict.values())
print(vertibu_list)

print(new_dict.get("k1")) #izdrukā vērtību ar noteiktu atslēgu

new_dict.pop("k2") #noņem k2 no vardnīcas
print(new_dict) 

new_dict.clear()
print(new_dict) #noņem visu

