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
