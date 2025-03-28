# #creare una serie di condizioni una dentro l'altra che a fronte di un unput per ogni id decidano se farti passare o no(3livelli, fate un paragone ==)
# #input dati
# lung = len(input("inserisci una frase"))
# #controlli di livello
# if(lung > 1):
#   print("la frase ha piu di un carattere ,1 livello")#liv1
#   if(lung > 10):
#     print("la frase e piu lunga di 10 caratteri, 2 livello")#liv2
#     if(lung > 20):
#       print("la frase e piu lunga di 20 caratteri, 3 livello")#liv3
# else:
#   print("frase troppo corta")#else

# #andare a creare un if con vari elif e un else che gestisca un menu per la selezione di un crud basilare(aggiungi rimuovi elimina)
# #su una lista di stringe

# #dichiarazione e stampa lista
# lista = ["peppe","pippo","la","coca"]
# print(f"ecco la tua lista {lista}")

# #cattura input scelta
# select = input("scegli se aggiungere,rimuovere un elemento o eliminare la lista, digita(a/r/e): ")
# if(select == "a"):
#   lista.append(input("digita cosa aggiungere: "))
# elif(select == "r"):
#   lista.pop(int(input("digita il numero dell elemento da togliere contando da 0: ")))
# elif(select == "e"):
#   lista.clear()
# else:
#   print("Scelta non disponibile")#else
# #stampa lista aggiornata
# print(f"ecco la lista aggiornata{lista}")

#creare un if con else dentro l if inserire una stuttura di creazione di dati(nome, pass, id dato del sistema a crescere)
#e nell else il controllo automatico la dove e presente l account nel sistema e solo se si passa dall else concludere lo script

accounts = [[1,'ciro', 'pippo']]  # Account predefinito
nextId = 1

# Creazione di un nuovo account o accesso
scelta = input("Vuoi creare un nuovo account? (s/n): ").lower()

if scelta == 's':
    nome = input("Inserisci il tuo nome: ").lower()  # Convertiamo a minuscolo
    password = input("Inserisci la tua password: ").lower() 
    # Creazione del nuovo account
    nuovoAccount = [nextId, nome, password]
    accounts.append(nuovoAccount)
    
    print(f"Account creato con successo! ID assegnato: {nextId}")
    nextId += 1
else:
    nome = input("Inserisci il tuo nome per l'accesso: ").lower()  # Convertiamo a minuscolo
    password = input("Inserisci la tua password: ").lower()  
    
    # Verifica degli account manualmente senza cicli
    accountTrovato = None
    # Primo account
    if nome in accounts[0] and password in accounts[0]:
        accountTrovato = accounts[0]

    # Verifica dell'account trovato
    if accountTrovato is not None:
        print(f"Accesso riuscito. Benvenuto {accountTrovato[1]} (ID: {accountTrovato[0]}).")
    else:
        print("Account non trovato o password errata.")


