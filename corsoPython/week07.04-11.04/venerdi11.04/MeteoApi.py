import requests
from datetime import datetime, timedelta

def metoo_get(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=it&format=json"
    response = requests.get(url)
    return response.json()

def meteo_get_data(lat, long):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m,precipitation_probability,wind_speed_10m,soil_temperature_0cm,wind_direction_10m&timezone=Europe%2FBerlin"
    response = requests.get(url)
    return response.json()

def day_calcolator(meteo, option):
    day = int(input("Vuoi vedere il meteo tra 1/3/7 giorni ---> "))
    tempi = meteo['hourly']['time']
    temperature = meteo['hourly']['temperature_2m']
    vento = meteo['hourly']['wind_speed_10m']
    precipitazioni = meteo['hourly']['precipitation_probability']
    times = [datetime.fromisoformat(t) for t in tempi]
    
    current_date = datetime.today().date()
    
    # Crea una lista di giorni da oggi fino al numero di giorni selezionato
    days = [current_date + timedelta(days=i) for i in range(0, day)]

    for day in days:
        print(f"\nMeteo per {day}:")
        for i in range(len(times)):
            if times[i].date() == day:
                print(f"Temperatura: {temperature[i]}°C")
                if option == 2:
                    print(f"Velocità del vento: {vento[i]} km/h")
                elif option == 3:
                    print(f"Probabilità di precipitazione: {precipitazioni[i]}%")
                break

def print_data(response):
    if "results" in response and len(response["results"]) > 0:
        result = response["results"][0]
        print(f"Città: {result['name']}")
        print(f"Nazione: {result['country']}")
        print(f"Latitudine: {result['latitude']}")
        print(f"Longitudine: {result['longitude']}")
        meteo = meteo_get_data(result['latitude'], result['longitude'])
        while True:
            try:
              ch = int(input("--- Menu --- \n 1) Meteo \n 2) Velocità del vento: \n 3) Probabilità di precipitazione \n 4) Exit \n ---> "))
              match ch:
                case 1:
                  day_calcolator(meteo, ch)  
                case 2:
                  day_calcolator(meteo, ch)  
                case 3:
                  day_calcolator(meteo, ch)  
                case _:
                  print("Opzione non valida, scegli 1, 2, 3")
                  continue
              if not input("Vuoi continuare? s/n ---> ").lower().strip() == "s":
                break
            except ValueError:
                print("Input non valido")

def main():
    print("--- Il Meteo ---")
    while True:
        while True:
            city = input("Inserisci citta ---> ")
            if not city.isalpha():
                print("Città non valida")
                continue
            break
        respons = metoo_get(city)
        print_data(respons)
        if not input("Vuoi inserire un'altra città? s/n ---> ") == "s":
            break

main()

