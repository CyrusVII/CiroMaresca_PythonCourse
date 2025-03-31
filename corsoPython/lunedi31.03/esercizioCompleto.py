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

#funzioni 
#funzione numero pari
def numEven(n):
    return f"Il numero {n} è pari" if n % 2 == 0 else f"Il numero {n} è dispari"

#funzione inserimento lista
def listInsert(nList, allNumber):
    for _ in range(nList):
        allNumber.append(int(input("Inserisci un numero: ")))

#funzione conta interi
def contInt(allNumber):
    print(f"Nella lista ci sono {len(set(allNumber))} numeri unici")

# inizio main
try:
    # var per il while
    b = True
    while b:
        taskNumber = int(input("Quante task vuoi fare: "))
        taskList = []
        
        # raccogliamo le scelte dell'utente in una lista
        for _ in range(taskNumber):
            taskList.append(int(input("-----\nCosa vuoi fare:\n1) Vediamo se il numero è pari \n2) Conto alla rovescia \n3) Calcoliamo il quadrato \n4) Gioco lista\n0) Abbandona \n---> ")))
        
        # eseguiamo le task in sequenza
        for task in taskList:
            match task:
                case 0:  # case di uscita
                    print("Arrivederci")
                    break
                case 1:  # primo esercizio troviamo un numero positivo
                    n = int(input("Inserisci un numero --> "))
                    print(numEven(n))
                case 2:  # contiamo alla rovescia
                    n = int(input("Inserisci un numero positivo --> "))
                    if n > 0:
                        for i in range(n, -1, -1):
                            print(i)
                    else:
                        print("Numero non positivo, ripetere l'operazione...")
                case 3:  # lista di numeri
                    # creiamo una lista vuota e prendiamo l'input per la grandezza della lista
                    allNumber = []
                    nList = int(input("Quanti numeri vuoi inserire? "))
                    # iteriamo per riempire la lista
                    listInsert(nList, allNumber)
                    # stampiamo il quadrato
                    for s in allNumber:
                        print(f"Il numero nella lista è {s} ---> {pow(s,2)} il quadrato.")
                case 4:  # lista dell'utente
                    # creiamo una lista vuota e prendiamo l'input per la grandezza della lista
                    allNumber = []
                    nList = int(input("Quanti numeri vuoi inserire? "))
                    # iteriamo per riempire la lista
                    listInsert(nList, allNumber)
                    # controlliamo se la lista è piena
                    if allNumber:
                        # stampiamo il numero massimo
                        print(f"Il numero massimo della lista è: {max(allNumber)} e ci sono {len(allNumber)} elementi nella lista")
                        # controlliamo quanti valori ci sono
                        contInt(allNumber)
                    else:
                        print("La lista è vuota")
        
        # domanda per ritornare al menu
        b = True if input("Vuoi tornare al menu? s/n ---> ").lower().strip() == "s" else False

    print("Fine programma")
except ValueError:
    print("Per favore, inserisci un numero valido!")