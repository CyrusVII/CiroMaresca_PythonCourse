import mysql.connector

def db_connection(db_name):
  try:
    # Dati di accesso al server MySQL (senza specificare il database)
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    cursor = conn.cursor()

    # Crea il database solo se non esiste già
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    #print(f"Database '{db_name}' verificato/creato.")

    # Chiude la connessione iniziale
    cursor.close()
    conn.close()

    # Ora ti connetti al database specifico
    myDB = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database=db_name
    )
    return myDB#,True
  except:
    pass#"Errore di conessione",False