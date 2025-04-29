import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant

# Funzione per caricare e pulire i dati
def take_data_clean():
  # Carica i dati
  df = pd.read_csv("MyCsv/kc_house_data.csv")
  print("Tipo di colonne:\n", df.dtypes)

  # Converte la colonna 'date' in formato datetime
  df['date'] = pd.to_datetime(df['date'], format='%Y%m%dT%H%M%S')
  df['date'] = df['date'].dt.date

  # Rimuove tutte le righe con valori NaN nella colonna 'date'
  df = df.dropna(subset=['date'])

  # Riempie i valori nulli per le colonne specifiche
  df['bedrooms'].fillna(df['bedrooms'].median(), inplace=True)
  df['bathrooms'].fillna(df['bathrooms'].median(), inplace=True)
  df['floors'].fillna(df['floors'].mode()[0], inplace=True)
  df['yr_renovated'].fillna(0, inplace=True)

  # Riempie tutti i valori NaN nelle colonne numeriche con la mediana
  df.fillna(df.median(numeric_only=True), inplace=True)

  # Colonne da standardizzare
  columns_to_standardize = ['price', 'sqft_living', 'sqft_lot', 'sqft_above', 
                          'sqft_basement', 'sqft_living15', 'sqft_lot15', 
                          'bathrooms', 'floors', 'lat', 'long']

  # Crea l'oggetto StandardScaler
  scaler = StandardScaler()

  # Applica la standardizzazione solo sulle colonne numeriche
  df[columns_to_standardize] = scaler.fit_transform(df[columns_to_standardize])

  # Togliere feature inutili (id)
  df.drop('id', axis=1, inplace=True)

  # Stampa e return
  print("Prime righe del DataFrame dopo pulizia e standardizzazione:\n", df.head())
  return df

#grafici matrice correlazione
def grafici_matrice_correlazione_confronto(corr_initial, corr_reduced):
    plt.figure(figsize=(16, 6))

    # Grafico della matrice iniziale
    plt.subplot(1, 2, 1)
    sns.heatmap(corr_initial, cmap='coolwarm', annot=False, fmt=".2f", square=True)
    plt.title("Matrice di Correlazione - Iniziale")

    # Grafico della matrice ridotta
    plt.subplot(1, 2, 2)
    sns.heatmap(corr_reduced, cmap='coolwarm', annot=False, fmt=".2f", square=True)
    plt.title("Matrice di Correlazione - Dopo VIF")

    plt.tight_layout()
    plt.show()

#matrice correlazione
def matrice_correlazione_vif(df):
  corr_matrix_initial = df.corr(numeric_only=True)
  print("\nMatrice di correlazione iniziale:\n", corr_matrix_initial)

  X = df.select_dtypes(include=['float64', 'int64'])
  X = add_constant(X)

  vif_data = pd.DataFrame()
  vif_data["feature"] = X.columns
  vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
  print("\nVIF iniziale:\n", vif_data)

  features_to_keep = vif_data[(vif_data["VIF"] <= 10) & (vif_data["feature"] != 'const')]["feature"].tolist()
  df_reduced = df[features_to_keep]

  corr_matrix_reduced = df_reduced.corr(numeric_only=True)
  print("\nMatrice di correlazione dopo rimozione VIF > 10:\n", corr_matrix_reduced)

  grafici_matrice_correlazione_confronto(corr_matrix_initial, corr_matrix_reduced)

#regression
def regressione_lineare(df, target_column='price'):
  # Separazione tra feature e target
  X = df.drop(columns=[target_column])
  y = df[target_column]

  # Suddivisione in training e test set
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

  # Inizializza e allena il modello
  model = LinearRegression()
  model.fit(X_train, y_train)

  # Predizione
  y_pred = model.predict(X_test)

  # Calcolo R^2
  r2 = r2_score(y_test, y_pred)
  print(f"R² Score: {r2:.4f}")

  return model

# Carica e pulisci i dati
df = take_data_clean()

# Calcola la matrice di correlazione e la matrice VIF
matrice_correlazione_vif(df)

# Riduci il DataFrame secondo il VIF
X = df.select_dtypes(include=['float64', 'int64'])
X = add_constant(X)
vif_data = pd.DataFrame()
vif_data["feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
features_to_keep = vif_data[(vif_data["VIF"] <= 10) & (vif_data["feature"] != 'const')]["feature"].tolist()

df_reduced = df[features_to_keep + ['price']]  # Assicurati di mantenere 'price' come target

# Regressione lineare
regressione_lineare(df_reduced, target_column='price')






