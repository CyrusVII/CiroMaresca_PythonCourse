import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import StandardScaler

def prepare_data():
    # 1. Carica il dataset
    df = pd.read_csv("MyCsv/AB_NYC_2019.csv")

    # 2. Definisci la variabile target e le feature numeriche
    target = 'price'
    features = [
        'minimum_nights', 'number_of_reviews', 'reviews_per_month',
        'calculated_host_listings_count', 'availability_365'
    ]

    # 3. Rimuovi righe con valori nulli
    df_model = df[features + [target]].dropna()

    # 4. Crea X e y
    X = df_model[features]
    y = df_model[target]

    # 5. Aggiungi la costante per la regressione OLS
    X_with_const = sm.add_constant(X)

    # 6. Regressione OLS per calcolo p-values
    ols_model = sm.OLS(y, X_with_const).fit()
    pvalues = ols_model.pvalues

    # 7. Calcola il VIF
    vif_data = pd.DataFrame()
    vif_data['feature'] = X.columns
    vif_data['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

    # 8. Rimuovi le colonne con p-value > 0.05 (escludendo 'const')
    significant_features = pvalues[pvalues < 0.05].index
    significant_features = [f for f in significant_features if f != 'const']

    # 9. Crea nuovo dataframe filtrato
    X_selected = X[significant_features]

    # 10. Mostra risultati
    print("P-values:\n", pvalues)
    print("\nVIF:\n", vif_data)
    print("\nFeature selezionate:\n", significant_features)
    
    # Colonne categoriche rilevanti
    categorical_features = ['neighbourhood_group', 'neighbourhood', 'room_type']

    # Seleziona solo le colonne utili
    df_selected = df[X_selected.columns.tolist() + categorical_features + [target]].dropna()
    
    # Standardizzazione delle feature numeriche
    scaler = StandardScaler()
    df_selected[X_selected.columns.tolist()] = scaler.fit_transform(df_selected[X_selected.columns.tolist()])
    
    df_selected[categorical_features] = df[categorical_features].astype('category')
    
    return df_selected,X_selected,y,categorical_features,scaler
    
prepare_data()



