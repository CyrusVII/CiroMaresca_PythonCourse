#Esecizi dizionario
st = input("inserisci una stringa ---> ")
dizionario = {}
for lettera in st:
    dizionario[lettera] = dizionario.get(lettera, 0) + 1
print(dizionario)

#senza metodi
st = input("inserisci string ---> ")
dizionario = {}
for lettera in st:
    if lettera in dizionario:
        dizionario[lettera] += 1
    else:
        dizionario[lettera] = 1
print(dizionario)

#altro metodo con counter
from collections import Counter
st = input("inserisci string ---> ")
conteggio = Counter(st) # crea un oggetto Counter a partire dalla stringa
dizionario  = dict(conteggio) # crea un dizionario a partire da un oggetto Counter
print(dizionario)