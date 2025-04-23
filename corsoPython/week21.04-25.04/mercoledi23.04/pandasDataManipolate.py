import pandas as pd

# Crea una sequenza di date che parte dal '2021-01-01', con 10 periodi, ognuno di un mese
data_range = pd.date_range(start='2021-01-01', periods=10, freq='M')

# Crea un DataFrame di esempio con dei dati casuali e usa la sequenza di date come indice
df = pd.DataFrame({
    'data': range(10)  # Alcuni dati di esempio per il DataFrame
}, index=data_range)

# Risampiona i dati per mese ('M') e calcola la media per ogni mese
df_resampled = df.resample('M').mean()  # Risampiona per mese e calcola la media

# Stampa il DataFrame risampionato
print(df_resampled)  # Stampa il DataFrame risampionato



# Converte la colonna 'date' in formato datetime
df['date'] = pd.to_datetime(df['date'], format='%y-%m-%d')
# 'date' ora è una colonna di tipo datetime

# Imposta la colonna 'date' come indice del DataFrame
df.index = pd.to_datetime(df['date'])
# Ora il DataFrame ha un indice di tipo DatetimeIndex basato sulla colonna 'date'

# Resampling: calcolare la media giornaliera
df_daily = df.resample('D').mean()
# 'D' sta per Daily, la media viene calcolata per ogni giorno

# Resampling: calcolare la somma mensile
df_monthly = df.resample('M').sum()
# 'M' sta per Monthly, la somma viene calcolata per ogni mese

#aggiungere una colonna con il valore del giorno precedente
df['prev_day'] = df['value'].shift(1)
#tasso di variazione giornaliero
df['daily_return'] = df['value'].pct_change() # equivalente a shift + calcolo

# Series.rolling calcola statistiche mobili su una finestra temporale scorevvole
#finestre mobile di 7 giorni media e deviazione standard
df['rolling_mean7'] = df['value'].rolling(window=7).mean()
df['rolling_std7'] = df['value'].rolling(window=7).std()
