# importing important libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
# import matplotlib # Già importato da matplotlib.pyplot

# Per scaling selettivo e gestione categoriche
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline # Utile per workflow complessi, ma non strettamente necessaria qui

# Per modelli e valutazione
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, BayesianRidge # Aggiunto Lasso, Ridge se li vuoi
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Imposta uno stile per i plot (opzionale)
plt.style.use('seaborn-v0_8-whitegrid') # Uno stile più neutro rispetto a ggplot

print("========== Inizio Esecuzione Script di Analisi e Modellazione ==========")

# --- Caricamento e Pulizia Dati Iniziale ---
print("\n--- Caricamento Dati ---")
# reading the data
try:
    data_abb=pd.read_csv('AirBNB.csv')
    print("Dataset 'AirBNB.csv' caricato con successo.")
    print(f"Dimensioni iniziali del dataset: {data_abb.shape}")
    # data_abb.head() # Stampare per debug
except FileNotFoundError:
    print("Errore: Il file 'AirBNB.csv' non trovato. Assicurati che sia nella directory corretta.")
    exit() # Esci se il file non è trovato

# Reset index per avere una colonna 'index' (come nel tuo script originale)
data_abb.reset_index(inplace=True)

# Drop della colonna 'id'
if 'id' in data_abb.columns:
    data_abb.drop('id',axis=1,inplace=True)
    print("Colonna 'id' rimossa.")
# data_abb.head() # Stampare per debug

# Riorganizzazione delle colonne (come nel tuo script originale, assicurandosi che esistano)
required_cols = ['name', 'host_id', 'host_name', 'neighbourhood_group', 'neighbourhood',
                 'latitude', 'longitude', 'room_type', 'minimum_nights',
                 'number_of_reviews', 'last_review', 'reviews_per_month',
                 'calculated_host_listings_count', 'availability_365','price']
# Mantieni solo le colonne richieste che esistono effettivamente nel DataFrame
existing_cols = [col for col in required_cols if col in data_abb.columns]
data_abb = data_abb[existing_cols]
print(f"Dataset riorganizzato con {len(existing_cols)} colonne.")
# data_abb.head() # Stampare per debug
# data_abb.shape # Stampare per debug

# Checking data info and missing values
print("\n--- Informazioni e Valori Mancanti ---")
data_abb.info()
print("\nValori mancanti per colonna:")
print(data_abb.isna().sum())

# Converting last_review to datetime and filling NaNs
# Filling NaN for reviews_per_month with 0
print("\n--- Gestione Valori Mancanti Specifici ---")
if 'last_review' in data_abb.columns:
    # Converti in datetime
    data_abb['last_review'] = pd.to_datetime(data_abb['last_review'], errors='coerce') # Usa errors='coerce' per gestire date non valide

    # Riempi i NaN in last_review con la data massima non-NaN o una data fittizia
    latest_review_date = data_abb['last_review'].dropna().max()
    if pd.isna(latest_review_date):
        latest_review_date = pd.to_datetime('1970-01-01') # Data fittizia se tutte le date sono NaN
        print("Nessuna data valida in 'last_review'. Riempimento con data fittizia 1970-01-01.")
    else:
         print(f"Data massima in 'last_review': {latest_review_date.date()}.")

    data_abb['last_review'].fillna(latest_review_date, inplace=True)
    print("'last_review' convertito in datetime e NaN riempiti.")
else:
    print("Colonna 'last_review' non trovata. Saltando gestione.")

if 'reviews_per_month' in data_abb.columns:
    data_abb['reviews_per_month'].fillna(0, inplace=True)
    print("'reviews_per_month' NaN riempiti con 0.")
else:
     print("Colonna 'reviews_per_month' non trovata. Saltando gestione.")

# Removing unwanted columns (testuali non usate nei modelli nel tuo script)
print("\n--- Rimozione Colonne Testuali ---")
cols_to_drop_text = ['name','host_name']
existing_cols_to_drop_text = [col for col in cols_to_drop_text if col in data_abb.columns]
if existing_cols_to_drop_text:
    data_abb.drop(existing_cols_to_drop_text, axis=1, inplace=True)
    print(f"Colonne testuali rimosse: {existing_cols_to_drop_text}")
else:
    print("Nessuna colonna testuale da rimuovere trovata.")

# Checking if any null values present now
print(f"\nNumero totale di valori NaN dopo la pulizia iniziale: {data_abb.isna().sum().sum()}")


# Filtering data based on price and availability
print("\n--- Filtraggio Righe ---")
initial_rows_filter = data_abb.shape[0]
data_abb = data_abb[(data_abb.price > 0) & (data_abb.availability_365 > 0)].copy() # Usa copy() dopo il filtraggio
rows_after_filter = data_abb.shape[0]
print(f"Righe prima del filtraggio (price > 0 e availability_365 > 0): {initial_rows_filter}")
print(f"Righe dopo il filtraggio: {rows_after_filter}")
print(f"Righe rimosse dal filtraggio: {initial_rows_filter - rows_after_filter}")

if data_abb.empty:
    print("\n⚠️ Nessuna riga rimasta dopo il filtraggio. Impossibile procedere con analisi e modellazione.")
    exit()

print("\n--- Statistiche Descrittive e Info Finali (Dopo Pulizia/Filtraggio) ---")
print(data_abb.describe())
data_abb.info()


# --- Esplorazione Dati e Visualizzazioni ---
print("\n--- Inizio Sezione Visualizzazioni ---")

# Setting figure size for visualizations
sns.set(rc={'figure.figsize':(10,8)})

