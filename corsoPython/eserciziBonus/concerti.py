#creiamo la registrazione utente ogni utente deve prima registrarsi con nome e password
#poi deve fare un login e per aggiungere concerti deve inserire una passowrd
#creazioni concerti per utente con inserimento pass "GHIBLI" massimo tre concerti "idUser nomeConcerto posti"
#possibilita per un utente di prenotare un concerto

#import 
import re

#registrazione utente
def register_user(userList):
    # Regex per validazione password
    regex = r"^(?=.*[A-Z])(?=.*\d)(?=.*[?!])[A-Za-z\d?!]{8,}$"
    print("--- Benvenuto registriamoci ---")
    while True:
        # Inseriamo il nome utente
        userName = input("Inserisci un nome utente: ")

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
        
        # controllo utente
        for i in userList:
          for s in userList:
            if s[0] == userName and s[1] == userPassword:
              print("Accesoo riuscito")
              return userList.index(s)
            else:
              print("Accesso non riuscito riprova...")

#creiamo la gestione della creazione dei concerti
def add_event(eventList):
    pass


#dichiarazioni var
userList = [["Cyrus","Pippo123!"]]
concerti = [[1 , "nome concerto", 10]]
eventList = []
#funzione main per far partire tutto
def main():
    #simuliamo un session token che sara la posizione della lista nella lista
    sessionId = -1
    #chiediamo se ha un account
    haveAccount = True if input("Hai un account? (s/n) ---> ").lower().strip() == "s" else False
    match haveAccount:
        case True:
            sessionId = login_user(userList)
        case False:
            register_user(userList)
            sessionId = login_user(userList)
            
    if sessionId > -1:
        pass

#avviamo il programma chiamando il main
main()