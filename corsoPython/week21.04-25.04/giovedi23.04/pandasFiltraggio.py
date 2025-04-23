import pandas as pd

# Dati di esempio
data = {
  'Nome' : ['Alice', 'Bob' , 'Carla'],
  'Eta' : [25,30,22],
  'Citta' : ['Roma', 'Milano', 'Npaoli']
}
df = pd.DataFrame(data)

# Selezione di una colonna
ages = df['eta']
# Filtraggio basato su una condizione
adults = df[df['eta'] >= 18]

# Ordinamento dati per eta
df_sorted = df.sort_values(by='eta')
# Unione di un dataframe
merge_df = pd.merge(df,df_sorted, on = 'nome')

# Applicazione di una funzione a una colonna
df['eta_doppia'] = df['eta'].apply(lambda x: x*2)

# Esportazione DataFrame in csv
df.to_csv("data_output.csv")