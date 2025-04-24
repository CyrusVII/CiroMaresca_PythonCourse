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
    # Impostazioni per il grafico
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Grafico dei dati originali
    sns.scatterplot(x=self.df['Altezza'], y=self.df['Peso'], hue=self.df['Età'], palette='viridis', ax=axes[0])
    axes[0].set_title('Dati Originali')
    axes[0].set_xlabel('Altezza (cm)')
    axes[0].set_ylabel('Peso (kg)')
    
    # Grafico dei dati normalizzati
    sns.scatterplot(x=self.dfNormalize['Altezza'], y=self.dfNormalize['Peso'], hue=self.dfNormalize['Età'], palette='viridis', ax=axes[1])
    axes[1].set_title('Dati Normalizzati')
    axes[1].set_xlabel('Altezza (Normalizzata)')
    axes[1].set_ylabel('Peso (Normalizzato)')
    
    sns.set_theme(style="darkgrid")
    plt.tight_layout()
    plt.show()

# Creiamo un'istanza della classe e chiamiamo il metodo grafico
df = Data()
df.grafico()