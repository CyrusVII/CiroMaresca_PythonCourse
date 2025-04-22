# ES analisi recap su NumPY
# Andare a creare un piccolo sistema di analisi dei dati SU un DB che deve essere e collegare almeno 3 tabelle
# relazionale
# generato tabelle.
# Ci dev'essere un menu per eseguire principali funzioni che hai

import sqlite3
import numpy as np

# === CREAZIONE DB E TABELLE ===
def crea_database():
  conn = sqlite3.connect('analisi.db')
  cur = conn.cursor()
  # Crea tabelle
  cur.execute('''CREATE TABLE IF NOT EXISTS stati (
    id INTEGER PRIMARY KEY,
    nome TEXT
  )''')
  
  cur.execute('''CREATE TABLE IF NOT EXISTS clienti (
  id INTEGER PRIMARY KEY,
  nome TEXT,
  eta INTEGER,
  id_stato INTEGER,
  FOREIGN KEY(id_stato) REFERENCES stati(id)
  )''')

  cur.execute('''CREATE TABLE IF NOT EXISTS prodotti (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    prezzo REAL
  )''')

  cur.execute('''CREATE TABLE IF NOT EXISTS ordini (
    id INTEGER PRIMARY KEY,
    id_cliente INTEGER,
    id_prodotto INTEGER,
    quantita INTEGER,
    FOREIGN KEY(id_cliente) REFERENCES clienti(id),
    FOREIGN KEY(id_prodotto) REFERENCES prodotti(id)
  )''')

  conn.commit()
  conn.close()

# === INSERIMENTO DATI DI TEST ===
def popola_database():
  conn = sqlite3.connect('analisi.db')
  cur = conn.cursor()

  stati = [('Italia',), ('Germania',), ('Francia',)]
  cur.executemany("INSERT INTO stati (nome) VALUES (?)", stati)
  
  clienti = [('Mario', 30), ('Luisa', 25), ('Giovanni', 45)]
  prodotti = [('Laptop', 1200.50), ('Mouse', 25.00), ('Tastiera', 45.75)]
  ordini = [(1, 1, 2), (2, 2, 1), (3, 1, 1), (1, 3, 1)]

  cur.executemany("INSERT INTO clienti (nome, eta) VALUES (?, ?)", clienti)
  cur.executemany("INSERT INTO prodotti (nome, prezzo) VALUES (?, ?)", prodotti)
  cur.executemany("INSERT INTO ordini (id_cliente, id_prodotto, quantita) VALUES (?, ?, ?)", ordini)

  conn.commit()
  conn.close()

# === ANALISI VENDITE TOTALI ===
def analisi_vendite():
  conn = sqlite3.connect('analisi.db')
  cur = conn.cursor()

  cur.execute('''
    SELECT prodotti.prezzo, ordini.quantita
    FROM ordini
    JOIN prodotti ON ordini.id_prodotto = prodotti.id
  ''')

  dati = np.array(cur.fetchall())
  conn.close()
  ricavi = dati[:, 0] * dati[:, 1]
  print("\n-- ANALISI VENDITE --")
  print("Totale ricavi: €", np.sum(ricavi))
  print("Ricavo medio per ordine: €", np.mean(ricavi))
  print("Ricavo massimo per ordine: €", np.max(ricavi))
  
# === ANALISI VENDITE SINGOLI PRODOTTI ===
def analisi_vendite_prodotto():
  conn = sqlite3.connect('analisi.db')
  cur = conn.cursor()

  cur.execute('''
    SELECT prodotti.nome, prodotti.prezzo, ordini.quantita
    FROM ordini
    JOIN prodotti ON ordini.id_prodotto = prodotti.id
  ''')

  dati = np.array(cur.fetchall())
  conn.close()

  # Conversione dei tipi (prezzo e quantita)
  nomi = dati[:, 0]
  prezzi = dati[:, 1].astype(float)
  quantita = dati[:, 2].astype(int)
  ricavi = prezzi * quantita

  # Trova i nomi unici dei prodotti
  prodotti_unici = np.unique(nomi)
  print("\n-- ANALISI VENDITE PER PRODOTTO ---")
  for prodotto in prodotti_unici:
    mask = nomi == prodotto
    ricavo_totale = np.sum(ricavi[mask])
    print(f"{prodotto}: €{ricavo_totale:.2f}")

