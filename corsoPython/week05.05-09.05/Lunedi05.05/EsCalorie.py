import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# --- Caricamento dati ---
train_df = pd.read_csv("MyCsv/EsCalorie/train.csv")
test_df  = pd.read_csv("MyCsv/EsCalorie/test.csv")

# --- Codifica della colonna 'Sex' ---
le = LabelEncoder()
train_df['Sex'] = le.fit_transform(train_df['Sex'].astype(str))
test_df ['Sex'] = le.transform(test_df['Sex'].astype(str))

# --- Separazione feature e target ---
X = train_df.drop(['id', 'Calories'], axis=1)
y = train_df['Calories']

# --- Controlli diagnostici per NaN ---
print("Valori NaN in X:\n", X.isnull().sum())
print("Valori NaN in y:\n", y.isnull().sum())

# --- Se ci sono NaN, puoi riempirli così (opzionale) ---
# X = X.fillna(X.mean())
# y = y.fillna(y.mean())

# --- Conversione forzata a numerico ---
X = X.astype(float)
y = y.astype(float)

# --- Addestramento del modello ---
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# --- Previsione sul test set ---
X_test = test_df.drop('id', axis=1).astype(float)
predictions = model.predict(X_test)

# --- Creazione del file di sottomissione ---
submission = pd.DataFrame({
    'id': test_df['id'],
    'Calories': predictions
})

# --- Salvataggio ---
submission.to_csv("MyCsv/EsCalorie/final_submission.csv", index=False)
print("File 'final_submission.csv' creato con successo.")

print("fine")
