import pandas as pd

#percorso del file csv
file_path = 'MyCsv/sales_data.csv'

#caricamento dati nel dataFrame
df = pd.read_csv(file_path)

#le prime righe del dataFrame per confermare
#print(df.head())

# === ESEMPIO 2 ===
#creazione di un dataFrame con dati di esempio
data = {
  'Nome' : ['Alice', 'Bob' , 'Carla'],
  'Eta' : [25,30,22],
  'Citta' : ['Roma', 'Milano', 'Npaoli']
}
df = pd.DataFrame(data)

#Stampa del DataFrame originale
print('DataFrame Originale: \n',df)

#Selezione delle righe dove l eta e superiore a 23
#andando a creare quindi un df solo con le persone con eta superiore a 23
df_older = df[df['Eta'] > 23]
#stampa righe selezionate
print("\nPersone con eta superiore a 23: \n", df_older)

#aggiungiamo una nuova colonna la persona magiorenne
df['Magiorenne'] = df['Eta'] > 17
#stampa DataFrame con nuova colonna
print('\nDataFrame con colonna Magiorenne: \n',df)
# Esempio di stampa finale :
# DataFrame con colonna Magiorenne:
#      Nome  Eta   Citta  Magiorenne
# 0  Alice   25    Roma        True
# 1    Bob   30  Milano        True
# 2  Carla   22  Npaoli        True