# Plot: Hosts with the most listings
if 'host_id' in data_abb.columns:
    print("\nVisualizzazione: Hosts con più listings...")
    top_host=data_abb.host_id.value_counts().head(10)
    plt.figure(figsize=(10,8))
    viz_1=top_host.plot(kind='bar',cmap='plasma')
    viz_1.set_title('Hosts with the most listings in NYC')
    viz_1.set_ylabel('Count of listings')
    viz_1.set_xlabel('Host IDs')
    plt.xticks(rotation=45, ha='right') # Migliora rotazione etichette
    plt.tight_layout()
    plt.show()
else:
     print("\nColonna 'host_id' non trovata. Saltando visualizzazione 'Hosts con più listings'.")

# Plot: Total listings by Neighbourhood Group (sum of calculated_host_listings_count)
if 'neighbourhood_group' in data_abb.columns and 'calculated_host_listings_count' in data_abb.columns:
    print("\nVisualizzazione: Listings totali per Neighbourhood Group...")
    # Assicurati che neighbourhood_group sia di tipo stringa per il groupby
    data_abb['neighbourhood_group'] = data_abb['neighbourhood_group'].astype(str)
    a=data_abb.groupby('neighbourhood_group').calculated_host_listings_count.sum()
    plt.figure(figsize=(10,8))
    a.plot(kind='bar')
    plt.title('Total listings by Neighbourhood Group (sum of calculated_host_listings_count)')
    plt.xlabel('Neighbourhood Group')
    plt.ylabel('Total listings')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
else:
    print("\nColonne 'neighbourhood_group' o 'calculated_host_listings_count' non trovate. Saltando visualizzazione 'Listings totali per Neighbourhood Group'.")


# Plot: Count of listings by Neighbourhood Group
if 'neighbourhood_group' in data_abb.columns:
    print("\nVisualizzazione: Conteggio listings per Neighbourhood Group...")
    plt.figure(figsize=(10,8))
    sns.countplot(x='neighbourhood_group',data=data_abb)
    plt.title('Count of listings by Neighbourhood Group')
    plt.xlabel('Neighbourhood Group')
    plt.ylabel('Number of listings')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
else:
    print("\nColonna 'neighbourhood_group' non trovata. Saltando visualizzazione 'Conteggio listings per Neighbourhood Group'.")


# Plot: Number of unique Neighbourhoods per Neighbourhood Group
if 'neighbourhood_group' in data_abb.columns and 'neighbourhood' in data_abb.columns:
    print("\nVisualizzazione: Numero di quartieri unici per Neighbourhood Group...")
    # Assicurati che neighbourhood sia di tipo stringa per il nunique
    data_abb['neighbourhood'] = data_abb['neighbourhood'].astype(str)
    plt.figure(figsize=(10,8))
    data_abb.groupby('neighbourhood_group')['neighbourhood'].nunique().plot(kind='bar',colormap='Set3')
    plt.xlabel('Neighbourhood groups')
    plt.ylabel('Number of Neighbourhoods')
    plt.title('Number of unique Neighbourhoods per Neighbourhood Group')
    print('Numero di quartieri unici per gruppo di quartieri:\n{}'.format(data_abb.groupby('neighbourhood_group')['neighbourhood'].nunique()))
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
else:
    print("\nColonne 'neighbourhood_group' o 'neighbourhood' non trovate. Saltando visualizzazione 'Numero di quartieri unici per Neighbourhood Group'.")

if 'neighbourhood' in data_abb.columns:
    print('Total neighbourhoods in NYC in which listings are located: {}'.format(data_abb.neighbourhood.value_counts().sum()))
else:
    print("\nColonna 'neighbourhood' non trovata. Saltando conteggio totale quartieri.")


# Plot: Top/Least 10 neighbourhoods
if 'neighbourhood' in data_abb.columns:
    print("\nVisualizzazione: Top/Least 10 neighbourhoods...")
    plt.figure(figsize=(10,12)) # Ajusta la dimensione per due subplot verticali
    # Top 10 neighbourhoods in NYC
    plt.subplot(2,1,1) # Primo subplot nella griglia 2x1
    # Ottieni l'ordine dei top 10
    top_10_neighbourhoods_order = data_abb.neighbourhood.value_counts().iloc[:10].index
    sns.countplot(y='neighbourhood', data=data_abb, order=top_10_neighbourhoods_order,
                  edgecolor=(0,0,0), linewidth=1) # Riduci linewidth leggermente
    plt.title('Listings by Top 10 NYC Neighbourhoods')
    plt.xlabel('Number of Listings')
    plt.ylabel('Neighbourhood')

    # 10 Least preferred neighbourhood in NYC
    plt.subplot(2,1,2) # Secondo subplot nella griglia 2x1
    # Ottieni l'ordine dei least 10
    least_10_neighbourhoods_order = data_abb.neighbourhood.value_counts().iloc[-10:].index
    sns.countplot(y='neighbourhood', data=data_abb, order=least_10_neighbourhoods_order,
                  edgecolor=(0,0,0), linewidth=1) # Riduci linewidth leggermente
    plt.title('Listings by 10 Least Preferred NYC Neighbourhoods')
    plt.xlabel('Number of Listings')
    plt.ylabel('Neighbourhood')

    plt.tight_layout()
    plt.show()
else:
    print("\nColonna 'neighbourhood' non trovata. Saltando visualizzazioni Top/Least 10 neighbourhoods.")


# Plot: Room Type counts and percentage pie chart
if 'room_type' in data_abb.columns:
    print("\nVisualizzazione: Room Type counts e percentuale...")
    # Assicurati che room_type sia di tipo stringa per il countplot
    data_abb['room_type'] = data_abb['room_type'].astype(str)

    plt.figure(figsize=(10,8))
    sns.countplot(x='room_type',data=data_abb,edgecolor=sns.color_palette("dark", len(data_abb.room_type.unique()))) # Usa len(unique) per il numero di colori
    plt.title('Count of listings by Room Type')
    plt.xlabel('Room Type')
    plt.ylabel('Number of listings')
    plt.show()

    # Pie chart
    room_type_counts = data_abb.room_type.value_counts()
    room_type_percentage = (room_type_counts / room_type_counts.sum()) * 100
    print('Percentage of room types available in AirBnB registered listings are:\n {}'.format(room_type_percentage))

    plt.figure(figsize=(8,8))
    room_type_percentage.plot.pie(autopct='%.2f',fontsize=12, cmap='Set3') # Usa colormap per pie chart
    plt.title('Room types availability in AirBnB',fontsize=20)
    plt.ylabel('') # Rimuove etichetta y per grafico a torta
    plt.show()
