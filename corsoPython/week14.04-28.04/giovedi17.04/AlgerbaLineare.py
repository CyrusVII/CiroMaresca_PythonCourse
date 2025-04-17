import numpy as np
# Creazione di una matrice 2x2
A = np.array([[1, 2], [3, 4]])
#print("A matrice:\n", A)

# Calcolo dell'inversa della matrice A
# L'inversa di una matrice quadrata A è una matrice A⁻¹ tale che:
# A * A⁻¹ = I, dove I è la matrice identità (una matrice con 1 sulla diagonale e 0 altrove)
# Non tutte le matrici hanno un'inversa: una matrice è invertibile solo se il suo determinante è diverso da 0
# np.linalg.inv(A) utilizza funzioni di algebra lineare per calcolare l'inversa (se esiste)
A_inv = np.linalg.inv(A)
#print("Inversa di A:\n", A_inv)
# Verifica (opzionale): prodotto di A per la sua inversa dovrebbe dare la matrice identità
I = np.dot(A, A_inv)
#print("A * A_inv (matrice identità):\n", I)


# Creazione di un vettore (2D in questo caso)
v = np.array([3, 4])
# Calcolo della norma del vettore
# La norma di un vettore è una misura della sua "lunghezza" (o modulo)
# Per un vettore 2D [x, y], la norma euclidea (o L2) è:
# sqrt(x^2 + y^2)
# Quindi in questo caso: sqrt(3^2 + 4^2) = sqrt(9 + 16) = sqrt(25) = 5
# np.linalg.norm() calcola proprio questa norma euclidea di default
norm_v = np.linalg.norm(v)
#print("Norma di v:", norm_v)


# Creazione di un array NumPy 1D
arr = np.array([1, 2, 3, 4])
# Definizione di uno scalare
scalar = 10
# Broadcasting: somma tra array e scalare
# NumPy applica automaticamente lo scalare a ciascun elemento dell'array
# In pratica fa: [1+10, 2+10, 3+10, 4+10] → [11, 12, 13, 14]
# Questo comportamento si chiama "broadcasting" ed è uno dei punti di forza di NumPy
result = arr + scalar
print(result)


import numpy as np

# Creazione di due array NumPy 1D
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# Operazioni aritmetiche tra array
# Qui viene fatta una somma elemento per elemento (element-wise)
# Risultato: [1+4, 2+5, 3+6] = [5, 7, 9]
c = a + b
print("Somma elemento per elemento:", c)
# Funzioni matematiche su array
# np.sin() applica la funzione seno a ogni elemento dell'array
# Calcola: [sin(1), sin(2), sin(3)] (in radianti)
d = np.sin(a)
print("Seno degli elementi di a:", d)
# Algebra lineare
# np.dot(a, b) calcola il prodotto scalare tra i due vettori
# Formula: 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32
e = np.dot(a, b)
print("Prodotto scalare tra a e b:", e)

