# Scenario: Devi scrivere un programma Python che simuli un sistema di login. Il sistema deve permettere 
# all'utente di inserire un nome utente e una password. Poi, deve verificare se la combinazione di nome utente e password è corretta. 
# Per semplicità, puoi hardcodare nel codice una coppia di nome utente e password che sia considerata corretta. Requisiti:
# 1.Input dell'Utente:
# • Il programma chiede all'utente di inserire il nome utente.
# • Poi, chiede all'utente di inserire la password.
# 2. Verifica delle Credenziali:
# • Il programma controlla se il nome utente e la password inseriti corrispondono a quelli predefiniti.
# • Puoi decidere di avere le credenziali hardcoded nel codice per questo esercizio. Ad esempio, puoi usare "admin" come nome utente e "12345" come password.
# 3. Output del Programma:
# • Se il nome utente e la password sono corretti, stampa un messaggio di benvenuto.
# • Altrimenti, informa l'utente che le credenziali sono errate.
# 4. Modifica dati del Programma:
# • Inserisci una condizione interna che si occupi di cambiare un dato specifico tra quelli inseriti
# O
# Appena loggato fai scegliere fra due opzioni di domanda segreta e la risposta ( qual'è il colore preferito, quale animale preferito )

accounts = [[1,'ciro', 'pippo','cane','lebuche','mirko']]  # Account predefinito
nextId = 1
#inserimento dati utente
nome = input("Inserisci il tuo nome per l'accesso: ").lower()  # Convertiamo a minuscolo
password = input("Inserisci la tua password: ").lower()  
    
# Verifica degli account 
accountTrovato = None
# Primo account controllo
if nome in accounts[0] and password in accounts[0]:
    accountTrovato = accounts[0]
    select = input("Scegli la tua domanda di sicurezza (a,b,c): ").lower()
    dom = None
    #domande di sicurezza
    match select:
      case 'a':
        dom = input('Che animale ti piace? ')
      case 'b':
        dom = input('Cosa ti piace di roma? ')
      case 'c':
        dom = input('Chi e il tuo prof preferito? ')
    #controllo domanda di sicurezza
    if dom in accounts[0]:
      print(f"-----\nAccesso riuscito. Benvenuto {accountTrovato[1]} (ID: {accountTrovato[0]}).")
      request = int(input('che dato dell account vuoi cambiare nome/password/domanda 1/domanda 2/domanda3(un numero da 1 a 5)? '))
      #match per cambio dei dati
      match request:
        case 1:
          accounts[0][1] = input("inserisci nuovo nome: ")
        case 2:
          accounts[0][2] = input("inserisci nuova password: ")
        case 3:
          accounts[0][3] = input("inserisci nuovo animale: ")
        case 4:
          accounts[0][4] = input("inserisci cosa ti piace di roma: ")
        case 5:
          accounts[0][5] = input("inserisci il tuo prof preferito: ")
      print(f"ecco i dati aggiornati: \n{accounts}")
else:
  print("Account non trovato o password errata.")#fine programma
        