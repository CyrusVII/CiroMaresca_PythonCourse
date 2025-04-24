# L'obiettivo di questo esercizio è generare un set di dati di serie temporali utilizzando NumPy, analizzarli con pandas e visualizzare i risultati usando Matplotlib. 
# Gli studenti dovranno eseguire le seguenti operazioni:
# 1. Generazione dei Dati: Utilizzare NumPy per generare una serie temporale di 365 giorni di dati, simulando il numero di visitatori giornalieri in un parco. 
# Assumere che il numero medio di visitatori sia 2000 con una deviazione standard di 500. Inoltre, aggiungere un trend crescente nel tempo per simulare l'aumento 
# della popolarità del parco.
# 2. Creazione del DataFrame: Creare un DataFrame pandas con le date come indice e il numero di visitatori come colonna.
# 3. Analisi dei Dati: Calcolare il numero medio di visitatori per mese e la deviazione standard.
# 4. Visualizzazione dei Dati:
# © Creare un grafico a linee del numero di visitatori giornalieri.
# Aggiungere al grafico la media mobile a 7 giorni per mostrare la tendenza settimanale.
# • Creare un secondo grafico che mostri la media mensile dei visitatori.]

import matplotlib.pyplot as plt
import seaborn as sbs
import numpy as np
import pandas as pd
import matplotlib.dates as mdates

# Classe per generare i dati simulati
class Generator():
  
  @staticmethod
  def data_generator():
    # Genera una serie di 365 date fino ad oggi
    date = pd.date_range(end=pd.Timestamp.today().normalize(), periods=365)

    # Trend lineare da 0 a 1000
    trend = np.linspace(0, 1000, len(date))

    # Valori base con media 2000 e deviazione standard 500
    base = np.random.normal(loc=2000, scale=500, size=len(date))
    base = np.clip(base, 1000, None)  

    # Somma del trend al valore base
    visitatori = base + trend

    # Crea il DataFrame
    df = pd.DataFrame({
      'visitatori': visitatori.astype(int)
      }, index=date)

    print(df)
    return df

  @staticmethod 
  def med_visitatori_mese(df):
    # Media mensile dei visitatori
    return df.resample('M').mean()

  @staticmethod 
  def deviazione_visitatori_mese(df):
    # Deviazione standard mensile dei visitatori
    return df.resample('M').std()
  
  @staticmethod
  def med_sette_giorni(df):
    # Calcolo della media mobile a 7 giorni
    return df['visitatori'].rolling(window=7).mean()


# Classe per generare i grafici
class GraficGenerator():

  @staticmethod
  def primo_grafico(df):
    # Calcolo della media mobile
    med_week = Generator.med_sette_giorni(df)

    # Crea una figura unica
    plt.figure(figsize=(14, 6))

    # Linea dei visitatori giornalieri
    plt.plot(df.index, df['visitatori'], label='Visitatori Giornalieri', alpha=0.5)

    # Punti rossi ogni 7 giorni (media mobile)
    plt.scatter(df.index[6:], med_week[6:], label='Media Mobile 7gg', color='red', zorder=5)
    
    # Personalizzazioni
    plt.title('Visitatori Giornalieri e Tendenza Settimanale (Media Mobile 7gg)')
    plt.xlabel('Data')
    plt.ylabel('Numero di Visitatori')
    
    # Mostra una data mese giorni sull'asse X
    plt.gca().xaxis.set_major_locator(mdates. MonthLocator(interval=1))  # ogni mese
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%b-%y'))     # formato tipo 24-Apr

    plt.xticks(rotation=45)  # ruota le date 
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

  @staticmethod
  def secondo_grafico(df):
    # Media mensile dei visitatori
    media_mensile = Generator.med_visitatori_mese(df)

    # Crea una figura per il grafico mensile
    plt.figure(figsize=(14, 6))

    # Linea con marker della media mensile
    plt.plot(media_mensile.index, media_mensile['visitatori'], label='Media Mensile Visitatori', color='green', marker='o')

    # Personalizzazioni
    plt.title('Media Mensile dei Visitatori')
    plt.xlabel('Mese')
    plt.ylabel('Numero di Visitatori')
    
    # Mostra una data ogni mese sull'asse X
    plt.gca().xaxis.set_major_locator(mdates. MonthLocator(interval=1))  # ogni mese
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%b-%y'))     # formato tipo 24-Apr

    plt.xticks(rotation=45)  # ruota le date 
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

  @staticmethod
  def grafico_unito(df):
    # Crea un'unica figura con 2 sottotrame (subplots)
    fig, axs = plt.subplots(2, 1, figsize=(14, 12))  # 2 righe, 1 colonna

    # === PRIMO GRAFICO: Giornaliero ===
    med_week = Generator.med_sette_giorni(df)
    axs[0].plot(df.index, df['visitatori'], label='Visitatori Giornalieri', alpha=0.5)
    axs[0].scatter(df.index[6:], med_week[6:], label='Media Mobile 7gg', color='red', zorder=5)

    axs[0].set_title('Visitatori Giornalieri e Tendenza Settimanale (Media Mobile 7gg)')
    axs[0].set_xlabel('Data')
    axs[0].set_ylabel('Numero di Visitatori')
    axs[0].legend()
    axs[0].grid(True)

    # === SECONDO GRAFICO: Media mensile ===
    media_mensile = Generator.med_visitatori_mese(df)
    axs[1].plot(media_mensile.index, media_mensile['visitatori'], label='Media Mensile Visitatori', color='green', marker='o')

    axs[1].set_title('Media Mensile dei Visitatori')
    axs[1].set_xlabel('Mese')
    axs[1].set_ylabel('Numero di Visitatori')
    axs[1].legend()
    axs[1].grid(True)

    # Ottimizzazione layout per evitare sovrapposizioni
    plt.tight_layout()
    plt.show()


# Menù interattivo per scegliere i grafici da visualizzare
def menu():
  df = Generator.data_generator()
  while True:
    print('\n--- MENU ---')
    print('1. Grafico visitatori giornaliero')
    print('2. Grafico visitatori mese')
    print('3. Grafico entrambi')
    print('4. Esci')
    ch = input('---> ')
    match ch:
      case '1':
        GraficGenerator.primo_grafico(df)
      case '2':
        GraficGenerator.secondo_grafico(df)
      case '3':
        GraficGenerator.grafico_unito(df)
      case '4':
        print("Exit....")
        break

# Avvia il programma
if __name__ == "__main__":
  menu()