else:
    print("\nColonna 'room_type' non trovata. Saltando visualizzazioni Room Type.")

# Plot: Neighbourhood Groups vs Room Types Availability (using countplot)
if 'neighbourhood_group' in data_abb.columns and 'room_type' in data_abb.columns:
    print("\nVisualizzazione: Neighbourhood Groups vs Room Types Availability...")
    # Assicurati che entrambe le colonne siano di tipo stringa/categoria per il countplot
    data_abb['neighbourhood_group'] = data_abb['neighbourhood_group'].astype(str)
    data_abb['room_type'] = data_abb['room_type'].astype(str)

    plt.figure(figsize=(10,8))
    sns.countplot(y='neighbourhood_group', hue='room_type', data=data_abb)
    plt.xlabel('Number of Listings')
    plt.ylabel('Neighbourhood Groups')
    plt.title('Neighbourhood Groups vs Room Types Availability')
    plt.show()
else:
    print("\nColonne 'neighbourhood_group' o 'room_type' non trovate. Saltando visualizzazione 'Neighbourhood Groups vs Room Types'.")


# Plot: Listings count by Price Range and Room Type per Neighbourhood Group
if 'price' in data_abb.columns and 'neighbourhood_group' in data_abb.columns and 'room_type' in data_abb.columns:
    print("\nVisualizzazione: Listings count by Price Range and Room Type per Neighbourhood Group...")
    # setting up bins for price
    # Assicurati che price sia numerico valido (già filtrato price > 0)
    # q=10 crea 10 bin. duplicates='drop' gestisce casi con molti valori uguali.
    try:
        data_abb['price_range'] = pd.qcut(data_abb['price'], q=10, labels=False, duplicates='drop')
        print("'price_range' creato con successo.")

        # Assicurati che neighbourhood_group e room_type siano stringa/categoria
        data_abb['neighbourhood_group'] = data_abb['neighbourhood_group'].astype(str)
        data_abb['room_type'] = data_abb['room_type'].astype(str)

        neighbourhood_groups = list(data_abb.neighbourhood_group.unique())
        n_groups = len(neighbourhood_groups)
        # Calcola le dimensioni della griglia dei subplot
        n_cols = 2
        n_rows = (n_groups + n_cols - 1) // n_cols # Calcolo ceiling division

        plt.figure(figsize=(10 * n_cols, 8 * n_rows)) # Ajusta la dimensione della figura

        for i, neighbour in enumerate(neighbourhood_groups):
            plt.subplot(n_rows, n_cols, i + 1)
            subset = data_abb[data_abb['neighbourhood_group'] == neighbour]
            if not subset.empty:
                 sns.countplot(y='price_range', hue='room_type', data=subset)
                 plt.xlabel('Number of listings')
                 plt.ylabel('Price range index')
                 plt.title(f'Listings count by Price Range and Room Type in {neighbour}')
            else:
                 plt.title(f'{neighbour} (No data)')
                 plt.text(0.5, 0.5, 'No data', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)


        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Errore durante la creazione o il plotting di 'price_range': {e}")
        print("Saltando visualizzazione 'Listings count by Price Range...'.")

else:
    print("\nColonne necessarie ('price', 'neighbourhood_group', 'room_type') non trovate per visualizzazione 'Listings count by Price Range...'.")


# Plot: Neighbourhood Group price distribution < 500
if 'price' in data_abb.columns and 'neighbourhood_group' in data_abb.columns:
    print("\nVisualizzazione: Distribuzione prezzi (< 500) per Neighbourhood Group...")
    g = data_abb[data_abb.price < 500].copy() # Usa copy() dopo il filtraggio
    if not g.empty:
        plt.figure(figsize=(10,6))
        sns.boxplot(y="price",x ='neighbourhood_group' ,data = g)
        plt.title("Neighbourhood Group price distribution for listings < 500")
        plt.xlabel('Neighbourhood Group')
        plt.ylabel('Price')
        plt.show()
    else:
        print("Nessun dato con price < 500 per visualizzazione.")
else:
     print("\nColonne necessarie ('price', 'neighbourhood_group') non trovate per visualizzazione 'Distribuzione prezzi (< 500)...'.")


# Plot: Borough wise price distribution (using kdeplot)
if 'price' in data_abb.columns and 'neighbourhood_group' in data_abb.columns:
    print("\nVisualizzazione: Distribuzione prezzi per Borough (KDE)...")
    # Assicurati che price sia numerico valido e neighbourhood_group sia stringa/categoria
    data_abb['neighbourhood_group'] = data_abb['neighbourhood_group'].astype(str)

    plt.figure(figsize=(10,6))
    # Usa kdeplot o histplot per la stima della densità/distribuzione
    # Filtra price < 2000 come nel tuo script originale
    subset_price_filtered = data_abb[data_abb.price < 2000].copy() # Usa copy()
    if not subset_price_filtered.empty:
        sns.kdeplot(data=subset_price_filtered, x='price', hue='neighbourhood_group', common_norm=False) # common_norm=False per densità per gruppo

        plt.title('Borough wise price distribution for price < 2000')
        plt.xlabel('Price')
        plt.ylabel('Density')
        plt.xlim(0, 2000)
        plt.legend(title='Boroughs')
        plt.show()
    else:
        print("Nessun dato con price < 2000 per visualizzazione distribuzione prezzi.")
