# Esercizio Slicing e F. Indexing
# ampariMirko is sharing
# Esercizio su NumPy Slicing
# Consegna:
# 1. Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50.
# 2. Utilizza Lo slicing per estrarre i primi 10 dell'array.
# 3. Utilizza dell'array.
# elementi
# 9
# lo slicing per estrarre gli ultimi 5 elementi +
# 4. Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso).
# 5. Utilizza dell'array.
# 6. Modifica,
# Lo slicing per estrarre ogni terzo elemento
# tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99.
# 7. Stampa l'array originale e tutti i sottoarray ottenuti tramite slicing.
# Obiettivo:
# Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre e modificare sottoarray specifici da un array più grande.

import numpy as np
arr = np.random.randint(10, 51, size=20) 
arrPrimiNumeri = arr[:10]
arrUltimi = arr[16:]
arrAlternato  = arr[2: :3]
#prendo l array originale e modifico i numeri da 5 a 9 in 99
arrModificato = arr; arrModificato[5:10] = 99
print("--- Array comleto ---\n",arr)
print("--- Primi 10 numeri ---\n", arrPrimiNumeri)
print("--- Ultimi 5 numeri ---\n", arrUltimi)
print("--- Ogni 3 numeri ---\n", arrAlternato)
print("--- Modifica valori da 5 a 9 con 99 ---\n",arrModificato)