# Carica il dataset Iris.
# Standardizza le caratteristiche
# utilizzando StandardScaler.
# Suddividi i dati in training e test set
# (70% training, 30% test).
# Applica l'algoritmo
# DecisionTreeClassifier.
# Valuta la performance del modello
# utilizzando il classification_report
# (precisione, recall, F1-score).
# Visualizza la matrice di confusione.

# Importiamo le librerie necessarie
from sklearn import datasets  # Per caricare il dataset Iris
from sklearn.model_selection import train_test_split  # Per suddividere i dati in training e test set
from sklearn.preprocessing import StandardScaler  # Per standardizzare le caratteristiche
from sklearn.tree import DecisionTreeClassifier  # Per applicare l'albero decisionale
from sklearn.metrics import classification_report, confusion_matrix  # Per la valutazione del modello
import seaborn as sns  # Per la visualizzazione della matrice di confusione
import matplotlib.pyplot as plt  # Per la visualizzazione grafica

# 1. Carica il dataset Iris
iris = datasets.load_iris()  # Carichiamo il dataset Iris, che è predefinito in sklearn
X = iris.data  # Le caratteristiche (features)
y = iris.target  # Le etichette (target)

# 2. Standardizza le caratteristiche
scaler = StandardScaler()  # Creiamo un oggetto StandardScaler per standardizzare i dati
X_scaled = scaler.fit_transform(X)  # Standardizziamo le caratteristiche per avere media=0 e varianza=1

# 3. Suddividi i dati in training e test set (70% training, 30% test)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42, stratify=y
)  # Dividiamo i dati in training (70%) e test (30%), assicurandoci che le classi siano bilanciate

# 4. Applica l'algoritmo DecisionTreeClassifier
clf = DecisionTreeClassifier(random_state=42)  # Creiamo un albero decisionale, fissando il random_state per riproducibilità
clf.fit(X_train, y_train)  # Alleniamo l'albero decisionale con i dati di training

# 5. Valuta la performance del modello utilizzando classification_report
y_pred = clf.predict(X_test)  # Prediciamo le etichette per il test set
print(classification_report(y_test, y_pred, target_names=iris.target_names))  # Stampa il report con precisione, recall, F1-score per ciascuna classe

# Calcoliamo la matrice di confusione
cm = confusion_matrix(y_test, y_pred)  # Calcoliamo la matrice di confusione tra le etichette vere e quelle predette

# Creiamo una visualizzazione grafica della matrice di confusione
plt.figure(figsize=(6, 5))  # Impostiamo la dimensione della figura per la matrice di confusione
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=iris.target_names, yticklabels=iris.target_names) 
# Creiamo la heatmap della matrice di confusione, con annotazioni dei numeri e colori blu
plt.title('Matrice di Confusione')  # Titolo del grafico
plt.xlabel('Predizioni')  # Etichetta per l'asse X (predizioni)
plt.ylabel('Vere etichette')  # Etichetta per l'asse Y (etichette reali)
plt.show()  # Mostriamo il grafico

