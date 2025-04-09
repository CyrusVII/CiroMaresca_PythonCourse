import random

# Funzione per generare numeri casuali
def random_number():
  return [random.randint(1, 100) for _ in range(5)]

# Funzione per scrivere i numeri in un file di testo
def write_txt():
  with open('csvFolder/numeri_casuali.txt', 'w') as f:
      f.write(",".join(map(str, random_number())))
  print("File numeri_casuali.txt scritto con successo.")

# Funzione per leggere i numeri dal file di testo
def read_text():
  with open("csvFolder/numeri_casuali.txt", 'r', encoding='utf-8') as f:
    lines = f.read() 
  number = lines.strip().split(',')
  return [int(num) for num in number if num.strip() != ''] 

# Funzione principale per il gioco
def main():
  print("\nCerca di indovinare uno dei numeri generati (tra 1 e 100)!")
  random_number = read_text()
  #print(f"Numeri generati: {numeri_casuali}")  
    
  # Loop per tentativi
  while True:
    try:
      guess = int(input("Inserisci il tuo tentativo o premi una lettera per uscire ---> "))
      
      # Controlla se il numero è uno di quelli generati
      if guess in random_number:
        print(f"Congratulazioni! Hai indovinato il numero {guess}!")
        break
      else:
        print("Numero errato, riprova!")
        
    except ValueError:
      print("Hai abbandonato....")
      break
    except:
      print("input non valido")
      
  print(f"I numeri erano {random_number}")

write_txt()
main()

