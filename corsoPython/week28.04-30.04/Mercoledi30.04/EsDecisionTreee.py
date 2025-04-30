from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# ---------------------------
# 1. Caricamento del dataset Iris
# ---------------------------

iris = load_iris()
X = iris.data
y = iris.target

# ---------------------------
# 2. Divisione del dataset in training e test
# ---------------------------

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---------------------------
# 3. Creazione del modello Decision Tree
# ---------------------------

tree = DecisionTreeClassifier(random_state=42)

# ---------------------------
# 4. Definizione dei parametri per la GridSearch
# ---------------------------

param_grid = {
    'max_depth': [3, 5, 10, None],  # Proviamo profondità diverse
    'min_samples_split': [2, 5, 10],  # Numero minimo di campioni per dividere un nodo
    'min_samples_leaf': [1, 2, 4]  # Numero minimo di campioni per essere una foglia
}

# ---------------------------
# 5. Eseguiamo GridSearchCV per trovare i migliori parametri
# ---------------------------

# Creiamo un oggetto GridSearchCV per eseguire una ricerca esaustiva su una griglia di iperparametri
# GridSearchCV esplora tutte le combinazioni dei parametri definiti in 'param_grid' e utilizza la cross-validation (cv=5)
# per determinare i migliori parametri basati sull'accuratezza del modello. In questo caso, la metrica di valutazione
# è l'accuratezza ('accuracy'), ma si potrebbe usare anche un'altra metrica a seconda delle necessità.
grid_search = GridSearchCV(estimator=tree, param_grid=param_grid, cv=5, scoring='accuracy')

grid_search.fit(X_train, y_train)

# Visualizziamo i migliori parametri trovati
print("Migliori parametri trovati:", grid_search.best_params_)

# ---------------------------
# 6. Valutazione del modello con i migliori parametri
# ---------------------------

# Utilizziamo il miglior modello trovato da GridSearch
best_tree = grid_search.best_estimator_

# Previsione sui dati di test
y_pred = best_tree.predict(X_test)

# Calcoliamo l'accuratezza
acc = accuracy_score(y_test, y_pred)
print(f"Accuratezza del modello con GridSearch: {acc:.2f}")

# ---------------------------
# 7. Visualizzazione dell'albero decisionale con i migliori parametri
# ---------------------------

plt.figure(figsize=(12, 8))
plot_tree(best_tree, filled=True, feature_names=iris.feature_names, class_names=iris.target_names, rounded=True)
plt.title("Albero Decisionale con i migliori parametri trovati")
plt.show()
