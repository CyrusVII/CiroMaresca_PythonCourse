
#scelta utente
ch = int(input("Scegli cosa vuoi fare: \n1) Conto alla rovescia \n2) Troviamo i numeri primi e pari \n0) Esci dal programma\n--->"))
#funzioni utili
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

match ch:
  case 0:
    print("arrivederci...")
  case 1:
    n = int(input("Inserisci numero: "))
    while n >= 0:#ciclo per print
      print(n)
      n -= 1
  case 2:
    # Lista per memorizzare i numeri primi
    primes = []
    even = []

    while len(primes) < 5 and len(even) < 5:  # Si ferma quando ha 5 numeri primi e 5 numeri pari
        try:
            # Chiedi all'utente di inserire un numero
            number = int(input("Inserisci un numero: "))
            
            # Controllo numeri primi
            if len(primes) < 5:
                if isPrime(number):
                    primes.append(number)  # Aggiungi il numero primo alla lista
                    print(f"{number} è un numero primo!")
                else:
                    print(f"{number} non è un numero primo!")

            print("------")  # Print estetico

            # Controllo numeri pari
            if len(even) < 5:
                if isEven(number):
                    even.append(number)  # Aggiungi il numero pari alla lista
                    print(f"{number} è un numero pari!")
                else:
                    print(f"{number} non è un numero pari!")

            print(f"-----\nHai inserito {len(primes)}/5 numeri primi e {len(even)}/5 numeri pari\n-----")
        
        except ValueError:
            print("Per favore, inserisci un numero valido!")
  case _:
    print("Scelta non valida arrivederci...")




