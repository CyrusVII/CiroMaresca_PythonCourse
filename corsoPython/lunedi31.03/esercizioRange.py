# 1.Base / Numeri pari e dispari o sequenza Descrizione:
# Scrivi un programma che chiede all'utente di inserire un numero o una stringa scegliendo prima quale. Il programma dovrebbe determinare se 
# il numero è pari o dispari e stampare il risultato e se deve ripetere o stampare e poi ripetere.
# 2.Intermedio/ Numeri primi in un intervallo :
# Chiedi all'utente di inserire due numeri che definiscono un intervallo (es 10 e 50). Il programma dovrebbe stampare tutti i numeri primi compresi in
# quell'intervallo o i numeri non primi o entrambi divisi a tua scelta, salvandoli in due aggregazioni differenti e chiedere se deve ripetere
# 3. Avanzato/ Fattori comuni Descrizione:
# Chiedi all'utente di inserire due numeri. Il programma dovrebbe determinare e stampare i 
# fattori comuni di entrambi i numeri. Se non ci sono fattori comuni oltre 1, dovrebbe stampare "I numeri sono coprimi".
# La stessa cosa ma anche per due stringhe (.equal) e chiedere se deve ripetere ma sono complementari" solo se hanno tutte le lettere in comune (es:abs/ sab)

#import 
import math

#funzione inserimento di un numero
def numInsert():
  return int(input("Inserisci un numero intero: "))

#funzione calcolo numeri primi
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#funzione stampa liste
def printList(l):
  for s in l:
    print(s, end=",")#usiamo end per fare una stampa lineare
    
#funzione fattori comuni
def commonFactorsFound(a, b):
    mcd = math.gcd(a, b)  # Trova il massimo comune divisore
    return [i for i in range(1, mcd + 1) if mcd % i == 0] #trova i fattori comuni
  
#funzione stringe complementari
def complementarWorld(st1,st2):
  #controlliamo se l utente a inserito due parole uguali
  if st1 != st2:
    print(f"Le due parole {st1} e {st2} sono complementari") if sorted(st1) == sorted(st2) else print(f"Le due parole {st1} e {st2} non sono complementari")
  else:
    print("Le due stringe sono la stessa parola")

try:
  while True:
    #menu di scelta
    ch = int(input("----- Menu -----\n 1) Trova pari e dispari \n 2) Intervallo numeri primi \n 3) Fattori comuni numeri \n 4) Fatttori comuni stringe \n ---> "))
    print("-----")#print estetico
    
    #match per le scelte
    match ch:
      
      case 1:#case numero pari
        while True: #while per ripetere operazione
          #facciamo scegliere a un utente cosa inserire
          n = numInsert() if input("Vuoi inserire un intero o una stringa? (i/s) ---> ").lower().strip() == "i" else input("Inserisci numero in formato stringa ---> ")
          print(f"Il numero {n} e pari") if int(n)%2 == 0 else print(f"il numero {n} e dispari") #printiamo il risultato
          #facciamo scegliere all utente se rifare il calcolo o no
          if input("Vuoi trovare un altro numero pari? (s/n) ---> ").lower().strip() == "n":
            break
          
      case 2:#case numeri primi
        #dichiarazione liste
        prime = []
        notPrime = []
        #l utenter inserisce due numeri
        print("\n---- Adesso inserirai i due numeri che comoppranno il range di controllo. es(da 1 a 50) -----")
        n1 = numInsert()
        n2 = numInsert() + 1
        #usiamo la funzione per controllare con un ciclo che itera per i due numeri
        for i in range(n1, n2, 1):
          prime.append(i) if isPrime(i) else notPrime.append(i)
        #stampiamo le liste
        print(f"Ecco i numeri primi trovati nel range:")
        printList(prime)
        print("")
        print(f"Ecco i numeri non primi trovati nel range:")
        printList(notPrime)
        print("")
        
      case 3: #fattori comuni numeri
        #lista fattori comuni
        commonFactor = None
        #prendiamo i numeri in input
        n1 = numInsert()
        n2 = numInsert()
        #usiamo la funzione
        commonFactor = (commonFactorsFound(n1,n2))
        #controlliamo se hanno fattori comuni oltre a 1
        if len(commonFactor) > 1:
          print(f"i fattori comuni di {n1} e {n2} sono: {commonFactor}")
        else:
          print("I numeri sono comprimi")
      
      case 4:#stringe complementari
        #prendiamo i dati dell utente
        st1 = input("inserisci la prima parola: ").strip()
        st2 = input("inserisci la seconda parola: ").strip()
        complementarWorld(st1,st2) #usiamo la funzione per la complementarita
        
    #sceltqa utente per tornare al menu
    if input("Vuoi tornare al menu? (s/n) --> ").lower().strip() == "n":
      print("Chiusura programma....")
      break
    print("------")
        
    
except ValueError:
    print("Per favore, inserisci un numero valido!")