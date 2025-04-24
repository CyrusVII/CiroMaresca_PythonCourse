# Importiamo la libreria seaborn per il caricamento dei dati e la creazione del grafico
#familiarizza con i grafici heatmaps , pair plots, facet grids e violin plots 
import seaborn as sns
import matplotlib.pyplot as plt

# === ES1 ===
# Carichiamo un dataset di esempio chiamato 'tips' da seaborn
# tips = sns.load_dataset('tips')

# # Creiamo un grafico a barre che mostra il totale dei conti (total_bill) per ciascun giorno (day)
# sns.barplot(x='day', y='total_bill', data=tips)

# # Aggiungiamo un titolo al grafico
# plt.title('Conto totale per giorno')

# # Mostriamo il grafico
# plt.show()


# === ES2 ===

# Carica il dataset 'fmri'
# fmri = sns.load_dataset('fmri')

# # Crea il grafico a linee
# sns.lineplot(x="timepoint", y="signal", data=fmri, hue="region", style="event")

# # Aggiungi un titolo al grafico
# plt.title('Segnale FMRI nel Tempo')

# # Mostra il grafico
# plt.show()

# === ES3 === 

# Generare dati casuali
# Carica il dataset "penguins"
data = sns.load_dataset("penguins")

# Crea un istogramma con KDE (stima della densità di probabilità)
sns.histplot(data=data, x="flipper_length_mm", kde=True)
# Aggiungi un titolo al grafico
plt.title('Distribuzione Lunghezza Pinne dei Pinguini')
# Mostra il grafico
plt.show()