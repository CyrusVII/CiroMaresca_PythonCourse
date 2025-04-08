import string 
alfMin = string.ascii_lowercase
alfUp = string.ascii_uppercase
num = list(range(1,11))
def cript():
  st,key = stInput()
  cripted = ''
  for i in st:
    if i.islower():
      new_index = (alfMin.index(i) + key) % 26
      cripted += alfMin[new_index]
    elif i.isupper():
      new_index = (alfUp.index(i) + key) % 26
      cripted += alfUp[new_index]
    elif i.isdigit():
      new_index = (num.index(int(i)) + key) % 10
      cripted += str(num[new_index])
    else:
      cripted += i
  return cripted

def deco():
  st,key = stInput()
  cripted = ''
  for i in st:
    if i.islower():
      new_index = (alfMin.index(i) - key) % 26
      cripted += alfMin[new_index]
    elif i.isupper():
      new_index = (alfUp.index(i) - key) % 26
      cripted += alfUp[new_index]
    elif i.isdigit():
      new_index = (num.index(int(i)) - key) % 10
      cripted += str(num[new_index])
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