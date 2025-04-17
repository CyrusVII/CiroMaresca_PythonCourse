#studia da slide 221 -225
# numpy_basi.py
# Assicurati di aver installato numpy con:
# pip install numpy

import numpy as np

# --- 1. CREAZIONE DI ARRAY ---

# Array unidimensionale
arr1 = np.array([1, 2, 3, 4, 5])
print("Array 1D:", arr1)

# Array bidimensionale (matrice)
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Array 2D:\n", arr2d)

# Array di zeri (3 righe, 3 colonne)
zeros = np.zeros((3, 3))
print("Array di zeri:\n", zeros)

# Array di uni
ones = np.ones((2, 4))
print("Array di uni:\n", ones)

# Array con numeri casuali tra 0 e 1
random = np.random.rand(2, 2)
print("Array casuale:\n", random)

# Array con numeri in sequenza
# np.arange(10) farebbe da  uno a 10
arange_arr = np.arange(0, 10, 2)#start stop step
print("Array con arange:", arange_arr)

# Array con numeri equidistanti
linspace_arr = np.linspace(0, 1, 5)
print("Array con linspace:", linspace_arr)

#array shape
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape) #rida numero arrai 2 e dati negli array 4 quindi 2,4

# --- 2. OPERAZIONI MATEMATICHE ---

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Somma:", a + b)
print("Sottrazione:", a - b)
print("Moltiplicazione:", a * b)
print("Divisione:", a / b)

# --- 3. STATISTICHE DI BASE ---

stats_arr = np.array([1, 2, 3, 4, 5])

print("Media:", np.mean(stats_arr))
print("Mediana:", np.median(stats_arr))
print("Deviazione standard:", np.std(stats_arr))
print("Valore massimo:", np.max(stats_arr))
print("Valore minimo:", np.min(stats_arr))

# --- 4. INDICIZZAZIONE E SLICING ---

slicing_arr = np.array([10, 20, 30, 40, 50])

print("Elemento all'indice 2:", slicing_arr[2])
print("Slice da indice 1 a 4:", slicing_arr[1:4])
print("Ultimo elemento:", slicing_arr[-1])
print(slicing_arr[1,4])# [20,50]
indices = [2,4]
print(slicing_arr[indices])# [30,50] 

arrScaling = np.array([[1,2,3,4],
                       [5,6,7,8],
                       [9,10,11,12]])
#scaling sulle righe
print(arrScaling[1:3])#output[[5 6 7 8] [9 10 11 12]]

#scaling sulle colonne
print(arrScaling[:, 1:2])#output [[2 3] [6 7] [10 11]]

#scaling misto 
print(arrScaling[1:, 1:3])#output [[6 7] [10 11]]

arrSlicing = np.array([0,1,2,3,4,5,6,7,8,9,10])

#slicing base
print(arr[2:7])

#slicing con passo
print(arr[1:8:2]) #output [1 3 5 7]

#omettere start and stop
print(arr[:5]) #stampa da 0 a 5
print(arr[5:]) #stampa da 5 a 9

#utilizzare indici negativi
print(arr[:-5]) #stampa da 5 a 9
print(arr[-5:]) #stampa da 0 a 4

# --- 5. RESHAPE E TRASPOSTA ---

reshape_arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = reshape_arr.reshape(2, 3)
print("Array reshape 2x3:\n", reshaped)

# Trasposta di una matrice
print("Trasposta:\n", reshaped.T)

# --- 6. OPERAZIONI SU ARRAY 2D ---

mat2d = np.array([[1, 2], [3, 4]])

print("Somma totale:", np.sum(mat2d))
print("Somma per righe:", np.sum(mat2d, axis=1))
print("Somma per colonne:", np.sum(mat2d, axis=0))

# --- 7. OPERAZIONI LOGICHE / FILTRAGGIO ---
logic_arr = np.array([5, 10, 15, 20])





# Maschera booleana
mask = logic_arr > 10
print("Maschera logica:", mask)
print("Elementi maggiori di 10:", logic_arr[mask])

# --- FINE ---
