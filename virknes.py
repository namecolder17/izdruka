"""vards = input("Kā tevi sauc? ")
print("Labdien, " + vards)

vecums = int(input("Cik tev ir gadu? "))

print(f"Tev ir {vecums} gadi.")

print(f"Tavs dzimšanas gads ir {2021-vecums}.") #viens veids

dzimsGads = 2021 - vecums
print(f"Tavs dzimšanas gads ir {dzimsGads}.") #otrais veids

temperatura = int(input("Ieraksti temperatūru Celsijos: "))
farenheits = temperatura *9/5+32
print(f"Tas ir {farenheits} grādi farenheita skalā") #temperatūra

platums = float(input("Uzraksti istabas platumu metros: "))
garums = float(input("Uzraksti istabas garumu metros: ")) #istaba
augstums = float(input("Uzraksti istabas augstumu metros: "))
tilpums = platums*garums*augstums
print(f"Tavas istabas tilpums ir {tilpums} kubikmetri.")"""
#Strings (rakstzīmju virknes)
"""print("Sveiki")
print('Sveiki')
print("I'm going on a run")
print('Arī šis ir "risinājums"')

print("Sveika, \npasaule!") #Izdruka tekstu divās rindās
print("Sveika, \tpasaule!") 
#Drukā ar tabulācijas atkāpi

#String garums - len()
print(len("Sveiki")) 
#drukā burtu skaitu
print(len("Ko tu domā?"))
#atstarpes skaitās arī
# [sākums:beigas:solis]"""
myString = "Sveiki, pasaule!"
print(myString)
print(myString[0]) #izdrukā 1. simbolu
print(myString[6]) #izdrukā 7. simbolu
print(myString[8]) #izdrukā rakstzīmi ar 8. indeksu
print(myString[-1]) #izdrukā pēdējo simbolu
print(myString[13]) #izdrukā 14. rakstzīmi
print(myString[-3]) #izdrukā 14. rakstzīmi

myString = "abcdefghijklmnoprstuvz"
print(myString)
print(myString[2]) #izdrukā c
print(myString[2:]) #izdrukā visu, sakot no c
print(myString[:3]) #izdrukā visu līdz 3. indeksam, neieskaitot
print(myString[3:6]) #izdrukā visu no 3. indeksa līdz 6. , neieskaitot
print(myString[::]) #izdrukā visu
print(myString[::2]) #izdrukā katru otro rakstzīmi
print(myString[2:7:2]) #izdrukā no c līdz g, bet katru otro