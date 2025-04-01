# Scrivi un programma che esegua le seguenti operazioni:
# 1. Chiedi all'utente di inserire un numero intero positivo n. Se l'utente inserisce un numero negativo o zero, 
# continua a chiedere un numero fino a quando non viene inserito un numero positivo.
# 2. Genera una lista di numeri interi casuali tra 1 e n (incluso). La lunghezza della lista deve essere n.
# 3. Utilizza un ciclo for per calcolare e stampare la somma dei numeri pari nella lista.
# 4. Utilizza un ciclo for per stampare tutti i numeri dispari nella lista.
# 5. Utilizza una funzione per determinare se un numero è primo. La funzione deve restituire True se il numero è primo, altrimenti False.
# 6. Utilizza un ciclo for per stampare tutti i numeri primi nella lista.
# 7. Infine, utilizza una struttura if per determinare se la somma di tutti i numeri nella lista è un numero primo e stampa il risultato

import random

# Funzione per inserire un numero intero positivo
def insert_int():
    while True:
        try:
            n = int(input("Inserisci un numero intero che determinerà il range di creazione della lista: "))
            if n > 0:
                return n
            else:
                print("Per favore, inserisci un numero positivo maggiore di zero!")
        except ValueError:
            print("Per favore, inserisci un numero valido!")

# Funzione per generare una lista con numeri randomici dalla lista originale
def random_list(randomList, numberList, n):
    numRandomCiclo = random.randint(1, n)  # Numero casuale di elementi da selezionare
    for _ in range(numRandomCiclo):
        numR = random.choice(numberList)  # Seleziona un numero casuale dalla lista originale
        randomList.append(numR)

# Funzione per trovare numeri pari e dispari
def even_shots_number(randomList):
    evenTotal = sum(i for i in randomList if i % 2 == 0)  # Somma dei numeri pari
    shotsList = [i for i in randomList if i % 2 != 0]  # Lista dei numeri dispari
    print(f"La somma dei numeri pari nella lista è: {evenTotal}\nI numeri dispari nella lista sono: {shotsList}")
    
#trova i primi
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#gira l array
def check_prime_list(numbers):
    prime_results = {num: is_prime(num) for num in numbers}
    print("I numeri primi sono: ")
    for num, result in prime_results.items():
        print(f"{num}: {result}")
        
#somma numeri nella lista
def list_total(numbers):
  total = 0
  for i in numbers:
    total += i
  if(is_prime(total)):
    print(f"\nLa somma dei numeri nella lista e un numero primo: {total}")
  else:
    print(f"\nLa somma dei numeri nella lista non e un numero primo: {total}")
    

# Chiamata alla funzione principale
n = insert_int()
numberListComplete = list(range(1, n + 1))
numerRandomList = []

random_list(numerRandomList, numberListComplete, n)
print(f"La lista random è: {numerRandomList}\n-----")

# Analizza i numeri pari e dispari
even_shots_number(numerRandomList)

#troviamo i primi
check_prime_list(numerRandomList)

#troviamo il totale primo
list_total(numerRandomList)

