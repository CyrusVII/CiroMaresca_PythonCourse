# 1. Capire la struttura e le colonne
# Quali sono le colonne disponibili nel dataset?
# Che tipo di dati contiene ciascuna colonna? (numerico, categorico, testo, booleano?)
# Ci sono colonne che sembrano superflue o irrilevanti? (es: PassengerId, Name, Ticket)
# Qual è il target (obiettivo) che vogliamo prevedere?

# 2. Pulizia dei dati (missing values e qualità)
# Ci sono colonne con valori mancanti (null o NaN)?
# ➔ Quali colonne e in quale percentuale?
# Come possiamo gestire i valori mancanti? (eliminazione, imputazione media/moda, altro?)
# Alcune colonne hanno troppi valori unici per essere utili? (es: Cabin, Ticket)
# Alcune colonne hanno dati "sporchi" (errori evidenti, formati incoerenti)?

# 5. Relazioni tra le colonne tra loro
# L'età (Age) varia in base alla classe (Pclass)?
# I passeggeri che hanno pagato di più (Fare) viaggiavano sempre in prima classe (Pclass = 1)?
# La dimensione della famiglia (SibSp + Parch) influenza la sopravvivenza?

# 6. Creazione di nuove feature utili
# È utile combinare SibSp e Parch per ottenere una nuova feature tipo "FamilySize"?
# È utile creare una feature "IsAlone" (1 se passeggero solo, 0 altrimenti)?
# È utile estrarre il titolo (Mr, Mrs, Miss, Master, ecc.) dal nome (Name)?

# 7. Preparazione finale prima dei modelli
# Ci sono colonne categoriche che devono essere codificate? (Sex, Embarked, Title) ➔ (LabelEncoder o get_dummies?)
# È necessario normalizzare o scalare le variabili numeriche? (es: Age, Fare)
# Quali feature teniamo, quali eliminiamo?

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV,train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report

#--------------------------
# === TAKE DATA DAL DATASET ===
def take_data():
  
  # Carica i dati
  df = pd.read_csv('MyCsv/train.csv')

  # 1. Rimuovi colonne non informative per analisi visive generali
  df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

  # 2. Gestione valori mancanti
  df['Age'].fillna(df['Age'].median(), inplace=True)
  df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

  # 3. Codifica variabili categoriche
  df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

  # 4. Conversione tipi e ordinamento se necessario
  df = df.astype({'Sex': 'int64'})

  # Dataframe pulito pronto per grafici
  print(df.head())
  
  return df

#--------------------------
# === ANALISI A COLONNE ===

# Qual è la distribuzione delle età (Age) dei passeggeri?
def age_distribution(df):
  #Crea l'istogramma della distribuzione delle età
  sns.histplot(data=df, x='Age', bins=30, kde=True, color='skyblue')

  # Aggiungi titolo e etichette
  plt.title('Distribuzione delle età dei passeggeri del Titanic')
  plt.xlabel('Età')
  plt.ylabel('Numero di passeggeri')

  # Mostra il grafico
  plt.show()

# Come è distribuito il prezzo del biglietto (Fare)?
def ticket_price(df):
  # Istogramma della distribuzione dei prezzi dei biglietti
  sns.histplot(data=df, x='Fare', bins=40, kde=True, color='orange')

  plt.title('Distribuzione del prezzo del biglietto (Fare)')
  plt.xlabel('Prezzo del biglietto')
  plt.ylabel('Numero di passeggeri')
  plt.show()

# Quali sono i valori unici nelle colonne categoriche (Sex, Embarked, Pclass)?
def unique_val_sep(df):
  # Visualizza i valori unici per ciascuna colonna categorica
  print("Valori unici in 'Sex':", df['Sex'].unique())
  print("Valori unici in 'Embarked':", df['Embarked'].unique())
  print("Valori unici in 'Pclass':", df['Pclass'].unique())

