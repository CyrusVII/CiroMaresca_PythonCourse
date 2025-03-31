#chiedere all utente di inserire un numero. il programma dovrebbe fare un conto alla rovescia a partire da quel numero fino a zero stampando ogni
#numero 

#input utente
# n = int(input("Inserisci numero: "))
# while n >= 0:#ciclo per print
#   print(n)
#   n -= 1
  
#chiedi all utente di inserire un numero il programma dovrebbe controllare se il numero inserito e primo/pari o no se e primo lo salva
#e lo stampa il numero e primo altrimenti stampa il numero non e primo si ferma il tutto quando ha 5 numeri

#funzione per controllare numero primo
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Lista per memorizzare i numeri primi
primes = []

while len(primes) < 5:  # Si ferma quando ha 5 numeri primi
    try:
        # Chiedi all'utente di inserire un numero
        number = int(input("Inserisci un numero: "))
        
        if isPrime(number):
            primes.append(number)  # Aggiungi il numero primo alla lista
            print(f"{number} è un numero primo!")
        else:
            print(f"{number} non è un numero primo!")
        
    except ValueError:
        print("Per favore, inserisci un numero valido!")

# Stampa tutti i numeri primi trovati
print("\nNumeri primi trovati:", primes)
