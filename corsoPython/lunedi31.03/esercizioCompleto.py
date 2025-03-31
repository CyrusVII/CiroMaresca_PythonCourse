# Punto 1: Utilizzo di if
# Scrivi un sistema che prende in input un numero e stampa "Pari" se il numero è pari e "Dispari" se il numero è dispari.
# Punto 2: Utilizzo di while e range
# Scrivi un sistema che prende in input un numero intero positivo n e stampa tutti i numeri da n a 0 (compreso), 
# decrementando di 1.Deve potersi ripete all'infinito
# Punto 3: Utilizzo di for
# Scrivi un sistema che prende in input una lista di numeri e stampa il quadrato di ciascun numero nella lista.
# Punto 4: Utilizzo di if, while e for insieme Scrivi un sistema che prende in 
# input una lista di numeri interi che precedente è stata valorizzata dall'utente. Il sistema deve:
# 1. Utilizzare un ciclo for per trovare il numero massimo nella lista.
# 2. Utilizzare un ciclo while per contare quanti numeri sono presenti nella lista. 
# 3. Utilizzare una condizione if per stampare "Lista Vuota" se la lista è vuota, altrimenti stampare il numero massimo trovato e il numero di elementi nella lista.

#dichiarazione funzioni
def numEven(n):
  if n%2 == 0:
    return f"Il numero {n} e pari"
  return f"Il numero {n} e dispari"

#inizio main
try:  
  
  #var per il while
  b = True
  while b:
    #scelta dell utente 
    st = int(input("-----\nCosa vuoi fare:\n1)Vediamo se il numero e pari \n2)Conto alla rovescia \n3)Calcoliamo il quadrato \n4)Gioco lista\n0) Abbandona \n---> "))
    #match per la scelta
    match st:
      case 0:#case di uscita
        print("Arrivederci")
        break
      case 1:#primo esercizio troviamo un numero positivo
        n = int(input("Inserisci un numero -->"))
        print(numEven(n))
      case 2:#contiamo alla rovescia
        n = int(input("Inserisci un numero positivo-->"))
        if(n > 0):
          for i in range(n, -1, -1):
            print(i)
          else:
            print("numero non positivo ripetere l operazione....")
      case 3:#lista di numeri
        #creiamo una lista vuota e prendiamo l input per la grandezza della lista
        allNumber = []
        nList = int(input("Quanti numeri vuoi inserire? "))
        #iteriamo per riempire la lista
        for i in range(nList):
          nTemp = float(input("Inserisci un numero--> "))
          allNumber.append(nTemp)
        #stampiamo il quadrato
        for s in allNumber:
          print(f"Il numero nella lista e {s} ---> {pow(s,2)} il quadrato.")
      case 4:#lista dell utente
        #creiamo una lista vuota e prendiamo l input per la grandezza della lista
        allNumber = []
        nList = int(input("Quanti numeri vuoi inserire? "))
        #iteriamo per riempire la lista
        for i in range(nList):
          nTemp = float(input("Inserisci un numero--> "))
          allNumber.append(nTemp)
        #controlliamo se la lista e piena
        if len(allNumber) > 0:
          #stampiamo il numero massimo
          print(f"Il numero massimo della lista e: {max(allNumber)} e ci sono {len(allNumber)} elementi nella lista")
          #controlliamo quanti valori ci sono
          cont = 0
          indice = 0
          while indice < len(allNumber):
            if isinstance(allNumber[indice], (int, float)):  # Controlla se è numero
              cont += 1
            indice += 1
          print(f"Ci sono {cont} numeri nella lista.")
        else:
          print("la lista e vuota...")
    
    #domanda per ritornare al menu
    b = True if input("Vuoir tornare al menu? s/n ---> ").lower().strip() == "s" else False
  print("Fine programma")
except ValueError:
  print("Per favore, inserisci un numero valido!")
  