# Alcune categorie sono sbilanciate (es: molti più uomini che donne)?
def balance_unique(df):
  # Imposta il layout dei grafici
  fig, axes = plt.subplots(1, 3, figsize=(18, 5))

  # Grafico distribuzione 'Sex'
  sns.countplot(ax=axes[0], data=df, x='Sex', palette='pastel')
  axes[0].set_title("Distribuzione per Sesso")
  axes[0].set_ylabel("Numero di passeggeri")
  axes[0].set_xticklabels(['Maschio', 'Femmina'])

  # Grafico distribuzione 'Embarked'
  sns.countplot(ax=axes[1], data=df, x='Embarked', palette='muted')
  axes[1].set_title("Distribuzione per Porto d'Imbarco")
  axes[1].set_ylabel("Numero di passeggeri")

  # Grafico distribuzione 'Pclass'
  sns.countplot(ax=axes[2], data=df, x='Pclass', palette='Set2')
  axes[2].set_title("Distribuzione per Classe")
  axes[2].set_ylabel("Numero di passeggeri")

  plt.tight_layout()
  plt.show()

#--------------------------
# === Relazioni tra le colonne e il target (Survived) ===

# La probabilità di sopravvivenza cambia a seconda del sesso (Sex)?
def sex_prob_alive(df):
  # Crea un grafico a barre della sopravvivenza in base al sesso, separando sopravvissuti e non sopravvissuti
  plt.figure(figsize=(10, 6))
  ax = sns.countplot(data=df, x='Sex', hue='Survived', palette='Set2')

  # Aggiungi titolo e etichette
  plt.title('Distribuzione di sopravvissuti e non sopravvissuti per sesso')
  plt.xlabel('Sesso')
  plt.ylabel('Numero di passeggeri')

  # Modifica le etichette dell'asse x per rappresentare maschio e femmina
  plt.xticks([0, 1], ['Maschio', 'Femmina'])

  # Personalizza la legenda per sostituire "0" e "1" con "Non Sopravvissuto" e "Sopravvissuto"
  handles, labels = ax.get_legend_handles_labels()
  labels = ['Non Sopravvissuto', 'Sopravvissuto']
  ax.legend(handles, labels, title='Sopravvivenza')
  
  # Mostra il grafico
  plt.tight_layout()
  plt.show()

# La sopravvivenza dipende dalla classe di viaggio (Pclass)?
def clas_prob_alive(df):
  # Crea un grafico a barre della sopravvivenza per classe, separando sopravvissuti e non sopravvissuti
  fig, axes = plt.subplots(1, 3, figsize=(18, 6))

  # Per ciascuna classe
  for i, pclass in enumerate([1, 2, 3]):
    # Filtra i dati per la classe corrente
    class_data = df[df['Pclass'] == pclass]
    
    # Crea un countplot separato per i sopravvissuti e non sopravvissuti
    sns.countplot(ax=axes[i], data=class_data, x='Survived', palette='Set2')

    # Imposta il titolo e le etichette
    axes[i].set_title(f"Sopravvissuti e non sopravvissuti - Classe {pclass}")
    axes[i].set_xlabel('Sopravvissuti')
    axes[i].set_ylabel('Numero di passeggeri')
    axes[i].set_xticklabels(['Non Sopravvissuti', 'Sopravvissuti'])

  plt.tight_layout()
  plt.show()

