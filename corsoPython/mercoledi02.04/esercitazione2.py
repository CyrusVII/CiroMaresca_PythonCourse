
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

#found book title
def found_book(bookListAv,bookId):
    # Troviamo il libro corrispondente nell'elenco dei libri disponibili
    for book in bookListAv:
        if book[0] == bookId:
            # Stampiamo il titolo del libro
            return {book[1]}
     
# Funzione per prenotare un libro
def take_book(userBookList, bookListAv, id):
    print("--- Prenotazione di un libro ---")
    # Visualizza i libri disponibili
    print("Libri disponibili:")
    for book in bookListAv:
        if book[2] > 0:  # Se il libro ha copie disponibili
            print(f"ID: {book[0]} - Titolo: {book[1]} - Copie disponibili: {book[2]}")

    # Selezione del libro
    bookId = int(input("Inserisci l'ID del libro che desideri prenotare: "))
    for book in bookListAv:
        if book[0] == bookId and book[2] > 0:
            # Prenotiamo il libro
            book[2] -= 1  # Riduciamo la disponibilità del libro
            # Aggiungiamo il libro alla lista dei libri posseduti dall'utente
            for userBook in userBookList:
                if userBook[0] == id:
                    userBook.append(bookId)
                    print(f"Libro '{book[1]}' prenotato con successo!")
                    return
            # Se l'utente non ha ancora prenotato nulla
            userBookList.append([id, bookId])
            print(f"Libro '{book[1]}' prenotato con successo!")
            return
    print("ID libro non valido o nessuna copia disponibile.")

#funzione per posare un libro
def back_book(userBookList, bookListAv, id):
    print("--- Ritorna un libro ---")
    
    # Trova i libri posseduti dall'utente
    user_books = None
    for book in userBookList:
        if book[0] == id:
            user_books = book  # Salviamo la lista dei libri posseduti dall'utente
            break

    if not user_books or len(user_books) == 1:
        print("Non hai libri da restituire.")
        return
    
    print("Libri disponibili per la restituzione:")
    for i in range(1, len(user_books)):  # Partiamo dall'elemento 1
        print(f"{user_books[i]} - {found_book(bookListAv, user_books[i])}")

    try:
        ch = int(input("Inserisci l'ID del libro da restituire: "))
    except ValueError:
        print("Errore: Devi inserire un numero.")
        return
    
    if ch not in user_books[1:]:  # Controlliamo che il libro sia effettivamente in possesso dell'utente
        print("Non hai questo libro.")
        return
    
    # Aggiorniamo la disponibilità del libro nella lista principale
    for book in bookListAv:
        if book[0] == ch:
            book[2] += 1  # Aumentiamo la disponibilità
            break
    
    #aggiorniamo lista utenteLibri
    for book in userBookList:
        if book[0] == id:
            book.remove[ch]
            break
    
    print("Libro restituito con successo.")

    
#funzione per vedere i dati dell utente
def view_user_date(userList,userBookList,id,bookListAv):
     #stampiamo il nome dell utente e i relativi dati 
    print(f"Benvenuto {userList[id][0]} ecco i libri in tuo possesso:")
    # Ciclo per stampare i libri posseduti dall'utente
    for userBook in userBookList:
        if userBook[0] == id:  # Se l'ID dell'utente corrisponde
            # Otteniamo l'ID del libro 
            n = len(userBook)-1
            for i in range(n):
              bookId = userBook[i+1]
              print(found_book(bookListAv,bookId))
   

#creiamo una funzione per il menu
def menu(sessionId):
    #while per ciclare fintato che l utente vuole fare qualcosa
    while True:
        #stampa del menu con presa input
        ch = int(input("--- Menu --- \n 1) Visulizza i tuoi dati \n 2) Prenota libro \n 3) Restituisci libro \n 4) Logout \n ---> "))
        match ch:
            case 1:
                view_user_date(userList,userBookList,sessionId,bookListAvalible)
            case 2: 
                take_book(userBookList,bookListAvalible,sessionId)
            case 3:
                back_book(userBookList,bookListAvalible,sessionId)
            case 4:
                print("Exit programm")
                sys.exit()
            case _:
                print('Caso non valido...')
        if input("Vuoi continuare? (s/n) ---> ").lower().strip() == "n":
            break

#dichiarazioni var
userList = [["Cyrus","Pippo123!"]]
#creo una lista dei libri disponibili id,titolo,copi
bookListAvalible = [[0,"Viaggio al centro della terra",10],[1,"La sauna",7]]
#creo una lista di libri posseduti da un utente idUser,Idbook,idBook
userBookList = [[0,0,1]]
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
            menu(sessionId)
        case False:
            print('Problemi con l accesso')
            
main()