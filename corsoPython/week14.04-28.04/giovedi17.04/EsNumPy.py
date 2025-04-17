# Crea un array NumPy utilizzando arange e verifica il tipo di dato (dtype) e la forma (shape) dell'array.
# Esercizio:
# 1. Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
# 2. Verifica il tipo di dato dell'array e stampa il risultato.
# 3. Cambia
# il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato.
# 4. Stampa la forma dell'array.
import numpy as np
#genero l arr da 10 a 49 e verifico sia inter
arr = np.arange(10,50,dtype=np.int64)
print(f"--- Array interi --- \n {arr}") #stampa array int
#converto l array in float
arr_float = arr.astype(float)
print(f"--- Array float --- \n tipo : {arr_float.dtype} \n {arr_float} ") 
print("Forma array float", np.shape(arr_float))