else:
     print("\nColonne necessarie ('price', 'neighbourhood_group') non trovate per visualizzazione 'Distribuzione prezzi per Borough...'.")


# Plot: Minimum nights vs Price Range per Room Type (Boxplot)
if 'minimum_nights' in data_abb.columns and 'price_range' in data_abb.columns and 'room_type' in data_abb.columns:
    print("\nVisualizzazione: Minimum Nights vs Price Range per Room Type...")
    # Assicurati che le colonne siano tipi adatti
    data_abb['room_type'] = data_abb['room_type'].astype(str) # Assicurati che room_type sia stringa/categoria
    # 'price_range' dovrebbe essere già numerico o categorico a seconda di come lo crei
    # Filtra minimum_nights se ci sono outlier estremi che rendono il plot illeggibile
    subset_nights_filtered = data_abb[data_abb['minimum_nights'] < data_abb['minimum_nights'].quantile(0.99)].copy() # Filtra outlier (es. al 99mo percentile)

    rooms = list(subset_nights_filtered.room_type.unique())
    n_rooms = len(rooms)
    n_cols_rooms = 3 # Esempio: 3 colonne di subplot
    n_rows_rooms = (n_rooms + n_cols_rooms - 1) // n_cols_rooms

    plt.figure(figsize=(6 * n_cols_rooms, 5 * n_rows_rooms)) # Ajusta la dimensione

    for i, room in enumerate(rooms):
        plt.subplot(n_rows_rooms, n_cols_rooms, i + 1)
        subset = subset_nights_filtered[subset_nights_filtered.room_type == room]
        if not subset.empty:
             sns.boxplot(data=subset, x='price_range', y='minimum_nights')
             plt.title(f'{room}') # Titolo solo con il tipo di stanza
             plt.xlabel('Price Range Index')
             plt.ylabel('Minimum Nights (Filtered)')
             plt.xticks(rotation=45, ha='right')
        else:
             plt.title(f'{room} (No data)')
             plt.text(0.5, 0.5, 'No data', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)

    plt.tight_layout()
    plt.show()
else:
     print("\nColonne necessarie ('minimum_nights', 'price_range', 'room_type') non trovate per visualizzazione 'Minimum Nights vs Price Range...'.")


# Scatter plot between minimum_nights and price
if 'minimum_nights' in data_abb.columns and 'price' in data_abb.columns:
    print("\nVisualizzazione: Price vs Minimum Nights (Scatterplot)...")
    plt.figure(figsize=(10,6))
    # Usa un campione casuale se il dataset è molto grande per il plotting scatter
    sample_size_scatter = 5000 # Dimensione del campione
    if data_abb.shape[0] > sample_size_scatter:
         plot_data_scatter = data_abb.sample(sample_size_scatter, random_state=42).copy()
         print(f"Plotting un campione casuale di {sample_size_scatter} punti.")
    else:
         plot_data_scatter = data_abb.copy()
         print(f"Plotting tutti i {data_abb.shape[0]} punti.")

    sns.scatterplot(data=plot_data_scatter, x='minimum_nights', y='price', alpha=0.3, s=5) # Riduci dimensione punti e aumenta trasparenza

    plt.title('Price vs Minimum Nights')
    plt.xlabel('Minimum Nights')
    plt.ylabel('Price')
    # Limita gli assi per gestire outlier se necessario
    # plt.xlim(0, 365) # Esempio
    # plt.ylim(0, 1000) # Esempio
    plt.show()
else:
     print("\nColonne necessarie ('minimum_nights', 'price') non trovate per visualizzazione 'Price vs Minimum Nights...'.")


# Geographic Distribution of Listings colored by Neighbourhood Group
# Aggiungo legend=False qui per uniformità, anche se l'errore sembra avvenire con hue numerici
if 'longitude' in data_abb.columns and 'latitude' in data_abb.columns and 'neighbourhood_group' in data_abb.columns:
    print("\nVisualizzazione: Distribuzione Geografica per Neighbourhood Group...")
    plt.figure(figsize=(10,8)) # Ajusta la dimensione
    # Assicurati che i dati siano validi per el plotting (no NaN nelle colonne usate)
    plot_data_geo_group = data_abb.dropna(subset=['latitude', 'longitude', 'neighbourhood_group']).copy()
    if not plot_data_geo_group.empty:
         sns.scatterplot(data=plot_data_geo_group,
                         x='longitude', y='latitude',
                         hue='neighbourhood_group', # Corretto: usa hue per colorare per categoria
                         s=10, alpha=0.6,
                         legend=False) # <--- Aggiunto legend=False

         plt.title('Geographic Distribution of Listings by Neighbourhood Group')
         plt.xlabel('Longitude')
         plt.ylabel('Latitude')
         plt.show()
    else:
        print("Nessun dato valido per visualizzazione 'Distribuzione Geografica per Neighbourhood Group'.")
else:
    print("\nColonne necessarie ('longitude', 'latitude', 'neighbourhood_group') non trovate per visualizzazione 'Distribuzione Geografica per Neighbourhood Group'.")


# Geographic Distribution colored by availability_365
# Questo è il plot che causa l'errore 'AttributeError: Line2D.set() got an unexpected keyword argument 'cmap''
# La soluzione è aggiungere legend=False
if 'longitude' in data_abb.columns and 'latitude' in data_abb.columns and 'availability_365' in data_abb.columns:
    print("\nVisualizzazione: Distribuzione Geografica per Availability_365...")
    plt.figure(figsize=(10,8)) # Ajusta la dimensione
    # Assicurati che i dati siano validi per el plotting (no NaN nelle colonne usate)
    plot_data_geo_avail = data_abb.dropna(subset=['latitude', 'longitude', 'availability_365']).copy()
    if not plot_data_geo_avail.empty:
        # Usa hue per colorare per valore numerico con colormap
        sns.scatterplot(data=plot_data_geo_avail,
                        x='longitude', y='latitude',
                        hue='availability_365', cmap='viridis', # Usa una colormap per dati numerici
                        edgecolor='black', linewidth=0.2, alpha=0.6, s=10,
                        legend=False) # <--- AGGIUNTA LA CORREZIONE QUI: Disabilita la legenda

        # Seaborn dovrebbe aggiungere la colorbar automaticamente con hue numerico.

        plt.title('Geographic Distribution colored by Availability (availability_365)')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.show()
    else:
        print("Nessun dato valido per visualizzazione 'Distribuzione Geografica per Availability_365'.")

