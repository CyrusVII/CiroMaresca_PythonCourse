from sklearn.preprocessing import LabelEncoder

# Dati di esempio: etichette categoriche
etichette = ['rosso', 'blu', 'verde', 'blu', 'rosso', 'verde']

# Creazione dell'oggetto LabelEncoder
encoder = LabelEncoder()

# Adattamento e trasformazione delle etichette
etichette_numeriche = encoder.fit_transform(etichette)

# Per ritrasformare, utilizziamo le etichette numeriche
ritorno = encoder.inverse_transform(etichette_numeriche)

print("Etichette numeriche:", etichette_numeriche)
print("Ritorno alle etichette originali:", ritorno)
