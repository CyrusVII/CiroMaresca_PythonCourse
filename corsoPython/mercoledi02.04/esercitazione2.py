
# Es riassuntivo prt 2
# Andiamo ora a creare un sistema di funzioni che richiami tutte le singole parti che abbiamo creato nel precedente esercizio, 
# devono essere usate SOLO funzioni e almeno da 2 decoratori ed essere ripetibile.
#import 
import re
import sys
import time

#registrazione utente
def register_user(userList):
    # Regex per validazione password
    regex = r"^(?=.*[A-Z])(?=.*\d)(?=.*[?!])[A-Za-z\d?!]{8,}$"
    print("--- Benvenuto registriamoci ---")
    while True:
        # Inseriamo il nome utente
        userName = input("Inserisci un nome utente: ")
        time.sleep(2)#simuliamo il tempo di accesso
        # Controllo se il nome utente è già presente
        nome_gia_esistente = False
        for sotto_lista in userList:
            for utente in sotto_lista:
                if utente[0] == userName:
                    print("Nome utente già esistente, scegline un altro.")
                    nome_gia_esistente = True
                    break
            if nome_gia_esistente:
                break

        if not nome_gia_esistente:
            break  # Se il nome utente non esiste, usciamo dal ciclo

    # Validazione della password
    while True:
        password = input("Inserisci una password valida: ")
        time.sleep(2)#simuliamo il tempo di accesso
        if re.match(regex, password):
            print("Password valida!")
            break
        else:
            print("Password non valida. Deve contenere almeno 8 caratteri, una maiuscola, un numero e un carattere speciale tra ? e !. Riprova.")

    # Salviamo l'utente nella lista
    userList.append([[userName, password]])
    print("Registrazione completata con successo!")

#login utente
def login_user(userList):
    print("--- Benvenuto entra nel tuo account ---")
    while True:
        # Inserimento del nome utente
        userName = input("Inserisci il tuo nome utente: ")
        userPassword = input("Inserisci la tua password: ")
        
        time.sleep(2)#simuliamo il tempo di accesso
        # controllo utente
        for i in userList:
          for s in userList:
            if s[0] == userName and s[1] == userPassword:
              print("Accesoo riuscito")
              return userList.index(s)
            else:
              print("Accesso non riuscito riprova...")

#creiamo una funzione per il menu
def menu():
    #stampa del menu con presa input
    ch = int(input("--- Menu --- \n 1) Visulizza i tuoi dati \n 2) Prenota libro \n 3) Restituisci libro \n 4) Logout"))
    #while per ciclare fintato che l utente vuole fare qualcosa
    while True:
        match ch:
            case 1:
                pass
            case 2: 
                pass
            case 3:
                pass
            case 4:
                print("Exit programm")
                sys.exit()
            case _:
                print('Caso non valido...')
        if input("Vuoi continuare? (s/n) ---> ").lower().strip() == "n":
            break

#dichiarazioni var
userList = [["Cyrus","Pippo123!"]]
#funzione main per far partire tutto
def main():
    #simuliamo un session token che sara la posizione della lista nella lista
    sessionId = -1
    #chiediamo se ha un account
    while sessionId < 0:
        haveAccount = True if input("Hai un account? (s/n) ---> ").lower().strip() == "s" else False
        match haveAccount:
            case True:
                sessionId = login_user(userList)
            case False:
                register_user(userList)
                sessionId = login_user(userList)
    
    #controllo se l id di sessione se e valido
    match sessionId > -1:
        case True:
            menu()
        case False:
            print('Problemi con l accesso')