else:
     print("\nColonne necessarie ('longitude', 'latitude', 'availability_365') non trovate per visualizzazione 'Distribuzione Geografica per Availability_365'.")


# Heatmap using folium (This generates an HTML map, not a static plot)
# if 'latitude' in data_abb.columns and 'longitude' in data_abb.columns:
#     print("\nCreazione mappa di calore con Folium (output HTML)...")
#     try:
#         import folium
#         from folium.plugins import HeatMap
#         # Assicurati che i dati per la heatmap siano numerici e non abbiano NaN
#         heatmap_data = data_abb[['latitude','longitude']].dropna().values.tolist() # Ottieni lista di liste
#         if heatmap_data: # Controlla se la lista non è vuota
#             m=folium.Map([40.7128,-74.0060],zoom_start=11)
#             HeatMap(heatmap_data,radius=8,gradient={0.2:'blue',0.4:'purple',0.6:'orange',1.0:'red'}).add_to(m)
#             # Per visualizzare la mappa, salvala in un file HTML
#             map_file = 'airbnb_heatmap.html'
#             m.save(map_file)
#             print(f"Mappa di calore salvata come {map_file}")
#             # Per aprirla automaticamente (potrebbe non funzionare in tutti gli ambienti)
#             # import webbrowser
#             # webbrowser.open(map_file)
#         else:
#             print("Nessun dato valido per creare la heatmap con Folium.")
#     except ImportError:
#         print("Libreria 'folium' non installata. Saltando la creazione della heatmap.")
#         print("Installa con: pip install folium")
#     except Exception as e:
#         print(f"Errore durante la creazione della heatmap con Folium: {e}")

# else:
#     print("\nColonne necessarie ('latitude', 'longitude') non trovate per creare la heatmap.")


# Analysis of top reviewed listings
if 'number_of_reviews' in data_abb.columns and 'price' in data_abb.columns and 'room_type' in data_abb.columns:
    print("\n--- Analisi Top 100 Listings Recensiti ---")
    #let's grab 100 most reviewed listings in NYC
    top_reviewed_listings=data_abb.nlargest(100,'number_of_reviews').copy() # Usa copy()
    # top_reviewed_listings # stampare per debug

    if not top_reviewed_listings.empty:
        price_avrg=top_reviewed_listings.price.mean()
        print('Average price per night for top 100 most reviewed listings: {}'.format(price_avrg))

        # top_reviewed_listings.groupby('room_type')['price'].describe() # stampare solo per debug

        print("\nVisualizzazione: Distribuzione prezzi (Top 100 recensiti) per Room Type...")
        plt.figure(figsize=(10,6))
        sns.boxplot(y='price',x='room_type',data=top_reviewed_listings)
        plt.title('Price Distribution by Room Type for Top 100 Most Reviewed Listings')
        plt.xlabel('Room Type')
        plt.ylabel('Price')
        plt.show()
    else:
        print("Nessuna listing trovata tra le top 100 recensite.")
else:
     print("\nColonne necessarie ('number_of_reviews', 'price', 'room_type') non trovate per analisi 'Top 100 Listings Recensiti'.")


# Distribution of minimum_nights (filtered)
if 'minimum_nights' in data_abb.columns:
    print("\nVisualizzazione: Distribuzione Minimum Nights (1-30)...")
    plt.figure(figsize=(10,6))
    # Usa histplot invece di distplot (deprecato)
    # Filtra minimum_nights tra 1 e 30 inclusi
    subset_min_nights = data_abb[(data_abb['minimum_nights'] >= 1) & (data_abb['minimum_nights'] <= 30)].copy()
    if not subset_min_nights.empty:
        sns.histplot(data=subset_min_nights, x='minimum_nights', bins=30, kde=True) # bins=30 per intervalli giornalieri da 1 a 30
        plt.title('Distribution of Minimum Nights (1-30)')
        plt.xlabel('Minimum Nights')
        plt.ylabel('Count')
        plt.show()
    else:
        print("Nessun dato con Minimum Nights tra 1 e 30 per visualizzazione.")
else:
     print("\nColonna 'minimum_nights' non trovata. Saltando visualizzazione 'Distribuzione Minimum Nights (1-30)'.")


# Distribution of log(Minimum Nights) with Normal Fit
if 'minimum_nights' in data_abb.columns:
    print("\nVisualizzazione: Distribuzione log(Minimum Nights) con Normal Fit...")
    # Filtra per valori > 0 prima del log
    min_nights_positive = data_abb[data_abb['minimum_nights'] > 0]['minimum_nights'].copy()
    if not min_nights_positive.empty:
         log_min_night = np.log(min_nights_positive)
         plt.figure(figsize=(10,6))
         # Usa histplot con kde=True e fit
         sns.histplot(log_min_night, kde=True, stat='density')

         # Fitta la distribuzione normale e plotta la PDF
         try:
             from scipy.stats import norm
             mu, std = norm.fit(log_min_night)
             xmin, xmax = plt.xlim()
             x = np.linspace(xmin, xmax, 100)
             p = norm.pdf(x, mu, std)
             plt.plot(x, p, 'k', linewidth=2, label=f'Normal Fit: mu={mu:.2f}, std={std:.2f}')
             plt.legend()
         except Exception as e:
             print(f"Errore durante il fitting o il plotting della distribuzione normale: {e}")


         plt.title('Distribution of log(Minimum Nights) with Normal Fit')
         plt.xlabel('log(Minimum Nights)')
         plt.ylabel('Density')
         plt.show()
    else:
        print("Nessun valore positivo in 'minimum_nights' per calcolare il log.")
