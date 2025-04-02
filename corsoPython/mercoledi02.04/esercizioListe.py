def quadrato():
  n = int(input("Inserisci un numero: "))
  print(f"Il quadrato di {n} = {pow(n,2)}")
  

def somma_lista():
  nLista = []
  while True:
    n = int(input("Inserisci un numero: "))
    nLista.append(n)
    if input("Vuoi aggingere ancora? (s/n) ---> ").lower().strip() == "n":
      break
  somma = 0
  
  for i in nLista:
    print(f"Il quadrato di {i} = {pow(i,2)}")
    somma += i
    
  print(f"Il quadrato della lista e: {pow(somma,2)}")

def main():
  while True:
    match int(input("--- Menu --- \n 1) Quadrato di un numero \n 2) Quadrato di una lista e somma \n ---> ")):
      case 1:
        quadrato()
      case 2:
        somma_lista()
        
    if input("Vuoi tornare al menu? (s/n) ---> ").lower().strip() == "n":
      break
    
main()