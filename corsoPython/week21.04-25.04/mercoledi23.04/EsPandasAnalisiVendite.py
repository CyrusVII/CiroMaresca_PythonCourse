# Esercizio 1: Analisi di Vendite Fittizie
# Obiettivo: Utilizzare pandas per analizzare un set di dati di vendite generato casualmente, applicando le tecniche di pivot e groupby.
# Descrizione: Gli studenti dovranno generare un DataFrame di vendite che include i seguenti campi: "Data", "Città", "Prodotto" e "Vendite". 
# I date devono essere generati per un periodo di un mese, con vendite registrate+ per tre diverse città e tre tipi di prodotti.
# 1. Generazione dei Dati: Utilizzare numpy per creare un set di dati casuali.
# 2. Creazione della Tabella Pivot: Creare una tabella pivot per analizzare le vendite medie di ciascun prodotto per città.
# 3. Applicazione di GroupBy: Utilizzare il metodo groupby per calcolare le vendite totali per ogni prodotto.

import pandas as pd
import numpy as np
import re
from datetime import datetime, timedelta

class SalesUtils:

  @staticmethod
  def generate_data():
    prodotti = ['Mouse', 'Tastiera', 'Monitor', 'Webcam']
    città = ['Roma', 'Milano', 'Napoli', 'Torino', 'Bologna']
    num_righe = 15

    inizio = datetime(2024, 1, 1)
    oggi = datetime.today()
    date_casuali = [inizio + timedelta(days=np.random.randint(0, (oggi - inizio).days)) for _ in range(num_righe)]

    prodotti_scelti = np.random.choice(prodotti, size=num_righe)
    quantità = np.random.randint(1, 6, size=num_righe)
    prezzo_unitario = np.round(np.random.uniform(15.0, 1000.0, size=num_righe), 2)
    città_scelte = np.random.choice(città, size=num_righe)
    vendite = np.round(quantità * prezzo_unitario, 2)

    df = pd.DataFrame({
        'Data': date_casuali,
        'Città': città_scelte,
        'Prodotto': prodotti_scelti,
        'Vendite': vendite
    })

    return df
  
  @staticmethod
  def pivot_sales(df: pd.DataFrame):
    pivot = pd.pivot_table(
        df,
        values='Vendite',
        index='Prodotto',
        columns='Città',
        aggfunc='mean'
    )
    print("\n--- Tabella Pivot: Vendite Medie ---\n", pivot)
    SalesUtils.save_data(pivot)
    
  @staticmethod
  def group_by_product(df: pd.DataFrame):
    totale = df.groupby('Prodotto')['Vendite'].sum()
    print("\n--- Vendite Totali per Prodotto ---\n", totale.reset_index())
    SalesUtils.save_data(totale)
  
  @staticmethod
  def is_valid_filename(self,name: str) -> bool:
    filename_regex = r'^(?!^(PRN|AUX|NUL|CON|COM[1-9]|LPT[1-9])(\..*)?$)[^<>:"/\\|?*\s][^<>:"/\\|?*]{0,253}[^<>:"/\\|?*.\s]$'
    return re.match(filename_regex, name) is not None
  
  @staticmethod
  def save_data(df: pd.DataFrame):
    #scelta se vuoi salvare il file
    print("Vuoi salvare il file? (s/n)")
    sc = input("---> ").strip().lower()
    
    #anullamento salvataggio
    if sc != 's':
      print("Salvataggio annullato.")
      return

    #scelta tipo di formato
    print("Scegli il formato di salvataggio:")
    print("1. CSV")
    print("2. Excel (XLSX)")
    print("3. JSON")
    formato = input("Inserisci il numero del formato desiderato: ").strip()
    
    #scelta nome file con controllo
    while True:
      filename = input("Inserisci il nome del file (senza estensione): ").strip()
      if not SalesUtils.is_valid_filename(filename):
            print("Nome file non valido! Controlla la sintassi del nome del file.")
            continue
      break
    
    #match per il dalvataggio
    match formato:
      case '1':
        df.to_csv(f"{filename}.csv", index=False)
        print(f"File salvato come {filename}.csv")
      case '2':
        df.to_excel(f"{filename}.xlsx", index=False)
        print(f"File salvato come {filename}.xlsx")
      case '3':
        df.to_json(f"{filename}.json", orient='records', indent=2)
        print(f"File salvato come {filename}.json")
      case _:
        print("Formato non valido. Salvataggio annullato.")

# === MENU ===
def menu():
  df = SalesUtils.generate_data()
  while True:
    try:
      print("--- Menu ---")
      print('0. Exit')
      print('1. Stampa df originale')
      print('2. Pivot vendite medie')
      print('3. Group by')
      print('4. Salva df originale')

      ch = input("---> ")
      match ch:
        case '0':
          print('Fine programma...')
          break
        case '1':
          print("--- DataFrame ---\n", df)
        case '2':
          SalesUtils.pivot_sales(df)
        case '3':
          SalesUtils.group_by_product(df)
        case 4:
          SalesUtils.save_data(df)

    except Exception as e:
      print("Errore: ", e)

if __name__ == "__main__":
  menu()