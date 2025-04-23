#Seaborn lavora in tandem con matplotlib, quindi molte delle impostazoioni di stile
#di seaborn influenzeranno o grafici creati con matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# === DATI DI ESEMPIO ===

#plt.rcParams['figure.figsize'] = [10,6]
# Imposta la dimensione predefinita delle figure

#plt.rcParams['figure.dpi'] = 100
# Imposta la risoluzione delle figure in DPI

# Puoi anche impostare caratteristiche come il colore di sfondo, il tipo di font ecc..
#plt.rcParams['figure.facecolor'] = 'white' # Colore di sfondo della figure


# === ES2 ===
def es2():
  # Configura il tema di Seaborn per i grafici
  # "darkgrid" aggiunge una griglia di sfondo scura utile per interpretare meglio i dati
  sns.set_theme(style="darkgrid")

  # Crea un array di 100 numeri casuali estratti da una distribuzione normale standard (media=0, deviazione standard=1)
  data = np.random.normal(size=100)

  # Crea un istogramma con curva KDE (Kernel Density Estimate)
  # L'istogramma mostra la frequenza dei valori, la KDE rappresenta una stima liscia della distribuzione dei dati
  sns.histplot(data, kde=True)

  # Aggiunge un titolo al grafico
  plt.title('Distribuzione dei dati')

  # Mostra il grafico
  plt.show()

# === ES3 ===
def es3():
  # La 'figura' rappresenta l'intera area del disegno (può contenere uno o più grafici)
  fig = plt.figure()  # Crea una nuova figura vuota

  # Gli 'axes' sono ciò che comunemente chiamiamo "grafico": un sistema di assi x e y
  # Una figura può contenere più oggetti axes (es. in un layout con più subplot)
  ax = fig.add_subplot(111)  # Aggiunge un oggetto axes alla figura (1 riga, 1 colonna, primo subplot)

  # Aggiungo un titolo
  ax.set_title('Istogramma dei dati')

  # Mando il diagramma
  plt.show()

# === Grafico a line ===
def grafico_line():
  # Dati da plottare: ascisse (x) e ordinate (y)
  x = [1, 2, 3, 4, 5]  # Valori sull'asse X
  y = [2, 3, 5, 7, 11] # Valori sull'asse Y (in questo caso, numeri primi)

  # Crea una nuova figura per il grafico
  plt.figure()
  # Crea un grafico a linee con i dati forniti
  plt.plot(x, y)
  # Aggiunge un titolo al grafico
  plt.title('Grafico a linee')
  # Etichetta per l'asse X
  plt.xlabel('X Axis')
  # Etichetta per l'asse Y
  plt.ylabel('Y Axis')
  # Mostra il grafico
  plt.show()

# === Grafico a Barre ===
def grafico_barre():
  # Categorie (asse X) e valori (altezza barre)
  categorie = ['a', 'b', 'c', 'd', 'e']
  valori = [3, 7, 2, 5, 8]

  # Crea una nuova figura
  plt.figure()
  # Crea il grafico a barre
  plt.bar(categorie, valori, color='lightgreen', edgecolor='black')
  # Aggiunge titolo e etichette
  plt.title('Grafico a barre - Valori per categoria')
  plt.xlabel('Categorie')
  plt.ylabel('Valori')
  # Mostra il grafico
  plt.show()

# === Istogramma ===
def istogramma():
  # Genera 1000 numeri casuali distribuiti normalmente (media=0, deviazione standard=1)
  data = np.random.randn(1000)
  # Crea una nuova figura per il grafico
  plt.figure()
  # === Crea un istogramma dei dati ===
  # 'bins=30' divide i dati in 30 intervalli → maggiore dettaglio sulla distribuzione
  plt.hist(data, bins=30, color='skyblue', edgecolor='black')
  # Aggiunge un titolo al grafico
  plt.title('Istogramma')
  # Etichetta per l'asse X
  plt.xlabel('Valori')
  # Etichetta per l'asse Y
  plt.ylabel('Frequenza')
  # Mostra il grafico
  plt.show()
  
# === Scatter Plot ===
def scatter_plot():
  """Crea un grafico a dispersione (scatter plot) con 50 punti casuali."""
  
  # Genera 50 valori casuali per l'asse X e 50 per l'asse Y
  x = np.random.rand(50)  # 50 numeri casuali tra 0 e 1 per l'asse X
  y = np.random.rand(50)  # 50 numeri casuali tra 0 e 1 per l'asse Y

  # Crea una nuova figura per il grafico
  plt.figure()
  # Crea il grafico a dispersione (scatter plot) con i punti (x, y)
  plt.scatter(x, y)
  # Aggiungi un titolo al grafico
  plt.title('Scatter Plot')
  # Etichetta per l'asse X
  plt.xlabel('X Axis')
  # Etichetta per l'asse Y
  plt.ylabel('Y Axis')
  # Mostra il grafico
  plt.show()
