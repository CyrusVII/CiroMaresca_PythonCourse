import pandas as pd
import numpy as np  # Importa la libreria NumPy, utile per gestire valori numerici e NaN

# === ESEMPIO 3 ===

# Creazione di un dizionario con dati di esempio per il DataFrame
data = {
  'Nome' : ['Alice', 'Bob' , 'Carla', 'Bob', 'Carla', 'Alice', None],  # Colonna con nomi, inclusi duplicati e un valore mancante (None)
  'Eta' : [25, 30, 22, 30, np.nan, 25, 29],  # Colonna con età, incluso un valore mancante (np.nan)
  'Citta' : ['Roma', 'Milano', 'Napaoli', 'Milano', 'Napaoli', 'Roma', 'Roma']  # Colonna con città
}

# Creazione del DataFrame a partire dal dizionario
df = pd.DataFrame(data)

# Stampa del DataFrame originale con i dati non ancora puliti
print('DataFrame Originale: \n', df)

# Rimozione delle righe duplicate (basata su tutte le colonne)
df = df.drop_duplicates()

# Gestione dei dati mancanti
# Rimozione delle righe che contengono almeno un valore mancante (NaN o None)
df_cleaned = df.dropna()

# Sostituzione dei valori mancanti nella colonna 'Eta' con la media della colonna stessa
# Nota: questa riga genera un FutureWarning, è meglio usare: df['Eta'] = df['Eta'].fillna(df['Eta'].mean())
df['Eta'].fillna(df['Eta'].mean(), inplace=True)

# Stampa del DataFrame "pulito", dove sono state eliminate tutte le righe con dati mancanti
print("\nDataFrame dopo la pulizia: \n", df_cleaned)

# Stampa del DataFrame dove i dati mancanti nella colonna 'Eta' sono stati sostituiti con la media
print("\nDataFrame con dati mancanti sostituiti: \n", df)


