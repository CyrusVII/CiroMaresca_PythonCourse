#se devo modifcare la struttura basta execute se devo gestire la struttura commit se devo catturare i dati fetch

# Importa il modulo mysql.connector, che permette di connettersi a un database MySQL da Python
import mysql.connector

# Crea una connessione al database MySQL
# Specifica i parametri: host (server), user (nome utente), password
# In questo esempio, si connette a un server MySQL in locale (localhost) con l'utente 'root' e nessuna password
myDB = mysql.connector.connect(
  host = "localhost",   # Indirizzo del server MySQL (localhost = stesso computer)
  user = "root",        # Nome utente per accedere a MySQL
  password = "",       # Password associata all'utente (qui è vuota)
  #port = #porta se usi una porta personalizzata (di default è 3306, quindi questa riga può essere omessa se non si usa una porta diversa)
  database = "corsoPython" #per accedere a un db specifico
)

# Crea un oggetto cursor, che serve per eseguire comandi SQL sul database
myCursor = myDB.cursor() 

# Definisce una query SQL per creare un nuovo database chiamato "corsoPython"
queryCreate = "CREATE DATABASE corsoPython"
# Esegue la query SQL usando il cursor
#myCursor.execute(queryCreate)

# Definisce una query SQL per elencare tutti i database presenti nel server MySQL
queryShowDb = "SHOW DATABASES"
## Esegue la query usando il cursor
#myCursor.execute(queryShowDb)
## Itera attraverso i risultati della query e stampa ciascun database trovato
# for db in myCursor:
#   print(db)

# Definisce una query SQL per creare una tabella chiamata "utenti"
# La tabella avrà:
# - ID: intero, chiave primaria, con incremento automatico
# - NAME: campo di tipo VARCHAR (fino a 50 caratteri) per il nome
# - INDIRIZZO: campo di tipo VARCHAR (fino a 50 caratteri) per l'indirizzo
queryCreateTable = "CREATE TABLE utenti(ID int AUTO_INCREMENT PRIMARY KEY, NAME VARCHAR(50), ADRESS VARCHAR(50))"
## Esegue la query per creare la tabella "utenti"
#myCursor.execute(queryCreateTable)
## Definisce una query per mostrare tutte le tabelle presenti nel database selezionato
#queryShowTb = "SHOW TABLES"
## Esegue la query per ottenere l'elenco delle tabelle
#myCursor.execute(queryShowTb)
## Itera attraverso i risultati e stampa il nome di ogni tabella
#for db in myCursor:
#  print(db)

# Definisce una query SQL per inserire un nuovo utente nella tabella 'utenti'
# I campi specificati sono NAME e ADRESS (ID verrà assegnato automaticamente)
queryInsertUtenti = "INSERT INTO utenti(NAME, ADRESS) VALUES(%s, %s)"
## Dati dell'utente da inserire: nome e indirizzo
#val = ("Ciro", "Via Roma")
## Esegue l'inserimento dei dati usando il cursore
#myCursor.execute(queryInsertUtenti, val)
## Salva le modifiche al database (rende permanente l'inserimento)
#myDB.commit()
## Stampa quante righe sono state inserite con successo (dovrebbe essere 1)
#print(myCursor.rowcount, "righe inserite!")

#in cas l id non fosse settato su auto increment esempio di alter table
queryAlterTbUtenti = "ALTER TABLE utenti MODIFY ID AUTO_INCREMENT"
# myCursor.execute(queryAlterTbUtenti)

#per passare piu valori alla volta
queryInsertUtenti1 = "INSERT INTO utenti(NAME, ADRESS) VALUES(%s, %s)"
# Dati dell'utente da inserire: nome e indirizzo
val = [("Pippo", "Via Roma"),
       ("Maria","Via napoli")]
# Esegue l'inserimento di piu dati usando il cursore
myCursor.executemany(queryInsertUtenti1, val)
# Salva le modifiche al database (rende permanente l'inserimento)
myDB.commit()#per l invio dei dati
# Stampa quante righe sono state inserite con successo (dovrebbe essere 1)
print(myCursor.rowcount, "righe inserite!")
print("Ultimo ID inserito", myCursor.lastrowid)
#versione come funzione
def insertManyRow(dati):
  queryInsertUtenti1 = "INSERT INTO utenti(NAME, ADRESS) VALUES(%s, %s)"
  myCursor.executemany(queryInsertUtenti1,dati)
  myDB.commit()
  
  print(myCursor.rowcount, "righe inserite!")
  print("Ultimo ID inserito", myCursor.lastrowid)
  
#funzione per leggere piu rige
def readRows():
  query = "select * from utenti"
  myCursor.execute(query)
  result = myCursor.fetchall()#fetch per la cattura dei dati
  for row in result:
    print(row)
    
readRows()

#funzione per leggere una riga
def readRow():
  query = "select * from utenti"
  myCursor.execute(query)
  result = myCursor.fetchone()
  print(result)

readRow()

myDB.close()#per chiudere la conessione

