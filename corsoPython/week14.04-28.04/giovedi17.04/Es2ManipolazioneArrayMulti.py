# Manipolazione di Array Multidimensionali
# Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25. 
# Estrarre e stampare la seconda colonna della matrice.
# Estrarre e stampare la terza riga della matrice.
# Calcolare e stampare la somma degli elementi della diagonale principale della matrice.
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
  
def menu():
  print("--- Menu ---")
  print("1. Estrarre e stampare una colonna della matrice")
  print("2. Estrarre e stampare una riga della matrice.")
  print("3. Calcolare e stampare la somma degli elementi della diagonale principale della matrice.")
  print("4. Exit")
  return input("---> ")

def colonna(arr):
  try:
    # Mostra all'utente quante colonne sono disponibili
    num_colonne = arr.shape[1]
    print(f"La matrice ha {num_colonne} colonne (da 0 a {num_colonne - 1})")
    # Input utente per selezionare la colonna
    num = int(input("Inserisci l'indice della colonna che vuoi estrarre: "))
    # Controllo: l'indice deve essere compreso tra 0 e num_colonne - 1
    if num < 0 or num >= num_colonne:
        print("Indice fuori dal range disponibile.")
        return
    # Estrazione e stampa della colonna
    col = arr[:, num]
    print(f"Colonna {num}:", col)
  except ValueError:
      print("Errore: devi inserire un numero intero.")
  except IndexError:
      print("Errore: indice colonna non valido.")
  except Exception as e:
      print("Errore inatteso:", e)

def riga(arr):
  try:
    # Mostra all'utente quante righe sono disponibili
    num_righe = arr.shape[0]
    print(f"La matrice ha {num_righe} righe (da 0 a {num_righe - 1})")
    # Input utente per selezionare la riga
    num = int(input("Inserisci l'indice della riga che vuoi estrarre: "))
    # Controllo che l'indice sia valido
    if num < 0 or num >= num_righe:
        print("Indice fuori dal range disponibile.")
        return
    # Estrazione e stampa della riga
    r = arr[num]
    print(f"Riga {num}:", r)
  except ValueError:
      print("Errore: devi inserire un numero intero.")
  except IndexError:
      print("Errore: indice riga non valido.")
  except Exception as e:
      print("Errore inatteso:", e)

def somma_diagonale(arr):
  # Calcolo della somma della diagonale principale
  somma_diag = np.trace(arr)
  print("Somma della diagonale principale:", somma_diag)
  
def main():
  print("Creazione Array")
  arr = create_array()
  print("\nArray generato:", arr)
  while True:
    match menu():
      case "1":
        colonna(arr)
      case "2":
        riga(arr)
      case "3":
        somma_diagonale(arr)
      case "4":
          break
      case _:
        print("Scelta non valida")
          
if __name__ == "__main__":
    main()