# Pandas
# Esercizio 1: Analisi Esplorativa dei Dati
# Obiettivo: Familiarizzare con le operazioni di base per l'esplorazione dei dati usando pandas.
# Dataset: Utilizzare un dataset di esempio che include le seguenti informazioni su un gruppo di persone: Nome, Età, Città e Salario.
# 1. Caricare i dati in un DataFrame autogenerandoli casualmente
# 2. Visualizzare le prime e le ultime cinque righe del DataFrame. 3. Visualizzare il tipo di dati di ciascuna colonna.
# 4. Calcolare statistiche descrittive di base per le colonne numeriche (media, mediana, deviazione standard).
# 5. Identificare e rimuovere eventuali duplicati.
# 6. Gestire i valori mancanti sostituendoli con la mediana della rispettiva colonna.
# 7. Aggiungere una nuova colonna chiamata "Categoria Età" che classifica le persone come "Giovane", "Adulto" o "Senior" 
# basandosi sull'età (es., 0-18 anni: Giovane, 19-65 anni: Adulto, oltre 65 anni: Senior).
# 8. Salvare il DataFrame pulito in un nuovo file CSV.
import pandas as pd
file_path = 'MyCsv/dati_persone.csv'

def take_data():
  df = pd.read_csv(file_path)
  
  # Gestire i valori mancanti sostituendoli con la mediana della colonna
  df['Età'] = df['Età'].fillna(df['Età'].median())
  df['Salario'] = df['Salario'].fillna(df['Salario'].median())
  
  # Per le colonne testuali possiamo scegliere di riempirle con una stringa placeholder
  df['Nome'] = df['Nome'].fillna("Sconosciuto")
  df['Città'] = df['Città'].fillna("Non specificata")
  
  # Visualizzare le prime e le ultime cinque righe
  print("Prime 5 righe:\n", df.head())
  print("\nUltime 5 righe:\n", df.tail())

  # Visualizzare il tipo di dati di ciascuna colonna
  print("\nTipi di dati:\n", df.dtypes)

  # Statistiche descrittive per le colonne numeriche
  print("\nStatistiche descrittive:\n", df.describe().round(2))
  
  # Rimuoviamo duplicati
  df = df.drop_duplicates()
  
  # Funzione per modificare l eta
  def classifica_eta(eta):
    if eta <= 18:
        return 'Giovane'
    elif eta <= 65:
        return 'Adulto'
    else:
        return 'Senior'
  
  # Comando per modificare l eta
  df['Categoria Età'] = df['Età'].apply(classifica_eta)
  
  # Salvare il DataFrame pulito in un nuovo file CSV
  df.to_csv('MyCsv/dati_persone_pulito.csv', index=False)

# Eseguo il tutto
take_data()