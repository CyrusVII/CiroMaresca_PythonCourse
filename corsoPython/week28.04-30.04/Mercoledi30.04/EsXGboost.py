import xgboost as xgb
from sklearn.datasets import load_diabetes
import numpy as np

# ----------------------------------------------------------
# 1. Caricamento del dataset diabetes (regressione)
# ----------------------------------------------------------
diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target

# ----------------------------------------------------------
# 2. Creazione della DMatrix per XGBoost
# (richiesta da XGBoost per efficienza e gestione dei dati mancanti)
# ----------------------------------------------------------
dtrain = xgb.DMatrix(X, label=y, missing=np.nan)

# ----------------------------------------------------------
# 3. Parametri base del modello
# objective: tipo di problema (regressione)
# eta: learning rate
# max_depth: profondità massima degli alberi
# ----------------------------------------------------------
params = {
    'objective': 'reg:squarederror',
    'eta': 0.1,
    'max_depth': 4,
}

# ----------------------------------------------------------
# 4. Definizione della griglia per la ricerca di alpha e lambda
# alpha: regolarizzazione L1 (lasso)
# lambda: regolarizzazione L2 (ridge)
# ----------------------------------------------------------
param_grid = {
    'alpha': [0, 0.1, 0.5, 1],
    'lambda': [0, 0.1, 0.5, 1]
}

# Variabili per salvare i migliori risultati
best_params = {}
best_rmse = float("inf")

# ----------------------------------------------------------
# 5. Ricerca a griglia manuale con cross-validation
# Utilizziamo xgb.cv per valutare ogni combinazione
# ----------------------------------------------------------
for alpha in param_grid['alpha']:
    for lambda_ in param_grid['lambda']:
        # Aggiorniamo i parametri con i valori correnti della griglia
        params['alpha'] = alpha
        params['lambda'] = lambda_

        # Eseguiamo la cross-validation
        cv_results = xgb.cv(
            params=params,
            dtrain=dtrain,
            num_boost_round=100,
            nfold=5,
            metrics="rmse",
            early_stopping_rounds=10,
            seed=42,
            verbose_eval=False
        )

        # Calcoliamo il minimo RMSE medio sui fold di validazione
        mean_rmse = cv_results['test-rmse-mean'].min()

        print(f"alpha: {alpha}, lambda: {lambda_}, RMSE: {mean_rmse:.4f}")

        # Salviamo i migliori parametri
        if mean_rmse < best_rmse:
            best_rmse = mean_rmse
            best_params = {'alpha': alpha, 'lambda': lambda_}

# ----------------------------------------------------------
# 6. Risultato finale
# ----------------------------------------------------------
print(f"\nMigliori parametri trovati: {best_params} con RMSE: {best_rmse:.4f}")
