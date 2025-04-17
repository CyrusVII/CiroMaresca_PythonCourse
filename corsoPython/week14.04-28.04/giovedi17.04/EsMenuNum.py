import numpy as np

def generaArray(start,end,step):
  array = np.arange(start, end, step)
  return array

def menu():
    array_list = []  # Lista che conterrà più array

    while True:
      try:
        # Inserimento start, end, e step
        start = int(input("Inserisci numero di start ---> "))
        end = int(input("Inserisci numero di end ---> ")) 

        # Controllo che end sia maggiore di start
        if end <= start:
          raise Exception("End deve essere maggiore di Start.")
        
        step = int(input("Inserisci numero di step ---> "))
        
        # Controllo che step sia maggiore di 0, altrimenti lo settiamo a 1
        if step < 1:
          step = 1
        
        # Generazione dell'array utilizzando numpy e aggiunta alla lista
        nuovo_array = generaArray(start, end, step)
        array_list.append(nuovo_array)
        print(f"Array generato: {nuovo_array}")
        
        # Chiedi all'utente se vuole aggiungere altre linee
        if input("Vuoi aggiungere altre linee? s/n ---> ").lower().strip() != 's':
          break

      except Exception as e:
        print(f"Errore nell'inserimento: {e}")
    
    return array_list

def main():
  matrice = menu()
  print("\n--- Matrice con lunghezze variabili ---")
  print(matrice)
  
main()