# 1. Esercizio Base: Indovina il numero
# Descrizione: Scrivi un programma che genera un numero casuale tra 1 e 100 (inclusi). 
# L'utente deve indovinare quale numero è stato generato. Dopo ogni tentativo, il programma dovrebbe dire all'utente se il numero da 
# indovinare è più alto o più basso rispetto al numero inserito. Il gioco termina quando l'utente indovina il numero o decide di uscire.
# 2. Esercizio Avanzato: Sequenza di Fibonacci fino a N Descrizione: Chiedi all'utente di inserire un numero N. Il programma dovrebbe stampare 
# la sequenza di Fibonacci fino a N. Ad esempio, se l'utente inserisce 100, il programma dovrebbe stampare tutti i numeri della sequenza di 
# Fibonacci minori o uguali 100.
# Chat

#funzione indovina il numero
import random
def found_the_number():
  try:
    n = random.randint(1, 100)
    while True:
      ch = int(input("Indovina il numero da 1 a 100: "))
      print("Il numero e piu alto ") if ch > n else print("il numero e piu basso")
      if input("Vuoi proseguire s/n ---> ").lower().strip() == "n":
        break
  except ValueError:
            print("Per favore, inserisci un numero valido!")
            
# Funzione per generare la sequenza di Fibonacci fino a N
def fibonacci_found(n):
    sequenza = []
    a, b = 0, 1
    while a <= n:
        sequenza.append(a)
        a, b = b, a + b
    return sequenza
      
#inizio while per il menu      
while True:
  #try per il controllo degli interi
  try:
    #l utente sceglie cosa fare
    ch = int(input("---Menu---\n 1) Indovina il numero \n 2) Fibonacci \n ---> "))
    
    #match che gestisce la scelta dell utente
    match ch:
      
      case 1:
        found_the_number()
        
      case 2: 
        n = int(input("Inserisci un numero intero ---> "))
        sequenza = fibonacci_found(n)
        print(f"La sequenza e: {sequenza}")
      case _:
        print("Scelta non valida222")
        
    #domanda per tornare al menu
    if input("Vuoi proseguire s/n ---> ").lower().strip() == "n":
      break
  except ValueError:
            print("Per favore, inserisci un numero valido!")