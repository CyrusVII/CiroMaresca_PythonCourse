# Apri il file CSV
#'r': Modalità lettura. Apre il file per la lettura. Se il file non esiste, viene sollevato un errore
#'w': Modalità scrittura. Apre il file per la scrittura. Se il file esiste già, il suo contenuto verrà
#'a': Modalità append. Apre il file per aggiungere nuovi dati alla fine. Se il file non esiste, verrà creato.
#'x': Modalità creazione. Apre il file per la scrittura, ma se il file esiste già, solleva un errore (FileExistsError).
#'b': Modalità binaria. Usa questa modalità insieme a una delle altre modalità (ad esempio 'rb' o 'wb') per lavorare con file binari (ad esempio immagini o file audio).
#'t': Modalità testo (default). Usa questa modalità per lavorare con file di testo (come CSV, TXT, ecc.). Non è necessario specificarla esplicitamente, è la modalità predefinita.
#'r+': Modalità lettura e scrittura. Apre il file sia per la lettura che per la scrittura. Se il file non esiste, solleva un errore.
#'w+': Modalità lettura e scrittura. Apre il file per la lettura e la scrittura. Se il file esiste, viene sovrascritto; se non esiste, viene creato.
#'a+': Modalità lettura e append. Apre il file per lettura e aggiunta. Se il file non esiste, viene creato.
#per leggere 
#with open("annual-enterprise-survey-2023-financial-year-provisional-size-bands.csv", 'r', encoding='utf-8') as f:
#     lines = f.readlines()

# # Elabora ogni riga
# for line in lines:
#     # Rimuove newline e divide per virgola
#     fields = line.strip().split(',')
#     print(fields)

import csv
# Dati da scrivere nel file CSV
dati = [
    ['Nome', 'Cognome', 'Età'],  # Intestazione
    ['Mario', 'Rossi', 30],
    ['Luca', 'Bianchi', 25],
    ['Giulia', 'Verdi', 28]
]
# Apri il file in modalità scrittura ('w')
with open('csvFolder/file.csv', 'w', newline='', encoding='utf-8') as f:
    # Crea un oggetto writer per scrivere nel file
    writer = csv.writer(f)
    # Scrivi i dati nel file
    writer.writerows(dati)  # Scrive tutte le righe in una volta

print("File CSV scritto con successo.")