else:
    print("\nColonna 'minimum_nights' non trovata. Saltando visualizzazione log(Minimum Nights).")


# --- Feature Engineering (Label Encoding) ---
# Applica Label Encoding alle colonne categoriche come nel tuo script originale
print("\n--- Feature Engineering (Label Encoding) ---")
cat_cols_for_le = ['neighbourhood_group', 'neighbourhood', 'room_type']
le = LabelEncoder()

for col in cat_cols_for_le:
    # Verifica se la colonna esiste E se è di tipo object o category (pre-conversione a stringa)
    if col in data_abb.columns:
         # Converti in stringa prima dell'encoding per gestire bene NaN o altri tipi
         original_dtype = data_abb[col].dtype
         data_abb[col] = data_abb[col].astype(str)
         # Aggiungi una verifica più robusta per identificare le colonne categoriche
         # Usa una soglia per il numero di valori unici rispetto al numero di righe
         # O verifica se il dtype originale non era numerico
         if original_dtype == 'object' or data_abb[col].nunique() < data_abb.shape[0]*0.1: # Esempio: meno del 10% di valori unici rispetto alle righe
             data_abb[col] = le.fit_transform(data_abb[col])
             print(f"Label Encoding applicato a '{col}'.")
         else:
             # Per le colonne che sembrano testuali ma con molti valori unici (come 'name'),
             # non vogliamo applicare Label Encoding. Queste dovrebbero idealmente essere rimosse prima.
             # Assicurati che le colonne non desiderate come 'name', 'host_name' siano rimosse.
             # Se altre colonne testuali con molti valori unici (es. recensioni testuali)
             # non sono state rimosse e non sono nel tuo X_cols per la modellazione,
             # questo avviso va bene.
             print(f"Colonna '{col}' non sembra categorica (dtype originale: {original_dtype}, valori unici: {data_abb[col].nunique()}). Saltando Label Encoding.")

    else:
        print(f"Colonna '{col}' non trovata per Label Encoding. Saltando.")

print("Feature Engineering (Label Encoding) completato.")
print("Esempio dtypes dopo LE:\n", data_abb.dtypes)


# --- Matrice di Correlazione (dopo Label Encoding) ---
print("\n--- Matrice di Correlazione (Numeriche e Label Encoded) ---")
# Calcola la matrice di correlazione sulle colonne numeriche (inclusi quelli Label Encoded)
# Escludi host_id perché è un identificativo numerico ma non una feature predittiva diretta in questo contesto
cols_for_corr = data_abb.select_dtypes(include=np.number).columns.tolist()
if 'host_id' in cols_for_corr:
    cols_for_corr.remove('host_id')
# Escludi 'index' aggiunto da reset_index se è numerico
if 'index' in cols_for_corr:
    cols_for_corr.remove('index')
# Escludi 'price_range' in quanto è derivata dal target 'price' e usata per plot
if 'price_range' in cols_for_corr:
     cols_for_corr.remove('price_range')


if len(cols_for_corr) > 1:
    correlation_matrix = data_abb[cols_for_corr].corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', annot_kws={"size": 8}) # Ajusta dimensione annotazioni
    plt.title('Matrice di Correlazione (Numeriche e Label Encoded Features)')
    plt.show()
else:
    print("Meno di due colonne numeriche/Label Encoded per visualizzare la matrice di correlazione.")
print("Fine generazione matrice di correlazione.")


# --- Preparazione Dati per Modellazione ---
print("\n--- Preparazione Dati per Modellazione ---")

# Setting the target variable (log10 transformed) and independent variables
# Usa le colonne Label Encoded per le feature categoriche
X_cols = ['latitude','longitude','minimum_nights','number_of_reviews','availability_365',
          'room_type','neighbourhood_group','neighbourhood', # Queste sono ora Label Encoded (int)
          'reviews_per_month','calculated_host_listings_count'] # Le altre numeriche

# Assicurati che tutte le colonne specificate per X esistano nel DataFrame
X_cols_existing = [col for col in X_cols if col in data_abb.columns]
missing_cols = [col for col in X_cols if col not in data_abb.columns]
if missing_cols:
    print(f"AVVISO: Le seguenti colonne specificate per le feature (X) non sono state trovate: {missing_cols}")

X = data_abb[X_cols_existing].copy() # Usa solo colonne esistenti e crea una copia
y = np.log10(data_abb['price']).copy() # Calcola il log del prezzo e crea una copia del risultato

# Verifica che X contenga solo dtypes numerici (int o float)
if not all(pd.api.types.is_numeric_dtype(X[col]) for col in X.columns):
    print("\nERRORE: X contiene colonne non numeriche dopo Feature Engineering. Verifica dtypes:")
    print(X.dtypes)
    print("Colonne non numeriche rilevate:", list(X.select_dtypes(exclude=np.number).columns))
    print("Impossibile procedere con la modellazione.")
    exit()
else:
    print("Dati feature (X) preparati e verificati come numerici.")
    print("Shape di X:", X.shape)
    print("Shape di y:", y.shape)


# Split train/test
print("\n--- Suddivisione Training/Test ---")
# Usa lo stesso random_state per split riproducibili
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42) # Usa un test_size e random_state

print(f"Shape X_train: {X_train.shape}, Shape X_test: {X_test.shape}")
print(f"Shape y_train: {y_train.shape}, Shape y_test: {y_test.shape}")
print("Suddivisione completata.")


