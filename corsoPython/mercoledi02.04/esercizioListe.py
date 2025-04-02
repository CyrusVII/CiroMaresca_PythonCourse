#funzione calcolo quadrato singolo
def quadrato():
  n = int(input("Inserisci un numero: "))
  print(f"Il quadrato di {n} = {pow(n,2)}")
  
#funzione calcolo quadrato lista
def somma_lista():
  nLista = []
  #ciclo per fa inserire i numeri nella lista
  while True:
    n = int(input("Inserisci un numero: "))
    nLista.append(n)
    if input("Vuoi aggingere ancora? (s/n) ---> ").lower().strip() == "n":
      break
  #dichiaro una variabile somma 
  somma = 0
  #faccio un ciclo per iterare la lista e fare i quadrati piu la somma
  for i in nLista:
    print(f"Il quadrato di {i} = {pow(i,2)}")
    somma += i
    
  print(f"Il quadrato della lista e: {pow(somma,2)}")

#funzione main per avviare il tutto
def main():
  #un menu per gestire i due esercizi
  while True:
    match int(input("--- Menu --- \n 1) Quadrato di un numero \n 2) Quadrato di una lista e somma \n ---> ")):
      case 1:
        quadrato()
      case 2:
        somma_lista()
        
    if input("-----\n Vuoi tornare al menu? (s/n) ---> ").lower().strip() == "n":
      break

#chiamo il main che avvia il programma
main()