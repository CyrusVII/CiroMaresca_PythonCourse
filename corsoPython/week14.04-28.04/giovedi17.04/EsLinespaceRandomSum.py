# Es1: linspace, random, sum
# Descrizione: Crea un array utilizzando linspace, cambia la sua forma con reshape, genera un array casuale e calcola la somma degli elementi.
# Esercizio:
# 1. Crea
# un array di 12 numeri equidistanti tra 0 e 1 usando linspace.
# 2. Cambia la forma dell'array a una matrice 3x4.
# 3. Genera una matrice 3x4 di numeri casuali tra 0 e 1.
# 4. Calcola matrici.
# e stampa la somma degli elementi di entrambe le
import numpy as np

def menu():
    print("Seleziona un'opzione:")
    print("1. Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace.")
    print("2. Cambia la forma dell'array a una matrice 3x4.")
    print("3. Crea una matrice 3x4 di numeri casuali tra 0 e 1.")
    print("4. Calcola e stampa la somma degli elementi di entrambe le matrici.")
    print("5. Esci.")
    
    scelta = int(input("---> "))
    return scelta

def crea_linspace():
    array = np.round(np.linspace(0, 1, 12), 3)
    print("Array creato con linspace:")
    print(array)
    return array

def cambia_forma():
    array = crea_linspace()
    matrice = array.reshape(3, 4)
    print("Matrice 3x4:")
    print(matrice)

def matrice_casuale():
    matrice = np.round(np.random.rand(3, 4),3)
    print("Matrice casuale 3x4:")
    print(matrice)
    return matrice

def calcola_somma():
    matrice1 = crea_linspace()
    matrice2 = matrice_casuale()
    somma1 = np.sum(matrice1)
    somma2 = np.sum(matrice2)
    print(f"Somma degli elementi della matrice 1: {somma1}")
    print(f"Somma degli elementi della matrice 2: {somma2}")
    
def main():
  while True:
    ch = menu()
    match ch:
      case 1:
        crea_linspace()
      case 2:
        cambia_forma()
      case 3:
        matrice_casuale()
      case 4:
        calcola_somma()
      case 5:
        print("Abbandono programma....")
        break
      
main()