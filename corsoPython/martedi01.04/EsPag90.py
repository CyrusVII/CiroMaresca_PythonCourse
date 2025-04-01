# Descrizione: Scrivi un programma che chieda all'utente di inserire un numero intero positivo n. Il programma deve poi eseguire le seguenti operazioni:
# 1. Utilizzare un ciclo while per garantire che l'utente inserisca un numero positivo. Se l'utente inserisce un numero negativo o zero, il programma deve 
# continuare a chiedere un numero fino a quando non viene inserito un numero positivo.
# 2. Utilizzare un ciclo for con range per calcolare e stampare la somma dei numeri pari da 1 a n.
# 3. Utilizzare un ciclo for per stampare tutti i numeri dispari da 1 a n.
# 4. Utilizzare una struttura if per determinare se n è un numero primo. Un numero primo è divisibile solo per 1 e per se stesso. Il programma deve 
# stampare se n è primo o no.

#funzione per inserire un numero intero positivo
def insertInt():
    while True:
        try:
          #input utente
            n = int(input("Inserisci un numero intero: "))
            #controllo se e un numero intero
            if n >= 0:
                return n
            else:
                print("Per favore, inserisci un numero positivo!")
        except ValueError:
            print("Per favore, inserisci un numero valido!")
            
#funzione per trovare numeri pari e dispari
def evenShotsNumber(even,shots,r):
  for i in range(1,r):
    if(i%2 == 0):
      even.append(i)
    else:
      shots.append(i)
      
#funzione per individurare un numero primo
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Chiamata alla funzione
n = insertInt()
evenNumber = []
shotsNumber = []
evenShotsNumber(evenNumber,shotsNumber,n)
print(f" Ecco i numeri Pari da 1 a {n}: {evenNumber}\n Ecco i numeri dispari da 1 a {n}: {shotsNumber}")
print(f"Il numero {n} inserito da te e un numero primo? {isPrime(n)}")


