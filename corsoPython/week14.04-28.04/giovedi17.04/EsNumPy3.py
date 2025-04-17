import numpy as np

# 1. Crea una matrice 2D di dimensioni 6x6 contenente numeri interi casuali tra 1 e 100
matrice_originale = np.random.randint(0, 101, size=(6, 6))
# 2. Estrai la sotto-matrice centrale 4x4 dalla matrice originale
sottomatrice_centrale = matrice_originale[1:5, 1:5].copy()
# 3. Inverti le righe della matrice estratta (cioè, la prima riga diventa l'ultima, la seconda diventa la penultima, e così via)
matrice_invertita = np.flipud(sottomatrice_centrale)
# 4. Estrai la diagonale principale della matrice invertita e crea un array 1D contenente questi elementi
diagonale_principale = np.diagonal(matrice_invertita)
# 5. Sostituisci tutti gli elementi della matrice invertita che sono multipli di 3 con il valore -1
matrice_invertita[matrice_invertita % 3 == 0] = -1

# 6. Stampa tutte le matrici richieste
print("Matrice Originale:")
print(matrice_originale)

print("\nSotto-matrice Centrale 4x4:")
print(sottomatrice_centrale)

print("\nMatrice Invertita (righe invertite):")
print(matrice_invertita)

print("\nDiagonale Principale della Matrice Invertita:")
print(diagonale_principale)

print("\nMatrice Invertita Modificata (multipli di 3 sostituiti con -1):")
print(matrice_invertita)


import sqlite3
def crea_db():
  conn = sqlite3.connect("scuola.db")
  cursor = conn.cursor()

  # Crea la tabella
  cursor.execute("""
  CREATE TABLE IF NOT EXISTS voti (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nome TEXT,
      matematica INTEGER,
      fisica INTEGER,
      informatica INTEGER
  )
  """)

  # Inserisce dati di esempio
  dati_studenti = [
      ("Marco", 87, 75, 91),
      ("Lucia", 92, 88, 96),
      ("Giovanni", 78, 82, 85),
      ("Elena", 84, 79, 89),
      ("Simone", 67, 73, 70)
  ]

  cursor.executemany("INSERT INTO voti (nome, matematica, fisica, informatica) VALUES (?, ?, ?, ?)", dati_studenti)

  # Salva e chiude
  conn.commit()
  conn.close()
  
def esegui():
  #esempio con cattura da db
  
  crea_db()
  # Connessione al database
  conn = sqlite3.connect('scuola.db')
  cursor = conn.cursor()

  # Eseguo la query per prendere i voti
  cursor.execute("SELECT matematica, fisica, informatica FROM voti")
  risultato = cursor.fetchall()

  # Converto il risultato in array NumPy
  voti_array = np.array(risultato)

  print("Array dei voti:")
  print(voti_array)

  # Chiudo la connessione
  conn.close()

esegui()