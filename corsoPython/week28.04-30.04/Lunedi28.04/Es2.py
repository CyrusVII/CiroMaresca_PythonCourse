# Importazione delle librerie necessarie
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 1. Creazione di un dataset di esempio
# Simuliamo un dataset con 200 campioni e 5 feature casuali
np.random.seed(42)  # Impostiamo il seed per riproducibilità
X = np.random.rand(200, 5)

# 2. Normalizzazione delle feature
# È buona prassi normalizzare le feature prima di eseguire PCA
# Questo perché PCA è influenzata dalla scala delle variabili
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Istanziazione del modello PCA
# Impostiamo n_components=2 per ridurre la dimensionalità a 2 componenti principali
pca = PCA(n_components=2)

# 4. Applicazione della PCA ai dati normalizzati
X_pca = pca.fit_transform(X_scaled)

# 5. Stampa della varianza spiegata da ciascuna delle due componenti principali
# Questo ci dice quanta informazione dei dati originali è mantenuta
print("Varianza spiegata da ciascuna componente:", pca.explained_variance_ratio_)

# 6. Visualizzazione dei dati proiettati sulle due componenti principali
plt.figure(figsize=(8, 6))
plt.scatter(
    X_pca[:, 0],         # Prima componente principale
    X_pca[:, 1],         # Seconda componente principale
    c='blue',            # Colore dei punti
    edgecolor='k',       # Colore del bordo dei punti
    alpha=0.7            # Trasparenza
)
plt.xlabel("Prima componente principale")
plt.ylabel("Seconda componente principale")
plt.title("Visualizzazione dati dopo PCA (2D)")
plt.grid(True)
plt.tight_layout()
plt.show()