# === ETA MEDIA CLIENTI / ETA MIN - ETA MAX ===
def analisi_eta_clienti():
  conn = sqlite3.connect('analisi.db')
  cur = conn.cursor()

  cur.execute('''
    SELECT eta
    FROM clienti
  ''')

  dati = np.array(cur.fetchall())
  conn.close()
  media_eta = np.mean(dati)
  
  print("\n--- ANALISI ETA CLIENTI ---")
  print(f"Età media clienti: {media_eta:.0f}")
  print(f"Eta massima: {np.max(dati)}")
  print(f"Eta minima: {np.min(dati)}")

# === ASSEGNA STATO ===
def assegna_stato_cliente():
  conn = sqlite3.connect('analisi.db')
  cur = conn.cursor()

  # Seleziona i clienti senza stato
  cur.execute('SELECT id, nome FROM clienti WHERE id_stato IS NULL')
  clienti_senza_stato = np.array(cur.fetchall())

  if clienti_senza_stato.size == 0:
    print("Tutti i clienti hanno già uno stato assegnato!")
    conn.close()
    return

  print("\nClienti senza stato:")
  for id_, nome in clienti_senza_stato:
    print(f"{id_}. {nome}")

  try:
    id_cliente = int(input("\nSeleziona l'ID del cliente da aggiornare (0 per annullare): ").strip())
  except ValueError:
    print("Input non valido!")
    conn.close()
    return

  if id_cliente == 0:
    print("Operazione annullata.")
    conn.close()
    return

  # Verifica ID valido 
  if not np.any(clienti_senza_stato[:, 0].astype(int) == id_cliente):
    print("ID cliente non valido!")
    conn.close()
    return

  # Seleziona gli stati
  cur.execute('SELECT id, nome FROM stati')
  stati = np.array(cur.fetchall())

  if stati.size == 0:
    print("Nessuno stato disponibile!")
    conn.close()
    return

  print("\nStati disponibili:")
  for id_, nome in stati:
    print(f"{id_}. {nome}")

  try:
    id_stato = int(input("\nSeleziona l'ID dello stato da assegnare: ").strip())
  except ValueError:
    print("Input non valido!")
    conn.close()
    return

  # Verifica ID stato valido con NumPy
  if not np.any(stati[:, 0].astype(int) == id_stato):
    print("ID stato non valido!")
    conn.close()
    return

  # Esegui aggiornamento
  cur.execute('UPDATE clienti SET id_stato = ? WHERE id = ?', (id_stato, id_cliente))
  conn.commit()
  conn.close()

  print(f"Stato assegnato correttamente al cliente ID {id_cliente}.")

# === ANALISI VENDITE PER  STATO ===
def analisi_per_stato():
  conn = sqlite3.connect('analisi.db')
  cur = conn.cursor()

  cur.execute('''
    SELECT stati.nome, prodotti.prezzo, ordini.quantita
    FROM ordini
    JOIN clienti ON ordini.id_cliente = clienti.id
    JOIN stati ON clienti.id_stato = stati.id
    JOIN prodotti ON ordini.id_prodotto = prodotti.id
  ''')

  dati = np.array(cur.fetchall())
  conn.close()

  nomi_stati = dati[:, 0]
  prezzi = dati[:, 1].astype(float)
  quantita = dati[:, 2].astype(int)
  ricavi = prezzi * quantita

  print("\n--- ANALISI VENDITE PER STATO ---")
  for stato in np.unique(nomi_stati):
    mask = nomi_stati == stato
    ricavo_totale = np.sum(ricavi[mask])
    print(f"{stato}: €{ricavo_totale:.2f}")
    
# === MENU PRINCIPALE ===
def menu():
  while True:
    print("\n--- MENU ---")
    print("1. Analizza Vendite")
    print("2. Analisi vendite singolo prodotto")
    print("3. Analisi eta dei clienti")
    print("4. Assegna stati")
    print("5. Analisi vendite per stato")
    print("6. Esci")
    ch = input("Scegli un'opzione: ").strip()
    
    match ch:
      case "1":
        analisi_vendite()
      case "2":
        analisi_vendite_prodotto()
      case "3":
        analisi_eta_clienti()
      case "4":
        assegna_stato_cliente()
      case "5":
        analisi_per_stato()
      case "6":
        print("Uscita.")
        break

# === AVVIO ===
if __name__ == "__main__":
  #Creo e popolo il db per avere datyi fitizzi da analizzare
  crea_database()
  popola_database()
  #Avvio il programma
  menu()
