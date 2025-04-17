# Esercizio 1: Somma e Media di Elementi
# Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e 100.
# Calcolare e stampare la somma di tutti gli elementi dell'array. Calcolare e stampare la media di tutti gli elementi dell'array.
import numpy as np

def create_array():
    while True:
        try:
            n1 = int(input("Inserisci start ---> "))
            n2 = int(input("Inserisci stop ---> "))
            if n2 <= n1:
                raise Exception("Stop deve essere maggiore di start. Riprova.")
            el = int(input("Inserisci la dimensione dell'array ---> "))
            break
        except Exception as e:
            print("Errore:", e)
    return np.random.randint(n1, n2, el)

def main():
    arr = create_array()
    print("\nArray generato:", arr)
    
    somma = np.sum(arr)    # Calcola la somma degli elementi
    media = np.mean(arr)   # Calcola la media
    
    print("Somma degli elementi:", somma)
    print("Media degli elementi:", media)

if __name__ == "__main__":
    main()
