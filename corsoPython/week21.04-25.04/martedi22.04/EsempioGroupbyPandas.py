import pandas as pd  # Importa la libreria pandas

# Dati di esempio sotto forma di dizionario
data = {
    'Data': ['2021-01-01', '2021-01-01','2021-01-01', '2021-01-02', '2021-01-02'],
    'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
    'Prodotto': ['Mouse', 'Tastiera', 'Mouse', 'Tastiera', 'Mouse'], 
    'Vendite': [100, 200, 150, 300, 250]  # Valori di vendita
}

# 1. Creazione del DataFrame a partire dai dati
df = pd.DataFrame(data)
print("DataFrame normale")
print(df)

# 2. Raggruppamento per 'Prodotto' e somma dei valori numerici (in questo caso solo 'Vendite')
#grouped_df = df.groupby('Prodotto').sum() facendo solo cosi incatena anche le stringe creando una cosa non proprio bella da vedere
grouped_df = df.groupby('Prodotto')[['Vendite']].sum()

# 3. Visualizzazione del DataFrame raggruppato
print("\nGrouped df")
print(grouped_df)
