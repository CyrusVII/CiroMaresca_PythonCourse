import numpy as np

# Crea un array con 5 valori equidistanti tra 0 e 1
arr = np.linspace(0, 1, 5)
print(arr)  # Uscita: [0.   0.25 0.5  0.75 1.  ]

# Crea una matrice 3x3 con valori casuali distribuiti uniformemente tra 0 e 1
random_arr = np.random.rand(3, 3)
print(random_arr)  # Uscita: Valori casuali tra 0 e 1 in una matrice 3x3

# Crea un array monodimensionale
arr1 = np.array([1, 2, 3, 4, 5])

# Calcola la somma di tutti gli elementi di arr1
sum_value = np.sum(arr1)
# Calcola la media (valore medio) di tutti gli elementi di arr1
mean_value = np.mean(arr1)
# Calcola la deviazione standard degli elementi di arr1
std_value = np.std(arr1)

# Stampa la somma, la media e la deviazione standard
print("Somma: ", sum_value)  # Uscita: Somma degli elementi di arr1 (15)
print("Media: ", mean_value)  # Uscita: Media degli elementi di arr1 (3.0)
print("Deviazione standard: ", std_value)  # Uscita: Deviazione standard degli elementi di arr1 (~1.4142135623730951)

