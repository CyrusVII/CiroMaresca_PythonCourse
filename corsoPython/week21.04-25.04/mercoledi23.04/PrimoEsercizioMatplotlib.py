# Hai a disposizione un dataset, che devi autogenerare, contenuto in un DataFrame pandas con una singola colonna 
# temperature che rappresenta la temperatura giornaliera in una città per un mese.
# Scrivi un programma Python che calcoli e stampi le seguenti statistiche:
# • La temperatura massima
# • La temperatura minima
# • La temperatura media
# La mediana delle temperature
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#classe temperature
class Temperature:
  def __init__(self):
    self.df = self.generator()
  
  def generator(self):
    temp = np.random.randint(0,30,size=30)
    date = pd.date_range(end=pd.Timestamp.today().date(), periods=30, freq='D')
    df = pd.DataFrame({
      'date' : date,
      'temperature' : temp
      })
    return df
  
  # Metodo per calcolare la temperatura massima
  def max_temp(self):
    maxx =self.df['temperature'].max()
    print("Temperatura massima: ",maxx)
    return maxx
  
  # Metodo per calcolare la temperatura minima
  def min_temp(self):
    min = self.df['temperature'].min()
    print("Temperatura minima: ",min)
    return min

  # Metodo per calcolare la temperatura media
  def avg_temp(self):
    avg = self.df['temperature'].mean()
    print("Temperatura media: ",avg)
    return avg
  
  # Metodo per calcolare la mediana delle temperature
  def median_temp(self):
    med = self.df['temperature'].median()
    print("Mediana Temperatura: ",med)
    return med
  
  #grafioc temp giornaliera
  def grafico_temp_giornaliero(self):
    maxx = self.max_temp()
    min = self.min_temp()
    avg = self.avg_temp()
    med = self.median_temp()
    # Crea una nuova figura per il grafico
    plt.figure(figsize=(10, 6))  # Imposta la dimensione della figura (10x6 pollici)
    
    # Traccia il grafico delle temperature giornaliere
    # self.df['date']: serie di date per l'asse X
    # self.df['temperature']: serie di temperature per l'asse Y
    # label: etichetta per la legenda
    # color: colore della linea
    # marker='o': usa un marker a forma di cerchio per ogni punto
    plt.plot(self.df['date'], self.df['temperature'], label='Temperature giornaliere', color='b', marker='o')
    
    # Aggiungi linee tratteggiate per la temperatura massima, minima, media e mediana
    plt.axhline(y=maxx, color='r', linestyle='--', label=f'Temperatura massima: {maxx}°C')
    plt.axhline(y=min, color='g', linestyle='--', label=f'Temperatura minima: {min}°C')
    plt.axhline(y=avg, color='y', linestyle='--', label=f'Temperatura media: {avg:.2f}°C')
    plt.axhline(y=med, color='m', linestyle='--', label=f'Mediana Temperatura: {med}°C')
    
    # Imposta il titolo del grafico
    plt.title('Andamento delle Temperature Giornalieri')
    # Aggiungi etichetta all'asse X (Data)
    plt.xlabel('Data')
    # Aggiungi etichetta all'asse Y (Temperatura in °C)
    plt.ylabel('Temperatura (°C)')
    # Ruota le etichette dell'asse X (le date) di 45 gradi 
    plt.xticks(rotation=45)
    # Aggiungi la griglia per facilitare la lettura del grafico
    plt.grid(True)
    # Mostra la legenda con l'etichetta definita precedentemente
    plt.legend()
    # Ottimizza il layout per evitare sovrapposizioni 
    plt.tight_layout()
    # Mostra il grafico
    plt.show()
    
  #grafico statistiche
  def stats_temp(self):
    # Crea una nuova figura per il grafico delle statistiche
    plt.figure(figsize=(8, 5))  # Imposta la dimensione della figura (8x5 pollici)
    
    # Definisci le etichette per le statistiche delle temperature
    stats = ['Massima', 'Minima', 'Media', 'Mediana']
    
    # Definisci i valori delle statistiche da visualizzare nel grafico
    values = [self.max_temp(), self.min_temp(), self.avg_temp(), self.median_temp()]
    
    # Crea un grafico a barre per visualizzare le statistiche
    # 'stats': le etichette per le barre (massima, minima, media, mediana)
    # 'values': i valori corrispondenti a ciascuna statistica
    # 'color': imposta il colore delle barre per ciascuna statistica
    # 'edgecolor': imposta il colore del bordo delle barre
    plt.bar(stats, values, color=['red', 'green', 'blue', 'orange'], edgecolor='black')
    
    # Imposta il titolo del grafico
    plt.title('Statistiche delle Temperature')
    
    # Aggiungi etichetta all'asse Y (Temperatura in °C)
    plt.ylabel('Temperatura (°C)')
    
    # Ottimizza il layout per evitare sovrapposizioni (soprattutto per le etichette)
    plt.tight_layout()
    
    # Mostra il grafico
    plt.show()
  
# Funzione per il menu 
def menu():
  tp = Temperature()

  while True:
    print("\n----- Menu -----")
    print("1. Mostra informazioni sul dataset")
    print("2. Grafico giornaliero")
    print("3. Grafico Statistiche sulle temperature")
    print("4. Esci")
    scelta = input("Scegli un'opzione (1-4): ")

    match scelta:
      case "1":
        print(tp.df)
      case "2":
        tp.grafico_temp_giornaliero()
      case "3":
        tp.stats_temp()
      case "4":
        print("Uscita in corso...")
        break
      case _:
        print("Opzione non valida, riprova.")

# Avvia il menu
if __name__ == "__main__":
  menu()
