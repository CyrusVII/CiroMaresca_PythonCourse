# Importiamo il dataset California Housing da sklearn.datasets
from sklearn.datasets import fetch_california_housing
# Importiamo pandas per la gestione dei DataFrame
import pandas as pd
import matplotlib.pyplot as plt

# Carichiamo il dataset California Housing come un DataFrame usando as_frame=True
california = fetch_california_housing(as_frame=True)
# Estraiamo il DataFrame completo (caratteristiche + target)
housing = california.frame
# Visualizziamo le prime 5 righe del DataFrame per avere un'anteprima dei dati
print(housing.head())
print(housing.info())

# Tracciamo un istogramma per ciascuna colonna numerica del DataFrame "housing"
# Impostiamo 50 intervalli (bins) per una risoluzione dettagliata e una dimensione della figura di 10x4
housing.hist(bins=50, figsize=(10, 4))
# Ottimizza automaticamente il layout per evitare sovrapposizioni tra etichette e grafici
plt.tight_layout()
# Mostra effettivamente tutti i grafici
plt.show()
