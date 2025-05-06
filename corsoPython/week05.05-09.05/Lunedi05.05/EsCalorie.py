import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_log_error

# --- Caricamento dei dati ---
train_df = pd.read_csv("MyCsv/EsCalorie/train.csv")
test_df = pd.read_csv("MyCsv/EsCalorie/test.csv")

# --- Codifica variabile categorica 'Sex' ---
le = LabelEncoder()
train_df['Sex'] = le.fit_transform(train_df['Sex'].astype(str))
test_df['Sex'] = le.transform(test_df['Sex'].astype(str))

# --- Feature Engineering: crea BMI e Effort ---
for df in [train_df, test_df]:
    df['BMI'] = df['Weight'] / ((df['Height'] / 100) ** 2)     # BMI = peso / altezza²
    df['Effort'] = df['Heart_Rate'] * df['Duration']           # Intensità = battito x durata

# --- Separazione delle feature e del target ---
X = train_df.drop(['id', 'Calories'], axis=1)
y = np.log1p(train_df['Calories'])  # Trasformazione log1p per ottimizzare con MSLE
X_test = test_df.drop('id', axis=1)

# --- Pulizia (riempimento valori mancanti e tipi coerenti) ---
X = X.fillna(X.mean()).astype(float)
X_test = X_test.fillna(X_test.mean()).astype(float)

# --- Definizione del modello base XGBoost ---
xgb = XGBRegressor(objective='reg:squarederror', random_state=42)

# --- Griglia estesa di iperparametri ---
param_grid = {
    'n_estimators': [100, 200, 300],         # Numero di alberi
    'learning_rate': [0.01, 0.05, 0.1],      # Tasso di apprendimento
    'max_depth': [3, 4, 5],                  # Profondità degli alberi
    'subsample': [0.6, 0.8, 1.0],            # Percentuale di dati per ogni albero
    'colsample_bytree': [0.6, 0.8, 1.0]      # Percentuale di feature da usare per albero
}

# --- Ricerca iperparametri con validazione incrociata ---
grid_search = GridSearchCV(
    estimator=xgb,
    param_grid=param_grid,
    cv=5,
    scoring='neg_mean_squared_error',  # MSLE richiede errori piccoli in scala log
    verbose=1,
    n_jobs=-1
)

# --- Addestramento con GridSearch ---
grid_search.fit(X, y)
best_model = grid_search.best_estimator_
print("Migliori parametri trovati:", grid_search.best_params_)

# --- Predizione e ritorno alla scala originale ---
log_preds = best_model.predict(X_test)
predictions = np.expm1(log_preds)              # Inverso di log1p
predictions = np.maximum(predictions, 0)       # Elimina valori negativi per sicurezza

# --- Creazione del file di sottomissione ---
submission = pd.DataFrame({
    'id': test_df['id'],
    'Calories': predictions
})

# --- Salvataggio del file ---
submission.to_csv("MyCsv/EsCalorie/final_submission.csv", index=False)
print("File 'final_submission.csv' creato con successo.")



