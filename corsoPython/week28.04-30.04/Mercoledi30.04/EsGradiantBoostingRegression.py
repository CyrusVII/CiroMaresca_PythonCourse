from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# 1. Creazione di un dataset di regressione sintetico
# ---------------------------
X, y = make_regression(n_samples=1000, n_features=10, noise=15, random_state=42)

# ---------------------------
# 2. Divisione in training e test
# ---------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---------------------------
# 3. Normalizzazione delle feature (StandardScaler)
# ---------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ---------------------------
# 4. Addestramento del modello Gradient Boosting
# ---------------------------
gbr = GradientBoostingRegressor(random_state=42)
gbr.fit(X_train_scaled, y_train)

# ---------------------------
# 5. Previsioni e metriche di valutazione
# ---------------------------
y_pred = gbr.predict(X_test_scaled)

# Coefficiente di determinazione R²
r2 = r2_score(y_test, y_pred)

# Errore quadratico medio (RMSE)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"Punteggio R²: {r2:.2f}")
print(f"RMSE (Root Mean Squared Error): {rmse:.2f}")

# ---------------------------
# 6. Visualizzazione del confronto tra valori reali e predetti
# ---------------------------
plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred, alpha=0.6, edgecolor='k')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.title("Confronto tra Valori Reali e Predetti (Gradient Boosting)")
plt.xlabel("Valori Reali")
plt.ylabel("Valori Predetti")
plt.grid(True)
plt.tight_layout()
plt.show()