# I bambini (Age) hanno avuto più probabilità di sopravvivere rispetto agli adulti?
def age_prob_alive(df):
  # Crea le fasce di età
  age_bins = [0, 12, 18, 30, 40, 50, 60, 100]  # Fasce di età
  age_labels = ['0-12', '13-18', '19-30', '31-40', '41-50', '51-60', '60+']  # Etichette per le fasce
  df['AgeGroup'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=False)

  # Crea un grafico a barre della sopravvivenza in base alle fasce di età, separando sopravvissuti e non sopravvissuti
  plt.figure(figsize=(10, 6))
  sns.countplot(data=df, x='AgeGroup', hue='Survived', palette='Set2')

  # Aggiungi titolo e etichette
  plt.title('Distribuzione di sopravvissuti e non sopravvissuti per fasce di età')
  plt.xlabel('Fasce di Età')
  plt.ylabel('Numero di passeggeri')

  # Personalizza la legenda
  handles, labels = plt.gca().get_legend_handles_labels()
  labels = ['Non Sopravvissuto', 'Sopravvissuto']
  plt.gca().legend(handles, labels, title='Sopravvivenza')

  # Mostra il grafico
  plt.tight_layout()
  plt.show()
# L’imbarco in una certa città (Embarked) ha influenzato la sopravvivenza?
# Il prezzo del biglietto (Fare) è correlato alla probabilità di sopravvivenza?

# === PREDICTION ===
def alive_prediction(df):
  # Prendi i dati
  X = df[['Age', 'Sex', 'Pclass']]
  y = df['Survived']

  # 2. Suddividi il dataset in training e test (80% training, 20% test)
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

  # 3. Definisci i parametri per GridSearchCV
  param_grid = {
    'criterion': ['gini', 'entropy'],           # Tipo di criterio per l'albero
    'max_depth': [None, 10, 20, 30],            # Profondità massima
    'min_samples_split': [2, 5, 10],            # Minimo di campioni per dividere un nodo
    'min_samples_leaf': [1, 2, 4]               # Minimo di campioni per nodo foglia
  }

  # 4. Crea il modello DecisionTreeClassifier
  model = DecisionTreeClassifier(random_state=42)

  # 5. Crea il GridSearchCV per trovare i migliori parametri
  grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=-1)

  # 6. Fai il fit con i dati di addestramento
  grid_search.fit(X_train, y_train)

  # 7. Mostra i migliori parametri trovati
  print(f"Migliori parametri trovati: {grid_search.best_params_}")

  # 8. Usa il miglior modello per fare previsioni
  best_model = grid_search.best_estimator_
  y_pred = best_model.predict(X_test)

  # 9. Calcola e stampa l'accuratezza
  accuracy = accuracy_score(y_test, y_pred)
  print(f"Accuratezza del modello con GridSearch: {accuracy * 100:.2f}%")

  # 10. Stampa il classification report
  print(classification_report(y_test, y_pred, target_names=['Non Sopravvissuto', 'Sopravvissuto']))

  # 11. Calcola la matrice di confusione
  cm = confusion_matrix(y_test, y_pred)

  # 12. Visualizza la matrice di confusione
  plt.figure(figsize=(6, 5))
  sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Non Sopravvissuto', 'Sopravvissuto'], yticklabels=['Non Sopravvissuto', 'Sopravvissuto'])
  plt.title('Matrice di Confusione con GridSearch')
  plt.xlabel('Predizione')
  plt.ylabel('Valore Reale')
  plt.show()

# === MENU ===
def menu():
  df = take_data()
  while True:
    print("--- Menu ---")
    print("0. Exit")
    print('1. Distribuzione Eta passegeri')
    print('2. Distribuzione Ticket price')
    print("3. Valori Unici Sex, Embarked, Pclass ")
    print("4. Grafico valori unici")
    print("5. Grafico di sopravvivenza per sesso")
    print("6. Probabilita di sopravvivenza per classe")
    print("7. Sopravvivenza per fascie di eta")
    print("8. Prediction")
    ch = input("---> ")
    match ch:
      case "0":
        print("Exit...")
        break
      case "1":
        age_distribution(df)
      case "2":
        ticket_price(df)
      case"3":
        unique_val_sep(df)
      case "4":
        balance_unique(df)
      case"5":
        sex_prob_alive(df)
      case "6":
        clas_prob_alive(df)
      case "7":
        age_prob_alive(df)
      case "8":
        alive_prediction(df)

# === AVVIO ===
if __name__ == "__main__":
  menu()
