import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

def elimina_variabili_vif_pvalue(X_train, y_train, vif_threshold=10.0, pvalue_threshold=0.05):
  """
  Rimuove variabili da X_train basandosi su VIF e p-value.
  
  - Elimina solo variabili con VIF > soglia e p-value > soglia.
  - Ricalcola VIF e p-value dopo ogni eliminazione.
  """
  
  # Copia dei dati per lavorare in sicurezza
  X_current = X_train.copy()
  
  # Aggiungi costante per statsmodels
  X_const = sm.add_constant(X_current)
  
  while True:
    # Modello OLS per calcolare p-value
    model = sm.OLS(y_train, X_const).fit()
    pvalues = model.pvalues.drop('const')  # escludi l'intercetta
    
    # Calcolo VIF
    vif = pd.DataFrame()
    vif["Feature"] = X_current.columns
    vif["VIF"] = [variance_inflation_factor(X_current.values, i) for i in range(X_current.shape[1])]
    
    # Unisco p-value e VIF
    stats = vif.copy()
    stats["p-value"] = pvalues.values
    
    # Trova candidati da eliminare: VIF alto + p-value alto
    candidates = stats[(stats["VIF"] > vif_threshold) & (stats["p-value"] > pvalue_threshold)]
    
    if candidates.empty:
        print("\nNessuna variabile da eliminare. Selezione completata.")
        break
    
    # Elimina la variabile con il VIF piÃ¹ alto tra i candidati
    worst_feature = candidates.sort_values(by="VIF", ascending=False)["Feature"].iloc[0]
    print(f"Rimuovo '{worst_feature}' con VIF = {candidates.loc[candidates['Feature'] == worst_feature, 'VIF'].values[0]:.2f} "
          f"e p-value = {candidates.loc[candidates['Feature'] == worst_feature, 'p-value'].values[0]:.4f}")
    
    # Aggiorna i dati
    X_current = X_current.drop(columns=[worst_feature])
    X_const = sm.add_constant(X_current)
  
  print("\nFeature finali selezionate:")
  print(X_current.columns.tolist())
  
  return X_current