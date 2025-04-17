# Operazioni con Fancy Indexing
# Creare un array NumPy di forma (4, 4) contenente numeri casuali interi tra 10 e 50. Utilizzare fancy 
# indexing per selezionare e stampare gli elementi agli indici (0, 1), (1, 3), (2, 2) e (3, 0).
# Utilizzare fancy indexing per selezionare e stampare tutte le righe dispari dell'array (considerando la numerazione delle righe che parte da 0).
# Modificare gli elementi selezionati nel primo punto dell'esercizio aggiungendo 10 al loro valore.
import numpy as np

def create_array():
    while True:
        try:
            n1 = int(input("Inserisci start ---> "))
            n2 = int(input("Inserisci stop ---> "))
            if n2 <= n1:
                raise Exception("Stop deve essere maggiore di start. Riprova.")
            el = int(input("Inserisci la dimensione della matrice ---> "))
            break
        except ValueError:
          print("Dato non valido inserisci un intero")
        except Exception as e:
            print("Errore:", e)
    return np.random.randint(n1, n2, size=(el,el))
  
# Funzione per selezionare e stampare gli elementi agli indici scelti dall'utente
def seleziona_elementi(arr):
  print("\nIndici disponibili dell'array:")
  print(arr)
  try:
    riga = int(input("Inserisci numero riga ---> "))
    colonna = int(input("Inserisci numero colonna ---> "))
    selected_elements = arr[riga,colonna]
    print("Elementi selezionati:", selected_elements)
  except Exception as e:
    print("Errore:", e)

# Funzione per selezionare e stampare tutte le righe dispari dell'array
def righe_dispari(arr):
  print("\nIndici disponibili dell'array:")
  print(arr)
  print("Righe dispari dell'array:")
  print(arr[::2])  # Seleziona tutte le righe dispari

# Funzione per modificare gli elementi selezionati aggiungendo 10 al loro valore
def modifica_elementi(arr):
  print("\nIndici disponibili dell'array:")
  print(arr)
  try:
    riga = int(input("Inserisci numero riga ---> "))
    colonna = int(input("Inserisci numero colonna ---> "))
    arr[riga,colonna] += 10
    print("Array dopo la modifica:")
    print(arr)
  except Exception as e:
    print("Errore:", e)
    
def menu():
    print("--- Menu ---")
    print("1. Selezionare e stampare gli elementi agli indici scelti da utente tramite Fancy Indexing.")
    print("2. Selezionare e stampare tutte le righe dispari dell'array.")
    print("3. Modificare gli elementi selezionati aggiungendo 10 al loro valore.")
    print("4. Exit")
    return input("---> ")

def main():
  print("Creazione Array")
  arr = create_array()
  print("\nArray generato:", arr)
  while True:
    match menu():
      case "1":
        seleziona_elementi(arr)
      case "2":
        righe_dispari(arr)
      case "3":
        modifica_elementi(arr)
      case "4":
          break
      case _:
        print("Scelta non valida")
          
if __name__ == "__main__":
    main()