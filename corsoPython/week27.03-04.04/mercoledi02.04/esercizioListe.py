#funzione calcolo quadrato singolo
def quadrato():
  n = int(input("Inserisci un numero: "))
  print(f"Il quadrato di {n} = {pow(n,2)}")
  
#somma liste
def sum_list(lista, somma):
    """Itera la lista, stampa il quadrato di ogni numero e aggiorna la somma"""
    for i in lista:
        print(f"Il quadrato di {i} = {pow(i,2)}")
        somma += i
    return somma  

# funzione calcolo quadrato lista
def somma_lista():
    """Permette di creare più liste, calcola il quadrato di ogni numero e il quadrato della somma totale"""
    somma = 0
    nLista = []
    
    while True:
        n = int(input("Inserisci un numero: "))
        nLista.append(n)
        
        if input("Vuoi aggiungere ancora? (s/n) ---> ").lower().strip() == "n":
            if input("----- \n Vuoi fare un'altra lista? (s/n) ---> ").lower().strip() == "s":
                somma = sum_list(nLista, somma)  
                nLista.clear()
            else:
                somma = sum_list(nLista, somma) 
                break
    
    print(f"Il quadrato della somma totale è: {pow(somma,2)}")

#funzione main per avviare il tutto
def main():
  #un menu per gestire i due esercizi
  while True:
    match int(input("--- Menu --- \n 1) Quadrato di un numero \n 2) Quadrato di una lista o piu e somma \n ---> ")):
      case 1:
        quadrato()
      case 2:
        somma_lista()
        
    if input("-----\n Vuoi tornare al menu? (s/n) ---> ").lower().strip() == "n":
      break

#chiamo il main che avvia il programma
main()

