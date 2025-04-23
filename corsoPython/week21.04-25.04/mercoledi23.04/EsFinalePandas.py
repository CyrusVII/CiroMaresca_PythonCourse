# Obiettivo: Utilizzare pandas e numpy per esplorare, pulire, trasformare e analizzare un dataset di clienti della compagnia di telecomunicazioni. 
# • ID_Cliente: Identificativo unico per ogni cliente
# Età: Età del cliente
# ⚫ Durata Abonnamento: Quanti mesi il cliente è stato abbonato
# • Tariffa_Mensile: Quanto il cliente paga al mese
# • Dati Consumati: GB di dati consumati al mese
# • Servizio Clienti Contatti: Quante volte il cliente ha contattato il servizio clienti
# Churn: Se il cliente ha lasciato la compagnia (Si/No)
# 1. Caricamento e Esplorazione Iniziale:
# ⚫ Caricare i dati da un file CSV.
# Utilizzare info(), describe(), e value_counts() per esaminare la distribuzione dei dati e identificare colonne con valori mancanti.
# 2. Pulizia dei Dati:
# - Gestire i valori mancanti in modo appropriato, considerando l'imputazione o la rimozione delle righe.
# • Verificare e correggere eventuali anomalie nei dati (es. età negative, tariffe mensili irrealistiche).
# 3. Analisi Esplorativa dei Dati (EDA):
# Creare nuove colonne che potrebbero essere utili, come Costo_per_GB (tariffa mensile divisa per i dati consumati). Utilizzare groupby() 
# per esplorare la relazione tra Età, Durata_Abonnamento, Tariffa_Mensile e la Churn.
# Utilizzare metodi come corr() per identificare possibili correlazioni tra le variabili.
# 4. Preparazione dei Dati per la Modellazione:
# • Convertire la colonna Churn in formato numerico (0 per "No", 1 per "Si").
# Normalizzare le colonne numeriche usando numpy per prepararle per la modellazione.
# 5. Analisi Statistica e Predittiva:
# Implementare un semplice modello di regressione logistica usando scikit-learn per predire la probabilità di churn basata su altri fattori.
# Valutare la performance del modello attraverso metriche come l'accuratezza e l'AUC (Area Under Curve).
import pandas as pd

class DataContainer:
  def __init__(self):
    self.file_path = 'MyCsv/dati_telecom.csv'
    self.df = self.take_data()
    self.dfNormalize = None

  def take_data(self):
    # Carica il CSV
    df = pd.read_csv(self.file_path)

    print("-----\nINFO:")
    print(df.info())

    print("\n-----\nDESCRIBE:")
    print(df.describe())

    if 'Churn' in df.columns:
      print("\n-----\nDISTRIBUZIONE 'Churn':")
      print(df['Churn'].value_counts())

    # Gestione dei valori mancanti
    for column in df.columns:
      if df[column].isnull().sum() > 0:
          if df[column].dtype == 'object':
            moda = df[column].mode()[0]
            df[column].fillna(moda, inplace=True)
          else:
            media = df[column].mean()
            df[column].fillna(media, inplace=True)

    # Correzione anomalie
    if 'Età' in df.columns:
      df = df[df['Età'] > 0]  # Età positive

    if 'Tariffa_Mensile' in df.columns:
      df = df[(df['Tariffa_Mensile'] >= 5) & (df['Tariffa_Mensile'] <= 150)]  # range plausibile

    return df

  def create_costo_per_gb(self):
    # Creazione della colonna Costo_per_GB
    if 'Tariffa_Mensile' in self.df.columns and 'Dati_Consumati' in self.df.columns:
      self.df['Costo_per_GB'] = self.df.apply(
          lambda row: round(row['Tariffa_Mensile'] / row['Dati_Consumati'], 2)  if row['Dati_Consumati'] > 0 else 0,
          axis=1
      )
  
  def calcola_correlazione(self):
    # Calcolo delle correlazioni
    corr_matrix = self.df[['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Costo_per_GB']].corr()
    print("\n-----\n Matrice di correlazione:")
    print(corr_matrix)
  
  def conversione_dati_churm(self):
    if 'Churn' in self.df.columns:
        self.df['Churn'] = self.df['Churn'].map({'No': 0, 'Si': 1})
  
  def mostra_dati(self):
    print("\n-----\nDati Attuali:")
    print(self.df)
  
  def normalize_data(self):
    # Normalizzazione delle colonne numeriche
    numeriche = ['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Costo_per_GB']
    self.dfNormalize = self.df
    for col in numeriche:
        if col in self.dfNormalize.columns:
            min_val =  self.dfNormalize[col].min()
            max_val =  self.dfNormalize[col].max()
            self.dfNormalize[col] = ( self.dfNormalize[col] - min_val) / (max_val - min_val) 
  
  def mostra_dati_normalize(self):
    print("\n-----\nDati Attuali Normalizzati:")
    print(self.dfNormalize)


# Funzione per il menu 
def menu():
  dc = DataContainer()

  while True:
    print("\n----- Menu -----")
    print("1. Mostra informazioni sul dataset")
    print("2. Calcola costo per GB")
    print("3. Calcola correlazione")
    print("4. Converti 'Churn' in valori numerici e normalizzare i dati numerici")
    print("5. Crea DataSet Normalizzato")
    print("6. Mostra il dataset originale")
    print("7. Mostra il dataset normalizzato")
    print("8. Esci")
    scelta = input("Scegli un'opzione (1-6): ")

    match scelta:
      case "1":
        dc.take_data()
      case "2":
        dc.create_costo_per_gb()
        print("Colonna 'Costo_per_GB' creata.")
      case "3":
        dc.calcola_correlazione()
      case "4":
        dc.conversione_dati_churm()
        dc.normalize_data()
        print("Colonna 'Churn' convertita in valori numerici")
      case '5':
        dc.normalize_data()
        dc.mostra_dati_normalize()
      case "6":
        dc.mostra_dati()
      case "8":
        dc.mostra_dati_normalize()
      case "8":
        print("Uscita in corso...")
        break
      case _:
        print("Opzione non valida, riprova.")

# Avvia il menu
if __name__ == "__main__":
  menu()

