# Definizione di un decoratore chiamato "decorator"
def decorator(funzione):
    # Definiamo una funzione interna chiamata "wrapper", che avvolge la funzione originale
    def wrapper():
        print("Prima dell'esecuzione della funzione")  # Messaggio prima di eseguire la funzione originale
        funzione()  # Chiamata alla funzione originale
        print("Dopo l'esecuzione della funzione")  # Messaggio dopo aver eseguito la funzione originale
    return wrapper  # Restituiamo la funzione "wrapper" senza eseguirla

# Usiamo il decoratore sopra la funzione "saluta"
@decorator  # Equivalente a: saluta = decorator(saluta)
def saluta():
    print('Ciao!')  # Questa è la funzione originale che vogliamo decorare

# Chiamiamo la funzione "saluta"
#saluta()  # In realtà, ora esegue "wrapper", che stampa i messaggi prima e dopo "saluta"

# Definizione di un decoratore che può accettare argomenti
def decorator_con_argomenti(funzione):
    # La funzione wrapper accetta argomenti variabili (sia posizionali che keyword)
    def wrapper(*args, **kwargs):
        print("Prima")  # Messaggio prima di chiamare la funzione originale
        risultato = funzione(*args, **kwargs)  # Chiama la funzione originale con gli argomenti passati
        #print(args[0]," + ",args[1]) #per prendere il valore di un singolo elemento che viene passato alla funzione
        print("Dopo")  # Messaggio dopo aver eseguito la funzione originale
        #print(risultato)
        #risultato += 2
        return risultato  # Restituisce il risultato della funzione originale
    return wrapper  # Restituiamo la funzione wrapper, che avvolge la funzione originale

# Decoriamo la funzione "somma" usando il decoratore sopra definito
@decorator_con_argomenti  # Questo è equivalente a: somma = decorator_con_argomenti(somma)
def somma(a, b):
    return a + b  # Funzione che restituisce la somma di due numeri

# Chiamiamo la funzione decorata "somma" con due argomenti
#print(somma(3, 4))  # Il risultato della somma è 7, ma prima e dopo vengono stampati i messaggi
#somma(4,3)

#esempio 3
import time  # Importiamo il modulo time per misurare il tempo

# Definizione del decoratore che misura il tempo di esecuzione
def tempo_di_esecuzione(funzione):
    # La funzione wrapper avvolge la funzione originale e misura il tempo
    def wrapper(*args, **kwargs):
        # Tempo di inizio prima di eseguire la funzione
        inizio = time.time()
        
        print("Esecuzione della funzione in corso...")
        
        # Eseguiamo la funzione originale con gli argomenti
        risultato = funzione(*args, **kwargs)
        
        # Tempo di fine dopo che la funzione è stata eseguita
        fine = time.time()
        
        # Calcoliamo il tempo di esecuzione
        tempo = fine - inizio
        
        print(f"La funzione ha impiegato {tempo:.5f} secondi per essere eseguita.")
        
        return risultato  # Restituiamo il risultato della funzione originale
    return wrapper  # Restituiamo la funzione wrapper che misura il tempo

# Decoriamo la funzione "esempio_funzione" con il decoratore tempo_di_esecuzione
@tempo_di_esecuzione
def esempio_funzione():
    # Simuliamo un'operazione che richiede tempo, come un calcolo complesso
    time.sleep(2)  # Pausa di 2 secondi per simulare un'attività lunga
    print("Funzione completata!")

# Chiamiamo la funzione decorata per vedere quanto tempo impiega
esempio_funzione()




