#come istruzioni abbiamo il break che viene utilizzato per interrompere l'esecuzione di un ciclo in anticipo
# numeri = [1,2,3,4,5]

# for numero in numeri:
#   if numero == 3:
#     break
#   print(numero)
  
#continue viene utilizzato per saltare il resto del blocco di codice all interno di un ciclo e passare alla prossima iterazione
# numeri = [1,2,3,4,5]

# for numero in numeri:
#   if numero == 3:
#     continue
#   print(numero)
  
#pass viene utilizzato quando si desidera eseguire alcuna azione all interno di un ciclo
# for i in range(5):
#   if i == 3:
#     pass
#   print(i)

#riempie velocemente una lista
# numeri = [*range(1,11)]
# print(numeri)

#le tuple
#le tuple sono strutture dati simile alla lista, ma con una differenza chiave sono immutabili
# Definizione di una tupla che rappresenta un punto nel piano cartesiano
# punto = (3, 4)  
# # Definizione di una tupla che rappresenta un colore in formato RGB
# colore_rgb = (255, 128, 0)  
# # Definizione di una tupla con informazioni personali
# informazioni_persona = ("Alice", 25, "Femmina")  
# # Assegnazione senza parentesi: Python la interpreta comunque come una tupla (tuple packing)
# pippo = 3, 4  
# # Tuple unpacking: i valori della tupla 'pippo' vengono assegnati alle variabili x e y
# x, y = pippo  
# # Stampa dei valori di x e y
# print(x, y)  # Output: 3 4

#insiemi ----
# Creazione di un insieme usando la funzione set()
set1 = set([1, 2, 3, 4, 5])  
# Creazione di un insieme usando la sintassi con le parentesi graffe
set2 = {4, 5, 6, 7, 8}  
# Creazione di un insieme con valori duplicati (i duplicati vengono eliminati automaticamente)
set3 = {1, 2, 3, 4, 5, 5, 6}  
# Stampa dell'insieme set3 (mostrerà solo valori univoci)
print(set3)  # Output: {1, 2, 3, 4, 5, 6}
a = {1, 2, 3}
b = {3, 4, 5}
# Creazione di due insiemi di esempio
set_a = {1, 2, 3}
set_b = {3, 4, 5}
# 1) Unione - Combina tutti gli elementi, eliminando i duplicati
union_set = set_a.union(set_b)  # Metodo
union_operator = set_a | set_b  # Operatore '|'
print(f"Unione (union() o |): {union_set}")
# 2) Intersezione - Trova gli elementi comuni tra i due insiemi
intersection_set = set_a.intersection(set_b)  # Metodo
intersection_operator = set_a & set_b  # Operatore '&'
print(f"Intersezione (intersection() o &): {intersection_set}")
# 3) Differenza - Elementi presenti solo nel primo insieme
difference_set = set_a.difference(set_b)  # Metodo
difference_operator = set_a - set_b  # Operatore '-'
print(f"Differenza (difference() o -): {difference_set}")
# 4) Differenza Simmetrica - Elementi unici tra i due insiemi (esclude quelli comuni)
symmetric_diff_set = set_a.symmetric_difference(set_b)  # Metodo
symmetric_diff_operator = set_a ^ set_b  # Operatore '^'
print(f"Differenza Simmetrica (symmetric_difference() o ^): {symmetric_diff_set}")
# Aggiunta di un elemento
set1.add(4)  # {1, 2, 3, 4}
# Rimozione di un elemento (genera errore se l'elemento non esiste)
set1.remove(2)  # {1, 3, 4}
# Rimozione di un elemento senza errore se non esiste
set1.discard(10)  # Non fa nulla se 10 non esiste
# Estrazione casuale di un elemento
elem = set1.pop()  # Rimuove e restituisce un elemento casuale
# Svuotare completamente l'insieme
set1.clear()  # diventa un insieme vuoto: set()
# Verifica se 'a' è un sottoinsieme di 'b'
print(a.issubset(b))  # True
# Verifica se 'b' è un superinsieme di 'a'
print(b.issuperset(a))  # True
# Verifica se due insiemi sono disgiunti (non hanno elementi in comune)
print(a.isdisjoint({6, 7}))  # True