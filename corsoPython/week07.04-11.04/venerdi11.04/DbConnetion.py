import mysql.connector

def db_connection(db_name):
  # Dati di accesso al server MySQL (senza specificare il database)
  conn = mysql.connector.connect(
      host="localhost",
      user="root",
      password=""
  )
  cursor = conn.cursor()

  # Controlla se il database esiste
  cursor.execute("SHOW DATABASES")
  db_exists = False
  for (database,) in cursor:
      if database == db_name:
          db_exists = True
          break

  # Se non esiste, lo crea
  if not db_exists:
      cursor.execute(f"CREATE DATABASE {db_name}")
      print(f"Database '{db_name}' creato.")
  else:
      print(f"Database '{db_name}' già esistente.")

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

  print(f"Connesso al database '{db_name}' con successo.")
  return myDB