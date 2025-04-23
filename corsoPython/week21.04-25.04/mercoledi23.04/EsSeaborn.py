# Creato un DataFrame pandas con tre colonne: altezza, peso e età di un gruppo di persone, 
# normalizza i dati di altezza e peso usando la normalizzazione min- max (ridimensiona i valori in modo che varino tra 0 e 1). 
# Assicurati di lasciare inalterata la colonna età; mostra il DataFrame originale e quello modificato.
# Fornisci un codice che:
# 1. Carichi il DataFrame (puoi assumere che i dati siano già disponibili in un DataFrame chiamato df).
# 2. Applichi la normalizzazione min-max alle colonne altezza e peso.
# 3. Stampa sia il DataFrame originale sia quello modificato per compararli.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class Data:
  def __init__(self):
    self.df = self.generator()
    self.dfNormalize = self.normalize()
  
  def generator(self):
    # Generiamo dati casuali
    altezza = np.random.randint(150, 190, size=10)  # Altezza tra 150 e 190 cm
    peso = np.random.randint(50, 100, size=10)  # Peso tra 50 e 100 kg
    eta = np.random.randint(18, 60, size=10)  # Età tra 18 e 60 anni

    # Creiamo il DataFrame
    df = pd.DataFrame({
      'Altezza': altezza,
      'Peso': peso,
      'Età': eta
    })

    return df
  
  def normalize(self):
    # Normalizzazione delle colonne numeriche
    numeriche = ['Altezza', 'Peso']
    dfNorm = self.df.copy()
    for col in numeriche:
      if col in dfNorm.columns:
        min_val =  dfNorm[col].min()
        max_val =  dfNorm[col].max()
        dfNorm[col] = ( dfNorm[col] - min_val) / (max_val - min_val) 
    return dfNorm

  def grafico(self):
    # Creiamo la figura con due sotto-grafici 3D per il confronto
    fig = plt.figure(figsize=(14, 7))

    # Grafico per i dati originali
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.scatter(self.df['Altezza'], self.df['Peso'], self.df['Età'], c=self.df['Età'], cmap='viridis')
    ax1.set_xlabel('Altezza')
    ax1.set_ylabel('Peso')
    ax1.set_zlabel('Età')
    ax1.set_title('Dati Originali', pad=5)  

    # Grafico per i dati normalizzati
    ax2 = fig.add_subplot(122, projection='3d')
    ax2.scatter(self.dfNormalize['Altezza'], self.dfNormalize['Peso'], self.dfNormalize['Età'], c=self.dfNormalize['Età'], cmap='viridis')
    ax2.set_xlabel('Altezza Normalizzata')
    ax2.set_ylabel('Peso Normalizzato')
    ax2.set_zlabel('Età Normalizzata')
    ax2.set_title('Dati Normalizzati', pad=5)

    plt.tight_layout()
    plt.show()

# Creiamo un'istanza della classe e chiamiamo il metodo grafico
df = Data()
df.grafico()