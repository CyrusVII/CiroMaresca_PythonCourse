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
  
#funzione numeri pari
def isEven(n):
  if n % 2 == 0:
    return True
  return False

# Lista per memorizzare i numeri primi
primes = []
even = []

while len(primes) < 5 and len(even) < 5:  # Si ferma quando ha 5 numeri primi
    try:
        # Chiedi all'utente di inserire un numero
        number = int(input("Inserisci un numero: "))
        
        if( len(primes) < 5):
          if isPrime(number):
              primes.append(number)  # Aggiungi il numero primo alla lista
              print(f"{number} è un numero primo!")
          else:
              print(f"{number} non è un numero primo!")
        
        print("------")#print estetico
        
        #controllo pari
        if( len(even) < 5):
          if isEven(number):
              even.append(number)  # Aggiungi il numero pari alla lista
              print(f"{number} è un numero pari!")
          else:
              print(f"{number} non è un numero pari!")
              
        print(f"-----\n hai inserito {len(primes)}/5 numeri primi e {len(even)}/5 numeri dispari\n-----")
              
    except ValueError:
        print("Per favore, inserisci un numero valido!")

# Stampa tutti i numeri primi trovati
print("\nNumeri primi trovati:", primes)

