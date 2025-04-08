import re
#funzione per creare il dizionario
from collections import Counter
def map_creation(st):
    words = st.split()  # Dividi la stringa in parole
    word_count = Counter(words)  # Conta le occorrenze di ogni parola
    return word_count
  
#funziona validazione duplicati
def calcolate_duplicate(words):
  print(f"\n--- Calcolo duplicati --- ") 
  for key,val in words.items():
    print(f"La parola {key} ha {val} duplicati e lunga : {len(key)}") if val > 1 else print(f"La parola {key} non a duplicati")

#funzione calcolo lungezza parola
def calcolate_length(words):
  print(f"\n--- Calcolo length --- ") 
  for key in words.keys():
    print(f"La parola {key} e lunga {len(key)}")

#funzione main
def main():
    st = re.sub(r'[^a-zA-Z0-9 ]', ' ', input("Inserisci la frase ---> ")).lower().strip() 
    words = map_creation(st)
    if words:
      calcolate_duplicate(words)
      calcolate_length(words)

# Esegui il programma
main()

