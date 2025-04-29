#  Importiamo le librerie necessarie
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.feature_selection import SelectKBest, f_regression, RFE
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from statsmodels.stats.outliers_influence import variance_inflation_factor

#  Creazione di un dataset sintetico con 4 feature e una variabile target
np.random.seed(42)
X = np.random.rand(100, 4) * 10  # 4 feature indipendenti
y = 3 * X[:, 0] + 2 * X[:, 1] - 1.5 * X[:, 2] + np.random.randn(100) * 2  # Relazione lineare con rumore

#  Suddivisione in training e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# =========================
#  Standardizzazione delle feature
# =========================
scaler = StandardScaler()  # Normalizza i dati con media=0 e deviazione standard=1
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# =========================
#  Rimozione della Multicollinearità con VIF
# =========================
# Calcoliamo il VIF per ogni feature
vif_data = pd.DataFrame()
vif_data["Feature"] = [f"X{i}" for i in range(X.shape[1])]
vif_data["VIF"] = [variance_inflation_factor(X_train_scaled, i) for i in range(X_train_scaled.shape[1])]

# Selezioniamo solo le feature con VIF < 10 (soglia accettabile per evitare multicollinearità)
selected_features = vif_data[vif_data["VIF"] < 10]["Feature"].index  # Manteniamo solo le feature con VIF accettabile
X_train_vif = X_train_scaled[:, selected_features]
X_test_vif = X_test_scaled[:, selected_features]

# =========================
#  Regolarizzazione (Ridge e Lasso)
# =========================
ridge = Ridge(alpha=1.0)  # Regolarizzazione L2, alpha=1 significa una leggera penalizzazione
ridge.fit(X_train_vif, y_train)
y_pred_ridge = ridge.predict(X_test_vif)
r2_ridge = r2_score(y_test, y_pred_ridge)  # Calcoliamo l'R^2

lasso = Lasso(alpha=0.1)  # Regolarizzazione L1, alpha più alto riduce più coefficienti a 0
lasso.fit(X_train_vif, y_train)
y_pred_lasso = lasso.predict(X_test_vif)
r2_lasso = r2_score(y_test, y_pred_lasso)  # Calcoliamo l'R^2

# =========================
#  Selezione delle Feature (`SelectKBest` e `RFE`)
# =========================
# SelectKBest: seleziona le 2 feature migliori in base alla statistica F
selector_kbest = SelectKBest(score_func=f_regression, k=2)
X_train_kbest = selector_kbest.fit_transform(X_train_vif, y_train)
X_test_kbest = selector_kbest.transform(X_test_vif)

# Recursive Feature Elimination (RFE): seleziona le 2 feature più importanti
model = LinearRegression()
selector_rfe = RFE(model, n_features_to_select=2)
X_train_rfe = selector_rfe.fit_transform(X_train_vif, y_train)
X_test_rfe = selector_rfe.transform(X_test_vif)

# =========================
#  Aggiunta di Termini Non Lineari (Regressione Polinomiale)
# =========================
poly = PolynomialFeatures(degree=2)  # Generiamo feature quadratiche
X_train_poly = poly.fit_transform(X_train_vif)
X_test_poly = poly.transform(X_test_vif)

# Creiamo un modello di regressione polinomiale
poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)
y_pred_poly = poly_model.predict(X_test_poly)
r2_poly = r2_score(y_test, y_pred_poly)  # Calcoliamo l'R^2

# =========================
#  Risultati
# =========================
results = {
    "R^2 Ridge": r2_ridge,
    "R^2 Lasso": r2_lasso,
    "R^2 Polinomiale": r2_poly,
}
results