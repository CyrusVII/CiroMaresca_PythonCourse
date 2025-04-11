import json
# Stringa JSON corretta (usa doppi apici)
fileJson = '{"nome" : "Tommaso", "cognome" : "muraca"}'
# Converte la stringa JSON in un dizionario Python
dizionario = json.loads(fileJson)
# Stampa il dizionario risultante
print(dizionario["nome"])
#lo riconvertiamo in json
jsonMio = json.dumps(dizionario)
print(type(jsonMio))

#facciamo ua request
import requests
url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,rain&timezone=Europe%2FBerlin"
respone = requests.get(url)
print(respone.json())
dizionario = respone.json()
rain = dizionario["hourly"]["rain"]
print("latidudine", dizionario["latitude"] , "piogia: ",rain[:5])