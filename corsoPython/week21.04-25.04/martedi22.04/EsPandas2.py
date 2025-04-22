# Esercizio 2: Manipolazione e Aggregazione dei Dati
# Obiettivo: Approfondire le capacità di manipolazione e aggregazione dei dati con pandas.
# Dataset: Utilizzare un dataset che registra le vendite di prodotti in diverse città, includendo le colonne Prodotto, Quantità, Prezzo Unitario e Città.
# 1. Caricare i dati in un DataFrame.
# 2. Aggiungere una colonna "Totale Vendite" che sia il risultato del prodotto tra Quantità e Prezzo Unitario.
# 3. Raggruppare i dati per Prodotto e calcolare il totale delle vendite per ciascun prodotto.
# 4. Trovare il prodotto più venduto in termini di Quantità.
# 5. Identificare la città con il maggior volume di vendite totali.
# 6. Creare un nuovo DataFrame che mostri solo le vendite superiori a un certo valore (es., 1000 euro).
# 7. Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine decrescente.
# 8. Visualizzare il numero di vendite per ogni città.

import pandas as pd
import numpy as np

# Aggiunta colonna "Totale Vendite"
def add_column_tot_sales(df):
  df['Totale Vendite'] = df['Quantita'] * df['Prezzo Unitario']

# Raggruppa per prodotto e somma le vendite
def products_group(df):
  print("--- Group for products ---")
  print(df.groupby('Prodotto')[['Totale Vendite']].sum())

# Prodotto che ha venduto più pezzi
def product_max_sales(df):
  temp = df.groupby('Prodotto')[['Quantita']].sum()
  # Trova il prodotto con il maggior numero di pezzi venduti
  prodotto_top = temp['Quantita'].idxmax()
  vendite_top = temp['Quantita'].max()
  print("--- Prodotto più venduto ---")
  print(f"{prodotto_top} con {vendite_top} pezzi venduti")

# 5. Identificare la città con il maggior volume di vendite totali
def city_max_sales(df):
  temp = df.groupby('Citta')[['Totale Vendite']].sum()
  city_top = temp['Totale Vendite'].idxmax()
  sales_top = temp['Totale Vendite'].max()
  print("--- Città con maggiori vendite ---")
  print(f"{city_top} con €{sales_top:.2f} di vendite totali")

# 6. Creare un nuovo DataFrame che mostra solo le vendite superiori a un certo valore (ad esempio, 1000 euro)
def filter_sales_above(df, value):
  filtered_df = df[df['Totale Vendite'] > value]
  print(f"--- Vendite superiori a {value} euro ---")
  print(filtered_df)

# 7. Ordinare il DataFrame per la colonna "Totale Vendite" in ordine decrescente
def sort_by_sales(df):
  sorted_df = df.sort_values(by='Totale Vendite', ascending=False)
  print("--- DataFrame ordinato per Totale Vendite ---")
  print(sorted_df)

# 8. Visualizzare il numero di vendite per ogni città
def sales_by_city(df):
  city_sales = df.groupby('Città')[['Quantita']].sum()
  print("--- Numero di vendite per ogni città ---")
  print(city_sales)
  
#9 pivot personalizzato
def personalize_pivot(df):
  print("\n--- Personalizza la tua Pivot Table ---")
  
  # Mostra le colonne disponibili con numerazione
  print("Colonne disponibili:")
  columns_list = df.columns.tolist()
  for i, col in enumerate(columns_list, start=1):
    print(f"{i}. {col}")
  
  try:
    def choise():
      return int(input(f"Scegli un numero (1-{len(columns_list)}): ").strip())
  
    # Chiedi all'utente di scegliere la colonna da utilizzare come 'index'
    print("\nScegli la colonna da utilizzare come 'index':")
    index_choice = choise()
    index_col = columns_list[index_choice - 1]
    
    # Chiedi all'utente di scegliere la colonna da utilizzare come 'columns'
    print("\nScegli la colonna da utilizzare come 'columns':")
    columns_choice = choise()
    columns_col = columns_list[columns_choice - 1]
    
    # Chiedi all'utente di scegliere la colonna da utilizzare come 'values'
    print("\nScegli la colonna da utilizzare come 'values':")
    values_choice = choise()
    values_col = columns_list[values_choice - 1]
    
    # Chiedi all'utente quale funzione di aggregazione usare
    aggfunc = input("Scegli la funzione di aggregazione ('sum', 'mean', 'count'): ").strip()

    # Crea la pivot table
    pivot_df = df.pivot_table(values=values_col, index=index_col, columns=columns_col, aggfunc=aggfunc)

    # Stampa la pivot table
    print("\n--- Pivot Table Personalizzata ---")
    print(pivot_df)
    
  except Exception as e:
    print("Error ---> ", e)
    
def menu():
  # Liste di riferimento
  prodotti = ['Mouse', 'Tastiera', 'Monitor', 'Webcam']
  città = ['Roma', 'Milano', 'Napoli', 'Torino', 'Bologna']

  # Numero di righe da generare
  num_righe = 15

  # Generazione casuale dei dati
  dati = {
      'Prodotto': np.random.choice(prodotti, size=num_righe),
      'Quantita': np.random.randint(1, 6, size=num_righe),  # da 1 a 5 inclusi
      'Prezzo Unitario': np.round(np.random.uniform(15.0, 1000.0, size=num_righe), 2),
      'Citta': np.random.choice(città, size=num_righe)
  }
  
  df = pd.DataFrame(dati)
  add_column_tot_sales(df)
  
  while True:
    print("--- Menu ---")
    print('0. Exit')
    print('1. Stampa df originale')
    print('2. Per prodotto con tot vendite')
    print('3. Prodotto che ha venduto di piu')
    print('4. Città con maggiori vendite')
    print('5. Filtra vendite superiori a 1000 euro')
    print('6. Ordina per vendite')
    print('7. Numero di vendite per ogni città')
    print('8. Pivot personalizzato')
    
    ch = input("---> ")
    match ch:
      case '0':
        print('Fine...')
        break
      case '1':
        print("---- Ecco i dati -----\n", df)
      case '2':
        products_group(df)
      case '3':
        product_max_sales(df)
      case '4':
        city_max_sales(df)
      case '5':
        filter_sales_above(df, 1000)
      case '6':
        sort_by_sales(df)
      case '7':
        sales_by_city(df)
      case '8':
        personalize_pivot(df)
        
if __name__ == "__main__":
  menu()