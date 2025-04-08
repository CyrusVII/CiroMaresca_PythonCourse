def cript():
  st,key = stInput()
  cripted = ''
  for i in st:
    if i.islower():
      #Questo calcolo effettua lo spostamento della lettera tenendo conto dell'alfabeto, 
      # con il modulo 26 per assicurarsi che, superato 'z' o 'Z', si ricominci da 'a' o 'A'.
      cripted += chr(((ord(i) - ord('a') + key) % 26) + ord('a'))
    elif i.isupper():
      cripted += chr(((ord(i) - ord('A') + key) % 26) + ord('A'))
    elif i.isdigit():
      cripted += chr(((ord(i) - ord('0') + key) % 10) + ord('0'))
    else:
      cripted += i
  return cripted

def deco():
  st,key = stInput()
  cripted = ''
  for i in st:
    if i.islower():
      #Questo calcolo effettua lo spostamento della lettera tenendo conto dell'alfabeto, 
      # con il modulo 26 per assicurarsi che, superato 'z' o 'Z', si ricominci da 'a' o 'A'.
      cripted += chr(((ord(i) - ord('a') - key) % 26) + ord('a'))
    elif i.isupper():
      cripted += chr(((ord(i) - ord('A') - key) % 26) + ord('A'))
    elif i.isdigit():
      cripted += chr(((ord(i) - ord('0') - key) % 10) + ord('0'))
    else:
      cripted += i
  return cripted

def stInput():
  st = input("Inserisci la frase ---> ").strip()
  key = int(input("Inserisci chiave ---> "))
  return st,key

import time
def main():
  while True:
    time.sleep(2)
    ch = int(input("--- Menu --- \n1) Cifrare \n2) Decifrare \n3) Exit \n ---> "))
    match ch:
      case 1:
        print(f"Ecco la tua parola criptata {cript()}")
      case 2:
        print(f"Ecco la tua parola decriptata {deco()}")
      case _:
        print("Selezione non valida arrivederci")
        break

main()