# --- Scaling Features (Solo Numeriche Originali) ---
# Identifica le colonne che erano numeriche originali (float) vs quelle Label Encoded (int)
# e scala solo le prime.
print("\n--- Scaling Features Numeriche (Solo Float) ---")

# Le colonne Label Encoded sono ora int
# Le colonne numeriche originali (latitude, longitude, minimum_nights, number_of_reviews,
# reviews_per_month, calculated_host_listings_count, availability_365) dovrebbero essere float.
# Verifica i dtypes nel set di training per essere sicuro.
float_cols_train = X_train.select_dtypes(include=np.floating).columns.tolist()
int_cols_train = X_train.select_dtypes(include=np.integer).columns.tolist() # Queste non verranno scalate

print(f"Colonne da scalare (float): {float_cols_train}")
print(f"Colonne non scalate (int/Label Encoded): {int_cols_train}")


if float_cols_train:
    # Crea un ColumnTransformer per applicare lo StandardScaler solo alle colonne float
    # remainder='passthrough' mantiene le colonne int (Label Encoded) non scalate
    scaler_transformer = ColumnTransformer(
        transformers=[
            ('scaler', StandardScaler(), float_cols_train)
        ],
        remainder='passthrough'
    )

    # Applica scaling fit su training, transform su training e test
    X_train_scaled_array = scaler_transformer.fit_transform(X_train)
    X_test_scaled_array = scaler_transformer.transform(X_test)

    # Recupera i nomi delle colonne dopo la trasformazione
    scaled_feature_names = scaler_transformer.get_feature_names_out()
    # Rimuovi i prefissi aggiunti da ColumnTransformer ('scaler__')
    cleaned_feature_names = [name.replace('scaler__', '') for name in scaled_feature_names]

    # Converti gli array numpy risultanti in DataFrames, mantenendo gli indici originali
    X_train_scaled = pd.DataFrame(X_train_scaled_array, columns=cleaned_feature_names, index=X_train.index)
    X_test_scaled = pd.DataFrame(X_test_scaled_array, columns=cleaned_feature_names, index=X_test.index)

    print("Scaling colonne float completato.")
    # print("Esempio dtypes X_train_scaled:\n", X_train_scaled.dtypes)

else:
    print("Nessuna colonna float da scalare. Saltando lo scaling.")
    X_train_scaled = X_train.copy() # Usa copy()
    X_test_scaled = X_test.copy() # Usa copy()


print("Preparazione dati (split e scaling) completata.")


# --- Addestramento e Valutazione Modelli ---
print("\n--- Inizio Addestramento e Valutazione Modelli ---")

results = {}
preds = {} # Dizionario per memorizzare le predizioni per il plot finale

# Modelli Lineari (richiedono scaling)
print("\nAddestramento Modelli Lineari (su dati scalati)...")
models_linear = {
    "Linear Regression": LinearRegression(),
    "Bayesian Ridge":    BayesianRidge(),
    # "Ridge":  Ridge(alpha=1.0), # Esempio di altri modelli lineari
    # "Lasso":  Lasso(alpha=0.1),
}

for name, model in models_linear.items():
    print(f"Addestramento modello: {name}")
    try:
        # Allena sul dataset scalato
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
        results[name] = {
            'RMSE': np.sqrt(mean_squared_error(y_test, y_pred)),
            'R2':   r2_score(y_test, y_pred),
            'MAE':  mean_absolute_error(y_test, y_pred)
        }
        preds[name] = y_pred
        print(f"Valutazione {name} completata.")
    except Exception as e:
        print(f"Errore durante l'addestramento/valutazione per {name}: {e}")
        results[name] = {'RMSE': np.nan, 'R2': np.nan, 'MAE': np.nan}
        preds[name] = np.array([]) # Salva array vuoto per evitare errori successivi


# Modelli basati su Alberi (non richiedono scaling sui dati Label Encoded/Numerici)
print("\nAddestramento Modelli basati su Alberi (su dati non scalati)...")
models_tree = {
     "Decision Tree":     DecisionTreeRegressor(criterion='squared_error', max_depth=8, random_state=42), # max_depth di esempio, criterion='squared_error' corretto
     "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42),
}

for name, model in models_tree.items():
    print(f"Addestramento modello: {name}")
    try:
        # Allena sui dati NON SCALATI (contengono int da Label Encoding)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test) # Predici su dati NON SCALATI
        results[name] = {
            'RMSE': np.sqrt(mean_squared_error(y_test, y_pred)),
            'R2':   r2_score(y_test, y_pred),
            'MAE':  mean_absolute_error(y_test, y_pred)
        }
        preds[name] = y_pred
        print(f"Valutazione {name} completata.")

        # Esegui Cross-validation sul training set per questo modello (es. Gradient Boosting)
        if name == "Gradient Boosting": # Esempio di cross-val solo per uno dei modelli
             print(f"Esecuzione Cross-validation (cv=5) sul Training Set per {name}...")
             try:
                 # Usa X_train (non scalato per modelli ad albero) e y_train
                 cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='r2')
                 print(f"Score R2 di Cross-validation (cv=5) per {name}: {cv_scores}")
                 print(f"Media Score R2 di Cross-validation per {name}: {cv_scores.mean():.4f}") # Usa cv_scores.mean()
             except Exception as e:
                  print(f"Errore durante la cross-validation per {name}: {e}")


    except Exception as e:
        print(f"Errore durante l'addestramento/valutazione per {name}: {e}")
        results[name] = {'RMSE': np.nan, 'R2': np.nan, 'MAE': np.nan}
        preds[name] = np.array([]) # Salva array vuoto


# --- Riassunto Risultati ---
print("\n--- Risultati Valutazione Modelli (su Test Set) ---")
if not results:
     print("Nessun risultato di valutazione disponibile (tutti i modelli hanno fallito o sono stati saltati).")
