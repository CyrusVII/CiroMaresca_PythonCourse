import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ---------------------
# 1. Creazione dati sintetici
# ---------------------

# Generiamo 3 classi con punti distribuiti nello spazio
np.random.seed(0)
X1 = np.random.randn(50, 2) + [2, 2]   # Classe 0
X2 = np.random.randn(50, 2) + [6, 2]   # Classe 1
X3 = np.random.randn(50, 2) + [4, 6]   # Classe 2

# Uniamo tutti i dati
X = np.vstack((X1, X2, X3))
y = np.array([0]*50 + [1]*50 + [2]*50)

# ---------------------
# 2. Divisione train/test
# ---------------------

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---------------------
# 3. Proviamo diversi k
# ---------------------

accuratezze = []
k_values = range(1, 21)

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuratezze.append(acc)
    print(f"k={k}, Accuratezza={acc:.2f}")

# ---------------------
# 4. Analisi statistiche
# ---------------------

max_acc = max(accuratezze)
min_acc = min(accuratezze)
mean_acc = np.mean(accuratezze)

k_max = k_values[accuratezze.index(max_acc)]
k_min = k_values[accuratezze.index(min_acc)]

# ---------------------
# 5. Visualizzazione
# ---------------------

plt.figure(figsize=(10, 6))
plt.plot(k_values, accuratezze, marker='o', label='Accuratezza')

# Linea tratteggiata per il massimo
plt.axvline(k_max, linestyle='--', color='green', label=f'Massimo (k={k_max}, {max_acc:.2f})')
# Linea tratteggiata per il minimo
plt.axvline(k_min, linestyle='--', color='red', label=f'Minimo (k={k_min}, {min_acc:.2f})')
# Linea orizzontale per la media
plt.axhline(mean_acc, linestyle='--', color='blue', label=f'Media accuracy ({mean_acc:.2f})')

# Etichette e stile
plt.title('Accuratezza del modello k-NN per diversi valori di k')
plt.xlabel('Numero di vicini (k)')
plt.ylabel('Accuratezza')
plt.xticks(k_values)
plt.grid(True)
plt.legend(loc='lower right')
plt.tight_layout()
plt.show()


