# prt 1
# Hai 60 min per creare un esercizio che rappresenti tutto quello che hai imparato nella settimana precedente, 
# riprendi la tabella delle conoscenze per maggiori info.

#useremo le funzioni per dividere tutti i macro argomenti

# Decoratore per misurare il tempo di esecuzione di una funzione
import time

def misura_tempo(func):
    #Decorator che misura il tempo di esecuzione di una funzione.
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tempo di esecuzione di {func.__name__}: {end_time - start_time:.4f} secondi")
        return result
    return wrapper

# Funzione per lavorare con variabili di base
@misura_tempo
def variabili_base():
    #Chiede all'utente un testo e un numero, poi li stampa.
    testo = input("Inserisci un testo: ") 
    numero = int(input("Inserisci un numero: "))
    print(f"Testo = {testo}, Numero = {numero}")

# Funzione per dimostrare l'uso di if-else
@misura_tempo
def condizionali():
    #Esempio di utilizzo di un'istruzione if-else.
    numero = int(input("Inserisci un numero: "))
    if numero > 0:
        print("Il numero è positivo.")
    elif numero < 0:
        print("Il numero è negativo.")
    else:
        print("Il numero è zero.")

# Funzione per dimostrare il ciclo while
@misura_tempo
def ciclo_while():
    #Esempio di ciclo while per contare fino a un numero dato dall'utente.
    numero = int(input("Inserisci un numero positivo: "))
    contatore = 0
    while contatore <= numero:
        print(contatore)
        contatore += 1

# Funzione per dimostrare il ciclo for con liste
@misura_tempo
def ciclo_for_liste():
    #Esempio di utilizzo del ciclo for per scorrere una lista.
    lista = ["Mela", "Banana", "Ciliegia", "Dattilo"]
    for frutto in lista:
        print(frutto)

# Funzione per dimostrare il ciclo for con range
@misura_tempo
def ciclo_for_range():
    #Esempio di utilizzo del ciclo for con range.
    for i in range(1, 6):  # Stampa numeri da 1 a 5
        print(i)

# Funzione per lavorare con insiemi
@misura_tempo
def operazioni_insiemi():
    #Esegue operazioni sugli insiemi come unione, intersezione e differenza.
    set_a = {1, 2, 3}
    set_b = {3, 4, 5}
    
    print("Unione:", set_a | set_b)
    print("Intersezione:", set_a & set_b)
    print("Differenza:", set_a - set_b)
    print("Differenza Simmetrica:", set_a ^ set_b)

# Chiamata alle funzioni per la dimostrazione simulando un menu
print("Inizio dimostrazione: ")
while True:
  ch = int(input("--- Menu --- \n 1) Variabili base \n 2) Condizionali \n 3) Ciclo whilw \n 4) Ciclo for liste \n 5) Ciclo for range \n 6) Operazioni insieme \n 0) exit \n ---> "))
  match ch:
    case 1:
      variabili_base()
    case 2:
      condizionali()
    case 3:
      ciclo_while()
    case 4:
      ciclo_for_liste()
    case 5:
      ciclo_for_range()
    case 6:
      operazioni_insiemi()
    case _:
      break
  print("------")#print estetico
print("\n--- Fine dimostrazione ---")
