import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
import numpy as np

# Funzione per caricare e pulire i dati
def take_data_clean():
    # Caricamento del dataset
    df = pd.read_csv("MyCsv/kc_house_data.csv")
    print("Tipo di colonne:\n", df.dtypes)

    # Conversione della colonna 'date' in formato datetime, poi in solo data (senza orario)
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%dT%H%M%S')
    df['date'] = df['date'].dt.date

    # Rimozione righe con valori mancanti nella colonna 'date'
    df = df.dropna(subset=['date'])

    # Gestione dei valori nulli per colonne specifiche
    df['bedrooms'].fillna(df['bedrooms'].median(), inplace=True)
    df['bathrooms'].fillna(df['bathrooms'].median(), inplace=True)
    df['floors'].fillna(df['floors'].mode()[0], inplace=True)
    df['yr_renovated'].fillna(0, inplace=True)

    # Riempimento dei valori NaN restanti con la mediana delle colonne numeriche
    df.fillna(df.median(numeric_only=True), inplace=True)

    # Lista delle colonne da standardizzare (scalare)
    columns_to_standardize = ['price', 'sqft_living', 'sqft_lot', 'sqft_above', 
                              'sqft_basement', 'sqft_living15', 'sqft_lot15', 
                              'bathrooms', 'floors', 'lat', 'long']

    # Standardizzazione dei valori numerici (media = 0, std = 1)
    scaler = StandardScaler()
    df[columns_to_standardize] = scaler.fit_transform(df[columns_to_standardize])

    # Rimozione della colonna 'id' (non utile per la modellazione)
    df.drop('id', axis=1, inplace=True)

    # Output dei primi record dopo la pulizia
    print("Prime righe del DataFrame dopo pulizia e standardizzazione:\n", df.head())
    return df

# Funzione per mostrare i grafici delle matrici di correlazione prima e dopo il VIF
def grafici_matrice_correlazione_confronto(corr_initial, corr_reduced):
    plt.figure(figsize=(16, 6))

    # Matrice iniziale
    plt.subplot(1, 2, 1)
    sns.heatmap(corr_initial, cmap='coolwarm', annot=False, fmt=".2f", square=True)
    plt.title("Matrice di Correlazione - Iniziale")

    # Matrice dopo rimozione VIF > 10
    plt.subplot(1, 2, 2)
    sns.heatmap(corr_reduced, cmap='coolwarm', annot=False, fmt=".2f", square=True)
    plt.title("Matrice di Correlazione - Dopo VIF")

    plt.tight_layout()
    plt.show()

# Funzione che calcola il VIF e rimuove iterativamente le variabili con VIF > 10
def matrice_correlazione_vif(df):
    # Calcolo matrice di correlazione iniziale
    corr_matrix_initial = df.corr(numeric_only=True)
    print("\nMatrice di correlazione iniziale:\n", corr_matrix_initial)

    # Selezione delle feature numeriche escludendo il target 'price'
    X = df.select_dtypes(include=['float64', 'int64']).drop(columns=['price'], errors='ignore')

    # Ciclo che continua finché esiste un VIF maggiore di 10
    while True:
        # Aggiunta della costante per il calcolo del VIF
        X_const = add_constant(X)

        # Calcolo del VIF per ciascuna variabile
        vif_data = pd.DataFrame()
        vif_data["feature"] = X_const.columns
        vif_data["VIF"] = [variance_inflation_factor(X_const.values, i) for i in range(X_const.shape[1])]
        print("\nVIF corrente:\n", vif_data)

        # Escludiamo la costante e troviamo la variabile con VIF massimo
        vif_data_no_const = vif_data[vif_data["feature"] != "const"]
        vif_max = vif_data_no_const.loc[vif_data_no_const["VIF"].idxmax()]

        # Se il VIF massimo è accettabile, si esce dal ciclo
        if vif_max["VIF"] <= 10:
            break

        # Altrimenti, si rimuove la variabile con VIF più alto
        print(f"Rimuovo la variabile '{vif_max['feature']}' con VIF = {vif_max['VIF']:.2f}")
        X = X.drop(columns=[vif_max["feature"]])

    # Creazione del DataFrame ridotto con solo le feature ritenute accettabili + target
    df_reduced = df[X.columns.tolist() + ['price']]

    # Calcolo nuova matrice di correlazione
    corr_matrix_reduced = df_reduced.corr(numeric_only=True)
    print("\nMatrice di correlazione dopo la rimozione delle variabili con VIF > 10:\n", corr_matrix_reduced)

    # Visualizzazione comparativa delle matrici
    grafici_matrice_correlazione_confronto(corr_matrix_initial, corr_matrix_reduced)

    # Ritorna il DataFrame ridotto
    return df_reduced

# Funzione per eseguire la regressione lineare
def regressione_lineare(df, target_column='price'):
    # Separazione tra feature (X) e target (y)
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Suddivisione del dataset in train (80%) e test (20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Addestramento del modello di regressione lineare
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predizione sul test set
    y_pred = model.predict(X_test)

    # Calcolo del coefficiente R²
    r2 = r2_score(y_test, y_pred)
    print(f"R² Score: {r2:.4f}")

    return model

import statsmodels.api as sm

# Funzione per eseguire la regressione lineare e rimuovere le variabili con p-value > 0.05
def regressione_lineare_pvalue(df, target_column='price'):
    # Separazione tra feature (X) e target (y)
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Suddivisione in training e test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Aggiunta dell'intercetta (constante) per il modello OLS
    X_train_const = sm.add_constant(X_train)
    X_test_const = sm.add_constant(X_test)

    # Inizializzazione del modello con tutte le variabili
    model = sm.OLS(y_train, X_train_const).fit()

    # Iterativamente rimuove le variabili con p-value > 0.05
    while True:
        pvalues = model.pvalues.drop("const")  # escludi la costante
        max_pval = pvalues.max()
        if max_pval <= 0.05:
            break  # Tutti i p-value sono sotto la soglia

        # Variabile con p-value più alto
        worst_feature = pvalues.idxmax()
        print(f"Rimuovo la variabile '{worst_feature}' con p-value = {max_pval:.4f}")

        # Rimuove la variabile con p-value più alto da entrambe le versioni
        X_train_const = X_train_const.drop(columns=[worst_feature])
        X_test_const = X_test_const.drop(columns=[worst_feature])

        # Ricrea il modello senza quella variabile
        model = sm.OLS(y_train, X_train_const).fit()

    # Predizione sui dati di test
    y_pred = model.predict(X_test_const)

    # Calcolo del coefficiente di determinazione R²
    r2 = r2_score(y_test, y_pred)
    print(f"\nR² Score: {r2:.4f}")

    # Calcolo dell'errore quadratico medio (RMSE)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f"RMSE: {rmse:.4f}")

    # Stampa del sommario finale (solo variabili significative)
    print("\nSommario del modello finale (variabili con p <= 0.05):")
    print(model.summary())

    return model

# Esecuzione completa del processo
df = take_data_clean()                            # Pulizia e preparazione dei dati
df_reduced = matrice_correlazione_vif(df)         # Riduzione multicollinearità via VIF
#regressione_lineare(df_reduced, target_column='price')  # Addestramento modello
regressione_lineare_pvalue(df_reduced, target_column='price')
