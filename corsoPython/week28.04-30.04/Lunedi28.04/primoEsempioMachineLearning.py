# Importazione delle librerie necessarie
from sklearn.datasets import load_iris                    # Per caricare il dataset Iris predefinito
from sklearn.model_selection import train_test_split      # Per dividere i dati in training e test set
from sklearn.ensemble import RandomForestClassifier       # Modello di classificazione Random Forest
from sklearn.metrics import accuracy_score                # Per calcolare l'accuratezza del modello

# Caricamento del dataset Iris
data = load_iris()
X = data.data      # 'X' contiene le caratteristiche (feature) dei fiori: lunghezza sepalo, larghezza sepalo, ecc.
y = data.target    # 'y' contiene le etichette (target): i nomi delle specie di fiori (setosa, versicolor, virginica)

# Divisione dei dati in set di addestramento e set di test
X_train, X_test, y_train, y_test = train_test_split(
    X, y,              # I dati da dividere
    test_size=0.2,     # Il 20% dei dati sarà usato per il test
    random_state=42    # Per garantire che la divisione sia sempre la stessa (riproducibilità)
)

# Creazione del modello di classificazione Random Forest
model = RandomForestClassifier(
    n_estimators=100,  # Numero di alberi nella foresta
    random_state=42   # Random seed per rendere l'addestramento riproducibile
)

# Addestramento del modello sui dati di training
model.fit(X_train, y_train)

# Predizione delle etichette sui dati di test
predictions = model.predict(X_test)

# Calcolo dell'accuratezza del modello confrontando predizioni e valori reali
accuracy = accuracy_score(y_test, predictions)

# Stampa dell'accuratezza (in percentuale, con due decimali)
print(f'Accuracy: {accuracy:.2f}')
