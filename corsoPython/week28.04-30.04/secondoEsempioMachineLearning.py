# Importare le librerie necessarie
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import random

# Caricare il dataset Iris
iris = load_iris()
X = iris.data  # Caratteristiche
y = iris.target  # Etichette

# Scegliere due valori casuali di n_neighbors
n_neighbors_list = [random.randint(1, 10) for _ in range(2)]
print(f"Valori scelti di n_neighbors: {n_neighbors_list}")

# Eseguire i test
for n_neighbors in n_neighbors_list:
  print(f"\nTest per n_neighbors = {n_neighbors}")
  for i in range(10):  # 10 prove con random_state diversi
    rand_state = random.randint(0, 100)

    # Suddividere il dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=rand_state)
    
    # Definire il modello
    model = KNeighborsClassifier(n_neighbors=n_neighbors)

    # Addestrare e predire
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Valutare accuratezza
    accuracy = accuracy_score(y_test, y_pred)

    # Stampare i risultati
    print(f"  Test {i+1}: random_state={rand_state} -> Accuracy: {accuracy:.2f}")