else:
    # Ordina i modelli per R² (decrescente), gestendo i NaN
    sorted_results = sorted(results.items(), key=lambda item: item[1]['R2'] if not np.isnan(item[1]['R2']) else -1, reverse=True)

    print("{:<25} | {:<10} | {:<10} | {:<10}".format("Model", "RMSE", "R2 Score", "MAE"))
    print("-" * 60)
    for name, metrics in sorted_results:
        # Formatta l'output gestendo i NaN
        rmse_str = f"{metrics['RMSE']:.4f}" if not np.isnan(metrics['RMSE']) else "N/A "
        r2_str = f"{metrics['R2']:.4f}" if not np.isnan(metrics['R2']) else "N/A "
        mae_str = f"{metrics['MAE']:.4f}" if not np.isnan(metrics['MAE']) else "N/A "
        print(f"{name:<25} | {rmse_str:<10} | {r2_str:<10} | {mae_str:<10}")

    print("\nNOTA: Le metriche (RMSE, MAE) sono calcolate sulla variabile target log-trasformata (log10(price)).")


# --- Visualizzazione Predizioni vs Reale ---
print("\n--- Confronto Grafico Predizioni vs Reale ---")

# Verifica se ci sono predizioni valide da plottare
models_with_preds = [name for name, y_pred in preds.items() if y_pred.size > 0 and not np.isnan(y_pred).all()]

if models_with_preds:
    plt.figure(figsize=(10, 8))

    # Utilizza un campione casuale del test set per i plot scatter se il test set è molto grande
    sample_size = 2000 # Dimensione del campione per il plot
    if X_test.shape[0] > sample_size:
        # Ottieni indici casuali dal test set
        np.random.seed(42) # Per riproducibilità del campionamento
        sample_indices = np.random.choice(X_test.index, size=sample_size, replace=False)
        y_test_sample = y_test.loc[sample_indices]
        print(f"Utilizzando un campione casuale di {sample_size} punti per i plot scatter.")
        is_sampled = True
    else:
        y_test_sample = y_test
        print(f"Utilizzando tutti i {X_test.shape[0]} punti del test set per i plot scatter.")
        is_sampled = False


    # Plotta le predizioni per ciascun modello (usando il campione se applicato)
    colors = plt.cm.get_cmap('tab10', len(models_with_preds)) # Colormap per distinguere i modelli
    color_index = 0
    for name in models_with_preds:
        y_pred = preds[name] # Ottieni le predizioni complete per il modello

        if is_sampled:
            # Se è stato usato un campione per y_test, campiona anche le predizioni corrispondenti
            # Assicurati che le predizioni abbiano lo stesso indice del test set completo prima di campionare
            y_pred_series = pd.Series(y_pred, index=X_test.index)
            y_pred_sample = y_pred_series.loc[sample_indices]
        else:
            y_pred_sample = y_pred # Usa tutte le predizioni se non c'è campionamento

        plt.scatter(y_test_sample, y_pred_sample, alpha=0.6, label=name, s=15, color=colors(color_index)) # s riduce la dimensione punti, alpha per trasparenza
        color_index += 1


    # Disegna la linea ideale y=x (dove le predizioni sono perfette)
    # Trova i limiti comuni per gli assi basandosi su valori reali e predetti validi nel campione/test set
    all_values_list = [y_test_sample.values] + [pd.Series(preds[name], index=X_test.index).loc[y_test_sample.index].values for name in models_with_preds if pd.Series(preds[name], index=X_test.index).loc[y_test_sample.index].size > 0]
    if all_values_list: # Controlla se la lista di array non è vuota
        all_values_sample = np.concatenate(all_values_list)
        min_val = np.min(all_values_sample) * 0.95 # Estendi un po' i limiti
        max_val = np.max(all_values_sample) * 1.05 # Estendi un po' i limiti
        lims = [min_val, max_val]
        plt.plot(lims, lims, 'k--', lw=2, label='Ideale (y=x)') # Linea ideale

        plt.xlabel("Prezzo Reale (log10)")
        plt.ylabel("Prezzo Predetto (log10)")
        plt.title("Prezzi Reali vs Predetti dai Modelli (su scala log10)")
        plt.legend(markerscale=1.5) # markerscale aumenta la dimensione dei marker nella legenda
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.axis('equal') # Imposta gli assi per avere la stessa scala
        plt.show()
    else:
         print("Nessun dato valido per disegnare la linea ideale nel grafico di confronto.")


else:
    print("\nNessuna predizione valida disponibile per generare il grafico di confronto.")


# --- Sezione finale (Modifica di X_test - per coerenza con script originale) ---
# NOTA: Questa sezione modifica il DataFrame X_test DOPO la valutazione dei modelli.
# Questa non è una pratica standard nell'analisi di machine learning, poiché il test set
# dovrebbe rimanere intatto dopo la valutazione per garantire l'imparzialità.
# Se hai bisogno di un DataFrame con le predizioni o i prezzi originali, è meglio
# creare un nuovo DataFrame o Serie separatamente.
print("\n--- Modifica del DataFrame X_test (per coerenza con script originale) ---")
if not X_test.empty:
    # Trasforma y_test (log10) di nuovo nella scala originale (price)
    # Assicurati che y_test sia una Series o DataFrame per usare .copy() e .loc
    y_test_original_scale = 10**y_test.copy() # Usa .copy() per evitare SettingWithCopyWarning

    # Assicurati che gli indici di X_test e y_test_original_scale siano allineati (lo sono dallo split)
    X_test['Price'] = y_test_original_scale
    print("Colonna 'Price' (prezzo originale) aggiunta a X_test.")
    print("Head di X_test modificato:")
    print(X_test.head())
else:
    print("X_test è vuoto. Saltando la modifica.")


print("\n========== Fine Esecuzione Script ==========")